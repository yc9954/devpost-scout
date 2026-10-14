import { useMemo, useState } from "react"
import { BookOpen, ChevronRight, FileText, Folder, Pencil, Plus, Trash2 } from "lucide-react"
import ReactMarkdown from "react-markdown"
import remarkGfm from "remark-gfm"
import { toast } from "sonner"
import { Button } from "../../components/ui/button"
import { Dialog, DialogContent, DialogDescription, DialogHeader, DialogTitle } from "../../components/ui/dialog"
import { Input } from "../../components/ui/input"
import { useHashRoute } from "../../use-hash-route"
import { useWorkspace } from "../../workspace-context"
import type { PageInput, PageSpace, WorkspaceDocument } from "../../workspace"
import { EmptyState, Field, selectClass, Surface, WorkspacePage } from "./workspace-ui"
import { NovelEditor } from "./novel-editor"

const spaceNames: Record<PageSpace, string> = {
  personal: "My workspace", projects: "Projects", learning: "Learning", scout: "Devpost Scout",
}

export function NewPageDialog({ open, onOpenChange, context, onCreated }: {
  open: boolean
  onOpenChange: (open: boolean) => void
  context?: { space: PageSpace; project_id?: string | null; parent_id?: string | null }
  onCreated?: (page: WorkspaceDocument) => void
}) {
  const { createPage, projects } = useWorkspace()
  const [title, setTitle] = useState("")
  const [kind, setKind] = useState<"page" | "folder">("page")
  const [space, setSpace] = useState<PageSpace>(context?.space ?? "personal")
  const [projectId, setProjectId] = useState(context?.project_id ?? "")
  const [saving, setSaving] = useState(false)
  const fixed = !!context
  const submit = async (event: React.FormEvent) => {
    event.preventDefault()
    if (!title.trim()) return
    setSaving(true)
    try {
      const page = await createPage({ title: title.trim(), body: "", kind,
        space: context?.space ?? space,
        project_id: context?.project_id ?? (space === "projects" ? projectId || null : null),
        parent_id: context?.parent_id ?? null })
      setTitle("")
      setKind("page")
      onOpenChange(false)
      if (onCreated) onCreated(page)
      else window.location.hash = `#/pages/${page.id}`
      toast.success(`${kind === "folder" ? "Folder" : "Page"} created`)
    } catch (error) { toast.error(error instanceof Error ? error.message : String(error)) }
    finally { setSaving(false) }
  }
  return <Dialog open={open} onOpenChange={onOpenChange}>
    <DialogContent className="!max-w-md"><DialogHeader><DialogTitle>New page or folder</DialogTitle><DialogDescription>Keep documents inside a space or project.</DialogDescription></DialogHeader>
      <form className="space-y-4" onSubmit={(event) => void submit(event)}>
        <Field label="Name"><Input autoFocus value={title} onChange={(event) => setTitle(event.target.value)} maxLength={200} placeholder="Untitled page" /></Field>
        <div className="grid grid-cols-2 gap-3"><Field label="Type"><select className={selectClass} value={kind} onChange={(event) => setKind(event.target.value as "page" | "folder")}><option value="page">Page</option><option value="folder">Folder</option></select></Field>
          <Field label="Space"><select className={selectClass} value={context?.space ?? space} disabled={fixed} onChange={(event) => { setSpace(event.target.value as PageSpace); setProjectId("") }}>{Object.entries(spaceNames).map(([key, name]) => <option key={key} value={key}>{name}</option>)}</select></Field></div>
        {!fixed && space === "projects" && <Field label="Inside project (optional)"><select className={selectClass} value={projectId} onChange={(event) => setProjectId(event.target.value)}><option value="">Projects root</option>{projects.map((project) => <option key={project.id} value={project.id}>{project.title}</option>)}</select></Field>}
        {context?.project_id && <p className="text-xs text-muted-foreground">Inside {projects.find((item) => item.id === context.project_id)?.title ?? "project"}</p>}
        <div className="flex justify-end gap-2"><Button type="button" variant="outline" onClick={() => onOpenChange(false)}>Cancel</Button><Button type="submit" disabled={saving || !title.trim()}>{saving ? "Creating…" : "Create"}</Button></div>
      </form>
    </DialogContent>
  </Dialog>
}

export function PagesView() {
  const hash = useHashRoute()
  const { pages, projects, updatePage, deletePage, loading } = useWorkspace()
  const id = hash.match(/^#\/pages\/([a-f0-9]{32})$/)?.[1]
  const page = pages.find((item) => item.id === id)
  const [creating, setCreating] = useState(false)
  const [editingId, setEditingId] = useState<string | null>(null)
  const [title, setTitle] = useState("")
  const [body, setBody] = useState("")
  const [saving, setSaving] = useState(false)
  const children = useMemo(() => pages.filter((item) => item.parent_id === id), [pages, id])
  const ancestors = useMemo(() => {
    const result: WorkspaceDocument[] = []
    let parent = page?.parent_id
    while (parent) {
      const found = pages.find((item) => item.id === parent)
      if (!found || result.some((item) => item.id === found.id)) break
      result.unshift(found)
      parent = found.parent_id
    }
    return result
  }, [page, pages])
  const beginEdit = () => { if (page) { setTitle(page.title); setBody(page.body); setEditingId(page.id) } }
  const save = async (event: React.FormEvent) => {
    event.preventDefault()
    if (!page || !title.trim()) return
    setSaving(true)
    try { await updatePage(page.id, { title: title.trim(), body: page.kind === "folder" ? "" : body }); setEditingId(null); toast.success("Page saved") }
    catch (error) { toast.error(error instanceof Error ? error.message : String(error)) }
    finally { setSaving(false) }
  }
  const remove = async () => {
    if (!page || !window.confirm(`Delete “${page.title}”? Its child pages will move to the space root.`)) return
    try { await deletePage(page.id); window.location.hash = page.project_id ? `#/projects/${page.project_id}` : "#/pages"; toast.success("Page deleted") }
    catch (error) { toast.error(error instanceof Error ? error.message : String(error)) }
  }

  if (!id) return <WorkspacePage title="Pages" description="Documents and folders across your workspace." action={<Button size="sm" onClick={() => setCreating(true)}><Plus className="h-4 w-4 mr-1" />New page</Button>}>
    <div className="grid sm:grid-cols-2 lg:grid-cols-3 gap-3">{pages.filter((item) => !item.parent_id && !item.project_id).map((item) => <Surface key={item.id} className="p-4" onClick={() => { window.location.hash = `#/pages/${item.id}` }}><div className="flex items-center gap-2">{item.kind === "folder" ? <Folder className="h-4 w-4 text-blue-400" /> : <FileText className="h-4 w-4 text-blue-400" />}<span className="text-sm font-medium truncate">{item.title}</span></div><p className="text-xs text-muted-foreground mt-2">{spaceNames[item.space]}</p></Surface>)}</div>
    {!pages.length && <EmptyState title={loading ? "Loading pages…" : "No pages yet"} detail="Create a page inside a space or project." action={<Button size="sm" variant="outline" onClick={() => setCreating(true)}>New page</Button>} />}
    <NewPageDialog open={creating} onOpenChange={setCreating} />
  </WorkspacePage>

  if (!page) return <WorkspacePage title="Page" description="This page is unavailable."><EmptyState title={loading ? "Loading…" : "Page not found"} detail="Select a page from the sidebar." /></WorkspacePage>

  const project = projects.find((item) => item.id === page.project_id)
  return <WorkspacePage title={page.title} action={<div className="flex gap-2"><Button size="sm" variant="outline" onClick={() => setCreating(true)}><Plus className="h-4 w-4 mr-1" />Child</Button><Button size="sm" variant="outline" onClick={beginEdit}><Pencil className="h-4 w-4 mr-1" />Edit</Button></div>}>
    <nav className="flex items-center gap-1 text-xs text-muted-foreground flex-wrap" aria-label="Page breadcrumb"><button className="hover:text-foreground" onClick={() => { window.location.hash = page.project_id ? "#/projects" : "#/pages" }}>{spaceNames[page.space]}</button>{project && <><ChevronRight className="h-3 w-3" /><button className="hover:text-foreground" onClick={() => { window.location.hash = `#/projects/${project.id}` }}>{project.title}</button></>}{ancestors.map((item) => <span key={item.id} className="inline-flex items-center gap-1"><ChevronRight className="h-3 w-3" /><button className="hover:text-foreground" onClick={() => { window.location.hash = `#/pages/${item.id}` }}>{item.title}</button></span>)}<ChevronRight className="h-3 w-3" /><span className="text-foreground">{page.title}</span></nav>
    <div className="max-w-3xl space-y-6"><div><div className="flex items-center gap-3 text-blue-400">{page.kind === "folder" ? <Folder className="h-7 w-7" /> : <BookOpen className="h-7 w-7" />}<h1 className="text-3xl font-semibold tracking-tight text-foreground">{page.title}</h1></div><p className="text-xs text-muted-foreground mt-3">{page.kind === "folder" ? "Folder" : "Page"} · {spaceNames[page.space]}</p></div>
      {editingId === page.id ? <form className="space-y-4" onSubmit={(event) => void save(event)}><Field label="Title"><Input value={title} onChange={(event) => setTitle(event.target.value)} maxLength={200} /></Field>{page.kind === "page" && <div><p className="mb-1.5 text-xs font-medium text-muted-foreground">Page content · Novel editor</p><NovelEditor key={page.id} title={title} value={body} onChange={setBody} minHeight="45vh" /></div>}<div className="flex items-center gap-2"><Button type="button" variant="ghost" size="sm" className="text-destructive" onClick={() => void remove()}><Trash2 className="h-4 w-4 mr-1" />Delete</Button><div className="ml-auto flex gap-2"><Button type="button" variant="outline" onClick={() => setEditingId(null)}>Cancel</Button><Button type="submit" disabled={saving || !title.trim()}>{saving ? "Saving…" : "Save page"}</Button></div></div></form> : page.kind === "page" && <article className="prose dark:prose-invert prose-sm max-w-none min-h-48 break-words allow-text-selection rounded-xl border border-border/60 bg-card/30 px-6 py-5" onClick={!page.body ? beginEdit : undefined}>{page.body ? <ReactMarkdown remarkPlugins={[remarkGfm]}>{page.body}</ReactMarkdown> : <p className="text-muted-foreground">Click Edit to start writing this page.</p>}</article>}
      <section><div className="flex items-center justify-between mb-3"><h2 className="text-sm font-semibold">Inside this {page.kind}</h2><span className="text-xs text-muted-foreground">{children.length} items</span></div>{children.length ? <Surface className="divide-y divide-border/60">{children.map((child) => <button key={child.id} className="w-full flex items-center gap-3 px-4 py-3 text-left text-sm hover:bg-foreground/[0.035]" onClick={() => { window.location.hash = `#/pages/${child.id}` }}>{child.kind === "folder" ? <Folder className="h-4 w-4 text-blue-400" /> : <FileText className="h-4 w-4 text-blue-400" />}<span className="flex-1 truncate">{child.title}</span><ChevronRight className="h-4 w-4 text-muted-foreground" /></button>)}</Surface> : <EmptyState title="No child pages" detail="Add a page or folder to organize this area." action={<Button size="sm" variant="outline" onClick={() => setCreating(true)}>Add child</Button>} />}</section>
    </div>
    <NewPageDialog open={creating} onOpenChange={setCreating} context={{ space: page.space, project_id: page.project_id, parent_id: page.id }} />
  </WorkspacePage>
}
