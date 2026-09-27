import { useApp } from "../../store"
import { Badge } from "../../components/ui/badge"
import { Skeleton } from "../../components/ui/skeleton"
import { Tooltip, TooltipContent, TooltipTrigger } from "../../components/ui/tooltip"
import { cn } from "../../lib/utils"

/** Mode badge from GET /api/health: `claude` (API key set) or `local` (deterministic router). */
export function ModeBadge({ className }: { className?: string }) {
  const health = useApp((s) => s.health)
  const healthError = useApp((s) => s.healthError)

  if (!health && !healthError) {
    return (
      <div className={cn("flex items-center gap-2 px-1", className)}>
        <Skeleton className="h-5 w-16 rounded-full" />
        <Skeleton className="h-3 w-24" />
      </div>
    )
  }

  if (!health) {
    return (
      <Tooltip>
        <TooltipTrigger asChild>
          <div className={cn("flex items-center gap-2 px-1 cursor-default", className)}>
            <Badge variant="outline" className="text-[10px] font-medium border-destructive/40 text-destructive gap-1">
              <span className="w-1.5 h-1.5 rounded-full bg-destructive" />
              offline
            </Badge>
            <span className="text-[11px] text-muted-foreground/60 truncate">server unreachable</span>
          </div>
        </TooltipTrigger>
        <TooltipContent side="top" className="max-w-[240px]">
          {healthError}. Start it with <code className="font-mono text-[10px]">python3 -m scout</code>, or add <code className="font-mono text-[10px]">?mock=1</code>.
        </TooltipContent>
      </Tooltip>
    )
  }

  const isClaude = health.mode === "claude"
  return (
    <Tooltip>
      <TooltipTrigger asChild>
        <div className={cn("flex items-center gap-2 px-1 cursor-default min-w-0", className)}>
          <Badge
            variant={isClaude ? "default" : "secondary"}
            className={cn("text-[10px] font-medium gap-1 flex-shrink-0", isClaude && "hover:bg-primary")}
          >
            <span className={cn("w-1.5 h-1.5 rounded-full", isClaude ? "bg-white" : "bg-muted-foreground")} />
            {health.mode}
          </Badge>
          <span className="text-[11px] text-muted-foreground/60 truncate">{health.model}</span>
        </div>
      </TooltipTrigger>
      <TooltipContent side="top" className="flex flex-col items-start gap-0.5">
        <span>{isClaude ? "Claude mode — ANTHROPIC_API_KEY is set" : "Local mode — deterministic intent router"}</span>
        <span className="text-[10px] text-muted-foreground">census {health.census_date} · {health.counts.total.toLocaleString()} hackathons</span>
      </TooltipContent>
    </Tooltip>
  )
}
