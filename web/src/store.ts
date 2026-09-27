// App state (zustand). Chat transcripts are accumulated from the SSE stream (SPEC §3).

import { create } from "zustand"
import { toast } from "sonner"
import { api } from "./api"
import type {
  ChatMessage,
  ChatSummary,
  Health,
  JobProgress,
  MessagePart,
  SSEEvent,
  ToolCallPart,
} from "./types"

export type View = "chat" | "dashboard"

function viewFromHash(): View {
  const h = typeof window !== "undefined" ? window.location.hash : ""
  return h.startsWith("#/dashboard") ? "dashboard" : "chat"
}

// ---------------------------------------------------------------------------

interface AppState {
  view: View
  setView: (v: View) => void

  health: Health | null
  healthError: string | null
  loadHealth: () => Promise<void>

  chats: ChatSummary[]
  chatsLoading: boolean
  loadChats: () => Promise<void>

  activeChatId: string | null
  messages: Record<string, ChatMessage[]>
  transcriptLoading: Record<string, boolean>
  streaming: Record<string, boolean>
  statusLine: Record<string, string | null>
  aborters: Record<string, AbortController>

  openChat: (id: string | null) => Promise<void>
  newChat: () => Promise<string>
  send: (text: string, chatId?: string) => Promise<void>
  stop: (chatId: string) => void
  /** From the dashboard: open Chat and send `scout <title>`. */
  scoutFromDashboard: (title: string) => Promise<void>
}

export const useApp = create<AppState>((set, get) => ({
  view: viewFromHash(),
  setView: (v) => {
    if (typeof window !== "undefined") {
      const target = v === "dashboard" ? "#/dashboard" : "#/chat"
      if (window.location.hash !== target) window.history.pushState(null, "", target)
    }
    set({ view: v })
  },

  health: null,
  healthError: null,
  loadHealth: async () => {
    try {
      const health = await api.health()
      set({ health, healthError: null })
    } catch (e) {
      const msg = e instanceof Error ? e.message : String(e)
      set({ healthError: msg })
    }
  },

  chats: [],
  chatsLoading: false,
  loadChats: async () => {
    set({ chatsLoading: true })
    try {
      const chats = await api.chats()
      set({ chats, chatsLoading: false })
    } catch (e) {
      set({ chatsLoading: false })
      toast.error("Could not load chats", { description: e instanceof Error ? e.message : String(e) })
    }
  },

  activeChatId: null,
  messages: {},
  transcriptLoading: {},
  streaming: {},
  statusLine: {},
  aborters: {},

  openChat: async (id) => {
    set({ activeChatId: id, view: "chat" })
    if (typeof window !== "undefined" && window.location.hash.startsWith("#/dashboard")) {
      window.history.pushState(null, "", "#/chat")
    }
    if (!id) return
    if (get().messages[id] && !get().transcriptLoading[id]) return
    set((s) => ({ transcriptLoading: { ...s.transcriptLoading, [id]: true } }))
    try {
      const t = await api.chat(id)
      const messages = (t.messages || []).map(normaliseMessage)
      set((s) => ({
        messages: { ...s.messages, [id]: messages },
        transcriptLoading: { ...s.transcriptLoading, [id]: false },
      }))
    } catch (e) {
      set((s) => ({ transcriptLoading: { ...s.transcriptLoading, [id]: false } }))
      toast.error("Could not load chat", { description: e instanceof Error ? e.message : String(e) })
    }
  },

  newChat: async () => {
    const { id } = await api.createChat()
    const summary: ChatSummary = { id, title: "New chat", created_at: new Date().toISOString() }
    set((s) => ({
      chats: [summary, ...s.chats],
      activeChatId: id,
      view: "chat",
      messages: { ...s.messages, [id]: [] },
    }))
    return id
  },

  send: async (text, chatIdArg) => {
    const trimmed = text.trim()
    if (!trimmed) return
    let chatId = chatIdArg ?? get().activeChatId
    if (!chatId) chatId = await get().newChat()
    if (get().streaming[chatId]) {
      toast("Still answering", { description: "Wait for the current reply to finish." })
      return
    }

    const userMsg: ChatMessage = {
      id: `u_${Date.now()}`,
      role: "user",
      parts: [{ kind: "text", text: trimmed }],
      created_at: new Date().toISOString(),
    }
    const assistantId = `a_${Date.now()}`
    const assistant: ChatMessage = { id: assistantId, role: "assistant", parts: [] }
    const aborter = new AbortController()

    set((s) => ({
      messages: { ...s.messages, [chatId!]: [...(s.messages[chatId!] || []), userMsg, assistant] },
      streaming: { ...s.streaming, [chatId!]: true },
      statusLine: { ...s.statusLine, [chatId!]: null },
      aborters: { ...s.aborters, [chatId!]: aborter },
      chats: s.chats.map((c) =>
        c.id === chatId && (c.title === "New chat" || !c.title) ? { ...c, title: trimmed.slice(0, 60) } : c,
      ),
    }))

    const patch = (fn: (m: ChatMessage) => ChatMessage) => {
      set((s) => ({
        messages: {
          ...s.messages,
          [chatId!]: (s.messages[chatId!] || []).map((m) => (m.id === assistantId ? fn(m) : m)),
        },
      }))
    }

    try {
      for await (const ev of api.sendMessage(chatId, trimmed, aborter.signal)) {
        applyEvent(ev, patch, (line) =>
          set((s) => ({ statusLine: { ...s.statusLine, [chatId!]: line } })),
        )
      }
    } catch (e) {
      if (!aborter.signal.aborted) {
        const msg = e instanceof Error ? e.message : String(e)
        patch((m) => ({ ...m, error: msg }))
        toast.error("Message failed", { description: msg })
      }
    } finally {
      // Any tool still pending when the stream closes is unresolved, not done.
      patch((m) => ({
        ...m,
        parts: m.parts.map((p) =>
          p.kind === "tool" && p.status === "pending" ? { ...p, status: "error", summary: p.summary || "Interrupted" } : p,
        ),
      }))
      set((s) => {
        const { [chatId!]: _gone, ...aborters } = s.aborters
        return {
          streaming: { ...s.streaming, [chatId!]: false },
          statusLine: { ...s.statusLine, [chatId!]: null },
          aborters,
        }
      })
    }
  },

  stop: (chatId) => {
    get().aborters[chatId]?.abort()
  },

  scoutFromDashboard: async (title) => {
    const id = await get().newChat()
    get().setView("chat")
    await get().send(`scout ${title}`, id)
  },
}))

// ---------------------------------------------------------------------------

function applyEvent(
  ev: SSEEvent,
  patch: (fn: (m: ChatMessage) => ChatMessage) => void,
  setStatus: (line: string | null) => void,
) {
  switch (ev.type) {
    case "message_start":
      patch((m) => ({ ...m, id: m.id, created_at: new Date().toISOString() }))
      break
    case "text_delta": {
      const text = ev.data?.text ?? ""
      if (!text) break
      setStatus(null)
      patch((m) => {
        const parts = m.parts.slice()
        const last = parts[parts.length - 1]
        if (last && last.kind === "text") parts[parts.length - 1] = { kind: "text", text: last.text + text }
        else parts.push({ kind: "text", text })
        return { ...m, parts }
      })
      break
    }
    case "thinking": {
      const text = ev.data?.text ?? ""
      setStatus(text || null)
      if (text) patch((m) => ({ ...m, parts: [...m.parts, { kind: "thinking", text }] }))
      break
    }
    case "tool_call": {
      const part: ToolCallPart = {
        kind: "tool",
        id: ev.data.id,
        name: ev.data.name,
        input: ev.data.input || {},
        status: "pending",
      }
      setStatus(null)
      patch((m) => ({ ...m, parts: [...m.parts, part] }))
      break
    }
    case "tool_result": {
      const d = ev.data
      patch((m) => {
        let found = false
        const parts = m.parts.map((p) => {
          if (p.kind === "tool" && p.id === d.id) {
            found = true
            return { ...p, status: d.ok ? "ok" : "error", summary: d.summary, data: d.data } as ToolCallPart
          }
          return p
        })
        if (!found) {
          parts.push({ kind: "tool", id: d.id, name: d.name, input: {}, status: d.ok ? "ok" : "error", summary: d.summary, data: d.data })
        }
        return { ...m, parts }
      })
      break
    }
    case "job_progress": {
      const jp: JobProgress = ev.data
      patch((m) => {
        const parts = m.parts.slice()
        let idx = parts.findIndex((p) => p.kind === "tool" && p.id === jp.job_id)
        if (idx === -1) {
          for (let i = parts.length - 1; i >= 0; i--) {
            const p = parts[i]
            if (p.kind === "tool" && p.status === "pending") {
              idx = i
              break
            }
          }
        }
        if (idx !== -1) parts[idx] = { ...(parts[idx] as ToolCallPart), progress: jp }
        return { ...m, parts }
      })
      break
    }
    case "error":
      patch((m) => ({ ...m, error: ev.data?.message || "Unknown error" }))
      toast.error("Agent error", { description: ev.data?.message })
      break
    case "message_end":
      patch((m) => ({ ...m, usage: ev.data?.usage }))
      setStatus(null)
      break
    default:
      break
  }
}

/** Accept a few transcript shapes so a persisted chat renders even if the server stores `text` or `content`. */
function normaliseMessage(raw: unknown): ChatMessage {
  const r = (raw || {}) as Record<string, unknown>
  const role = r.role === "user" ? "user" : "assistant"
  let parts: MessagePart[] = []
  if (Array.isArray(r.parts)) {
    parts = (r.parts as Record<string, unknown>[]).map((p): MessagePart => {
      const kind = (p.kind || p.type) as string
      if (kind === "tool" || kind === "tool_call" || kind === "tool_result") {
        return {
          kind: "tool",
          id: String(p.id ?? ""),
          name: String(p.name ?? ""),
          input: (p.input as Record<string, unknown>) || {},
          status: (p.status as ToolCallPart["status"]) || (p.ok === false ? "error" : "ok"),
          summary: p.summary as string | undefined,
          data: p.data,
        }
      }
      if (kind === "thinking") return { kind: "thinking", text: String(p.text ?? "") }
      return { kind: "text", text: String(p.text ?? p.content ?? "") }
    })
  } else {
    // The engine persists {text, tool_calls:[{id,name,input,result:{ok,summary,data}}]}:
    // tool cards first (they happened before the prose), then the text.
    const calls = Array.isArray(r.tool_calls) ? (r.tool_calls as Record<string, unknown>[]) : []
    parts = calls.map((c): MessagePart => {
      const res = (c.result as Record<string, unknown>) || {}
      return {
        kind: "tool",
        id: String(c.id ?? ""),
        name: String(c.name ?? ""),
        input: (c.input as Record<string, unknown>) || {},
        status: res.ok === false ? "error" : "ok",
        summary: res.summary as string | undefined,
        data: res.data,
      }
    })
    const text = String(r.text ?? r.content ?? "")
    if (text) parts.push({ kind: "text", text })
  }
  return {
    id: String(r.id ?? `${role}_${Math.random().toString(36).slice(2, 8)}`),
    role,
    parts,
    created_at: r.created_at as string | undefined,
    usage: r.usage as ChatMessage["usage"],
    error: r.error as string | undefined,
  }
}

// Keep `view` in sync with back/forward navigation.
if (typeof window !== "undefined") {
  window.addEventListener("popstate", () => useApp.setState({ view: viewFromHash() }))
}
