export type ProjectStatus = "planned" | "active" | "paused" | "done"
export type TaskStatus = "todo" | "doing" | "done"
export type StudyStatus = "inbox" | "learning" | "reviewing" | "mastered"
export type StudyCategory = "general" | "hackathon"
export type AgentStatus = "active" | "paused"

interface DatedRecord {
  id: string
  created_at: string
  updated_at: string
}

export interface WorkspaceProject extends DatedRecord {
  title: string
  description: string
  goal: string
  next_action: string
  target_on: string | null
  status: ProjectStatus
}

export interface WorkspaceMilestone extends DatedRecord {
  title: string
  project_id: string
  due_on: string | null
  status: "planned" | "doing" | "done"
}

export interface LearningPath extends DatedRecord {
  title: string
  outcome: string
  category: StudyCategory
  project_id: string | null
}

export type PageSpace = "personal" | "projects" | "learning" | "scout"

export interface WorkspaceDocument extends DatedRecord {
  title: string
  body: string
  kind: "page" | "folder"
  space: PageSpace
  parent_id: string | null
  project_id: string | null
}

export interface WorkspaceAgent extends DatedRecord {
  name: string
  role: string
  launch_url: string
  status: AgentStatus
}

export interface WorkspaceTask extends DatedRecord {
  title: string
  details: string
  status: TaskStatus
  priority: "low" | "medium" | "high"
  due_on: string | null
  project_id: string | null
  milestone_id: string | null
  agent_id: string | null
}

export function compareOpenTasks(a: WorkspaceTask, b: WorkspaceTask): number {
  const due = (a.due_on || "9999").localeCompare(b.due_on || "9999")
  if (due) return due
  if (a.status !== b.status) return a.status === "doing" ? -1 : 1
  const priority = { high: 0, medium: 1, low: 2 }
  return priority[a.priority] - priority[b.priority] || b.updated_at.localeCompare(a.updated_at)
}

export interface StudyItem extends DatedRecord {
  title: string
  summary: string
  body: string
  status: StudyStatus
  category: StudyCategory
  source_url: string
  project_id: string | null
  path_id: string | null
  objective: string
  review_on: string | null
  hackathon_host: string
}

export type ProjectInput = Pick<WorkspaceProject, "title" | "description" | "status"> & Partial<Pick<WorkspaceProject, "goal" | "next_action" | "target_on">>
export type MilestoneInput = Pick<WorkspaceMilestone, "title" | "project_id" | "status" | "due_on">
export type LearningPathInput = Pick<LearningPath, "title" | "outcome" | "category" | "project_id">
export type PageInput = Pick<WorkspaceDocument, "title" | "body" | "kind" | "space" | "parent_id" | "project_id">
export type AgentInput = Pick<WorkspaceAgent, "name" | "role" | "launch_url" | "status">
export type TaskInput = Pick<WorkspaceTask, "title" | "details" | "status" | "priority" | "due_on" | "project_id" | "agent_id"> & Partial<Pick<WorkspaceTask, "milestone_id">>
export type StudyInput = Pick<StudyItem, "title" | "summary" | "body" | "status" | "category" | "source_url" | "project_id" | "hackathon_host"> & Partial<Pick<StudyItem, "path_id" | "objective" | "review_on">>

async function request<T>(path: string, init?: RequestInit): Promise<T> {
  const response = await fetch(`/api/workspace/${path}`, {
    ...init,
    headers: { "content-type": "application/json", ...(init?.headers || {}) },
  })
  if (!response.ok) {
    let message = `${response.status} ${response.statusText}`
    try {
      const body: { error?: string } = await response.json()
      if (body.error) message = body.error
    } catch { /* no JSON response */ }
    throw new Error(message)
  }
  return response.json() as Promise<T>
}

function collection<T, I>(name: string) {
  return {
    list: () => request<T[]>(name),
    create: (value: I) => request<T>(name, { method: "POST", body: JSON.stringify(value) }),
    update: (id: string, value: Partial<I>) => request<T>(`${name}/${id}`, { method: "PATCH", body: JSON.stringify(value) }),
    remove: (id: string) => request<{ ok: true }>(`${name}/${id}`, { method: "DELETE" }),
  }
}

export const workspaceApi = {
  projects: collection<WorkspaceProject, ProjectInput>("projects"),
  milestones: collection<WorkspaceMilestone, MilestoneInput>("milestones"),
  learningPaths: collection<LearningPath, LearningPathInput>("learning_paths"),
  pages: collection<WorkspaceDocument, PageInput>("pages"),
  tasks: collection<WorkspaceTask, TaskInput>("tasks"),
  studies: collection<StudyItem, StudyInput>("studies"),
  agents: collection<WorkspaceAgent, AgentInput>("agents"),
}
