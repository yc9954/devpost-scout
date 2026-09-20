---
slug: "aesthetica"
url: "https://devpost.com/software/aesthetica"
title: "aesthetica"
hackathon: "TreeHacks 2026"
organization: "TreeHacks"
winner: true
words: 655
team_size: 4
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "mechanism/retrieval_grounding"
  - "mechanism/vision_ocr"
  - "domain/retail_commerce"
  - "substrate/geospatial"
  - "substrate/structured_db"
  - "substrate/video_visual"
---

# aesthetica

> the 1st spatial fashion system. w 1 gesture on meta glasses, u turn any outfit u c into aesthetic data, matched products, a taste profile that evolves w u u see it u like it u want it u got it.

[Devpost](https://devpost.com/software/aesthetica) · hackathon [[TreeHacks 2026]]

## Facets

**mechanism** [[realtime_stream]] [[retrieval_grounding]] [[vision_ocr]]
**domain** [[retail_commerce]]
**substrate** [[geospatial]] [[structured_db]] [[video_visual]]

**stack** fastapi/uvicorn/websockets, next.js/react, postgresql-(supabase)-+-sqlalchemy/alembic, python, redis/celery, tailwind/radix-ui, tensorflow.js-(bodypix-+-movenet-pose), typescript

## How they structured the write-up

- what aesthetica does
- 1. spatial capture layer
- 2. garment & body mapping (computer vision stack)
- 3. catalog engine
- 4. structured taste graph
- 5. persistent taste engine

## Body

GIF Imagine this. You’re walking down the street and someone passes you wearing your exact ideal blazer. The cut, the drape, the color temperature, the silhouette against the light. It’s perfect. By the time you pull out your phone, unlock it, open the camera, and awkwardly try to capture the outfit without being obvious… they’re gone. Even if you get the photo: Reverse image search takes minutes. Results are noisy and generic. You forget why you liked it. The moment doesn’t compound. Inspiration disappears. Taste doesn’t accumulate. We built Aesthetica to fix that. What Aesthetica Does Aesthetica is spatial fashion intelligence for the real world. With a single gesture while wearing Meta Ray-Ban glasses, users capture any outfit they see. We're also fully integrated with Poke, the best conversational assistant one could have. Within five seconds, Poke pings you on iMessages, "saw you liked that outfit. here's what we found." The system isolates garments in the live camera feed. It extracts structured, multi-attribute embeddings. It performs reverse visual retrieval across product databases. It updates a persistent, interpretable taste graph with a fully unique, fully comparable Fashion Identity. This is not just visual search. It is a continuously learning taste engine. Technical Architecture Aesthetica consists of five core layers: 1. Spatial Capture Layer Using Meta Ray-Ban camera input and gesture triggers, we capture short-frame sequences aligned with user gaze. We perform: Real-time object detection Garment segmentation Human pose estimation for body-part localization This allows us to isolate: Tops Bottoms Outerwear Footwear Accessories and anchor them relative to body geometry. 2. Garment & Body Mapping (Computer Vision Stack) We use CV models to: Segment garments from background Map clothing to anatomical regions Extract silhouette contours Estimate drape and structure features Identify layering relationships We compute structured features including: Silhouette type (structured, relaxed, oversized, tapered) Color palette distributions (dominant + secondary tones) Texture embeddings (wool, satin-like, denim-like, etc.) Pattern detection (solid, plaid, striped, etc.) Formality classification Gender-neutral style archetypes Rather than storing a single opaque embedding vector, we decompose each capture into interpretable attribute nodes. 3. Catalog Engine You upload any photo (outfit, garment, or inspiration). The pipeline: Runs OpenAI-based style analysis on the image (garment name, five style scores, and a short description) Uses OpenAI to generate a shopping query and rationale from that style signal Searches the open web via SerpAPI (e.g. Google Shopping) with the query You get visually similar, purchasable items plus a Poke notification with a link and short opener. 4. Structured Taste Graph This is the core innovation. Instead of just saving products, we maintain a dynamic user-specific style graph. Over time, the system learns: What you consistently notice What you ignore How your taste drifts seasonally Which attributes correlate Your aesthetic identity becomes computationally modeled. 5. Persistent Taste Engine Most fashion AI tools answer: “What is this?” Aesthetica answers: “What does this say about you?” We build: A persistent style embedding A continuously updated attribute distribution A style trajectory over time An interpretable preference surface The more you capture, the more accurate the system becomes. Taste compounds. What We Built for This Hackathon Gesture-triggered capture pipeline Real-time garment segmentation and body mapping Multi-attribute embedding extraction Vector-based reverse image retrieval Structured style graph engine Real-time product surfacing UI Under-five-second end-to-end flow Challenges Segmenting garments in uncontrolled, in-the-wild lighting Handling occlusion and motion blur Building an interpretable preference model instead of a black-box vector Balancing retrieval accuracy with low latency Designing a graph update rule that meaningfully reflects aesthetic evolution The hardest problem was not visual search. It was modeling identity. The Bigger Vision As spatial computing becomes ambient, commerce must become ambient. When cameras are always available and gestures replace screens, discovery should be frictionless. Aesthetica is building the infrastructure layer for spatial commerce: Real-world capture Structured aesthetic modeling Persistent taste intelligence Instant conversion to commerce Fashion isn’t just what you buy. It’s what you notice. And now, noticing is enough. <div