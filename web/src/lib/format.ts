export function formatMoney(n: number | undefined | null): string {
  if (n === undefined || n === null || Number.isNaN(n)) return "—"
  if (n >= 1_000_000) return `$${(n / 1_000_000).toFixed(n % 1_000_000 === 0 ? 0 : 1)}M`
  if (n >= 10_000) return `$${Math.round(n / 1000)}k`
  return `$${n.toLocaleString("en-US")}`
}

export function formatInt(n: number | undefined | null): string {
  if (n === undefined || n === null || Number.isNaN(n)) return "—"
  return n.toLocaleString("en-US")
}

/** "closes in 4 days" / "opens in 12 days" / "closed" — derived from `days_left` (SPEC §2). */
export function deadlineLabel(h: { status: string; days_left?: number }): string {
  if (h.status === "ended") return "Closed"
  const d = h.days_left
  if (d === undefined || d === null) return h.status === "upcoming" ? "Upcoming" : "Open"
  const verb = h.status === "upcoming" ? "Opens" : "Closes"
  if (d <= 0) return h.status === "upcoming" ? "Opens today" : "Closes today"
  if (d === 1) return `${verb} tomorrow`
  return `${verb} in ${d} days`
}

export function httpsThumb(url: string | undefined): string {
  if (!url) return ""
  if (url.startsWith("//")) return `https:${url}`
  return url
}
