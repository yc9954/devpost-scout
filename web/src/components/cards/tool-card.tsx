// Picks the card for a tool_result by tool name (SPEC §4 → §5).

import { HackathonGrid } from "./hackathon-card"
import { BriefCard } from "./brief-card"
import { WinnersList, EmptyNote } from "./winners-list"
import { IdeasList } from "./ideas-list"
import { VaultNotes } from "./vault-notes"
import { FieldCard } from "./field-card"
import { StatsCard } from "./stats-card"
import type {
  Brief,
  FieldData,
  Hackathon,
  Idea,
  IdeateData,
  ListHackathonsData,
  ScoutData,
  SearchWinnersData,
  Stats,
  VaultLookupData,
} from "../../types"

const isObj = (v: unknown): v is Record<string, unknown> => !!v && typeof v === "object" && !Array.isArray(v)
const as = <T,>(v: unknown): T => v as T

export function ToolCard({ name, data }: { name: string; data: unknown }) {
  if (data === undefined || data === null) return null

  switch (name) {
    case "list_hackathons": {
      const rows = (isObj(data) ? as<ListHackathonsData>(data).rows : (data as Hackathon[])) || []
      if (rows.length === 0) return <EmptyNote>No hackathons match this filter in the census.</EmptyNote>
      const total = isObj(data) ? as<ListHackathonsData>(data).total : rows.length
      return (
        <div className="space-y-1.5">
          <HackathonGrid rows={rows} compact />
          {total > rows.length && (
            <p className="text-[10px] text-muted-foreground/60 px-0.5">
              showing {rows.length} of {total.toLocaleString("en-US")}
            </p>
          )}
        </div>
      )
    }
    case "hackathon_brief":
      return isObj(data) && Array.isArray(data.criteria) ? <BriefCard brief={data as unknown as Brief} /> : <RawJson data={data} />
    case "search_winners":
      return <WinnersList rows={(isObj(data) ? as<SearchWinnersData>(data).rows : (data as SearchWinnersData["rows"])) || []} />
    case "field":
      return isObj(data) ? <FieldCard data={data as unknown as FieldData} /> : <RawJson data={data} />
    case "ideate": {
      const candidates = (isObj(data) ? as<IdeateData>(data).candidates : (data as Idea[])) || []
      return <IdeasList candidates={candidates} />
    }
    case "vault_lookup":
      return <VaultNotes notes={(isObj(data) ? as<VaultLookupData>(data).notes : []) || []} />
    case "census_stats":
      return isObj(data) && isObj(data.counts) ? <StatsCard stats={data as unknown as Stats} /> : <RawJson data={data} />
    case "scout": {
      if (!isObj(data)) return <RawJson data={data} />
      const s = data as ScoutData
      const ideas = Array.isArray(s.ideas) ? s.ideas : s.ideas?.candidates || []
      return (
        <div className="space-y-2">
          {s.brief && <BriefCard brief={s.brief} />}
          {s.field && <FieldCard data={s.field} />}
          {ideas.length > 0 && <IdeasList candidates={ideas} />}
          {!s.brief && !s.field && ideas.length === 0 && <RawJson data={data} />}
        </div>
      )
    }
    default:
      return <RawJson data={data} />
  }
}

export function RawJson({ data }: { data: unknown }) {
  let text: string
  try {
    text = typeof data === "string" ? data : JSON.stringify(data, null, 2)
  } catch {
    text = String(data)
  }
  return (
    <pre className="rounded-lg border bg-muted/50 p-2.5 text-[11px] font-mono text-muted-foreground overflow-x-auto max-h-64 whitespace-pre-wrap break-words">
      {text}
    </pre>
  )
}
