---
slug: "insightforge-ai"
url: "https://devpost.com/software/insightforge-ai"
title: "InsightForge AI"
hackathon: "Amazon Nova AI Hackathon"
organization: "Amazon"
winner: true
words: 651
team_size: 1
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/retrieval_grounding"
  - "mechanism/vision_ocr"
  - "substrate/code_repository"
  - "substrate/document_pdf"
  - "substrate/structured_db"
  - "substrate/video_visual"
---

# InsightForge AI

> Multimodal document intelligence powered by Amazon Nova.

[Devpost](https://devpost.com/software/insightforge-ai) · hackathon [[Amazon Nova AI Hackathon]]

## Facets

**mechanism** [[retrieval_grounding]] [[vision_ocr]]
  <sub>weak: realtime_stream</sub>
**substrate** [[code_repository]] [[document_pdf]] [[structured_db]] [[video_visual]]

**stack** ai, amazon, amazon-web-services, bedrock, css, iam, javascript, multimodal, nova, novalite, novavision, python, python-package-index, rag

## How they structured the write-up

- 🚀 insightforge ai
- what's next for insightforge ai we plan to expand insightforge ai into: ### 🚀 enterprise intelligence platform - s3 & sharepoint integrations - real-time kpi monitoring - risk anomaly alerts - predictive analytics future formula-driven forecasting example: $$ \text{forecast}_{t+1} = \text{current value} \times (1 + \text{growth rate}) $$ ---
- built with languages - python framework - streamlit ai & cloud - amazon bedrock - amazon nova lite - amazon nova vision data & processing - pandas - numpy - faiss

## Body

🚀 InsightForge AI Multilingual AI Intelligence Engine powered by Amazon Nova Inspiration In today’s world, organizations generate massive volumes of documents — reports, Excel sheets, contracts, scanned PDFs, presentations, and multilingual news articles. Despite advances in AI, extracting executive-level insights still requires manual effort. We asked ourselves: What if uploading a document was enough to instantly generate a boardroom-ready dashboard? That question inspired InsightForge AI — a system that transforms static files into structured intelligence using Amazon Nova. What it does InsightForge AI allows users to upload: 📄 PDF (digital or scanned) 📊 Excel / CSV 🖼️ Images 📝 Word documents 📽️ PowerPoint presentations 🌐 Multilingual content (Tamil, Hindi, English, and more) From a single upload, the system automatically: Extracts text (including OCR for scanned PDFs) Detects document language Generates an Executive Dashboard Identifies meaningful KPIs Computes derived statistics Extracts key dates and timelines Detects risks and recommended actions Enables document chat with evidence grounding Exports a professional PDF report All insights are generated in the same language as the uploaded document. How we built it InsightForge AI is built using a hybrid AI architecture powered by Amazon Bedrock and Amazon Nova. 1️⃣ Multimodal Document Processing PDF parsing using pypdf OCR fallback using Nova Vision Excel parsing using pandas Word & PowerPoint extraction Image-to-text conversion via Nova multimodal capabilities 2️⃣ Fully AI-Controlled Executive Dashboard We use Amazon Nova Lite to generate structured dashboard insights in strict JSON format. For example, when multiple numeric signals exist, Nova dynamically computes: Inline formula example: Displayed formula: $$ \text{Risk Score} = \frac{\text{Detected Risks}}{\text{Total Signals}} \times 100 $$ This ensures the dashboard is not static — it is dynamically reasoned. --- ### 3️⃣ Retrieval-Augmented Generation (RAG) Documents are: - Chunked - Converted to embeddings - Indexed using FAISS - Retrieved contextually for question answering This enables grounded responses with evidence. Example code structure: python hits, scores = rag.search(user_query, k=top_k) answer = ask_with_evidence(user_query, context_chunks) 4️⃣ Multilingual Intelligence We automatically detect document language and instruct Nova to respond strictly in that language. Tamil input → Tamil insights Hindi input → Hindi insights English input → English insights This significantly improves accessibility. --- ## Challenges we ran into ### 🔹 OCR Noise Scanned newspaper PDFs sometimes generate duplicated timestamps like: 2019-02-13 10:30:00 2019-02-13 10:30:00 We implemented text normalization and filtering before AI processing. --- ### 🔹 Excel KPI Noise Excel files often contain many numeric columns that are not meaningful KPIs. We solved this by: - Scoring column names semantically - Filtering numeric density - Ignoring small or date-like values - Prioritizing business-relevant signals --- 🔹 Strict JSON Enforcement Large Language Models sometimes output malformed JSON. We enforced: - Structured prompting - Schema validation - Safe parsing with fallbacks --- ## Accomplishments that we're proud of - ✅ Fully multimodal ingestion - ✅ AI-driven executive dashboard - ✅ Language-aware insight generation - ✅ Evidence-backed document chat - ✅ Professional PDF report export - ✅ Clean premium UI with animated AI background Most importantly: > We transformed document upload into instant intelligence generation. --- ## What we learned - Hybrid AI systems are more reliable than pure LLM outputs. - Multilingual prompting significantly improves output quality. - Structured schema prompts dramatically improve AI reliability. - Amazon Nova performs exceptionally well when guided with precise context. --- What's next for InsightForge AI We plan to expand InsightForge AI into: ### 🚀 Enterprise Intelligence Platform - S3 & SharePoint integrations - Real-time KPI monitoring - Risk anomaly alerts - Predictive analytics Future formula-driven forecasting example: $$ \text{Forecast}_{t+1} = \text{Current Value} \times (1 + \text{Growth Rate}) $$ --- Built With Languages - Python Framework - Streamlit AI & Cloud - Amazon Bedrock - Amazon Nova Lite - Amazon Nova Vision Data & Processing - Pandas - NumPy - FAISS Document Tools - pypdf - PyMuPDF - python-docx - python-pptx - Pillow Report Generation - ReportLab --- ## Repository InsightForge AI on GitHub <div