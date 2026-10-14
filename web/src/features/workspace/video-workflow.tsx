import { useState } from "react"
import { BookOpen, ChevronRight, FileText, Film, FolderKanban, Plus } from "lucide-react"
import { toast } from "sonner"
import { Button } from "../../components/ui/button"
import { useWorkspace } from "../../workspace-context"
import { Field, selectClass, Surface } from "./workspace-ui"

function briefTemplate(project: string) {
  return `# ${project} · 영상 제작 브리프

## 목표와 제출 조건
- 대상 시청자와 한 문장 핵심 메시지:
- 대회별 영상 길이, 음성, 공개 URL, 언어 요구사항 확인:
- 영상에서 증명할 제품 동작과 근거:

## 콘티와 촬영 목록
1. **0–15초 · 제품이 실제로 작동하는 장면** — 로고나 팀 소개보다 먼저 보여준다.
2. **15–35초 · 문제와 효과** — 검증한 근거를 한 문장으로 설명한다.
3. **35–150초 · 한 작업을 처음부터 끝까지** — 클릭·결과·핵심 변화를 촬영한다.
4. **150–165초 · 검증** — 테스트나 측정 결과를 화면에 보여준다.
5. **마무리 · 라이브 URL** — 읽을 수 있게 충분히 유지한다.

각 장면에서 관객이 품을 질문, 화면의 실제 동작, 대사, 감정의 변화와 다음 장면으로 넘어갈 이유를 적는다. 10–15초 무음 시안만 봐도 핵심 변화가 보여야 한다.

## 에셋과 제작 방식
| 장면 | 원본 파일·출처 | 실제 촬영 / 모션 / 스톡 | 사용권 | 편집 방식 |
| --- | --- | --- | --- | --- |
| | | | | |

실제 작동 증거는 제품 화면을 촬영한다. 분위기 컷은 사용권을 확인한 실사·모션을 쓸 수 있다. 음악·효과음·내레이션은 별도 레이어로 관리한다.

## 내레이션과 자막
- 화면별 한 줄 대사:
- 대사 길이를 먼저 측정하고 화면 컷을 맞춘다.
- 자막은 대사 타이밍에서 만들고, 번인과 별도 SRT 중 한 방식을 선택한다.

## 촬영·편집 체크
- [ ] 민감한 정보가 화면에 나오지 않는지 확인
- [ ] 반복 가능한 터미널 장면은 VHS 테이프, 실제 브라우저 장면은 평면 캡처로 분리
- [ ] 불필요한 대기와 설정 화면을 잘라내고, 카메라·커서 움직임은 후반에 적용
- [ ] 최종 길이·소리·가독성을 확인하고 대회 제출 조건에 맞게 공개

## 원본 가이드
- 이 저장소의 build/FILM.md: 실제 브라우저 데모 촬영, 내레이션, 60fps 후반 합성
- 이 저장소의 build/TERMINAL.md: VHS 터미널 장면, 컷 구성과 3분 예산
- .agents/skills/scout/SKILL.md의 7단계: 대회별 제출 조건 확인 후 촬영

Screen Studio에서는 화면 녹화·가져오기·트림·프레이밍·속도·MP4/GIF 내보내기를 할 수 있습니다. 60fps 자동 카메라·커서 합성, VHS, 내레이션 및 SRT 생성은 아직 별도 build/film/ 도구를 사용합니다.
`
}

export function VideoWorkflow({ projectId, onProjectChange, disabled }: {
  projectId: string | null
  onProjectChange: (id: string | null) => void
  disabled: boolean
}) {
  const { projects, learningPaths, studies, createPage } = useWorkspace()
  const [creating, setCreating] = useState(false)
  const project = projects.find((item) => item.id === projectId)
  const training = learningPaths.find((path) => path.title === "자동 영상·Screen Studio 워크플로")
  const lessons = studies.filter((study) => study.path_id === training?.id)
  const featuredTitles = ["스토리텔링 · 레퍼런스에서 장면으로", "데모 메시지와 콘티 설계", "브라우저 데모 촬영 · 평면 캡처", "멀티미디어 콘텐츠 제작 · 실사·모션·사운드", "후반 편집 · 카메라·커서·내레이션·자막", "제출 영상 검수 · 길이·근거·공개 범위"]
  const featured = featuredTitles.map((title) => lessons.find((study) => study.title === title)).filter((study) => study !== undefined)
  const scoutChecklist = studies.find((study) => study.title === "Devpost 데모 영상 제작 체크리스트")

  const createBrief = async () => {
    if (!project || disabled) return
    setCreating(true)
    try {
      const page = await createPage({ title: `영상 제작 브리프 · ${project.title}`, body: briefTemplate(project.title),
        kind: "page", space: "projects", parent_id: null, project_id: project.id })
      window.location.hash = `#/pages/${page.id}`
      toast.success("Video brief created in the project")
    } catch (error) { toast.error(error instanceof Error ? error.message : String(error)) }
    finally { setCreating(false) }
  }

  return <Surface className="p-4 space-y-4">
    <div className="flex flex-wrap items-start justify-between gap-3"><div><h2 className="inline-flex items-center gap-2 text-sm font-semibold"><Film className="h-4 w-4 text-blue-400" />Production workflow</h2><p className="mt-1 text-xs text-muted-foreground">Plan a demo, record it, edit it, and verify the submission against Scout’s filming guide.</p></div>{training && <button type="button" className="inline-flex items-center gap-1 text-xs text-blue-300 hover:underline" onClick={() => { window.location.hash = `#/studies/path/${training.id}` }}><BookOpen className="h-3.5 w-3.5" />Open learning path · {lessons.length}<ChevronRight className="h-3 w-3" /></button>}</div>
    <div className="flex flex-wrap items-end gap-3"><Field label="Project for this recording"><select aria-label="Production project" className={`${selectClass} !w-72 max-w-full`} value={projectId ?? ""} disabled={disabled} onChange={(event) => onProjectChange(event.target.value || null)}><option value="">No project</option>{projects.map((item) => <option key={item.id} value={item.id}>{item.title}</option>)}</select></Field>{project && <><Button type="button" size="sm" variant="outline" disabled={disabled || creating} onClick={() => void createBrief()}><Plus className="mr-1 h-3.5 w-3.5" />{creating ? "Creating…" : "New video brief"}</Button><button type="button" className="inline-flex items-center gap-1 pb-2 text-xs text-muted-foreground hover:text-foreground" onClick={() => { window.location.hash = `#/projects/${project.id}` }}><FolderKanban className="h-3.5 w-3.5" />Open project</button></>}</div>
    <div className="grid gap-2 md:grid-cols-4 text-xs">{[
      ["1 · Plan", "Set the audience, judging rules, message, and shot list."],
      ["2 · Capture", "Show the working product early. Capture browser and terminal beats separately."],
      ["3 · Edit", "Trim pauses, frame the action, then align narration and captions."],
      ["4 · Verify", "Check the time cap, audio, readable URL, and public submission link."],
    ].map(([title, detail]) => <div key={title} className="rounded-lg border border-border/60 bg-muted/20 p-3"><p className="font-medium text-foreground">{title}</p><p className="mt-1 text-muted-foreground leading-relaxed">{detail}</p></div>)}</div>
    {lessons.length > 0 && <div className="border-t border-border/60 pt-3"><p className="mb-2 text-[11px] font-medium text-muted-foreground">Learn the filming and editing method</p><div className="flex flex-wrap gap-2">{featured.map((study) => <button key={study.id} type="button" className="inline-flex items-center gap-1 rounded-md border border-border/60 px-2 py-1 text-[11px] hover:border-blue-500/40 hover:text-blue-300" onClick={() => { window.location.hash = `#/studies/${study.id}` }}><FileText className="h-3 w-3" />{study.title}</button>)}{project?.title === "Devpost Scout" && scoutChecklist && <button type="button" className="inline-flex items-center gap-1 rounded-md border border-blue-500/30 px-2 py-1 text-[11px] text-blue-300" onClick={() => { window.location.hash = `#/hackathon-study/${scoutChecklist.id}` }}><FileText className="h-3 w-3" />{scoutChecklist.title}</button>}</div></div>}
  </Surface>
}
