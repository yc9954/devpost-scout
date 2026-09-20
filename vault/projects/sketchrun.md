---
slug: "sketchrun"
url: "https://devpost.com/software/sketchrun"
title: "Sketchrun"
hackathon: "Cloud Run Hackathon"
organization: "Google"
winner: true
words: 1290
team_size: 1
has_repo: false
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/benchmark_measured"
  - "mechanism/realtime_stream"
  - "mechanism/vision_ocr"
  - "domain/accessibility"
  - "domain/developer_tools"
  - "domain/immigration_refugee"
  - "domain/transportation"
  - "user/developer"
  - "user/government_staff"
  - "substrate/geospatial"
  - "substrate/structured_db"
  - "substrate/video_visual"
  - "substrate/web_dom"
---

# Sketchrun

> Transform wireframe sketches into production-ready Next.js code in seconds using GPU-accelerated AI and fine-tuned Gemma models.

[Devpost](https://devpost.com/software/sketchrun) · hackathon [[Cloud Run Hackathon]]

## Facets

**mechanism** [[benchmark_measured]] [[realtime_stream]] [[vision_ocr]]
**domain** [[accessibility]] [[developer_tools]] [[immigration_refugee]] [[transportation]]
**user** [[developer]] [[government_staff]]
**substrate** [[geospatial]] [[structured_db]] [[video_visual]] [[web_dom]]

**stack** clerk, e2b, firebase-genkit, gemini-ai, gemma, google-cloud, google-cloud-run, google-cloud-sql, google-cloud-vision, google-cloud-vision-api, huggingface, indexeddb, nextjs, nvidia-l4-gpu

## How they structured the write-up

- inspiration
- what it does
- how i built it
- challenges i ran into
- accomplishments that i'm proud of
- what i learned
- what's next for sketchrun

## Body

Inspiration As a developer, I've always been frustrated by the gap between design and development. Designers create beautiful mockups in Figma, but translating them to code takes hours of manual work. I wanted to democratize web development by allowing anyone, from founders sketching on napkins to designers wireframing on tablets, to instantly see their ideas come to life as production-ready code . When I learned about the Cloud Run GPU Hackathon, I saw the perfect opportunity to build practical developer tools. The availability of NVIDIA L4 GPUs on Cloud Run meant I could deploy a finely tuned solution that makes real-time design-to-code generation actually feasible. What It Does SketchRun is an AI-enabled platform that converts hand-drawn UI wireframes into production-ready Next.js applications: Style Extraction Upload 1-3 reference images (existing websites, mockups, or design inspiration) Gemini 2.5 Pro analyzes them using GPU-accelerated vision models Extracts a comprehensive style guide: Color palette (6 hex codes: primary, secondary, accent, neutral, background, text) Typography (font families, sizes, weights, line heights) Border styles (width, radius, colors) Shadows (box-shadow, text-shadow) Design aesthetic (Neobrutalism, Glassmorphism, Minimalist, Material, Corporate) Sketch Analysis Upload your hand-drawn wireframe (photo, scan, or digital sketch) Gemini 2.5 Pro + Cloud Vision analyze the layout: Component detection : buttons, forms, cards, headers, navigation Layout structure : grid, flexbox, absolute positioning Text content : OCR extraction via Cloud Vision API Spatial hierarchy : understands which elements are grouped, nested, or separate GPU-Accelerated Code Generation My fine-tuned Gemma 2-9B-IT model (trained on design-to-code examples) generates: Complete Next.js 16 component with App Router Tailwind CSS utility classes with exact hex colors from style guide shadcn/ui components for consistency Lucide React icons Responsive design with mobile-first breakpoints Accessible HTML with semantic markup and ARIA labels Live Preview Code is deployed to an E2B sandboxed environment Runs a real Next.js dev server with Hot Module Replacement Returns a live URL: https://{sandbox-id}.e2b.dev Preview updates in real-time as you modify code Production-Ready Output The generated code is production-ready: Clean, modular React components Responsive across all devices Accessible to screen readers How I Built It Architecture I built SketchRun as a full-stack serverless application using 100% Google Cloud services: Frontend (Next.js on Cloud Run) Next.js 16 with React 18 and App Router Tailwind CSS for styling shadcn/ui component library Clerk for authentication Zustand + IndexedDB for canvas state management (solving localStorage quota issues) Prisma ORM for database access Deployed as a Cloud Run Service (auto-scaling, no GPU needed) Backend (FastAPI on Cloud Run with NVIDIA L4 GPU) FastAPI (Python 3.13) for API server NVIDIA L4 GPU in europe-west4 region Gemini 2.5 Pro via Vertex AI for vision analysis Gemma 2-9B-IT fine-tuned on design-to-code datasets: Design2Code (484 real webpages, Stanford SALT Lab) Pix2Code (1,750+ GUI screenshots) WebSight (500K+ website screenshots) Cloud Vision API for OCR text extraction E2B Code Interpreter for sandboxed Next.js previews Deployed as a Cloud Run Service with GPU support Data Layer Cloud Storage (GCS) for images and generated code Cloud SQL (PostgreSQL) for projects, users, style guides, code versions Prisma for type-safe database operations with cascade deletes AI/ML Pipeline Reference Images → Gemini 2.5 Pro (GPU) → Style Guide ↓ Sketch Image → Gemini 2.5 Pro (GPU) → Layout Analysis ↓ Style Guide + Layout → Gemma 2-9B-IT (GPU) → Next.js Code ↓ Generated Code → E2B Sandbox → Live Preview URL Fine-tuning Gemma 2-9B-IT The core innovation is my fine-tuned Gemma model for sketch-to-code: Base Model : google/gemma-2-9b-it (instruction-tuned variant) Training Data (500K+ examples): Design2Code: Real-world webpages with screenshots + React code Pix2Code: GUI screenshots + DSL code for web/iOS/Android WebSight: Massive dataset of website screenshots + HTML/CSS Training Setup : Hardware: NVIDIA L4 GPU on Cloud Run Optimization: LoRA (Low-Rank Adaptation) for efficient fine-tuning Epochs: 3 Batch Size: 8 Learning Rate: 2e-5 Task: Multi-modal vision-to-code generation Why Gemma? : 10x faster inference than Gemini (9B vs 1.5T parameters) 3x cheaper at scale ($5 vs $15 per 1K requests) Specialized for sketch-to-code task Open-source and fully customizable Key Technical Innovations 1. Style Transfer Most sketch-to-code tools try to recreate the exact sketch appearance. I realized sketches are wireframes —they show structure, not style_ My approach us to: Extract polished aesthetics from reference images Extract layout structure from sketch And combine them to create professional UIs 2. GPU Optimization for Real-Time Generation Lazy loading: Models load on first request (not at startup) Structured output: Schema validation ensures valid JSON responses Retry logic: Exponential backoff for rate limit handling Parallel processing: Multiple images analyzed simultaneously 3. E2B Custom Template I created a custom E2B template ( sketchrun-nextjs ) with: Next.js 16 + Turbopack pre-installed Tailwind CSS configured All shadcn/ui components pre-installed Lucide React icons ready 4. IndexedDB for Canvas Storage Solved the localStorage quota problem (5-10MB) by switching to IndexedDB (50MB-1GB): Users can create complex sketches with hundreds of shapes 50-entry history for undo/redo No more "quota exceeded" errors Challenges I Ran Into 1. E2B Sandbox Startup Delays Problem : Initial E2B sandbox creation took 3-5 minutes because Next.js needed to install dependencies and compile with Turbopack on every run. Solution : Created a custom E2B template with all dependencies pre-installed: Reduced startup from 3-5 minutes to 10-15 seconds Pre-installed Next.js 16, Tailwind, shadcn/ui, Lucide icons Dockerfile optimization to minimize image size 2. Canvas Storage Quota Exceeded Problem : Users hit localStorage quota (5-10MB) after drawing 50-100 shapes with undo/redo history. Solution : Migrated to IndexedDB using idb-keyval : 50MB-1GB quota (10-100x larger) Limited history to 50 entries (trimmed automatically) Async persistence doesn't block UI 3. GPU Cold Start Times Problem : First request to GPU service took 60-90 seconds to load the Gemma model into VRAM. Solution : Implemented lazy loading : Server starts immediately (no model loading at startup) Model loads on first request (user sees loading indicator) Subsequent requests are instant (model stays in VRAM) Fallback to Gemini if GPU unavailable 4. Structured Output Schema Validation Problem : Gemini sometimes returned invalid JSON with missing fields or wrong types. Solution : Used Firebase Genkit with response_schema : Defined JSON schema for style guide output Gemini now guarantees valid structure Reduced parsing errors from ~10% to <1% Accomplishments That I'm Proud Of Technical Achievements Fine-tuned Gemma 2-9B-IT on 500K+ examples First time working with model fine-tuning at this scale Achieved 3-5x faster inference than Gemini Specialized model for sketch-to-code task 100% Serverless on Google Cloud Auto-scaling from 0 to N instances No server management Pay only for actual usage Production-Ready Code Output Not just prototypes—actual deployable Next.js apps Responsive, accessible, modern best practices Users can deploy directly to Vercel/Netlify What I Learned Technical Learnings GPU Acceleration Is a Game-Changer 3-5x faster inference enables entirely new UX patterns Real-time AI becomes possible at scale But cold starts and memory management are critical Fine-Tuning > Prompt Engineering for Specialized Tasks Gemma 2-9B-IT (fine-tuned) beats Gemini 2.5 Pro (prompted) for sketch-to-code Smaller models can outperform larger ones when specialized Trade-off: upfront training cost vs long-term inference savings Serverless + GPU = Perfect Match Scale to zero when not in use (huge cost savings) Burst to handle traffic spikes No infrastructure management Structured Output Is Essential for Production AI Schema validation reduces errors dramatically Easier to parse and validate Modern LLMs support it natively What's Next for SketchRun Enhanced Gemma Fine-Tuning Train on specialized design systems (Material Design, Ant Design) Improve component recognition accuracy Add support for dark mode generation Multi-Page Application Generation Generate entire sites from multiple sketches Automatic routing and navigation Shared components across pages Code Iteration via Chat "Make the button bigger" "Change color scheme to dark mode" "Add a pricing section below hero" Powered by Gemini with code editing capabilities Component Library Build reusable library from generated code Version control with git-style diffs Share components across projects <div