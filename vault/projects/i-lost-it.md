---
slug: "i-lost-it"
url: "https://devpost.com/software/i-lost-it"
title: "I LOST IT"
hackathon: "ConUHacks X"
organization: "HackConcordia"
winner: true
words: 594
team_size: 4
has_repo: true
has_live: true
has_video: false
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "mechanism/retrieval_grounding"
  - "mechanism/vision_ocr"
  - "domain/finance_payments"
  - "domain/supply_logistics"
  - "domain/transportation"
  - "substrate/structured_db"
  - "substrate/video_visual"
---

# I LOST IT

> 🚀 Ever lose something and realize “Lost & Found” is basically a black hole? ilostit fixes that. 📸 Snap it. 🔎 Search by text/photo. ⚡ Instant multimodal matches. 🔐 Get items back fast.

[Devpost](https://devpost.com/software/i-lost-it) · hackathon [[ConUHacks X]]

## Facets

**mechanism** [[realtime_stream]] [[retrieval_grounding]] [[vision_ocr]]
**domain** [[finance_payments]] [[supply_logistics]] [[transportation]]
**substrate** [[structured_db]] [[video_visual]]

**stack** clip, css, dinov2, fastapi, gemini, milvus, next.js, python, pytorch, react, shadcn/ui, supabase, tailwind, typescript

## How they structured the write-up

- inspiration
- what it does
- how we built it
- matching pipeline:
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for i lost it

## Body

Landing page Item management Inquiries management AI Item matching Inspiration Lost and found systems are broken. University campuses, gyms, and workplaces accumulate boxes of unclaimed items while their owners have no efficient way to search for them. Traditional lost and found relies on manual descriptions and visual scanning through cluttered bins—a process that's frustrating for users and time-consuming for staff. We asked ourselves: what if AI could match lost items to their owners using the same visual understanding that humans use, but faster and more reliably? What it does I LOST IT is an AI-powered lost and found platform that matches lost items using multimodal search. Users describe what they lost (with text, image, or both), and our system searches through a database of found items using four different AI matching approaches simultaneously: Image-to-Image: Visual similarity using DINOv2 (finds items that look alike) Image-to-Caption: Cross-modal matching using CLIP (matches your photo against AI-generated descriptions of found items) Text-to-Image: Reverse cross-modal matching (your description matched against item photos) Text-to-Text: Semantic similarity for detailed descriptions The system generates intelligent follow-up questions using Gemini to gather more details, then produces verification questions that only the true owner could answer—preventing fraudulent claims. Staff can manage inventory through an assistant portal, organizing items into collections by location. How we built it Backend (Python/FastAPI): Milvus vector database storing embeddings across 4 collections (DINOv2, CLIP image, CLIP caption, sentence embeddings) DINOv2 for self-supervised visual representations that capture fine-grained visual details CLIP for cross-modal understanding between images and text Sentence Transformers for semantic text matching Gemini 2.0 Flash for caption generation, OCR, and dynamic question generation Supabase for authentication, metadata storage, and image hosting Frontend (Next.js/React): Modern, mobile-first UI with Framer Motion animations Real-time inquiry tracking and match notifications Assistant portal for inventory management Matching Pipeline: Each search combines results from multiple embedding types with weighted scoring, filters by collection/location, and ranks potential matches. The weighted fusion approach ensures that both visual and textual signals contribute to finding the right item. Challenges we ran into Embedding dimension mismatches: Each model produces different embedding sizes (DINOv2: 768, CLIP: 768, Sentence Transformers: 384), requiring separate Milvus collections with proper indexing Cross-modal alignment: Getting CLIP to reliably match user descriptions to AI-generated captions required careful prompt engineering for the caption generation Score fusion: Balancing weights between different matching modalities to produce meaningful combined scores without one signal dominating Real-time performance: Optimizing the search pipeline to query 4 vector collections and merge results quickly Accomplishments that we're proud of Built a complete multimodal search pipeline that combines 4 different AI matching approaches Created an intelligent verification system that generates questions only the true owner could answer Designed a clean, intuitive UX that makes submitting lost item inquiries as easy as posting on social media Implemented a robust assistant workflow with collection management, match review, and fraud prevention What we learned Vector databases like Milvus are incredibly powerful for similarity search at scale Cross-modal embeddings (CLIP) enable fascinating search capabilities that weren't possible before Combining multiple embedding approaches with weighted fusion produces better results than any single model Gemini's structured output mode with Pydantic schemas makes building reliable AI features much easier What's next for I LOST IT Notification system: Alert users when new items matching their inquiry are added Mobile app: Native iOS/Android apps with camera integration for instant submissions Organization dashboard: Analytics for institutions to track lost and found patterns Federated search: Allow multiple locations (universities, transit, venues) to share a connected network Claim verification: Streamlined pickup flow with QR codes and identity verification <div