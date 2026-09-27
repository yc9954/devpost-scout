// Mock backend for developing without `python3 -m scout`. Enabled with `?mock=1`.
// Shapes follow SPEC.md §3 / §5 exactly so every card type renders.

import type {
  Brief,
  ChatSummary,
  ChatTranscript,
  Hackathon,
  HackathonDetail,
  Health,
  Idea,
  JobProgress,
  SSEEvent,
  Stats,
  VaultNote,
  Winner,
} from "./types"
import type { HackathonQuery } from "./api"

const CENSUS_DATE = "2026-09-06"
const TODAY = new Date()

function daysUntil(iso: string): number {
  const end = new Date(iso + "T23:59:59")
  return Math.ceil((end.getTime() - TODAY.getTime()) / 86_400_000)
}

function statusFor(start: string, end: string): Hackathon["status"] {
  const s = new Date(start + "T00:00:00").getTime()
  const e = new Date(end + "T23:59:59").getTime()
  const now = TODAY.getTime()
  if (now < s) return "upcoming"
  if (now > e) return "ended"
  return "open"
}

function row(
  h: Omit<Hackathon, "status" | "days_left" | "census_state" | "prize_display" | "host" | "url" | "gallery_url"> & {
    start: string
    end: string
    host: string
  },
): Hackathon {
  const status = statusFor(h.start, h.end)
  return {
    ...h,
    status,
    census_state: status,
    days_left: status === "ended" ? undefined : daysUntil(status === "upcoming" ? h.start : h.end),
    prize_display: `$${h.prize_usd.toLocaleString("en-US")}`,
    url: `https://${h.host}.devpost.com/`,
    gallery_url: `https://${h.host}.devpost.com/project-gallery`,
  }
}

export const HACKATHONS: Hackathon[] = [
  row({
    id: 24101,
    title: "RevenueCat Shipaton 2026",
    host: "revenuecat-shipaton-2026",
    org: "RevenueCat",
    dates: "Jul 31 - Oct 01, 2026",
    start: "2026-07-31",
    end: "2026-10-01",
    themes: ["Design", "Gaming", "Mobile"],
    prize_usd: 740000,
    prizes_counts: 42,
    registrations: 23594,
    thumbnail: "https://d112y698adiu2z.cloudfront.net/photos/production/challenge_thumbnails/003/612/812/datas/medium_square.png",
    featured: true,
    winners_announced: false,
    location: "Online",
  }),
  row({
    id: 24230,
    title: "Gemini Live Agent Challenge",
    host: "gemini-live-agent",
    org: "Google",
    dates: "Sep 09 - Oct 06, 2026",
    start: "2026-09-09",
    end: "2026-10-06",
    themes: ["Machine Learning/AI", "Voice", "Productivity"],
    prize_usd: 150000,
    prizes_counts: 12,
    registrations: 8112,
    thumbnail: "https://d112y698adiu2z.cloudfront.net/photos/production/challenge_thumbnails/003/641/002/datas/medium_square.png",
    featured: true,
    winners_announced: false,
    location: "Online",
  }),
  row({
    id: 24377,
    title: "Health × Voice Build Week",
    host: "health-voice-build-week",
    org: "Vapi",
    dates: "Sep 22 - Sep 29, 2026",
    start: "2026-09-22",
    end: "2026-09-29",
    themes: ["Health", "Voice", "Accessibility"],
    prize_usd: 25000,
    prizes_counts: 5,
    registrations: 1204,
    thumbnail: "",
    featured: false,
    winners_announced: false,
    location: "Online",
  }),
  row({
    id: 24510,
    title: "MCP Agents Hackathon: Fall 2026",
    host: "mcp-agents-fall-2026",
    org: "Anthropic Developer Community",
    dates: "Oct 10 - Nov 14, 2026",
    start: "2026-10-10",
    end: "2026-11-14",
    themes: ["Machine Learning/AI", "DevOps", "Open Ended"],
    prize_usd: 60000,
    prizes_counts: 9,
    registrations: 3411,
    thumbnail: "",
    featured: false,
    winners_announced: false,
    location: "Online",
  }),
  row({
    id: 24555,
    title: "Global Fintech Hack 2026",
    host: "global-fintech-hack-2026",
    org: "Stripe",
    dates: "Nov 02 - Dec 05, 2026",
    start: "2026-11-02",
    end: "2026-12-05",
    themes: ["Fintech", "Web", "Enterprise"],
    prize_usd: 120000,
    prizes_counts: 8,
    registrations: 902,
    thumbnail: "",
    featured: false,
    winners_announced: false,
    location: "San Francisco, CA + Online",
  }),
  row({
    id: 23988,
    title: "WebMCP Hackathon",
    host: "webmcp",
    org: "Google Chrome",
    dates: "Aug 05 - Sep 12, 2026",
    start: "2026-08-05",
    end: "2026-09-12",
    themes: ["Web", "Machine Learning/AI", "Productivity"],
    prize_usd: 100000,
    prizes_counts: 15,
    registrations: 12400,
    thumbnail: "",
    featured: false,
    winners_announced: true,
    location: "Online",
  }),
]

export const BRIEF: Brief = {
  title: "RevenueCat Shipaton 2026",
  host: "revenuecat-shipaton-2026",
  url: "https://revenuecat-shipaton-2026.devpost.com/",
  dates: "Jul 31 - Oct 01, 2026",
  weighting: "weighted",
  criteria_source: "https://revenuecat-shipaton-2026.devpost.com/rules",
  tiebreak_criterion: "Quality of the Idea",
  criteria: [
    { label: "Quality of the Idea", text: "Includes creativity and originality of the idea, and the app's potential to become a real business.", weight: 30 },
    { label: "Implementation", text: "How well was the idea executed? Does the app ship the core loop, and does the RevenueCat SDK integration work end to end?", weight: 25 },
    { label: "Design", text: "Is the user experience polished and intentional? Does the paywall feel native to the app?", weight: 20 },
    { label: "Traction", text: "Evidence of real users: downloads, trials started, and paying customers measured through RevenueCat.", weight: 15 },
    { label: "Presentation", text: "The demo video and written description clearly explain what was built and why.", weight: 10 },
  ],
  requirements: [
    "New app published to the App Store or Google Play during the submission period",
    "Integrates the RevenueCat SDK with at least one purchasable product",
    "Demo video of 3 minutes or less",
    "Public URL to the app store listing",
    "Written description of the app and how RevenueCat was used",
  ],
  prizes: [
    { name: "Grand Prize", amount: "$100,000" },
    { name: "Best Design", amount: "$25,000" },
    { name: "Best Game", amount: "$25,000" },
    { name: "#BuildInPublic Award", amount: "$10,000" },
    { name: "Peace Prize (community vote)", amount: "$5,000" },
  ],
}

export const WINNERS: Winner[] = [
  { slug: "seeing-ai-companion", title: "Seeing AI Companion", tagline: "A voice agent that narrates what your camera sees and answers follow-up questions hands-free.", host: "gemini-live-agent-2025", hackathon_title: "Gemini Live Agent Challenge 2025", url: "https://devpost.com/software/seeing-ai-companion", is_winner: true },
  { slug: "signbridge", title: "SignBridge", tagline: "Real-time sign-language to speech for video calls, built as an MCP tool any agent can call.", host: "mcp-agents-spring-2026", hackathon_title: "MCP Agents Hackathon: Spring 2026", url: "https://devpost.com/software/signbridge", is_winner: true },
  { slug: "countersign-vmy83b", title: "Countersign", tagline: "Screen reader agent that fills forms by reading the page's own ARIA tree, never guessing.", host: "webmcp", hackathon_title: "WebMCP Hackathon", url: "https://devpost.com/software/countersign-vmy83b", is_winner: true },
  { slug: "loudly", title: "Loudly", tagline: "Turns any PDF into an interactive audio lesson for low-vision students.", host: "accessibility-hack-2025", hackathon_title: "Accessibility Hackathon 2025", url: "https://devpost.com/software/loudly", is_winner: true },
]

export const IDEAS: Idea[] = [
  {
    title: "Paywall coach for indie apps",
    mechanism: "agent-in-the-loop",
    domain: "monetization",
    user: "indie mobile developers",
    substrate: "mobile app + RevenueCat SDK",
    expected_wins: 3.4,
    evidence: [
      { slug: "paywall-lab", title: "Paywall Lab", host: "revenuecat-shipaton-2025" },
      { slug: "subly", title: "Subly", host: "revenuecat-shipaton-2025" },
      { slug: "trial-tuner", title: "Trial Tuner", host: "mobile-monetization-2025" },
    ],
    why: "Mechanism (agent-in-the-loop) won 11 times in the corpus; domain (monetization) is the host's own product — every prior Shipaton grand prize integrated RevenueCat analytics visibly.",
    risk: "Traction criterion (15%) needs real paying users inside the window; ship by day 3.",
  },
  {
    title: "Voice-first habit game with subscriptions",
    mechanism: "voice interface",
    domain: "health",
    user: "people building daily habits",
    substrate: "mobile game",
    expected_wins: 2.1,
    evidence: [
      { slug: "streakquest", title: "StreakQuest", host: "revenuecat-shipaton-2025" },
      { slug: "habitica-voice", title: "Habitica Voice", host: "health-hack-2025" },
    ],
    why: "Both halves proven (voice ×8 wins, health-game ×5), intersection empty in the 2,300-winner corpus — a gap note exists in the vault.",
    risk: "Design (20%) is crowded; the Best Game track had 61 entries last year.",
  },
]

export const VAULT_NOTES: VaultNote[] = [
  { title: "health × voice", path: "vault/_gaps/health-x-voice.md", excerpt: "Both facets proven independently (health: 41 winners, voice: 19 winners). No winning project combines them. Nearest neighbours: Loudly (audio, education), Seeing AI Companion (voice, accessibility)." },
  { title: "voice interface", path: "vault/mechanisms/voice-interface.md", excerpt: "19 winning projects. Common substrate: mobile (11), web (6), hardware (2). Judges reward latency demos measured on-camera." },
  { title: "health", path: "vault/domains/health.md", excerpt: "41 winning projects across 27 hackathons. Impact anchors usually cite a WHO or CDC prevalence figure in the first paragraph." },
]

export async function health(): Promise<Health> {
  await wait(120)
  const counts = countsOf(HACKATHONS)
  return { ok: true, mode: "local", model: "local-router", census_date: CENSUS_DATE, counts: { ...counts, total: 1863 } }
}

function countsOf(rows: Hackathon[]) {
  return {
    open: rows.filter((r) => r.status === "open").length,
    upcoming: rows.filter((r) => r.status === "upcoming").length,
    ended: rows.filter((r) => r.status === "ended").length,
    total: rows.length,
  }
}

export async function hackathons(query: HackathonQuery): Promise<Hackathon[]> {
  await wait(250)
  let rows = HACKATHONS.slice()
  if (query.status && query.status !== "all") rows = rows.filter((r) => r.status === query.status)
  if (query.theme) rows = rows.filter((r) => r.themes.includes(query.theme!))
  if (query.q) {
    const q = query.q.toLowerCase()
    rows = rows.filter((r) => r.title.toLowerCase().includes(q) || r.org.toLowerCase().includes(q))
  }
  const sort = query.sort || "deadline"
  rows.sort((a, b) => {
    if (sort === "prize") return b.prize_usd - a.prize_usd
    if (sort === "registrations") return b.registrations - a.registrations
    return (a.days_left ?? 9999) - (b.days_left ?? 9999)
  })
  return rows.slice(0, query.limit || 100)
}

export async function hackathon(id: string | number): Promise<HackathonDetail> {
  await wait(200)
  const h = HACKATHONS.find((r) => String(r.id) === String(id))
  if (!h) throw new Error(`No hackathon ${id}`)
  return { ...h, brief: h.host === BRIEF.host ? BRIEF : null }
}

export async function stats(): Promise<Stats> {
  await wait(150)
  const counts = countsOf(HACKATHONS)
  const open = HACKATHONS.filter((r) => r.status === "open")
  const themeCounts = new Map<string, number>()
  for (const r of HACKATHONS) for (const t of r.themes) themeCounts.set(t, (themeCounts.get(t) || 0) + 1)
  return {
    counts,
    prize_total_open: open.reduce((s, r) => s + r.prize_usd, 0),
    themes: [...themeCounts.entries()].map(([name, count]) => ({ name, count })).sort((a, b) => b.count - a.count),
    top_orgs: [
      { name: "Google", count: 14 },
      { name: "RevenueCat", count: 3 },
      { name: "Microsoft", count: 9 },
    ],
    deadlines_next_14d: open.filter((r) => (r.days_left ?? 99) <= 14),
  }
}

export async function winners(q: string, limit: number): Promise<Winner[]> {
  await wait(200)
  const needle = q.toLowerCase()
  return WINNERS.filter((w) => !needle || `${w.title} ${w.tagline}`.toLowerCase().includes(needle)).slice(0, limit)
}

const CHATS: ChatTranscript[] = [
  {
    id: "c_demo",
    title: "Scout RevenueCat Shipaton 2026",
    created_at: new Date(Date.now() - 3 * 3600_000).toISOString(),
    updated_at: new Date(Date.now() - 2 * 3600_000).toISOString(),
    messages: [],
  },
  {
    id: "c_open",
    title: "What's open this week?",
    created_at: new Date(Date.now() - 26 * 3600_000).toISOString(),
    updated_at: new Date(Date.now() - 26 * 3600_000).toISOString(),
    messages: [],
  },
]

export async function chats(): Promise<ChatSummary[]> {
  await wait(100)
  return CHATS.map(({ messages: _m, ...rest }) => rest)
}

export async function chat(id: string): Promise<ChatTranscript> {
  await wait(120)
  const c = CHATS.find((x) => x.id === id)
  if (!c) throw new Error(`No chat ${id}`)
  return c
}

export async function createChat(title?: string): Promise<{ id: string }> {
  await wait(80)
  const id = `c_${Math.random().toString(36).slice(2, 8)}`
  CHATS.unshift({ id, title: title || "New chat", created_at: new Date().toISOString(), updated_at: new Date().toISOString(), messages: [] })
  return { id }
}

export async function startJob(kind: "scout" | "refresh"): Promise<{ job_id: string }> {
  await wait(80)
  return { job_id: `${kind}_${Math.random().toString(36).slice(2, 8)}` }
}

export async function* jobStream(jobId: string, signal?: AbortSignal): AsyncGenerator<JobProgress> {
  const steps = jobId.startsWith("refresh")
    ? ["Listing /api/hackathons", "Paging 1–400", "Paging 400–1,200", "Paging 1,200–1,863", "Writing data/hackathons.jsonl"]
    : ["Resolving hackathon", "Parsing rubric", "Collecting gallery", "Extracting facets", "Generating ideas"]
  for (let i = 0; i < steps.length; i++) {
    if (signal?.aborted) return
    await wait(600)
    yield { job_id: jobId, step: steps[i], pct: Math.round(((i + 1) / steps.length) * 100), note: i === 1 ? "24 per page, plain HTTP" : undefined }
  }
}

// ---------------------------------------------------------------------------
// Canned SSE conversation. Exercises every card type in one reply.
// ---------------------------------------------------------------------------

export async function* sendMessage(chatId: string, text: string, signal?: AbortSignal): AsyncGenerator<SSEEvent> {
  const msgId = `m_${Math.random().toString(36).slice(2, 8)}`
  const chat = CHATS.find((c) => c.id === chatId)
  if (chat && chat.title === "New chat") chat.title = text.slice(0, 60)

  const script: SSEEvent[] = []
  const t = text.toLowerCase()
  script.push({ type: "message_start", data: { chat_id: chatId, message_id: msgId, mode: "local" } })

  if (/open|upcoming|deadline|ending|prize|this week/.test(t)) {
    script.push({ type: "thinking", data: { text: "Filtering the census for open hackathons…" } })
    script.push({ type: "tool_call", data: { id: "t1", name: "list_hackathons", input: { status: "open", sort: "deadline", limit: 6 } } })
    const rows = HACKATHONS.filter((r) => r.status === "open")
    script.push({ type: "tool_result", data: { id: "t1", name: "list_hackathons", ok: true, summary: `${rows.length} open hackathons, sorted by deadline`, data: { rows, total: rows.length } } })
    script.push(...deltas(`**${rows.length} hackathons are open** as of the ${CENSUS_DATE} census, sorted by deadline.\n\n` +
      rows.map((r) => `- **${r.title}** (${r.org}) — ${r.prize_display}, ${r.registrations.toLocaleString()} registered, closes in ${r.days_left} days`).join("\n") +
      `\n\nSay \`scout <name>\` to pull the rubric and the field for one of them.`))
  } else if (/winner|past project/.test(t)) {
    script.push({ type: "thinking", data: { text: "Searching the winners corpus (FTS over title + tagline)…" } })
    script.push({ type: "tool_call", data: { id: "t1", name: "search_winners", input: { query: "agents accessibility", limit: 10 } } })
    script.push({ type: "tool_result", data: { id: "t1", name: "search_winners", ok: true, summary: `${WINNERS.length} winners match — shortlist, not a ranking`, data: { rows: WINNERS } } })
    script.push(...deltas(`Found **${WINNERS.length} winning projects** whose title or tagline mention agents and accessibility. This is a shortlist over ~100-character taglines — it does not rank them, and an idea distinguished only in its body will not surface here.\n\nThe two nearest to a voice agent are *Seeing AI Companion* and *SignBridge*; both won at hosts with an AI-first rubric.`))
  } else if (/gap|mechanism|domain/.test(t)) {
    script.push({ type: "thinking", data: { text: "Looking up vault notes…" } })
    script.push({ type: "tool_call", data: { id: "t1", name: "vault_lookup", input: { query: "health voice", kind: "gap" } } })
    script.push({ type: "tool_result", data: { id: "t1", name: "vault_lookup", ok: true, summary: `${VAULT_NOTES.length} notes`, data: { notes: VAULT_NOTES } } })
    script.push(...deltas(`There is a gap note for **health × voice**: both facets are proven on their own (41 and 19 winners) and no winner in the 2,300-project corpus combines them. The nearest neighbours are listed in the note.`))
  } else if (/stats|how many/.test(t)) {
    script.push({ type: "tool_call", data: { id: "t1", name: "census_stats", input: {} } })
    const s = await stats()
    script.push({ type: "tool_result", data: { id: "t1", name: "census_stats", ok: true, summary: `${s.counts.open} open · $${s.prize_total_open.toLocaleString()} in open prizes`, data: s } })
    script.push(...deltas(`Census of ${CENSUS_DATE}: **${s.counts.open} open**, ${s.counts.upcoming} upcoming, ${s.counts.ended} ended. Open prize pool: **$${s.prize_total_open.toLocaleString()}**.`))
  } else {
    // "scout X" / "what should I build for X" — the full pipeline
    script.push({ type: "thinking", data: { text: "Resolving the hackathon on Devpost…" } })
    script.push({ type: "tool_call", data: { id: "t1", name: "hackathon_brief", input: { name_or_url: "RevenueCat Shipaton 2026" } } })
    script.push({ type: "tool_result", data: { id: "t1", name: "hackathon_brief", ok: true, summary: "5 criteria, weighted 30/25/20/15/10 · tie-break: Quality of the Idea", data: BRIEF } })
    script.push(...deltas(`**RevenueCat Shipaton 2026** judges on five weighted criteria (30/25/20/15/10). The tie-break criterion is **Quality of the Idea** — Devpost's standard tie-break resolves on the first-listed criterion, so at the top of a bunched field it decides placements.\n\nFive requirements fail an entry outright; the one people miss is *published to a store during the submission period*.\n\n`))
    script.push({ type: "thinking", data: { text: "Collecting the project gallery (24 per page)…" } })
    script.push({ type: "tool_call", data: { id: "t2", name: "field", input: { host: "revenuecat-shipaton-2026", winners_only: false, limit: 500 } } })
    script.push({ type: "job_progress", data: { job_id: "t2", step: "Paging gallery", pct: 35, note: "page 9 of 26" } })
    script.push({ type: "job_progress", data: { job_id: "t2", step: "Paging gallery", pct: 80, note: "page 21 of 26" } })
    script.push({ type: "tool_result", data: { id: "t2", name: "field", ok: true, summary: "612 projects in the gallery (source: devpost gallery, 26 pages)", data: { total: 612, source: "gallery", rows: [
      { slug: "paywall-lab", title: "Paywall Lab", tagline: "A/B test paywalls with one line of code.", url: "https://devpost.com/software/paywall-lab", is_winner: false, members: ["ana", "kirill"] },
      { slug: "subly", title: "Subly", tagline: "Track every subscription you pay for, cancel in one tap.", url: "https://devpost.com/software/subly", is_winner: false },
      { slug: "streakquest", title: "StreakQuest", tagline: "A habit RPG where your streak is your HP.", url: "https://devpost.com/software/streakquest", is_winner: false },
    ] } } })
    script.push({ type: "thinking", data: { text: "Generating ideas from facets + brief…" } })
    script.push({ type: "tool_call", data: { id: "t3", name: "ideate", input: { host: "revenuecat-shipaton-2026" } } })
    script.push({ type: "tool_result", data: { id: "t3", name: "ideate", ok: true, summary: `${IDEAS.length} candidates`, data: { candidates: IDEAS } } })
    script.push(...deltas(`The field is **612 projects** so far (gallery published, 26 pages). Two candidate ideas clear the gate in \`position/IDEA-SELECTION.md\`; the first has the most evidence (3 prior winners share its mechanism and domain).\n\n> Expected wins are counts from the winner corpus, not predictions. Shortlist, then verify against the rubric.`))
  }
  script.push({ type: "message_end", data: { usage: { input_tokens: 2140, output_tokens: 412, total_tokens: 2552, duration_ms: 4200, model: "local-router" } } })

  for (const ev of script) {
    if (signal?.aborted) return
    await wait(ev.type === "text_delta" ? 18 : ev.type === "tool_call" ? 700 : 250)
    yield ev
  }
}

function deltas(text: string): SSEEvent[] {
  const out: SSEEvent[] = []
  const words = text.split(/(\s+)/)
  let chunk = ""
  for (const w of words) {
    chunk += w
    if (chunk.length > 12) {
      out.push({ type: "text_delta", data: { text: chunk } })
      chunk = ""
    }
  }
  if (chunk) out.push({ type: "text_delta", data: { text: chunk } })
  return out
}

function wait(ms: number) {
  return new Promise((r) => setTimeout(r, ms))
}
