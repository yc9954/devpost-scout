---
slug: "memolune"
url: "https://devpost.com/software/memolune"
title: "MemoLune"
hackathon: "RevenueCat Shipaton 2025"
organization: "RevenueCat"
winner: true
words: 810
team_size: 1
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/retrieval_grounding"
  - "mechanism/vision_ocr"
  - "domain/developer_tools"
  - "domain/education"
  - "user/developer"
  - "substrate/transcript_audio"
  - "substrate/video_visual"
---

# MemoLune

> "Capture ideas instantly — with voice or text." Voice Input × OCR for Quick Notes. Record your everyday moments with voice or text, and keep them safe.

[Devpost](https://devpost.com/software/memolune) · hackathon [[RevenueCat Shipaton 2025]]

## Facets

**mechanism** [[retrieval_grounding]] [[vision_ocr]]
  <sub>weak: realtime_stream, voice_speech</sub>
**domain** [[developer_tools]] [[education]]
**user** [[developer]]
  <sub>weak: educator_student, researcher</sub>
**substrate** [[transcript_audio]] [[video_visual]]
  <sub>weak: code_repository</sub>

**stack** firebase, swift

## Body

MemoLune Project Story Inspiration The spark for MemoLune came when I saw a friend using a social media app’s one-person group chat just to leave memos for herself. That small act made me wonder: why wasn’t there a tool that was as light and natural as chatting, but designed entirely for your own thoughts? At the same time, I was already known in Japan as the author of the best-selling book 「#100日チャレンジ」 (#100-Day Challenge). That book was built on countless memos I had kept while creating 100 apps in 100 days with generative AI. Because of that, I had already become recognized as someone deeply tied to “memo culture.” So when the hackathon was announced, I decided to commit: I would spend 100 days—from the announcement period until release—building MemoLune. It wasn’t just coding; it was a living story I was writing every day. What it does MemoLune is a memo app that feels like a chat app. You can: Speak and see instant transcripts appear. Snap a photo or screenshot and extract text with OCR. Search by calendar, making it easy to revisit what you were thinking on any given day. It already supports six languages (English, Japanese, Korean, Chinese, Spanish, and more), so users across the world can use it naturally. How we built it The app was built in Swift, applying Clean Architecture for scalability and maintainability. Key components included: Apple’s Speech Recognition API for real-time transcription. Vision framework for OCR. Firebase & AdMob for analytics and monetization. But more than code, what shaped MemoLune was daily practice. For 100 days, I used MemoLune myself and had friends test it weekly. Each moment of friction became an opportunity to refine. In fact, I rebuilt MemoLune three times in those 100 days until it felt truly natural. Challenges we ran into The biggest challenge was not technical—it was understanding what I actually wanted. At first, MemoLune was “just another memo app.” But as I lived with it daily, I realized it needed to be closer to a conversation than a note. On the technical side, I faced the usual headaches: code signing issues, App Store privacy requirements, and the difficulty of keeping OCR and speech recognition accurate while maintaining speed. These struggles pushed me to grow both as a developer and as a product thinker. Accomplishments that we're proud of The highlight of this journey was releasing MemoLune live during my keynote at PyCon JP. Since publishing my best-selling book 「#100日チャレンジ」 (#100-Day Challenge), this project has been my largest and most personal challenge—a 100-day journey where I poured in the same intensity, or even more. Sharing the release on the keynote stage wasn’t just a presentation—it was a way to show the developer community what happens when you dedicate yourself to building, testing, and refining every single day. Completed a full 100-day development sprint, rebuilding the app twice before delivering a polished third version. Released MemoLune in front of 500+ developers as a living example of how small daily progress can grow into something real. Demonstrated that the same memo-driven mindset that produced a best-selling book could also lead to a product shaping how people capture their thoughts. What we learned The greatest lesson: you don’t know what you truly want until you live with it. By forcing myself to use MemoLune every day, and by letting friends test it weekly, I uncovered countless “intuitive mismatches” and fixed them. This process taught me the value of iteration, and how daily discomforts can lead to breakthrough designs. What's next for MemoLune MemoLune’s journey is just beginning. Next steps include: RAG (Retrieval-Augmented Generation) for AI-powered memory recall. Automatic translation for seamless cross-language notes. High-accuracy OCR and speech recognition through external APIs, to supplement the built-in frameworks. Stronger multi-device sync, expanding across desktops and mobile. MemoLune began as a 100-day challenge, but it has grown into a vision: a lifelong companion for thoughts, memories, and creativity. P.S. About my background Before MemoLune, I published the best-selling book 「#100日チャレンジ」 (#100-Day Challenge). The story behind it is unusual: I originally dove into ChatGPT because I wanted to spend more time on video games and skip homework. My teacher noticed and said, “You’re too good at using generative AI”, and brought me to an academic conference. There, I reframed “skipping homework” as “optimizing software development”, and ended up receiving an award. That led me to attempt the #100-Day Challenge—building 100 apps in 100 days with AI—which became the foundation of my book. The book is built entirely from the countless memos I kept along the way, capturing my ups and downs. Today, that same spirit fuels MemoLune. From a “talent for skipping homework,” I have grown into someone who gives talks at universities, companies, and conferences both in Japan and abroad—with the same conviction: I succeeded only with the talent of skipping homework. <div