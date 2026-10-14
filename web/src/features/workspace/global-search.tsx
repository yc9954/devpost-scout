import { useEffect, useMemo, useState } from "react"
import { Archive, BookOpen, CheckSquare2, FileText, FolderKanban, Search } from "lucide-react"
import { Dialog, DialogContent, DialogDescription, DialogHeader, DialogTitle } from "../../components/ui/dialog"
import { Input } from "../../components/ui/input"
import { historyApi } from "../../history"
import type { ImportedNoteSummary } from "../../history"
import { useWorkspace } from "../../workspace-context"

export function GlobalSearch({ open, onOpenChange, onNavigate }: { open: boolean; onOpenChange: (open: boolean) => void; onNavigate?: () => void }) {
  const { projects, pages, tasks, studies } = useWorkspace()
  const [query, setQuery] = useState("")
  const [notes, setNotes] = useState<ImportedNoteSummary[]>([])
  const [historyTotal, setHistoryTotal] = useState(0)
  useEffect(() => {
    const keydown = (event: KeyboardEvent) => {
      if ((event.metaKey || event.ctrlKey) && event.key.toLowerCase() === "k") { event.preventDefault(); onOpenChange(true) }
    }
    window.addEventListener("keydown", keydown)
    return () => window.removeEventListener("keydown", keydown)
  }, [onOpenChange])
  useEffect(() => {
    if (!open || query.trim().length < 2) { setNotes([]); setHistoryTotal(0); return }
    let alive = true
    const timer = window.setTimeout(() => {
      void historyApi.search({ q: query.trim(), source: "", kind: "", scope: "mine", offset: 0 })
        .then((result) => { if (alive) { setNotes(result.items.slice(0, 5)); setHistoryTotal(result.total) } })
        .catch(() => { if (alive) { setNotes([]); setHistoryTotal(0) } })
    }, 220)
    return () => { alive = false; window.clearTimeout(timer) }
  }, [open, query])
  const matched = useMemo(() => {
    const q = query.trim().toLowerCase()
    if (!q) return []
    return [
      ...projects.filter((item) => `${item.title} ${item.description}`.toLowerCase().includes(q)).map((item) => ({ id: item.id, title: item.title, kind: "Project", path: `#/projects/${item.id}`, icon: <FolderKanban className="h-4 w-4" /> })),
      ...pages.filter((item) => `${item.title} ${item.body}`.toLowerCase().includes(q)).map((item) => ({ id: item.id, title: item.title, kind: item.kind === "folder" ? "Folder" : "Page", path: `#/pages/${item.id}`, icon: <FileText className="h-4 w-4" /> })),
      ...tasks.filter((item) => `${item.title} ${item.details}`.toLowerCase().includes(q)).map((item) => ({ id: item.id, title: item.title, kind: "To Do", path: `#/tasks/${item.id}`, icon: <CheckSquare2 className="h-4 w-4" /> })),
      ...studies.filter((item) => `${item.title} ${item.summary} ${item.body}`.toLowerCase().includes(q)).map((item) => ({ id: item.id, title: item.title, kind: "Study", path: `#/studies/${item.id}`, icon: <BookOpen className="h-4 w-4" /> })),
    ].slice(0, 12)
  }, [query, projects, pages, tasks, studies])
  const navigate = (path: string) => { window.location.hash = path; onOpenChange(false); onNavigate?.() }
  return <Dialog open={open} onOpenChange={onOpenChange}><DialogContent className="!max-w-2xl max-h-[85vh] overflow-y-auto"><DialogHeader><DialogTitle>Search workspace</DialogTitle><DialogDescription>Search projects, pages, to dos, study items, and your collected notes.</DialogDescription></DialogHeader>
    <div className="relative"><Search className="h-4 w-4 absolute left-3 top-2.5 text-muted-foreground" /><Input autoFocus aria-label="Search workspace" className="pl-9" placeholder="Search everything…" value={query} onChange={(event) => setQuery(event.target.value)} /></div>
    {query.trim() && <div className="space-y-4"><section><h3 className="text-xs font-semibold text-muted-foreground mb-2">Workspace items</h3><div className="rounded-lg border divide-y divide-border/60">{matched.length ? matched.map((item) => <button type="button" key={`${item.kind}-${item.id}`} className="w-full flex items-center gap-3 px-3 py-2.5 text-left hover:bg-foreground/5" onClick={() => navigate(item.path)}><span className="text-blue-400">{item.icon}</span><span className="flex-1 truncate text-sm">{item.title}</span><span className="text-[11px] text-muted-foreground">{item.kind}</span></button>) : <p className="p-3 text-xs text-muted-foreground">No matching workspace items.</p>}</div></section>
      {query.trim().length >= 2 && <section><div className="flex items-center justify-between mb-2"><h3 className="text-xs font-semibold text-muted-foreground">Collected notes · {historyTotal}</h3><button type="button" className="text-xs text-blue-400 hover:underline" onClick={() => navigate("#/history")}>Open full archive</button></div><div className="rounded-lg border divide-y divide-border/60">{notes.length ? notes.map((note) => <button type="button" key={note.id} className="w-full flex items-center gap-3 px-3 py-2.5 text-left hover:bg-foreground/5" onClick={() => navigate(`#/history/${note.id}`)}><Archive className="h-4 w-4 text-muted-foreground" /><span className="flex-1 truncate text-sm">{note.title}</span><span className="text-[11px] text-muted-foreground">{note.source}</span></button>) : <p className="p-3 text-xs text-muted-foreground">No matching notes.</p>}</div></section>}</div>}
  </DialogContent></Dialog>
}
