---
slug: "refugee-legal-navigator"
url: "https://devpost.com/software/refugee-legal-navigator"
title: "Refugee Legal Navigator"
hackathon: "Amazon Nova AI Hackathon"
organization: "Amazon"
winner: true
words: 828
team_size: 1
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/retrieval_grounding"
  - "domain/education"
  - "domain/immigration_refugee"
  - "domain/legal_justice"
  - "domain/media_journalism"
  - "user/legal_professional"
  - "substrate/document_pdf"
  - "substrate/geospatial"
  - "substrate/regulation_legal_text"
---

# Refugee Legal Navigator

> Empowering the displaced with Amazon Nova-driven legal aid, 22+ language support, and agentic UI automation to navigate complex asylum paths with compassion and precision.

[Devpost](https://devpost.com/software/refugee-legal-navigator) · hackathon [[Amazon Nova AI Hackathon]]

## Facets

**mechanism** [[retrieval_grounding]]
**domain** [[education]] [[immigration_refugee]] [[legal_justice]] [[media_journalism]]
**user** [[legal_professional]]
**substrate** [[document_pdf]] [[geospatial]] [[regulation_legal_text]]

**stack** 19, act, amazon, amazon-web-services, api, bedrock, css, embeddings, fastapi, framer, javascript, mediarecorder, motion, nova

## How they structured the write-up

- 🌟 inspiration
- 🧠 what it does
- ✨ the magic moment
- 🎨 architecture diagram
- 🏗 how it was built
- 🚧 challenges we solved
- 🏆 accomplishments we're proud of
- 📊 impact potential
- 🔮 what's next
- 🧠 what we learned
- ❤️ why this matters

## Body

🌟 Inspiration A mother fleeing violence arrives at the border with her two children. She doesn't speak English. She doesn't understand asylum law. Here's what the data says: Detained asylum seekers with legal representation are five times more likely to win their cases. Yet most face the system alone. Every year, hundreds of thousands navigate complex refugee law without representation. They lose not because their cases lack merit — but because they lack access to clear, understandable guidance in their own language. Refugee Legal Navigator was built to close that gap. 🧠 What It Does Refugee Legal Navigator is the first AI-powered legal assistant that combines native multilingual support with voice interaction, grounded entirely in real, retrievable asylum law. Our architecture orchestrates four Amazon AI services: Service Role Amazon Nova Lite Conversational reasoning engine Amazon Nova Act Automated workflow execution Amazon Nova Sonic Voice input/output for low-literacy users Amazon Titan Embeddings Semantic search across legal documents Together, they power a fully grounded RAG pipeline that delivers jurisdiction-specific asylum guidance — not generic chatbot responses. ✨ The Magic Moment A user asks in Arabic from a crowded refugee camp, using a borrowed smartphone: "هل يمكنني التقدم بطلب لجوء إذا دخلت بدون تأشيرة?" ("Can I apply for asylum if I entered without a visa?") The system understands the fear, not just the words. It retrieves the exact U.S. asylum statute, grounds the answer in real law, and responds clearly in Arabic: "Yes. Entering without a visa does not automatically bar you. But you must prove a well-founded fear of persecution. Here is what that means and what you need to do next." This isn't translation. It's access. 🎨 Architecture Diagram System Flow graph TD User([User]) <--> Frontend[React Frontend - Vite] subgraph "Backend Layer (FastAPI)" Frontend <--> API[API Endpoints: /chat, /track-case, /health] API <--> RAG[RAG Pipeline] API <--> CaseTracker[Case Tracker Agent] end subgraph "AI & Data Layer (AWS Bedrock)" RAG <--> NovaLite[Amazon Nova Lite - Chat LLM] RAG <--> TitanEmbed[Amazon Titan Embeddings - Vector RAG] CaseTracker <--> NovaAct[Amazon Nova Act - Browser Automation] API <--> NovaSonic[Amazon Nova Sonic - TTS Voice] TitanEmbed <--> LocalCache[(Local Vector Cache)] end subgraph "External Resources" NovaAct <--> USCIS[[USCIS Portal]] TitanEmbed <--> LegalDocs[(Legal Corpus - Asylum Law)] end Visual Architecture Architecture Diagram : 🏗 How It Was Built Retrieval-Augmented Generation (RAG) Legal documents are chunked and embedded using Titan Embeddings. Semantic retrieval selects the most relevant sources. Responses are generated strictly using retrieved legal context. Disk caching prevents expensive re-embedding on restart. Result: Substantive, citation-grounded answers instead of AI hallucinations. Production-Grade Cloud Engineering Deployed on AWS App Runner with a hardened startup architecture: Asynchronous RAG initialization passes health checks instantly Lazy initialization patterns prevent credential crashes Correct FastAPI route ordering prevents silent shadowing After 15+ deployment iterations , the system is stable, resilient, and serving real responses in production. This is not a demo — it's a live system engineered for reliability. 🚧 Challenges We Solved Challenge Solution Startup Latency Background loading pattern allows immediate health check success while embeddings load asynchronously Credential Timing Refactored module-level clients to factory-based lazy initialization Route Shadowing Reordered FastAPI routes to prevent catch-all SPA routes from blocking API endpoints Dependency Loss Installed packages directly into copied directory to survive multi-stage Docker build Each problem strengthened production readiness. 🏆 Accomplishments We're Proud Of ✅ Fully deployed on AWS App Runner ✅ Four Amazon AI services orchestrated in one cohesive system ✅ Multilingual, voice-enabled legal assistant with real legal grounding ✅ Asynchronous cloud-safe architecture with disk-cached embeddings Most importantly: ✅ Making asylum law understandable to people who need it most 📊 Impact Potential Over 1 million asylum applications are filed globally each year. Most lack representation. Language barriers reduce success rates. Refugee Legal Navigator: 📈 Increases access to understandable legal information 🚫 Reduces misinformation from unreliable sources 💪 Helps applicants prepare more confidently for interviews 🌍 Scales globally at near-zero marginal cost Technology cannot replace attorneys — but it can dramatically improve access to legal understanding. 🔮 What's Next Priority Initiative 🌍 Multi-country legal expansion – EU, UK, Canada, Australia 🤝 Legal aid integration – Direct referrals to pro bono immigration organizations 📝 Document preparation assistant – Guided workflows for asylum forms and evidence 📱 Offline mode – Deployable versions for refugee camps with limited connectivity 🧠 What We Learned Managed cloud platforms require deeper runtime awareness than expected Lazy initialization is essential for credential-safe AI systems RAG caching transforms usability from "minutes" to "instant" Multilingual support must be native, not an afterthought The most powerful AI systems are those grounded in real-world truth. ❤️ Why This Matters Refugees don't need another chatbot. They need clarity. They need language access. They need grounded, accurate information about laws that shape their future. Refugee Legal Navigator transforms cutting-edge AI into a tool for dignity, access, and justice. Refugee Legal Navigator is live on AWS App Runner today. It works. It helps. With your support, it scales from a powerful prototype to a global lifeline. <div