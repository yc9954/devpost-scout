// Payload types — SPEC.md §5 (card payloads) and §3 (API / SSE).

export type HackathonStatus = "open" | "upcoming" | "ended"

export interface Hackathon {
  id: number | string
  title: string
  url: string
  host: string
  org: string
  status: HackathonStatus
  census_state: string
  dates: string
  start?: string
  end?: string
  days_left?: number
  themes: string[]
  prize_usd: number
  prize_display: string
  prizes_counts: number
  registrations: number
  thumbnail: string
  featured: boolean
  winners_announced: boolean
  gallery_url: string
  location: string
}

export interface BriefCriterion {
  label: string
  text: string
  weight?: number
}

export interface Brief {
  title: string
  host: string
  url: string
  criteria: BriefCriterion[]
  weighting: "equal" | "weighted" | "unknown"
  tiebreak_criterion: string
  requirements: string[]
  prizes: { name: string; amount?: string | number }[]
  dates: string
  criteria_source: string | null
}

export interface Winner {
  slug: string
  title: string
  tagline: string
  host: string
  hackathon_title: string
  url: string
  is_winner: boolean
}

export interface Project {
  slug: string
  title: string
  tagline: string
  url: string
  is_winner: boolean
  members?: string[]
}

export interface IdeaEvidence {
  slug: string
  title: string
  host: string
}

export interface Idea {
  title: string
  mechanism: string
  domain: string
  user: string
  substrate: string
  expected_wins: number
  evidence: IdeaEvidence[]
  why: string
  risk: string
}

export interface VaultNote {
  title: string
  path: string
  excerpt: string
}

// ---- tool result payloads (SPEC §4 "returns (data)") ----

export interface ListHackathonsData {
  rows: Hackathon[]
  total: number
}
export interface SearchWinnersData {
  rows: Winner[]
}
export interface FieldData {
  rows: Project[]
  total: number
  source: string
}
export interface IdeateData {
  candidates: Idea[]
}
export interface VaultLookupData {
  notes: VaultNote[]
}
export interface ScoutData {
  brief?: Brief
  field?: FieldData
  ideas?: IdeateData | Idea[]
}

export type ToolName =
  | "list_hackathons"
  | "hackathon_brief"
  | "search_winners"
  | "field"
  | "ideate"
  | "vault_lookup"
  | "census_stats"
  | "scout"

// ---- API responses ----

export interface Counts {
  open: number
  upcoming: number
  ended: number
  total: number
}

export interface Health {
  ok: boolean
  mode: "claude" | "local"
  model: string
  census_date: string
  counts: Counts
}

export interface Stats {
  counts: Counts
  prize_total_open: number
  themes: { name: string; count: number }[]
  top_orgs: { name: string; count: number }[]
  deadlines_next_14d: Hackathon[]
}

export interface HackathonDetail extends Hackathon {
  brief?: Brief | null
}

export interface ChatSummary {
  id: string
  title: string
  created_at?: string
  updated_at?: string
}

export interface ToolCallPart {
  kind: "tool"
  id: string
  name: string
  input: Record<string, unknown>
  status: "pending" | "ok" | "error"
  summary?: string
  data?: unknown
  progress?: JobProgress
}

export interface TextPart {
  kind: "text"
  text: string
}

export interface ThinkingPart {
  kind: "thinking"
  text: string
}

export type MessagePart = TextPart | ToolCallPart | ThinkingPart

export interface ChatMessage {
  id: string
  role: "user" | "assistant"
  parts: MessagePart[]
  created_at?: string
  usage?: Usage
  error?: string
}

export interface ChatTranscript extends ChatSummary {
  messages: ChatMessage[]
}

export interface Usage {
  input_tokens?: number
  output_tokens?: number
  total_tokens?: number
  duration_ms?: number
  model?: string
}

export interface JobProgress {
  job_id: string
  step: string
  pct: number
  note?: string
}

// ---- SSE events (SPEC §3) ----

export type SSEEvent =
  | { type: "message_start"; data: { chat_id: string; message_id: string; mode: "claude" | "local" } }
  | { type: "text_delta"; data: { text: string } }
  | { type: "thinking"; data: { text: string } }
  | { type: "tool_call"; data: { id: string; name: string; input: Record<string, unknown> } }
  | { type: "tool_result"; data: { id: string; name: string; ok: boolean; summary: string; data: unknown } }
  | { type: "job_progress"; data: JobProgress }
  | { type: "error"; data: { message: string } }
  | { type: "message_end"; data: { usage?: Usage } }
  | { type: "done"; data: unknown }
