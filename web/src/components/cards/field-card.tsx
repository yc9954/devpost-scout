// Field card (SPEC §4 `field` → {rows:[Project], total, source}).
// When the gallery is unpublished, say so — an empty field is not an empty field.

import { Grid2x2, TriangleAlert } from "lucide-react"
import type { FieldData } from "../../types"

export function FieldCard({ data }: { data: FieldData }) {
  const rows = data.rows || []
  const unpublished = data.total === 0 || /unpublished|not published|none/i.test(data.source || "")
  return (
    <div className="rounded-xl border bg-card overflow-hidden">
      <div className="px-3 py-2 border-b flex items-center gap-2 text-xs text-muted-foreground">
        <Grid2x2 className="w-3.5 h-3.5" />
        <span>
          <span className="text-foreground font-medium">{data.total.toLocaleString("en-US")}</span> projects
        </span>
        {data.source && <span className="ml-auto text-[10px] uppercase tracking-wide text-muted-foreground/60">source · {data.source}</span>}
      </div>
      {unpublished ? (
        <div className="px-3 py-3 flex items-start gap-2 text-xs text-amber-600 dark:text-amber-400">
          <TriangleAlert className="w-3.5 h-3.5 mt-[1px] flex-shrink-0" />
          <span>
            The gallery is unpublished or returned nothing. This is not a measured field of zero — enumerate through
            search + participants before quoting a size.
          </span>
        </div>
      ) : rows.length === 0 ? (
        <div className="px-3 py-3 text-xs text-muted-foreground">Rows were cached to disk; total above is from the gallery header.</div>
      ) : (
        <>
          <ul className="divide-y divide-border/60 max-h-72 overflow-y-auto">
            {rows.map((p) => (
              <li key={p.slug} className="px-3 py-1.5 flex items-center gap-2 min-w-0">
                <a href={p.url} target="_blank" rel="noopener noreferrer" className="text-sm truncate hover:text-primary transition-colors">
                  {p.title}
                </a>
                {p.is_winner && (
                  <span className="rounded-md bg-amber-500/15 text-amber-600 dark:text-amber-400 px-1.5 py-0.5 text-[10px] font-medium flex-shrink-0">
                    winner
                  </span>
                )}
                {p.tagline && <span className="text-xs text-muted-foreground truncate flex-1 min-w-0">— {p.tagline}</span>}
                {p.members && p.members.length > 0 && (
                  <span className="text-[10px] text-muted-foreground/60 flex-shrink-0">{p.members.length} members</span>
                )}
              </li>
            ))}
          </ul>
          {rows.length < data.total && (
            <div className="px-3 py-1.5 border-t text-[10px] text-muted-foreground/60">
              showing {rows.length.toLocaleString("en-US")} of {data.total.toLocaleString("en-US")}
            </div>
          )}
        </>
      )}
    </div>
  )
}
