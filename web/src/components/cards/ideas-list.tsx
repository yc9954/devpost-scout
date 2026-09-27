// Ideas list (SPEC §5 `Idea`): expected wins, facet chips, evidence chips, why, risk.

import { Lightbulb, TriangleAlert } from "lucide-react"
import { EmptyNote } from "./winners-list"
import type { Idea } from "../../types"

export function IdeasList({ candidates }: { candidates: Idea[] }) {
  if (candidates.length === 0) {
    return <EmptyNote>No candidates cleared the gate. Run `hackathon_brief` first — ideate needs the cached brief.</EmptyNote>
  }
  return (
    <div className="space-y-2">
      {candidates.map((idea, i) => (
        <div key={i} className="rounded-xl border bg-card px-3 py-2.5 space-y-2">
          <div className="flex items-start gap-2">
            <Lightbulb className="w-3.5 h-3.5 mt-[3px] text-muted-foreground flex-shrink-0" />
            <div className="flex-1 min-w-0">
              <div className="flex items-center gap-2">
                <span className="text-sm font-medium flex-1 min-w-0 truncate">{idea.title}</span>
                <span
                  className="text-[11px] font-mono tabular-nums rounded-md bg-primary/10 text-primary px-1.5 py-0.5 flex-shrink-0"
                  title="Expected wins — a count from the winner corpus, not a prediction"
                >
                  {Number.isFinite(idea.expected_wins) ? idea.expected_wins.toFixed(1) : "—"} wins
                </span>
              </div>
              <div className="mt-1 flex flex-wrap gap-1">
                {(
                  [
                    ["mechanism", idea.mechanism],
                    ["domain", idea.domain],
                    ["user", idea.user],
                    ["substrate", idea.substrate],
                  ] as const
                )
                  .filter(([, v]) => !!v)
                  .map(([k, v]) => (
                    <span key={k} className="inline-flex items-center gap-1 rounded-md bg-muted px-1.5 py-0.5 text-[10px] text-muted-foreground">
                      <span className="text-muted-foreground/50">{k}</span>
                      <span className="text-foreground/80">{v}</span>
                    </span>
                  ))}
              </div>
            </div>
          </div>

          {idea.why && <p className="text-xs text-muted-foreground leading-relaxed pl-5.5 ml-[22px]">{idea.why}</p>}

          {idea.risk && (
            <p className="text-xs text-amber-600 dark:text-amber-400/90 leading-relaxed flex items-start gap-1.5 ml-[22px]">
              <TriangleAlert className="w-3 h-3 mt-[2px] flex-shrink-0" />
              <span>{idea.risk}</span>
            </p>
          )}

          {idea.evidence.length > 0 && (
            <div className="ml-[22px] flex flex-wrap items-center gap-1">
              <span className="text-[10px] uppercase tracking-wide text-muted-foreground/60 mr-0.5">evidence</span>
              {idea.evidence.map((e) => (
                <a
                  key={e.slug}
                  href={`https://devpost.com/software/${e.slug}`}
                  target="_blank"
                  rel="noopener noreferrer"
                  title={e.host}
                  className="rounded-full border border-border px-2 py-0.5 text-[10px] text-muted-foreground hover:text-foreground hover:bg-foreground/5 transition-colors"
                >
                  {e.title}
                </a>
              ))}
            </div>
          )}
        </div>
      ))}
    </div>
  )
}
