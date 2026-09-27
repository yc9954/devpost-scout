"use client"

// Adapted from 1code `features/agents/ui/agent-user-message-bubble.tsx` (Apache-2.0).
// Dropped: image attachments, @-mention rendering and in-chat search highlighting.
// Kept: the bubble classes, overflow-detection fade, and the "Full message" dialog.

import { useState, useRef, memo } from "react"
import { cn } from "../../lib/utils"
import { useOverflowDetection } from "../../hooks/use-overflow-detection"
import { Dialog, DialogContent, DialogHeader, DialogTitle } from "../../components/ui/dialog"

interface AgentUserMessageBubbleProps {
  messageId: string
  textContent: string
}

export const AgentUserMessageBubble = memo(function AgentUserMessageBubble({
  messageId,
  textContent,
}: AgentUserMessageBubbleProps) {
  const [isExpanded, setIsExpanded] = useState(false)
  const contentRef = useRef<HTMLDivElement>(null)

  // VS Code style overflow detection using ResizeObserver (no layout thrashing)
  const showGradient = useOverflowDetection(contentRef, [textContent])

  return (
    <>
      <div className="flex justify-start drop-shadow-[0_10px_20px_hsl(var(--background))]" data-user-bubble>
        <div className="space-y-2 w-full">
          {textContent ? (
            <div
              ref={contentRef}
              onClick={() => showGradient && setIsExpanded(true)}
              className={cn(
                "relative bg-input-background border px-3 py-2 rounded-xl whitespace-pre-wrap text-sm transition-all duration-200 max-h-[100px] overflow-hidden",
                showGradient && "cursor-pointer hover:brightness-110",
              )}
              data-message-id={messageId}
              data-part-index={0}
              data-part-type="text"
            >
              {textContent}
              {showGradient && (
                <div className="absolute bottom-0 left-0 right-0 h-10 pointer-events-none bg-gradient-to-t from-[hsl(var(--input-background))] to-transparent rounded-b-xl" />
              )}
            </div>
          ) : null}
        </div>
      </div>

      {/* Full message dialog */}
      <Dialog open={isExpanded} onOpenChange={setIsExpanded}>
        <DialogContent className="max-w-2xl max-h-[80vh] overflow-y-auto">
          <DialogHeader>
            <DialogTitle className="text-sm font-medium text-muted-foreground">Full message</DialogTitle>
          </DialogHeader>
          <div className="space-y-3">
            <div className="whitespace-pre-wrap text-sm">{textContent}</div>
          </div>
        </DialogContent>
      </Dialog>
    </>
  )
})
