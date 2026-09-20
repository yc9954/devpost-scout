---
slug: "threat-feeds-ai-powered-threat-report-explorer"
url: "https://devpost.com/software/threat-feeds-ai-powered-threat-report-explorer"
title: "AI‑Powered Threat Report Explorer"
hackathon: "Frostbyte Hackathon"
organization: "FrostByte Club"
winner: true
words: 763
team_size: 0
has_repo: true
has_live: false
has_video: false
tags:
  - "project"
  - "mechanism/retrieval_grounding"
  - "domain/security_privacy"
  - "user/researcher"
  - "substrate/document_pdf"
  - "substrate/web_dom"
---

# AI‑Powered Threat Report Explorer

> Threat Feeds aggregates threat intel reports lets users search and ask questions over them auto extract and enriches IOC flags false positives and surfaces related reports to speed upsecurity analysis

[Devpost](https://devpost.com/software/threat-feeds-ai-powered-threat-report-explorer) · hackathon [[Frostbyte Hackathon]]

## Facets

**mechanism** [[retrieval_grounding]]
**domain** [[security_privacy]]
**user** [[researcher]]
**substrate** [[document_pdf]] [[web_dom]]

**stack** all-minilm-l6-v2, amazon-web-services, attack, aws-elastic-beanstalk, chromadb, flask, mitre, nist-nvd, pinecone-assistant, postgresql, python, qwen2.5-14b, rss-feeds, sqlite

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for threat feeds: ai‑powered threat report explorer

## Body

Inspiration Every day, security teams publish detailed threat reports packed with IOCs, tactics, and hard‑won insights—but actually using that intelligence is painful.[web:105] Analysts skim dozens of PDFs and blogs, copy‑paste indicators into homegrown scripts, and still risk missing key clues or drowning in false positives.[web:109] I wanted a tool that treats threat reports as a living knowledge base: searchable, explorable with AI, and directly usable for enrichment and detection. That became Threat Feeds: a way to turn the global stream of threat reports into an interactive, AI‑powered research surface instead of a pile of links.[page:1] What it does Threat Feeds is an AI‑powered explorer for public threat intelligence reports.[page:1] It aggregates feeds from vendors like Mandiant, Sophos, Microsoft, Google, Check Point, CISA, SANS and others into one web app and lets you: Filter reports by title, source, and publish date. Run full‑text search across all report contents. Use Ask AI to ask natural‑language questions about specific reports or across the corpus. Auto‑extract IOCs (hashes, IPs, domains, URLs, CVEs, MITRE ATT&CK entities, YARA rules). Flag likely false‑positive IOCs using LLM reasoning over the original context. Enrich indicators with VirusTotal, NIST NVD, and MITRE ATT&CK links. Discover related reports via semantic similarity so you can follow a campaign across vendors. Access everything through APIs for listing, searching, retrieving reports, and Q&A.[page:1] Instead of manually mining each PDF, analysts can search, question, and pivot across reports like they would in any modern data tool. How we built it Threat Feeds is built as a pipeline + web app:[page:1] A list of RSS feeds defines which vendor threat blogs and advisories to ingest. A crawler fetches new reports, parses the content, and uses patterns plus LLM help to extract candidate IOCs (IPs, domains, hashes, CVEs, YARA, MITRE entities, etc.). IOCs are stored initially in SQLite, with raw pages in local storage and parsed text indexed in a Whoosh search collection for full‑text queries.[page:1] The Qwen2.5‑14B model scores IOCs for likely false positives based on surrounding context.[page:1] For “related reports”, embeddings from all-MiniLM-L6-v2 are stored in ChromaDB and used to find similar documents.[page:1] For “Ask AI”, Pinecone Assistant powers a document‑aware QA layer over the vectorized report chunks.[page:1] Data is periodically migrated into PostgreSQL on AWS, and the Flask web app is deployed via Elastic Beanstalk.[page:1] The result is a stack where ingestion, enrichment, vector search, and Q&A all feed into the same UI and API. Challenges we ran into Keeping LLM costs manageable while iterating on prompts for false‑positive detection—each tweak meant re‑running evaluations on real reports.[page:1] Validating that extractions and FP flags were trustworthy required manually reading many reports and cross‑checking IOCs, which is time‑consuming but essential.[page:1] Frontend/UI wasn’t my strongest area, so designing a clean interface for filtering, search, Ask AI, IOCs, and related reports involved a lot of learning and trial‑and‑error.[page:1] Balancing speed and depth: deciding which fields to extract, which enrichments to run, and when to fall back to lazy/on‑demand computations.[page:1] Accomplishments that we're proud of Shipping a feature‑rich, end‑to‑end web app that ingests real vendor feeds, exposes full‑text and vector search, and supports both UI and API access.[page:1] Getting AI‑assisted IOC extraction and false‑positive detection to work well enough to meaningfully reduce noise compared to naive regex‑based tools.[page:1] Implementing semantic “more like this” navigation across reports, which makes campaign and actor research feel much more natural.[page:1] Building a foundation that can be extended to private reports, team workflows, and integrations with existing security stacks.[page:1] What we learned Working on Threat Feeds gave me a much deeper appreciation for how meticulous vendor threat research is and how messy real‑world reports can be.[page:1] I learned more about MITRE ATT&CK entities, vulnerability ecosystems, and how RAG + embeddings can turn static text into an interactive knowledge layer.[web:105][page:1] I also saw firsthand that combining classic search (Whoosh) with vector search and LLM reasoning is far more powerful than any one of them alone.[web:107] What's next for Threat Feeds: AI‑Powered Threat Report Explorer Support user‑generated and private reports, with options for sharing and access control. Let analysts vote and comment on IOCs, and explicitly mark true vs false positives to improve future scoring. Add richer AI features: summaries, mitigation recommendations, and suggested action items per report.[page:1] Expand file support (PDF, STIX, more vendor formats) and add a chatbot for longer, contextual conversations about report contents. Integrate with tools like OpenCTI and SOAR platforms to push enriched intel directly into existing workflows.[page:1] The goal is to turn Threat Feeds into a shared, living intelligence console where reading a report is just the starting point—not the whole job. <div