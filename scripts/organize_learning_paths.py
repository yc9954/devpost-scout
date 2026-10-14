"""Conservatively split the imported personal roadmap into useful study paths.

Only moves notes still in the original roadmap path. Re-running is safe and does
not override paths a person has assigned later. Source text and links are untouched.
"""

from scout.workspace import WorkspaceStore


GROUPS = {
    '개발 기초 · 시스템과 인프라': (
        '운영체제, Git, 동시성, 데이터·클라우드 인프라를 실제 개발에 적용한다.',
        ('[Course] Operating System', '깃미남의 Git', 'OpenAI AI Deployment Engineer',
         '운영체제 기초', 'Git과 GitHub', '클라우드 인프라', 'Docker · Kubernetes',
         '데이터 아키텍처', '비동기·동시성'),
    ),
    '에이전트 · LLM 학습': (
        '에이전트 실행·평가, RAG, 모델 학습 및 브라우저 자동화의 핵심 개념을 구현한다.',
        ('Claude for everyday work', '[한글자막] AI 에이전트', 'RAG가 이렇게',
         'AI 에이전트 100개', "What I Learned From DeepSeek's Harness",
         '[Paper Review] Introduction of Reinforcement Learning', 'feat(x402)',
         'LilMGenius/polysona', 'NVIDIA NemoClaw', 'Playwright · CDP',
         'LLM 파인튜닝'),
    ),
    '제품 디자인 · UI 컴포넌트': (
        '디자인 레퍼런스와 UI 컴포넌트를 실제 제품 화면에 적용한다.',
        ('Turn Claude into a Design Genius', 'Stitch - Design',
         'Baehaus on Instagram: "‘Neo-Brutalism', 'Baehaus on Instagram: "해외에서',
         's1m4ne/typora', 'lw-figmate', '318+ Features Components',
         'Discover community-made UI', '제품 디자인 시스템'),
    ),
    '영상 · 3D 제작': (
        '영상 합성, 모션 트래킹, 3D 모델링과 창작 도구를 프로토타입에 적용한다.',
        ('바이브코딩 게임', '85后建筑师', '입털킹 LIP', '블렌더 모션트래킹',
         '실제배경에 오브젝트'),
    ),
    '커리어 · 행사와 사례': (
        '행사·채용·네트워킹 자료를 검토하고 구체적인 다음 행동을 정한다.',
        ('이게 바로 콜드컨택', '이공계 취업', '젠스파크 on Instagram',
         'AI Freaks |', 'brave-people/Dev-Event', 'Notes on the Industry Job Search'),
    ),
}


def organize(store):
    project = next((p for p in store.list('projects') if p['title'] == '개인 학습 로드맵'), None)
    if not project:
        return 0
    original = next((p for p in store.list('learning_paths')
                     if p['project_id'] == project['id'] and p['title'] == project['title']
                     and p['category'] == 'general'), None)
    if not original:
        return 0
    notes = [s for s in store.list('studies') if s['path_id'] == original['id']]
    moved = 0
    for title, (outcome, prefixes) in GROUPS.items():
        matches = [note for note in notes if note['title'].startswith(prefixes)]
        if not matches:
            continue
        existing = next((p for p in store.list('learning_paths')
                         if p['project_id'] == project['id'] and p['title'] == title), None)
        path = existing or store.create('learning_paths', {
            'title': title, 'outcome': outcome, 'category': 'general',
            'project_id': project['id']})
        for note in matches:
            store.update('studies', note['id'], {'path_id': path['id']})
            notes.remove(note)
            moved += 1
    return moved


if __name__ == '__main__':
    print(f'Moved {organize(WorkspaceStore())} study items into topic paths.')
