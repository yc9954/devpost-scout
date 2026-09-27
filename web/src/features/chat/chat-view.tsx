// Chat screen (SPEC §6.1). Thread container widths follow 1code's active-chat.tsx
// (`max-w-2xl mx-auto px-2 space-y-4`).

import { useCallback, useEffect, useMemo, useRef } from "react"
import { useApp } from "../../store"
import { AgentUserMessageBubble } from "./agent-user-message-bubble"
import { AgentToolCall } from "./agent-tool-call"
import { AgentThinkingTool, StatusLine } from "./agent-thinking-tool"
import { AgentMessageUsage } from "./agent-message-usage"
import { Markdown } from "./markdown"
import { ChatInput, SUGGESTIONS } from "./chat-input"
import { Skeleton } from "../../components/ui/skeleton"
import { ScoutMark } from "../sidebar/agents-sidebar"
import type { ChatMessage } from "../../types"

export function ChatView() {
  const activeChatId = useApp((s) => s.activeChatId)
  const chats = useApp((s) => s.chats)
  const health = useApp((s) => s.health)
  const messages = useApp((s) => (activeChatId ? s.messages[activeChatId] : undefined))
  const loading = useApp((s) => (activeChatId ? !!s.transcriptLoading[activeChatId] : false))
  const isStreaming = useApp((s) => (activeChatId ? !!s.streaming[activeChatId] : false))
  const statusLine = useApp((s) => (activeChatId ? s.statusLine[activeChatId] : null))
  const send = useApp((s) => s.send)
  const stop = useApp((s) => s.stop)
  const newChat = useApp((s) => s.newChat)

  const title = useMemo(() => chats.find((c) => c.id === activeChatId)?.title, [chats, activeChatId])
  const list = messages || []
  const isEmpty = !activeChatId || (!loading && list.length === 0)

  // ⌘N → new chat (1code hotkey)
  useEffect(() => {
    const onKey = (e: KeyboardEvent) => {
      if ((e.metaKey || e.ctrlKey) && e.key.toLowerCase() === "n") {
        e.preventDefault()
        void newChat()
      }
    }
    window.addEventListener("keydown", onKey)
    return () => window.removeEventListener("keydown", onKey)
  }, [newChat])

  // Auto-scroll while streaming when the user is near the bottom.
  const scrollRef = useRef<HTMLDivElement>(null)
  const stickRef = useRef(true)
  const onScroll = useCallback(() => {
    const el = scrollRef.current
    if (!el) return
    stickRef.current = el.scrollHeight - el.scrollTop - el.clientHeight < 80
  }, [])
  useEffect(() => {
    const el = scrollRef.current
    if (!el || !stickRef.current) return
    el.scrollTop = el.scrollHeight
  }, [list, statusLine])
  useEffect(() => {
    stickRef.current = true
    const el = scrollRef.current
    if (el) el.scrollTop = el.scrollHeight
  }, [activeChatId])

  const handleSend = useCallback((text: string) => void send(text), [send])
  const handleStop = useCallback(() => activeChatId && stop(activeChatId), [activeChatId, stop])

  return (
    <div className="flex flex-col h-full min-h-0">
      {/* Header */}
      <div className="h-10 flex items-center px-4 gap-2 flex-shrink-0">
        <span className="text-sm font-medium truncate pl-6 md:pl-0">{title || (activeChatId ? "New chat" : "Scout")}</span>
        {health && (
          <span className="ml-auto text-[11px] text-muted-foreground/60 whitespace-nowrap">
            census {health.census_date}
          </span>
        )}
      </div>

      {/* Thread */}
      <div ref={scrollRef} onScroll={onScroll} className="flex-1 overflow-y-auto w-full relative allow-text-selection outline-none select-text">
        {loading ? (
          <div className="px-2 max-w-2xl mx-auto space-y-4 py-4">
            <Skeleton className="h-10 w-2/3 rounded-xl" />
            <Skeleton className="h-4 w-1/3" />
            <Skeleton className="h-24 w-full rounded-xl" />
          </div>
        ) : isEmpty ? (
          <EmptyThread onPick={handleSend} />
        ) : (
          <div className="px-2 max-w-2xl mx-auto space-y-4 py-4">
            {list.map((m) => (
              <MessageRow key={m.id} message={m} isStreaming={isStreaming && m.id === list[list.length - 1]?.id} statusLine={statusLine} />
            ))}
            <div className="h-2" />
          </div>
        )}
      </div>

      <ChatInput isStreaming={isStreaming} onSend={handleSend} onStop={handleStop} showSuggestions={isEmpty} autoFocus />
    </div>
  )
}

function MessageRow({ message, isStreaming, statusLine }: { message: ChatMessage; isStreaming: boolean; statusLine: string | null }) {
  if (message.role === "user") {
    const text = message.parts.map((p) => (p.kind === "text" ? p.text : "")).join("")
    return <AgentUserMessageBubble messageId={message.id} textContent={text} />
  }

  const last = message.parts[message.parts.length - 1]
  const showStatus = isStreaming && statusLine && !(last && last.kind === "text")
  const showIdle = isStreaming && message.parts.length === 0 && !statusLine

  return (
    <div className="space-y-1.5" data-message-id={message.id}>
      {message.parts.map((part, i) => {
        const isLast = i === message.parts.length - 1
        if (part.kind === "text") {
          return (
            <div key={i} className="px-2 py-1">
              <Markdown content={part.text} isStreaming={isStreaming && isLast} />
            </div>
          )
        }
        if (part.kind === "tool") return <AgentToolCall key={part.id || i} part={part} />
        // thinking: live only while it is the newest part of a streaming reply
        return <AgentThinkingTool key={i} text={part.text} isStreaming={isStreaming && isLast && !statusLine} />
      })}
      {showStatus && <StatusLine text={statusLine} />}
      {showIdle && <StatusLine text="Thinking" />}
      {message.error && (
        <div className="mx-2 rounded-lg border border-destructive/40 bg-destructive/10 px-3 py-2 text-xs text-destructive">
          {message.error}
        </div>
      )}
      {!isStreaming && message.usage && (
        <div className="flex justify-end px-2">
          <AgentMessageUsage
            metadata={{
              model: message.usage.model,
              inputTokens: message.usage.input_tokens,
              outputTokens: message.usage.output_tokens,
              totalTokens: message.usage.total_tokens,
              durationMs: message.usage.duration_ms,
            }}
          />
        </div>
      )}
    </div>
  )
}

function EmptyThread({ onPick }: { onPick: (text: string) => void }) {
  return (
    <div className="h-full flex items-center justify-center px-4">
      <div className="max-w-md w-full text-center space-y-5">
        <div className="mx-auto w-10 h-10">
          <ScoutMark />
        </div>
        <div className="space-y-1.5">
          <h1 className="text-lg font-medium">What are you entering?</h1>
          <p className="text-sm text-muted-foreground">
            Name a Devpost hackathon and Scout pulls its rubric, enumerates the field, and shortlists ideas from
            the winners corpus. Every number is measured or quoted — nothing invented.
          </p>
        </div>
        <div className="flex flex-wrap justify-center gap-1.5">
          {SUGGESTIONS.map((s) => (
            <button
              key={s}
              type="button"
              onClick={() => onPick(s)}
              className="rounded-full border border-border bg-background px-3 py-1.5 text-xs text-muted-foreground hover:text-foreground hover:bg-foreground/5 transition-[background-color,color,transform] duration-150 ease-out active:scale-[0.97]"
            >
              {s}
            </button>
          ))}
        </div>
      </div>
    </div>
  )
}
