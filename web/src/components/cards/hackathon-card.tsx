// Hackathon grid card — shared by the chat `list_hackathons` result and the Dashboard (SPEC §6).

import { memo, useState } from "react"
import { Clock, Trophy, Users } from "lucide-react"
import { cn } from "../../lib/utils"
import { deadlineLabel, formatInt, formatMoney, httpsThumb } from "../../lib/format"
import { Skeleton } from "../ui/skeleton"
import type { Hackathon } from "../../types"

export function StatusPill({ status, className }: { status: Hackathon["status"]; className?: string }) {
  const map = {
    open: { dot: "bg-emerald-500", text: "text-emerald-600 dark:text-emerald-400", label: "Open" },
    upcoming: { dot: "bg-blue-500", text: "text-blue-600 dark:text-blue-400", label: "Upcoming" },
    ended: { dot: "bg-muted-foreground/50", text: "text-muted-foreground", label: "Ended" },
  }[status] || { dot: "bg-muted-foreground/50", text: "text-muted-foreground", label: status }
  return (
    <span className={cn("inline-flex items-center gap-1.5 text-[11px] font-medium", map.text, className)}>
      <span className={cn("w-1.5 h-1.5 rounded-full", map.dot)} />
      {map.label}
    </span>
  )
}

export function Thumb({ src, title, className }: { src?: string; title: string; className?: string }) {
  const url = httpsThumb(src)
  const [broken, setBroken] = useState(false)
  const showImg = !!url && !broken
  return (
    <div className={cn("relative flex-shrink-0 rounded-md overflow-hidden bg-muted border border-border/60", className)}>
      {showImg && <img src={url} alt="" loading="lazy" className="w-full h-full object-cover" onError={() => setBroken(true)} />}
      {!showImg && (
        <div className="absolute inset-0 flex items-center justify-center text-sm font-semibold text-muted-foreground/60 select-none">
          {title.slice(0, 1).toUpperCase()}
        </div>
      )}
    </div>
  )
}

interface HackathonCardProps {
  h: Hackathon
  onClick?: (h: Hackathon) => void
  compact?: boolean
}

export const HackathonCard = memo(function HackathonCard({ h, onClick, compact }: HackathonCardProps) {
  const deadline = deadlineLabel(h)
  const urgent = h.status === "open" && (h.days_left ?? 99) <= 7
  const Wrapper: React.ElementType = onClick ? "button" : "div"
  return (
    <Wrapper
      type={onClick ? "button" : undefined}
      onClick={onClick ? () => onClick(h) : undefined}
      className={cn(
        "group text-left w-full rounded-xl border bg-card p-3 flex flex-col gap-2.5 min-w-0",
        "transition-[background-color,border-color,transform] duration-150 ease-out",
        onClick && "cursor-pointer hover:bg-foreground/[0.03] hover:border-border/80 active:scale-[0.995] outline-offset-2 focus-visible:outline focus-visible:outline-2 focus-visible:outline-ring/70",
      )}
    >
      <div className="flex items-start gap-3 min-w-0">
        <Thumb src={h.thumbnail} title={h.title} className={compact ? "w-10 h-10" : "w-12 h-12"} />
        <div className="flex-1 min-w-0">
          <div className="flex items-center gap-2 min-w-0">
            <span className="text-sm font-medium truncate">{h.title}</span>
            {h.featured && <span className="text-[10px] uppercase tracking-wide text-primary/80 flex-shrink-0">featured</span>}
          </div>
          <div className="text-xs text-muted-foreground truncate">{h.org || h.host}</div>
          <div className="mt-1 flex items-center gap-2.5 flex-wrap">
            <StatusPill status={h.status} />
            <span className={cn("inline-flex items-center gap-1 text-[11px]", urgent ? "text-amber-600 dark:text-amber-400" : "text-muted-foreground")}>
              <Clock className="w-3 h-3" />
              {deadline}
            </span>
          </div>
        </div>
      </div>

      <div className="flex items-center gap-3 text-[11px] text-muted-foreground">
        <span className="inline-flex items-center gap-1 text-foreground font-medium">
          <Trophy className="w-3 h-3 text-muted-foreground" />
          {h.prize_usd > 0 ? formatMoney(h.prize_usd) : h.prize_display || "—"}
        </span>
        <span className="inline-flex items-center gap-1">
          <Users className="w-3 h-3" />
          {formatInt(h.registrations)}
        </span>
        <span className="ml-auto truncate">{h.dates}</span>
      </div>

      {h.themes.length > 0 && (
        <div className="flex flex-wrap gap-1">
          {h.themes.slice(0, compact ? 3 : 5).map((t) => (
            <span key={t} className="rounded-md bg-muted px-1.5 py-0.5 text-[10px] text-muted-foreground">
              {t}
            </span>
          ))}
          {h.themes.length > (compact ? 3 : 5) && (
            <span className="text-[10px] text-muted-foreground/60 px-1">+{h.themes.length - (compact ? 3 : 5)}</span>
          )}
        </div>
      )}
    </Wrapper>
  )
})

export function HackathonGrid({ rows, onClick, compact }: { rows: Hackathon[]; onClick?: (h: Hackathon) => void; compact?: boolean }) {
  return (
    <div className="@container">
      <div className={cn("grid gap-2", compact ? "grid-cols-1 @md:grid-cols-2" : "grid-cols-1 @lg:grid-cols-2 @4xl:grid-cols-3")}>
        {rows.map((h) => (
          <HackathonCard key={h.id} h={h} onClick={onClick} compact={compact} />
        ))}
      </div>
    </div>
  )
}

export function HackathonGridSkeleton({ n = 6 }: { n?: number }) {
  return (
    <div className="@container">
      <div className="grid gap-2 grid-cols-1 @lg:grid-cols-2 @4xl:grid-cols-3">
        {Array.from({ length: n }).map((_, i) => (
          <div key={i} className="rounded-xl border bg-card p-3 flex flex-col gap-2.5">
            <div className="flex items-start gap-3">
              <Skeleton className="w-12 h-12 rounded-md" />
              <div className="flex-1 space-y-1.5">
                <Skeleton className="h-4 w-3/4" />
                <Skeleton className="h-3 w-1/3" />
                <Skeleton className="h-3 w-1/2" />
              </div>
            </div>
            <Skeleton className="h-3 w-2/3" />
            <div className="flex gap-1">
              <Skeleton className="h-4 w-12" />
              <Skeleton className="h-4 w-14" />
            </div>
          </div>
        ))}
      </div>
    </div>
  )
}
