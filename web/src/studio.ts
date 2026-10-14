export interface StudioRecording {
  id: string
  title: string
  extension: string
  mime_type: string
  size: number
  duration: number
  width: number
  height: number
  has_audio: boolean
  project_id: string | null
  created_at: string
}

export interface StudioStatus { ready: boolean; message: string }
export type StudioAspect = "source" | "wide" | "vertical" | "square"
export interface StudioExportOptions {
  format: "mp4" | "gif"
  start: number
  end: number
  aspect: StudioAspect
  padding: number
  background: string
  zoom: number
  focus_x: number
  focus_y: number
  speed: number
}

const root = "/api/studio/recordings"

async function checked(response: Response) {
  if (response.ok) return response
  let message = `Request failed (${response.status})`
  try { message = (await response.json() as { error?: string }).error || message } catch { /* binary or empty reply */ }
  throw new Error(message)
}

function saveBlob(blob: Blob, name: string) {
  const url = URL.createObjectURL(blob)
  const link = document.createElement("a")
  link.href = url
  link.download = name
  document.body.appendChild(link)
  link.click()
  link.remove()
  window.setTimeout(() => URL.revokeObjectURL(url), 60_000)
}

export const studioApi = {
  async status(): Promise<StudioStatus> { return (await checked(await fetch("/api/studio/status"))).json() },
  async list(): Promise<StudioRecording[]> { return (await checked(await fetch(root))).json() },
  async upload(file: Blob, title: string, duration = 0, projectId: string | null = null): Promise<StudioRecording> {
    const response = await fetch(root, {
      method: "POST", body: file,
      headers: {
        "Content-Type": file.type || "video/webm",
        "X-Recording-Title": encodeURIComponent(title),
        "X-Recording-Duration": String(duration),
        ...(projectId ? { "X-Project-Id": projectId } : {}),
      },
    })
    return (await checked(response)).json()
  },
  async rename(id: string, title: string): Promise<StudioRecording> {
    return (await checked(await fetch(`${root}/${id}`, {
      method: "PATCH", headers: { "Content-Type": "application/json" }, body: JSON.stringify({ title }),
    }))).json()
  },
  async assignProject(id: string, projectId: string | null): Promise<StudioRecording> {
    return (await checked(await fetch(`${root}/${id}`, {
      method: "PATCH", headers: { "Content-Type": "application/json" }, body: JSON.stringify({ project_id: projectId }),
    }))).json()
  },
  async remove(id: string): Promise<void> { await checked(await fetch(`${root}/${id}`, { method: "DELETE" })) },
  fileUrl(id: string) { return `${root}/${id}/file` },
  downloadUrl(id: string) { return `${root}/${id}/download` },
  async export(recording: StudioRecording, options: StudioExportOptions): Promise<void> {
    const response = await checked(await fetch(`${root}/${recording.id}/export`, {
      method: "POST", headers: { "Content-Type": "application/json" }, body: JSON.stringify(options),
    }))
    saveBlob(await response.blob(), `${recording.title}.${options.format}`)
  },
}
