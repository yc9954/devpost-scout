import { useEffect, useState } from "react"
import { ArrowLeft, BookOpen, CheckSquare2, ChevronRight, FileText, Flag, Folder, Plus, Save, Trash2, Video } from "lucide-react"
import ReactMarkdown from "react-markdown"
import remarkGfm from "remark-gfm"
import { toast } from "sonner"
import { Button } from "../../components/ui/button"
import { Input } from "../../components/ui/input"
import { useWorkspace } from "../../workspace-context"
import type { WorkspaceMilestone, WorkspaceProject } from "../../workspace"
import { EmptyState, Field, formatDate, selectClass, SourceLinks, StatePill, Surface, WorkspacePage } from "./workspace-ui"
import { NewPageDialog } from "./pages-view"
import { NovelEditor } from "./novel-editor"
import { studioApi, type StudioRecording } from "../../studio"

export function ProjectDetailView({ project }: { project: WorkspaceProject }) {
  const { pages, tasks, studies, milestones, updateProject, createTask, createStudy, createMilestone, updateMilestone, deleteMilestone, updateTask } = useWorkspace()
  const [editing, setEditing] = useState(false)
  const [title, setTitle] = useState(project.title)
  const [description, setDescription] = useState(project.description)
  const [status, setStatus] = useState(project.status)
  const [goal, setGoal] = useState(project.goal)
  const [nextAction, setNextAction] = useState(project.next_action)
  const [targetOn, setTargetOn] = useState(project.target_on ?? "")
  const [newMilestone, setNewMilestone] = useState("")
  const [newMilestoneDue, setNewMilestoneDue] = useState("")
  const [newPage, setNewPage] = useState(false)
  const [taskDrafts, setTaskDrafts] = useState<Record<string, string>>({})
  const [newStudy, setNewStudy] = useState("")
  const [saving, setSaving] = useState(false)
  const [recordings, setRecordings] = useState<StudioRecording[]>([])
  useEffect(() => {
    let active = true
    studioApi.list().then((rows) => { if (active) setRecordings(rows.filter((item) => item.project_id === project.id)) }).catch(() => {})
    return () => { active = false }
  }, [project.id])
  const projectPages = pages.filter((item) => item.project_id === project.id && !item.parent_id)
  const projectTasks = tasks.filter((item) => item.project_id === project.id)
  const projectStudies = studies.filter((item) => item.project_id === project.id)
  const projectMilestones = milestones.filter((item) => item.project_id === project.id).sort((a, b) => (a.due_on || "9999").localeCompare(b.due_on || "9999"))
  const taskDone = projectTasks.filter((item) => item.status === "done").length
  const save = async (event: React.FormEvent) => {
    event.preventDefault()
    setSaving(true)
    try { await updateProject(project.id, { title, description, status, goal, next_action: nextAction, target_on: targetOn || null }); setEditing(false); toast.success("Project saved") }
    catch (error) { toast.error(error instanceof Error ? error.message : String(error)) }
    finally { setSaving(false) }
  }
  const addTask = async (event: React.FormEvent, milestoneId: string | null = null) => {
    event.preventDefault()
    const key = milestoneId ?? "unassigned"
    const draft = taskDrafts[key] ?? ""
    if (!draft.trim()) return
    try { await createTask({ title: draft.trim(), details: "", status: "todo", priority: "medium", due_on: null, project_id: project.id, milestone_id: milestoneId, agent_id: null }); setTaskDrafts((current) => ({ ...current, [key]: "" })); toast.success("To do added") }
    catch (error) { toast.error(error instanceof Error ? error.message : String(error)) }
  }
  const addStudy = async (event: React.FormEvent) => {
    event.preventDefault()
    if (!newStudy.trim()) return
    try { await createStudy({ title: newStudy.trim(), summary: "", body: "", status: "inbox", category: "general", source_url: "", project_id: project.id, hackathon_host: "" }); setNewStudy(""); toast.success("Study item added") }
    catch (error) { toast.error(error instanceof Error ? error.message : String(error)) }
  }
  const addMilestone = async (event: React.FormEvent) => {
    event.preventDefault()
    if (!newMilestone.trim()) return
    try { await createMilestone({ title: newMilestone.trim(), project_id: project.id, due_on: newMilestoneDue || null, status: "planned" }); setNewMilestone(""); setNewMilestoneDue(""); toast.success("Milestone added") }
    catch (error) { toast.error(error instanceof Error ? error.message : String(error)) }
  }
  const changeMilestone = async (item: WorkspaceMilestone, next: WorkspaceMilestone["status"]) => {
    try { await updateMilestone(item.id, { status: next }) }
    catch (error) { toast.error(error instanceof Error ? error.message : String(error)) }
  }
  const removeMilestone = async (item: WorkspaceMilestone) => {
    if (!window.confirm(`Delete milestone “${item.title}”? Its to dos will remain in this project.`)) return
    try { await deleteMilestone(item.id) }
    catch (error) { toast.error(error instanceof Error ? error.message : String(error)) }
  }
  const toggleTask = async (id: string, done: boolean) => {
    try { await updateTask(id, { status: done ? "todo" : "done" }) }
    catch (error) { toast.error(error instanceof Error ? error.message : String(error)) }
  }
  return <WorkspacePage title={project.title} action={<Button size="sm" variant="outline" onClick={() => { setTitle(project.title); setDescription(project.description); setStatus(project.status); setGoal(project.goal); setNextAction(project.next_action); setTargetOn(project.target_on ?? ""); setEditing((value) => !value) }}>{editing ? "Close editor" : "Edit project"}</Button>}>
    <nav className="flex items-center gap-1 text-xs text-muted-foreground"><button className="hover:text-foreground inline-flex items-center gap-1" onClick={() => { window.location.hash = "#/projects" }}><ArrowLeft className="h-3 w-3" />Projects</button><ChevronRight className="h-3 w-3" /><span className="text-foreground truncate">{project.title}</span></nav>
    <div className="max-w-5xl space-y-7"><div><div className="flex items-center gap-3"><Folder className="h-8 w-8 text-blue-400" /><h1 className="text-3xl font-semibold tracking-tight">{project.title}</h1></div><div className="mt-3 flex flex-wrap items-center gap-3"><StatePill value={project.status} tone={project.status === "active" ? "blue" : project.status === "done" ? "green" : "neutral"} />{project.target_on && <span className="text-xs text-muted-foreground">Target {formatDate(project.target_on)}</span>}<span className="text-xs text-muted-foreground">{taskDone}/{projectTasks.length} to dos · {projectMilestones.filter((item) => item.status === "done").length}/{projectMilestones.length} milestones</span></div></div>
      {editing ? <form className="space-y-4 rounded-xl border bg-card/40 p-5" onSubmit={(event) => void save(event)}>
        <Field label="Project name"><Input value={title} onChange={(event) => setTitle(event.target.value)} maxLength={200} /></Field>
        <div className="grid sm:grid-cols-2 gap-3"><Field label="Status"><select className={selectClass} value={status} onChange={(event) => setStatus(event.target.value as WorkspaceProject["status"])}><option value="planned">Planned</option><option value="active">Active</option><option value="paused">Paused</option><option value="done">Done</option></select></Field><Field label="Target date"><Input type="date" value={targetOn} onChange={(event) => setTargetOn(event.target.value)} /></Field></div>
        <Field label="Goal"><Input value={goal} onChange={(event) => setGoal(event.target.value)} maxLength={1000} placeholder="What does success look like?" /></Field>
        <Field label="Next action"><Input value={nextAction} onChange={(event) => setNextAction(event.target.value)} maxLength={1000} placeholder="The next concrete step" /></Field>
        <div><p className="mb-1.5 text-xs font-medium text-muted-foreground">Project brief · Novel editor</p><NovelEditor title={title} value={description} onChange={setDescription} minHeight="12rem" /></div>
        <div className="flex justify-end"><Button type="submit" disabled={saving || !title.trim()}><Save className="h-4 w-4 mr-1" />Save project</Button></div>
      </form> : <div className="rounded-xl border bg-card/30 p-5 allow-text-selection">{(project.goal || project.next_action) && <div className="grid sm:grid-cols-2 gap-3 mb-4">{project.goal && <div><p className="text-[11px] uppercase text-muted-foreground mb-1">Goal</p><p className="text-sm">{project.goal}</p></div>}{project.next_action && <div><p className="text-[11px] uppercase text-muted-foreground mb-1">Next action</p><p className="text-sm text-blue-300">{project.next_action}</p></div>}</div>}<div className="prose prose-sm dark:prose-invert max-w-none break-words"><ReactMarkdown remarkPlugins={[remarkGfm]}>{project.description.split("\n\n관련 기록:")[0] || "Add a project brief."}</ReactMarkdown></div><div className="mt-5 pt-4 border-t"><SourceLinks text={project.description} /></div></div>}
      <section className="space-y-3"><h2 className="text-sm font-semibold flex items-center gap-2"><Flag className="h-4 w-4 text-blue-400" />Milestones</h2>
        <div className="grid md:grid-cols-2 gap-3">{projectMilestones.map((milestone) => { const related = projectTasks.filter((task) => task.milestone_id === milestone.id); const completed = related.filter((task) => task.status === "done").length; return <Surface key={milestone.id} className="overflow-hidden"><div className="flex items-center gap-2 p-3 border-b border-border/60"><Flag className="h-4 w-4 text-blue-400" /><span className="flex-1 truncate text-sm font-medium">{milestone.title}</span><button type="button" aria-label={`Delete ${milestone.title}`} className="text-muted-foreground hover:text-destructive" onClick={() => void removeMilestone(milestone)}><Trash2 className="h-3.5 w-3.5" /></button></div><div className="flex items-center justify-between gap-2 px-3 py-2 text-xs text-muted-foreground"><span>{completed}/{related.length} to dos · {milestone.due_on ? formatDate(milestone.due_on) : "No date"}</span><select aria-label={`Status for ${milestone.title}`} className="rounded border bg-muted px-1 py-0.5 text-xs text-foreground" value={milestone.status} onChange={(event) => void changeMilestone(milestone, event.target.value as WorkspaceMilestone["status"])}><option value="planned">Planned</option><option value="doing">Doing</option><option value="done">Done</option></select></div><div className="h-1 bg-foreground/5"><div className="h-full bg-blue-500" style={{ width: `${related.length ? completed / related.length * 100 : milestone.status === "done" ? 100 : 0}%` }} /></div><div className="divide-y divide-border/60">{related.map((task) => <div key={task.id} className="flex items-center gap-2 px-3 py-2 text-sm"><input aria-label={`Complete ${task.title}`} type="checkbox" checked={task.status === "done"} onChange={() => void toggleTask(task.id, task.status === "done")} /><button className="flex-1 truncate text-left hover:text-blue-300" onClick={() => { window.location.hash = `#/tasks/${task.id}` }}>{task.title}</button></div>)}</div><form className="flex gap-2 p-3" onSubmit={(event) => void addTask(event, milestone.id)}><Input aria-label={`Add step to ${milestone.title}`} placeholder="Add a step…" value={taskDrafts[milestone.id] ?? ""} onChange={(event) => setTaskDrafts((current) => ({ ...current, [milestone.id]: event.target.value }))} /><Button type="submit" size="sm" disabled={!taskDrafts[milestone.id]?.trim()}><Plus className="h-4 w-4" /></Button></form></Surface> })}</div>
        <form className="flex flex-wrap gap-2 rounded-xl border border-dashed border-border p-3" onSubmit={(event) => void addMilestone(event)}><Input aria-label="New milestone" className="flex-1 min-w-48" placeholder="New milestone" value={newMilestone} onChange={(event) => setNewMilestone(event.target.value)} maxLength={200} /><Input aria-label="Milestone due date" className="w-40" type="date" value={newMilestoneDue} onChange={(event) => setNewMilestoneDue(event.target.value)} /><Button type="submit" size="sm" disabled={!newMilestone.trim()}><Plus className="h-4 w-4 mr-1" />Add</Button></form>
      </section>
      <section><div className="flex items-center justify-between mb-3"><h2 className="text-sm font-semibold flex items-center gap-2"><Video className="h-4 w-4 text-blue-400" />Videos <span className="text-muted-foreground font-normal">{recordings.length}</span></h2><Button size="sm" variant="outline" onClick={() => { window.location.hash = `#/studio/${project.id}` }}><Video className="h-3.5 w-3.5 mr-1" />Open Screen Studio</Button></div>{recordings.length > 0 && <Surface className="divide-y divide-border/60">{recordings.map((recording) => <button key={recording.id} className="w-full flex items-center gap-3 px-4 py-3 text-left text-sm hover:bg-foreground/[0.035]" onClick={() => { window.location.hash = `#/studio/${project.id}/${recording.id}` }}><Video className="h-4 w-4 text-blue-400" /><span className="flex-1 truncate">{recording.title}</span><span className="text-xs text-muted-foreground">{Math.round(recording.duration)}s</span><ChevronRight className="h-4 w-4 text-muted-foreground" /></button>)}</Surface>}{recordings.length === 0 && <p className="text-xs text-muted-foreground">Record a demo or link an existing video to this project in Screen Studio.</p>}</section>
      <section><div className="flex items-center justify-between mb-3"><h2 className="text-sm font-semibold flex items-center gap-2"><FileText className="h-4 w-4 text-blue-400" />Pages & folders <span className="text-muted-foreground font-normal">{projectPages.length}</span></h2><Button size="sm" variant="outline" onClick={() => setNewPage(true)}><Plus className="h-3.5 w-3.5 mr-1" />New page</Button></div>{projectPages.length ? <Surface className="divide-y divide-border/60">{projectPages.map((page) => <button key={page.id} className="w-full flex items-center gap-3 px-4 py-3 text-left text-sm hover:bg-foreground/[0.035]" onClick={() => { window.location.hash = `#/pages/${page.id}` }}>{page.kind === "folder" ? <Folder className="h-4 w-4 text-blue-400" /> : <FileText className="h-4 w-4 text-blue-400" />}<span className="flex-1 truncate">{page.title}</span><ChevronRight className="h-4 w-4 text-muted-foreground" /></button>)}</Surface> : <EmptyState title="No pages yet" detail="Create a brief, research note, or folder inside this project." />}</section>
      <div className="grid lg:grid-cols-2 gap-5"><section><div className="flex items-center justify-between mb-3"><h2 className="text-sm font-semibold flex items-center gap-2"><CheckSquare2 className="h-4 w-4 text-blue-400" />Other to dos <span className="text-muted-foreground font-normal">{projectTasks.filter((task) => !task.milestone_id).length}</span></h2><button className="text-xs text-muted-foreground hover:text-foreground" onClick={() => { window.location.hash = "#/tasks" }}>Open database</button></div><Surface className="divide-y divide-border/60">{projectTasks.filter((task) => !task.milestone_id).map((task) => <button key={task.id} className="w-full flex items-center gap-2 px-4 py-3 text-left text-sm hover:bg-foreground/[0.035]" onClick={() => { window.location.hash = `#/tasks/${task.id}` }}><span className={`h-4 w-4 rounded border ${task.status === "done" ? "bg-blue-500 border-blue-500" : "border-muted-foreground/50"}`} /><span className="flex-1 truncate">{task.title}</span><StatePill value={task.status} tone={task.status === "doing" ? "blue" : task.status === "done" ? "green" : "neutral"} /></button>)}<form className="flex gap-2 p-3" onSubmit={(event) => void addTask(event)}><Input aria-label="Add project to do" placeholder="Add a to do…" value={taskDrafts.unassigned ?? ""} onChange={(event) => setTaskDrafts((current) => ({ ...current, unassigned: event.target.value }))} /><Button type="submit" size="sm" disabled={!taskDrafts.unassigned?.trim()}><Plus className="h-4 w-4" /></Button></form></Surface></section>
        <section><div className="flex items-center justify-between mb-3"><h2 className="text-sm font-semibold flex items-center gap-2"><BookOpen className="h-4 w-4 text-blue-400" />Study <span className="text-muted-foreground font-normal">{projectStudies.length}</span></h2><button className="text-xs text-muted-foreground hover:text-foreground" onClick={() => { window.location.hash = "#/studies" }}>Open database</button></div><Surface className="divide-y divide-border/60">{projectStudies.map((study) => <button key={study.id} className="w-full flex items-center gap-2 px-4 py-3 text-left text-sm hover:bg-foreground/[0.035]" onClick={() => { window.location.hash = `#/studies/${study.id}` }}><BookOpen className="h-4 w-4 text-muted-foreground" /><span className="flex-1 truncate">{study.title}</span><StatePill value={study.status} tone={study.status === "learning" ? "blue" : "neutral"} /></button>)}<form className="flex gap-2 p-3" onSubmit={(event) => void addStudy(event)}><Input aria-label="Add project study" placeholder="Add a study item…" value={newStudy} onChange={(event) => setNewStudy(event.target.value)} /><Button type="submit" size="sm" disabled={!newStudy.trim()}><Plus className="h-4 w-4" /></Button></form></Surface></section></div>
    </div>
    <NewPageDialog open={newPage} onOpenChange={setNewPage} context={{ space: "projects", project_id: project.id }} />
  </WorkspacePage>
}
