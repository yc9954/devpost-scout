// The bottom prompt. Wraps 1code's `components/ui/prompt-input.tsx` (verbatim) with the container
// classes from 1code's `chat-input-area.tsx`: bordered input-background box, ring on focus, actions row.

import { useRef, useState } from "react"
import { ArrowUp, Square } from "lucide-react"
import { cn } from "../../lib/utils"
import {
  PromptInput,
  PromptInputAction,
  PromptInputActions,
  PromptInputTextarea,
} from "../../components/ui/prompt-input"
import { Kbd } from "../../components/ui/kbd"
import { Button } from "../../components/ui/button"

export const SUGGESTIONS = [
  "What's open this week?",
  "Scout RevenueCat Shipaton 2026",
  "Winners about agents for accessibility",
  "Gaps in health × voice",
]

interface ChatInputProps {
  isStreaming: boolean
  onSend: (text: string) => void
  onStop: () => void
  showSuggestions?: boolean
  autoFocus?: boolean
}

export function ChatInput({ isStreaming, onSend, onStop, showSuggestions, autoFocus }: ChatInputProps) {
  const [value, setValue] = useState("")
  const [isFocused, setIsFocused] = useState(false)
  const textareaRef = useRef<HTMLTextAreaElement>(null)

  const submit = () => {
    const text = value.trim()
    if (!text || isStreaming) return
    setValue("")
    onSend(text)
  }

  return (
    <div className="px-2 pb-2 shadow-sm shadow-background relative z-10">
      <div className="w-full max-w-2xl mx-auto">
        {showSuggestions && (
          <div className="flex flex-wrap gap-1.5 pb-2 px-0.5">
            {SUGGESTIONS.map((s) => (
              <button
                key={s}
                type="button"
                disabled={isStreaming}
                onClick={() => onSend(s)}
                className="rounded-full border border-border bg-background px-2.5 py-1 text-xs text-muted-foreground hover:text-foreground hover:bg-foreground/5 transition-[background-color,color,transform] duration-150 ease-out active:scale-[0.97] disabled:opacity-50"
              >
                {s}
              </button>
            ))}
          </div>
        )}
        <div className="relative w-full cursor-text" onClick={() => textareaRef.current?.focus()}>
          <PromptInput
            className={cn(
              "border bg-input-background relative z-10 p-2 rounded-xl transition-[border-color,box-shadow] duration-150",
              isFocused && "ring-2 ring-primary/50",
            )}
            maxHeight={200}
            value={value}
            onValueChange={setValue}
            onSubmit={submit}
            isLoading={isStreaming}
          >
            <PromptInputTextarea
              ref={textareaRef}
              autoFocus={autoFocus}
              placeholder={isStreaming ? "Answering…" : "Name a hackathon, or ask what's open"}
              className="bg-transparent max-h-[200px] overflow-y-auto p-1 text-sm placeholder:text-muted-foreground/50"
              onFocus={() => setIsFocused(true)}
              onBlur={() => setIsFocused(false)}
            />
            <PromptInputActions className="w-full">
              <div className="flex items-center gap-0.5 flex-1 min-w-0">
                <span className="hidden min-420:flex items-center gap-1.5 px-1 text-[11px] text-muted-foreground/50">
                  <Kbd>↵</Kbd>
                  <span>send</span>
                  <span className="opacity-60">·</span>
                  <Kbd>⇧↵</Kbd>
                  <span>newline</span>
                </span>
              </div>
              <div className="flex items-center gap-1">
                {isStreaming ? (
                  <PromptInputAction tooltip="Stop">
                    <Button
                      type="button"
                      variant="outline"
                      size="icon"
                      onClick={onStop}
                      className="h-7 w-7 rounded-lg outline-offset-2 focus-visible:outline focus-visible:outline-2 focus-visible:outline-ring/70"
                      aria-label="Stop"
                    >
                      <Square className="h-3 w-3 fill-current" />
                    </Button>
                  </PromptInputAction>
                ) : (
                  <PromptInputAction tooltip="Send">
                    <Button
                      type="button"
                      size="icon"
                      disabled={!value.trim()}
                      onClick={submit}
                      className="h-7 w-7 rounded-lg transition-[background-color,transform,opacity] duration-150 ease-out active:scale-[0.97]"
                      aria-label="Send"
                    >
                      <ArrowUp className="h-4 w-4" />
                    </Button>
                  </PromptInputAction>
                )}
              </div>
            </PromptInputActions>
          </PromptInput>
        </div>
      </div>
    </div>
  )
}
