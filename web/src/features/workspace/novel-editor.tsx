import { useEffect, useMemo, useRef, useState } from "react"
import { Bold, CheckSquare2, Code2, Heading1, Heading2, Italic, Link2, List, ListOrdered, Quote, Sparkles, Undo2, Redo2 } from "lucide-react"
import {
  Command, EditorCommand, EditorCommandEmpty, EditorCommandItem, EditorCommandList,
  EditorContent, EditorRoot, handleCommandNavigation, Placeholder, StarterKit,
  TaskItem, TaskList, TiptapImage, TiptapLink, TiptapUnderline, useEditor,
  createSuggestionItems, renderItems, type JSONContent,
} from "novel"
import { Markdown } from "tiptap-markdown"
import { DOMParser as ProseMirrorDOMParser } from "@tiptap/pm/model"
import { codexApi, type WritingRequest } from "../../codex"

const suggestions = createSuggestionItems([
  { title: "Text", description: "Paragraph", icon: <span>¶</span>, command: ({ editor, range }) => { editor.chain().focus().deleteRange(range).setParagraph().run() } },
  { title: "Heading 1", description: "Main section", icon: <Heading1 size={16} />, command: ({ editor, range }) => { editor.chain().focus().deleteRange(range).setHeading({ level: 1 }).run() } },
  { title: "Heading 2", description: "Subsection", icon: <Heading2 size={16} />, command: ({ editor, range }) => { editor.chain().focus().deleteRange(range).setHeading({ level: 2 }).run() } },
  { title: "Bulleted list", description: "Group ideas", icon: <List size={16} />, command: ({ editor, range }) => { editor.chain().focus().deleteRange(range).toggleBulletList().run() } },
  { title: "Numbered list", description: "Ordered steps", icon: <ListOrdered size={16} />, command: ({ editor, range }) => { editor.chain().focus().deleteRange(range).toggleOrderedList().run() } },
  { title: "Checklist", description: "Track steps in a note", icon: <CheckSquare2 size={16} />, command: ({ editor, range }) => { editor.chain().focus().deleteRange(range).toggleTaskList().run() } },
  { title: "Quote", description: "Highlight a source", icon: <Quote size={16} />, command: ({ editor, range }) => { editor.chain().focus().deleteRange(range).toggleBlockquote().run() } },
  { title: "Code", description: "Code block", icon: <Code2 size={16} />, command: ({ editor, range }) => { editor.chain().focus().deleteRange(range).toggleCodeBlock().run() } },
])

const extensions = [
  StarterKit,
  Placeholder.configure({ placeholder: "Write here, or type / for blocks…" }),
  TiptapLink.configure({ openOnClick: false, autolink: false }),
  TiptapImage,
  TiptapUnderline,
  TaskList,
  TaskItem.configure({ nested: true }),
  Markdown.configure({ html: false, transformPastedText: false }),
  Command.configure({ suggestion: { items: () => suggestions, render: renderItems } }),
]

function Toolbar({ onAI }: { onAI: () => void }) {
  const { editor } = useEditor()
  if (!editor) return null
  const commands = [
    { label: "Undo", icon: Undo2, active: false, run: () => editor.chain().focus().undo().run() },
    { label: "Redo", icon: Redo2, active: false, run: () => editor.chain().focus().redo().run() },
    { label: "Heading", icon: Heading2, active: editor.isActive("heading", { level: 2 }), run: () => editor.chain().focus().toggleHeading({ level: 2 }).run() },
    { label: "Bold", icon: Bold, active: editor.isActive("bold"), run: () => editor.chain().focus().toggleBold().run() },
    { label: "Italic", icon: Italic, active: editor.isActive("italic"), run: () => editor.chain().focus().toggleItalic().run() },
    { label: "Bulleted list", icon: List, active: editor.isActive("bulletList"), run: () => editor.chain().focus().toggleBulletList().run() },
    { label: "Checklist", icon: CheckSquare2, active: editor.isActive("taskList"), run: () => editor.chain().focus().toggleTaskList().run() },
    { label: "Code", icon: Code2, active: editor.isActive("codeBlock"), run: () => editor.chain().focus().toggleCodeBlock().run() },
  ]
  return <div className="flex flex-wrap items-center gap-0.5 border-b border-border/60 px-2 py-1.5" role="toolbar" aria-label="Writing tools">
    {commands.map(({ label, icon: Icon, active, run }) => <button key={label} type="button" title={label} aria-label={label} aria-pressed={active} className={`rounded-md p-1.5 ${active ? "bg-blue-500/15 text-blue-300" : "text-muted-foreground hover:bg-foreground/10 hover:text-foreground"}`} onMouseDown={(event) => event.preventDefault()} onClick={run}><Icon className="h-4 w-4" /></button>)}
    <button type="button" title="Link" aria-label="Link" className="rounded-md p-1.5 text-muted-foreground hover:bg-foreground/10 hover:text-foreground" onMouseDown={(event) => event.preventDefault()} onClick={() => {
      const href = window.prompt("Link URL", editor.getAttributes("link").href || "https://")
      if (href === null) return
      if (!href.trim()) editor.chain().focus().unsetLink().run()
      else if (/^https?:\/\//i.test(href.trim())) editor.chain().focus().setLink({ href: href.trim() }).run()
    }}><Link2 className="h-4 w-4" /></button>
    <button type="button" title="Write with Codex" aria-label="Write with Codex" className="inline-flex items-center gap-1 rounded-md px-2 py-1.5 text-blue-300 hover:bg-blue-500/10" onMouseDown={(event) => event.preventDefault()} onClick={onAI}><Sparkles className="h-4 w-4" /><span className="text-xs">AI write</span></button>
    <span className="ml-auto px-2 text-[11px] text-muted-foreground">Type / for blocks</span>
  </div>
}

function AIWriter({ title }: { title: string }) {
  const { editor } = useEditor()
  const [open, setOpen] = useState(false)
  const [mode, setMode] = useState<WritingRequest["mode"]>("continue")
  const [instruction, setInstruction] = useState("")
  const [preview, setPreview] = useState("")
  const [error, setError] = useState("")
  const [loading, setLoading] = useState(false)
  const range = useRef<{ from: number; to: number } | null>(null)
  const source = useRef("")
  const aborter = useRef<AbortController | null>(null)
  useEffect(() => () => aborter.current?.abort(), [])
  if (!editor) return null

  const show = () => {
    const selection = editor.state.selection
    const cursor = selection.empty && !editor.isFocused ? editor.state.doc.content.size : selection.from
    range.current = { from: cursor, to: selection.empty ? cursor : selection.to }
    setMode(range.current.from === range.current.to ? "continue" : "rewrite")
    setInstruction("")
    setPreview("")
    setError("")
    setOpen(true)
  }
  const generate = async () => {
    const selection = range.current
    if (!selection || loading) return
    source.current = editor.storage.markdown.getMarkdown()
    const document = editor.state.doc
    const request: WritingRequest = {
      mode, title: title.slice(0, 200), instruction: instruction.trim(),
      before: document.textBetween(0, selection.from, "\n").slice(-8000),
      selected: document.textBetween(selection.from, selection.to, "\n").slice(0, 8000),
      after: document.textBetween(selection.to, document.content.size, "\n").slice(0, 2000),
    }
    if (mode === "custom" && !request.instruction) { setError("Tell Codex what to write."); return }
    if (mode === "rewrite" && !request.selected.trim()) { setError("Select text in the editor first."); return }
    aborter.current?.abort()
    aborter.current = new AbortController()
    setPreview("")
    setError("")
    setLoading(true)
    try {
      for await (const event of codexApi.complete(request, aborter.current.signal)) {
        if (event.type === "delta") setPreview((text) => text + ((event.data as { text?: string }).text ?? ""))
        if (event.type === "done") setPreview((event.data as { text: string }).text)
        if (event.type === "error") throw new Error((event.data as { message?: string }).message || "Codex could not complete the text")
      }
    } catch (cause) {
      if ((cause as Error).name !== "AbortError") setError(cause instanceof Error ? cause.message : String(cause))
    } finally { setLoading(false); aborter.current = null }
  }
  const insert = () => {
    if (!preview.trim() || !range.current) return
    if (editor.storage.markdown.getMarkdown() !== source.current) {
      setError("The document changed while Codex was writing. Generate again to use the current text.")
      return
    }
    const rendered = document.createElement("div")
    rendered.innerHTML = editor.storage.markdown.parser.parse(preview)
    for (const table of rendered.querySelectorAll("table")) {
      const headers = [...table.querySelectorAll("thead th")].map((cell) => cell.textContent?.trim() ?? "")
      const list = document.createElement("ul")
      for (const row of table.querySelectorAll("tbody tr")) {
        const item = document.createElement("li")
        item.textContent = [...row.children].map((cell, index) =>
          `${headers[index] ? `${headers[index]}: ` : ""}${cell.textContent?.trim() ?? ""}`).join(" · ")
        list.append(item)
      }
      table.replaceWith(list)
    }
    const slice = ProseMirrorDOMParser.fromSchema(editor.schema).parseSlice(rendered)
    editor.view.dispatch(editor.state.tr.replaceRange(range.current.from, range.current.to, slice))
    editor.commands.focus()
    setOpen(false)
    setPreview("")
  }
  return <>
    <Toolbar onAI={show} />
    {open && <div className="border-b border-blue-500/20 bg-blue-500/[0.055] p-3 space-y-2" aria-label="Codex writing assistant">
      <div className="flex items-center justify-between"><span className="inline-flex items-center gap-1.5 text-xs font-medium text-blue-300"><Sparkles className="h-3.5 w-3.5" />Write with Codex</span><button type="button" className="text-xs text-muted-foreground hover:text-foreground" onClick={() => { aborter.current?.abort(); setOpen(false) }}>Close</button></div>
      <div className="flex flex-wrap gap-1">{([['continue', 'Continue'], ['rewrite', 'Rewrite selection'], ['outline', 'Outline'], ['custom', 'Custom']] as const).map(([value, label]) => <button key={value} type="button" onClick={() => setMode(value)} className={`rounded px-2 py-1 text-[11px] ${mode === value ? "bg-blue-500/20 text-blue-200" : "text-muted-foreground hover:bg-foreground/10"}`}>{label}</button>)}</div>
      <div className="flex flex-wrap gap-2"><input aria-label="Writing instruction" className="min-w-48 flex-1 rounded-md border border-border bg-background px-2 py-1.5 text-xs focus:outline-none focus:ring-1 focus:ring-blue-500" placeholder="Optional direction, tone, or topic…" value={instruction} maxLength={500} onChange={(event) => setInstruction(event.target.value)} onKeyDown={(event) => { if (event.key === "Enter") { event.preventDefault(); void generate() } }} /><button type="button" disabled={loading} className="rounded-md bg-blue-600 px-3 py-1.5 text-xs text-white disabled:opacity-50" onClick={() => void generate()}>{loading ? "Writing…" : "Generate"}</button>{loading && <button type="button" className="text-xs text-muted-foreground" onClick={() => aborter.current?.abort()}>Stop</button>}</div>
      {error && <p role="alert" className="text-xs text-red-400">{error}</p>}
      {preview && <div className="space-y-2"><pre className="max-h-48 overflow-auto whitespace-pre-wrap rounded-md border border-border bg-background/70 p-3 text-xs font-sans leading-relaxed select-text">{preview}</pre><div className="flex items-center justify-between"><span className="text-[11px] text-muted-foreground">Preview only · inserted text still needs Save{/(?:^|\n)\|[^\n]+\|\n\|?\s*:?-{3,}/.test(preview) ? " · Tables become labeled lists" : ""}</span><button type="button" disabled={loading} className="rounded-md border border-blue-500/40 px-3 py-1 text-xs text-blue-300 disabled:opacity-50" onClick={insert}>{mode === "rewrite" ? "Replace selection" : "Insert at cursor"}</button></div></div>}
      <p className="text-[10px] text-muted-foreground">Uses your signed-in Codex account. Nothing is inserted until you accept it.</p>
    </div>}
  </>
}

export function NovelEditor({ value, onChange, minHeight = "16rem", title = "" }: { value: string; onChange: (markdown: string) => void; minHeight?: string; title?: string }) {
  const sourceOnly = /(?:^|\n)\|[^\n]*\|\n\|?\s*:?-{3,}/.test(value) || /<(?:table|details|iframe|script|style)\b/i.test(value)
  const [mode, setMode] = useState<"rich" | "source">(sourceOnly ? "source" : "rich")
  // Novel types initialContent as JSON, while its Tiptap Markdown extension accepts a Markdown string.
  const initialContent = useMemo(() => value as unknown as JSONContent, [mode])
  return <div className="novel-workspace-editor relative overflow-hidden rounded-lg border border-input bg-muted/40 allow-text-selection">
    <div className="flex items-center gap-1 border-b border-border/60 px-2 py-1.5 text-[11px]"><button type="button" className={`rounded px-2 py-1 ${mode === "rich" ? "bg-blue-500/15 text-blue-300" : "text-muted-foreground"}`} disabled={sourceOnly} onClick={() => setMode("rich")}>Rich text</button><button type="button" className={`rounded px-2 py-1 ${mode === "source" ? "bg-blue-500/15 text-blue-300" : "text-muted-foreground"}`} onClick={() => setMode("source")}>Markdown source</button>{sourceOnly && <span className="ml-auto text-muted-foreground">Source mode preserves tables or embeds</span>}</div>
    {mode === "source" ? <textarea aria-label="Markdown source" className="w-full resize-y bg-transparent px-5 py-4 font-mono text-xs leading-relaxed text-foreground focus:outline-none" style={{ minHeight }} value={value} onChange={(event) => onChange(event.target.value)} maxLength={100000} /> : <EditorRoot key={mode}>
      <EditorContent
        initialContent={initialContent}
        extensions={extensions}
        editorProps={{
          attributes: { class: "prose prose-sm dark:prose-invert max-w-none px-5 py-4 focus:outline-none break-words text-foreground" },
          handleDOMEvents: { keydown: (_view, event) => handleCommandNavigation(event) },
        }}
        className="min-h-48"
        onUpdate={({ editor }) => onChange(editor.storage.markdown.getMarkdown())}
      >
        <AIWriter title={title} />
        <EditorCommand className="z-[100] max-h-72 overflow-y-auto rounded-lg border border-border bg-popover p-1 shadow-xl">
          <EditorCommandEmpty className="px-3 py-2 text-xs text-muted-foreground">No matching block</EditorCommandEmpty>
          <EditorCommandList>{suggestions.map((item) => <EditorCommandItem key={item.title} value={item.title} onCommand={(props) => item.command?.(props)} className="flex items-center gap-3 rounded-md px-3 py-2 text-left text-sm hover:bg-muted aria-selected:bg-muted"><span className="text-blue-400">{item.icon}</span><span><span className="block">{item.title}</span><span className="block text-[11px] text-muted-foreground">{item.description}</span></span></EditorCommandItem>)}</EditorCommandList>
        </EditorCommand>
      </EditorContent>
    </EditorRoot>}
    <style>{`.novel-workspace-editor .ProseMirror { min-height: ${minHeight}; } .novel-workspace-editor .ProseMirror p.is-editor-empty:first-child::before { color: hsl(var(--muted-foreground)); content: attr(data-placeholder); float: left; height: 0; pointer-events: none; } .novel-workspace-editor .ProseMirror ul[data-type="taskList"] { list-style: none; padding-left: 0; } .novel-workspace-editor .ProseMirror ul[data-type="taskList"] li { display: flex; gap: .5rem; align-items: flex-start; } .novel-workspace-editor .ProseMirror ul[data-type="taskList"] li > label { margin-top: .2rem; } .novel-workspace-editor .ProseMirror ul[data-type="taskList"] li > div { flex: 1; }`}</style>
  </div>
}
