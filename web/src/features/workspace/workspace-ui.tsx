import type { ReactNode } from "react"
import { cn } from "../../lib/utils"
import { Button } from "../../components/ui/button"
import { useWorkspace } from "../../workspace-context"

export function WorkspacePage({ title, description, action, children }: {
  title: string; description?: string; action?: ReactNode; children: ReactNode
}) {
  const { error, reload } = useWorkspace()
  return (
    <div className="flex flex-col h-full min-h-0">
      <div className="h-12 flex items-center px-5 gap-3 flex-shrink-0 border-b border-border/60">
        <span className="text-sm font-semibold pl-6 md:pl-0">{title}</span>
        <div className="ml-auto">{action}</div>
      </div>
      <div className="flex-1 overflow-y-auto min-h-0">
        <div className="max-w-6xl mx-auto px-5 py-7 pb-12 space-y-6">
          {description && <p className="text-sm text-muted-foreground">{description}</p>}
          {error && (
            <div className="rounded-xl border border-destructive/40 bg-destructive/10 px-4 py-3 flex items-center gap-3">
              <span className="text-sm flex-1">Could not load workspace data: {error}</span>
              <Button variant="outline" size="sm" onClick={() => void reload()}>Retry</Button>
            </div>
          )}
          {children}
        </div>
      </div>
    </div>
  )
}

export function Surface({ children, className, onClick }: { children: ReactNode; className?: string; onClick?: () => void }) {
  const content = cn("rounded-lg border border-border/80 bg-card", className)
  return onClick ? (
    <button type="button" className={cn(content, "text-left hover:border-foreground/25 hover:bg-foreground/[0.035] transition-colors")} onClick={onClick}>{children}</button>
  ) : <div className={content}>{children}</div>
}

export function SectionTitle({ title, hint, action }: { title: string; hint?: string; action?: ReactNode }) {
  return <div className="flex items-center gap-3 mb-3"><h2 className="text-sm font-semibold">{title}</h2>{hint && <span className="text-xs text-muted-foreground">{hint}</span>}<div className="ml-auto">{action}</div></div>
}

export function EmptyState({ title, detail, action }: { title: string; detail: string; action?: ReactNode }) {
  return <div className="rounded-xl border border-dashed border-border px-5 py-10 text-center"><p className="text-sm font-medium">{title}</p><p className="mt-1 text-xs text-muted-foreground">{detail}</p>{action && <div className="mt-4">{action}</div>}</div>
}

export function StatePill({ value, tone = "neutral" }: { value: string; tone?: "neutral" | "blue" | "green" | "amber" }) {
  const colors = {
    neutral: "bg-foreground/5 text-muted-foreground",
    blue: "bg-blue-500/10 text-blue-700",
    green: "bg-emerald-500/10 text-emerald-400",
    amber: "bg-amber-500/10 text-amber-400",
  }
  return <span className={cn("inline-flex items-center rounded-md px-2 py-0.5 text-[11px] font-medium", colors[tone])}>{value}</span>
}

export function Field({ label, children, hint }: { label: string; children: ReactNode; hint?: string }) {
  return <label className="block space-y-1.5"><span className="text-xs font-medium text-muted-foreground">{label}</span>{children}{hint && <span className="block text-[11px] text-muted-foreground/70">{hint}</span>}</label>
}

export function SourceLinks({ text, onNavigate }: { text: string; onNavigate?: () => void }) {
  const seen = new Set<string>()
  const links = text.split("\n").flatMap((line) => {
    const match = line.match(/#\/history\/([a-f0-9]{32})/)
    if (!match || seen.has(match[1])) return []
    seen.add(match[1])
    const label = line.match(/^[-\s]*([\w-]+)\s+(\d{4}-\d{2}-\d{2})/)
    return [{ id: match[1], label: label ? `${label[1]} · ${label[2]}` : "Original record" }]
  })
  if (!links.length) return null
  return <div className="space-y-2"><p className="text-xs font-medium text-muted-foreground">Source records</p><div className="flex flex-wrap gap-2">{links.map((link) => <a key={link.id} href={`#/history/${link.id}`} onClick={onNavigate} className="rounded-md border px-2.5 py-1.5 text-xs text-blue-400 hover:bg-foreground/5 hover:underline">{link.label}</a>)}</div></div>
}

export const selectClass = "flex h-9 w-full rounded-md border border-input bg-muted px-3 py-1 text-sm text-foreground focus:outline-none focus:ring-2 focus:ring-ring"
export const textareaClass = "flex w-full rounded-md border border-input bg-muted px-3 py-2 text-sm text-foreground focus:outline-none focus:ring-2 focus:ring-ring resize-y"

export function formatDate(value: string | null | undefined) {
  if (!value) return "—"
  const date = new Date(value.length === 10 ? `${value}T12:00:00` : value)
  return Number.isNaN(date.getTime()) ? value : date.toLocaleDateString(undefined, { year: "numeric", month: "short", day: "numeric" })
}
