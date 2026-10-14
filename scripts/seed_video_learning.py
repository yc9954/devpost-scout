"""Add the repo's filming method to the editable learning database once.

Stable IDs keep later edits, status changes and review dates intact on reruns.
Existing link-only notes and imported source records are never changed.
"""

import uuid
from datetime import datetime, timezone

from scout.workspace import WorkspaceStore


VIDEO_PROJECT = '자동 영상·Screen Studio 워크플로'
VIDEO_OUTCOME = '콘티·평면 촬영·후반 편집·제출 검수를 연결해 프로젝트의 실제 데모 영상을 완성한다.'

LESSONS = (
    ('storyboard', '데모 메시지와 콘티 설계',
     '대회별 제출 조건과 심사 기준에서 시청자에게 보여줄 한 작업을 정한다.',
     '첫 10–15초에 작동하는 제품을 보여주고, 문제·시연·근거·마무리를 시간 안에 배치할 수 있다.',
     '''## 촬영 전에 결정할 것
1. 대회의 영상 길이·오디오·공개 URL·언어 요구를 원문으로 확인한다. 3분은 Scout 실전 사례의 예산이지 모든 대회의 공통 규칙은 아니다.
2. 첫 10–15초에 실제 제품 동작을 보여준다. 로고와 팀 소개는 뒤로 미룬다.
3. 시청자가 볼 **하나의 완결된 작업**을 정하고, 각 장면의 행동·화면·대사를 적는다.
4. 검증 수치가 있다면 재현 가능한 근거와 일치시키고, 마지막에는 읽을 수 있는 라이브 URL을 보여준다.

## 3분 예시 예산
- 0–15초: 작동 장면
- 15–35초: 문제와 기대 효과
- 35–150초: 작업의 시작부터 결과까지
- 150–165초: 검증 화면
- 165초 이후: 라이브 URL과 마무리. 실제 대회 제한보다 여유를 둔다.

원본: build/FILM.md, build/TERMINAL.md, .agents/skills/scout/SKILL.md 7단계. 관련 메모: [콘티 뽑아주는 하네스](#/history/e281f1ece1e844fcc79cfd99a7968d97).'''),
    ('storytelling', '스토리텔링 · 레퍼런스에서 장면으로',
     '레퍼런스의 겉모습보다 관객의 질문·감정·화면 전환을 분석해 자기 프로젝트의 이야기를 만든다.',
     '레퍼런스 1개를 분석하고 제품의 문제·작동·변화를 장면별 이야기로 다시 쓸 수 있다.',
     '''## 레퍼런스를 분석하는 순서
1. 시청자가 처음 품어야 할 질문과 마지막에 얻어야 할 답을 한 문장씩 적는다.
2. 각 장면마다 **보이는 행동, 전달할 정보, 감정의 변화, 다음 장면으로 넘어갈 이유**를 나눈다.
3. 타이틀·예쁜 효과보다 실제 제품 동작과 근거가 이야기를 밀고 가는지 확인한다.
4. 레퍼런스에서 색·질감·음악은 참고하되, 제품의 작업 흐름과 다른 장면을 그대로 복제하지 않는다.
5. 10–15초 무음 프리뷰를 보고 화면만으로 무엇이 달라지는지 설명할 수 없으면 콘티를 고친다.

## 장면 카드
| 시간 | 관객의 질문 | 화면에 보일 실제 동작·에셋 | 대사/자막 | 감정과 전환 | 검증 근거 |
| --- | --- | --- | --- | --- | --- |
| 첫 장면 | 무엇이 되나? | 작동하는 결과 | 한 문장 | 놀라움 → 궁금증 | 실제 캡처 |

사용자는 이전 영상에 대해 “어떤 스토리인지 모르겠고 영감도 못 얻겠다”고 지적했다. 기술적 완성도만으로 대체하지 말고, 위 장면 카드를 먼저 완성한다.

원본: [영상 레퍼런스와 스토리텔링 피드백](#/history/60d855e00d805c4041c30a967639c7bb), [콘티 스타일 메모](#/history/3e96c9453989f0e0670a72c0af2131cd), build/TERMINAL.md의 데모 예산.'''),
    ('capture', '브라우저 데모 촬영 · 평면 캡처',
     '브라우저 제품을 평면으로 촬영하고 카메라·커서 움직임을 후반에 만든다.',
     '실제 앱 동작을 일정한 품질로 재촬영하고 잘못된 테이크를 검출할 수 있다.',
     '''## 촬영 방식
- 제품 상태 변화는 실제 앱에서 촬영한다. 설정·대기·비밀 정보 화면은 노출하지 않는다.
- 카메라 확대와 부드러운 커서는 촬영 중 화면에 굽지 않는다. Chrome은 화면이 변할 때 프레임을 보내므로 연속 움직임이 저프레임으로 고정될 수 있다.
- 반복 가능한 동작은 장면별 스크립트로 만들고, 기대한 화면·도구 수·결과가 실제로 나타났는지 확인한다.
- 장면마다 화면 크기와 스케일을 기록한다. 원본은 보존하고 편집본을 별도로 만든다.

Screen Studio는 화면·창 캡처와 기본 트림·프레이밍에 적합하다. Scout의 60fps 카메라·커서 후반 합성은 build/film/record.py → compose.py 파이프라인에 있다.

원본: build/FILM.md, build/film/README.original.md. 아이디어 원문: [커맨드 기반 촬영 시스템](#/history/709887be25d074514696252819778357).'''),
    ('terminal', '터미널 데모 · VHS 테이프',
     '반복 가능한 CLI 장면을 VHS 테이프로 만들고 브라우저 컷과 결합한다.',
     '고정 Sleep 없이 재현되는 터미널 데모를 만들고 화면 촬영본과 정확히 이어 붙일 수 있다.',
     '''## 터미널 장면 제작
- VHS의 .tape 파일에 명령, 타이핑 속도, 화면 크기, 테마, 대기 조건을 기록한다.
- 완료 조건은 고정 Sleep보다 Wait+Screen 정규식으로 기다린다.
- 설정과 인증정보를 보여주지 않는 구간은 Hide/Show로 구분한다.
- 브라우저 장면과 터미널 장면은 따로 촬영한 뒤 코덱·fps·해상도를 맞춰 이어 붙인다.
- 테이프와 결과 영상을 함께 남겨 재현 가능성을 확보한다.

원본: build/TERMINAL.md. 실제 브라우저용 영상 파이프라인: build/FILM.md.'''),
    ('edit', '후반 편집 · 카메라·커서·내레이션·자막',
     '촬영본을 다듬고 대사 타이밍에 맞춰 카메라·커서·자막을 편집한다.',
     '평면 촬영본을 읽기 쉬운 데모로 편집하고 영상·음성·자막의 타이밍을 맞출 수 있다.',
     '''## 편집 순서
1. 의미 없는 대기와 반복을 잘라내고 각 장면이 말하는 한 가지를 남긴다.
2. 내레이션을 먼저 녹음하거나 생성해 실제 길이를 측정한다. 컷 길이를 대사에 맞춘다.
3. 브라우저 데모의 확대·이동·커서는 평면 프레임 위에 후반 합성한다. Scout 예제는 60fps 출력이다.
4. 자막은 같은 대사 타이밍에서 SRT로 만들고 번인 자막과 중복하지 않는다.
5. 소리 클리핑, 화면 글자 크기, 잘린 UI를 720p 프리뷰에서도 확인한다.

Screen Studio에서 가능한 편집: 트림, 화면 비율, 배경, 패딩, 수동 줌·초점, 속도, MP4/GIF 출력. 자동 커서 추적·60fps 후반 합성·나레이션/SRT 생성은 별도 build/film/ 도구가 필요하다.

원본: build/FILM.md, build/film/narrate.py, build/film/compose.py, build/film/mux.py.'''),
    ('multimedia', '멀티미디어 콘텐츠 제작 · 실사·모션·사운드',
     '실제 촬영, 생성한 모션, 음악과 효과음을 장면의 목적에 맞게 조합한다.',
     '에셋의 출처와 용도를 기록하고 짧은 장면을 합성해 재생 가능한 영상으로 검증할 수 있다.',
     '''## 장면별 제작 방법
- **실제 제품 동작:** Screen Studio나 평면 브라우저 캡처를 쓴다. 작동 증거를 생성 영상으로 바꾸지 않는다.
- **분위기와 비유:** 사용 허가 범위를 확인한 Pexels 등의 실사 소스를 선택하고, 출처·라이선스·사용 컷을 기록한다.
- **추상 모션:** Three.js/Canvas로 입자·궤적·형태를 프레임 단위로 만들 수 있다. HTML 모션 도구를 쓴다면 한 컷 시안으로 출력 품질을 확인한다.
- **음악:** MIDI 편곡과 가상 악기 소리를 별도 트랙으로 만들거나 사용권이 확인된 음원을 사용한다. 효과음과 내레이션은 서로 다른 레이어로 관리한다.
- **최종 합성:** 컷의 해상도·fps·색을 맞춘 뒤 FFmpeg로 영상·음악·효과음을 합치고 소리 크기와 싱크를 확인한다.

## 작은 실습
실사 1컷 + 모션 1컷 + 실제 제품 동작 1컷으로 15초 시안을 만든다. 각 컷의 역할, 원본 파일, 사용권, 편집 가능성, 재촬영 비용을 장면 카드에 적고 스토리텔링 항목의 질문·답이 전달되는지 본다.

원본: [실사·Three.js·MIDI·FFmpeg 제작 방식과 피드백](#/history/60d855e00d805c4041c30a967639c7bb), build/FILM.md.'''),
    ('formats', '콘텐츠 형식과 제작 도구 선택',
     '제품 시연, HTML 기반 영상, 3D 합성을 목적에 맞게 구분한다.',
     '원하는 콘텐츠의 증거·반복성·후반 작업에 맞춰 제작 경로를 선택할 수 있다.',
     '''## 어떤 도구를 쓸까
- **실제 제품 시연:** Screen Studio로 화면을 녹화한다. 반복 재현이 중요하면 build/film/의 스크립트 촬영 방식을 검토한다.
- **터미널 동작:** VHS 테이프로 명령과 대기 조건을 남긴다.
- **HTML 기반 모션 영상:** 저장해 둔 [Hyperframes 자료](https://github.com/heygen-com/hyperframes)를 읽고 별도 렌더링 워크플로를 평가한다.
- **실사·3D 합성:** [Blender 모션 트래킹 자료](#/studies/ec6f9301fc9a03e9ef37c5958e832ec1)처럼 촬영 원본과 오브젝트의 정합성을 검증한다.
- **AI 생성 영상:** 사용 기록의 [Higgsfield 설정 요청](#/history/2bda3af052007a2ce353a6497d46893f)을 출발점으로 사용 범위와 후반 편집 필요 여부를 확인한다.

링크를 저장한 것만으로 도구의 품질이나 적합성이 검증된 것은 아니다. 짧은 시안 1개를 만들어 화면 품질·편집 가능성·재현성을 비교한다.'''),
    ('verify', '제출 영상 검수 · 길이·근거·공개 범위',
     '마지막 컷과 공개된 영상이 대회 제출 규칙에 맞는지 검증한다.',
     '길이·소리·자막·URL·근거를 확인하고 제출 링크의 실제 재생 상태를 검증할 수 있다.',
     '''## 내보내기 전 검수
- 대회 원문의 시간 제한보다 여유를 두고 렌더한다. 업로드 후 플레이어에 보이는 길이도 확인한다.
- 첫 10초에 제품이 실제로 작동하는가? 화면의 수치가 검증 문서와 일치하는가?
- 음성이 필요한 대회라면 오디오 트랙과 볼륨을 확인한다. GIF에는 소리가 없다.
- 라이브 URL을 읽고 입력할 수 있는 크기로 충분히 오래 표시한다.
- 퍼블릭 제출 조건이면 실제 공개 상태에서 새 브라우저로 재생을 확인한다.
- 비밀 정보·테스트 계정·개인 연락처가 장면과 터미널 스크롤에 나오지 않는지 확인한다.

원본: build/FILM.md, build/TERMINAL.md, .agents/skills/scout/SKILL.md 7단계.'''),
)

SCOUT_CHECKLIST = (
    'Devpost 데모 영상 제작 체크리스트',
    '대회별 제출 조건을 확인하고 콘티·촬영·편집·검수 흐름을 실제 Scout 데모에 적용한다.',
    'Scout 프로젝트의 실제 제출 영상 브리프를 만들고 Screen Studio 녹화물과 연결할 수 있다.',
    '''## 시작
1. Scout에서 해당 해커톤의 평가 기준, 영상 길이, 공개 URL, 오디오 요구를 먼저 읽는다.
2. [영상 제작 학습 경로](#/studies/path/VIDEO_PATH_ID)의 콘티·촬영·편집·검수 항목을 순서대로 진행한다.
3. Screen Studio에서 **Devpost Scout** 프로젝트를 선택하고 영상 제작 브리프를 만든다.
4. 실제 제품 시연을 녹화·가져온 뒤 프로젝트에 연결한다. 결과 영상은 프로젝트의 Videos에서 다시 연다.

## 제출 전
- [ ] 첫 10–15초에 실제 기능이 보임
- [ ] 심사 기준과 주장 근거가 일치함
- [ ] 길이·오디오·자막·공개 상태·URL 확인

원본: .agents/skills/scout/SKILL.md, build/FILM.md, build/TERMINAL.md.''',
)


def stable_id(slug):
    return uuid.uuid5(uuid.NAMESPACE_URL, f'devpost-scout/video-learning/{slug}').hex


def seed(store):
    projects = {row['title']: row for row in store.list('projects')}
    video = projects.get(VIDEO_PROJECT)
    if not video:
        return 0
    paths = store.list('learning_paths')
    path = next((row for row in paths if row['project_id'] == video['id'] and
                 row['category'] == 'general'), None)
    if not path:
        return 0
    timestamp = datetime.now(timezone.utc).isoformat(timespec='milliseconds')
    added = 0
    with store._db() as db:
        db.execute("UPDATE learning_paths SET outcome = ?, updated_at = ? WHERE id = ? AND outcome = ''",
                   (VIDEO_OUTCOME, timestamp, path['id']))
        for slug, title, summary, objective, body in LESSONS:
            result = db.execute('''INSERT OR IGNORE INTO studies
                (id, title, summary, body, status, category, source_url, project_id,
                 path_id, objective, review_on, hackathon_host, created_at, updated_at)
                VALUES (?, ?, ?, ?, 'inbox', 'general', '', ?, ?, ?, NULL, '', ?, ?)''',
                (stable_id(slug), title, summary, body, video['id'], path['id'], objective,
                 timestamp, timestamp))
            added += result.rowcount
        scout = projects.get('Devpost Scout')
        scout_path = next((row for row in paths if scout and row['project_id'] == scout['id'] and
                           row['category'] == 'hackathon'), None)
        if scout_path:
            title, summary, objective, body = SCOUT_CHECKLIST
            body = body.replace('VIDEO_PATH_ID', path['id'])
            result = db.execute('''INSERT OR IGNORE INTO studies
                (id, title, summary, body, status, category, source_url, project_id,
                 path_id, objective, review_on, hackathon_host, created_at, updated_at)
                VALUES (?, ?, ?, ?, 'inbox', 'hackathon', '', ?, ?, ?, NULL, '', ?, ?)''',
                (stable_id('scout-checklist'), title, summary, body, scout['id'],
                 scout_path['id'], objective, timestamp, timestamp))
            added += result.rowcount
    return added


if __name__ == '__main__':
    print(f'Added {seed(WorkspaceStore())} video learning items.')
