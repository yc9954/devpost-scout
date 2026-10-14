import { useMemo, useState } from "react"
import { CalendarDays, Check, ChevronLeft, ChevronRight, Columns3, List, Plus, Search, Trash2 } from "lucide-react"
import { toast } from "sonner"
import { Button } from "../../components/ui/button"
import { Dialog, DialogContent, DialogDescription, DialogHeader, DialogTitle } from "../../components/ui/dialog"
import { Input } from "../../components/ui/input"
import { useWorkspace } from "../../workspace-context"
import { useHashRoute } from "../../use-hash-route"
import { compareOpenTasks, type TaskInput, type TaskStatus, type WorkspaceTask } from "../../workspace"
import { EmptyState, Field, formatDate, selectClass, SourceLinks, StatePill, Surface, textareaClass, WorkspacePage } from "./workspace-ui"

const statusLabel: Record<TaskStatus, string> = { todo: "To do", doing: "Doing", done: "Done" }

export function TasksView() {
  const hash = useHashRoute()
  const { tasks, projects, agents, updateTask, loading } = useWorkspace()
  const [query, setQuery] = useState("")
  const [status, setStatus] = useState("open")
  const [projectId, setProjectId] = useState("all")
  const [editingId, setEditingId] = useState<string | null>(null)
  const [creating, setCreating] = useState(false)
  const [viewMode, setViewMode] = useState<"table" | "board" | "calendar">("table")
  const [calendarMonth, setCalendarMonth] = useState(() => new Date(new Date().getFullYear(), new Date().getMonth(), 1))
  const rows = useMemo(() => tasks.filter((task) =>
    (status === "all" || (status === "open" ? task.status !== "done" : task.status === status)) &&
    (projectId === "all" || task.project_id === projectId) &&
    `${task.title} ${task.details}`.toLowerCase().includes(query.toLowerCase().trim()),
  ).sort((a, b) => {
    if (a.status === "done" && b.status !== "done") return 1
    if (b.status === "done" && a.status !== "done") return -1
    return compareOpenTasks(a, b)
  }), [tasks, status, projectId, query])
  const routeId = hash.match(/^#\/tasks\/([a-f0-9]{32})$/)?.[1]
  const selected = tasks.find((task) => task.id === (routeId ?? editingId)) ?? null
  const closeEditor = () => { setCreating(false); setEditingId(null); if (routeId) window.location.hash = "#/tasks" }
  const now = new Date()
  const today = `${now.getFullYear()}-${String(now.getMonth() + 1).padStart(2, "0")}-${String(now.getDate()).padStart(2, "0")}`

  const toggle = async (task: WorkspaceTask) => {
    try { await updateTask(task.id, { status: task.status === "done" ? "todo" : "done" }) }
    catch (e) { toast.error(e instanceof Error ? e.message : String(e)) }
  }
  const move = async (task: WorkspaceTask, next: TaskStatus) => {
    try { await updateTask(task.id, { status: next }) }
    catch (e) { toast.error(e instanceof Error ? e.message : String(e)) }
  }

  return <WorkspacePage title="To Do" description="Track next actions across all projects and assign work to your agents." action={<Button size="sm" onClick={() => setCreating(true)}><Plus className="h-4 w-4 mr-1" />New to do</Button>}>
    <div className="flex flex-wrap gap-2 items-center">
      <div className="relative flex-1 min-w-48 max-w-sm"><Search className="absolute left-3 top-2.5 h-4 w-4 text-muted-foreground" /><Input aria-label="Search to dos" className="pl-9" placeholder="Search to dos" value={query} onChange={(e) => setQuery(e.target.value)} /></div>
      <select aria-label="Filter to dos by status" className={`${selectClass} !w-32`} value={status} onChange={(e) => setStatus(e.target.value)}><option value="open">Open</option><option value="all">All</option>{Object.entries(statusLabel).map(([value, label]) => <option key={value} value={value}>{label}</option>)}</select>
      <select aria-label="Filter to dos by project" className={`${selectClass} !w-44`} value={projectId} onChange={(e) => setProjectId(e.target.value)}><option value="all">All projects</option>{projects.map((project) => <option key={project.id} value={project.id}>{project.title}</option>)}</select>
      <span className="text-xs text-muted-foreground ml-auto">{rows.length} to dos</span>
    </div>
    <div role="tablist" aria-label="To Do views" className="flex items-center gap-1 border-b border-border/70 pb-2">{([["table", List, "Table"], ["board", Columns3, "Board"], ["calendar", CalendarDays, "Calendar"]] as const).map(([mode, Icon, label]) => <button key={mode} role="tab" aria-selected={viewMode === mode} type="button" className={`px-3 py-1.5 rounded-md text-xs flex items-center gap-1.5 ${viewMode === mode ? "bg-blue-500/10 text-blue-300" : "text-muted-foreground hover:bg-foreground/5"}`} onClick={() => { setViewMode(mode); if (mode === "board") setStatus("all") }}><Icon className="h-3.5 w-3.5" />{label}</button>)}</div>
    {viewMode === "table" && (rows.length ? <Surface className="divide-y divide-border/70 overflow-hidden"><div className="hidden sm:grid grid-cols-[minmax(0,1fr)_110px_90px_100px] gap-3 px-4 py-2 bg-muted/30 text-[11px] font-medium text-muted-foreground"><span>Name / project</span><span>Due</span><span>Priority</span><span>Status</span></div>{rows.map((task) => {
      const project = projects.find((p) => p.id === task.project_id)
      const agent = agents.find((a) => a.id === task.agent_id)
      const overdue = task.due_on && task.due_on < today && task.status !== "done"
      return <div key={task.id} className="flex items-center gap-3 px-4 py-3 hover:bg-foreground/[0.035]">
        <button type="button" aria-label={task.status === "done" ? `Reopen ${task.title}` : `Complete ${task.title}`} onClick={() => void toggle(task)} className={`h-[18px] w-[18px] rounded border flex items-center justify-center flex-shrink-0 ${task.status === "done" ? "bg-blue-600 border-blue-600 text-white" : "border-muted-foreground/50 hover:border-blue-400"}`}>{task.status === "done" && <Check className="h-3.5 w-3.5" />}</button>
        <button type="button" className="flex-1 min-w-0 text-left" onClick={() => setEditingId(task.id)}><span className={`text-sm block truncate ${task.status === "done" ? "line-through text-muted-foreground" : ""}`}>{task.title}</span><span className="text-[11px] text-muted-foreground flex gap-2 mt-0.5">{project && <span>{project.title}</span>}{agent && <span>→ {agent.name}</span>}{task.details && !project && !agent && <span className="truncate">{task.details}</span>}</span></button>
        <div className="hidden sm:grid grid-cols-[110px_90px_100px] gap-3 items-center"><span className={`text-[11px] ${overdue ? "text-amber-400" : "text-muted-foreground"}`}>{task.due_on ? formatDate(task.due_on) : "—"}</span><span className="text-[11px] text-muted-foreground capitalize">{task.priority}</span><StatePill value={statusLabel[task.status]} tone={task.status === "done" ? "green" : task.status === "doing" ? "blue" : "neutral"} /></div>
      </div>
    })}</Surface> : <EmptyState title={loading ? "Loading to dos…" : "No to dos here"} detail="Add a task or change your filters." action={!loading && <Button size="sm" variant="outline" onClick={() => setCreating(true)}>Add a to do</Button>} />)}
    {viewMode === "board" && <div className="grid md:grid-cols-3 gap-3 items-start">{(["todo", "doing", "done"] as const).map((column) => { const items = rows.filter((task) => task.status === column); return <section key={column} className="rounded-xl border border-border/70 bg-card/30 min-h-44"><div className="flex items-center justify-between px-3 py-2 border-b border-border/70"><h2 className="text-xs font-semibold">{statusLabel[column]}</h2><span className="text-xs text-muted-foreground">{items.length}</span></div><div className="p-2 space-y-2 max-h-[65vh] overflow-y-auto">{items.map((task) => <div key={task.id} className="rounded-lg border border-border/70 bg-background/80 p-3"><button className="w-full text-left text-sm font-medium hover:text-blue-300" onClick={() => setEditingId(task.id)}>{task.title}</button><div className="flex items-center gap-2 text-[11px] text-muted-foreground mt-2"><span className="capitalize">{task.priority}</span>{task.due_on && <span>{formatDate(task.due_on)}</span>}</div><div className="flex items-center gap-2 mt-3">{column !== "todo" && <button type="button" className="text-[11px] text-muted-foreground hover:text-foreground" onClick={() => void move(task, column === "done" ? "doing" : "todo")}>← Move back</button>}{column !== "done" && <button type="button" className="text-[11px] text-blue-400 hover:underline ml-auto" onClick={() => void move(task, column === "todo" ? "doing" : "done")}>{column === "todo" ? "Start →" : "Complete →"}</button>}</div></div>)}</div></section> })}</div>}
    {viewMode === "calendar" && <TaskCalendar tasks={rows} month={calendarMonth} onMonthChange={setCalendarMonth} onOpen={(id) => setEditingId(id)} />}
    <Dialog open={creating || !!selected} onOpenChange={(open) => { if (!open) closeEditor() }}>
      <DialogContent className="!max-w-xl max-h-[85vh] overflow-y-auto"><DialogHeader><DialogTitle>{selected ? "Edit to do" : "New to do"}</DialogTitle><DialogDescription>Capture a clear next action.</DialogDescription></DialogHeader><TaskEditor key={selected?.id ?? "new"} task={selected} onClose={closeEditor} /></DialogContent>
    </Dialog>
  </WorkspacePage>
}

function TaskEditor({ task, onClose }: { task: WorkspaceTask | null; onClose: () => void }) {
  const { projects, milestones, agents, createTask, updateTask, deleteTask } = useWorkspace()
  const [form, setForm] = useState<TaskInput>({ title: task?.title ?? "", details: task?.details ?? "", status: task?.status ?? "todo", priority: task?.priority ?? "medium", due_on: task?.due_on ?? null, project_id: task?.project_id ?? null, milestone_id: task?.milestone_id ?? null, agent_id: task?.agent_id ?? null })
  const [saving, setSaving] = useState(false)
  const save = async (event: React.FormEvent) => {
    event.preventDefault()
    if (!form.title.trim()) return toast.error("To do title is required")
    setSaving(true)
    try { if (task) await updateTask(task.id, form); else await createTask(form); toast.success(task ? "To do updated" : "To do created"); onClose() }
    catch (e) { toast.error(e instanceof Error ? e.message : String(e)) }
    finally { setSaving(false) }
  }
  const remove = async () => {
    if (!task || !window.confirm(`Delete “${task.title}”?`)) return
    try { await deleteTask(task.id); toast.success("To do deleted"); onClose() }
    catch (e) { toast.error(e instanceof Error ? e.message : String(e)) }
  }
  return <form onSubmit={(event) => void save(event)} className="space-y-4">
    <Field label="To do"><Input autoFocus value={form.title} onChange={(e) => setForm({ ...form, title: e.target.value })} maxLength={200} placeholder="What needs to happen?" /></Field>
    <Field label="Details"><textarea className={`${textareaClass} min-h-20`} value={form.details} onChange={(e) => setForm({ ...form, details: e.target.value })} maxLength={20000} placeholder="Notes, steps, or a definition of done" /></Field>
    <div className="grid grid-cols-2 gap-3"><Field label="Status"><select className={selectClass} value={form.status} onChange={(e) => setForm({ ...form, status: e.target.value as TaskStatus })}>{Object.entries(statusLabel).map(([value, label]) => <option key={value} value={value}>{label}</option>)}</select></Field><Field label="Priority"><select className={selectClass} value={form.priority} onChange={(e) => setForm({ ...form, priority: e.target.value as TaskInput["priority"] })}><option value="low">Low</option><option value="medium">Medium</option><option value="high">High</option></select></Field></div>
    <div className="grid grid-cols-2 gap-3"><Field label="Due date"><Input type="date" value={form.due_on ?? ""} onChange={(e) => setForm({ ...form, due_on: e.target.value || null })} /></Field><Field label="Project"><select className={selectClass} value={form.project_id ?? ""} onChange={(e) => setForm({ ...form, project_id: e.target.value || null, milestone_id: null })}><option value="">No project</option>{projects.map((project) => <option key={project.id} value={project.id}>{project.title}</option>)}</select></Field></div>
    {form.project_id && <Field label="Milestone"><select className={selectClass} value={form.milestone_id ?? ""} onChange={(e) => setForm({ ...form, milestone_id: e.target.value || null })}><option value="">No milestone</option>{milestones.filter((item) => item.project_id === form.project_id).map((item) => <option key={item.id} value={item.id}>{item.title}</option>)}</select></Field>}
    <Field label="Assigned agent" hint="Agents are a directory and assignment list; external agents need a launch URL."><select className={selectClass} value={form.agent_id ?? ""} onChange={(e) => setForm({ ...form, agent_id: e.target.value || null })}><option value="">Unassigned</option>{agents.map((agent) => <option key={agent.id} value={agent.id}>{agent.name}</option>)}</select></Field>
    <SourceLinks text={form.details} onNavigate={onClose} />
    <div className="flex items-center gap-2 pt-1">{task && <Button type="button" variant="ghost" size="sm" className="text-muted-foreground hover:text-destructive" onClick={() => void remove()}><Trash2 className="h-3.5 w-3.5 mr-1" />Delete</Button>}<div className="ml-auto flex gap-2"><Button type="button" variant="outline" onClick={onClose}>Cancel</Button><Button type="submit" disabled={saving}>{saving ? "Saving…" : "Save to do"}</Button></div></div>
  </form>
}

function TaskCalendar({ tasks, month, onMonthChange, onOpen }: {
  tasks: WorkspaceTask[]
  month: Date
  onMonthChange: (value: Date) => void
  onOpen: (id: string) => void
}) {
  const year = month.getFullYear()
  const monthIndex = month.getMonth()
  const start = new Date(year, monthIndex, 1).getDay()
  const days = new Date(year, monthIndex + 1, 0).getDate()
  const cells = Array.from({ length: Math.ceil((start + days) / 7) * 7 }, (_, index) => index - start + 1)
  const undated = tasks.filter((task) => !task.due_on)
  return <div className="space-y-5"><div className="flex items-center gap-3"><h2 className="text-sm font-semibold flex-1">{month.toLocaleDateString(undefined, { month: "long", year: "numeric" })}</h2><Button size="sm" variant="outline" aria-label="Previous month" onClick={() => onMonthChange(new Date(year, monthIndex - 1, 1))}><ChevronLeft className="h-4 w-4" /></Button><Button size="sm" variant="outline" onClick={() => onMonthChange(new Date(new Date().getFullYear(), new Date().getMonth(), 1))}>Today</Button><Button size="sm" variant="outline" aria-label="Next month" onClick={() => onMonthChange(new Date(year, monthIndex + 1, 1))}><ChevronRight className="h-4 w-4" /></Button></div>
    <div className="grid grid-cols-7 gap-px overflow-hidden rounded-xl border border-border/70 bg-border/70">{["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"].map((day) => <div key={day} className="bg-card px-2 py-2 text-[11px] font-medium text-muted-foreground">{day}</div>)}{cells.map((day, index) => {
      const date = day >= 1 && day <= days ? `${year}-${String(monthIndex + 1).padStart(2, "0")}-${String(day).padStart(2, "0")}` : ""
      const due = date ? tasks.filter((task) => task.due_on === date) : []
      return <div key={index} className={`bg-background min-h-24 p-1.5 ${date ? "" : "opacity-30"}`}><span className="text-[11px] text-muted-foreground">{date ? day : ""}</span><div className="space-y-1 mt-1">{due.map((task) => <button key={task.id} type="button" className={`block w-full truncate rounded px-1.5 py-1 text-left text-[11px] ${task.status === "done" ? "bg-emerald-500/10 text-emerald-300" : "bg-blue-500/10 text-blue-300"}`} onClick={() => onOpen(task.id)}>{task.title}</button>)}</div></div>
    })}</div>
    {undated.length > 0 && <section><h2 className="text-sm font-semibold mb-2">No due date <span className="text-muted-foreground font-normal">{undated.length}</span></h2><Surface className="divide-y divide-border/60 max-h-64 overflow-y-auto">{undated.map((task) => <button key={task.id} type="button" className="block w-full text-left px-3 py-2 text-xs hover:bg-foreground/5" onClick={() => onOpen(task.id)}>{task.title}</button>)}</Surface></section>}
  </div>
}
