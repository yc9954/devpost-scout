import { ArrowRight, Archive, BookOpen, Bot, CheckSquare2, Compass, FolderKanban, Sparkles, Video } from "lucide-react"
import { Button } from "../../components/ui/button"
import { useApp } from "../../store"
import { useWorkspace } from "../../workspace-context"
import { compareOpenTasks } from "../../workspace"
import { EmptyState, formatDate, SectionTitle, StatePill, Surface, WorkspacePage } from "./workspace-ui"

export function OverviewView() {
  const { projects, tasks, studies, agents, loading } = useWorkspace()
  const setView = useApp((s) => s.setView)
  const activeProjects = projects.filter((p) => p.status === "active")
  const openTasks = tasks.filter((t) => t.status !== "done").sort(compareOpenTasks)
  const learning = studies.filter((s) => s.status === "learning" || s.status === "reviewing")

  return <WorkspacePage title="My workspace" description="Spaces hold your projects, pages, databases, conversations, and recordings.">
    <div>
      <div className="mb-4"><p className="text-[11px] uppercase tracking-[0.16em] text-blue-400 font-semibold">Personal workspace</p><h1 className="text-2xl font-semibold tracking-tight mt-1">Your work, in one place</h1></div>
      <div className="grid grid-cols-2 lg:grid-cols-4 gap-2">
        <Metric label="Active projects" value={activeProjects.length} icon={<FolderKanban className="h-4 w-4" />} onClick={() => setView("projects")} />
        <Metric label="Open to dos" value={openTasks.length} icon={<CheckSquare2 className="h-4 w-4" />} onClick={() => setView("tasks")} />
        <Metric label="In progress study" value={learning.length} icon={<BookOpen className="h-4 w-4" />} onClick={() => setView("studies")} />
        <Metric label="Your agents" value={agents.length + 2} icon={<Sparkles className="h-4 w-4" />} onClick={() => setView("agents")} />
      </div>
    </div>

    <section><SectionTitle title="Spaces" hint="Browse your workspace" /><div className="grid sm:grid-cols-2 lg:grid-cols-3 gap-2">
      <SpaceLink label="Projects" detail="Project pages, notes, and related work" icon={<FolderKanban className="h-4 w-4" />} onClick={() => setView("projects")} />
      <SpaceLink label="Learning" detail="Study database and learning pages" icon={<BookOpen className="h-4 w-4" />} onClick={() => setView("studies")} />
      <SpaceLink label="Agents" detail="Codex chat and agent directory" icon={<Bot className="h-4 w-4" />} onClick={() => setView("agents")} />
      <SpaceLink label="Devpost Scout" detail="Hackathons, research, and Scout chat" icon={<Compass className="h-4 w-4" />} onClick={() => setView("dashboard")} />
      <SpaceLink label="Screen Studio" detail="Record and edit your screen" icon={<Video className="h-4 w-4" />} onClick={() => setView("studio")} />
      <SpaceLink label="Collected notes" detail="Search source messages and links" icon={<Archive className="h-4 w-4" />} onClick={() => setView("history")} />
    </div></section>

    <div className="grid lg:grid-cols-[1.3fr_1fr] gap-5">
      <section>
        <SectionTitle title="Next actions" hint={loading ? "Loading…" : `${openTasks.length} open`} action={<TextLink label="All to dos" onClick={() => setView("tasks")} />} />
        {openTasks.length ? <Surface className="divide-y divide-border/60">{openTasks.slice(0, 6).map((task) => <button key={task.id} type="button" className="w-full px-4 py-3 flex items-center gap-3 text-left hover:bg-foreground/[0.035]" onClick={() => setView("tasks")}><span className="h-4 w-4 rounded border border-muted-foreground/40 flex-shrink-0" /><span className="text-sm flex-1 truncate">{task.title}</span>{task.due_on && <span className="text-xs text-muted-foreground">{formatDate(task.due_on)}</span>}<StatePill value={task.status === "doing" ? "Doing" : "To do"} tone={task.status === "doing" ? "blue" : "neutral"} /></button>)}</Surface> : <EmptyState title="No open to dos" detail="Add a task to keep your next action visible." action={<Button size="sm" variant="outline" onClick={() => setView("tasks")}>Open to dos</Button>} />}
      </section>
      <section>
        <SectionTitle title="Learning now" hint={loading ? "Loading…" : `${learning.length} items`} action={<TextLink label="Study library" onClick={() => setView("studies")} />} />
        {learning.length ? <div className="space-y-2">{learning.slice(0, 4).map((study) => <Surface key={study.id} className="block w-full px-4 py-3" onClick={() => setView(study.category === "hackathon" ? "hackathon-study" : "studies")}><div className="flex items-center gap-2"><BookOpen className="h-4 w-4 text-blue-400" /><span className="text-sm font-medium truncate flex-1">{study.title}</span><StatePill value={study.status === "learning" ? "Learning" : "Reviewing"} tone="blue" /></div><p className="text-xs text-muted-foreground line-clamp-1 mt-1 ml-6">{study.summary || (study.category === "hackathon" ? "Hackathon study" : "Study note")}</p></Surface>)}</div> : <EmptyState title="Nothing in progress" detail="Open a study item and mark it as Learning." />}
      </section>
    </div>

    <section><SectionTitle title="Active projects" action={<TextLink label="All projects" onClick={() => setView("projects")} />} />{activeProjects.length ? <div className="grid sm:grid-cols-2 lg:grid-cols-4 gap-2">{activeProjects.slice(0, 4).map((project) => { const related = tasks.filter((task) => task.project_id === project.id); const done = related.filter((task) => task.status === "done").length; return <Surface key={project.id} className="p-4 min-h-28" onClick={() => { window.location.hash = `#/projects/${project.id}` }}><div className="flex items-center gap-2"><FolderKanban className="h-4 w-4 text-blue-400" /><span className="text-sm font-medium truncate">{project.title}</span></div><p className="text-xs text-muted-foreground line-clamp-2 mt-2">{project.description.split("\n\n관련 기록:")[0] || "No description yet"}</p><p className="text-[11px] text-muted-foreground mt-3">{done} / {related.length} tasks done</p></Surface> })}</div> : <EmptyState title="No active projects" detail="Create a project to group tasks and study notes." />}</section>
  </WorkspacePage>
}

function Metric({ label, value, icon, onClick }: { label: string; value: number; icon: React.ReactNode; onClick: () => void }) {
  return <Surface className="p-4 min-h-24 w-full" onClick={onClick}><div className="flex items-center justify-between text-muted-foreground"><span className="text-xs">{label}</span>{icon}</div><div className="text-2xl font-semibold tabular-nums mt-2">{value}</div></Surface>
}

function TextLink({ label, onClick }: { label: string; onClick: () => void }) {
  return <button type="button" onClick={onClick} className="text-xs text-muted-foreground hover:text-foreground flex items-center gap-1">{label}<ArrowRight className="h-3 w-3" /></button>
}

function SpaceLink({ label, detail, icon, onClick }: { label: string; detail: string; icon: React.ReactNode; onClick: () => void }) {
  return <Surface className="p-4 flex items-start gap-3 min-h-20" onClick={onClick}><span className="rounded-lg bg-blue-500/10 text-blue-400 p-2">{icon}</span><span className="min-w-0"><span className="block text-sm font-medium">{label}</span><span className="block text-xs text-muted-foreground mt-1">{detail}</span></span></Surface>
}
