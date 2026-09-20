---
slug: "tradeproof"
url: "https://devpost.com/software/tradeproof"
title: "TradeProof"
hackathon: "TreeHacks 2026"
organization: "TreeHacks"
winner: true
words: 1103
team_size: 3
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/on_device_local"
  - "mechanism/retrieval_grounding"
  - "mechanism/simulation_digital_twin"
  - "domain/developer_tools"
  - "domain/education"
  - "domain/labor_employment"
  - "substrate/video_visual"
---

# TradeProof

> AI-Native Infrastructure that Reimagines Trade Work for Blue-Collar Careers.

[Devpost](https://devpost.com/software/tradeproof) · hackathon [[TreeHacks 2026]]

## Facets

**mechanism** [[on_device_local]] [[retrieval_grounding]] [[simulation_digital_twin]]
**domain** [[developer_tools]] [[education]] [[labor_employment]]
  <sub>weak: finance_payments</sub>
**substrate** [[video_visual]]

**stack** c#, chatgpt, claude, css, git, github, javascript, metaxr, next.js, openxr, perplexity, shaders, stripe, supabase

## How they structured the write-up

- what inspired us
- what we learned
- how we built it
- challenges we faced
- customer interviews and product feedback

## Body

Home Page Upload Proof of Work Done AI Analysis TradeProof User Profile TradeProof User Portfolio TradeProof User Skills Passport Marketplace As a blue-collar worker, you can match with jobs Browse skilled blue-collar workers, explore their portfolios, compare hourly rates, and hire with confidence Detailed information about potential contractors As an employer, you can scout talent and hire new employees As a blue-collar worker, learn from other blue-collar workers in your trade TradeProof: Cursor for the Skilled Trades What Inspired Us The skilled trades are facing a genuine crisis. While everyone is building AI for xyz and moving industries forward at the speed of light, no one is advancing the infrastructure supporting the backbone of our society, trades work. Presently, there aren't enough people entering the field, and fewer high schoolers are pursuing trades as a career path, and the pipeline is shrinking. The ones who do go through trade school come out underprepared for real job sites, with classroom knowledge that doesn't prepare them for hands-on work. And for the experienced workers, moving between states means starting almost from scratch since licenses don't transfer, records don't follow you, and nobody can tell you exactly what you're missing. We talked to electricians and heard all three of these problems firsthand. TradeProof is built to address them: an all-in-one platform that gets early-career tradespeople up to speed faster, turns their work into portable proof, and makes it easier to hire and be hired based on what you've actually done. What We Learned We also learned that local codes matter enormously. Every electrician we talked to knew the Code Book and the NEC, but the real complexity is in the local amendments layered on top. What passes in one city fails in the one down the street. So we built TradeProof to inject jurisdiction-specific codes directly into every analysis, grounding feedback in the exact rules that apply to where you are working, not generic national standards. Portability came up constantly. People moving to Texas or Arizona want to know exactly what's missing, and right now, there's no good answer for that. So we built the Passport: your skills against another state's requirements, with gaps and course suggestions surfaced instantly. How We Built It TradeProof is a fully working product built on Next.js with Claude handling vision and code analysis. The core flow is: photograph your work → get AI analysis against real NEC codes → recheck after fixes → build a verified portfolio → use it to move states or get hired. Check My Work is the heart of the product. You pick a work type, describe what you did, and submit a photo. TradeProof sends it to Claude with the relevant NEC sections and local amendments injected, including 22 NEC sections scoped by work type, plus jurisdiction-specific amendments. It outputs a structured compliance report: a score, specific violations with exact code sections and fix instructions, and the items you got right. You can submit a before photo, and after fixing something, upload a new photo that tells you exactly what got resolved and what's still open. Every analysis builds your portfolio, tracking compliance scores and eight skill categories over time. Knowledge surfaces expert insight cards tied to what you're actually working on. Trigger keywords from your analysis pull relevant clips, such as an analysis flagging panel work might surface a card on Federal Pacific panels or aluminum wiring. It's learning in context, not a separate course you have to go take. Passport takes your portfolio and runs a live gap analysis against another state's licensing requirements. Moving from California to Texas? You see exactly which certifications you're missing, which hour requirements you haven't hit, and what courses could close the gap, giving you real cost in terms of time and pricing. Marketplace is where the portfolio becomes leveraged. Employers see a credential view with your TradeProof compliance stats, skill scores, and trend alongside a traditional resume. Workers swipe on jobs, employers swipe on workers, and matches are grounded in verified proof, not self-reported experience. Challenges We Faced Tailored feedback. Generic AI analysis isn't good enough for a working electrician. The feedback needs to match the exact codes they're held to on the job. Getting there meant building a RAG system over the Code Book so that every analysis is grounded in the specific NEC sections and local amendments that actually apply, not a broad guess at what might be relevant. That was the foundation on which everything else was built. Getting a fully functional electrician training sim running on a standalone VR headset was one of the hardest parts of this project. We built over 60 C# scripts that generate every 3D object from scratch at runtime, including a graph-based circuit simulator that actually tracks how electricity flows through wires, breakers, and outlets, so the VR training behaves like a real electrical system. Coordinating hand tracking, tool interactions, and physics-based snapping across seven different training tasks - each with its own scoring, NEC code validation, and step-by-step logic meant debugging issues we couldn't Google, since most VR projects don't procedurally generate entire electrical panels with functioning circuit breakers. Also, the Meta Quest 2 only has a mobile chip with limited memory, so getting all of this to compile and run smoothly on-device without any pre-built assets or prefabs required constant optimization and was a serious engineering challenge. Customer Interviews and Product Feedback We interviewed over 8 customers in the span of 24 hours. We were able to get 3 paying customers at 50$ pricepoint with following core feedback points: Validation that the problem space is “untapped” potential (eg. electricians do not have software to support their day to day work BUT would love to have/are willing to adopt) The TAM and target demographic for our problem space is huge, through talking with customers we learned that trade schools, educators, individual business owners and even homeowners would be possible paying customers The problem is bigger than we expected, experienced blue collar workers are retiring and 1) no one to train future workforce 2) young people are discouraged by a lack of infrastructure and job clarity resulting in less tradespeople. The time is now to build the end to end infrastructure to solve these 2 core problems that are growing daily. Our product was later recommended to Douglas Hansen, writer of the famous book (Code Check) which is referenced by every electrician. We spoke with Douglas and learned that this space has had no innovation for decades. A product like ours, if proven reliable, would be revolutionary for the work he does that reaches thousands daily. <div