// Dashboard (SPEC §6.2): stat tiles, filters, hackathon grid, detail dialog with brief +
// "Scout this", census date + "Refresh census" with job progress.

import { useCallback, useEffect, useMemo, useRef, useState } from "react"
import { toast } from "sonner"
import { Compass, ExternalLink, RefreshCw, Search, X } from "lucide-react"
import { api } from "../../api"
import { useApp } from "../../store"
import { cn } from "../../lib/utils"
import { deadlineLabel, formatInt, formatMoney } from "../../lib/format"
import { Button } from "../../components/ui/button"
import { Input } from "../../components/ui/input"
import { Progress } from "../../components/ui/progress"
import { Skeleton } from "../../components/ui/skeleton"
import { Tabs, TabsList, TabsTrigger } from "../../components/ui/tabs"
import { Select, SelectContent, SelectItem, SelectTrigger, SelectValue } from "../../components/ui/select"
import { Dialog, DialogContent, DialogDescription, DialogHeader, DialogTitle } from "../../components/ui/dialog"
import { HackathonGrid, HackathonGridSkeleton, StatusPill, Thumb } from "../../components/cards/hackathon-card"
import { BriefCard } from "../../components/cards/brief-card"
import { StatTile, StatTilesSkeleton } from "../../components/cards/stats-card"
import type { Hackathon, HackathonDetail, JobProgress, Stats } from "../../types"

type Status = "open" | "upcoming" | "ended" | "all"
type Sort = "deadline" | "prize" | "registrations"
const ALL = "__all__"

export function DashboardView() {
  const health = useApp((s) => s.health)
  const loadHealth = useApp((s) => s.loadHealth)
  const scoutFromDashboard = useApp((s) => s.scoutFromDashboard)

  const [stats, setStats] = useState<Stats | null>(null)
  const [statsError, setStatsError] = useState<string | null>(null)
  const [status, setStatus] = useState<Status>("open")
  const [theme, setTheme] = useState<string>(ALL)
  const [sort, setSort] = useState<Sort>("deadline")
  const [q, setQ] = useState("")
  const [debouncedQ, setDebouncedQ] = useState("")
  const [rows, setRows] = useState<Hackathon[] | null>(null)
  const [rowsLoading, setRowsLoading] = useState(true)
  const [selected, setSelected] = useState<Hackathon | null>(null)
  const [refreshTick, setRefreshTick] = useState(0)

  useEffect(() => {
    const t = setTimeout(() => setDebouncedQ(q.trim()), 250)
    return () => clearTimeout(t)
  }, [q])

  useEffect(() => {
    let cancelled = false
    api
      .stats()
      .then((s) => !cancelled && (setStats(s), setStatsError(null)))
      .catch((e) => {
        if (cancelled) return
        setStatsError(e instanceof Error ? e.message : String(e))
        toast.error("Could not load stats", { description: e instanceof Error ? e.message : String(e) })
      })
    return () => {
      cancelled = true
    }
  }, [refreshTick])

  useEffect(() => {
    let cancelled = false
    setRowsLoading(true)
    api
      .hackathons({ status, q: debouncedQ || undefined, theme: theme === ALL ? undefined : theme, sort, limit: 200 })
      .then((r) => {
        if (cancelled) return
        setRows(r)
        setRowsLoading(false)
      })
      .catch((e) => {
        if (cancelled) return
        setRows([])
        setRowsLoading(false)
        toast.error("Could not load hackathons", { description: e instanceof Error ? e.message : String(e) })
      })
    return () => {
      cancelled = true
    }
  }, [status, debouncedQ, theme, sort, refreshTick])

  const ending7 = useMemo(() => (stats?.deadlines_next_14d || []).filter((h) => (h.days_left ?? 99) <= 7).length, [stats])
  const themes = useMemo(() => (stats?.themes || []).map((t) => t.name), [stats])

  const onRefreshed = useCallback(() => {
    setRefreshTick((t) => t + 1)
    void loadHealth()
  }, [loadHealth])

  return (
    <div className="flex flex-col h-full min-h-0">
      {/* Header */}
      <div className="h-10 flex items-center px-4 gap-3 flex-shrink-0">
        <span className="text-sm font-medium pl-6 md:pl-0">Dashboard</span>
        <div className="ml-auto flex items-center gap-2">
          <CensusRefresh censusDate={health?.census_date} onDone={onRefreshed} />
        </div>
      </div>

      <div className="flex-1 overflow-y-auto min-h-0">
        <div className="@container max-w-6xl mx-auto px-4 pb-8 space-y-4">
          {/* Stat tiles */}
          {stats ? (
            <div className="grid grid-cols-2 @2xl:grid-cols-4 gap-2">
              <StatTile label="Open" value={formatInt(stats.counts.open)} hint={`${formatInt(stats.counts.total)} in census`} />
              <StatTile label="Upcoming" value={formatInt(stats.counts.upcoming)} />
              <StatTile label="Ending in 7 days" value={formatInt(ending7)} hint={`${stats.deadlines_next_14d?.length ?? 0} in 14 days`} />
              <StatTile label="Prize pool · open" value={formatMoney(stats.prize_total_open)} hint="sum of parsed prize_amount" />
            </div>
          ) : statsError ? (
            <div className="rounded-xl border border-dashed px-3 py-3 text-xs text-muted-foreground">
              Stats unavailable — {statsError}
            </div>
          ) : (
            <StatTilesSkeleton />
          )}

          {/* Filters */}
          <div className="flex flex-wrap items-center gap-2">
            <Tabs value={status} onValueChange={(v) => setStatus(v as Status)}>
              <TabsList className="h-8">
                <TabsTrigger value="open" className="text-xs">Open</TabsTrigger>
                <TabsTrigger value="upcoming" className="text-xs">Upcoming</TabsTrigger>
                <TabsTrigger value="ended" className="text-xs">Ended</TabsTrigger>
                <TabsTrigger value="all" className="text-xs">All</TabsTrigger>
              </TabsList>
            </Tabs>

            <div className="relative flex-1 min-w-[180px] max-w-sm">
              <Search className="absolute left-2 top-1/2 -translate-y-1/2 w-3.5 h-3.5 text-muted-foreground/60 pointer-events-none" />
              <Input
                value={q}
                onChange={(e) => setQ(e.target.value)}
                placeholder="Search title or organizer…"
                className="h-8 pl-7 pr-7 rounded-lg text-sm bg-muted border border-input placeholder:text-muted-foreground/40"
              />
              {q && (
                <button
                  type="button"
                  onClick={() => setQ("")}
                  className="absolute right-1.5 top-1/2 -translate-y-1/2 text-muted-foreground/60 hover:text-foreground"
                  aria-label="Clear search"
                >
                  <X className="w-3.5 h-3.5" />
                </button>
              )}
            </div>

            <Select value={theme} onValueChange={setTheme}>
              <SelectTrigger className="h-8 w-[170px] text-xs">
                <SelectValue placeholder="Theme" />
              </SelectTrigger>
              <SelectContent>
                <SelectItem value={ALL}>All themes</SelectItem>
                {themes.map((t) => (
                  <SelectItem key={t} value={t}>
                    {t}
                  </SelectItem>
                ))}
              </SelectContent>
            </Select>

            <Select value={sort} onValueChange={(v) => setSort(v as Sort)}>
              <SelectTrigger className="h-8 w-[150px] text-xs">
                <SelectValue placeholder="Sort" />
              </SelectTrigger>
              <SelectContent>
                <SelectItem value="deadline">Deadline</SelectItem>
                <SelectItem value="prize">Prize</SelectItem>
                <SelectItem value="registrations">Registrations</SelectItem>
              </SelectContent>
            </Select>

            {rows && !rowsLoading && (
              <span className="text-[11px] text-muted-foreground/60 ml-auto tabular-nums">{rows.length.toLocaleString("en-US")} shown</span>
            )}
          </div>

          {/* Grid */}
          {rowsLoading && !rows ? (
            <HackathonGridSkeleton />
          ) : rows && rows.length > 0 ? (
            <div className={cn(rowsLoading && "opacity-60 transition-opacity")}>
              <HackathonGrid rows={rows} onClick={setSelected} />
            </div>
          ) : (
            <div className="rounded-xl border border-dashed px-4 py-10 text-center">
              <p className="text-sm text-muted-foreground">No hackathons match.</p>
              <p className="text-xs text-muted-foreground/60 mt-1">
                Try another status tab or clear the search. Census date: {health?.census_date ?? "—"}.
              </p>
            </div>
          )}
        </div>
      </div>

      <HackathonDialog
        h={selected}
        onClose={() => setSelected(null)}
        onScout={(title) => {
          setSelected(null)
          void scoutFromDashboard(title)
        }}
      />
    </div>
  )
}

// ---------------------------------------------------------------------------

function HackathonDialog({ h, onClose, onScout }: { h: Hackathon | null; onClose: () => void; onScout: (title: string) => void }) {
  const [detail, setDetail] = useState<HackathonDetail | null>(null)
  const [loading, setLoading] = useState(false)

  useEffect(() => {
    if (!h) {
      setDetail(null)
      return
    }
    let cancelled = false
    setLoading(true)
    api
      .hackathon(h.id)
      .then((d) => !cancelled && setDetail(d))
      .catch((e) => !cancelled && toast.error("Could not load details", { description: e instanceof Error ? e.message : String(e) }))
      .finally(() => !cancelled && setLoading(false))
    return () => {
      cancelled = true
    }
  }, [h])

  const row = detail || h
  return (
    <Dialog open={!!h} onOpenChange={(o) => !o && onClose()}>
      <DialogContent className="max-w-2xl max-h-[85vh] overflow-y-auto">
        {row && (
          <>
            <DialogHeader>
              <div className="flex items-start gap-3 pr-6">
                <Thumb src={row.thumbnail} title={row.title} className="w-12 h-12" />
                <div className="min-w-0 flex-1">
                  <DialogTitle className="text-base font-medium leading-tight truncate">{row.title}</DialogTitle>
                  <DialogDescription className="text-xs truncate">
                    {row.org || row.host} · {row.dates}
                    {row.location ? ` · ${row.location}` : ""}
                  </DialogDescription>
                  <div className="mt-1.5 flex items-center gap-3 flex-wrap text-[11px] text-muted-foreground">
                    <StatusPill status={row.status} />
                    <span>{deadlineLabel(row)}</span>
                    <span className="text-foreground font-medium">{row.prize_usd > 0 ? formatMoney(row.prize_usd) : row.prize_display}</span>
                    <span>{formatInt(row.registrations)} registered</span>
                    {row.winners_announced && <span>winners announced</span>}
                  </div>
                </div>
              </div>
            </DialogHeader>

            <div className="flex items-center gap-2 pt-1">
              <Button size="sm" onClick={() => onScout(row.title)} className="gap-1.5">
                <Compass className="w-3.5 h-3.5" />
                Scout this
              </Button>
              <Button asChild variant="outline" size="sm" className="gap-1.5">
                <a href={row.url} target="_blank" rel="noopener noreferrer">
                  <ExternalLink className="w-3.5 h-3.5" />
                  Devpost
                </a>
              </Button>
              {row.gallery_url && (
                <Button asChild variant="ghost" size="sm">
                  <a href={row.gallery_url} target="_blank" rel="noopener noreferrer">
                    Gallery
                  </a>
                </Button>
              )}
            </div>

            {row.themes.length > 0 && (
              <div className="flex flex-wrap gap-1">
                {row.themes.map((t) => (
                  <span key={t} className="rounded-md bg-muted px-1.5 py-0.5 text-[10px] text-muted-foreground">
                    {t}
                  </span>
                ))}
              </div>
            )}

            <div className="pt-1">
              {loading && !detail ? (
                <div className="space-y-2">
                  <Skeleton className="h-4 w-1/3" />
                  <Skeleton className="h-24 w-full rounded-xl" />
                </div>
              ) : detail?.brief ? (
                <BriefCard brief={detail.brief} />
              ) : (
                <div className="rounded-xl border border-dashed px-3 py-4 text-xs text-muted-foreground text-center">
                  No brief resolved yet. <span className="text-foreground">Scout this</span> pulls the rubric, requirements and prizes from
                  Devpost and caches them here.
                </div>
              )}
            </div>
          </>
        )}
      </DialogContent>
    </Dialog>
  )
}

// ---------------------------------------------------------------------------

function CensusRefresh({ censusDate, onDone }: { censusDate?: string; onDone: () => void }) {
  const [progress, setProgress] = useState<JobProgress | null>(null)
  const [running, setRunning] = useState(false)
  const aborter = useRef<AbortController | null>(null)

  useEffect(() => () => aborter.current?.abort(), [])

  const start = async () => {
    if (running) return
    setRunning(true)
    setProgress(null)
    const ac = new AbortController()
    aborter.current = ac
    try {
      const { job_id } = await api.refreshCensus()
      toast("Census refresh started", { description: "Re-listing /api/hackathons in the background." })
      for await (const p of api.jobStream(job_id, ac.signal)) setProgress(p)
      toast.success("Census refreshed")
      onDone()
    } catch (e) {
      if (!ac.signal.aborted) toast.error("Refresh failed", { description: e instanceof Error ? e.message : String(e) })
    } finally {
      setRunning(false)
      setProgress(null)
    }
  }

  return (
    <div className="flex items-center gap-2">
      {running && progress ? (
        <div className="flex items-center gap-2 text-[11px] text-muted-foreground">
          <Progress value={progress.pct} className="h-1 w-24 bg-muted" />
          <span className="tabular-nums">{Math.round(progress.pct)}%</span>
          <span className="truncate max-w-[220px]">
            {progress.step}
            {progress.note ? ` · ${progress.note}` : ""}
          </span>
        </div>
      ) : (
        <span className="text-[11px] text-muted-foreground/60 whitespace-nowrap">census {censusDate ?? "—"}</span>
      )}
      <Button variant="outline" size="sm" onClick={start} disabled={running} className="h-7 gap-1.5 text-xs rounded-lg">
        <RefreshCw className={cn("w-3.5 h-3.5", running && "animate-spin")} />
        {running ? "Refreshing" : "Refresh census"}
      </Button>
    </div>
  )
}
