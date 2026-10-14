// Workspace routes inside the original 1code sidebar shell (Apache-2.0).

import { useCallback, useEffect, useState } from "react"
import { Toaster } from "sonner"
import { TooltipProvider } from "../../components/ui/tooltip"
import { AgentsSidebar } from "../sidebar/agents-sidebar"
import { GlobalSearch } from "../workspace/global-search"
import { ChatView } from "../chat/chat-view"
import { DashboardView } from "../dashboard/dashboard-view"
import { OverviewView } from "../workspace/overview-view"
import { ProjectsView } from "../workspace/projects-view"
import { PagesView } from "../workspace/pages-view"
import { TasksView } from "../workspace/tasks-view"
import { StudiesView } from "../workspace/studies-view"
import { HistoryView } from "../workspace/history-view"
import { AgentsView } from "../workspace/agents-view"
import { CodexView } from "../workspace/codex-view"
import { StudioView } from "../workspace/studio-view"
import { useApp } from "../../store"
import { cn } from "../../lib/utils"
import { IconOpenSidebar } from "../../components/ui/icons"
import { Button } from "../../components/ui/button"

const SIDEBAR_WIDTH = 240

export function AgentsLayout() {
  const view = useApp((s) => s.view)
  const [isMobile, setIsMobile] = useState(() => window.innerWidth < 768)
  const [sidebarOpen, setSidebarOpen] = useState(() => window.innerWidth >= 768)
  const [searchOpen, setSearchOpen] = useState(false)
  const closeSidebar = useCallback(() => setSidebarOpen(false), [])

  useEffect(() => {
    const update = () => {
      const mobile = window.innerWidth < 768
      setIsMobile((previous) => {
        if (previous !== mobile) setSidebarOpen(!mobile)
        return mobile
      })
    }
    window.addEventListener("resize", update)
    return () => window.removeEventListener("resize", update)
  }, [])

  return (
    <TooltipProvider delayDuration={300}>
      <div className="relative flex h-screen w-full flex-col overflow-hidden bg-background select-none">
        <div className="flex min-h-0 flex-1 overflow-hidden">
          {sidebarOpen && isMobile && <button type="button" aria-label="Close navigation" className="absolute inset-0 z-30 bg-black/40" onClick={closeSidebar} />}
          <div
            className={cn("z-20 flex-shrink-0 overflow-hidden border-r bg-background transition-[width] duration-150 ease-out", isMobile && "absolute inset-y-0 left-0 z-40 shadow-xl")}
            style={{ width: sidebarOpen ? SIDEBAR_WIDTH : 0, borderRightWidth: sidebarOpen ? "0.5px" : 0 }}
          >
            <div className="h-full" style={{ width: SIDEBAR_WIDTH }}>
              <AgentsSidebar
                onToggleSidebar={closeSidebar}
                onNavigate={isMobile ? closeSidebar : undefined}
                onSearch={() => setSearchOpen(true)}
              />
            </div>
          </div>

          <div className="relative flex min-w-0 flex-1 flex-col overflow-hidden">
            {!sidebarOpen && (
              <div className="absolute left-2 top-2 z-30">
                <Button
                  variant="ghost"
                  size="icon"
                  onClick={() => setSidebarOpen(true)}
                  className="h-6 w-6 rounded-md p-0 text-muted-foreground transition-[background-color,transform] duration-150 ease-out hover:bg-foreground/10 hover:text-foreground active:scale-[0.97]"
                  aria-label="Open sidebar"
                >
                  <IconOpenSidebar className="h-4 w-4" />
                </Button>
              </div>
            )}
            {view === "overview" && <OverviewView />}
            {view === "projects" && <ProjectsView />}
            {view === "pages" && <PagesView />}
            {view === "tasks" && <TasksView />}
            {view === "studies" && <StudiesView />}
            {view === "history" && <HistoryView />}
            {view === "agents" && <AgentsView />}
            {view === "codex" && <CodexView />}
            {view === "studio" && <StudioView />}
            {view === "dashboard" && <DashboardView />}
            {view === "hackathon-study" && <StudiesView category="hackathon" />}
            {view === "chat" && <ChatView />}
          </div>
        </div>
      </div>
      <Toaster position="bottom-right" theme="light" closeButton />
      <GlobalSearch open={searchOpen} onOpenChange={setSearchOpen} onNavigate={isMobile ? closeSidebar : undefined} />
    </TooltipProvider>
  )
}
