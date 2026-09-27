// Adapted from 1code `features/sidebar/agents-sidebar.tsx` (Apache-2.0).
// The original is a 3.5k-line workspace list wired to jotai + tRPC + Electron. This keeps its
// visual structure and class names — header row with logo, search + "New" button, nav links,
// scrollable list with TypewriterText rows, footer — over the Scout store instead.

import { memo, useCallback, useMemo, useRef, useState } from "react"
import { LayoutGrid, MessageSquare } from "lucide-react"
import { cn } from "../../lib/utils"
import { formatTimeAgo } from "../../lib/utils/format-time-ago"
import { useApp } from "../../store"
import { Button } from "../../components/ui/button"
import { Input } from "../../components/ui/input"
import { Kbd } from "../../components/ui/kbd"
import { Skeleton } from "../../components/ui/skeleton"
import { TypewriterText } from "../../components/ui/typewriter-text"
import { Tooltip, TooltipContent, TooltipTrigger } from "../../components/ui/tooltip"
import { IconDoubleChevronLeft, LoadingDot } from "../../components/ui/icons"
import { ModeBadge } from "./mode-badge"

interface AgentsSidebarProps {
  onToggleSidebar?: () => void
}

export function AgentsSidebar({ onToggleSidebar }: AgentsSidebarProps) {
  const chats = useApp((s) => s.chats)
  const chatsLoading = useApp((s) => s.chatsLoading)
  const activeChatId = useApp((s) => s.activeChatId)
  const view = useApp((s) => s.view)
  const streaming = useApp((s) => s.streaming)
  const openChat = useApp((s) => s.openChat)
  const newChat = useApp((s) => s.newChat)
  const setView = useApp((s) => s.setView)

  const [searchQuery, setSearchQuery] = useState("")
  const searchInputRef = useRef<HTMLInputElement>(null)
  const justCreatedRef = useRef<Set<string>>(new Set())

  const filteredChats = useMemo(() => {
    const q = searchQuery.trim().toLowerCase()
    if (!q) return chats
    return chats.filter((c) => (c.title || "").toLowerCase().includes(q))
  }, [chats, searchQuery])

  const handleNewChat = useCallback(async () => {
    const id = await newChat()
    justCreatedRef.current.add(id)
  }, [newChat])

  const handleChatClick = useCallback(
    (id: string) => {
      void openChat(id)
    },
    [openChat],
  )

  return (
    <div className="flex flex-col h-full bg-background">
      {/* Header — logo + collapse control (1code: team button row) */}
      <div className="px-2 pt-2 pb-2">
        <div className="flex items-center gap-1">
          <div className="flex-1 min-w-0">
            <div className="h-6 px-1.5 flex items-center gap-1.5 min-w-0 max-w-full">
              <div className="flex items-center justify-center flex-shrink-0">
                <ScoutMark className="w-3.5 h-3.5" />
              </div>
              <div className="text-sm font-medium text-foreground truncate">Scout</div>
            </div>
          </div>
          <Tooltip delayDuration={500}>
            <TooltipTrigger asChild>
              <Button
                variant="ghost"
                size="icon"
                onClick={onToggleSidebar}
                className="h-6 w-6 p-0 hover:bg-foreground/10 transition-[background-color,transform] duration-150 ease-out active:scale-[0.97] text-foreground flex-shrink-0 rounded-md"
                aria-label="Close sidebar"
              >
                <IconDoubleChevronLeft className="h-4 w-4" />
              </Button>
            </TooltipTrigger>
            <TooltipContent side="right">Close sidebar</TooltipContent>
          </Tooltip>
        </div>
      </div>

      {/* Search + New chat (1code: "New Workspace") */}
      <div className="px-2 pb-3 flex-shrink-0">
        <div className="space-y-2">
          <div className="relative">
            <Input
              ref={searchInputRef}
              placeholder="Search chats..."
              value={searchQuery}
              onChange={(e) => setSearchQuery(e.target.value)}
              onKeyDown={(e) => {
                if (e.key === "Escape") {
                  e.preventDefault()
                  searchInputRef.current?.blur()
                }
              }}
              className="w-full rounded-lg text-sm bg-muted border border-input placeholder:text-muted-foreground/40 h-7"
            />
          </div>
          <Tooltip delayDuration={500}>
            <TooltipTrigger asChild>
              <Button
                onClick={handleNewChat}
                variant="outline"
                size="sm"
                className="px-2 w-full hover:bg-foreground/10 transition-[background-color,transform] duration-150 ease-out active:scale-[0.97] text-foreground rounded-lg gap-1.5 h-7"
              >
                <span className="text-sm font-medium">New chat</span>
              </Button>
            </TooltipTrigger>
            <TooltipContent side="right" className="flex flex-col items-start gap-1">
              <span>Start a new chat</span>
              <span className="flex items-center gap-1.5">
                <Kbd>⌘N</Kbd>
              </span>
            </TooltipContent>
          </Tooltip>
        </div>
      </div>

      {/* Navigation Links (1code: Inbox & Automations) */}
      <div className="px-2 pb-3 flex-shrink-0 space-y-0.5 -mx-1">
        <NavButton
          active={view === "chat"}
          onClick={() => setView("chat")}
          icon={<MessageSquare className="h-4 w-4" />}
          label="Chat"
        />
        <NavButton
          active={view === "dashboard"}
          onClick={() => setView("dashboard")}
          icon={<LayoutGrid className="h-4 w-4" />}
          label="Dashboard"
        />
      </div>

      {/* Scrollable chat list */}
      <div className="flex-1 min-h-0 relative">
        <div className="h-full overflow-y-auto scrollbar-thin scrollbar-thumb-muted-foreground/20 scrollbar-track-transparent px-2">
          <div className="mb-4 -mx-1">
            <div className="flex items-center h-4 mb-1 pl-2">
              <h3 className="text-xs font-medium text-muted-foreground whitespace-nowrap">Chats</h3>
            </div>
            {chatsLoading && chats.length === 0 ? (
              <div className="space-y-1 px-2 pt-1">
                {[0, 1, 2].map((i) => (
                  <Skeleton key={i} className="h-7 w-full" />
                ))}
              </div>
            ) : filteredChats.length === 0 ? (
              <div className="px-2 py-3 text-xs text-muted-foreground/60">
                {searchQuery ? "No chats match." : "No chats yet. Ask something below."}
              </div>
            ) : (
              <div className="list-none p-0 m-0">
                {filteredChats.map((chat) => (
                  <ChatItem
                    key={chat.id}
                    chatId={chat.id}
                    chatName={chat.title}
                    updatedAt={chat.updated_at || chat.created_at}
                    isSelected={view === "chat" && activeChatId === chat.id}
                    isLoading={!!streaming[chat.id]}
                    isJustCreated={justCreatedRef.current.has(chat.id)}
                    onChatClick={handleChatClick}
                  />
                ))}
              </div>
            )}
          </div>
        </div>
      </div>

      {/* Footer — mode badge from /api/health */}
      <div className="p-2 pt-2 flex flex-col gap-2 flex-shrink-0 border-t" style={{ borderTopWidth: "0.5px" }}>
        <ModeBadge />
      </div>
    </div>
  )
}

function NavButton({
  active,
  onClick,
  icon,
  label,
}: {
  active: boolean
  onClick: () => void
  icon: React.ReactNode
  label: string
}) {
  return (
    <button
      type="button"
      onClick={onClick}
      className={cn(
        "flex items-center gap-2.5 w-full pl-2 pr-2 py-1.5 rounded-md text-sm transition-colors duration-150",
        active ? "bg-foreground/5 text-foreground" : "text-muted-foreground hover:bg-foreground/5 hover:text-foreground",
      )}
    >
      {icon}
      <span className="flex-1 text-left">{label}</span>
    </button>
  )
}

interface ChatItemProps {
  chatId: string
  chatName: string
  updatedAt?: string
  isSelected: boolean
  isLoading: boolean
  isJustCreated: boolean
  onChatClick: (id: string) => void
}

const ChatItem = memo(function ChatItem({
  chatId,
  chatName,
  updatedAt,
  isSelected,
  isLoading,
  isJustCreated,
  onChatClick,
}: ChatItemProps) {
  return (
    <div
      role="button"
      tabIndex={0}
      onClick={() => onChatClick(chatId)}
      onKeyDown={(e) => {
        if (e.key === "Enter" || e.key === " ") {
          e.preventDefault()
          onChatClick(chatId)
        }
      }}
      className={cn(
        "w-full text-left py-1.5 cursor-pointer group relative",
        "transition-colors duration-75",
        "outline-offset-2 focus-visible:outline focus-visible:outline-2 focus-visible:outline-ring/70",
        "pl-2 pr-2 rounded-md",
        isSelected ? "bg-foreground/5 text-foreground" : "text-muted-foreground hover:bg-foreground/5 hover:text-foreground",
      )}
    >
      <div className="flex items-start gap-2.5">
        <div className="pt-0.5">
          <div className="relative flex-shrink-0 w-4 h-4 flex items-center justify-center">
            {isLoading ? (
              <LoadingDot isLoading={true} className="w-2.5 h-2.5 text-muted-foreground" />
            ) : (
              <MessageSquare className="w-3.5 h-3.5 text-muted-foreground/70" />
            )}
          </div>
        </div>
        <div className="flex-1 min-w-0 flex flex-col gap-0.5">
          <div className="flex items-center gap-1">
            <span className="truncate block text-sm leading-tight flex-1">
              <TypewriterText text={chatName || ""} placeholder="New chat" id={chatId} isJustCreated={isJustCreated} showPlaceholder />
            </span>
          </div>
          <div className="flex items-center justify-between gap-2">
            <span className="text-[11px] text-muted-foreground/60 truncate">
              {isLoading ? <span className="text-blue-500">Working</span> : "Chat"}
            </span>
            <span className="text-[11px] text-muted-foreground/60 flex-shrink-0">{formatTimeAgo(updatedAt)}</span>
          </div>
        </div>
      </div>
    </div>
  )
})

/** Scout's own mark, drawn in the same 400-unit box as 1code's `Logo`. */
export function ScoutMark({ className }: { className?: string }) {
  return (
    <svg viewBox="0 0 400 400" fill="none" xmlns="http://www.w3.org/2000/svg" className={cn("w-full h-full", className)} aria-label="Scout">
      <rect width="400" height="400" rx="88" fill="hsl(var(--primary))" />
      <circle cx="180" cy="180" r="84" stroke="white" strokeWidth="36" />
      <path d="M244 244L318 318" stroke="white" strokeWidth="36" strokeLinecap="round" />
    </svg>
  )
}
