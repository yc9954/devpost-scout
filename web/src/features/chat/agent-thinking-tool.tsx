"use client"

// Adapted from 1code `features/agents/ui/agent-thinking-tool.tsx` (Apache-2.0).
// Scout's `thinking` SSE event is a one-line status ("Resolving the hackathon…"), so this keeps
// the header row (shimmer while live, "Thought" preview after) and drops the scrolling body.

import { memo } from "react"
import { cn } from "../../lib/utils"
import { TextShimmer } from "../../components/ui/text-shimmer"

interface AgentThinkingToolProps {
  text: string
  isStreaming: boolean
}

const PREVIEW_LENGTH = 80

export const AgentThinkingTool = memo(function AgentThinkingTool({ text, isStreaming }: AgentThinkingToolProps) {
  const previewText = text.slice(0, PREVIEW_LENGTH).replace(/\n/g, " ")
  return (
    <div>
      <div className="group flex items-start gap-1.5 py-0.5 px-2">
        <div className="flex-1 min-w-0 flex items-center gap-1">
          <div className="text-xs flex items-center gap-1.5 min-w-0">
            <span className="font-medium whitespace-nowrap flex-shrink-0">
              {isStreaming ? (
                <TextShimmer as="span" duration={1.2} className="inline-flex items-center text-xs leading-none h-4 m-0">
                  {previewText || "Thinking"}
                </TextShimmer>
              ) : (
                <span className="text-muted-foreground">Thought</span>
              )}
            </span>
            {!isStreaming && previewText && (
              <span className={cn("text-muted-foreground/60 truncate")}>{previewText}</span>
            )}
          </div>
        </div>
      </div>
    </div>
  )
})

/** The live status line under a streaming reply (SPEC §6: "shimmer while tools run"). */
export function StatusLine({ text }: { text: string }) {
  return (
    <div className="flex items-start gap-1.5 py-0.5 px-2">
      <TextShimmer as="span" duration={1.2} className="inline-flex items-center text-xs leading-none h-4 m-0 font-medium">
        {text}
      </TextShimmer>
    </div>
  )
}
