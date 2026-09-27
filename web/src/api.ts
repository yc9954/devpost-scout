// Data layer — SPEC.md §3. Plain fetch for JSON; fetch + ReadableStream for SSE.
// With `?mock=1` in the URL, every call is answered by src/mock.ts instead.

import type {
  ChatSummary,
  ChatTranscript,
  Hackathon,
  HackathonDetail,
  Health,
  JobProgress,
  SSEEvent,
  Stats,
  Winner,
} from "./types"
import * as mock from "./mock"

export const isMock = (): boolean => {
  if (typeof window === "undefined") return false
  return new URLSearchParams(window.location.search).get("mock") === "1"
}

export class ApiError extends Error {
  status: number
  constructor(status: number, message: string) {
    super(message)
    this.status = status
  }
}

async function json<T>(input: string, init?: RequestInit): Promise<T> {
  const res = await fetch(input, {
    ...init,
    headers: { "content-type": "application/json", ...(init?.headers || {}) },
  })
  if (!res.ok) {
    let msg = `${res.status} ${res.statusText}`
    try {
      const body = await res.json()
      if (body && typeof body.error === "string") msg = body.error
      else if (body && typeof body.message === "string") msg = body.message
    } catch {
      /* body not JSON */
    }
    throw new ApiError(res.status, msg)
  }
  return (await res.json()) as T
}

// ---------------------------------------------------------------------------
// SSE parser (fetch + ReadableStream). Yields one SSEEvent per `event:`/`data:`
// block. Tolerates CRLF, comments, multi-line data, and a missing `event:`.
// ---------------------------------------------------------------------------

export async function* parseSSE(
  body: ReadableStream<Uint8Array>,
  signal?: AbortSignal,
): AsyncGenerator<SSEEvent> {
  const reader = body.getReader()
  const decoder = new TextDecoder()
  let buffer = ""
  const onAbort = () => {
    reader.cancel().catch(() => {})
  }
  signal?.addEventListener("abort", onAbort)
  try {
    while (true) {
      const { value, done } = await reader.read()
      if (done) break
      buffer += decoder.decode(value, { stream: true })
      buffer = buffer.replace(/\r\n/g, "\n")
      let idx: number
      while ((idx = buffer.indexOf("\n\n")) !== -1) {
        const block = buffer.slice(0, idx)
        buffer = buffer.slice(idx + 2)
        const ev = parseBlock(block)
        if (ev) yield ev
      }
    }
    if (buffer.trim()) {
      const ev = parseBlock(buffer)
      if (ev) yield ev
    }
  } finally {
    signal?.removeEventListener("abort", onAbort)
    reader.releaseLock()
  }
}

function parseBlock(block: string): SSEEvent | null {
  let event = "message"
  const dataLines: string[] = []
  for (const raw of block.split("\n")) {
    if (!raw || raw.startsWith(":")) continue
    const colon = raw.indexOf(":")
    const field = colon === -1 ? raw : raw.slice(0, colon)
    let value = colon === -1 ? "" : raw.slice(colon + 1)
    if (value.startsWith(" ")) value = value.slice(1)
    if (field === "event") event = value
    else if (field === "data") dataLines.push(value)
  }
  if (dataLines.length === 0) return null
  const text = dataLines.join("\n")
  let data: unknown = text
  try {
    data = JSON.parse(text)
  } catch {
    /* keep raw text */
  }
  // If the server omitted `event:` but put a type inside the JSON, honour it.
  if (event === "message" && data && typeof data === "object" && "type" in (data as object)) {
    const d = data as { type: string; data?: unknown }
    return { type: d.type, data: d.data ?? d } as SSEEvent
  }
  return { type: event, data } as SSEEvent
}

// ---------------------------------------------------------------------------
// Endpoints
// ---------------------------------------------------------------------------

export interface HackathonQuery {
  status?: "open" | "upcoming" | "ended" | "all"
  q?: string
  theme?: string
  sort?: "deadline" | "prize" | "registrations"
  limit?: number
}

function qs(params: Record<string, string | number | undefined>): string {
  const u = new URLSearchParams()
  for (const [k, v] of Object.entries(params)) {
    if (v !== undefined && v !== "" && v !== null) u.set(k, String(v))
  }
  const s = u.toString()
  return s ? `?${s}` : ""
}

export const api = {
  health(): Promise<Health> {
    if (isMock()) return mock.health()
    return json<Health>("/api/health")
  },

  hackathons(query: HackathonQuery = {}): Promise<Hackathon[]> {
    if (isMock()) return mock.hackathons(query)
    return json<Hackathon[] | { rows: Hackathon[] }>(`/api/hackathons${qs({ ...query })}`).then((r) =>
      Array.isArray(r) ? r : r.rows,
    )
  },

  hackathon(id: string | number): Promise<HackathonDetail> {
    if (isMock()) return mock.hackathon(id)
    return json<HackathonDetail>(`/api/hackathons/${encodeURIComponent(String(id))}`)
  },

  stats(): Promise<Stats> {
    if (isMock()) return mock.stats()
    return json<Stats>("/api/stats")
  },

  winners(q: string, limit = 20): Promise<Winner[]> {
    if (isMock()) return mock.winners(q, limit)
    return json<Winner[] | { rows: Winner[] }>(`/api/winners${qs({ q, limit })}`).then((r) =>
      Array.isArray(r) ? r : r.rows,
    )
  },

  chats(): Promise<ChatSummary[]> {
    if (isMock()) return mock.chats()
    return json<ChatSummary[] | { chats: ChatSummary[] }>("/api/chats").then((r) =>
      Array.isArray(r) ? r : r.chats,
    )
  },

  chat(id: string): Promise<ChatTranscript> {
    if (isMock()) return mock.chat(id)
    return json<ChatTranscript>(`/api/chats/${encodeURIComponent(id)}`)
  },

  createChat(title?: string): Promise<{ id: string }> {
    if (isMock()) return mock.createChat(title)
    return json<{ id: string }>("/api/chats", {
      method: "POST",
      body: JSON.stringify(title ? { title } : {}),
    })
  },

  /** POST /api/chats/{id}/messages — streams SSE events (SPEC §3). */
  async *sendMessage(chatId: string, text: string, signal?: AbortSignal): AsyncGenerator<SSEEvent> {
    if (isMock()) {
      yield* mock.sendMessage(chatId, text, signal)
      return
    }
    const res = await fetch(`/api/chats/${encodeURIComponent(chatId)}/messages`, {
      method: "POST",
      headers: { "content-type": "application/json", accept: "text/event-stream" },
      body: JSON.stringify({ text }),
      signal,
    })
    if (!res.ok || !res.body) {
      throw new ApiError(res.status, `Message failed: ${res.status} ${res.statusText}`)
    }
    yield* parseSSE(res.body, signal)
  },

  startScoutJob(hackathon: string): Promise<{ job_id: string }> {
    if (isMock()) return mock.startJob("scout")
    return json<{ job_id: string }>("/api/jobs/scout", {
      method: "POST",
      body: JSON.stringify({ hackathon }),
    })
  },

  refreshCensus(): Promise<{ job_id: string }> {
    if (isMock()) return mock.startJob("refresh")
    return json<{ job_id: string }>("/api/jobs/refresh", { method: "POST", body: "{}" })
  },

  /** GET /api/jobs/{id}/stream — SSE of job_progress events. */
  async *jobStream(jobId: string, signal?: AbortSignal): AsyncGenerator<JobProgress> {
    if (isMock()) {
      yield* mock.jobStream(jobId, signal)
      return
    }
    const res = await fetch(`/api/jobs/${encodeURIComponent(jobId)}/stream`, {
      headers: { accept: "text/event-stream" },
      signal,
    })
    if (!res.ok || !res.body) throw new ApiError(res.status, `Job stream failed: ${res.status}`)
    for await (const ev of parseSSE(res.body, signal)) {
      if (ev.type === "job_progress") yield ev.data
      else if (ev.type === "error") throw new Error((ev.data as { message: string }).message)
      else if (ev.type === "done" || ev.type === "message_end") return
    }
  },
}
