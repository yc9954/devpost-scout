import { useCallback, useEffect, useRef, useState } from "react"
import { Camera, Download, Film, Mic, Monitor, Pause, Play, Square, Trash2, Upload, Volume2, VolumeX } from "lucide-react"
import { toast } from "sonner"
import { Button } from "../../components/ui/button"
import { Input } from "../../components/ui/input"
import { studioApi } from "../../studio"
import type { StudioAspect, StudioExportOptions, StudioRecording, StudioStatus } from "../../studio"
import { useHashRoute } from "../../use-hash-route"
import { useWorkspace } from "../../workspace-context"
import { EmptyState, Field, selectClass, StatePill, Surface, WorkspacePage } from "./workspace-ui"
import { VideoWorkflow } from "./video-workflow"

type CaptureState = "idle" | "starting" | "recording" | "paused" | "saving"
type WebcamShape = "rounded" | "circle"

interface CaptureSession {
  recorder: MediaRecorder
  streams: MediaStream[]
  output: MediaStream
  audioContext?: AudioContext
  screenVideo: HTMLVideoElement
  cameraVideo?: HTMLVideoElement
  animationFrame: number
  chunks: Blob[]
  title: string
  projectId: string | null
  startedAt: number
  elapsed: number
  mime: string
}

const aspectSizes: Record<Exclude<StudioAspect, "source">, [number, number]> = {
  wide: [1280, 720], vertical: [720, 1280], square: [1080, 1080],
}

function sourceFrameSize(recording: StudioRecording): [number, number] {
  const scale = Math.min(1, 1920 / recording.width, 1080 / recording.height)
  return [Math.max(2, Math.floor(recording.width * scale / 2) * 2), Math.max(2, Math.floor(recording.height * scale / 2) * 2)]
}

function clockTime(seconds: number) {
  if (!Number.isFinite(seconds)) return "0:00"
  const whole = Math.max(0, Math.floor(seconds))
  return `${Math.floor(whole / 60)}:${String(whole % 60).padStart(2, "0")}`
}

function fileSize(bytes: number) {
  return bytes >= 1024 ** 2 ? `${(bytes / 1024 ** 2).toFixed(1)} MB` : `${Math.round(bytes / 1024)} KB`
}

function videoElement(stream: MediaStream) {
  const video = document.createElement("video")
  video.srcObject = stream
  video.muted = true
  video.playsInline = true
  return video
}

function drawCamera(ctx: CanvasRenderingContext2D, video: HTMLVideoElement, width: number, height: number, shape: WebcamShape) {
  if (video.readyState < 2 || !video.videoWidth || !video.videoHeight) return
  const boxWidth = Math.round(width * 0.22)
  const boxHeight = Math.round(boxWidth * 0.68)
  const margin = Math.round(width * 0.025)
  const x = width - boxWidth - margin
  const y = height - boxHeight - margin
  const scale = Math.max(boxWidth / video.videoWidth, boxHeight / video.videoHeight)
  const sourceWidth = boxWidth / scale
  const sourceHeight = boxHeight / scale
  ctx.save()
  ctx.beginPath()
  if (shape === "circle") ctx.ellipse(x + boxWidth / 2, y + boxHeight / 2, Math.min(boxWidth, boxHeight) / 2, Math.min(boxWidth, boxHeight) / 2, 0, 0, 2 * Math.PI)
  else ctx.roundRect(x, y, boxWidth, boxHeight, Math.round(boxWidth * 0.06))
  ctx.clip()
  ctx.drawImage(video, (video.videoWidth - sourceWidth) / 2, (video.videoHeight - sourceHeight) / 2,
    sourceWidth, sourceHeight, x, y, boxWidth, boxHeight)
  ctx.restore()
  ctx.strokeStyle = "rgba(255,255,255,.7)"
  ctx.lineWidth = Math.max(2, Math.round(width / 700))
  ctx.beginPath()
  if (shape === "circle") ctx.ellipse(x + boxWidth / 2, y + boxHeight / 2, Math.min(boxWidth, boxHeight) / 2, Math.min(boxWidth, boxHeight) / 2, 0, 0, 2 * Math.PI)
  else ctx.roundRect(x, y, boxWidth, boxHeight, Math.round(boxWidth * 0.06))
  ctx.stroke()
}

function stopTracks(streams: MediaStream[]) {
  for (const stream of streams) for (const track of stream.getTracks()) track.stop()
}

export function StudioView() {
  const hash = useHashRoute()
  const { projects } = useWorkspace()
  const route = hash.match(/^#\/studio\/([a-f0-9]{32})(?:\/([a-f0-9]{32}))?$/)
  const [projectId, setProjectId] = useState<string | null>(route?.[1] ?? null)
  const [status, setStatus] = useState<StudioStatus | null>(null)
  const [recordings, setRecordings] = useState<StudioRecording[]>([])
  const [selectedId, setSelectedId] = useState<string | null>(null)
  const [loading, setLoading] = useState(true)
  const [captureState, setCaptureState] = useState<CaptureState>("idle")
  const [captureTitle, setCaptureTitle] = useState("Screen recording")
  const [systemAudio, setSystemAudio] = useState(true)
  const [microphone, setMicrophone] = useState(false)
  const [webcam, setWebcam] = useState(false)
  const [webcamShape, setWebcamShape] = useState<WebcamShape>("rounded")
  const [elapsed, setElapsed] = useState(0)
  const [uploading, setUploading] = useState(false)
  const [exporting, setExporting] = useState(false)
  const [format, setFormat] = useState<"mp4" | "gif">("mp4")
  const [aspect, setAspect] = useState<StudioAspect>("source")
  const [padding, setPadding] = useState(24)
  const [background, setBackground] = useState("#111827")
  const [zoom, setZoom] = useState(1)
  const [focusX, setFocusX] = useState(0.5)
  const [focusY, setFocusY] = useState(0.5)
  const [speed, setSpeed] = useState(1)
  const [trimStart, setTrimStart] = useState(0)
  const [trimEnd, setTrimEnd] = useState(0)
  const [playhead, setPlayhead] = useState(0)
  const [playing, setPlaying] = useState(false)
  const [muted, setMuted] = useState(false)
  const [titleDraft, setTitleDraft] = useState("")
  const canvasRef = useRef<HTMLCanvasElement>(null)
  const videoRef = useRef<HTMLVideoElement>(null)
  const fileInputRef = useRef<HTMLInputElement>(null)
  const sessionRef = useRef<CaptureSession | null>(null)
  const selected = recordings.find((item) => item.id === selectedId) ?? null

  useEffect(() => {
    setProjectId(route?.[1] ?? null)
    if (route?.[2]) setSelectedId(route[2])
  }, [hash])

  const refresh = useCallback(async () => {
    const rows = await studioApi.list()
    setRecordings(rows)
    setSelectedId((current) => current && rows.some((row) => row.id === current) ? current : rows[0]?.id ?? null)
  }, [])

  useEffect(() => {
    let alive = true
    Promise.all([studioApi.status(), studioApi.list()]).then(([nextStatus, rows]) => {
      if (!alive) return
      setStatus(nextStatus)
      setRecordings(rows)
      setSelectedId((current) => current && rows.some((row) => row.id === current) ? current : rows[0]?.id ?? null)
    }).catch((error: Error) => toast.error("Could not load Screen Studio", { description: error.message })).finally(() => { if (alive) setLoading(false) })
    return () => { alive = false }
  }, [])

  useEffect(() => {
    setTrimStart(0)
    setTrimEnd(selected?.duration ?? 0)
    setPlayhead(0)
    setPlaying(false)
    setTitleDraft(selected?.title ?? "")
    setAspect("source")
    setZoom(1)
    setFocusX(0.5)
    setFocusY(0.5)
  }, [selected?.id])

  useEffect(() => { if (videoRef.current) videoRef.current.playbackRate = speed }, [speed, selected?.id])

  useEffect(() => {
    if (captureState !== "recording" && captureState !== "paused") return
    const interval = window.setInterval(() => {
      const session = sessionRef.current
      if (session) setElapsed(session.elapsed + (session.recorder.state === "recording" ? (performance.now() - session.startedAt) / 1000 : 0))
    }, 250)
    return () => window.clearInterval(interval)
  }, [captureState])

  const stopCapture = useCallback(() => {
    const session = sessionRef.current
    if (!session || session.recorder.state === "inactive") return
    if (session.recorder.state === "recording") session.elapsed += (performance.now() - session.startedAt) / 1000
    session.recorder.stop()
    setCaptureState("saving")
  }, [])

  useEffect(() => () => { if (sessionRef.current?.recorder.state !== "inactive") stopCapture() }, [stopCapture])

  const startCapture = async () => {
    if (captureState !== "idle" || !status?.ready) return
    if (!navigator.mediaDevices?.getDisplayMedia || typeof MediaRecorder === "undefined" || !HTMLCanvasElement.prototype.captureStream) {
      toast.error("This browser does not support screen recording")
      return
    }
    const mime = ["video/webm;codecs=vp9,opus", "video/webm;codecs=vp8,opus", "video/webm", "video/mp4"]
      .find((candidate) => MediaRecorder.isTypeSupported(candidate))
    if (!mime) { toast.error("No supported recording format is available in this browser"); return }
    const streams: MediaStream[] = []
    let audioContext: AudioContext | undefined
    let output: MediaStream | undefined
    let screenVideo: HTMLVideoElement | undefined
    let cameraVideo: HTMLVideoElement | undefined
    let animationFrame = 0
    try {
      // Keep the browser's source picker directly in the click handler's user activation.
      const displayRequest = navigator.mediaDevices.getDisplayMedia({ video: { frameRate: 30 }, audio: systemAudio })
      setCaptureState("starting")
      const display = await displayRequest
      streams.push(display)
      if (microphone) streams.push(await navigator.mediaDevices.getUserMedia({ audio: true }))
      if (webcam) streams.push(await navigator.mediaDevices.getUserMedia({ video: true }))
      screenVideo = videoElement(display)
      await screenVideo.play()
      if (webcam) {
        cameraVideo = videoElement(streams[streams.length - 1])
        await cameraVideo.play()
      }
      const canvas = canvasRef.current
      const ctx = canvas?.getContext("2d", { alpha: false })
      if (!canvas || !ctx) throw new Error("Could not create the recording canvas")
      const screenTrack = display.getVideoTracks()[0]
      const settings = screenTrack.getSettings()
      const sourceWidth = screenVideo.videoWidth || settings.width || 1280
      const sourceHeight = screenVideo.videoHeight || settings.height || 720
      const ratio = Math.min(1, 1920 / sourceWidth, 1080 / sourceHeight)
      canvas.width = Math.max(2, Math.floor(sourceWidth * ratio / 2) * 2)
      canvas.height = Math.max(2, Math.floor(sourceHeight * ratio / 2) * 2)
      const draw = () => {
        ctx.fillStyle = "#080b10"
        ctx.fillRect(0, 0, canvas.width, canvas.height)
        if (screenVideo!.readyState >= 2) ctx.drawImage(screenVideo!, 0, 0, canvas.width, canvas.height)
        if (cameraVideo) drawCamera(ctx, cameraVideo, canvas.width, canvas.height, webcamShape)
        animationFrame = window.requestAnimationFrame(draw)
        if (sessionRef.current) sessionRef.current.animationFrame = animationFrame
      }
      draw()
      output = canvas.captureStream(30)
      const audioStreams = streams.filter((stream) => stream.getAudioTracks().length)
      if (audioStreams.length) {
        audioContext = new AudioContext()
        const destination = audioContext.createMediaStreamDestination()
        for (const stream of audioStreams) {
          const source = audioContext.createMediaStreamSource(new MediaStream(stream.getAudioTracks()))
          source.connect(destination)
        }
        await audioContext.resume()
        for (const track of destination.stream.getAudioTracks()) output.addTrack(track)
      }
      const recorder = new MediaRecorder(output, { mimeType: mime, videoBitsPerSecond: 6_000_000 })
      const session: CaptureSession = {
        recorder, streams, output, audioContext, screenVideo, cameraVideo, animationFrame,
        chunks: [], title: captureTitle.trim() || "Screen recording", projectId,
        startedAt: performance.now(), elapsed: 0, mime,
      }
      sessionRef.current = session
      recorder.ondataavailable = (event) => { if (event.data.size) session.chunks.push(event.data) }
      recorder.onerror = () => toast.error("Recording failed; try another capture source")
      recorder.onstop = async () => {
        if (sessionRef.current === session) sessionRef.current = null
        window.cancelAnimationFrame(session.animationFrame)
        stopTracks([...session.streams, session.output])
        session.screenVideo.srcObject = null
        if (session.cameraVideo) session.cameraVideo.srcObject = null
      await session.audioContext?.close().catch(() => undefined)
        try {
          const blob = new Blob(session.chunks, { type: session.mime })
          if (!blob.size) throw new Error("The recording was empty")
          const saved = await studioApi.upload(blob, session.title, session.elapsed, session.projectId)
          await refresh()
          setSelectedId(saved.id)
          toast.success("Recording saved to Screen Studio")
        } catch (error) { toast.error("Could not save recording", { description: error instanceof Error ? error.message : String(error) }) }
        finally { setCaptureState("idle"); setElapsed(0) }
      }
      screenTrack.addEventListener("ended", stopCapture, { once: true })
      recorder.start(1000)
      setElapsed(0)
      setCaptureState("recording")
    } catch (error) {
      window.cancelAnimationFrame(animationFrame)
      stopTracks(streams)
      if (output) stopTracks([output])
      screenVideo && (screenVideo.srcObject = null)
      cameraVideo && (cameraVideo.srcObject = null)
      await audioContext?.close()
      sessionRef.current = null
      setCaptureState("idle")
      if ((error as DOMException).name !== "NotAllowedError" || streams.length > 0) toast.error("Could not start recording", { description: error instanceof Error ? error.message : String(error) })
    }
  }

  const togglePause = () => {
    const session = sessionRef.current
    if (!session) return
    if (session.recorder.state === "recording") {
      session.elapsed += (performance.now() - session.startedAt) / 1000
      session.recorder.pause()
      setCaptureState("paused")
    } else if (session.recorder.state === "paused") {
      session.startedAt = performance.now()
      session.recorder.resume()
      setCaptureState("recording")
    }
  }

  const importFile = async (file: File) => {
    setUploading(true)
    try {
      if (file.size > 2 * 1024 ** 3) throw new Error("Videos must be smaller than 2 GB")
      const extension = file.name.split(".").pop()?.toLowerCase()
      const mime = extension === "mp4" ? "video/mp4" : extension === "mov" ? "video/quicktime" : extension === "webm" ? "video/webm" : ""
      if (!mime) throw new Error("Choose a WebM, MP4, or MOV video")
      const typedFile = file.type === mime ? file : new File([file], file.name, { type: mime })
      const saved = await studioApi.upload(typedFile, file.name.replace(/\.[^.]+$/, ""), 0, projectId)
      await refresh()
      setSelectedId(saved.id)
      toast.success("Video added to Screen Studio")
    } catch (error) { toast.error("Could not import video", { description: error instanceof Error ? error.message : String(error) }) }
    finally { setUploading(false); if (fileInputRef.current) fileInputRef.current.value = "" }
  }

  const rename = async () => {
    if (!selected || !titleDraft.trim() || titleDraft.trim() === selected.title) return
    try { const updated = await studioApi.rename(selected.id, titleDraft.trim()); setRecordings((rows) => rows.map((row) => row.id === updated.id ? updated : row)); toast.success("Title updated") }
    catch (error) { toast.error(error instanceof Error ? error.message : String(error)) }
  }

  const assignProject = async (nextId: string | null) => {
    if (!selected) return
    try {
      const updated = await studioApi.assignProject(selected.id, nextId)
      setRecordings((rows) => rows.map((row) => row.id === updated.id ? updated : row))
      toast.success(nextId ? "Recording linked to project" : "Recording unlinked")
    } catch (error) { toast.error(error instanceof Error ? error.message : String(error)) }
  }

  const remove = async () => {
    if (!selected || !window.confirm(`Delete “${selected.title}” and its original video?`)) return
    try { await studioApi.remove(selected.id); await refresh(); toast.success("Recording deleted") }
    catch (error) { toast.error(error instanceof Error ? error.message : String(error)) }
  }

  const exportVideo = async () => {
    if (!selected || exporting || trimEnd - trimStart < 0.1) return
    const options: StudioExportOptions = {
      format, start: trimStart, end: trimEnd, aspect, padding: safePadding, background,
      zoom, focus_x: focusX, focus_y: focusY, speed,
    }
    setExporting(true)
    try { await studioApi.export(selected, options); toast.success(`${format.toUpperCase()} exported`) }
    catch (error) { toast.error("Export failed", { description: error instanceof Error ? error.message : String(error) }) }
    finally { setExporting(false) }
  }

  const togglePreview = () => {
    const video = videoRef.current
    if (!video) return
    if (video.paused) void video.play().catch((error: Error) => toast.error(error.message))
    else video.pause()
  }

  const frameSize: [number, number] = selected ? (aspect === "source" ? sourceFrameSize(selected) : aspectSizes[aspect]) : [16, 9]
  const maxPadding = Math.min(160, Math.max(0, Math.floor((Math.min(...frameSize) - 1) / 8) * 4))
  const safePadding = Math.min(padding, maxPadding)
  const paddingX = Math.min(45, safePadding / frameSize[0] * 100)
  const paddingY = Math.min(45, safePadding / frameSize[1] * 100)

  return <WorkspacePage title="Screen Studio" description="Capture your screen, add audio or webcam, trim the result, and export locally." action={<div className="flex items-center gap-2"><StatePill value={status?.ready ? "FFmpeg ready" : status ? "FFmpeg needed" : "Checking"} tone={status?.ready ? "green" : "amber"} /><input ref={fileInputRef} type="file" accept=".webm,.mp4,.mov,video/webm,video/mp4,video/quicktime" className="hidden" onChange={(event) => { const file = event.target.files?.[0]; if (file) void importFile(file) }} /><Button size="sm" variant="outline" disabled={!status?.ready || uploading} onClick={() => fileInputRef.current?.click()}><Upload className="h-4 w-4 mr-1.5" />{uploading ? "Importing…" : "Import video"}</Button></div>}>
    {status && !status.ready && <Surface className="p-4 border-amber-500/30 bg-amber-500/5"><p className="text-sm text-amber-300">{status.message}. Install FFmpeg and restart the server to use Screen Studio.</p></Surface>}
    <VideoWorkflow projectId={projectId} onProjectChange={setProjectId} disabled={captureState !== "idle"} />
    <Surface className="overflow-hidden">
      <div className="flex flex-wrap items-center gap-3 px-5 py-4 border-b border-border/60"><div className="flex h-9 w-9 items-center justify-center rounded-lg bg-blue-500/10 text-blue-400"><Monitor className="h-5 w-5" /></div><div><h2 className="text-sm font-semibold">New screen recording</h2><p className="text-xs text-muted-foreground">Choose a screen or window when your browser asks.</p></div><div className="ml-auto flex items-center gap-2">{captureState === "recording" || captureState === "paused" ? <><StatePill value={`${captureState === "paused" ? "Paused" : "Recording"} · ${clockTime(elapsed)}`} tone="amber" /><Button size="sm" variant="outline" onClick={togglePause}>{captureState === "paused" ? <Play className="h-4 w-4 mr-1" /> : <Pause className="h-4 w-4 mr-1" />}{captureState === "paused" ? "Resume" : "Pause"}</Button><Button size="sm" variant="destructive" onClick={stopCapture}><Square className="h-3.5 w-3.5 mr-1.5" />Stop & save</Button></> : <Button size="sm" disabled={!status?.ready || captureState !== "idle"} onClick={() => void startCapture()}><span className="h-2 w-2 rounded-full bg-white mr-2" />{captureState === "starting" ? "Choosing source…" : captureState === "saving" ? "Saving…" : "Start recording"}</Button>}</div></div>
      <div className="p-5 grid lg:grid-cols-[minmax(0,1fr)_280px] gap-5">
        <div className="min-w-0"><div className="aspect-video rounded-lg bg-[#090c12] border border-white/5 flex items-center justify-center overflow-hidden"><canvas ref={canvasRef} className={`w-full h-full object-contain ${captureState === "idle" ? "hidden" : ""}`} />{captureState === "idle" && <div className="text-center px-6"><Film className="h-8 w-8 mx-auto text-muted-foreground/50" /><p className="mt-3 text-sm text-muted-foreground">Your live capture appears here</p><p className="mt-1 text-[11px] text-muted-foreground/60">Recordings stay on this computer.</p></div>}</div></div>
        <div className="space-y-4"><Field label="Recording title"><Input value={captureTitle} onChange={(event) => setCaptureTitle(event.target.value)} maxLength={120} disabled={captureState !== "idle"} /></Field><div className="space-y-2"><CaptureOption icon={<Monitor className="h-4 w-4" />} label="System audio" detail="Available when the browser offers it" checked={systemAudio} disabled={captureState !== "idle"} onChange={setSystemAudio} /><CaptureOption icon={<Mic className="h-4 w-4" />} label="Microphone" detail="Mix your voice into the recording" checked={microphone} disabled={captureState !== "idle"} onChange={setMicrophone} /><CaptureOption icon={<Camera className="h-4 w-4" />} label="Webcam overlay" detail="Place your camera in the corner" checked={webcam} disabled={captureState !== "idle"} onChange={setWebcam} /></div>{webcam && <Field label="Webcam shape"><select className={selectClass} disabled={captureState !== "idle"} value={webcamShape} onChange={(event) => setWebcamShape(event.target.value as WebcamShape)}><option value="rounded">Rounded rectangle</option><option value="circle">Circle</option></select></Field>}<p className="text-[11px] leading-relaxed text-muted-foreground">Screen and device access is requested only when you start recording. Your browser chooses which screen or window is shared.</p></div>
      </div>
    </Surface>

    <div className="grid lg:grid-cols-[250px_minmax(0,1fr)] gap-5 items-start">
      <div className="space-y-3"><div className="flex items-center justify-between"><h2 className="text-sm font-semibold">Library</h2><span className="text-xs text-muted-foreground">{recordings.length} videos</span></div>{loading ? <Surface className="p-5 text-xs text-muted-foreground">Loading videos…</Surface> : recordings.length === 0 ? <EmptyState title="No recordings yet" detail="Record your screen or import a video to edit it here." /> : <div className="space-y-2 max-h-[600px] overflow-y-auto pr-1">{recordings.map((item) => <button key={item.id} type="button" onClick={() => setSelectedId(item.id)} className={`w-full rounded-xl border px-3 py-3 text-left transition-colors ${selectedId === item.id ? "border-blue-500/50 bg-blue-500/10" : "border-border/80 bg-card/60 hover:border-foreground/25"}`}><div className="flex gap-2.5 items-start"><div className="h-8 w-8 rounded-lg bg-foreground/5 flex items-center justify-center shrink-0"><Film className="h-4 w-4 text-muted-foreground" /></div><div className="min-w-0 flex-1"><p className="text-xs font-medium truncate">{item.title}</p><p className="text-[11px] text-muted-foreground mt-1">{clockTime(item.duration)} · {fileSize(item.size)}</p><p className="text-[10px] text-muted-foreground/60 mt-0.5">{item.width} × {item.height}</p></div></div></button>)}</div>}</div>
      <div className="min-w-0 space-y-4"><div className="flex items-center justify-between"><h2 className="text-sm font-semibold">Editor</h2>{selected && <StatePill value={selected.extension.toUpperCase().slice(1)} />}</div>{!selected ? <EmptyState title="Select a video to edit" detail="Your recordings and imported clips will appear in the library." /> : <Surface className="overflow-hidden"><div className="px-5 py-4 border-b border-border/60 flex flex-wrap items-center gap-2"><Input aria-label="Recording title" className="max-w-sm flex-1 min-w-40" value={titleDraft} maxLength={120} onChange={(event) => setTitleDraft(event.target.value)} onKeyDown={(event) => { if (event.key === "Enter") void rename() }} /><Button size="sm" variant="outline" disabled={!titleDraft.trim() || titleDraft.trim() === selected.title} onClick={() => void rename()}>Save title</Button><a href={studioApi.downloadUrl(selected.id)} download className="ml-auto inline-flex items-center gap-1.5 text-xs text-muted-foreground hover:text-foreground"><Download className="h-3.5 w-3.5" />Original</a><Button size="icon" variant="ghost" className="h-8 w-8 text-muted-foreground hover:text-destructive" aria-label="Delete recording" onClick={() => void remove()}><Trash2 className="h-4 w-4" /></Button></div>
        <div className="px-5 py-3 border-b border-border/60"><Field label="Linked project"><select aria-label="Recording project" className={`${selectClass} !w-72 max-w-full`} value={selected.project_id ?? ""} onChange={(event) => void assignProject(event.target.value || null)}><option value="">No project</option>{selected.project_id && !projects.some((item) => item.id === selected.project_id) && <option value={selected.project_id}>Deleted project</option>}{projects.map((item) => <option key={item.id} value={item.id}>{item.title}</option>)}</select></Field></div>
        <div className="p-5 space-y-5"><div className="rounded-lg bg-[#080b10] border border-border/50 p-3 flex justify-center overflow-hidden"><div className="relative w-full max-w-3xl overflow-hidden shadow-lg" style={{ aspectRatio: `${frameSize[0]} / ${frameSize[1]}`, maxHeight: 480, backgroundColor: background }}><div className="absolute overflow-hidden" style={{ left: `${paddingX}%`, right: `${paddingX}%`, top: `${paddingY}%`, bottom: `${paddingY}%` }}><video key={selected.id} ref={videoRef} src={studioApi.fileUrl(selected.id)} playsInline preload="metadata" muted={muted} className="w-full h-full object-contain cursor-pointer" style={{ transform: `scale(${zoom})`, transformOrigin: `${focusX * 100}% ${focusY * 100}%` }} onClick={togglePreview} onPlay={() => setPlaying(true)} onPause={() => setPlaying(false)} onEnded={() => setPlaying(false)} onTimeUpdate={(event) => setPlayhead(event.currentTarget.currentTime)} onLoadedMetadata={(event) => { event.currentTarget.playbackRate = speed; if (!selected.duration && Number.isFinite(event.currentTarget.duration)) setTrimEnd(event.currentTarget.duration) }} /></div></div></div>
          <div className="flex items-center gap-2"><Button size="icon" variant="ghost" className="h-8 w-8 shrink-0" aria-label={playing ? "Pause preview" : "Play preview"} onClick={togglePreview}>{playing ? <Pause className="h-4 w-4" /> : <Play className="h-4 w-4" />}</Button><span className="text-[11px] text-muted-foreground tabular-nums w-11 shrink-0">{clockTime(playhead)}</span><input type="range" aria-label="Video timeline" className="flex-1 min-w-0 accent-blue-500" min={0} max={Math.max(0.1, selected.duration)} step={0.1} value={Math.min(playhead, selected.duration)} onChange={(event) => { const time = Number(event.target.value); if (videoRef.current) videoRef.current.currentTime = time; setPlayhead(time) }} /><span className="text-[11px] text-muted-foreground tabular-nums w-11 text-right shrink-0">{clockTime(selected.duration)}</span>{selected.has_audio && <Button size="icon" variant="ghost" className="h-8 w-8 shrink-0" aria-label={muted ? "Unmute preview" : "Mute preview"} onClick={() => setMuted(!muted)}>{muted ? <VolumeX className="h-4 w-4" /> : <Volume2 className="h-4 w-4" />}</Button>}</div>
          <div className="grid sm:grid-cols-[1fr_1fr_auto] gap-3 items-end"><Field label={`In point · ${clockTime(trimStart)}`}><Input type="number" min={0} max={Math.max(0, trimEnd - 0.1)} step="0.1" value={trimStart} onChange={(event) => setTrimStart(Math.max(0, Math.min(Number(event.target.value) || 0, trimEnd - 0.1)))} /></Field><Field label={`Out point · ${clockTime(trimEnd)}`}><Input type="number" min={0} max={selected.duration} step="0.1" value={trimEnd} onChange={(event) => setTrimEnd(Math.min(selected.duration, Math.max(Number(event.target.value) || 0, trimStart + 0.1)))} /></Field><div className="flex gap-2"><Button variant="outline" size="sm" onClick={() => setTrimStart(Math.max(0, Math.min(playhead, trimEnd - 0.1)))}>Set in</Button><Button variant="outline" size="sm" onClick={() => setTrimEnd(Math.min(selected.duration, Math.max(playhead, trimStart + 0.1)))}>Set out</Button></div></div>
          <div className="grid sm:grid-cols-2 xl:grid-cols-4 gap-3"><Field label="Canvas"><select className={selectClass} value={aspect} onChange={(event) => setAspect(event.target.value as StudioAspect)}><option value="source">Source ratio</option><option value="wide">16:9 landscape</option><option value="vertical">9:16 portrait</option><option value="square">1:1 square</option></select></Field><Field label="Background"><Input type="color" className="h-9 p-1 cursor-pointer" value={background} onChange={(event) => setBackground(event.target.value)} /></Field><Field label={`Padding · ${safePadding}px`}><input aria-label="Canvas padding" type="range" min={0} max={maxPadding} step={4} value={safePadding} onChange={(event) => setPadding(Number(event.target.value))} className="w-full h-9 accent-blue-500" /></Field><Field label={`Speed · ${speed.toFixed(2)}×`}><input aria-label="Playback speed" type="range" min={0.5} max={2} step={0.25} value={speed} onChange={(event) => setSpeed(Number(event.target.value))} className="w-full h-9 accent-blue-500" /></Field></div>
          <div className="grid sm:grid-cols-3 gap-3"><Field label={`Zoom · ${zoom.toFixed(1)}×`}><input aria-label="Zoom" type="range" min={1} max={3} step={0.1} value={zoom} onChange={(event) => setZoom(Number(event.target.value))} className="w-full h-9 accent-blue-500" /></Field><Field label={`Focus X · ${Math.round(focusX * 100)}%`}><input aria-label="Focus X" type="range" min={0} max={1} step={0.05} value={focusX} onChange={(event) => setFocusX(Number(event.target.value))} className="w-full h-9 accent-blue-500" /></Field><Field label={`Focus Y · ${Math.round(focusY * 100)}%`}><input aria-label="Focus Y" type="range" min={0} max={1} step={0.05} value={focusY} onChange={(event) => setFocusY(Number(event.target.value))} className="w-full h-9 accent-blue-500" /></Field></div>
          <div className="border-t border-border/60 pt-4 flex flex-wrap items-center gap-3"><Field label="Export format"><select className={`${selectClass} !w-32`} value={format} onChange={(event) => setFormat(event.target.value as "mp4" | "gif")}><option value="mp4">MP4 video</option><option value="gif">GIF</option></select></Field><p className="text-[11px] text-muted-foreground flex-1 min-w-48">{clockTime(Math.max(0, trimEnd - trimStart) / speed)} output · {format === "gif" ? "GIF has no sound" : selected.has_audio ? "Audio included" : "No audio track"}</p><Button disabled={exporting || trimEnd - trimStart < 0.1 || trimEnd > selected.duration + 0.5} onClick={() => void exportVideo()}><Download className="h-4 w-4 mr-1.5" />{exporting ? "Exporting…" : `Export ${format.toUpperCase()}`}</Button></div>
        </div>
      </Surface>}</div>
    </div>
    <p className="text-[11px] text-muted-foreground">Screen Studio supports manual trim, framing, zoom and speed. Browser recording does not capture system-wide cursor positions for automatic zoom or native cursor effects.</p>
  </WorkspacePage>
}

function CaptureOption({ icon, label, detail, checked, disabled, onChange }: {
  icon: React.ReactNode; label: string; detail: string; checked: boolean; disabled: boolean; onChange: (checked: boolean) => void
}) {
  return <label className="flex items-center gap-3 rounded-lg border border-border/60 bg-muted/20 p-2.5 cursor-pointer"><span className="text-muted-foreground">{icon}</span><span className="flex-1 min-w-0"><span className="block text-xs font-medium">{label}</span><span className="block text-[10px] text-muted-foreground">{detail}</span></span><input type="checkbox" checked={checked} disabled={disabled} onChange={(event) => onChange(event.target.checked)} className="h-4 w-4 accent-blue-500" /></label>
}
