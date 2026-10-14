import { useEffect, useMemo, useState } from "react"
import { ArrowLeft, BookOpen, CalendarClock, ExternalLink, FileText, LayoutGrid, List, Map, Pencil, Plus, Search, Trash2 } from "lucide-react"
import ReactMarkdown from "react-markdown"
import remarkGfm from "remark-gfm"
import { toast } from "sonner"
import { Button } from "../../components/ui/button"
import { Dialog, DialogContent, DialogDescription, DialogHeader, DialogTitle } from "../../components/ui/dialog"
import { Input } from "../../components/ui/input"
import { useWorkspace } from "../../workspace-context"
import type { LearningPath, LearningPathInput, StudyCategory, StudyInput, StudyItem, StudyStatus } from "../../workspace"
import { EmptyState, Field, formatDate, selectClass, StatePill, Surface, WorkspacePage } from "./workspace-ui"
import { NovelEditor } from "./novel-editor"

const statusLabel: Record<StudyStatus, string> = { inbox: "Inbox", learning: "Learning", reviewing: "Reviewing", mastered: "Mastered" }

export function StudiesView({ category = "all" }: { category?: "all" | "hackathon" }) {
  const { studies, projects, learningPaths, loading } = useWorkspace()
  const [query, setQuery] = useState("")
  const [status, setStatus] = useState("all")
  const [editingId, setEditingId] = useState<string | null>(() => {
    const match = window.location.hash.match(/^#\/(?:studies|hackathon-study)\/([a-f0-9]{32})$/)
    return match?.[1] ?? null
  })
  useEffect(() => {
    const sync = () => setEditingId(window.location.hash.match(/^#\/(?:studies|hackathon-study)\/([a-f0-9]{32})$/)?.[1] ?? null)
    window.addEventListener("popstate", sync)
    window.addEventListener("hashchange", sync)
    return () => { window.removeEventListener("popstate", sync); window.removeEventListener("hashchange", sync) }
  }, [])
  const [creating, setCreating] = useState(false)
  const [defaultPathId, setDefaultPathId] = useState<string | null>(null)
  const [viewMode, setViewMode] = useState<"paths" | "gallery" | "table">("paths")
  const [pathFilter, setPathFilter] = useState("all")
  useEffect(() => setPathFilter("all"), [category])
  const rows = useMemo(() => studies.filter((study) =>
    (category === "all" || study.category === category) &&
    (pathFilter === "all" || study.path_id === pathFilter) &&
    (status === "all" || study.status === status) &&
    `${study.title} ${study.summary} ${study.body} ${study.objective}`.toLowerCase().includes(query.toLowerCase().trim()),
  ), [studies, category, pathFilter, status, query])
  const selected = studies.find((study) => study.id === editingId) ?? null
  const openItem = (id: string) => {
    setEditingId(id)
    window.history.pushState(null, "", `#/${category === "hackathon" ? "hackathon-study" : "studies"}/${id}`)
  }
  const closeItem = () => {
    setCreating(false)
    setDefaultPathId(null)
    setEditingId(null)
    if (window.location.hash.includes(`/${editingId}`)) window.history.replaceState(null, "", `#/${category === "hackathon" ? "hackathon-study" : "studies"}`)
  }

  return <WorkspacePage title={category === "hackathon" ? "Hackathon study" : "Study"} description={category === "hackathon" ? "Learn the skills and requirements for the hackathons you are exploring." : "Follow learning paths, record your understanding, and schedule reviews."} action={<Button size="sm" onClick={() => { setDefaultPathId(null); setCreating(true) }}><Plus className="h-4 w-4 mr-1" />New study item</Button>}>
    <div className="flex flex-wrap gap-2 items-center">
      <div className="relative flex-1 min-w-48 max-w-sm"><Search className="absolute left-3 top-2.5 h-4 w-4 text-muted-foreground" /><Input aria-label="Search study items" className="pl-9" placeholder="Search study items" value={query} onChange={(e) => setQuery(e.target.value)} /></div>
      <select aria-label="Filter study status" className={`${selectClass} !w-36`} value={status} onChange={(e) => setStatus(e.target.value)}><option value="all">All statuses</option>{Object.entries(statusLabel).map(([value, label]) => <option key={value} value={value}>{label}</option>)}</select>
      <select aria-label="Filter learning path" className={`${selectClass} !w-44`} value={pathFilter} onChange={(e) => setPathFilter(e.target.value)}><option value="all">All learning paths</option>{learningPaths.filter((path) => category === "all" || path.category === category).map((path) => <option key={path.id} value={path.id}>{path.title}</option>)}</select>
      <span className="text-xs text-muted-foreground ml-auto">{rows.length} items</span>
    </div>
    <div role="tablist" aria-label="Study views" className="flex items-center gap-1 border-b border-border/70 pb-2"><button role="tab" aria-selected={viewMode === "paths"} className={`px-3 py-1.5 rounded-md text-xs flex items-center gap-1.5 ${viewMode === "paths" ? "bg-blue-500/10 text-blue-300" : "text-muted-foreground hover:bg-foreground/5"}`} onClick={() => setViewMode("paths")}><Map className="h-3.5 w-3.5" />Learning paths</button><button role="tab" aria-selected={viewMode === "gallery"} className={`px-3 py-1.5 rounded-md text-xs flex items-center gap-1.5 ${viewMode === "gallery" ? "bg-blue-500/10 text-blue-300" : "text-muted-foreground hover:bg-foreground/5"}`} onClick={() => setViewMode("gallery")}><LayoutGrid className="h-3.5 w-3.5" />Gallery</button><button role="tab" aria-selected={viewMode === "table"} className={`px-3 py-1.5 rounded-md text-xs flex items-center gap-1.5 ${viewMode === "table" ? "bg-blue-500/10 text-blue-300" : "text-muted-foreground hover:bg-foreground/5"}`} onClick={() => setViewMode("table")}><List className="h-3.5 w-3.5" />Table</button></div>
    {viewMode === "paths" && <LearningPathsPanel category={category} onOpenItem={openItem} onNewItem={(id) => { setDefaultPathId(id); setCreating(true) }} />}
    {viewMode === "gallery" && (rows.length ? <div className="grid md:grid-cols-2 xl:grid-cols-3 gap-3">{rows.map((study) => {
      const project = projects.find((p) => p.id === study.project_id)
      return <Surface key={study.id} className="p-4 min-h-44 flex flex-col" onClick={() => openItem(study.id)}>
        <div className="flex items-start gap-2"><div className="h-8 w-8 rounded-lg bg-blue-500/10 text-blue-400 flex items-center justify-center flex-shrink-0"><BookOpen className="h-4 w-4" /></div><div className="min-w-0 flex-1"><h2 className="text-sm font-semibold line-clamp-2">{study.title}</h2><p className="text-[11px] text-muted-foreground mt-0.5 truncate">{study.hackathon_host || project?.title || (study.category === "hackathon" ? "Hackathon" : "General study")}</p></div></div>
        <p className="text-xs leading-relaxed text-muted-foreground line-clamp-2 mt-3">{study.summary || study.body || "Open to add study notes."}</p>
        <div className="flex items-center justify-between mt-auto pt-4"><StatePill value={statusLabel[study.status]} tone={study.status === "mastered" ? "green" : study.status === "learning" || study.status === "reviewing" ? "blue" : "neutral"} /><span className="text-[11px] text-muted-foreground">{formatDate(study.updated_at)}</span></div>
      </Surface>
    })}</div> : <EmptyState title={loading ? "Loading study items…" : "No study items here"} detail="Save a topic, a source, and your own notes to start learning." action={!loading && <Button size="sm" variant="outline" onClick={() => setCreating(true)}>Add study item</Button>} />)}
    {viewMode === "table" && <Surface className="divide-y divide-border/60 overflow-hidden"><div className="hidden sm:grid grid-cols-[minmax(0,1fr)_90px_100px_120px] gap-3 px-4 py-2 bg-muted/30 text-[11px] font-medium text-muted-foreground"><span>Name / project</span><span>Type</span><span>Status</span><span>Updated</span></div>{rows.map((study) => { const project = projects.find((item) => item.id === study.project_id); return <button key={study.id} type="button" className="w-full flex sm:grid sm:grid-cols-[minmax(0,1fr)_90px_100px_120px] gap-3 items-center px-4 py-3 text-left hover:bg-foreground/[0.035]" onClick={() => openItem(study.id)}><span className="min-w-0"><span className="block text-sm truncate">{study.title}</span><span className="block text-[11px] text-muted-foreground truncate">{project?.title || study.hackathon_host || "General"}</span></span><span className="hidden sm:block text-[11px] text-muted-foreground capitalize">{study.category}</span><span className="hidden sm:block"><StatePill value={statusLabel[study.status]} tone={study.status === "learning" || study.status === "reviewing" ? "blue" : study.status === "mastered" ? "green" : "neutral"} /></span><span className="hidden sm:block text-[11px] text-muted-foreground">{formatDate(study.updated_at)}</span></button> })}{!rows.length && <p className="p-6 text-sm text-muted-foreground">No study items match these filters.</p>}</Surface>}
    <Dialog open={creating || !!selected} onOpenChange={(open) => { if (!open) closeItem() }}>
      <DialogContent className="!max-w-4xl max-h-[90vh] overflow-y-auto"><DialogHeader><DialogTitle>{selected?.title ?? "New study item"}</DialogTitle><DialogDescription>Read, edit, and track your progress here.</DialogDescription></DialogHeader><StudyEditor key={selected?.id ?? `new-${defaultPathId}`} item={selected} defaultCategory={category === "hackathon" ? "hackathon" : "general"} defaultPathId={defaultPathId} onClose={closeItem} /></DialogContent>
    </Dialog>
  </WorkspacePage>
}

function StudyEditor({ item, defaultCategory, defaultPathId, onClose }: { item: StudyItem | null; defaultCategory: StudyCategory; defaultPathId: string | null; onClose: () => void }) {
  const { projects, learningPaths, createStudy, updateStudy, deleteStudy } = useWorkspace()
  const [editing, setEditing] = useState(!item)
  const [saving, setSaving] = useState(false)
  const initialPath = learningPaths.find((path) => path.id === defaultPathId)
  const initialForm: StudyInput = { title: item?.title ?? "", summary: item?.summary ?? "", body: item?.body ?? "", status: item?.status ?? "inbox", category: item?.category ?? initialPath?.category ?? defaultCategory, source_url: item?.source_url ?? "", project_id: item?.project_id ?? initialPath?.project_id ?? null, path_id: item?.path_id ?? defaultPathId, objective: item?.objective ?? "", review_on: item?.review_on ?? null, hackathon_host: item?.hackathon_host ?? "" }
  const [form, setForm] = useState<StudyInput>(initialForm)
  const save = async (event: React.FormEvent) => {
    event.preventDefault()
    if (!form.title.trim()) return toast.error("Study title is required")
    setSaving(true)
    try { if (item) { await updateStudy(item.id, form); setEditing(false) } else { await createStudy(form); onClose() } toast.success(item ? "Study item updated" : "Study item created") }
    catch (e) { toast.error(e instanceof Error ? e.message : String(e)) }
    finally { setSaving(false) }
  }
  const changeStatus = async (value: StudyStatus) => {
    if (!item) return
    try { await updateStudy(item.id, { status: value }); setForm((s) => ({ ...s, status: value })) }
    catch (e) { toast.error(e instanceof Error ? e.message : String(e)) }
  }
  const remove = async () => {
    if (!item || !window.confirm(`Delete “${item.title}”?`)) return
    try { await deleteStudy(item.id); toast.success("Study item deleted"); onClose() }
    catch (e) { toast.error(e instanceof Error ? e.message : String(e)) }
  }

  if (!editing && item) return <div className="space-y-5">
    <div className="flex flex-wrap gap-2 items-center"><StatePill value={item.category === "hackathon" ? "Hackathon" : "General"} tone={item.category === "hackathon" ? "blue" : "neutral"} />{item.hackathon_host && <span className="text-xs text-muted-foreground">{item.hackathon_host}</span>}{item.project_id && <span className="text-xs text-muted-foreground">{projects.find((p) => p.id === item.project_id)?.title}</span>}<span className="ml-auto text-[11px] text-muted-foreground">Updated {formatDate(item.updated_at)}</span></div>
    {item.summary && <p className="text-sm text-muted-foreground leading-relaxed">{item.summary}</p>}
    {item.objective && <div className="rounded-lg border border-blue-500/20 bg-blue-500/5 p-3"><p className="text-[11px] font-medium uppercase tracking-wide text-blue-300 mb-1">Learning objective</p><p className="text-sm">{item.objective}</p></div>}
    {(item.path_id || item.review_on) && <div className="flex flex-wrap gap-3 text-xs text-muted-foreground">{item.path_id && <span>Path: {learningPaths.find((path) => path.id === item.path_id)?.title}</span>}{item.review_on && <span className="inline-flex items-center gap-1"><CalendarClock className="h-3.5 w-3.5" />Review {formatDate(item.review_on)}</span>}</div>}
    {item.source_url && <a href={item.source_url} target="_blank" rel="noopener noreferrer" className="inline-flex items-center gap-1 text-xs text-blue-400 hover:underline"><ExternalLink className="h-3.5 w-3.5" />Open source</a>}
    <div className="rounded-lg border bg-muted/30 p-5 min-h-48 allow-text-selection">{item.body ? <div className="prose prose-sm dark:prose-invert max-w-none text-foreground break-words"><ReactMarkdown remarkPlugins={[remarkGfm]}>{item.body}</ReactMarkdown></div> : <div className="text-sm text-muted-foreground flex items-center gap-2"><FileText className="h-4 w-4" />No notes yet. Select Edit to add them.</div>}</div>
    <div className="border-t pt-4 flex flex-wrap items-end gap-2"><Field label="Learning status"><select aria-label="Learning status" className={`${selectClass} !w-40`} value={item.status} onChange={(e) => void changeStatus(e.target.value as StudyStatus)}>{Object.entries(statusLabel).map(([value, label]) => <option key={value} value={value}>{label}</option>)}</select></Field><div className="ml-auto flex gap-2"><Button variant="ghost" size="sm" className="text-muted-foreground hover:text-destructive" onClick={() => void remove()}><Trash2 className="h-3.5 w-3.5 mr-1" />Delete</Button><Button size="sm" variant="outline" onClick={() => setEditing(true)}><Pencil className="h-3.5 w-3.5 mr-1" />Edit</Button></div></div>
  </div>

  return <form onSubmit={(event) => void save(event)} className="space-y-4">
    <Field label="Title"><Input autoFocus value={form.title} onChange={(e) => setForm({ ...form, title: e.target.value })} maxLength={200} placeholder="What are you learning?" /></Field>
    <Field label="Summary"><Input value={form.summary} onChange={(e) => setForm({ ...form, summary: e.target.value })} maxLength={2000} placeholder="A short description" /></Field>
    <Field label="Learning objective"><Input value={form.objective ?? ""} onChange={(e) => setForm({ ...form, objective: e.target.value })} maxLength={2000} placeholder="What should you be able to explain or do?" /></Field>
    <div className="grid sm:grid-cols-3 gap-3"><Field label="Status"><select className={selectClass} value={form.status} onChange={(e) => setForm({ ...form, status: e.target.value as StudyStatus })}>{Object.entries(statusLabel).map(([value, label]) => <option key={value} value={value}>{label}</option>)}</select></Field><Field label="Category"><select className={selectClass} value={form.category} onChange={(e) => setForm({ ...form, category: e.target.value as StudyCategory, path_id: null, hackathon_host: e.target.value === "general" ? "" : form.hackathon_host })}><option value="general">General</option><option value="hackathon">Hackathon</option></select></Field><Field label="Project"><select className={selectClass} value={form.project_id ?? ""} onChange={(e) => setForm({ ...form, project_id: e.target.value || null })}><option value="">No project</option>{projects.map((project) => <option key={project.id} value={project.id}>{project.title}</option>)}</select></Field></div>
    <div className="grid sm:grid-cols-2 gap-3"><Field label="Learning path"><select className={selectClass} value={form.path_id ?? ""} onChange={(e) => setForm({ ...form, path_id: e.target.value || null })}><option value="">Unsorted</option>{learningPaths.filter((path) => path.category === form.category).map((path) => <option key={path.id} value={path.id}>{path.title}</option>)}</select></Field><Field label="Review date"><Input type="date" value={form.review_on ?? ""} onChange={(e) => setForm({ ...form, review_on: e.target.value || null })} /></Field></div>
    {form.category === "hackathon" && <Field label="Hackathon host" hint="Use the host shown in Devpost Scout to link the note to an event."><Input value={form.hackathon_host} onChange={(e) => setForm({ ...form, hackathon_host: e.target.value })} maxLength={255} placeholder="example.devpost.com" /></Field>}
    <Field label="Source URL"><Input type="url" value={form.source_url} onChange={(e) => setForm({ ...form, source_url: e.target.value })} placeholder="https://..." /></Field>
    <div><p className="mb-1.5 text-xs font-medium text-muted-foreground">Study notes · Novel editor</p><NovelEditor title={form.title} value={form.body} onChange={(body) => setForm((current) => ({ ...current, body }))} minHeight="18rem" /></div>
    <div className="flex justify-end gap-2"><Button type="button" variant="outline" onClick={() => { if (item) { setForm(initialForm); setEditing(false) } else onClose() }}>Cancel</Button><Button type="submit" disabled={saving}>{saving ? "Saving…" : "Save study item"}</Button></div>
  </form>
}

function LearningPathsPanel({ category, onOpenItem, onNewItem }: {
  category: "all" | "hackathon"
  onOpenItem: (id: string) => void
  onNewItem: (pathId: string) => void
}) {
  const { learningPaths, studies, projects, createLearningPath, updateLearningPath, deleteLearningPath, updateStudy } = useWorkspace()
  const pathFromHash = () => window.location.hash.match(/^#\/(?:studies|hackathon-study)\/path\/([a-f0-9]{32})$/)?.[1] ?? null
  const [selectedId, setSelectedId] = useState<string | null>(pathFromHash)
  useEffect(() => {
    const sync = () => { const id = pathFromHash(); if (id) setSelectedId(id) }
    window.addEventListener("hashchange", sync)
    window.addEventListener("popstate", sync)
    return () => { window.removeEventListener("hashchange", sync); window.removeEventListener("popstate", sync) }
  }, [])
  const [editing, setEditing] = useState(false)
  const [form, setForm] = useState<LearningPathInput>({ title: "", outcome: "", category: category === "hackathon" ? "hackathon" : "general", project_id: null })
  const [saving, setSaving] = useState(false)
  const paths = learningPaths.filter((path) => category === "all" || path.category === category)
  const selected = paths.find((path) => path.id === selectedId)
  const items = selected ? studies.filter((study) => study.path_id === selected.id).sort((a, b) => a.created_at.localeCompare(b.created_at)) : []
  const now = new Date()
  const today = `${now.getFullYear()}-${String(now.getMonth() + 1).padStart(2, "0")}-${String(now.getDate()).padStart(2, "0")}`
  const due = studies.filter((study) => (category === "all" || study.category === category) && study.status !== "mastered" && study.review_on && study.review_on <= today).sort((a, b) => (a.review_on || "").localeCompare(b.review_on || ""))
  const startCreate = () => { setForm({ title: "", outcome: "", category: category === "hackathon" ? "hackathon" : "general", project_id: null }); setEditing(true) }
  const startEdit = (path: LearningPath) => { setForm({ title: path.title, outcome: path.outcome, category: path.category, project_id: path.project_id }); setEditing(true) }
  const save = async (event: React.FormEvent) => {
    event.preventDefault()
    if (!form.title.trim()) return
    setSaving(true)
    try {
      if (editingPathId) await updateLearningPath(editingPathId, form)
      else { const created = await createLearningPath(form); setSelectedId(created.id) }
      setEditing(false)
      setEditingPathId(null)
      toast.success("Learning path saved")
    } catch (error) { toast.error(error instanceof Error ? error.message : String(error)) }
    finally { setSaving(false) }
  }
  const [editingPathId, setEditingPathId] = useState<string | null>(null)
  const remove = async () => {
    if (!selected || !window.confirm(`Delete learning path “${selected.title}”? Its study items will remain unsorted.`)) return
    try { await deleteLearningPath(selected.id); setSelectedId(null); toast.success("Learning path deleted") }
    catch (error) { toast.error(error instanceof Error ? error.message : String(error)) }
  }
  const changeStatus = async (study: StudyItem, status: StudyStatus) => {
    try { await updateStudy(study.id, { status }) }
    catch (error) { toast.error(error instanceof Error ? error.message : String(error)) }
  }
  return <div className="space-y-5">
    {due.length > 0 && <Surface className="overflow-hidden"><div className="flex items-center gap-2 border-b border-border/60 px-4 py-3"><CalendarClock className="h-4 w-4 text-amber-400" /><h2 className="text-sm font-semibold">Ready to review</h2><span className="text-xs text-muted-foreground">{due.length}</span></div><div className="divide-y divide-border/60 max-h-48 overflow-y-auto">{due.map((study) => <button key={study.id} className="flex w-full items-center gap-3 px-4 py-2.5 text-left text-sm hover:bg-foreground/5" onClick={() => onOpenItem(study.id)}><span className="flex-1 truncate">{study.title}</span><span className="text-[11px] text-amber-400">{formatDate(study.review_on)}</span></button>)}</div></Surface>}
    {selected ? <div className="space-y-4"><div className="flex items-start gap-3"><button className="mt-1 text-muted-foreground hover:text-foreground" aria-label="Back to learning paths" onClick={() => { setSelectedId(null); window.history.replaceState(null, "", `#/${category === "hackathon" ? "hackathon-study" : "studies"}`) }}><ArrowLeft className="h-4 w-4" /></button><div className="flex-1"><h2 className="text-xl font-semibold">{selected.title}</h2><p className="text-sm text-muted-foreground mt-1">{selected.outcome || "Add a learning outcome to make this path more focused."}</p></div><Button size="sm" variant="outline" onClick={() => { startEdit(selected); setEditingPathId(selected.id) }}>Edit path</Button></div>
      <div className="rounded-lg border border-border/70 bg-card/40 p-4"><div className="flex items-center justify-between text-xs text-muted-foreground"><span>{items.filter((item) => item.status === "mastered").length} of {items.length} mastered</span><span>{items.filter((item) => item.status === "learning" || item.status === "reviewing").length} in progress</span></div><div className="mt-2 h-2 rounded-full bg-foreground/5 overflow-hidden"><div className="h-full bg-blue-500" style={{ width: `${items.length ? items.filter((item) => item.status === "mastered").length / items.length * 100 : 0}%` }} /></div></div>
      {(["inbox", "learning", "reviewing", "mastered"] as const).map((stage) => { const rows = items.filter((item) => item.status === stage); return rows.length ? <section key={stage}><h3 className="mb-2 text-xs font-semibold uppercase tracking-wide text-muted-foreground">{statusLabel[stage]} · {rows.length}</h3><Surface className="divide-y divide-border/60">{rows.map((study, index) => <div key={study.id} className="flex items-center gap-3 px-4 py-3"><span className="w-5 text-[11px] text-muted-foreground">{index + 1}</span><button className="min-w-0 flex-1 text-left" onClick={() => onOpenItem(study.id)}><span className="block truncate text-sm font-medium">{study.title}</span><span className="block truncate text-[11px] text-muted-foreground">{study.objective || study.summary || "Add a learning objective"}</span></button>{study.review_on && <span className="hidden sm:block text-[11px] text-muted-foreground">Review {formatDate(study.review_on)}</span>}<select aria-label={`Learning status for ${study.title}`} className="rounded border bg-muted px-1 py-1 text-xs text-foreground" value={study.status} onChange={(event) => void changeStatus(study, event.target.value as StudyStatus)}>{Object.entries(statusLabel).map(([value, label]) => <option key={value} value={value}>{label}</option>)}</select></div>)}</Surface></section> : null })}
      <div className="flex items-center gap-2"><Button size="sm" variant="outline" onClick={() => onNewItem(selected.id)}><Plus className="h-4 w-4 mr-1" />Add study item</Button><Button size="sm" variant="ghost" className="text-muted-foreground hover:text-destructive" onClick={() => void remove()}><Trash2 className="h-4 w-4 mr-1" />Delete path</Button></div>
    </div> : <><div className="flex items-center justify-between"><div><h2 className="text-sm font-semibold">Learning paths</h2><p className="text-xs text-muted-foreground mt-1">Topics are grouped by project. Open a path to work through its material.</p></div><Button size="sm" variant="outline" onClick={() => { startCreate(); setEditingPathId(null) }}><Plus className="h-4 w-4 mr-1" />New path</Button></div><div className="grid md:grid-cols-2 xl:grid-cols-3 gap-3">{paths.map((path) => { const related = studies.filter((study) => study.path_id === path.id); const complete = related.filter((study) => study.status === "mastered").length; return <Surface key={path.id} className="flex flex-col p-4 min-h-36" onClick={() => { setSelectedId(path.id); window.history.pushState(null, "", `#/${category === "hackathon" ? "hackathon-study" : "studies"}/path/${path.id}`) }}><div className="flex items-start gap-2"><Map className="h-4 w-4 mt-0.5 text-blue-400" /><div className="min-w-0"><h3 className="text-sm font-semibold line-clamp-2">{path.title}</h3><p className="text-[11px] text-muted-foreground mt-1">{projects.find((item) => item.id === path.project_id)?.title || (path.category === "hackathon" ? "Hackathon" : "Independent")}</p></div></div><p className="text-xs text-muted-foreground line-clamp-2 mt-3">{path.outcome || `${related.length} items to study`}</p><div className="mt-auto pt-4"><div className="h-1.5 rounded-full bg-foreground/5 overflow-hidden"><div className="h-full bg-blue-500" style={{ width: `${related.length ? complete / related.length * 100 : 0}%` }} /></div><p className="text-[11px] text-muted-foreground mt-2">{complete}/{related.length} mastered</p></div></Surface> })}</div></>}
    <Dialog open={editing} onOpenChange={setEditing}><DialogContent className="!max-w-lg"><DialogHeader><DialogTitle>{editingPathId ? "Edit learning path" : "New learning path"}</DialogTitle><DialogDescription>Group related material around an outcome.</DialogDescription></DialogHeader><form className="space-y-4" onSubmit={(event) => void save(event)}><Field label="Path title"><Input autoFocus value={form.title} onChange={(event) => setForm({ ...form, title: event.target.value })} maxLength={200} placeholder="Example: Systems foundations" /></Field><Field label="Learning outcome"><Input value={form.outcome} onChange={(event) => setForm({ ...form, outcome: event.target.value })} maxLength={2000} placeholder="What will you be able to do?" /></Field><div className="grid grid-cols-2 gap-3"><Field label="Category"><select className={selectClass} value={form.category} disabled={category === "hackathon" || !!editingPathId && items.length > 0} onChange={(event) => setForm({ ...form, category: event.target.value as StudyCategory })}><option value="general">General</option><option value="hackathon">Hackathon</option></select></Field><Field label="Project"><select className={selectClass} value={form.project_id ?? ""} onChange={(event) => setForm({ ...form, project_id: event.target.value || null })}><option value="">No project</option>{projects.map((project) => <option key={project.id} value={project.id}>{project.title}</option>)}</select></Field></div><div className="flex justify-end gap-2"><Button type="button" variant="outline" onClick={() => setEditing(false)}>Cancel</Button><Button type="submit" disabled={saving || !form.title.trim()}>{saving ? "Saving…" : "Save path"}</Button></div></form></DialogContent></Dialog>
  </div>
}
