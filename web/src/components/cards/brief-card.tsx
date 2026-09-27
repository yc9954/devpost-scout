// Brief card (SPEC §5 `Brief`): criteria with weights, tie-break highlighted, requirements
// checklist, prizes. The tie-break is the first-listed criterion — Devpost resolves ties on it.

import { ExternalLink, SquareCheck, Trophy } from "lucide-react"
import { cn } from "../../lib/utils"
import { Badge } from "../ui/badge"
import type { Brief } from "../../types"

export function BriefCard({ brief, className }: { brief: Brief; className?: string }) {
  const weighted = brief.weighting === "weighted"
  const maxWeight = Math.max(1, ...brief.criteria.map((c) => c.weight ?? 0))
  return (
    <div className={cn("rounded-xl border bg-card overflow-hidden", className)}>
      <div className="px-3 py-2.5 border-b flex items-start gap-3">
        <div className="flex-1 min-w-0">
          <div className="flex items-center gap-2 min-w-0">
            <span className="text-sm font-medium truncate">{brief.title}</span>
            <Badge variant="secondary" className="text-[10px] flex-shrink-0">
              {brief.weighting === "unknown" ? "weights unknown" : `${brief.weighting} weights`}
            </Badge>
          </div>
          <div className="text-xs text-muted-foreground truncate">
            {brief.dates}
            {brief.host ? ` · ${brief.host}` : ""}
          </div>
        </div>
        {brief.url && (
          <a
            href={brief.url}
            target="_blank"
            rel="noopener noreferrer"
            className="text-muted-foreground hover:text-foreground transition-colors flex-shrink-0"
            aria-label="Open on Devpost"
          >
            <ExternalLink className="w-3.5 h-3.5" />
          </a>
        )}
      </div>

      <div className="px-3 py-2.5 space-y-3">
        {/* Criteria */}
        <section>
          <h4 className="text-[11px] font-medium text-muted-foreground uppercase tracking-wide mb-1.5">
            Judging criteria · {brief.criteria.length}
          </h4>
          {brief.criteria.length === 0 ? (
            <p className="text-xs text-muted-foreground/70">
              No criteria parsed{brief.criteria_source === null ? " (criteria_source is null — edit by hand)" : ""}.
            </p>
          ) : (
            <ol className="space-y-1.5">
              {brief.criteria.map((c, i) => {
                const isTie = !!brief.tiebreak_criterion && c.label === brief.tiebreak_criterion
                return (
                  <li
                    key={i}
                    className={cn(
                      "rounded-lg px-2.5 py-2 border",
                      isTie ? "border-primary/50 bg-primary/5" : "border-transparent bg-muted/40",
                    )}
                  >
                    <div className="flex items-center gap-2">
                      <span className="text-[11px] tabular-nums text-muted-foreground/60 w-4">{i + 1}.</span>
                      <span className="text-sm font-medium flex-1 min-w-0 truncate">{c.label}</span>
                      {isTie && (
                        <Badge className="text-[10px] gap-1 hover:bg-primary">
                          <Trophy className="w-2.5 h-2.5" />
                          tie-break
                        </Badge>
                      )}
                      {c.weight !== undefined && c.weight !== null && (
                        <span className="text-xs font-mono tabular-nums text-foreground">{c.weight}%</span>
                      )}
                    </div>
                    {weighted && c.weight !== undefined && c.weight !== null && (
                      <div className="mt-1.5 ml-6 h-1 rounded-full bg-muted overflow-hidden">
                        <div
                          className={cn("h-full rounded-full", isTie ? "bg-primary" : "bg-muted-foreground/40")}
                          style={{ width: `${Math.round((c.weight / maxWeight) * 100)}%` }}
                        />
                      </div>
                    )}
                    {c.text && <p className="mt-1 ml-6 text-xs text-muted-foreground leading-relaxed">{c.text}</p>}
                  </li>
                )
              })}
            </ol>
          )}
          {brief.tiebreak_criterion && (
            <p className="mt-1.5 text-[11px] text-muted-foreground/70">
              Ties resolve on <span className="text-foreground">{brief.tiebreak_criterion}</span> — at the top of a bunched
              field it decides placements.
            </p>
          )}
        </section>

        {/* Requirements */}
        {brief.requirements.length > 0 && (
          <section>
            <h4 className="text-[11px] font-medium text-muted-foreground uppercase tracking-wide mb-1.5">
              Requirements · fail an entry outright
            </h4>
            <ul className="space-y-1">
              {brief.requirements.map((r, i) => (
                <li key={i} className="flex items-start gap-2 text-xs">
                  <SquareCheck className="w-3.5 h-3.5 mt-[1px] text-muted-foreground/60 flex-shrink-0" />
                  <span className="text-foreground/90">{r}</span>
                </li>
              ))}
            </ul>
          </section>
        )}

        {/* Prizes */}
        {brief.prizes.length > 0 && (
          <section>
            <h4 className="text-[11px] font-medium text-muted-foreground uppercase tracking-wide mb-1.5">
              Prizes · {brief.prizes.length}
            </h4>
            <ul className="divide-y divide-border/60 rounded-lg border">
              {brief.prizes.map((p, i) => (
                <li key={i} className="flex items-center justify-between gap-3 px-2.5 py-1.5 text-xs">
                  <span className="truncate">{p.name}</span>
                  {p.amount !== undefined && p.amount !== null && p.amount !== "" && (
                    <span className="font-mono tabular-nums text-foreground flex-shrink-0">
                      {typeof p.amount === "number" ? `$${p.amount.toLocaleString("en-US")}` : p.amount}
                    </span>
                  )}
                </li>
              ))}
            </ul>
          </section>
        )}

        {brief.criteria_source && (
          <p className="text-[10px] text-muted-foreground/60 truncate">
            source:{" "}
            <a href={brief.criteria_source} target="_blank" rel="noopener noreferrer" className="hover:text-foreground underline-offset-2 hover:underline">
              {brief.criteria_source}
            </a>
          </p>
        )}
      </div>
    </div>
  )
}
