"use client"

// Adapted from 1code `features/agents/ui/agent-tool-call.tsx` and the collapsible pattern in
// `agent-web-search-collapsible.tsx` (Apache-2.0). The header row keeps 1code's classes and
// TextShimmer-while-pending; the expanded body is a Scout card chosen by tool name (SPEC §5),
// animated with motion/react.

import { memo, useEffect, useState } from "react"
import { AnimatePresence, motion } from "motion/react"
import {
  BarChart3,
  BookOpen,
  CalendarSearch,
  ChevronRight,
  CircleAlert,
  Compass,
  Grid2x2,
  Lightbulb,
  ScrollText,
  Trophy,
  Wrench,
} from "lucide-react"
import { cn } from "../../lib/utils"
import { TextShimmer } from "../../components/ui/text-shimmer"
import { Progress } from "../../components/ui/progress"
import { Tooltip, TooltipContent, TooltipTrigger } from "../../components/ui/tooltip"
import { ToolCard } from "../../components/cards/tool-card"
import type { ToolCallPart } from "../../types"

interface ToolMeta {
  icon: React.ComponentType<{ className?: string }>
  pending: string
  done: string
  hint?: (input: Record<string, unknown>) => string | undefined
}

const str = (v: unknown) => (v === undefined || v === null || v === "" ? undefined : String(v))

export const TOOL_META: Record<string, ToolMeta> = {
  list_hackathons: {
    icon: CalendarSearch,
    pending: "Listing hackathons",
    done: "Listed hackathons",
    hint: (i) => [str(i.status), str(i.theme), str(i.query)].filter(Boolean).join(" · ") || undefined,
  },
  hackathon_brief: {
    icon: ScrollText,
    pending: "Resolving rubric",
    done: "Resolved rubric",
    hint: (i) => str(i.name_or_url),
  },
  search_winners: {
    icon: Trophy,
    pending: "Searching winners",
    done: "Searched winners",
    hint: (i) => str(i.query),
  },
  field: {
    icon: Grid2x2,
    pending: "Collecting field",
    done: "Collected field",
    hint: (i) => [str(i.host), i.winners_only ? "winners only" : undefined].filter(Boolean).join(" · ") || undefined,
  },
  ideate: { icon: Lightbulb, pending: "Generating ideas", done: "Generated ideas", hint: (i) => str(i.host) },
  vault_lookup: {
    icon: BookOpen,
    pending: "Reading vault",
    done: "Read vault",
    hint: (i) => [str(i.kind), str(i.query)].filter(Boolean).join(" · ") || undefined,
  },
  census_stats: { icon: BarChart3, pending: "Counting census", done: "Counted census" },
  scout: { icon: Compass, pending: "Scouting", done: "Scouted", hint: (i) => str(i.hackathon) },
}

const FALLBACK_META: ToolMeta = { icon: Wrench, pending: "Running tool", done: "Ran tool" }

interface AgentToolCallProps {
  part: ToolCallPart
  isNested?: boolean
}

export const AgentToolCall = memo(
  function AgentToolCall({ part, isNested }: AgentToolCallProps) {
    const meta = TOOL_META[part.name] || FALLBACK_META
    const Icon = meta.icon
    const isPending = part.status === "pending"
    const isError = part.status === "error"
    const hasBody = !isPending && (part.data !== undefined || isError)

    // Expand once the result lands (the card is the point), collapse if the user asks.
    const [isExpanded, setIsExpanded] = useState(false)
    useEffect(() => {
      if (part.status === "ok" && part.data !== undefined) setIsExpanded(true)
    }, [part.status, part.data])

    const titleStr = isPending ? meta.pending : isError ? `${meta.done.replace(/ed\b/, "")} failed` : meta.done
    const hint = meta.hint?.(part.input)
    const subtitleStr = part.summary || hint

    return (
      <div>
        <div
          onClick={() => hasBody && setIsExpanded((v) => !v)}
          className={cn(
            "group flex items-start gap-1.5 py-0.5",
            isNested ? "px-2.5" : "rounded-md px-2",
            hasBody && "cursor-pointer",
          )}
        >
          <div className="flex-shrink-0 flex text-muted-foreground items-start pt-[1px]">
            {isError ? <CircleAlert className="w-3.5 h-3.5 text-destructive" /> : <Icon className="w-3.5 h-3.5" />}
          </div>

          <div className="flex-1 min-w-0 flex items-center gap-1.5">
            <div className="text-xs text-muted-foreground flex items-center gap-1.5 min-w-0">
              <span className={cn("font-medium whitespace-nowrap flex-shrink-0", isError && "text-destructive")}>
                {isPending ? (
                  <TextShimmer as="span" duration={1.2} className="inline-flex items-center text-xs leading-none h-4 m-0">
                    {titleStr}
                  </TextShimmer>
                ) : (
                  titleStr
                )}
              </span>
              {subtitleStr && (
                <Tooltip>
                  <TooltipTrigger asChild>
                    <span className="text-muted-foreground/60 font-normal truncate min-w-0">{subtitleStr}</span>
                  </TooltipTrigger>
                  <TooltipContent side="top" className="px-2 py-1.5 max-w-none flex items-center justify-center">
                    <span className="font-mono text-[10px] text-muted-foreground whitespace-nowrap leading-none">
                      {part.name}({Object.keys(part.input).length ? JSON.stringify(part.input) : ""})
                    </span>
                  </TooltipContent>
                </Tooltip>
              )}
              {hasBody && (
                <ChevronRight
                  className={cn(
                    "w-3.5 h-3.5 text-muted-foreground/60 transition-transform duration-200 ease-out flex-shrink-0",
                    isExpanded && "rotate-90",
                    !isExpanded && "opacity-0 group-hover:opacity-100",
                  )}
                />
              )}
            </div>
          </div>
        </div>

        {/* Long-tool progress (job_progress events) */}
        {isPending && part.progress && (
          <div className="px-2 pl-7 pb-1 pt-0.5">
            <div className="flex items-center gap-2 text-[11px] text-muted-foreground/70">
              <Progress value={part.progress.pct} className="h-1 w-32 bg-muted" />
              <span className="tabular-nums">{Math.round(part.progress.pct)}%</span>
              <span className="truncate">
                {part.progress.step}
                {part.progress.note ? ` · ${part.progress.note}` : ""}
              </span>
            </div>
          </div>
        )}

        <AnimatePresence initial={false}>
          {isExpanded && hasBody && (
            <motion.div
              key="body"
              initial={{ height: 0, opacity: 0 }}
              animate={{ height: "auto", opacity: 1 }}
              exit={{ height: 0, opacity: 0 }}
              transition={{ duration: 0.2, ease: "easeOut" }}
              className="overflow-hidden"
            >
              <div className="px-2 pt-1 pb-2">
                {isError ? (
                  <div className="rounded-lg border border-destructive/40 bg-destructive/10 px-3 py-2 text-xs text-destructive">
                    {part.summary || "The tool failed."}
                  </div>
                ) : (
                  <ToolCard name={part.name} data={part.data} />
                )}
              </div>
            </motion.div>
          )}
        </AnimatePresence>
      </div>
    )
  },
  (prev, next) =>
    prev.part.status === next.part.status &&
    prev.part.summary === next.part.summary &&
    prev.part.data === next.part.data &&
    prev.part.progress === next.part.progress &&
    prev.isNested === next.isNested,
)
