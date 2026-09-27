// Census stats (SPEC §3 /api/stats) — stat tiles shared by the chat card and the Dashboard.

import { cn } from "../../lib/utils"
import { formatInt, formatMoney } from "../../lib/format"
import { Skeleton } from "../ui/skeleton"
import type { Stats } from "../../types"

export function StatTile({ label, value, hint, className }: { label: string; value: React.ReactNode; hint?: string; className?: string }) {
  return (
    <div className={cn("rounded-xl border bg-card px-3 py-2.5 min-w-0", className)}>
      <div className="text-[11px] text-muted-foreground truncate">{label}</div>
      <div className="text-lg font-semibold tabular-nums leading-tight mt-0.5 truncate">{value}</div>
      {hint && <div className="text-[10px] text-muted-foreground/60 truncate mt-0.5">{hint}</div>}
    </div>
  )
}

export function StatTilesSkeleton({ n = 4 }: { n?: number }) {
  return (
    <div className="grid grid-cols-2 @2xl:grid-cols-4 gap-2">
      {Array.from({ length: n }).map((_, i) => (
        <div key={i} className="rounded-xl border bg-card px-3 py-2.5 space-y-1.5">
          <Skeleton className="h-3 w-16" />
          <Skeleton className="h-6 w-20" />
        </div>
      ))}
    </div>
  )
}

export function StatsCard({ stats }: { stats: Stats }) {
  const ending7 = (stats.deadlines_next_14d || []).filter((h) => (h.days_left ?? 99) <= 7).length
  return (
    <div className="@container space-y-2">
      <div className="grid grid-cols-2 @2xl:grid-cols-4 gap-2">
        <StatTile label="Open" value={formatInt(stats.counts.open)} />
        <StatTile label="Upcoming" value={formatInt(stats.counts.upcoming)} />
        <StatTile label="Ending in 7 days" value={formatInt(ending7)} hint={`${stats.deadlines_next_14d?.length ?? 0} in 14 days`} />
        <StatTile label="Prize pool · open" value={formatMoney(stats.prize_total_open)} />
      </div>
      {(stats.themes?.length > 0 || stats.top_orgs?.length > 0) && (
        <div className="grid grid-cols-1 @2xl:grid-cols-2 gap-2">
          {stats.themes?.length > 0 && (
            <div className="rounded-xl border bg-card px-3 py-2.5">
              <div className="text-[11px] text-muted-foreground mb-1.5">Top themes</div>
              <ul className="space-y-1">
                {stats.themes.slice(0, 6).map((t) => (
                  <li key={t.name} className="flex items-center gap-2 text-xs">
                    <span className="flex-1 truncate">{t.name}</span>
                    <span className="font-mono tabular-nums text-muted-foreground">{formatInt(t.count)}</span>
                  </li>
                ))}
              </ul>
            </div>
          )}
          {stats.top_orgs?.length > 0 && (
            <div className="rounded-xl border bg-card px-3 py-2.5">
              <div className="text-[11px] text-muted-foreground mb-1.5">Top organizers</div>
              <ul className="space-y-1">
                {stats.top_orgs.slice(0, 6).map((o) => (
                  <li key={o.name} className="flex items-center gap-2 text-xs">
                    <span className="flex-1 truncate">{o.name}</span>
                    <span className="font-mono tabular-nums text-muted-foreground">{formatInt(o.count)}</span>
                  </li>
                ))}
              </ul>
            </div>
          )}
        </div>
      )}
    </div>
  )
}
