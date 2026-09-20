---
slug: "forge-2qn7rt"
url: "https://devpost.com/software/forge-2qn7rt"
title: "Forge"
hackathon: "Cloud Run Hackathon"
organization: "Google"
winner: true
words: 759
team_size: 1
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/deterministic_policy"
  - "mechanism/realtime_stream"
  - "domain/developer_tools"
  - "user/general_public"
  - "substrate/code_repository"
  - "substrate/financial_record"
  - "substrate/geospatial"
  - "substrate/structured_db"
  - "substrate/video_visual"
  - "substrate/web_dom"
---

# Forge

> Text-to-3D on Cloud Run (GPU)

[Devpost](https://devpost.com/software/forge-2qn7rt) · hackathon [[Cloud Run Hackathon]]

## Facets

**mechanism** [[deterministic_policy]] [[realtime_stream]]
**domain** [[developer_tools]]
**user** [[general_public]]
**substrate** [[code_repository]] [[financial_record]] [[geospatial]] [[structured_db]] [[video_visual]] [[web_dom]]

**stack** cloud-build, cloud-run-(gpu-and-standard), cloud-storage, fastapi, gemini, imagen, imagen-3, nextjs

## How they structured the write-up

- inspiration
- what it does
- how we built it (gpu category)
- challenges we ran into
- accomplishments we’re proud of
- what we learned
- what’s next
- how this meets the judging criteria

## Body

Key Features Banner Architecture - Check GitHub for better quality Forge Master — Text-to-3D on Cloud Run (GPU) Elevator pitch. Forge Master turns short text prompts into production-ready 3D assets—generated, assessed, and delivered in under two minutes. It’s a fully serverless, Cloud Run–native app that uses an L4 GPU to run an open-source 3D pipeline end-to-end, with Google AI for image synthesis and quality analysis. Try it: Live demo at the public frontend and a clean, documented repo with deployment scripts and architecture notes. Inspiration Creating usable 3D assets is still slow and expensive. We wanted a one-click web app that produces game-ready meshes quickly, repeatably, and at a known unit cost—without managing clusters. Cloud Run with GPUs made that feasible for a weekend build, and the Google AI ecosystem closed the quality gap. What it does Type a prompt, get a 3D model you can inspect and download as GLB, OBJ, FBX, or STL. Forge Master: Generates a studio-lit reference image from your prompt Produces multi-view renders and reconstructs a watertight mesh Scores quality automatically and, if needed, iterates for improvements Serves an in-browser 3D viewer and one-click downloads Typical runtime: ~90 seconds. Success rate >95%. Average quality score 8.2/10. How we built it (GPU Category) Three services on Cloud Run with clear contracts and defense-in-depth: Frontend (Next.js + React Three Fiber) Public UI, real-time progress, interactive viewer, multi-format download buttons. Agent Service (FastAPI + Gemini) A four-agent pipeline: prompt enhancement, generation coordination, quality assurance, and iterative improvement. Handles retries, structured results, and logging. Public endpoint consumed only by the frontend. GPU Service (FastAPI on L4 GPU, europe-west1) Text→image via Imagen 4 , image→multi-view via Zero123++ , multi-view→mesh via LRM , followed by mesh post-processing (smoothing, component isolation, scaling) and multi-format export. Uploads artifacts to Cloud Storage and returns signed URLs. Security and cost control GPU service is IAM-protected ; only the agent service can invoke it (403 to the public). Frontend and agent are public; the most expensive path is never directly reachable. Fixed, observable cost per model (~$0.56) with clear breakdown (GPU time dominates). Why Google Cloud Cloud Run (GPU) : deploy a full PyTorch + Diffusers stack on L4 with autoscaling and zero-to-N behavior—no cluster admin. Imagen 4 and Gemini : higher-quality inputs and consistent QA, accessed via a single credentials model. Cloud Storage : durable, CDN-friendly artifact hosting with straightforward CORS and lifecycle policies. Cloud Build : push-button CI/CD for three services. Challenges we ran into End-to-end latency: minimized by keeping images small but sufficient for reconstruction, and by reducing post-processing passes. Model stability on L4: tuned mixed precision and batch sizes; added health checks and timeouts to avoid stuck reconstructions. Public abuse vs. usability: solved with Cloud Run IAM—agent can call GPU, browsers cannot. Accomplishments we’re proud of A clean three-tier architecture that scales from hackathon to production without rewrites. A full open-source 3D pipeline (InstantMesh) running reliably on Cloud Run GPU. A measurable quality system: per-model stats, scoring, and targeted re-generation when scores fall short. What we learned Cloud Run GPUs are practical for on-demand inference when you bound the workload and secure the hot path. Quality is a system property: prompt design (Gemini) + reference image (Imagen) + mesh post-processing matter as much as the core 3D model. IAM is the simplest and most effective line of defense for cost control in public AI apps. What’s next Batch jobs for bulk asset generation and dataset creation (Cloud Run Jobs). Optional texture baking and PBR maps. Project workspaces, history, and fine-grained rate limits. Veo/animated asset experiments for simple motion previews. How this meets the judging criteria Technical Implementation (40%) Well-executed, documented codebase: three independently deployable services, FastAPI type-validated endpoints, structured logs, and health checks. Core Cloud Run concepts: service-to-service auth via IAM, GPU service isolation, autoscaling, zero-to-idle, and CI/CD via Cloud Build. Production signals: error handling, bounded timeouts, QA scoring, iterative retries, and deterministic cost per request. UX: responsive Next.js frontend, progress states, and an integrated 3D viewer. Demo & Presentation (40%) Clear problem statement: fast, affordable, serverless 3D generation. Effective walkthrough: prompt → image → multi-view → mesh → download, with a quality badge. Architecture diagram and docs: included in the repo with deployment guides and service READMEs. Live link: public demo to test real prompts and download results. Innovation & Creativity (20%) Novel combination: serverless GPU reconstruction paired with Google Imagen and Gemini for higher-quality inputs and automated QA. Impact: compresses a traditionally manual pipeline into a single web flow with predictable cost, enabling indie games, prototyping, and education. <div