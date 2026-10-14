// Adapted from 1code's agents-sidebar.tsx (Apache-2.0). Workspace routes use its
// 240px single-column header, navigation rows, recent-chat list, and footer.

import { useEffect, useMemo, useState } from "react"
import { Archive, BookOpen, Bot, CheckSquare2, FileText, FolderKanban, Home, LayoutGrid, MessageSquare, Video } from "lucide-react"
import { cn } from "../../lib/utils"
import { formatTimeAgo } from "../../lib/utils/format-time-ago"
import { useApp } from "../../store"
import { useHashRoute } from "../../use-hash-route"
import { codexApi, type CodexChatSummary } from "../../codex"
import { Button } from "../../components/ui/button"
import { Kbd } from "../../components/ui/kbd"
import { Skeleton } from "../../components/ui/skeleton"
import { Tooltip, TooltipContent, TooltipTrigger } from "../../components/ui/tooltip"
import { IconDoubleChevronLeft, LoadingDot } from "../../components/ui/icons"
import { NewPageDialog } from "../workspace/pages-view"
import { ModeBadge } from "./mode-badge"
import { ScoutMark } from "./scout-mark"

interface AgentsSidebarProps {
  onToggleSidebar?: () => void
  onNavigate?: () => void
  onSearch: () => void
}

export function AgentsSidebar({ onToggleSidebar, onNavigate, onSearch }: AgentsSidebarProps) {
  const hash = useHashRoute()
  const chats = useApp((state) => state.chats)
  const chatsLoading = useApp((state) => state.chatsLoading)
  const streaming = useApp((state) => state.streaming)
  const openChat = useApp((state) => state.openChat)
  const [codexChats, setCodexChats] = useState<CodexChatSummary[]>([])
  const [newPageOpen, setNewPageOpen] = useState(false)

  useEffect(() => {
    const refresh = () => { void codexApi.chats().then(setCodexChats).catch(() => setCodexChats([])) }
    refresh()
    window.addEventListener("workspace:codex-chats-updated", refresh)
    return () => window.removeEventListener("workspace:codex-chats-updated", refresh)
  }, [])

  const recent = useMemo(() => [
    ...codexChats.map((chat) => ({ key: `codex-${chat.id}`, kind: "codex" as const, id: chat.id, title: chat.title || "New chat", updated: chat.updated_at || chat.created_at })),
    ...chats.map((chat) => ({ key: `scout-${chat.id}`, kind: "scout" as const, id: chat.id, title: chat.title || "New chat", updated: chat.updated || chat.updated_at || chat.created || chat.created_at })),
  ].sort((a, b) => (b.updated ?? "").localeCompare(a.updated ?? "")).slice(0, 6), [codexChats, chats])

  const navigate = (target: string) => { window.location.hash = target; onNavigate?.() }
  const visitChat = (kind: "codex" | "scout", id: string) => {
    if (kind === "codex") navigate(`#/codex/${id}`)
    else { void openChat(id); onNavigate?.() }
  }

  return <div className="flex h-full flex-col bg-background">
    <div className="px-2 pb-2 pt-2">
      <div className="flex items-center gap-1">
        <div className="min-w-0 flex-1">
          <div className="flex h-6 max-w-full min-w-0 items-center gap-1.5 px-1.5">
            <ScoutMark className="h-3.5 w-3.5 flex-shrink-0" />
            <span className="truncate text-sm font-medium text-foreground">Workspace</span>
          </div>
        </div>
        <Tooltip delayDuration={500}>
          <TooltipTrigger asChild>
            <Button variant="ghost" size="icon" onClick={onToggleSidebar} className="h-6 w-6 flex-shrink-0 rounded-md p-0 text-foreground transition-[background-color,transform] duration-150 ease-out hover:bg-foreground/10 active:scale-[0.97]" aria-label="Close sidebar"><IconDoubleChevronLeft className="h-4 w-4" /></Button>
          </TooltipTrigger>
          <TooltipContent side="right">Close sidebar</TooltipContent>
        </Tooltip>
      </div>
    </div>

    <div className="flex-shrink-0 space-y-2 px-2 pb-3">
      <button type="button" onClick={onSearch} className="flex h-7 w-full items-center rounded-lg border border-input bg-muted px-2 text-left text-sm text-muted-foreground/70 hover:text-foreground" aria-label="Search workspace"><span className="min-w-0 flex-1 truncate">Search workspace...</span><Kbd>⌘K</Kbd></button>
      <Button onClick={() => setNewPageOpen(true)} variant="outline" size="sm" className="h-7 w-full gap-1.5 rounded-lg px-2 text-foreground transition-[background-color,transform] duration-150 ease-out hover:bg-foreground/10 active:scale-[0.97]"><span className="text-sm font-medium">New page</span></Button>
    </div>

    <div className="min-h-0 flex-1 overflow-y-auto px-2 scrollbar-thin scrollbar-thumb-muted-foreground/20 scrollbar-track-transparent">
      <SidebarSection title="Workspace">
        <NavButton label="Home" icon={<Home className="h-4 w-4" />} active={!hash || hash === "#/overview"} onClick={() => navigate("#/overview")} />
        <NavButton label="Projects" icon={<FolderKanban className="h-4 w-4" />} active={hash.startsWith("#/projects")} onClick={() => navigate("#/projects")} />
        <NavButton label="To Do" icon={<CheckSquare2 className="h-4 w-4" />} active={hash.startsWith("#/tasks")} onClick={() => navigate("#/tasks")} />
        <NavButton label="Learning" icon={<BookOpen className="h-4 w-4" />} active={hash.startsWith("#/studies")} onClick={() => navigate("#/studies")} />
        <NavButton label="Pages" icon={<FileText className="h-4 w-4" />} active={hash.startsWith("#/pages")} onClick={() => navigate("#/pages")} />
        <NavButton label="Collected notes" icon={<Archive className="h-4 w-4" />} active={hash.startsWith("#/history")} onClick={() => navigate("#/history")} />
      </SidebarSection>

      <SidebarSection title="Tools">
        <NavButton label="Agents" icon={<LayoutGrid className="h-4 w-4" />} active={hash.startsWith("#/agents")} onClick={() => navigate("#/agents")} />
        <NavButton label="Codex" icon={<Bot className="h-4 w-4" />} active={hash.startsWith("#/codex")} onClick={() => navigate("#/codex")} />
        <NavButton label="Devpost Scout" icon={<ScoutMark className="h-4 w-4" />} active={hash.startsWith("#/dashboard")} onClick={() => navigate("#/dashboard")} />
        <NavButton label="Scout chat" icon={<MessageSquare className="h-4 w-4" />} active={hash.startsWith("#/chat")} onClick={() => { void openChat(null); onNavigate?.() }} />
        <NavButton label="Hackathon study" icon={<BookOpen className="h-4 w-4" />} active={hash.startsWith("#/hackathon-study")} onClick={() => navigate("#/hackathon-study")} />
        <NavButton label="Screen Studio" icon={<Video className="h-4 w-4" />} active={hash.startsWith("#/studio")} onClick={() => navigate("#/studio")} />
      </SidebarSection>

      <SidebarSection title="Recent chats">
        {chatsLoading && recent.length === 0 ? <div className="space-y-1 px-2 pt-1">{[0, 1, 2].map((index) => <Skeleton key={index} className="h-7 w-full" />)}</div> : recent.length === 0 ? <p className="px-2 py-3 text-xs text-muted-foreground/60">Conversations appear here.</p> : recent.map((chat) => <button key={chat.key} type="button" onClick={() => visitChat(chat.kind, chat.id)} className={cn("group w-full cursor-pointer rounded-md px-2 py-1.5 text-left transition-colors duration-75 focus-visible:outline focus-visible:outline-2 focus-visible:outline-ring/70", hash === `#/${chat.kind === "codex" ? "codex" : "chat"}/${chat.id}` ? "bg-foreground/5 text-foreground" : "text-muted-foreground hover:bg-foreground/5 hover:text-foreground")}>
          <span className="flex items-start gap-2.5"><span className="relative flex h-4 w-4 flex-shrink-0 items-center justify-center pt-0.5">{chat.kind === "scout" && streaming[chat.id] ? <LoadingDot isLoading className="h-2.5 w-2.5 text-muted-foreground" /> : <MessageSquare className="h-3.5 w-3.5 text-muted-foreground/70" />}</span><span className="min-w-0 flex-1"><span className="block truncate text-sm leading-tight">{chat.title}</span><span className="mt-0.5 flex items-center justify-between gap-2 text-[11px] text-muted-foreground/60"><span>{chat.kind === "codex" ? "Codex" : "Scout"}</span><span>{formatTimeAgo(chat.updated)}</span></span></span></span>
        </button>)}
      </SidebarSection>

    </div>

    <div className="flex flex-shrink-0 flex-col gap-2 border-t p-2 pt-2" style={{ borderTopWidth: "0.5px" }}><ModeBadge /></div>
    <NewPageDialog open={newPageOpen} onOpenChange={setNewPageOpen} onCreated={(page) => { navigate(`#/pages/${page.id}`) }} />
  </div>
}

function SidebarSection({ title, children }: { title: string; children: React.ReactNode }) {
  return <section className="mb-4 -mx-1"><div className="mb-1 flex h-4 items-center pl-2"><h3 className="whitespace-nowrap text-xs font-medium text-muted-foreground">{title}</h3></div><div className="space-y-0.5">{children}</div></section>
}

function NavButton({ label, icon, active, onClick }: { label: string; icon: React.ReactNode; active: boolean; onClick: () => void }) {
  return <button type="button" onClick={onClick} className={cn("flex w-full items-center gap-2.5 rounded-md py-1.5 pl-2 pr-2 text-sm transition-colors duration-150", active ? "bg-foreground/5 text-foreground" : "text-muted-foreground hover:bg-foreground/5 hover:text-foreground")}>{icon}<span className="min-w-0 flex-1 truncate text-left">{label}</span></button>
}
