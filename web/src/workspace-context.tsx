import { createContext, useCallback, useContext, useEffect, useMemo, useState } from "react"
import { workspaceApi } from "./workspace"
import type {
  AgentInput, LearningPath, LearningPathInput, MilestoneInput, PageInput, ProjectInput, StudyInput, TaskInput,
  StudyItem, WorkspaceAgent, WorkspaceDocument, WorkspaceMilestone, WorkspaceProject, WorkspaceTask,
} from "./workspace"

interface WorkspaceContextValue {
  projects: WorkspaceProject[]
  milestones: WorkspaceMilestone[]
  learningPaths: LearningPath[]
  pages: WorkspaceDocument[]
  tasks: WorkspaceTask[]
  studies: StudyItem[]
  agents: WorkspaceAgent[]
  loading: boolean
  error: string | null
  reload: () => Promise<void>
  createProject: (data: ProjectInput) => Promise<WorkspaceProject>
  updateProject: (id: string, data: Partial<ProjectInput>) => Promise<WorkspaceProject>
  deleteProject: (id: string) => Promise<void>
  createMilestone: (data: MilestoneInput) => Promise<WorkspaceMilestone>
  updateMilestone: (id: string, data: Partial<MilestoneInput>) => Promise<WorkspaceMilestone>
  deleteMilestone: (id: string) => Promise<void>
  createLearningPath: (data: LearningPathInput) => Promise<LearningPath>
  updateLearningPath: (id: string, data: Partial<LearningPathInput>) => Promise<LearningPath>
  deleteLearningPath: (id: string) => Promise<void>
  createPage: (data: PageInput) => Promise<WorkspaceDocument>
  updatePage: (id: string, data: Partial<PageInput>) => Promise<WorkspaceDocument>
  deletePage: (id: string) => Promise<void>
  createTask: (data: TaskInput) => Promise<WorkspaceTask>
  updateTask: (id: string, data: Partial<TaskInput>) => Promise<WorkspaceTask>
  deleteTask: (id: string) => Promise<void>
  createStudy: (data: StudyInput) => Promise<StudyItem>
  updateStudy: (id: string, data: Partial<StudyInput>) => Promise<StudyItem>
  deleteStudy: (id: string) => Promise<void>
  createAgent: (data: AgentInput) => Promise<WorkspaceAgent>
  updateAgent: (id: string, data: Partial<AgentInput>) => Promise<WorkspaceAgent>
  deleteAgent: (id: string) => Promise<void>
}

const WorkspaceContext = createContext<WorkspaceContextValue | null>(null)

function replace<T extends { id: string }>(rows: T[], updated: T) {
  return rows.map((row) => row.id === updated.id ? updated : row)
}

export function WorkspaceProvider({ children }: { children: React.ReactNode }) {
  const [projects, setProjects] = useState<WorkspaceProject[]>([])
  const [milestones, setMilestones] = useState<WorkspaceMilestone[]>([])
  const [learningPaths, setLearningPaths] = useState<LearningPath[]>([])
  const [pages, setPages] = useState<WorkspaceDocument[]>([])
  const [tasks, setTasks] = useState<WorkspaceTask[]>([])
  const [studies, setStudies] = useState<StudyItem[]>([])
  const [agents, setAgents] = useState<WorkspaceAgent[]>([])
  const [loading, setLoading] = useState(true)
  const [error, setError] = useState<string | null>(null)

  const reload = useCallback(async () => {
    setLoading(true)
    try {
      const [p, m, lp, pg, t, s, a] = await Promise.all([
        workspaceApi.projects.list(), workspaceApi.milestones.list(), workspaceApi.learningPaths.list(),
        workspaceApi.pages.list(), workspaceApi.tasks.list(),
        workspaceApi.studies.list(), workspaceApi.agents.list(),
      ])
      setProjects(p)
      setMilestones(m)
      setLearningPaths(lp)
      setPages(pg)
      setTasks(t)
      setStudies(s)
      setAgents(a)
      setError(null)
    } catch (e) {
      setError(e instanceof Error ? e.message : String(e))
    } finally {
      setLoading(false)
    }
  }, [])

  useEffect(() => { void reload() }, [reload])

  const value = useMemo<WorkspaceContextValue>(() => ({
    projects, milestones, learningPaths, pages, tasks, studies, agents, loading, error, reload,
    createProject: async (data) => { const item = await workspaceApi.projects.create(data); setProjects((s) => [item, ...s]); return item },
    updateProject: async (id, data) => { const item = await workspaceApi.projects.update(id, data); setProjects((s) => replace(s, item)); return item },
    deleteProject: async (id) => {
      await workspaceApi.projects.remove(id)
      setProjects((s) => s.filter((x) => x.id !== id))
      setMilestones((s) => s.filter((x) => x.project_id !== id))
      setLearningPaths((s) => s.map((x) => x.project_id === id ? { ...x, project_id: null } : x))
      setPages((s) => s.map((x) => x.project_id === id ? { ...x, project_id: null } : x))
      setTasks((s) => s.map((x) => x.project_id === id ? { ...x, project_id: null, milestone_id: null } : x))
      setStudies((s) => s.map((x) => x.project_id === id ? { ...x, project_id: null } : x))
    },
    createMilestone: async (data) => { const item = await workspaceApi.milestones.create(data); setMilestones((s) => [item, ...s]); return item },
    updateMilestone: async (id, data) => { const item = await workspaceApi.milestones.update(id, data); setMilestones((s) => replace(s, item)); return item },
    deleteMilestone: async (id) => { await workspaceApi.milestones.remove(id); setMilestones((s) => s.filter((x) => x.id !== id)); setTasks((s) => s.map((x) => x.milestone_id === id ? { ...x, milestone_id: null } : x)) },
    createLearningPath: async (data) => { const item = await workspaceApi.learningPaths.create(data); setLearningPaths((s) => [item, ...s]); return item },
    updateLearningPath: async (id, data) => { const item = await workspaceApi.learningPaths.update(id, data); setLearningPaths((s) => replace(s, item)); return item },
    deleteLearningPath: async (id) => { await workspaceApi.learningPaths.remove(id); setLearningPaths((s) => s.filter((x) => x.id !== id)); setStudies((s) => s.map((x) => x.path_id === id ? { ...x, path_id: null } : x)) },
    createPage: async (data) => { const item = await workspaceApi.pages.create(data); setPages((s) => [item, ...s]); return item },
    updatePage: async (id, data) => { const item = await workspaceApi.pages.update(id, data); setPages((s) => replace(s, item)); return item },
    deletePage: async (id) => {
      await workspaceApi.pages.remove(id)
      setPages((s) => s.filter((x) => x.id !== id).map((x) => x.parent_id === id ? { ...x, parent_id: null } : x))
    },
    createTask: async (data) => { const item = await workspaceApi.tasks.create(data); setTasks((s) => [item, ...s]); return item },
    updateTask: async (id, data) => { const item = await workspaceApi.tasks.update(id, data); setTasks((s) => replace(s, item)); return item },
    deleteTask: async (id) => { await workspaceApi.tasks.remove(id); setTasks((s) => s.filter((x) => x.id !== id)) },
    createStudy: async (data) => { const item = await workspaceApi.studies.create(data); setStudies((s) => [item, ...s]); return item },
    updateStudy: async (id, data) => { const item = await workspaceApi.studies.update(id, data); setStudies((s) => replace(s, item)); return item },
    deleteStudy: async (id) => { await workspaceApi.studies.remove(id); setStudies((s) => s.filter((x) => x.id !== id)) },
    createAgent: async (data) => { const item = await workspaceApi.agents.create(data); setAgents((s) => [item, ...s]); return item },
    updateAgent: async (id, data) => { const item = await workspaceApi.agents.update(id, data); setAgents((s) => replace(s, item)); return item },
    deleteAgent: async (id) => {
      await workspaceApi.agents.remove(id)
      setAgents((s) => s.filter((x) => x.id !== id))
      setTasks((s) => s.map((x) => x.agent_id === id ? { ...x, agent_id: null } : x))
    },
  }), [projects, milestones, learningPaths, pages, tasks, studies, agents, loading, error, reload])

  return <WorkspaceContext.Provider value={value}>{children}</WorkspaceContext.Provider>
}

export function useWorkspace() {
  const context = useContext(WorkspaceContext)
  if (!context) throw new Error("WorkspaceProvider is missing")
  return context
}
