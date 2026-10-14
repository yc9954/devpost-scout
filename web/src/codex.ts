import { parseSSE } from "./api"

export interface CodexStatus { ready: boolean; message: string }
export interface CodexChatSummary { id: string; title: string; created_at: string; updated_at: string }
export interface CodexMessage { id: string; role: "user" | "assistant" | "error"; text: string; created_at: string }
export interface CodexChat extends CodexChatSummary { codex_thread_id: string | null; messages: CodexMessage[] }
export interface WritingRequest {
  mode: "continue" | "rewrite" | "outline" | "custom"
  before: string
  selected: string
  after: string
  instruction: string
  title: string
}

async function request<T>(path: string, init?: RequestInit): Promise<T> {
  const response = await fetch(`/api/codex/${path}`, { ...init, headers: { "content-type": "application/json" } })
  if (!response.ok) {
    let message = `${response.status} ${response.statusText}`
    try { message = (await response.json() as { error?: string }).error || message } catch { /* no JSON */ }
    throw new Error(message)
  }
  return response.json() as Promise<T>
}

export const codexApi = {
  status: () => request<CodexStatus>("status"),
  chats: () => request<CodexChatSummary[]>("chats"),
  chat: (id: string) => request<CodexChat>(`chats/${id}`),
  create: () => request<CodexChatSummary>("chats", { method: "POST", body: "{}" }),
  remove: (id: string) => request<{ ok: true }>(`chats/${id}`, { method: "DELETE" }),
  async *complete(input: WritingRequest, signal?: AbortSignal): AsyncGenerator<{ type: string; data: unknown }> {
    const response = await fetch("/api/codex/complete", {
      method: "POST", headers: { "content-type": "application/json", accept: "text/event-stream" },
      body: JSON.stringify(input), signal,
    })
    if (!response.ok || !response.body) {
      let message = `${response.status} ${response.statusText}`
      try { message = (await response.json() as { error?: string }).error || message } catch { /* no JSON */ }
      throw new Error(message)
    }
    yield* parseSSE(response.body, signal)
  },
  async *send(id: string, text: string): AsyncGenerator<{ type: string; data: unknown }> {
    const response = await fetch(`/api/codex/chats/${id}/messages`, {
      method: "POST", headers: { "content-type": "application/json", accept: "text/event-stream" },
      body: JSON.stringify({ text }),
    })
    if (!response.ok || !response.body) {
      let message = `${response.status} ${response.statusText}`
      try { message = (await response.json() as { error?: string }).error || message } catch { /* no JSON */ }
      throw new Error(message)
    }
    yield* parseSSE(response.body)
  },
}
