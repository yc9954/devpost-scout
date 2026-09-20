---
slug: "thread-ai-sti7ju"
url: "https://devpost.com/software/thread-ai-sti7ju"
title: "Thread.ai"
hackathon: "NextGenHacks"
organization: "NextGenHacks"
winner: true
words: 746
team_size: 1
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "mechanism/retrieval_grounding"
  - "mechanism/vision_ocr"
  - "mechanism/voice_speech"
  - "substrate/code_repository"
  - "substrate/document_pdf"
  - "substrate/structured_db"
  - "substrate/video_visual"
---

# Thread.ai

> Talk to AI face-to-face. Thread.ai transforms conversations into real-time avatar video interactions powered by RAG, vision, OCR, and multimodal intelligence.

[Devpost](https://devpost.com/software/thread-ai-sti7ju) · hackathon [[NextGenHacks]]

## Facets

**mechanism** [[realtime_stream]] [[retrieval_grounding]] [[vision_ocr]] [[voice_speech]]
**substrate** [[code_repository]] [[document_pdf]] [[structured_db]] [[video_visual]]

**stack** apis, coco-ssd, express.js, firebase, firestore, framermotion, gooey.ai, node.js, pdfjs-dist, pinecone, rag, react, rest, supabase

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what changed and upgraded
- what's next for thread.ai
- links

## Body

Inspiration Most AI tools today are fragmented. Chatbots handle text, computer vision systems process images separately, document AI lacks real-time interaction, and avatar platforms often operate independently from retrieval and reasoning systems. We wanted to build a unified multimodal AI platform where conversational AI, Retrieval-Augmented Generation (RAG), OCR, computer vision, and AI avatars work together in a single seamless experience. That vision inspired Thread.ai — a real-time multimodal AI interaction platform designed to bridge the gap between understanding, reasoning, and human-like communication. Project Resources Live Product: https://threadai-bharat-aws-genai.vercel.app/ GitHub Repository: https://github.com/viv2005ek/ThreadAi-RealTimeAiVideoCall Demo Video: https://youtu.be/ci9qdkgSVss Technical Documentation: https://docs.google.com/document/d/1Uqi4W7bhbHs56ksUohuj69Ux1aw64ah1xIvUzm2ykf0/edit?usp=sharing What it does Thread.ai is a real-time multimodal AI interaction platform that combines multiple AI capabilities into a single intelligent workflow. The platform integrates: Conversational AI Retrieval-Augmented Generation (RAG) PDF Intelligence OCR (Optical Character Recognition) Computer Vision & Object Detection AI-Generated Lip-Synced Avatars Persistent Chat Storage & Context Memory Users can upload PDFs and interact with document-grounded AI through a Retrieval-Augmented Generation pipeline. Images can be analyzed using OCR and TensorFlow-powered object detection, enabling visual understanding alongside textual reasoning. Instead of receiving traditional text-only responses, users can interact with AI-generated talking avatars that deliver responses through synchronized speech and lip movement. The result is a richer and more immersive AI experience that combines understanding, retrieval, reasoning, and communication. How we built it Frontend Built using: React TypeScript Vite TailwindCSS Framer Motion The frontend handles: Real-time chat interactions Avatar rendering Conversation management Multi-session workflows Dashboard and authentication experiences AI & Knowledge Layer We integrated: Pinecone Vector Database PDF Parsing (pdfjs-dist) OCR using Tesseract.js TensorFlow.js COCO-SSD Object Detection The platform uses a Retrieval-Augmented Generation pipeline where: PDFs are uploaded and parsed Content is converted into embeddings Embeddings are stored in Pinecone Relevant chunks are retrieved during conversations Retrieved context is injected into AI responses This enables document-grounded reasoning instead of relying solely on model memory. Backend Infrastructure Built using: Node.js Express.js Firebase Authentication Firestore Database The backend handles: Authentication Conversation persistence AI orchestration Secure API handling Avatar generation workflows Avatar Generation Pipeline We integrated: Gooey.ai Text-to-Speech Generation Lip-Sync Video Rendering The avatar workflow is: Text Response → Speech Generation → Gooey.ai Lip Sync → AI Avatar Video Response This allows Thread.ai to communicate through realistic AI-generated talking avatars. Challenges we ran into The most difficult challenge was orchestrating multiple AI systems together in real time. Some of the major challenges included: Latency optimization across OCR, RAG, vision processing, and avatar generation Maintaining contextual consistency between multimodal inputs Synchronizing AI-generated speech with lip-synced video output Designing a smooth real-time interaction workflow Managing retrieval quality from uploaded documents Coordinating multiple asynchronous AI pipelines Combining retrieval, vision, OCR, and avatar generation into a single user experience required significant architectural iteration and optimization. Accomplishments that we're proud of Successfully integrated multiple AI modalities into a single platform Built a working real-time multimodal AI interaction system Implemented a complete Retrieval-Augmented Generation pipeline using Pinecone Enabled document-grounded conversations through PDF intelligence Integrated OCR and object detection into conversational workflows Built AI-generated lip-synced avatar responses Created a scalable modular architecture rather than a simple AI wrapper Developed a complete end-to-end multimodal workflow from input to avatar response We are especially proud that Thread.ai feels like a true AI interaction platform rather than a traditional chatbot demo. What we learned Building Thread.ai reinforced an important lesson: Modern AI products are orchestration systems, not simply model integrations. Throughout development, we gained experience with: Multimodal AI architectures Vector databases and semantic retrieval Retrieval-Augmented Generation systems OCR and computer vision workflows AI pipeline orchestration Frontend-backend synchronization Real-time interaction systems AI latency optimization Scalable GenAI application design Most importantly, we learned how multiple AI modalities can work together to create more natural, useful, and human-centered experiences. What Changed and Upgraded Now Its video quality and audio quality is enhanced. Its voice recoginition ability also upgraded. Rag doing its job but Gemini Reasoning model also validate the response is correct. Guardrails are getting used to protect mcp and Rag store documents. What's next for Thread.ai We see Thread.ai as the foundation for next-generation multimodal AI assistants. Future plans include: Real-time streaming LLM responses WebRTC-powered low-latency communication Autonomous AI agents Long-term multimodal memory systems Enterprise knowledge assistant capabilities Edge AI deployment Multi-avatar collaboration Production-ready containerized infrastructure Advanced multimodal reasoning pipelines Our long-term vision is to evolve Thread.ai into a scalable framework for intelligent multimodal assistants, AI personas, and real-time AI collaboration systems. Links Live Product: https://threadai-bharat-aws-genai.vercel.app/ GitHub Repository: https://github.com/viv2005ek/ThreadAi-RealTimeAiVideoCall Demo Video: https://youtu.be/ci9qdkgSVss Technical Documentation: https://docs.google.com/document/d/1Uqi4W7bhbHs56ksUohuj69Ux1aw64ah1xIvUzm2ykf0/edit?usp=sharing <div