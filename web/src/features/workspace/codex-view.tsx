import { useCallback, useEffect, useRef, useState } from "react"
import { Bot, Plus, Send, Trash2 } from "lucide-react"
import { toast } from "sonner"
import { Button } from "../../components/ui/button"
import { Markdown } from "../chat/markdown"
import { codexApi } from "../../codex"
import type { CodexChatSummary, CodexMessage, CodexStatus } from "../../codex"
import { useHashRoute } from "../../use-hash-route"
import { StatePill } from "./workspace-ui"

const SUGGESTIONS = ["내 프로젝트와 할 일을 요약해줘", "지금 공부 중인 주제를 정리해줘", "해커톤 공부 계획을 세워줘"]

export function CodexView() {
  const hash = useHashRoute()
  const [status, setStatus] = useState<CodexStatus | null>(null)
  const [chats, setChats] = useState<CodexChatSummary[]>([])
  const [activeId, setActiveId] = useState<string | null>(null)
  const [messages, setMessages] = useState<CodexMessage[]>([])
  const [draft, setDraft] = useState("")
  const [loading, setLoading] = useState(false)
  const [working, setWorking] = useState(false)
  const [streaming, setStreaming] = useState(false)
  const bottomRef = useRef<HTMLDivElement>(null)

  const reloadChats = useCallback(async () => {
    setChats(await codexApi.chats())
    window.dispatchEvent(new Event("workspace:codex-chats-updated"))
  }, [])
  useEffect(() => {
    void codexApi.status().then(setStatus).catch((error: Error) => setStatus({ ready: false, message: error.message }))
    void reloadChats().catch((error: Error) => toast.error(error.message))
  }, [reloadChats])
  useEffect(() => { bottomRef.current?.scrollIntoView({ behavior: "smooth", block: "end" }) }, [messages, streaming])

  const open = useCallback(async (id: string) => {
    if (working) return
    setActiveId(id)
    setMessages([])
    setLoading(true)
    try { setMessages((await codexApi.chat(id)).messages) }
    catch (error) { toast.error(error instanceof Error ? error.message : String(error)) }
    finally { setLoading(false) }
  }, [working])
  useEffect(() => {
    if (hash !== window.location.hash) return
    const id = hash.match(/^#\/codex\/([a-f0-9]{32})$/)?.[1] ?? null
    if (id && id !== activeId && !working) void open(id)
    else if (!id && activeId && !working) { setActiveId(null); setMessages([]) }
  }, [hash, activeId, working, open])

  const create = useCallback(async () => {
    if (working) return null
    try {
      const chat = await codexApi.create()
      setChats((current) => [chat, ...current])
      setActiveId(chat.id)
      setMessages([])
      window.location.hash = `#/codex/${chat.id}`
      window.dispatchEvent(new Event("workspace:codex-chats-updated"))
      return chat.id
    } catch (error) {
      toast.error(error instanceof Error ? error.message : String(error))
      return null
    }
  }, [working])

  const send = useCallback(async (text: string) => {
    const value = text.trim()
    if (!value || working || !status?.ready) return
    setWorking(true)
    setDraft("")
    let id = activeId
    try {
      if (!id) {
        const chat = await codexApi.create()
        id = chat.id
        setChats((current) => [chat, ...current])
        setActiveId(id)
        setMessages([])
        window.location.hash = `#/codex/${id}`
        window.dispatchEvent(new Event("workspace:codex-chats-updated"))
      }
      const pendingId = `pending-${Date.now()}`
      const timestamp = new Date().toISOString()
      setMessages((current) => [...current,
        { id: `user-${timestamp}`, role: "user", text: value, created_at: timestamp },
        { id: pendingId, role: "assistant", text: "", created_at: timestamp },
      ])
      setStreaming(true)
      for await (const event of codexApi.send(id, value)) {
        if (event.type === "delta") {
          const delta = (event.data as { text: string }).text
          setMessages((current) => current.map((item) => item.id === pendingId ? { ...item, text: item.text + delta } : item))
        } else if (event.type === "done") {
          const finalText = (event.data as { text: string }).text
          setMessages((current) => current.map((item) => item.id === pendingId ? { ...item, text: finalText } : item))
        } else if (event.type === "error") {
          throw new Error((event.data as { message: string }).message)
        }
      }
    } catch (error) {
      toast.error("Codex reply failed", { description: error instanceof Error ? error.message : String(error) })
    } finally {
      setStreaming(false)
      setWorking(false)
      if (id) {
        try { setMessages((await codexApi.chat(id)).messages); await reloadChats() }
        catch { /* keep the streamed reply visible if refreshing fails */ }
      }
    }
  }, [activeId, working, status, reloadChats])

  const remove = async () => {
    if (!activeId || working || !window.confirm("Delete this Codex chat from the workspace?")) return
    try {
      await codexApi.remove(activeId)
      setActiveId(null)
      setMessages([])
      window.location.hash = "#/codex"
      await reloadChats()
    } catch (error) { toast.error(error instanceof Error ? error.message : String(error)) }
  }

  const submit = (event: React.FormEvent) => { event.preventDefault(); void send(draft) }
  const title = chats.find((chat) => chat.id === activeId)?.title || "New chat"

  return <div className="flex flex-col h-full min-h-0">
    <div className="h-12 flex items-center px-5 gap-3 shrink-0 border-b border-border/60">
      <span className="text-sm font-semibold pl-6 md:pl-0">Codex</span>
      <span className="text-xs text-muted-foreground hidden sm:inline">Your local workspace assistant</span>
      <div className="ml-auto flex items-center gap-2"><StatePill value={status?.ready ? "Connected" : status ? "Unavailable" : "Checking"} tone={status?.ready ? "green" : "amber"} /><Button size="icon" variant="ghost" className="h-7 w-7" aria-label="New Codex chat" disabled={working} onClick={() => void create()}><Plus className="h-4 w-4" /></Button></div>
    </div>
    <div className="flex-1 min-w-0 min-h-0 flex flex-col">
        <div className="h-10 px-4 border-b border-border/40 flex items-center gap-2 shrink-0"><span className="text-sm font-medium truncate">{activeId ? title : "Codex chat"}</span><span className="ml-auto text-[11px] text-muted-foreground">Read only · local SDK</span>{activeId && <Button size="icon" variant="ghost" className="h-6 w-6 text-muted-foreground" aria-label="Delete Codex chat" disabled={working} onClick={() => void remove()}><Trash2 className="h-3.5 w-3.5" /></Button>}</div>
        <div className="flex-1 min-h-0 overflow-y-auto allow-text-selection select-text">
          {loading ? <p className="max-w-2xl mx-auto px-5 py-8 text-sm text-muted-foreground">Loading chat…</p> : messages.length === 0 ? <div className="min-h-full flex items-center justify-center px-5 py-10"><div className="max-w-lg text-center space-y-4"><div className="h-11 w-11 rounded-xl bg-blue-600 text-white flex items-center justify-center mx-auto"><Bot className="h-6 w-6" /></div><h1 className="text-lg font-semibold">Work with Codex</h1><p className="text-sm text-muted-foreground">Ask about your projects, to dos and study notes. Codex sees the current workspace index and can read details locally.</p><div className="flex flex-wrap justify-center gap-2">{SUGGESTIONS.map((item) => <button key={item} type="button" disabled={!status?.ready || working} onClick={() => void send(item)} className="rounded-full border border-border px-3 py-1.5 text-xs text-muted-foreground hover:text-foreground hover:bg-foreground/5 disabled:opacity-50">{item}</button>)}</div></div></div> : <div className="max-w-2xl mx-auto px-4 py-5 space-y-5">{messages.map((message) => message.role === "user" ? <div key={message.id} className="flex justify-end"><div className="max-w-[85%] rounded-xl bg-foreground/8 px-3 py-2 text-sm whitespace-pre-wrap">{message.text}</div></div> : message.role === "error" ? <div key={message.id} className="rounded-lg border border-destructive/40 bg-destructive/10 px-3 py-2 text-xs text-destructive">{message.text}</div> : <div key={message.id} className="px-1 py-1">{message.text ? <Markdown content={message.text} isStreaming={streaming && message.id.startsWith("pending-")} /> : <span className="text-xs text-muted-foreground animate-pulse">Codex is thinking…</span>}</div>)}<div ref={bottomRef} /></div>}
        </div>
        <div className="shrink-0 border-t border-border/50 px-4 py-3"><form onSubmit={submit} className="max-w-2xl mx-auto"><div className="rounded-xl border border-input bg-muted/40 p-2 flex items-end gap-2"><textarea aria-label="Message Codex" value={draft} disabled={!status?.ready || working} onChange={(event) => setDraft(event.target.value)} onKeyDown={(event) => { if (event.key === "Enter" && !event.shiftKey && !event.nativeEvent.isComposing) { event.preventDefault(); void send(draft) } }} rows={2} maxLength={10000} placeholder={status?.ready ? "Ask Codex about your workspace…" : "Codex is unavailable"} className="flex-1 resize-none bg-transparent outline-none px-1 py-1 text-sm min-h-12 disabled:opacity-50" /><Button size="icon" type="submit" disabled={!status?.ready || !draft.trim() || working} aria-label="Send to Codex"><Send className="h-4 w-4" /></Button></div><p className="mt-2 text-[11px] text-muted-foreground">Uses your Codex login and sends the current workspace index with each prompt.</p>{status && !status.ready && <p className="mt-2 text-xs text-amber-400">{status.message}</p>}</form></div>
    </div>
  </div>
}
