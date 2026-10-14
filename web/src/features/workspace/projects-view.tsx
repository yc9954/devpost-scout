import { useMemo, useState } from "react"
import { Columns3, FolderKanban, LayoutGrid, Plus, Search, Trash2 } from "lucide-react"
import { toast } from "sonner"
import { Button } from "../../components/ui/button"
import { Dialog, DialogContent, DialogDescription, DialogHeader, DialogTitle } from "../../components/ui/dialog"
import { Input } from "../../components/ui/input"
import { useApp } from "../../store"
import { useWorkspace } from "../../workspace-context"
import { useHashRoute } from "../../use-hash-route"
import type { ProjectInput, ProjectStatus, WorkspaceProject } from "../../workspace"
import { EmptyState, Field, formatDate, selectClass, SourceLinks, StatePill, Surface, textareaClass, WorkspacePage } from "./workspace-ui"
import { ProjectDetailView } from "./project-detail-view"

const statusLabel: Record<ProjectStatus, string> = { planned: "Planned", active: "Active", paused: "Paused", done: "Done" }

export function ProjectsView() {
  const hash = useHashRoute()
  const { projects, tasks, studies, milestones, updateProject, loading } = useWorkspace()
  const [query, setQuery] = useState("")
  const [filter, setFilter] = useState("all")
  const [viewMode, setViewMode] = useState<"cards" | "board">("cards")
  const [editingId, setEditingId] = useState<string | null>(null)
  const [creating, setCreating] = useState(false)
  const rows = useMemo(() => projects.filter((project) =>
    (filter === "all" || project.status === filter) &&
    `${project.title} ${project.description} ${project.goal} ${project.next_action}`.toLowerCase().includes(query.toLowerCase().trim()),
  ), [projects, filter, query])
  const selected = projects.find((project) => project.id === editingId) ?? null
  const routeId = hash.match(/^#\/projects\/([a-f0-9]{32})$/)?.[1]
  if (routeId) {
    const project = projects.find((item) => item.id === routeId)
    return project ? <ProjectDetailView key={project.id} project={project} /> : <WorkspacePage title="Project"><EmptyState title={loading ? "Loading project…" : "Project not found"} detail="Choose a project from the sidebar." /></WorkspacePage>
  }

  return <WorkspacePage title="Projects" description="Keep project plans, related to dos, and learning together." action={<Button size="sm" onClick={() => setCreating(true)}><Plus className="h-4 w-4 mr-1" />New project</Button>}>
    <div className="flex flex-wrap gap-2 items-center">
      <div className="relative flex-1 min-w-48 max-w-sm"><Search className="absolute left-3 top-2.5 h-4 w-4 text-muted-foreground" /><Input aria-label="Search projects" placeholder="Search projects" className="pl-9" value={query} onChange={(event) => setQuery(event.target.value)} /></div>
      <select aria-label="Filter projects" className={`${selectClass} !w-36`} value={filter} onChange={(event) => setFilter(event.target.value)}><option value="all">All statuses</option>{Object.entries(statusLabel).map(([value, label]) => <option key={value} value={value}>{label}</option>)}</select>
      <span className="text-xs text-muted-foreground ml-auto">{rows.length} projects</span>
    </div>
    <div role="tablist" aria-label="Project views" className="flex items-center gap-1 border-b border-border/70 pb-2"><button role="tab" aria-selected={viewMode === "cards"} className={`flex items-center gap-1.5 rounded-md px-3 py-1.5 text-xs ${viewMode === "cards" ? "bg-blue-500/10 text-blue-700" : "text-muted-foreground"}`} onClick={() => setViewMode("cards")}><LayoutGrid className="h-3.5 w-3.5" />Cards</button><button role="tab" aria-selected={viewMode === "board"} className={`flex items-center gap-1.5 rounded-md px-3 py-1.5 text-xs ${viewMode === "board" ? "bg-blue-500/10 text-blue-700" : "text-muted-foreground"}`} onClick={() => { setFilter("all"); setViewMode("board") }}><Columns3 className="h-3.5 w-3.5" />Board</button></div>
    {viewMode === "board" && <div className="grid md:grid-cols-2 xl:grid-cols-4 gap-3 items-start">{(["planned", "active", "paused", "done"] as const).map((column) => <section key={column} className="rounded-xl border border-border/70 bg-card/30 min-h-40"><div className="flex items-center justify-between border-b border-border/60 px-3 py-2"><h2 className="text-xs font-semibold">{statusLabel[column]}</h2><span className="text-xs text-muted-foreground">{rows.filter((project) => project.status === column).length}</span></div><div className="space-y-2 p-2 max-h-[70vh] overflow-y-auto">{rows.filter((project) => project.status === column).map((project) => <Surface key={project.id} className="p-3 space-y-2"><button className="w-full text-left text-sm font-semibold hover:text-blue-300" onClick={() => { window.location.hash = `#/projects/${project.id}` }}>{project.title}</button><p className="text-xs text-muted-foreground line-clamp-2">{project.goal || project.description.split("\n\n관련 기록:")[0]}</p>{project.next_action && <p className="text-[11px] text-blue-300 line-clamp-2">Next: {project.next_action}</p>}<div className="flex items-center justify-between gap-2"><span className="text-[11px] text-muted-foreground">{tasks.filter((task) => task.project_id === project.id && task.status === "done").length}/{tasks.filter((task) => task.project_id === project.id).length} to dos</span><select aria-label={`Status for ${project.title}`} className="rounded border bg-muted px-1 py-0.5 text-[11px]" value={project.status} onChange={async (event) => { try { await updateProject(project.id, { status: event.target.value as ProjectStatus }) } catch (error) { toast.error(error instanceof Error ? error.message : String(error)) } }}>{Object.entries(statusLabel).map(([value, label]) => <option key={value} value={value}>{label}</option>)}</select></div></Surface>)}</div></section>)}</div>}
    {viewMode === "cards" && (rows.length ? <div className="grid md:grid-cols-2 xl:grid-cols-3 gap-3">{rows.map((project) => {
      const relatedTasks = tasks.filter((task) => task.project_id === project.id)
      const done = relatedTasks.filter((task) => task.status === "done").length
      const relatedStudies = studies.filter((study) => study.project_id === project.id).length
      return <Surface key={project.id} className="p-4 min-h-44 flex flex-col" onClick={() => { window.location.hash = `#/projects/${project.id}` }}>
        <div className="flex items-start gap-2.5"><FolderKanban className="mt-0.5 h-4 w-4 flex-shrink-0 text-muted-foreground/70" /><div className="min-w-0 flex-1"><h2 className="text-sm font-semibold truncate">{project.title}</h2><div className="mt-1"><StatePill value={statusLabel[project.status]} tone={project.status === "active" ? "blue" : project.status === "done" ? "green" : "neutral"} /></div></div></div>
        <p className="text-xs leading-relaxed text-muted-foreground line-clamp-2 mt-3 min-h-8">{project.goal || project.description.split("\n\n관련 기록:")[0] || "Add a project goal."}</p>
        {project.next_action && <p className="text-xs text-blue-700 line-clamp-1 mt-2">Next: {project.next_action}</p>}
        <div className="mt-auto pt-4"><div className="h-1.5 w-full bg-foreground/5 rounded-full overflow-hidden"><div className="h-full bg-blue-500 rounded-full" style={{ width: `${relatedTasks.length ? done / relatedTasks.length * 100 : 0}%` }} /></div><div className="flex justify-between text-[11px] text-muted-foreground mt-2"><span>{done}/{relatedTasks.length} to dos · {milestones.filter((item) => item.project_id === project.id && item.status === "done").length}/{milestones.filter((item) => item.project_id === project.id).length} milestones</span><span>{project.target_on ? formatDate(project.target_on) : `${relatedStudies} notes`}</span></div></div>
      </Surface>
    })}</div> : <EmptyState title={loading ? "Loading projects…" : "No projects here"} detail="Create a project or change the filter." action={!loading && <Button size="sm" variant="outline" onClick={() => setCreating(true)}>Create project</Button>} />)}
    <Dialog open={creating || !!selected} onOpenChange={(open) => { if (!open) { setCreating(false); setEditingId(null) } }}>
      <DialogContent className="!max-w-2xl max-h-[85vh] overflow-y-auto">
        <DialogHeader><DialogTitle>{selected ? selected.title : "New project"}</DialogTitle><DialogDescription>Projects connect your tasks and study material.</DialogDescription></DialogHeader>
        <ProjectEditor key={selected?.id ?? "new"} project={selected} onClose={() => { setCreating(false); setEditingId(null) }} />
      </DialogContent>
    </Dialog>
  </WorkspacePage>
}

function ProjectEditor({ project, onClose }: { project: WorkspaceProject | null; onClose: () => void }) {
  const { createProject, updateProject, deleteProject, tasks, studies } = useWorkspace()
  const setView = useApp((state) => state.setView)
  const [form, setForm] = useState<ProjectInput>({ title: project?.title ?? "", description: project?.description ?? "", status: project?.status ?? "active", goal: project?.goal ?? "", next_action: project?.next_action ?? "", target_on: project?.target_on ?? null })
  const [saving, setSaving] = useState(false)
  const projectTasks = tasks.filter((task) => task.project_id === project?.id)
  const projectStudies = studies.filter((study) => study.project_id === project?.id)
  const save = async (event: React.FormEvent) => {
    event.preventDefault()
    if (!form.title.trim()) return toast.error("Project title is required")
    setSaving(true)
    try {
      if (project) await updateProject(project.id, form)
      else await createProject(form)
      toast.success(project ? "Project updated" : "Project created")
      onClose()
    } catch (e) { toast.error(e instanceof Error ? e.message : String(e)) }
    finally { setSaving(false) }
  }
  const remove = async () => {
    if (!project || !window.confirm(`Delete “${project.title}”? Its tasks and study notes will remain unlinked.`)) return
    try { await deleteProject(project.id); toast.success("Project deleted"); onClose() }
    catch (e) { toast.error(e instanceof Error ? e.message : String(e)) }
  }
  return <div className="space-y-5">
    <form onSubmit={(event) => void save(event)} className="space-y-4">
      <Field label="Project name"><Input autoFocus value={form.title} onChange={(event) => setForm({ ...form, title: event.target.value })} maxLength={200} placeholder="Name your project" /></Field>
      <Field label="Goal"><Input value={form.goal ?? ""} onChange={(event) => setForm({ ...form, goal: event.target.value })} maxLength={1000} placeholder="What does success look like?" /></Field>
      <Field label="Next action"><Input value={form.next_action ?? ""} onChange={(event) => setForm({ ...form, next_action: event.target.value })} maxLength={1000} placeholder="One concrete next step" /></Field>
      <Field label="Description"><textarea className={`${textareaClass} min-h-24`} value={form.description} onChange={(event) => setForm({ ...form, description: event.target.value })} maxLength={10000} placeholder="What are you working toward?" /></Field>
      <Field label="Status"><select className={selectClass} value={form.status} onChange={(event) => setForm({ ...form, status: event.target.value as ProjectStatus })}>{Object.entries(statusLabel).map(([value, label]) => <option key={value} value={value}>{label}</option>)}</select></Field>
      <Field label="Target date"><Input type="date" value={form.target_on ?? ""} onChange={(event) => setForm({ ...form, target_on: event.target.value || null })} /></Field>
      <div className="flex gap-2 justify-end"><Button type="button" variant="outline" onClick={onClose}>Cancel</Button><Button type="submit" disabled={saving}>{saving ? "Saving…" : "Save project"}</Button></div>
    </form>
    <SourceLinks text={form.description} onNavigate={onClose} />
    {project && <div className="border-t pt-4 space-y-3">
      <div className="grid sm:grid-cols-2 gap-3"><RelatedList title={`To dos (${projectTasks.length})`} items={projectTasks.map((task) => task.title)} onClick={() => { onClose(); setView("tasks") }} /><RelatedList title={`Study (${projectStudies.length})`} items={projectStudies.map((study) => study.title)} onClick={() => { onClose(); setView("studies") }} /></div>
      <Button variant="ghost" size="sm" className="text-muted-foreground hover:text-destructive" onClick={() => void remove()}><Trash2 className="h-3.5 w-3.5 mr-1" />Delete project</Button>
    </div>}
  </div>
}

function RelatedList({ title, items, onClick }: { title: string; items: string[]; onClick: () => void }) {
  return <button type="button" className="rounded-lg border p-3 text-left hover:bg-foreground/5" onClick={onClick}><span className="text-xs font-medium">{title}</span><span className="block text-[11px] text-muted-foreground mt-2 line-clamp-2">{items.length ? items.slice(0, 3).join(" · ") : "Nothing linked yet"}</span></button>
}
