"""Create an editable starting structure from the March–October 2026 archive.

Every seeded row has a stable ID. Running this again will add newly found rows without
overwriting edits the owner has made in the workspace. Original notes remain searchable.
Historical one-line ideas are kept in Collected notes unless there is evidence that
they are a current action or a useful study resource.
"""

import hashlib
import json
import re
import sqlite3
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import parse_qs, urlsplit

from scout import config


PROJECTS = [
    ('workspace', 'Personal Agent Workspace', '개인 프로젝트, 할 일, 공부, 에이전트, 원문 메모를 한곳에서 관리하는 로컬 워크스페이스. Colanode에서 필요한 개념을 참고하고 Devpost Scout 스타일로 통합.', 'active', ['개인 사용 목적을 위한 슬랙 + 메모앱', '개인용 에이전트들과의 워크 스페이스']),
    ('devpost-scout', 'Devpost Scout', '해커톤 탐색, 수상작·평가 기준 분석, 아이디어 발굴, 제출 준비를 돕는 에이전트와 대시보드.', 'active', ['해커톤 사냥 에이전트 구축', '직접 어떤 해커톤이던 알아서 아이디에이션부터 제출까지']),
    ('foresight', 'FORESIGHT · 팝업 월드모델', '오프라인 팝업·행사 기획을 위한 수요 예측, 공간 시뮬레이션, 페르소나, 브랜드 매칭과 PoC.', 'active', ['팝업 월드모델을 조금더 잘 디벨롭', '한국 팝업 혹은 오프라인 행사를 열고 싶은 해외 브랜드']),
    ('marketclaw', 'MarketClaw · 마케팅 자동화', '마케팅 리서치, 콘텐츠·광고 실험, 고객 확보를 에이전트와 스킬로 운영하는 프로젝트.', 'active', ['MarketClaw는 계속해', '마케팅 에이전트 완벽하게 만들기']),
    ('event-twin', 'Event Twin · 공간 시뮬레이션', '오프라인 이벤트의 공간, 동선, 대기, 선택, 집단 반응을 모델링하고 시각화하는 연구·데모.', 'active', ['event twin', '사용자 동선 분석']),
    ('obulus', 'Obulus · 개인 지식 네트워크', '개인 경험·기억을 검색 가능한 자산으로 만들고 에이전트가 조회·기여하는 네트워크와 정산 구조.', 'paused', ['obulus 앱 또는 mcp 형태', '개인의 삶과 경험을 검색 가능한 데이터베이스']),
    ('multi-device', '멀티 기기 에이전트 인프라', '여러 기기의 파일·연산·에이전트를 하나의 작업 흐름으로 연결하고 상태·메모리를 공유.', 'planned', ['한 컴퓨터의 데이터를 다른곳에서 처리하기', '멀티 머신에서 orchestrator']),
    ('agent24', 'Agent24 · 페르소나 시뮬레이션', '합성 페르소나와 에이전트의 판단 과정을 활용해 서비스·마케팅 반응을 예측하는 프로젝트.', 'planned', ['Agent24 레포지토리 기반으로 페르소나 합성기', '에이전트 결정 과정 투명화']),
    ('agent-harness', '에이전트 하네스 · Ralpli/Goaltending', '목표 설정, 멀티 세션, 평가·백프레셔, 자가 개선을 조립식 하네스로 연구.', 'active', ['하네스 만들어주는 하네스', 'goal tending 시스템']),
    ('airlock', 'Airlock · 진화 실행 스웜', '병렬 에이전트가 실제 실행 결과와 fitness를 비교해 더 나은 해법을 선택하는 실험.', 'paused', ['Airlock 괜찮은거같은데', '진화 실행 스웜']),
    ('biology', '생물학 월드모델 · 지식그래프', '논문·실험 근거의 관계를 추출하고 세포·유전자·질병 반응을 설명·시뮬레이션하는 연구.', 'planned', ['생물학 월드 모델 만들기', '논문 citation을 보고 에이전트들이']),
    ('spatial-design', '공간 컴퓨팅 · WorldLabs/Vision Pro', '3D 공간 캡처, Gaussian splatting, Vision Pro, 브라우저 기반 공간 편집과 디자인 연구.', 'paused', ['가우시안 스플래팅과 lidar', '특정 gene 클릭해서 simulation']),
    ('ax-console', 'AX Console · Sweetspot 내부 에이전트', '사내 에이전트, 데이터·보고서, 업무 흐름을 위한 콘솔과 자동화.', 'planned', ['업무 명령을 내리면 알아서 적절한 사람에게', 'sophy에 견적서 완벽하게']),
    ('popga', 'Popga · 팝업 데이터 플랫폼', '팝업 시장 데이터, 브랜드·상권 인사이트, QR·랭킹·바이럴 실험과 사용자 성장.', 'planned', ['팝업 qr, ip 바이럴 뉴스', '팝가 디자인시스템제작']),
    ('dots', '사내용 Dots · 미팅 에이전트', 'Slack DM에서 일정 알림, 이전 회의록 분석, 미팅 제안과 후속 작업을 제공하는 아이디어.', 'planned', ['사내용 Dots 만들기', '개인 미팅 시간별로 노티']),
    ('video', '자동 영상·Screen Studio 워크플로', '화면 녹화·편집, HTML 기반 영상, 콘티 생성과 해커톤·제품 데모 제작 워크플로.', 'planned', ['영상 촬영 시스템 오픈소스', '콘티 뽑아주는 하네스']),
    ('learning', '개인 학습 로드맵', 'OS·인프라·클라우드·ML·제품 디자인을 실제 자료와 학습 상태로 관리.', 'active', ['데이터 아키텍쳐 공부하기', '네모클로 html 다시 보고']),
    ('career', '포트폴리오 · 대외 활동', '해커톤 성과, GitHub README, 발표·영상, 네트워킹·지원 활동을 정리.', 'active', ['기사 기반으로 레쥬메에 하이퍼링크', '내 모든 yc9954 레포지토리 readme']),
    ('icml-review', 'ICML AC · 논문 리뷰 에이전트', '논문 초록·본문을 검토하고 리뷰, 메타리뷰, 점수, 수정 제안을 생성하는 에이전트 연구.', 'paused', ['ICML 논문 리뷰에이전트', '메타리뷰는 논문의 최종 결과']),
    ('octopus', 'Octopus · 마케팅 에이전트', '마케터의 리서치·기획·콘텐츠·광고 업무를 에이전트 채팅과 실시간 작업 화면으로 잇는 구상.', 'paused', ['n8n은 필요없고 human4depth', '모든 마케팅 과정이 알아서 작동']),
    ('sleep-coach', '수면·기상 AI 코치', '수면주기와 기상 시간을 바탕으로 추천을 보여주고 실제 기상 후 피드백을 수집하는 앱 아이디어.', 'paused', ['기상 후에 개운한지', '수면을 설정했다고']),
    ('punch-game', '위대한 직장인 · 펀치 게임', '모바일 펀치기계와 점수판, 직원 프로필, 기록 보기로 구성한 사내 게임 아이디어.', 'planned', ['펀치기계를 클릭으로', '위대한 직장인 이름의 기록 보기']),
    ('skill-hub', 'Self-Evolving Skill Hub', 'Helix 구조를 회사에 종속되지 않는 재사용 가능한 에이전트 스킬 아키텍처로 정리하는 구상.', 'planned', ['self-evolving-skill-hub']),
    ('tgp', 'TGP · 측정 기반 자기학습 에이전트', '정답이 있는 벤치마크와 실제 채팅 환경에서 개선 여부를 검증하는 자기학습 에이전트 연구.', 'paused', ['측정된 자기학습', 'TGP방식으로 해야하나']),
    ('stable-dag', 'StableDAG · 희귀질환 조절계층 연구', '희귀질환 유전자 발현 자료에서 방향성 조절 계층을 추론하는 StableDAG·CausalFlow 논문 초안.', 'paused', ['StableDAG', 'DEG Paper — Live Preview.pdf']),
    ('hub-gene', 'Disease-aware GraphSAGE · 허브 유전자', '질환 관련 발현·PPI·표현형 정보를 결합해 허브 유전자를 찾는 GraphSAGE 원고.', 'paused', ['Biologically Consistent Graph Embedding', 'Manuscript.docx']),
]


TASKS = [
    ('사내용 Dots의 Slack DM MVP 기획', '일정 알림, 이전 회의록 분석, 미팅 제안, 인프라 제공 범위를 정의하고 실제 사용자 흐름을 그린다.', 'dots', 'high', ['사내용 Dots 만들기', '슬랙 DM으로 만들기']),
    ('개인 워크스페이스에 다른 로컬 에이전트 연결 방식 정리', '현재 Codex SDK 연결을 기준으로 이후 Claude 및 개인 에이전트의 실행·상태 연결을 설계한다.', 'workspace', 'medium', ['모든 에이전트들이 소통가능한 일종의 mcp 형태']),
    ('과거 메모의 노출된 인증정보 점검 및 교체', '카카오톡·Slack·세션 원문에 API 키, 비밀번호, AWS 자격증명, 개인키가 보인다. 해당 자격증명의 사용 여부를 확인하고 필요한 것부터 교체한다. 화면에는 원문 값을 표시하지 않는다.', 'workspace', 'high', ['anthropic api 키', 'aws_secret_access_key']),
    ('Devpost Scout에 수상작 기반 아이디어 발굴 흐름 정리', '수상작의 핵심 아이디어·평가 근거를 구조화하고 목표 해커톤 조건과 연결한다.', 'devpost-scout', 'high', ['해커톤 우승자들 기반 아이디어 산출기', '아이디어들의 핵심내용이며 모든걸 아주 상세하게']),
    ('해커톤 평가·제출 체크리스트를 Scout에 연결', '평가 항목·필수 제출물·검증 결과를 한 흐름에서 볼 수 있게 정리한다.', 'devpost-scout', 'high', ['비밀리에 순위 분석 및 평가 에이전트', '직접 어떤 해커톤이던 알아서 아이디에이션부터 제출까지']),
    ('Scout 데모 녹화·편집 워크플로 정리', '워크스페이스 Screen Studio와 연결해 화면 녹화, 컷 편집, 제출 영상 제작 단계를 정리한다.', 'devpost-scout', 'medium', ['영상 촬영 시스템 오픈소스', 'screenstudio 기능']),
    ('FORESIGHT의 제품 효용을 검증할 벤치마크 정의', '실제 사용자 데이터와 시뮬레이션 결과를 비교할 지표·대조군·반증 조건을 문서화한다.', 'foresight', 'high', ['몇가지 벤치마크와 함께', '수치또한 정확하게 예상 가능하기 위한 모수 조절 연구']),
    ('FORESIGHT PoC 후보와 실행 계획 정리', '2026-09-28 메모의 PoC 3건 목표를 현재 상태와 비교해 후보, 담당자, 성공 지표를 업데이트한다.', 'foresight', 'high', ['PoC를 이번 분기 3건']),
    ('FORESIGHT GA 유입·전환 경로 확인', '기록에 GA 경로가 확인되지 않는 문제가 남아 있다. 광고 유입부터 질문·가입·리드까지 퍼널을 검증한다.', 'foresight', 'high', ['아직 ga 경로 확인 불가', 'GA 수치']),
    ('FORESIGHT 게스트 질문 후 이메일 리드 수집 흐름 설계', '비로그인 체험, 질문 횟수, 로그인 이후 이어가기, 기획안 이메일 전송을 사용자 흐름으로 묶는다.', 'foresight', 'medium', ['가입이 없어도 어느정도 무료로 질문', '기획안을 메일로 받아보기']),
    ('팝업 월드모델의 공간·동선·대기·선택 모델 분리 검증', '시각화와 실제 결과 예측을 구분하고 각 하위 모델의 입력·출력·측정 지표를 정의한다.', 'foresight', 'high', ['공간·이동·대기·선택', '사용자 동선 분석']),
    ('국가별 FORESIGHT 메시지와 광고 실험 설계', '시장별 언어와 가설을 나눠 캠페인·랜딩·전환 지표를 비교한다. 과거 광고 성과 메모를 기준선으로 사용한다.', 'foresight', 'medium', ['나라별로 나눠서 광고도', '아시아 애드셋 + 영상 소재 중단']),
    ('MarketClaw 프로토타입 기능의 이관 상태 점검', '기존 프로토타입에서 필요한 기능이 모두 옮겨졌는지 확인하고 누락을 작업 목록으로 만든다.', 'marketclaw', 'high', ['MarketClaw는 계속해', '원본 제외하고는 결국에 다 필요한거']),
    ('MarketClaw 설정·인증정보를 환경변수로 통일', '평문에 들어간 설정값과 토큰을 점검하고 로컬·배포 환경의 안전한 설정 경로로 옮긴다.', 'marketclaw', 'high', ['일단 평문으로 안들어가게 수정해줘']),
    ('마케팅 에이전트의 광고 A/B 테스트 루프 설계', '광고 설정, 성과 관측, 실험 중단·확대 판단을 검토 가능한 루프로 만든다.', 'marketclaw', 'medium', ['자율적으로 광고 셋팅과 A/B test']),
    ('Event Twin의 페르소나 30분 단위 일정 모델링', '행사 방문자의 시간대별 일정·관심 확률·타겟군 분포를 실측 데이터와 비교할 수 있게 정의한다.', 'event-twin', 'high', ['30분단위로 미리 세울필요']),
    ('Event Twin 시뮬레이션의 히트맵·동선 분석 추가', '공간별 이동·대기·선택 결과를 사용자에게 설명 가능한 시각화로 묶는다.', 'event-twin', 'medium', ['히트맵이나 여러 분석', '사용자 동선 분석']),
    ('GS2500 시뮬레이션 로직과 Event Twin의 관계 정리', '두 프로젝트의 모델·입력 데이터·데모 차이를 문서화하고 재사용할 부분을 식별한다.', 'event-twin', 'medium', ['gs2500 레포 시뮬레이션 로직 전달하기']),
    ('Obulus의 앱·MCP 제품 경로 결정', '개인 DB 검색, 유료 조회, 기여 정산을 어떤 인터페이스에서 시작할지 비교한다.', 'obulus', 'medium', ['obulus 앱 또는 mcp 형태']),
    ('멀티 기기 파일·에이전트 상태 검색 프로토타입', '파일이 어느 기기에 있는지 찾고 다른 기기에서 열거나 처리할 수 있는 최소 흐름을 만든다.', 'multi-device', 'medium', ['특정 파일이 회사 컴퓨터에 있었는지', '한 컴퓨터의 데이터를 다른곳에서 처리하기']),
    ('멀티 기기 오케스트레이터 메모리 구조 정리', '기기 간 에이전트 작업 분배와 메모리 동기화 경계를 정의한다.', 'multi-device', 'medium', ['멀티 머신에서 orchestrator 효율적으로']),
    ('Agent24 합성 페르소나와 결정 과정 표시 검토', '라운드·결정 이벤트를 스트림과 UI에 드러내고 페르소나 합성기 범위를 재확인한다.', 'agent24', 'medium', ['페르소나 합성기 완성하기', '에이전트 결정 과정 투명화']),
    ('Ralpli/Goaltending 평가 루프 문서화', '목표 분해, 병렬 실험, 평가 함수, 사용자 질문, 백프레셔를 한 아키텍처로 정리한다.', 'agent-harness', 'medium', ['goal tending 시스템', '하네스는 조립가능하고 단방향성을']),
    ('Airlock fitness 개선 데모와 검증 지표 재점검', '병렬 실행 후보가 실제로 더 나은 결과를 내는지 측정 가능한 사례를 정리한다.', 'airlock', 'medium', ['fitness그래프가 진짜 올라가서']),
    ('생물학 논문 인용 그래프 자동 확장 설계', '논문 citation에서 엔티티·관계를 추출하고 근거와 함께 지식그래프를 갱신하는 흐름을 설계한다.', 'biology', 'medium', ['논문 citation을 보고 에이전트들이']),
    ('Vision Pro 공간 캡처 품질 개선 근거 정리', 'Gaussian splatting과 LiDAR 조합, 문·창문 인식, 사용자 조작 화면의 문제를 묶어 다음 실험을 정의한다.', 'spatial-design', 'low', ['가우시안 스플래팅과 lidar', '문도 인식이 안되네']),
    ('Popga의 QR·바이럴·랭킹 실험 우선순위 정리', '2026-08 메모의 성장 아이디어를 검증 가능성·실행 비용 기준으로 정리한다.', 'popga', 'low', ['팝업 qr, ip 바이럴 뉴스']),
    ('GitHub 포트폴리오의 최신 데모·README 점검', '레포별 최신 화면, 설명, 영상, 수상 경력을 일치시키고 오래된 스크린샷을 교체한다.', 'career', 'medium', ['내 모든 yc9954 레포지토리 readme', 'motioncad 레포에 4번째 사진']),
    ('수상·보도 자료를 이력서와 포트폴리오에 연결', 'GS2500, Agent24, Ralphthon 등의 증빙 링크와 최신 성과를 정리한다.', 'career', 'medium', ['기사 기반으로 레쥬메에 하이퍼링크', 'Ralphthon @ICML finalist']),
    ('불필요한 구독·청구 상태 확인', '2026-09 메모의 Genspark, Kimi, LinkedIn, ElevenLabs, Meta 청구를 현재 상태와 대조하고 필요 없는 구독을 정리한다.', 'career', 'medium', ['젠스파크 구독끊기', '키미 구독 끊기']),
    ('NVIDIA·Applied AI 협업 후보 조사', '인셉션 프로그램, 관련 팀·연구자, 적합한 PoC 사례를 모아 연락 우선순위를 정한다.', 'career', 'low', ['엔비디아 인셉션 따기', 'applied ai 쪽 관심갖기']),
    ('ICML AC 리뷰 에이전트의 현재 학습·데모 상태 확인', '7월 기록의 점수 헤드, 메타리뷰, 논문 수정 루프가 현재 어느 단계인지 확인하고 재개 여부를 결정한다.', 'icml-review', 'medium', ['ICML 논문 리뷰에이전트', '학습 3시간 컷']),
    ('Octopus와 MarketClaw의 제품·코드 관계 정리', '6월 Octopus 구상과 9월 MarketClaw 구현이 공유하는 범위, 독립적인 아이디어, 남길 자산을 구분한다.', 'octopus', 'low', ['n8n은 필요없고 human4depth', '하나의 에이전트 채팅에서 모든 기능']),
    ('수면 코치의 기상 후 피드백과 설정 UI 점검', '사용자가 실제 수면 후 개운함을 기록할 수 있는지, 추천·설정 화면이 동작하는지 확인한다.', 'sleep-coach', 'low', ['기상 후에 개운한지', '설정탭이 아얘 없다']),
    ('펀치 게임의 점수·프로필 흐름 정리', '펀치 입력, 점수판, 이름 수정, 기록 보기 화면을 하나의 모바일 사용자 흐름으로 정리한다.', 'punch-game', 'low', ['펀치기계 아래에 위대한 직장인', '펀치기계를 클릭으로']),
    ('Self-Evolving Skill Hub의 범용 아키텍처 정리', 'Helix 기반 구조에서 회사 전용 경로·용어를 분리하고 독립 프로젝트의 범위를 정한다.', 'skill-hub', 'medium', ['self-evolving-skill-hub']),
    ('TGP 자기학습의 검증 지표와 데모 재점검', '정답률 상승 주장과 자유 채팅에서의 평가 기준을 구분하고 실제 개선 결과를 재현한다.', 'tgp', 'medium', ['측정된 자기학습', 'GSM8K 65%']),
    ('StableDAG 논문의 최신 검증·출판 상태 확인', '3월 작업 초안의 독립 검증, 결과 재현, 외부 리뷰와 최신 원고 상태를 확인한다.', 'stable-dag', 'low', ['StableDAG', 'DEG Paper — Live Preview.pdf']),
    ('GraphSAGE 허브 유전자 원고의 수정 표시 확인', '원고의 저자 기여·감사의 수정 메모와 방법·실험 결과 빈 부분이 이후 버전에서 해결됐는지 확인한다.', 'hub-gene', 'low', ['Manuscript.docx', 'Biologically Consistent Graph Embedding']),
]


STUDIES = [
    ('운영체제 기초와 프로세스', '커널, 프로세스, daemon, cron, 메모리·스왑의 관계를 이해한다.', 'OS 강의와 실습을 연결해 정리. 프로세스·스케줄링·파일 시스템·메모리를 순서대로 복습한다.', 'learning', ['Os책 사기', 'daemon과 cron 잡의 차이']),
    ('Git과 GitHub 작업 흐름', 'remote, branch, PR, merge, 배포와 협업 흐름을 실습한다.', 'Git 기초에서 협업까지 실제 레포 작업과 연결해 정리한다.', 'learning', ['git remote 및 git 조금더 잘알아보기', '철저한 git 프론트 백 공부']),
    ('클라우드 인프라 · GCP/AWS/Azure', '인스턴스, 네트워크, IAM, 배포, 비용을 한 아키텍처로 이해한다.', 'GCP·AWS·Azure의 공통 개념과 차이: VM, 방화벽, 프록시, 컨테이너, IAM, 관측성.', 'learning', ['Azure GitHub 인프라 관리 명확하게', 'gcp', 'aws bedrock 심도있게']),
    ('Docker · Kubernetes · Helm', '컨테이너 빌드와 배포·오케스트레이션을 연결한다.', 'Dockerfile·Compose·Kubernetes·Helm의 역할과 배포 단위를 비교한다.', 'learning', ['k8s도 심도있게 공부', 'Dockerfile Jib 어떤 차이']),
    ('데이터 아키텍처 · SQL/BigQuery/Databricks', '데이터베이스, 웨어하우스, 파이프라인, 스키마 설계를 이해한다.', 'SQLite·PostgreSQL·BigQuery·Databricks·DDL과 데이터 파이프라인을 실제 프로젝트 맥락에서 정리한다.', 'learning', ['데이터 아키텍쳐 공부하기', 'databricks 공부']),
    ('비동기·동시성 · Python 작업 실행', 'GIL, 스레드, 워커, 큐, 비동기 실행을 구분한다.', 'ThreadPoolExecutor, Redis/Celery, 스케줄러의 성능·격리 차이를 실습한다.', 'learning', ['ThreadPoolExecutor', 'redis celery 원리 확실히 알기']),
    ('RAG · 온톨로지 · 지식그래프', '검색 증강, 엔티티 관계, 도메인 온톨로지의 역할을 구분한다.', 'RAG와 지식그래프의 결합, citation 기반 관계 추출, Palantir 용어와 DB 용어의 차이를 정리한다.', 'biology', ['온톨로지랑 지식그래프는 다른거같긴한데', 'database의 ontology랑 palantir']),
    ('LLM 파인튜닝 · SFT/DPO', '모델 학습 방식과 프롬프트·메모리의 역할을 구분한다.', 'SFT, DPO, 데이터셋 품질, 지속적 개선과 프롬프트 누적의 한계를 비교한다.', 'learning', ['파인튜닝 공부', 'SFT: 좋은 입력/출력 예시']),
    ('에이전트 메모리와 MCP 아키텍처', '세션 간 기억, 도구 스키마, MCP 서버 경계를 이해한다.', '기억 저장·검색, 도구 정의 로딩, 에이전트 간 공유 메모리 구조를 정리한다.', 'agent-harness', ['오픈소스 mcp는 api키 없이 어떻게 작동하나', '툴 이름만 로드되고 스키마는']),
    ('Playwright · CDP · Computer Use', '브라우저 자동화 층위와 제약을 구분한다.', 'Playwright API와 CDP, DOM 조작, 화면 기반 조작의 차이를 실제 작업 흐름으로 비교한다.', 'learning', ['Playwright과 cdp의 차이가 뭘까', 'cua-driver computer use']),
    ('분산 추론과 이기종 GPU', '여러 기기·GPU에 모델 추론을 나누는 방법을 이해한다.', '레이어 분할, 네트워크 전송, 일관성·장애 복구를 DRIFT 등 사례와 연결한다.', 'multi-device', ['멀티 디바이스에 적절한 사양', '로컬 LLM인데 필요한 부분만']),
    ('사회·이벤트 월드모델', '사건, 상태 변화, 결과를 예측하는 모델의 학습·추론 구조를 연구한다.', '조회수만이 아니라 중간 사건·여론·집단 내부 상태·시간 곡선을 어떻게 표현할지 정리한다.', 'foresight', ['상태 · 사건 · 결과', '중간 중간에 발생하는 이벤트들이나']),
    ('에이전트 기반 공간 시뮬레이션', '공간·이동·대기·선택 모델과 결과 예측을 구분한다.', 'NVIDIA FLAME GPU와 실제 팝업·행사 데이터 적용 가능성을 검토한다.', 'event-twin', ['공간 시뮬레이션에는 어떤 방법', '사용자 동선 분석']),
    ('Gaussian Splatting · LiDAR · Vision Pro', '실제 공간을 3D로 캡처하고 편집·표시하는 기술을 익힌다.', 'Gaussian Splatting, LiDAR, 360 사진→공간, Vision Pro 렌더링의 장단점을 비교한다.', 'spatial-design', ['가우시안 스플래팅과 lidar', '비전프로']),
    ('마케팅 믹스 모델 · Bayesian 실험', '광고 기여도, 실험 설계, 포화·시차 효과를 학습한다.', 'MMM, adstock, saturation, geo-level 분석을 FORESIGHT 광고·고객 확보에 연결한다.', 'marketclaw', ['Marketing Mix Modeling', '빅테크의 마케팅 효과 예측 모델']),
    ('x402와 마이크로 결제', '에이전트가 유료 데이터 조회·기여 정산을 수행하는 구조를 이해한다.', 'HTTP 402, 결제 검증, 개인 데이터 접근 권한, 기여도 정산을 Obulus 설계와 연결한다.', 'obulus', ['x402', '개인 DB를 웹사이트처럼']),
    ('해커톤 평가 기준과 수상작 분석', '평가 항목, 제출 조건, 영상·데모 효과를 학습한다.', 'Devpost Scout에서 대회별 기준을 읽고 수상작과 비교해 아이디어·데모를 검증한다.', 'devpost-scout', ['해커톤 우승자들 기반 아이디어 산출기', '완성도: 팀이 최소한의 MVP']),
    ('영상 콘티 · HTML 기반 영상 제작', '화면 녹화, 컷 편집, HTML→영상, 내레이션과 자막을 익힌다.', 'Screen Studio, Hyperframes, Blender와 실제 데모 제작 흐름을 비교한다.', 'video', ['콘티 뽑아주는 하네스', '클로드처럼 영상편집하는법']),
    ('제품 디자인 시스템과 UI 컴포넌트', '재사용 가능한 컴포넌트, 시각적 일관성, 인터랙션 설계를 익힌다.', '21st.dev, Figma 가이드, 기존 제품 UI를 레퍼런스로 삼아 프로젝트별 디자인 시스템을 정리한다.', 'learning', ['팝가 디자인시스템제작', '스위트스팟 디자인시스템 제작']),
    ('NVIDIA NemoClaw · 에이전트 배포', '에이전트 런타임과 보안·통신 프로토콜을 이해한다.', 'NemoClaw 강의와 관련 아키텍처를 하나의 구조도로 정리한다.', 'learning', ['네모클로 html 다시 보고 통신 프로토콜']),
    ('Trainium · 모델 최적화 실험', '추론·학습 성능 지표와 실험 루프를 이해한다.', 'BPB, 후보 탐색, 평가와 원격 컴퓨트 운영을 사례로 정리한다.', 'airlock', ['trainium 해커톤 끝나고서도 계속 bpb']),
    ('ICML 리뷰·메타리뷰와 점수 헤드', '학술 리뷰, AC 메타리뷰, 점수 산정의 역할과 데이터 흐름을 이해한다.', '리뷰어 의견에서 메타리뷰와 총점을 만들고 수정 제안이 다음 논문 버전에 반영되는 루프를 정리한다.', 'icml-review', ['ICML 논문 리뷰에이전트', '메타리뷰는 논문의 최종 결과']),
    ('vLLM Multi-LoRA와 Score Head', '하나의 기반 모델에 여러 LoRA 어댑터를 올리는 방식과 별도 점수 헤드를 구분한다.', '서빙 구조, 학습 데이터, 추론 지연, 리뷰 점수 정규화 흐름을 ICML AC 프로젝트 맥락에서 검토한다.', 'icml-review', ['vLLM multi-LoRA', '스코어 헤드']),
    ('수면주기와 기상시간 추천 모델', '수면 단계, 90분 주기 가정, 개인차와 사용자 피드백을 구분한다.', '수면·기상 시간을 추천할 때 가정과 근거를 화면에 보여주고 기상 후 개운함 평가로 조정하는 방식을 공부한다.', 'sleep-coach', ['수면을 설정했다고', '기상 후에 개운한지']),
    ('TGP와 온라인 자기학습 평가', '정답이 있는 과제의 측정된 개선과 자유 채팅에서의 평가 문제를 이해한다.', 'GSM8K 같은 벤치마크와 실제 사용자 대화에 각각 어떤 fitness·검증 기준이 필요한지 비교한다.', 'tgp', ['측정된 자기학습', '자유 채팅엔 정답이 없어서']),
    ('StableDAG · 연속 DAG 학습과 CausalFlow', 'DAGMA 기반 연속 DAG 추정, 안정성 정규화, 유전자 조절 계층 점수화를 이해한다.', '부트스트랩 일치도, 희소성 설정, 방향성 검증과 질환 간 일반화 조건을 원고 초안에 연결해 정리한다.', 'stable-dag', ['StableDAG', 'CausalFlow']),
    ('Disease-aware GraphSAGE · 허브 유전자 발견', 'PPI·발현·HPO 표현형 신호를 결합하는 그래프 임베딩 구조를 이해한다.', 'SHEPHERD 임베딩, GraphSAGE, Procrustes 정렬, 허브 점수 구성과 실험 검증을 원고 초안에서 추적한다.', 'hub-gene', ['GraphSAGE', 'Hub Gene Discovery']),
]


def stable_id(kind, key):
    return hashlib.sha256(f'personal-workspace:2026-03:{kind}:{key}'.encode()).hexdigest()[:32]


def evidence(db, queries, limit=4):
    found = []
    for query in queries:
        rows = db.execute('SELECT id, source, occurred_at, source_url FROM imported_notes '
                          "WHERE kind != 'result' AND body LIKE ? ORDER BY occurred_at DESC LIMIT 2",
                          ('%' + query + '%',)).fetchall()
        for row in rows:
            if row['id'] not in {item['id'] for item in found}:
                found.append(dict(row))
            if len(found) >= limit:
                break
    return found[:limit]


def source_text(rows, markdown=False):
    if not rows:
        return ''
    return '\n'.join(f"- {row['source']} {row['occurred_at'][:10]} · "
                     + (f"[원문](#/history/{row['id']})" if markdown else f"#/history/{row['id']}")
                     + (f" · {row['source_url']}" if row['source_url'] else '') for row in rows)


def insert(db, table, values):
    keys = list(values)
    db.execute(f'INSERT OR IGNORE INTO {table} ({", ".join(keys)}) '
               f'VALUES ({", ".join("?" for _ in keys)})', tuple(values.values()))


def tag_sources(db, rows, table, item_id):
    for row in rows:
        db.execute("UPDATE imported_notes SET linked_type = ?, linked_id = ? WHERE id = ? AND linked_type = ''",
                   (table, item_id, row['id']))


def resource_project(title, url):
    text = (title + ' ' + url).lower()
    if any(word in text for word in ('hackathon', 'devpost', 'cococli', 'agent24/issues', 'trainium-frontier')):
        return 'devpost-scout'
    if any(word in text for word in ('hyperframes', 'blender', '영상', 'screen.studio', 'hologram')):
        return 'video'
    if any(word in text for word in ('drift', 'distributed', 'agent memory', 'hermes', 'claude code', 'prompt caching')):
        return 'agent-harness'
    if any(word in text for word in ('nvidia', 'nemoclaw', 'flame gpu', 'simulation')):
        return 'event-twin'
    if any(word in text for word in ('worldlabs', '360', 'vision', 'mumax3')):
        return 'spatial-design'
    if any(word in text for word in ('ontology', '지식그래프', 'disease biology')):
        return 'biology'
    if any(word in text for word in ('git', 'operating system', 'os course', 'inflearn')):
        return 'learning'
    if any(word in text for word in ('foresight', 'gs 해커톤', '팝업')):
        return 'foresight'
    return 'learning'


def include_resource(item):
    parts = urlsplit(item['url'])
    host, path = parts.hostname or '', parts.path
    if host in ('www.sec.gov', 'sqlitebrowser.org'):
        return False
    if host == 'github.com' and (path == '/yc9954' or '/issues/' in path):
        return False
    if host in ('instagram.com', 'www.instagram.com') and path.startswith('/2.ucan'):
        return False
    if host in ('alisawuffles.notion.site',) and item['title'].startswith('Notion |'):
        # The link is retained in Collected notes; metadata does not reveal its content.
        return False
    return True


def matching_resource_note(db, url):
    parts = urlsplit(url)
    target = parse_qs(parts.query).get('v', [''])[0] if 'youtube.com' in parts.netloc and parts.path == '/watch' else ''
    if not target:
        target = parts.netloc + parts.path
    row = db.execute('SELECT id, source, occurred_at, source_url FROM imported_notes '
                     "WHERE kind = 'link' AND urls_json LIKE ? ORDER BY occurred_at DESC LIMIT 1",
                     ('%' + target + '%',)).fetchone()
    return [dict(row)] if row else []


def main():
    path = config.DATA / 'workspace.db'
    db = sqlite3.connect(path)
    db.row_factory = sqlite3.Row
    db.execute('PRAGMA foreign_keys = ON')
    now = datetime.now(timezone.utc).isoformat(timespec='milliseconds')
    project_ids = {key: stable_id('project', key) for key, *_ in PROJECTS}
    unmatched = []
    for key, title, description, status, queries in PROJECTS:
        rows = evidence(db, queries)
        if not rows:
            unmatched.append('project:' + key)
        item_id = project_ids[key]
        insert(db, 'projects', {'id': item_id, 'title': title, 'description':
               description + ('\n\n관련 기록:\n' + source_text(rows) if rows else ''),
               'status': status, 'created_at': now, 'updated_at': now})
        tag_sources(db, rows, 'projects', item_id)
    for title, details, project, priority, queries in TASKS:
        rows = evidence(db, queries)
        if not rows:
            unmatched.append('task:' + title)
        item_id = stable_id('task', title)
        completed = False
        if title == 'MarketClaw 프로토타입 기능의 이관 상태 점검':
            result = db.execute("SELECT id, source, occurred_at, source_url FROM imported_notes "
                                "WHERE source = 'claude-result' AND body LIKE '%PR #2가 머지됐고%' "
                                'ORDER BY occurred_at DESC LIMIT 1').fetchone()
            if result:
                rows.append(dict(result))
                completed = True
        insert(db, 'tasks', {'id': item_id, 'title': title, 'details':
               details + ('\n\n관련 기록:\n' + source_text(rows) if rows else ''),
               'status': 'done' if completed else 'todo', 'priority': priority, 'due_on': None,
               'project_id': project_ids[project], 'agent_id': None,
               'created_at': now, 'updated_at': now})
        tag_sources(db, rows, 'tasks', item_id)
    for title, summary, outline, project, queries in STUDIES:
        rows = evidence(db, queries)
        if not rows:
            unmatched.append('study:' + title)
        item_id = stable_id('study', title)
        insert(db, 'studies', {'id': item_id, 'title': title, 'summary': summary,
               'body': outline + ('\n\n## 관련 기록\n' + source_text(rows, markdown=True) if rows else ''),
               'status': 'inbox', 'category': 'hackathon' if project == 'devpost-scout' else 'general',
               'source_url': '', 'project_id': project_ids[project], 'hackathon_host': '',
               'created_at': now, 'updated_at': now})
        tag_sources(db, rows, 'studies', item_id)
    metadata_path = config.DATA / 'import_2026-03/link_metadata.json'
    resources = json.loads(metadata_path.read_text(encoding='utf-8'))
    for resource in resources:
        if not include_resource(resource):
            continue
        url = resource['url']
        title = resource['title'] or (urlsplit(url).netloc + urlsplit(url).path)
        if title.startswith('GitHub - '):
            title = title.replace('GitHub - ', '', 1)
        if len(title) > 200:
            title = title[:197] + '…'
        rows = matching_resource_note(db, url)
        summary = (resource['description'] or '링크만 저장된 자료. 원문을 열어 확인한 뒤 학습 상태를 변경하세요.')[:2000]
        category = 'hackathon' if any(word in (title + url).lower() for word in ('hackathon', 'devpost', 'cococli')) else 'general'
        project = resource_project(title, url)
        body = ('링크로 저장한 자료입니다. 제목과 설명은 공개 페이지의 메타데이터에서 확인했습니다.'
                if resource['verified'] else '링크로 저장한 자료입니다. 공개 페이지 제목은 확인되지 않았습니다.')
        body += '\n\n' + summary + '\n\n원문: ' + url
        if rows:
            body += '\n\n## 저장 기록\n' + source_text(rows, markdown=True)
        item_id = stable_id('resource', url)
        insert(db, 'studies', {'id': item_id, 'title': title, 'summary': summary,
               'body': body, 'status': 'inbox', 'category': category, 'source_url': url,
               'project_id': project_ids[project],
               'hackathon_host': urlsplit(url).netloc if category == 'hackathon' else '',
               'created_at': now, 'updated_at': now})
        tag_sources(db, rows, 'studies', item_id)
    db.commit()
    print(json.dumps({'projects': db.execute('SELECT COUNT(*) FROM projects').fetchone()[0],
                      'tasks': db.execute('SELECT COUNT(*) FROM tasks').fetchone()[0],
                      'studies': db.execute('SELECT COUNT(*) FROM studies').fetchone()[0],
                      'unmatched_evidence': unmatched}, ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main()
