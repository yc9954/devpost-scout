---
slug: "jackqr"
url: "https://devpost.com/software/jackqr"
title: "jackqr"
hackathon: "Arm AI Developer Challenge "
organization: "arm"
winner: true
words: 730
team_size: 1
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/on_device_local"
  - "mechanism/vision_ocr"
  - "domain/education"
  - "user/educator_student"
  - "substrate/document_pdf"
  - "substrate/video_visual"
---

# jackqr

> studying enhanced with on device ai

[Devpost](https://devpost.com/software/jackqr) · hackathon [[Arm AI Developer Challenge]]

## Facets

**mechanism** [[on_device_local]] [[vision_ocr]]
**domain** [[education]]
**user** [[educator_student]]
**substrate** [[document_pdf]] [[video_visual]]
  <sub>weak: structured_db, web_dom</sub>

**stack** gemma, swift

## Body

Inspiration In Nigeria, most university students can't afford textbooks. The reality is harsh: a single textbook can cost more than a month's allowance. So we do what we've always done—we share PDFs. Scanned lecture notes, photographed textbook pages, downloaded materials passed around on WhatsApp groups. But these PDFs are often terrible. Poorly scanned, badly formatted, 200+ pages of dense text with no structure. Reading them on a phone (which is what most of us have) is exhausting. And when exam season hits, you're stuck scrolling through endless pages trying to find that one definition you need. On top of that, internet data is expensive and unreliable. You can't always count on cloud-based AI tools when your data runs out mid-study session or the network just decides to stop working. We built jackqr because we needed it ourselves. What it does jackqr transforms chaotic study materials into something actually usable—completely offline. Document Processing: Import PDFs or images of textbook pages On-device OCR extracts text from even poorly scanned documents Intelligent chunking breaks content into digestible sections AI-powered simplification rewrites complex passages while preserving core concepts Smart Reading: Clean, formatted text that's easy to read on any screen Navigate through content in logical chunks instead of endless scrolling Simplify difficult sections on-demand with a single tap Flashcard System with AI Grading: Create flashcard decks from your study materials Import existing flashcards via CSV/JSON SM-2 spaced repetition algorithm optimizes review timing: I(n)=I(n−1)×EF where I(n) is the interval after n reviews and EF is the easiness factor On-device AI grades your answers, understanding context and semantic meaning—not just exact string matches Track your progress and focus on what you actually need to review Everything runs locally. No internet required after initial setup. How we built it Tech Stack: Swift/SwiftUI for native iOS performance SwiftData for local persistence Vision framework for OCR Google's Gemma3 models (2B and 4B variants) running on-device via LiteRT Architecture: TextExtractor handles OCR from PDFs and images TextChunker intelligently segments content at natural boundaries TextSimplifier uses the on-device LLM to rewrite complex text FlashcardGrader evaluates user answers using AI with fallback to string similarity The Grading System: We optimized the LLM prompt to return simple YES/NO/PARTIAL responses rather than complex JSON, dramatically improving reliability on smaller models. The grading considers semantic equivalence—so "H₂O" and "water" are recognized as the same concept. Challenges we ran into Model Performance: Small on-device models aren't GPT-4. Getting reliable, consistent responses from Gemma3 1B required extensive prompt engineering. the 2B and 4B variants were much smarter and easier to work with, but require higher RAM capacities of at least 6gb. the 1B variant needed only 4 gigs. Empty Responses: The model would occasionally return nothing. We implemented a multi-layer fallback: AI grading → string similarity with semantic bonuses → conservative default scoring. Memory Constraints: Running an LLM on a phone while also doing OCR and managing a document library required careful resource management. We create fresh inference sessions rather than caching to avoid memory overflow. Model Downloads: HuggingFace URLs and model filenames kept changing. We had to track down the correct repositories and implement proper error handling for download failures. Accomplishments that we're proud of True offline functionality: Once the model is downloaded, everything works without internet AI grading that actually works: The system understands that "mitochondria is the powerhouse of the cell" and "the mitochondria produces ATP energy for cells" mean the same thing Clean UX from chaos: Taking a blurry photo of a textbook page and turning it into readable, navigable content Accessibility: Making AI-powered study tools available to students who can't afford subscriptions or reliable internet What we learned On-device AI is ready for real applications, but you have to design around its limitations Simpler prompts beat complex ones for small models Fallback systems aren't just nice-to-have—they're essential The best features come from solving your own problems What's next for jackqr Android version: Most Nigerian students use Android Collaborative decks: Share flashcard decks with classmates offline via AirDrop/Bluetooth Auto-generated flashcards: Use the LLM to automatically create Q&A pairs from document content Voice input: Answer flashcards by speaking, graded by AI Multi-language support: Hausa, Yoruba, Igbo, Pidgin—because not everyone thinks in English We're not trying to replace textbooks or teachers. We're just trying to make studying a little less painful for students who are already doing everything they can with what they have. <div