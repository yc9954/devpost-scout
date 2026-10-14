import { useState } from "react"
import { ArrowRight, ExternalLink, Plus, Sparkles, Trash2 } from "lucide-react"
import { toast } from "sonner"
import { Button } from "../../components/ui/button"
import { Dialog, DialogContent, DialogDescription, DialogHeader, DialogTitle } from "../../components/ui/dialog"
import { Input } from "../../components/ui/input"
import { useApp } from "../../store"
import { useWorkspace } from "../../workspace-context"
import type { AgentInput, AgentStatus, WorkspaceAgent } from "../../workspace"
import { Field, selectClass, StatePill, Surface, WorkspacePage } from "./workspace-ui"

export function AgentsView() {
  const { agents, tasks } = useWorkspace()
  const setView = useApp((state) => state.setView)
  const health = useApp((state) => state.health)
  const [creating, setCreating] = useState(false)
  const [editingId, setEditingId] = useState<string | null>(null)
  const selected = agents.find((agent) => agent.id === editingId) ?? null

  return <WorkspacePage title="Agents" description="Codex and Devpost Scout are ready to work with you. Add links for other agents when you connect them later." action={<Button size="sm" onClick={() => setCreating(true)}><Plus className="h-4 w-4 mr-1" />Add agent</Button>}>
    <div className="grid md:grid-cols-2 xl:grid-cols-3 gap-3">
      <Surface className="p-4 min-h-44 flex flex-col"><div className="flex items-start gap-3"><div className="h-9 w-9 rounded-lg bg-blue-600 flex items-center justify-center text-white"><Sparkles className="h-4 w-4" /></div><div><h2 className="text-sm font-semibold">Codex</h2><p className="text-[11px] text-muted-foreground mt-0.5">Built in · personal workspace</p></div><div className="ml-auto"><StatePill value="Local SDK" tone="green" /></div></div><p className="text-xs text-muted-foreground leading-relaxed mt-4">Discuss projects, to dos, and study notes with your locally signed-in Codex. Conversations are saved here.</p><div className="mt-auto pt-4"><Button size="sm" variant="outline" onClick={() => setView("codex")}>Open Codex <ArrowRight className="h-3.5 w-3.5 ml-1" /></Button></div></Surface>
      <Surface className="p-4 min-h-44 flex flex-col"><div className="flex items-start gap-3"><div className="h-9 w-9 rounded-lg bg-blue-600 flex items-center justify-center text-white"><Sparkles className="h-4 w-4" /></div><div><h2 className="text-sm font-semibold">Devpost Scout</h2><p className="text-[11px] text-muted-foreground mt-0.5">Built in · hackathon research</p></div><div className="ml-auto"><StatePill value={health ? health.mode : "Connecting"} tone="blue" /></div></div><p className="text-xs text-muted-foreground leading-relaxed mt-4">Explore events, inspect judging criteria and winning projects, then save what you need to study.</p><div className="mt-auto pt-4 flex gap-2"><Button size="sm" variant="outline" onClick={() => setView("chat")}>Open Scout <ArrowRight className="h-3.5 w-3.5 ml-1" /></Button><Button size="sm" variant="ghost" onClick={() => setView("dashboard")}>Hackathons</Button></div></Surface>
      {agents.map((agent) => { const assigned = tasks.filter((task) => task.agent_id === agent.id && task.status !== "done").length; return <Surface key={agent.id} className="p-4 min-h-44 flex flex-col"><div className="flex items-start gap-3"><div className="h-9 w-9 rounded-lg bg-foreground/5 flex items-center justify-center text-muted-foreground"><Sparkles className="h-4 w-4" /></div><div className="min-w-0 flex-1"><h2 className="text-sm font-semibold truncate">{agent.name}</h2><p className="text-[11px] text-muted-foreground mt-0.5">{assigned} open assigned to dos</p></div><StatePill value={agent.status === "active" ? "Active" : "Paused"} tone={agent.status === "active" ? "green" : "neutral"} /></div><p className="text-xs text-muted-foreground leading-relaxed mt-4 line-clamp-2">{agent.role || "Add a role to describe what this agent helps with."}</p><div className="mt-auto pt-4 flex gap-2"><Button size="sm" variant="outline" onClick={() => setEditingId(agent.id)}>Details</Button>{agent.launch_url && <Button size="sm" variant="ghost" asChild><a href={agent.launch_url} target="_blank" rel="noopener noreferrer">Open <ExternalLink className="h-3.5 w-3.5 ml-1" /></a></Button>}</div></Surface> })}
    </div>
    <p className="text-xs text-muted-foreground">Custom agents are stored as a directory and can be assigned to to dos. Adding a link does not connect the agent to this app's API.</p>
    <Dialog open={creating || !!selected} onOpenChange={(open) => { if (!open) { setCreating(false); setEditingId(null) } }}><DialogContent className="!max-w-xl"><DialogHeader><DialogTitle>{selected ? selected.name : "Add agent"}</DialogTitle><DialogDescription>Add a name, role, and optional link to its own workspace.</DialogDescription></DialogHeader><AgentEditor key={selected?.id ?? "new"} agent={selected} onClose={() => { setCreating(false); setEditingId(null) }} /></DialogContent></Dialog>
  </WorkspacePage>
}

function AgentEditor({ agent, onClose }: { agent: WorkspaceAgent | null; onClose: () => void }) {
  const { createAgent, updateAgent, deleteAgent } = useWorkspace()
  const [form, setForm] = useState<AgentInput>({ name: agent?.name ?? "", role: agent?.role ?? "", launch_url: agent?.launch_url ?? "", status: agent?.status ?? "active" })
  const [saving, setSaving] = useState(false)
  const save = async (event: React.FormEvent) => {
    event.preventDefault()
    if (!form.name.trim()) return toast.error("Agent name is required")
    setSaving(true)
    try { if (agent) await updateAgent(agent.id, form); else await createAgent(form); toast.success(agent ? "Agent updated" : "Agent added"); onClose() }
    catch (e) { toast.error(e instanceof Error ? e.message : String(e)) }
    finally { setSaving(false) }
  }
  const remove = async () => {
    if (!agent || !window.confirm(`Delete “${agent.name}”? Assigned to dos will remain unassigned.`)) return
    try { await deleteAgent(agent.id); toast.success("Agent removed"); onClose() }
    catch (e) { toast.error(e instanceof Error ? e.message : String(e)) }
  }
  return <form onSubmit={(event) => void save(event)} className="space-y-4"><Field label="Name"><Input autoFocus value={form.name} onChange={(e) => setForm({ ...form, name: e.target.value })} maxLength={120} placeholder="Agent name" /></Field><Field label="Role"><Input value={form.role} onChange={(e) => setForm({ ...form, role: e.target.value })} maxLength={500} placeholder="What does this agent do?" /></Field><Field label="Launch URL" hint="An external or local http(s) link to open this agent."><Input type="url" value={form.launch_url} onChange={(e) => setForm({ ...form, launch_url: e.target.value })} placeholder="https://..." /></Field><Field label="Status"><select className={selectClass} value={form.status} onChange={(e) => setForm({ ...form, status: e.target.value as AgentStatus })}><option value="active">Active</option><option value="paused">Paused</option></select></Field><div className="flex items-center gap-2 pt-1">{agent && <Button type="button" variant="ghost" size="sm" className="text-muted-foreground hover:text-destructive" onClick={() => void remove()}><Trash2 className="h-3.5 w-3.5 mr-1" />Delete</Button>}<div className="ml-auto flex gap-2"><Button type="button" variant="outline" onClick={onClose}>Cancel</Button><Button type="submit" disabled={saving}>{saving ? "Saving…" : "Save agent"}</Button></div></div></form>
}
