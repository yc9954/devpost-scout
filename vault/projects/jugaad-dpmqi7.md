---
slug: "jugaad-dpmqi7"
url: "https://devpost.com/software/jugaad-dpmqi7"
title: "JUGAAD"
hackathon: "UC Berkeley AI Hackathon 2026"
organization: "Cal Hacks"
winner: true
words: 1369
team_size: 4
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/graph_reasoning"
  - "mechanism/multi_agent"
  - "mechanism/realtime_stream"
  - "mechanism/structural_withholding"
  - "mechanism/voice_speech"
  - "domain/agriculture_food"
  - "domain/civic_government"
  - "domain/developer_tools"
  - "domain/education"
  - "domain/finance_payments"
  - "domain/housing_homeless"
  - "domain/mental_health"
  - "user/educator_student"
  - "user/general_public"
  - "user/legal_professional"
  - "user/researcher"
  - "user/social_worker"
  - "substrate/code_repository"
  - "substrate/financial_record"
  - "substrate/geospatial"
  - "substrate/transcript_audio"
---

# JUGAAD

> JUGAAD — Just-in-time University Guidance and Actionable Discovery — gives every Berkeley student the insider hacks on food, housing, and financial aid that only connected students know.

[Devpost](https://devpost.com/software/jugaad-dpmqi7) · hackathon [[UC Berkeley AI Hackathon 2026]]

## Facets

**mechanism** [[graph_reasoning]] [[multi_agent]] [[realtime_stream]] [[structural_withholding]] [[voice_speech]]
**domain** [[agriculture_food]] [[civic_government]] [[developer_tools]] [[education]] [[finance_payments]] [[housing_homeless]] [[mental_health]]
  <sub>weak: transportation</sub>
**user** [[educator_student]] [[general_public]] [[legal_professional]] [[researcher]] [[social_worker]]
**substrate** [[code_repository]] [[financial_record]] [[geospatial]] [[transcript_audio]]

**stack** anthropic, arize, browserbase, claude-code, claude-sonnet-4-6, deepgram, fastapi, fetch-ai, microsoft-band, next.js, python, railway, redis, stagehand

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments we're proud of
- what we learned
- what's next for jugaad

## Body

Agents Home Page Multi Agent Orchestration Chat History Student Recommended Resources Agent Registry Networks of Agent User Profile JUGAAD: Just-in-time Guidance & Actionable Discovery Inspiration At Berkeley, solutions to student crises actually exist. CalFresh can give a student $292/month for groceries. The BSC co-ops are 50% cheaper than dorms. The Special Circumstances Appeal can add thousands to your aid package. Let's Talk drop-in counseling has no waitlist and no appointment needed. But here's the problem: none of this information travels equally. It circulates through Greek life, legacy families, and established friend networks. First-gen students, transfer students, international students, and low-income students — the ones who need it most — are systematically excluded from this tribal knowledge. 39% of Berkeley undergrads experience food insecurity. 3,300+ students lack stable housing. FAFSA processing is literally paused right now. And the food pantry serving these students? It's one floor below the hackathon venue. The information asymmetry is the real inequity. JUGAAD stands for J ust-in-time U niversity G uidance and A ctionable D iscovery. We built it to make sure every student gets the hack — not just the connected ones. What It Does JUGAAD works in three steps: 1. Listen — Speak or type your problem. A Claude-powered intake agent asks 6–8 natural questions to understand your exact situation: SAI, citizenship status, meal plan, housing, current aid. This profile powers every personalized recommendation downstream. 2. Match — Five specialized Fetch.ai agents run in parallel, each searching their domain — food, financial aid, safety, wellness, and academics — drawing from a Redis knowledge graph and Browserbase web agents browsing Berkeley sites in real time. 3. Act — A personalized dashboard surfaces your specific "hack stack": not just what resources exist, but how to stack them, what exemptions you qualify for, and pre-filled applications ready to submit. Key features: Hack Stacks — For each domain, Claude assembles 3–6 complementary resources that compound together. Not just "here's the food pantry" but "here's how to stack CalFresh + pantry + Grab N Go + Market Match to eat well on near-zero budget." Apply Now — One click generates a pre-filled personal statement, appeal letter, or CalFresh intake summary using the student's actual profile. The emergency grant statement comes back in under 3 seconds. Deadline Alert Engine — Proactive alerts at 30 days, 7 days, and 48 hours before every relevant deadline tied to the student's matched resources. CalFresh Eligibility Checker — Walks through each student exemption. If SAI=0 and Pell Grant received, immediately surfaces the qualification without needing a full conversation. First 30 Days Checklist — Auto-generated chronological action plan of what to apply for and when. Lease Red-Flag Scanner — Paste a lease; Claude identifies predatory clauses, illegal security deposit terms, and waived habitability rights under California law. Berkeley Problem Map — Anonymized crowdsourced visualization of student struggles by neighborhood, time of day, and domain — a data tool for both individuals and advocacy. How We Built It AI / Claude Layer (Anthropic SDK) The intelligence core is a layered prompt architecture: A master orchestrator prompt defines JUGAAD's persona — a knowledgeable peer who gives you the specific hack, not a generic resource page link. It enforces four tone rules on every response: acknowledge the emotional reality first, normalize with a Berkeley-specific statistic, give the HACK, end with one concrete next action today. Six domain sub-prompts encode Berkeley-specific knowledge: CalFresh stacking strategies, BSC co-op details, the Special Circumstances Appeal process, Let's Talk drop-in locations, enrollment timing hacks. A Claude-as-judge evaluator runs automated quality scoring across 4 criteria (relevance, actionability, persona adherence, safety) and logs results to Arize. We ran 3 evaluation rounds during the hackathon and used the feedback to identify and fix prompt gaps — cross-domain crisis detection being the major improvement. AsyncAnthropic client with SSE streaming so chat responses appear progressively. Multi-Agent Architecture (Fetch.ai + Band) Five specialist agents registered on Agentverse with real addresses, coordinated by a JUGAAD Coordinator Agent via the Fetch.ai mailbox protocol. Band enables cross-domain intelligence: when the financial aid agent detects aid loss, the food agent proactively surfaces CalFresh hacks, and the wellness agent includes mental health resources for financial stress. Data Layer (Redis + Browserbase) Redis stores student session context, a vector-indexed knowledge graph of 30+ Berkeley-specific hacks, and a semantic cache for repeated queries. Browserbase agents browse Berkeley websites in real time — financial aid pages, food pantry hours, SHIP provider directories — ensuring results are never stale. Frontend + Voice (Next.js + Deepgram) Voice-first interface built with Next.js 14 and Tailwind. Deepgram STT captures voice input with live transcription; Deepgram TTS delivers responses back as natural speech. The full intake-to-dashboard flow works hands-free. A real-time agent activity feed shows which agents are running and what they're querying. Observability (Arize + Sentry) Every Claude call is instrumented through Arize with named traces — "intake" , "domain_classify" , "hack_stack_food" , "apply_now_grant" — so we can see the full reasoning chain. Sentry is integrated from the first commit for error monitoring and crash reporting. Challenges We Ran Into FAFSA and financial aid chaos: The One Big Beautiful Bill Act paused FAFSA processing on April 21, 2026. We had to make sure JUGAAD's financial aid prompts accurately reflected the current broken state — not the idealized process — and gave students concrete bridge strategies (short-term emergency loans, special circumstances appeals) for a system that's actively failing them. Citizenship complexity: CalFresh eligibility changed April 1, 2026 for DACA and non-citizen groups. Getting the citizenship routing right — never leaving a student without an option, always pivoting to an alternative — required careful prompt engineering and testing. Cross-domain crisis detection: A student saying "I'm sleeping in my car" isn't asking a housing question — it's a crisis. We built cross-domain distress detection into the master prompt so housing instability, financial hopelessness, and dropout talk all trigger mental health resources alongside the practical hacks. Async streaming in FastAPI: Early implementation of SSE streaming was blocking the event loop. Switched to AsyncAnthropic client and async generator pattern to fix. Vague deadline data: Seed data with deadlines like "end of semester" are unparseable for urgency calculations. We systematically replaced all vague strings with real Fall 2026 dates so the deadline alert engine could actually fire. Accomplishments We're Proud Of The Apply Now personal statement generates in under 3 seconds and sounds like the student wrote it — not like a template. Judges can watch this happen live. Our LLM-as-judge evaluation pipeline caught real prompt failures during the hackathon. We ran 3 rounds and improved the average safety score from 4.5 to 5.0 for housing and financial crisis scenarios by fixing cross-domain crisis detection. The hack stacking logic doesn't just surface the top 3 resources — Claude selects for combination value. A $10 Market Match that doubles CalFresh spend is worth more than a $50 resource used alone. The CalFresh short-circuit identifies likely eligibility in one turn for SAI=0 + Pell Grant students without running a full conversation — because urgency matters. We built a platform that could genuinely help 17,000 food-insecure students, starting with the ones in the building where we built it. What We Learned Prompt engineering for emotional context is fundamentally different from prompt engineering for task completion. Getting JUGAAD to acknowledge the shame of food insecurity before pivoting to the hack required explicit tone rules, not just implicit examples. LLM-as-judge evaluation is a real engineering practice, not a demo trick. It caught failures we wouldn't have found through manual testing. The gap between "resource exists" and "student can access resource" is enormous — and almost entirely an information problem. Berkeley's systems aren't broken in the way most people think; the knowledge about how to navigate them is just hoarded. What's next for JUGAAD Expand to all 10 UC campuses — the same problem exists at UCLA, UC San Diego, UC Davis. The Berkeley knowledge graph becomes a template; local coordinators populate campus-specific hacks. Add persistent user memory so returning students never re-onboard. Build the Food Surplus Network into a real two-sided platform: student organizations with leftover catering post in real time; nearby students get notified. Partner with the Berkeley Basic Needs Center to keep the knowledge graph current and verified. <div