import { useEffect, useState } from "react"
import { ArrowLeft, ArrowRight, BookOpen, CheckSquare2, ExternalLink, FolderKanban, Search } from "lucide-react"
import { toast } from "sonner"
import { Button } from "../../components/ui/button"
import { Dialog, DialogContent, DialogDescription, DialogHeader, DialogTitle } from "../../components/ui/dialog"
import { Input } from "../../components/ui/input"
import { historyApi } from "../../history"
import type { ImportPage, ImportStats, ImportedNote } from "../../history"
import { useWorkspace } from "../../workspace-context"
import { selectClass, StatePill, Surface, WorkspacePage } from "./workspace-ui"

const sourceNames: Record<string, string> = { kakao: "KakaoTalk", slack: "Slack · self DM", codex: "Codex prompt", claude: "Claude prompt", "codex-history": "Codex CLI history", "claude-history": "Claude CLI history", "codex-result": "Codex result", "claude-result": "Claude result" }
const kindNames: Record<string, string> = { note: "Note", idea: "Idea", action: "Action", study: "Study", link: "Link", result: "Result" }

export function HistoryView() {
  const [stats, setStats] = useState<ImportStats | null>(null)
  const [page, setPage] = useState<ImportPage | null>(null)
  const [query, setQuery] = useState("")
  const [scope, setScope] = useState("mine")
  const [source, setSource] = useState("")
  const [kind, setKind] = useState("")
  const [offset, setOffset] = useState(0)
  const [selected, setSelected] = useState<ImportedNote | null>(null)
  const [loading, setLoading] = useState(false)
  const [saving, setSaving] = useState(false)
  const { createProject, createTask, createStudy } = useWorkspace()

  useEffect(() => { void historyApi.stats().then(setStats).catch((error) => toast.error(String(error))) }, [])
  useEffect(() => {
    const syncSelection = () => {
      const id = window.location.hash.match(/^#\/history\/([a-f0-9]{32})$/)?.[1]
      if (id) void historyApi.get(id).then(setSelected).catch((error) => toast.error(String(error)))
      else setSelected(null)
    }
    syncSelection()
    window.addEventListener("popstate", syncSelection)
    window.addEventListener("hashchange", syncSelection)
    return () => { window.removeEventListener("popstate", syncSelection); window.removeEventListener("hashchange", syncSelection) }
  }, [])
  useEffect(() => {
    let active = true
    setLoading(true)
    const timer = window.setTimeout(() => {
      void historyApi.search({ q: query, source, kind, scope, offset })
        .then((data) => { if (active) setPage(data) })
        .catch((error) => { if (active) toast.error(String(error)) })
        .finally(() => { if (active) setLoading(false) })
    }, query ? 180 : 0)
    return () => { active = false; window.clearTimeout(timer) }
  }, [query, source, kind, scope, offset])

  const open = async (id: string) => {
    try { setSelected(await historyApi.get(id)); window.history.pushState(null, "", `#/history/${id}`) }
    catch (error) { toast.error(String(error)) }
  }
  const promote = async (type: "projects" | "tasks" | "studies") => {
    if (!selected || saving) return
    setSaving(true)
    try {
      const provenance = `원문: ${sourceNames[selected.source]} · ${selected.occurred_at.slice(0, 10)}${selected.source_url ? `\n${selected.source_url}` : ""}`
      const title = selected.title.slice(0, 200)
      let id: string
      if (type === "projects") {
        id = (await createProject({ title, description: `${selected.body.slice(0, 9000)}\n\n${provenance}`.slice(0, 10000), status: "planned" })).id
      } else if (type === "tasks") {
        id = (await createTask({ title, details: `${selected.body.slice(0, 19000)}\n\n${provenance}`.slice(0, 20000), status: "todo", priority: "medium", due_on: null, project_id: null, agent_id: null })).id
      } else {
        id = (await createStudy({ title, summary: selected.body.slice(0, 240), body: `${selected.body.slice(0, 99000)}\n\n${provenance}`.slice(0, 100000), status: "inbox", category: /해커톤|hackathon|devpost/i.test(selected.body) ? "hackathon" : "general", source_url: selected.urls[0] || selected.source_url, project_id: null, hackathon_host: "" })).id
      }
      const updated = await historyApi.link(selected.id, type, id)
      setSelected(updated)
      setPage((previous) => previous ? { ...previous, items: previous.items.map((item) => item.id === selected.id ? { ...item, linked_type: type, linked_id: id } : item) } : previous)
      toast.success(`${type === "projects" ? "Project" : type === "tasks" ? "To do" : "Study item"} created`)
    } catch (error) { toast.error(error instanceof Error ? error.message : String(error)) }
    finally { setSaving(false) }
  }

  return <WorkspacePage title="Collected notes" description="Your KakaoTalk notes, Slack self DM, local Codex and Claude sessions, and CLI histories since March 2026. Short notes, bare links, and agent conclusions remain searchable with their sources.">
    <div className="grid grid-cols-2 lg:grid-cols-4 gap-2">
      <Count label="Your notes" value={stats?.personal_total} />
      <Count label="Extra CLI history" value={stats?.history_total} />
      <Count label="Agent results" value={stats?.agent_total} />
      <Count label="All records" value={stats?.total} />
      <Count label="Bare links" value={stats?.personal_links} />
      <Count label="Media references" value={stats?.partial} />
      <Count label="KakaoTalk + Slack" value={stats ? (stats.sources.kakao || 0) + (stats.sources.slack || 0) : undefined} />
      <Count label="Codex + Claude" value={stats ? (stats.sources.codex || 0) + (stats.sources.claude || 0) : undefined} />
    </div>
    <div className="flex flex-wrap gap-2 items-center">
      <div className="relative flex-1 min-w-48 max-w-sm"><Search className="absolute left-3 top-2.5 h-4 w-4 text-muted-foreground" /><Input aria-label="Search collected notes" className="pl-9" placeholder="Search every note and link" value={query} onChange={(event) => { setQuery(event.target.value); setOffset(0) }} /></div>
      <select aria-label="Filter record scope" className={`${selectClass} !w-36`} value={scope} onChange={(event) => { setScope(event.target.value); setSource(""); setKind(""); setOffset(0) }}><option value="mine">Your notes</option><option value="history">CLI history</option><option value="agent">Agent results</option><option value="all">Everything</option></select>
      <select aria-label="Filter note source" className={`${selectClass} !w-44`} value={source} onChange={(event) => { setSource(event.target.value); setOffset(0) }}><option value="">All sources</option>{Object.entries(sourceNames).filter(([value]) => scope === "all" || (scope === "agent" ? value.endsWith("-result") : scope === "history" ? value.endsWith("-history") : !value.includes("-"))).map(([value, label]) => <option key={value} value={value}>{label}</option>)}</select>
      <select aria-label="Filter note kind" className={`${selectClass} !w-36`} value={kind} onChange={(event) => { setKind(event.target.value); setOffset(0) }}><option value="">All kinds</option>{Object.entries(kindNames).filter(([value]) => scope === "all" || (scope === "agent" ? value === "result" : value !== "result")).map(([value, label]) => <option key={value} value={value}>{label}</option>)}</select>
      <span className="text-xs text-muted-foreground ml-auto">{loading ? "Searching…" : `${page?.total ?? 0} results`}</span>
    </div>
    <Surface className="divide-y divide-border/70 overflow-hidden">
      {page?.items.map((note) => <button key={note.id} type="button" className="w-full text-left px-4 py-3 hover:bg-foreground/[0.035]" onClick={() => void open(note.id)}>
        <div className="flex items-center gap-2"><span className="text-sm font-medium truncate flex-1">{note.title}</span><StatePill value={kindNames[note.kind]} tone={note.kind === "action" ? "blue" : "neutral"} /></div>
        <p className="text-xs text-muted-foreground line-clamp-2 mt-1 break-words">{note.excerpt || note.urls[0] || "Attachment reference"}</p>
        <div className="flex flex-wrap gap-2 text-[11px] text-muted-foreground mt-2"><span>{sourceNames[note.source]}</span><span>{note.occurred_at.slice(0, 10)}</span>{note.urls.length > 0 && <span>🔗 {note.urls.length}</span>}{note.linked_type && <span>Saved to {note.linked_type}</span>}{note.partial === 1 && <span>Partial preview</span>}</div>
      </button>)}
      {!page?.items.length && <div className="p-8 text-center text-sm text-muted-foreground">{loading ? "Loading notes…" : "No notes match these filters."}</div>}
    </Surface>
    <div className="flex justify-between items-center text-xs text-muted-foreground"><span>{page?.total ? `${offset + 1}–${Math.min(offset + 40, page.total)} of ${page.total}` : ""}</span><div className="flex gap-2"><Button size="sm" variant="outline" disabled={offset === 0} onClick={() => setOffset(Math.max(0, offset - 40))}><ArrowLeft className="h-3.5 w-3.5 mr-1" />Previous</Button><Button size="sm" variant="outline" disabled={!page || offset + 40 >= page.total} onClick={() => setOffset(offset + 40)}>Next<ArrowRight className="h-3.5 w-3.5 ml-1" /></Button></div></div>
    <Dialog open={!!selected} onOpenChange={(value) => { if (!value) { setSelected(null); if (window.location.hash.startsWith("#/history/")) window.history.replaceState(null, "", "#/history") } }}>
      <DialogContent className="!max-w-4xl max-h-[90vh] overflow-y-auto"><DialogHeader><DialogTitle className="break-words">{selected?.title}</DialogTitle><DialogDescription>{selected ? `${sourceNames[selected.source]} · ${selected.occurred_at} · ${kindNames[selected.kind]}` : ""}</DialogDescription></DialogHeader>
        {selected && <div className="space-y-4 min-w-0">
          {selected.sensitive === 1 && <p className="text-xs text-amber-400">Credential-like text is masked in this view. The original remains in the local source archive.</p>}
          {selected.partial === 1 && <p className="text-xs text-amber-400">This record includes media or an attachment reference. Open the original chat or session to inspect the file itself.</p>}
          <pre className="whitespace-pre-wrap break-words rounded-lg border bg-muted/30 p-4 text-xs leading-relaxed select-text font-sans max-h-[50vh] overflow-auto">{selected.body}</pre>
          {selected.urls.length > 0 && <div><h3 className="text-xs font-semibold mb-2">Links ({selected.urls.length})</h3><div className="space-y-1">{selected.urls.map((url) => <a key={url} href={url} target="_blank" rel="noopener noreferrer" className="flex items-start gap-1 text-xs text-blue-400 hover:underline break-all"><ExternalLink className="h-3.5 w-3.5 mt-0.5 flex-shrink-0" />{url}</a>)}</div></div>}
          {selected.source_url && <a href={selected.source_url} target="_blank" rel="noopener noreferrer" className="inline-flex items-center gap-1 text-xs text-blue-400 hover:underline"><ExternalLink className="h-3.5 w-3.5" />Open original message</a>}
          {selected.session_path && <p className="text-[11px] text-muted-foreground break-all select-text">Local session: {selected.session_path}</p>}
          <div className="flex flex-wrap gap-2 pt-3 border-t">{selected.linked_type ? <span className="text-xs text-muted-foreground">Saved to {selected.linked_type}</span> : <><Button size="sm" variant="outline" disabled={saving} onClick={() => void promote("projects")}><FolderKanban className="h-3.5 w-3.5 mr-1" />Save as project</Button><Button size="sm" variant="outline" disabled={saving} onClick={() => void promote("tasks")}><CheckSquare2 className="h-3.5 w-3.5 mr-1" />Save as to do</Button><Button size="sm" variant="outline" disabled={saving} onClick={() => void promote("studies")}><BookOpen className="h-3.5 w-3.5 mr-1" />Save as study</Button></>}</div>
        </div>}
      </DialogContent>
    </Dialog>
  </WorkspacePage>
}

function Count({ label, value }: { label: string; value?: number }) {
  return <Surface className="p-4"><p className="text-xs text-muted-foreground">{label}</p><p className="text-xl font-semibold mt-1 tabular-nums">{value?.toLocaleString() ?? "—"}</p></Surface>
}
