---
slug: "not-my-nana"
url: "https://devpost.com/software/not-my-nana"
title: "Not My Nana ❤️"
hackathon: "Amazon Nova AI Hackathon"
organization: "Amazon"
winner: true
words: 1214
team_size: 1
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "mechanism/simulation_digital_twin"
  - "mechanism/structural_withholding"
  - "mechanism/vision_ocr"
  - "domain/education"
  - "domain/elder_child_care"
  - "domain/finance_payments"
  - "domain/immigration_refugee"
  - "domain/mental_health"
  - "domain/security_privacy"
  - "domain/transportation"
  - "user/developer"
  - "user/general_public"
  - "substrate/document_pdf"
  - "substrate/video_visual"
  - "substrate/web_dom"
---

# Not My Nana ❤️

> Protecting our loved ones from digital deception with the reasoning power of #AmazonNova.

[Devpost](https://devpost.com/software/not-my-nana) · hackathon [[Amazon Nova AI Hackathon]]

## Facets

**mechanism** [[realtime_stream]] [[simulation_digital_twin]] [[structural_withholding]] [[vision_ocr]]
**domain** [[education]] [[elder_child_care]] [[finance_payments]] [[immigration_refugee]] [[mental_health]] [[security_privacy]] [[transportation]]
**user** [[developer]] [[general_public]]
**substrate** [[document_pdf]] [[video_visual]] [[web_dom]]

**stack** ai, amazon, css, docker, fastapi, github, html, httpx, javascript, localstorage, multimodal, nova, ocr, pillow

## How they structured the write-up

- inspiration
- what it does
- how we built it
- why amazon nova was the key
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for not my nana ❤️

## Body

Redacted PII in Railway Prompt2: Grandchild Prompt1: Detective Scam message example Homepage, Dark Mode Loading, Day Mode Green result, Safe information Grey result, AI Image detected Yellow result, Viral messages detected Purple result, Sensitive messages detected Red result, Scam messages detected History, Thumbnails, Short result descriptions about the thumbnails, and Clear button Inspiration This project is deeply personal. My own parents and several elderly relatives have personally received fake wedding invitations, urgent "bank" PDF alerts, strangers demanding OTPs, fear-mongering viral posts, and prize messages that sound too good to be true. Some are harmless clickbait; others are sophisticated scams and often using AI-generated images or high-pressure tactics. The emotional toll is huge: shame, isolation, constant anxiety about every message. Worse, adult children sometimes unintentionally blame the elders for falling victim, yet they're often not there in real time to help decide. Many seniors feel too afraid or ashamed to ask us, and gentle corrections can make them stop sharing concerns entirely, widening the family gap. According to the FTC's FTC Protecting Older Consumers 2024-2025 report , reported fraud losses by adults 60+ skyrocketed to $2.4 billion in 2024 — a roughly fourfold increase from about $600 million in 2020 . This surge was largely driven by reports of losses over $100,000 . Due to widespread underreporting, the FTC estimates real losses could reach as high as $81.5 billion . Many elders have kind, trusting hearts and rarely cross-check sources instinctively. Scammers only need one success. While child online safety gets attention, lonely seniors, living alone or in care, face similar risks with less support. That's why Not My Nana exists: a private, gentle tool they control themselves , so they feel empowered, not scolded. What it does Not My Nana is a lightweight, privacy-first Progressive Web App (PWA) that lets elderly users check suspicious screenshots in just few taps. No login, no personal data ever collected. See something suspicious → take a screenshot. Open the app from your home screen. Tap the big orange button. Choose the screenshot you want to check. Results appear as large, color-coded boxes with clear emojis: ✅ Safe / Real (green) ❌ Scam! Danger (red) 🤖 Fake photo (AI) (grey) 👨‍👩‍👧‍👦 Talk to family (purple – sensitive topics) 📰 Clickbait News (yellow – viral content) We avoid blanket "100% safe" verdicts on borderline items to encourage gentle caution — many elders trust everything by default. Tapping details shows exactly two warm sentences from a simulated "grandchild" (in their detected language), e.g.: Scam: “🚨 Nana, this is a scam! They’re pretending to be the bank and want your details — please don’t reply or click. ❤️” AI image: “🖼️ Nana, this picture was made by a computer (AI). It looks real but the hands and background are wrong — it’s not a genuine photo. ❤️” Everything stays local : last 3 thumbnails in history, light/dark theme toggle, easy delete button. Only redacted image + OCR text ever touches the cloud. How we built it Frontend : Simple HTML/CSS/JS PWA (installable on iOS/Android home screen). Big touch-friendly button, color-coded results, localStorage for history (max 3 thumbnails), theme toggle. Backend : FastAPI (Python) server for analysis endpoint. Local privacy layer : Tesseract OCR + regex + Pillow to detect & black out PII (phones, names, cards, emails) before upload. AI pipeline : Two-stage calls to Amazon Nova 2 Lite: Detective prompt → strict JSON: category, is_ai, scam_probability, dominant_language, technical findings. Empathy prompt → warm 2-sentence title + grandma_reply in detected language. Hardening: retries, rate limiting (15/min per IP), idempotency keys, friendly fallbacks. Deployed as lightweight service (runs anywhere with Nova API key). Why Amazon Nova was the key Amazon Nova 2 Lite was essential for frontier multimodal reasoning at everyday speed & cost. True one-pass multimodal (pixels + text) : Spots AI artifacts (distorted hands, unnatural textures, lighting/physics issues) even when text seems normal. Deep reasoning beyond keywords : Detects urgency/fear/greed, clickbait patterns, sensitive topics. Automatic language detection & natural generation : Supports non-English families seamlessly. Fast (10–25s) + cost-effective : Perfect for quick, frequent checks. Large context window : Reliable & future-proof. No separate vision model needed. Nova handled everything in one efficient call, enabling the warm "grandchild" tone that builds trust. Challenges we ran into AWS Bedrock / Nova API access was painful at first (permissions, tokens failing). Prompt engineering took dozens of iterations, tiny wording changes often flipped categories completely. Fixing one bug sometimes silently altered behavior, so I had to re-test extensively. Coderabbit kept finding subtle bugs I missed (humbling and useful). Deciding what to build vs. cut was overwhelming. AI agents gave advanced suggestions, but I had to choose what was realistic in one week for a first-time full-web-app builder. Ensuring few taps simplicity, big text/emojis, fallback messages that feel kind ("❤️ Nana, my brain is having trouble connecting..."). Added retries/exponential backoff + idempotency to avoid double-billing or flaky experiences. Relying on Nova's detection to handle global families without manual tuning. Very much relying on the prompt for this. Accomplishments that we're proud of First serious use of so many tools — and it shipped! Built a truly full-stack, privacy-first, multimodal app in a sprint. Zero personal data, local redaction, everything deletable. Lightweight PWA, installs in seconds, works offline for history/theme, and UX so simple even non-tech grandparents can use it independently. Multimodal detection that confidently spots AI-generated images (via pixel + text analysis) and subtle scams humans might miss. Language-aware replies open the door to helping millions of non-English-speaking grandparents worldwide. The Detective → Grandchild handoff really works. Delivered warm, human-feeling advice via frontier AI, turns cold forensics into supportive "grandchild" words. Short, warm, clear answers. What we learned Time management is everything. I lost hours waiting for Coderabbit reviews when I could have been writing docs, scripting the video, or polishing README. Next time I’ll parallelize tasks. New tools become comfortable fast. In days I went from zero to confident with VS Code + GitHub, Coderabbit, Docker, Railway, terminal, async HTTP with retries. I really can build real software. Coming from security (not full-time dev), I always thought shipping production-grade apps was for others. This proved I can take an idea → wrestle with tools → deploy something that helps real people. That feeling is huge and addictive. Immersion beats perfection. Jumping into unfamiliar workflows felt overwhelming, but learning by doing was fastest and most rewarding. Seeing the app live on the internet made every late night worth it. Privacy isn't optional Redaction builds confidence for scam-vulnerable users. Multimodal frontier models like Nova 2 Lite can do empathetic rewriting + forensics in one ecosystem. Simplicity wins Every extra feature risks confusion; single-purpose tools are powerful. Real-world impact feels personal Protecting family from shame/loss is worth every debug night. What's next for Not My Nana ❤️ Open-source the full repo on GitHub soon (privacy-focused code). Share on Reddit groups, senior forums, family groups. Reach out to NGOs/senior centers for pilot testing/digital-literacy integration. Explore Nova 2 Sonic for optional voice input/output. Add offline mode hints, more maintainers, community feedback for edge cases. Long-term: Partner with AARP-like orgs to reach more families. Install the PWA https://not-my-nana-production.up.railway.app/ , try a suspicious screenshot, and share with grandparents/family. Let's make the internet kinder for those who raised us. AmazonNova #MultimodalUnderstanding <div