// Vault notes (SPEC §4 `vault_lookup` → {notes:[{title,path,excerpt}]}).

import { BookOpen } from "lucide-react"
import { EmptyNote } from "./winners-list"
import type { VaultNote } from "../../types"

function kindOf(path: string): string {
  const m = path.match(/vault\/([^/]+)\//)
  if (!m) return "note"
  return m[1].replace(/^_/, "").replace(/s$/, "")
}

export function VaultNotes({ notes }: { notes: VaultNote[] }) {
  if (notes.length === 0) return <EmptyNote>No vault notes match.</EmptyNote>
  return (
    <div className="rounded-xl border bg-card overflow-hidden">
      <div className="px-3 py-2 border-b flex items-center gap-2 text-xs text-muted-foreground">
        <BookOpen className="w-3.5 h-3.5" />
        <span>
          {notes.length} {notes.length === 1 ? "note" : "notes"}
        </span>
      </div>
      <ul className="divide-y divide-border/60">
        {notes.map((n) => (
          <li key={n.path} className="px-3 py-2">
            <div className="flex items-center gap-2 min-w-0">
              <span className="text-sm font-medium truncate">{n.title}</span>
              <span className="rounded-md bg-muted px-1.5 py-0.5 text-[10px] text-muted-foreground flex-shrink-0">{kindOf(n.path)}</span>
            </div>
            {n.excerpt && <p className="text-xs text-muted-foreground mt-0.5 leading-relaxed">{n.excerpt}</p>}
            <p className="text-[10px] font-mono text-muted-foreground/50 mt-1 truncate">{n.path}</p>
          </li>
        ))}
      </ul>
    </div>
  )
}
