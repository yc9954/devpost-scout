import { useEffect } from "react"
import { AgentsLayout } from "./features/layout/agents-layout"
import { useApp } from "./store"

export function App() {
  const loadHealth = useApp((s) => s.loadHealth)
  const loadChats = useApp((s) => s.loadChats)
  useEffect(() => {
    void loadHealth()
    void loadChats()
  }, [loadHealth, loadChats])
  return <AgentsLayout />
}
