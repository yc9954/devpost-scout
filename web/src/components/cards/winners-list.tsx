// Winners list (SPEC §5 `Winner`). FTS over title+tagline: it shortlists, never ranks.

import { Award, ExternalLink } from "lucide-react"
import type { Winner } from "../../types"

export function WinnersList({ rows }: { rows: Winner[] }) {
  if (rows.length === 0) {
    return <EmptyNote>No winners match. Taglines are ~100 characters — try a broader term.</EmptyNote>
  }
  return (
    <div className="rounded-xl border bg-card overflow-hidden">
      <div className="px-3 py-2 border-b flex items-center gap-2 text-xs text-muted-foreground">
        <Award className="w-3.5 h-3.5" />
        <span>
          {rows.length} {rows.length === 1 ? "winner" : "winners"}
        </span>
        <span className="ml-auto text-[10px] uppercase tracking-wide text-muted-foreground/60">shortlist · not a ranking</span>
      </div>
      <ul className="divide-y divide-border/60">
        {rows.map((w) => (
          <li key={w.slug} className="px-3 py-2 flex items-start gap-3">
            <div className="flex-1 min-w-0">
              <div className="flex items-center gap-2 min-w-0">
                <a
                  href={w.url}
                  target="_blank"
                  rel="noopener noreferrer"
                  className="text-sm font-medium truncate hover:text-primary transition-colors"
                >
                  {w.title}
                </a>
                {w.is_winner && (
                  <span className="rounded-md bg-amber-500/15 text-amber-600 dark:text-amber-400 px-1.5 py-0.5 text-[10px] font-medium flex-shrink-0">
                    winner
                  </span>
                )}
              </div>
              {w.tagline && <p className="text-xs text-muted-foreground mt-0.5 line-clamp-2">{w.tagline}</p>}
              <p className="text-[11px] text-muted-foreground/60 mt-1 truncate">{w.hackathon_title || w.host}</p>
            </div>
            <a href={w.url} target="_blank" rel="noopener noreferrer" className="text-muted-foreground/50 hover:text-foreground transition-colors mt-0.5 flex-shrink-0" aria-label="Open on Devpost">
              <ExternalLink className="w-3.5 h-3.5" />
            </a>
          </li>
        ))}
      </ul>
    </div>
  )
}

export function EmptyNote({ children }: { children: React.ReactNode }) {
  return <div className="rounded-xl border border-dashed bg-card/50 px-3 py-4 text-xs text-muted-foreground text-center">{children}</div>
}
