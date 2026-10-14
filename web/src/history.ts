export interface ImportedNoteSummary {
  id: string
  source: "kakao" | "slack" | "codex" | "claude" | "codex-history" | "claude-history" | "codex-result" | "claude-result"
  occurred_at: string
  title: string
  excerpt: string
  kind: "note" | "idea" | "action" | "study" | "link" | "result"
  urls: string[]
  source_url: string
  project_key: string
  sensitive: number
  partial: number
  linked_type: string
  linked_id: string
}

export interface ImportedNote extends Omit<ImportedNoteSummary, "excerpt"> {
  source_id: string
  body: string
  session_path: string
}

export interface ImportPage {
  total: number
  items: ImportedNoteSummary[]
  limit: number
  offset: number
}

export interface ImportStats {
  total: number
  personal_total: number
  history_total: number
  agent_total: number
  personal_links: number
  sources: Record<string, number>
  kinds: Record<string, number>
  with_links: number
  partial: number
}

async function request<T>(path: string, init?: RequestInit): Promise<T> {
  const response = await fetch(`/api/workspace/imports${path}`, init)
  if (!response.ok) {
    const body = await response.json().catch(() => ({})) as { error?: string }
    throw new Error(body.error || `${response.status} ${response.statusText}`)
  }
  return response.json() as Promise<T>
}

export const historyApi = {
  stats: () => request<ImportStats>("/stats"),
  search: (filters: { q: string; source: string; kind: string; scope: string; offset: number }) =>
    request<ImportPage>(`?${new URLSearchParams({ ...filters, offset: String(filters.offset), limit: "40" })}`),
  get: (id: string) => request<ImportedNote>(`/${id}`),
  link: (id: string, linked_type: string, linked_id: string) =>
    request<ImportedNote>(`/${id}/link`, { method: "PATCH", headers: { "content-type": "application/json" }, body: JSON.stringify({ linked_type, linked_id }) }),
}
