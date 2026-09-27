// Adapted from 1code `features/layout/agents-layout.tsx` (Apache-2.0).
// Dropped: jotai atoms, tRPC, Electron window/fullscreen, login modals, hotkey manager,
// resizable sidebar (needed a jotai atom). Kept: the shell structure and class names.

import { useCallback, useState } from "react"
import { Toaster } from "sonner"
import { TooltipProvider } from "../../components/ui/tooltip"
import { AgentsSidebar } from "../sidebar/agents-sidebar"
import { ChatView } from "../chat/chat-view"
import { DashboardView } from "../dashboard/dashboard-view"
import { useApp } from "../../store"
import { cn } from "../../lib/utils"
import { IconOpenSidebar } from "../../components/ui/icons"
import { Button } from "../../components/ui/button"

const SIDEBAR_WIDTH = 240

export function AgentsLayout() {
  const view = useApp((s) => s.view)
  const [sidebarOpen, setSidebarOpen] = useState(true)
  const handleCloseSidebar = useCallback(() => setSidebarOpen(false), [])

  return (
    <TooltipProvider delayDuration={300}>
      <div className="flex flex-col w-full h-screen relative overflow-hidden bg-background select-none">
        <div className="flex flex-1 overflow-hidden">
          {/* Left Sidebar */}
          <div
            className={cn(
              "overflow-hidden bg-background border-r flex-shrink-0 transition-[width] duration-150 ease-out",
            )}
            style={{ width: sidebarOpen ? SIDEBAR_WIDTH : 0, borderRightWidth: sidebarOpen ? "0.5px" : 0 }}
          >
            <div className="h-full" style={{ width: SIDEBAR_WIDTH }}>
              <AgentsSidebar onToggleSidebar={handleCloseSidebar} />
            </div>
          </div>

          {/* Main Content */}
          <div className="flex-1 overflow-hidden flex flex-col min-w-0 relative">
            {!sidebarOpen && (
              <div className="absolute left-2 top-2 z-30">
                <Button
                  variant="ghost"
                  size="icon"
                  onClick={() => setSidebarOpen(true)}
                  className="h-6 w-6 p-0 hover:bg-foreground/10 transition-[background-color,transform] duration-150 ease-out active:scale-[0.97] text-muted-foreground hover:text-foreground rounded-md"
                  aria-label="Open sidebar"
                >
                  <IconOpenSidebar className="h-4 w-4" />
                </Button>
              </div>
            )}
            {view === "dashboard" ? <DashboardView /> : <ChatView />}
          </div>
        </div>
      </div>
      <Toaster position="bottom-right" theme="dark" closeButton />
    </TooltipProvider>
  )
}
