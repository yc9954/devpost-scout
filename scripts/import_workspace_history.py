"""Import personal notes and human-authored agent prompts since March 2026.

The source files are *data*. Nothing in them is executed or treated as an instruction.
The complete extracted text is saved to a local, ignored JSONL archive. The searchable
workspace copy masks credentials so they do not appear in the browser.
"""

import csv
import hashlib
import json
import re
import shutil
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import parse_qsl, urlencode, urlsplit, urlunsplit
from zoneinfo import ZoneInfo

from scout import config
from scout.history import HistoryStore


SINCE = '2026-03-01'
KST = ZoneInfo('Asia/Seoul')
ROOT = Path.home()
OUT = config.DATA / 'import_2026-03'
KAKAO = ROOT / 'Downloads/KakaoTalk_Chat_유찬_2026-10-04-05-48-29.csv'
SLACK = OUT / 'slack_self_dm_raw.json'
SLACK_LONG = OUT / 'slack_long_text.json'
AUTO_PREFIXES = (
    'Current workspace snapshot (reference data):',
    '<system-reminder>', '<available_subagent_types>',
    'Briefly inform the user about the task result',
    'The following is the Codex agent history',
    'This session is being continued from a previous conversation',
    '<goal_context>', '<codex_internal_context', '<task-notification>',
    '<turn_aborted>', '<timestamp>', '<recommended_plugins>',
    '<skill>', '<scheduled-task', '<local-command-stdout>',
    '<command-name>', '<command-message>',
    '# AGENTS.md instructions for ',
    '[Request interrupted by user',
)
URL_RE = re.compile(r'https?://[^\s<>"\'\]\)]+', re.IGNORECASE)
SECRET_PATTERNS = (
    re.compile(r'-----BEGIN [A-Z ]*PRIVATE KEY-----[\s\S]*?(?:-----END [A-Z ]*PRIVATE KEY-----|$)'),
    re.compile(r'(?<![A-Za-z0-9])AKIA[A-Z0-9]{16}(?![A-Za-z0-9])'),
    re.compile(r'sk-ant-[A-Za-z0-9_-]{16,}'),
    re.compile(r'sk-[A-Za-z0-9_-]{24,}'),
    re.compile(r'\b(?:ghp|gho|ghu|ghs|ghr)_[A-Za-z0-9]{20,}\b'),
    re.compile(r'\b(?:xoxb|xoxp|xoxa|xoxs)-[A-Za-z0-9-]{20,}\b'),
    re.compile(r'\beyJ[A-Za-z0-9_-]{15,}\.eyJ[A-Za-z0-9_-]{15,}\.[A-Za-z0-9_-]{10,}\b'),
    re.compile(r'\bxapp-\d+-[A-Za-z0-9-]{20,}\b'),
    re.compile(r'\bGOCSPX-[A-Za-z0-9_-]{16,}\b'),
    re.compile(r'\bnvapi-[A-Za-z0-9_-]{20,}\b'),
    re.compile(r'\bvck_[A-Za-z0-9_-]{20,}\b'),
    re.compile(r'\b[A-Za-z][A-Za-z0-9]{5,}[!$#@]{1,3}(?!\w)'),
    re.compile(r'(?i)(?:Authorization\s*[:=]\s*["\']?Bearer\s+)[A-Za-z0-9._~-]{12,}'),
)
SENSITIVE_QUERY = {'key', 'rlkey', 'api_key', 'apikey', 'access_key', 'token', 'access_token',
                   'auth_token', 'refresh_token', 'password', 'secret', 'client_secret',
                   'signature', 'sig', 'auth', 'code', 'session_token'}


def mask_secrets(text):
    # URL query credentials need masking in the visible body as well as urls_json.
    result = URL_RE.sub(lambda match: clean_url(match.group(0)) or '[비밀정보 가림]', text)
    for pattern in SECRET_PATTERNS:
        result = pattern.sub('[비밀정보 가림]', result)
    result = re.sub(r'(?i)((?:비번|비밀번호|password|passwd|pw)\s*[:=]?\s*)(?!\[)(\S+)',
                    r'\1[비밀정보 가림]', result)
    result = re.sub(r'(?i)((?:aws_secret_access_key|aws_access_key_id)\s*=\s*)(?!\[)\S+',
                    r'\1[비밀정보 가림]', result)
    result = re.sub(r'(?i)((?:api\s*(?:키|key))\s*[:=]?\s*)[A-Za-z0-9_-]{16,}',
                    r'\1[비밀정보 가림]', result)
    result = re.sub(r'(?i)(\b(?:[A-Z][A-Z0-9_]*_)?(?:API_KEY|ACCESS_KEY|ACCESS_TOKEN|'
                    r'REFRESH_TOKEN|AUTH_TOKEN|CLIENT_SECRET|PRIVATE_KEY|BOT_TOKEN)\s*[:=]\s*["\']?)'
                    r'(?!\[비밀정보 가림\])[A-Za-z0-9_./+=-]{12,}', r'\1[비밀정보 가림]', result)
    result = re.sub(r'(?i)(\b(?:[A-Z_][A-Z0-9_]*_)?(?:APIKEY|CLIENTSECRET|TOKEN|SECRET|KEY|PASSWORD|CREDENTIAL)'
                    r'(?:_[A-Z0-9]+)*\s*[:=]\s*["\']?)'
                    r'(?!\[비밀정보 가림\])[^\s"\';,}&#?]{8,}', r'\1[비밀정보 가림]', result)

    def mask_contextual_opaque(match):
        before = result[max(0, match.start() - 70):match.start()]
        after = result[match.end():min(len(result), match.end() + 70)]
        # Keep hashes in public URLs and ordinary source checksums intact.
        if re.search(r'https?://[^\s]*$', before):
            return match.group(0)
        if re.search(r'(?i)\b(?:sha256|checksum|commit|oid)\s*[=:"\s]+$', before):
            return match.group(0)
        if re.search(r'(?i)api\b|token|secret|password|credential|bearer|private|키|인증',
                     before + after):
            return '[비밀정보 가림]'
        return match.group(0)

    result = re.sub(r'(?<![A-Za-z0-9])[A-Za-z0-9_-]{32,}(?![A-Za-z0-9])',
                    mask_contextual_opaque, result)
    return result, result != text


def clean_url(raw):
    raw = raw.rstrip('.,;')
    try:
        parts = urlsplit(raw)
        if parts.scheme not in ('http', 'https') or not parts.netloc:
            return ''
        query = [(key, '[가림]' if key.lower() in SENSITIVE_QUERY else value)
                 for key, value in parse_qsl(parts.query, keep_blank_values=True)]
        fragment_pairs = parse_qsl(parts.fragment, keep_blank_values=True)
        fragment = (urlencode([(key, '[가림]' if key.lower() in SENSITIVE_QUERY else value)
                               for key, value in fragment_pairs])
                    if any(key.lower() in SENSITIVE_QUERY for key, _ in fragment_pairs)
                    else parts.fragment)
        return urlunsplit((parts.scheme, parts.netloc, parts.path, urlencode(query), fragment))
    except ValueError:
        return ''


def links_in(text):
    return list(dict.fromkeys(url for match in URL_RE.finditer(text)
                              if (url := clean_url(match.group(0)))))


def clean_codex(text):
    text = re.sub(r'<environment_context>[\s\S]*?</environment_context>', '', text)
    text = re.sub(r'<in-app-browser-context\b[^>]*>[\s\S]*?</in-app-browser-context>', '', text)
    text = re.sub(r'<ide_opened_file>[\s\S]*?</ide_opened_file>', '', text)
    text = text.strip()
    if text.startswith('<send_user_message_question_reply>'):
        try:
            block = re.search(r'<send_user_message_question_reply>\s*([\s\S]*?)\s*</send_user_message_question_reply>', text)
            answers = json.loads(block.group(1)) if block else []
            return '\n'.join(str(item.get('answer', '')) for item in answers).strip()
        except (ValueError, AttributeError):
            pass
    if text.startswith('# Context from my IDE setup:') and '## My request:' not in text:
        return ''
    if text.startswith('# Context from my IDE setup:') and '## My request:' in text:
        text = text.split('## My request:', 1)[1].strip()
    if text.startswith('# Files mentioned by the user:') and '## My request:' in text:
        wrapper, request = text.split('## My request:', 1)
        paths = re.findall(r'^## .+?: (/.+)$', wrapper, re.M)
        text = request.strip()
        if paths:
            text += '\n\n[첨부 경로]\n' + '\n'.join(paths)
    if text.startswith('## My request:'):
        text = text.split('## My request:', 1)[1].strip()
    if text.startswith(AUTO_PREFIXES):
        return ''
    if text.startswith('[external unsupported block: image]'):
        text = text.replace('[external unsupported block: image]', '[이미지 첨부]', 1).strip()
    return text


def slack_text(raw):
    lines, urls = [], []
    for line in raw.splitlines():
        match = re.search(r'^\s*\d+\s+(text|텍스트)\s+(.+)$', line)
        if match:
            value = match.group(2).strip()
            if value and value not in ('', ''):
                lines.append(value)
            continue
        match = re.search(r'^\s*\d+\s+link\s+(.+)$', line)
        if match:
            value = re.search(r'Value:\s*([^,\s]+)', match.group(1))
            if value:
                url = value.group(1)
                if 'sweetspotkr.slack.com/archives/D0AJ2CRGN1L/p' in url:
                    continue
                url = clean_url(url if url.startswith('http') else 'https://' + url)
                if url:
                    urls.append(url)
        attachment = re.search(r'^\s*\d+\s+container\s+(.+\.(?:pdf|md|html|zip|gz|png|jpg|jpeg|mp4|txt))$', line, re.I)
        if attachment:
            lines.append('첨부 파일: ' + attachment.group(1))
    body = '\n'.join(lines)
    urls = list(dict.fromkeys(urls + links_in(body)))
    return body, urls


def title_for(body, urls):
    first = next((part.strip(' #*\t') for part in body.splitlines() if part.strip()), '')
    if first.startswith('# Files mentioned by the user:') and '## My request:' in body:
        first = body.split('## My request:', 1)[1].strip().splitlines()[0]
    first = re.sub(r'\s+', ' ', first).strip()
    if not first and urls:
        first = urlsplit(urls[0]).netloc + urlsplit(urls[0]).path
    return (first or '[내용 없는 첨부]')[:200]


def classify(body, urls):
    text = body.lower().strip()
    if urls and (not text or len(re.sub(URL_RE, '', text).strip()) < 16):
        return 'link'
    if re.search(r'공부|학습|강의|논문|배우|알아보|이해|read|learn|study|조사|궁금|차이가 뭘까|어떻게 작동', text):
        return 'study'
    if re.search(r'해야|하기\b|해보기|만들기|구축|정리하기|신청|구매|사기\b|예약|확인하기|수정|개선|추가|구현|fix|todo|할 일', text):
        return 'action'
    if re.search(r'아이디어|하면 좋|할 수 있|어떨까|구상|사업|서비스|프로덕트|기능|제안|what if|idea|만들자', text):
        return 'idea'
    return 'note'


PROJECT_PATTERNS = (
    ('workspace', r'colanode|개인용? 워크스페이스|personal workspace|devpost scout.*(?:탭|워크스페이스)|openscreen'),
    ('devpost-scout', r'devpost|해커톤|hackathon|스카우터|scouter agent'),
    ('icml-review', r'icml.?ac|icml 논문 리뷰|메타리뷰|score.head|스코어 헤드'),
    ('octopus', r'\boctopus\b|human4depth'),
    ('sleep-coach', r'수면.?코치|수면주기|기상.?시간|sleep.wake.cycle'),
    ('punch-game', r'펀치기계|위대한 직장인'),
    ('skill-hub', r'self.evolving.skill.hub|helix 레포'),
    ('tgp', r'\btgp\b|측정된 자기학습|자가학습'),
    ('stable-dag', r'stabledag|causalflow|DEG Paper'),
    ('hub-gene', r'graphsage|robust hub gene discovery|Manuscript\.docx'),
    ('true-agentic-os', r'true.agentic.os|orchestrator|오케스트레이터|멀티.?머신|agentic.os'),
    ('obulus', r'obulus|x402|소셜 월드모델|개인 db|페르소나.*정산'),
    ('sweetspot', r'sweetspot|sweetsophy|스위트스팟|샵엣피소드|브랜드.*분석|팝업.*브랜드'),
    ('biology', r'gene|cell|세포|유전자|deg\b|온톨로지|지식그래프|biolog|protein'),
    ('vision-pro', r'vision.?pro|비전프로|파노라마|panorama|spatial'),
    ('agent24', r'agent24|페르소나 합성기'),
    ('marketclaw', r'marketclaw|마케팅.?에이전트|marketing.?agent|marketingskills'),
    ('event-twin', r'event.?twin|gs.?2500|nemoclaw|네모클로'),
    ('airlock', r'airlock|daytona|데이토나'),
    ('agent-harness', r'ralpli|goaltending|oh.my.codex|하네스'),
    ('foresight', r'foresight|dtuition|팝업.?월드모델'),
    ('video', r'screen.?studio|hyperframes|영상.?자동|콘티'),
)

CWD_KEYS = {
    'devpost-scout': 'devpost-scout', 'openshelf': 'obulus', 'obolus': 'obulus',
    'sweetspot_worldlabs': 'spatial-design', 'sweetspot_visionpro': 'spatial-design',
    'sweetspot_omnivoice': 'ax-console', 'codex_hack': 'devpost-scout',
    'oh-my-codex': 'agent-harness', 'AX_CONSOLE': 'ax-console',
    'mirofish': 'foresight', 'brand_research': 'foresight',
    'agent24': 'agent24', 'WorldModel': 'biology', 'ralpli': 'agent-harness',
    'goaltending': 'agent-harness', 'marketingskills': 'marketclaw',
    'true_agentic_OS_v3': 'true-agentic-os', 'marketing_OASIS_engine': 'foresight',
    'ax_mia': 'foresight', 'ax_elenna': 'foresight', 'codex_dashboard': 'agent-harness',
    'icml-ac': 'icml-review', 'octopus': 'octopus',
}

KAKAO_LOCAL_ATTACHMENTS = {
    '2026-03-04T20:45:14': (
        ['unified_raw.db'],
        'Drive·Notion 추출 데이터가 들어 있는 SQLite 파일. 파일 자체는 로컬에 보존하며 개별 사내 데이터를 개인 메모로 자동 편입하지 않음.',
        '', 'Drive·Notion 통합 데이터 백업'),
    '2026-03-21T21:42:34': (
        ['Manuscript.docx'],
        'Disease-aware GraphSAGE로 허브 유전자를 찾는 원고 초안.',
        'manuscript_extract.txt',
        'Biologically Consistent Graph Embedding for Robust Hub Gene Discovery'),
    '2026-04-08T12:58:02': (
        ['DEG Paper — Live Preview.pdf'],
        'StableDAG·CausalFlow를 이용한 희귀질환 유전자 조절 계층 연구의 작업 초안.',
        'deg_paper_extract.txt',
        'Data-Driven Regulatory Hierarchy Discovery in Rare Diseases'),
    '2026-05-04T14:02:39': (
        ['KakaoTalk_Photo_2026-05-04-14-02-48.jpeg'],
        '사무실의 책상·모니터·화이트보드 배치가 보이는 파노라마 사진.', '', '사무실 공간 파노라마'),
    '2026-06-02T13:13:16': (
        ['KakaoTalk_Photo_2026-06-02-13-13-28 001.jpeg',
         'KakaoTalk_Photo_2026-06-02-13-13-29 002.jpeg'],
        '카카오T 택시 결제 내역 화면 두 장.', '', '카카오T 결제 내역 사진 2장'),
}


def project_key(body, session_path=''):
    for part in reversed(Path(session_path).parts):
        if part in CWD_KEYS:
            return CWD_KEYS[part]
    text = (body[:1500] + ' ' + session_path).lower()
    for key, pattern in PROJECT_PATTERNS:
        if re.search(pattern, text, re.I):
            return key
    return ''


def local_time(value):
    parsed = datetime.fromisoformat(value.replace('Z', '+00:00'))
    if parsed.tzinfo is None:
        parsed = parsed.replace(tzinfo=KST)
    return parsed.astimezone(KST).isoformat(timespec='seconds')


def make_record(source, source_id, at, body, urls=None, source_url='', session_path='', partial=False,
                project_context='', kind=None):
    urls = list(dict.fromkeys((urls or []) + links_in(body)))
    masked, sensitive = mask_secrets(body)
    urls = [url for url in (clean_url(item) for item in urls) if url]
    identifier = hashlib.sha256(f'{source}\0{source_id}'.encode()).hexdigest()[:32]
    return {'id': identifier, 'source': source, 'source_id': source_id,
            'occurred_at': local_time(at), 'title': title_for(masked, urls), 'body': masked,
            'kind': kind or classify(masked, urls), 'urls_json': json.dumps(urls, ensure_ascii=False),
            'source_url': source_url, 'session_path': session_path,
            'project_key': project_key(masked, project_context or session_path), 'sensitive': int(sensitive),
            'partial': int(partial), 'linked_type': '', 'linked_id': ''}, {
                'id': identifier, 'source': source, 'source_id': source_id,
                'occurred_at': at, 'occurred_at_kst': local_time(at), 'body': body, 'urls': urls,
                'source_url': source_url, 'session_path': session_path,
                'partial': bool(partial),
            }


def kakao_records():
    with KAKAO.open(encoding='utf-8-sig', newline='') as stream:
        for number, row in enumerate(csv.DictReader(stream), 2):
            at = row['Date'].strip()
            if local_time(at)[:10] < SINCE:
                continue
            body = row['Message']
            if body.strip():
                partial = bool(re.match(r'^(사진|파일:|동영상|음성)', body.strip()))
                attachment = KAKAO_LOCAL_ATTACHMENTS.get(local_time(at)[:19])
                if attachment:
                    names, summary, extracted, title = attachment
                    paths = [ROOT / 'Downloads' / name for name in names]
                    available = [path for path in paths if path.exists()]
                    if available:
                        body += '\n\n[확인한 로컬 첨부 파일]\n' + '\n'.join(str(path) for path in available)
                        body += '\n\n[내용 요약]\n' + summary
                        if extracted and (OUT / extracted).exists():
                            body += '\n\n[첨부 문서 텍스트 추출]\n' + (OUT / extracted).read_text(encoding='utf-8')
                    visible, original = make_record('kakao', str(number), at, body, partial=partial)
                    if title and available:
                        visible['title'] = title
                    yield visible, original
                else:
                    yield make_record('kakao', str(number), at, body, partial=partial)


def slack_records():
    full_text = ({row['ts']: row['text'] for row in json.loads(SLACK_LONG.read_text(encoding='utf-8'))}
                 if SLACK_LONG.exists() else {})
    for row in json.loads(SLACK.read_text(encoding='utf-8')):
        at = row['date']
        if local_time(at)[:10] < SINCE:
            continue
        body, urls = slack_text(row['raw'])
        ts = row['ts']
        if ts in full_text:
            body = full_text[ts]
        url = f'https://sweetspotkr.slack.com/archives/D0AJ2CRGN1L/p{ts}'
        partial = bool(re.search(r'\battachments?\b|files\.slack\.com|sweetspotkr\.slack\.com/files', row['raw'], re.I))
        if ts not in full_text and re.search(r'showing \d+-\d+ of \d+ items', row['raw']):
            partial = True
        yield make_record('slack', ts, at, body, urls, url, partial=partial)


def codex_records():
    folders = [ROOT / '.codex/sessions', ROOT / '.codex/archived_sessions']
    for folder in folders:
        for path in sorted(folder.rglob('*.jsonl')):
            cwd = ''
            with path.open(encoding='utf-8', errors='replace') as stream:
                for number, line in enumerate(stream, 1):
                    try:
                        row = json.loads(line)
                    except json.JSONDecodeError:
                        continue
                    at = row.get('timestamp', '')
                    if row.get('type') == 'session_meta':
                        cwd = (row.get('payload') or {}).get('cwd', '')
                        continue
                    if row.get('type') != 'response_item' or not at or local_time(at)[:10] < SINCE:
                        continue
                    payload = row.get('payload') or {}
                    if payload.get('role') != 'user' or payload.get('type') != 'message':
                        continue
                    content = payload.get('content') or []
                    text = '\n'.join(part.get('text', '') for part in content
                                     if isinstance(part, dict) and part.get('type') in ('input_text', 'text'))
                    text = clean_codex(text)
                    attachments = sum(1 for part in content if isinstance(part, dict)
                                      and part.get('type') not in ('input_text', 'text'))
                    if attachments and not text:
                        text = f'[첨부 {attachments}개 — 원본 세션 파일 참조]'
                    if text:
                        yield make_record('codex', f'{path}:{number}', at, text,
                                          session_path=str(path), project_context=cwd,
                                          partial=bool(attachments or '[이미지 첨부]' in text))


def claude_records():
    for path in sorted((ROOT / '.claude/projects').rglob('*.jsonl')):
        with path.open(encoding='utf-8', errors='replace') as stream:
            for number, line in enumerate(stream, 1):
                try:
                    row = json.loads(line)
                except json.JSONDecodeError:
                    continue
                at = row.get('timestamp', '')
                if row.get('type') != 'user' or not at or local_time(at)[:10] < SINCE:
                    continue
                if row.get('isMeta') or row.get('isSidechain') or (row.get('origin') or {}).get('kind') != 'human':
                    continue
                content = (row.get('message') or {}).get('content', '')
                text = content if isinstance(content, str) else '\n'.join(
                    part.get('text', '') for part in content
                    if isinstance(part, dict) and part.get('type') == 'text')
                text = re.sub(r'<system-reminder>[\s\S]*?</system-reminder>', '', text).strip()
                attachments = (isinstance(content, list) and any(
                    isinstance(part, dict) and part.get('type') != 'text' for part in content))
                if text.startswith('<command-message>') and not text.split('</command-name>')[-1].strip():
                    continue
                if text:
                    yield make_record('claude', row.get('uuid') or f'{path}:{number}', at, text,
                                      session_path=str(path), project_context=row.get('cwd', ''),
                                      partial=attachments)


def codex_result_records():
    """Keep agent conclusions alongside prompts without mixing them into personal notes."""
    folders = [ROOT / '.codex/sessions', ROOT / '.codex/archived_sessions']
    for folder in folders:
        for path in sorted(folder.rglob('*.jsonl')):
            cwd = ''
            with path.open(encoding='utf-8', errors='replace') as stream:
                for number, line in enumerate(stream, 1):
                    try:
                        row = json.loads(line)
                    except json.JSONDecodeError:
                        continue
                    at = row.get('timestamp', '')
                    if row.get('type') == 'session_meta':
                        cwd = (row.get('payload') or {}).get('cwd', '')
                        continue
                    if row.get('type') != 'response_item' or not at or local_time(at)[:10] < SINCE:
                        continue
                    payload = row.get('payload') or {}
                    if payload.get('type') != 'message' or payload.get('role') != 'assistant' \
                            or payload.get('phase') != 'final_answer':
                        continue
                    body = '\n'.join(part.get('text', '') for part in (payload.get('content') or [])
                                     if isinstance(part, dict) and part.get('type') == 'output_text').strip()
                    if body:
                        yield make_record('codex-result', f'{path}:{number}', at, body,
                                          session_path=str(path), project_context=cwd, kind='result')


def claude_result_records():
    for path in sorted((ROOT / '.claude/projects').rglob('*.jsonl')):
        with path.open(encoding='utf-8', errors='replace') as stream:
            for number, line in enumerate(stream, 1):
                try:
                    row = json.loads(line)
                except json.JSONDecodeError:
                    continue
                at = row.get('timestamp', '')
                if row.get('type') != 'assistant' or row.get('isSidechain') or not at \
                        or local_time(at)[:10] < SINCE:
                    continue
                message = row.get('message') or {}
                if message.get('stop_reason') != 'end_turn':
                    continue
                body = '\n'.join(part.get('text', '') for part in (message.get('content') or [])
                                 if isinstance(part, dict) and part.get('type') == 'text').strip()
                if body:
                    yield make_record('claude-result', row.get('uuid') or f'{path}:{number}', at, body,
                                      session_path=str(path), project_context=row.get('cwd', ''), kind='result')


SESSION_ID_RE = re.compile(r'[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}')


def history_records(session_records):
    """Recover user inputs present in CLI histories but absent from session JSONL files."""
    known, session_project = {}, {}
    for note in session_records:
        source = note['source']
        if source not in ('codex', 'claude'):
            continue
        match = SESSION_ID_RE.search(note['session_path'])
        if not match:
            continue
        key = (source, match.group())
        known.setdefault(key, set()).add(note['body'].strip())
        if note['project_key']:
            session_project[key] = note['project_key']

    inputs = (
        ('codex', ROOT / '.codex/history.jsonl', 'text', 'session_id', 1),
        ('claude', ROOT / '.claude/history.jsonl', 'display', 'sessionId', 1000),
    )
    for source, path, field, session_field, divisor in inputs:
        if not path.exists():
            continue
        seen = set()
        with path.open(encoding='utf-8', errors='replace') as stream:
            for number, line in enumerate(stream, 1):
                try:
                    row = json.loads(line)
                    at = datetime.fromtimestamp(row['ts' if source == 'codex' else 'timestamp'] / divisor,
                                                timezone.utc).isoformat()
                except (json.JSONDecodeError, KeyError, TypeError, ValueError, OverflowError):
                    continue
                if local_time(at)[:10] < SINCE:
                    continue
                body = row.get(field, '').strip()
                if source == 'codex':
                    body = clean_codex(body)
                else:
                    body = re.sub(r'<system-reminder>[\s\S]*?</system-reminder>', '', body).strip()
                pasted = row.get('pastedContents') or {}
                missing_paste = False
                for label, item in pasted.items():
                    content = item.get('content') if isinstance(item, dict) else None
                    if content:
                        body += f'\n\n[붙여넣은 참고자료 {label}]\n{content}'
                    else:
                        body += f'\n\n[붙여넣은 참고자료 {label}: 원문은 기록에 없음]'
                        missing_paste = True
                if not body:
                    continue
                session_id = row.get(session_field, '')
                clean_body = mask_secrets(body)[0].strip()
                key = (source, session_id)
                if not pasted and clean_body in known.get(key, set()):
                    continue
                duplicate = (session_id, clean_body)
                if duplicate in seen:
                    continue
                seen.add(duplicate)
                partial = missing_paste or bool(re.search(r'\[Image(?: #\d+)?\]|<image\b', body, re.I))
                visible, original = make_record(source + '-history', str(number), at, body,
                                                session_path=f'{path}:{number}',
                                                project_context=row.get('project', ''), partial=partial)
                if key in session_project:
                    visible['project_key'] = session_project[key]
                yield visible, original


def content_key(url):
    parts = urlsplit(url)
    host = (parts.hostname or '').removeprefix('www.')
    if host == 'youtube.com' and parts.path == '/watch':
        return host + ':' + dict(parse_qsl(parts.query)).get('v', '')
    if host == 'm.blog.naver.com':
        return host + ':' + dict(parse_qsl(parts.query)).get('logNo', '')
    return host + parts.path.rstrip('/')


def enrich_links(records):
    path = OUT / 'link_metadata.json'
    if not path.exists():
        return
    metadata = {content_key(row['url']): row for row in json.loads(path.read_text(encoding='utf-8'))
                if row.get('verified') and row.get('title')}
    for note in records:
        if note['kind'] != 'link':
            continue
        for url in json.loads(note['urls_json']):
            row = metadata.get(content_key(url))
            if not row:
                continue
            note['title'] = row['title'][:200]
            extra = '\n\n[공개 페이지 정보]\n제목: ' + row['title']
            if row.get('description'):
                extra += '\n설명: ' + row['description']
            note['body'] += extra
            break


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    backup = OUT / 'kakao_original.csv'
    if not backup.exists():
        shutil.copyfile(KAKAO, backup)
    records, raw, counts = [], [], Counter()
    for generator in (kakao_records, slack_records, codex_records, claude_records,
                      codex_result_records, claude_result_records):
        for visible, original in generator():
            records.append(visible)
            raw.append(original)
            counts[visible['source']] += 1
    for visible, original in history_records(records):
        records.append(visible)
        raw.append(original)
        counts[visible['source']] += 1
    enrich_links(records)
    raw_file = OUT / 'extracted_originals.jsonl'
    with raw_file.open('w', encoding='utf-8') as stream:
        for item in raw:
            stream.write(json.dumps(item, ensure_ascii=False) + '\n')
    for path in (backup, SLACK, raw_file, SLACK_LONG,
                 OUT / 'manuscript_extract.txt', OUT / 'deg_paper_extract.txt'):
        if not path.exists():
            continue
        path.chmod(0o600)
    store = HistoryStore()
    store.replace(records)
    print(json.dumps({'source_counts': counts, 'stored': store.stats(),
                      'raw_archive': str(raw_file)}, ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main()
