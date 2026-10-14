import { useEffect } from "react"
import { AgentsLayout } from "./features/layout/agents-layout"
import { useApp, viewFromHash } from "./store"
import { WorkspaceProvider } from "./workspace-context"

export function App() {
  const loadHealth = useApp((s) => s.loadHealth)
  const loadChats = useApp((s) => s.loadChats)
  useEffect(() => {
    void loadHealth()
    void loadChats()
  }, [loadHealth, loadChats])
  useEffect(() => {
    const syncRoute = () => useApp.setState({ view: viewFromHash() })
    window.addEventListener("hashchange", syncRoute)
    window.addEventListener("popstate", syncRoute)
    return () => { window.removeEventListener("hashchange", syncRoute); window.removeEventListener("popstate", syncRoute) }
  }, [])
  return <WorkspaceProvider><AgentsLayout /></WorkspaceProvider>
}
