---
slug: "threat-feeds"
url: "https://devpost.com/software/threat-feeds"
title: "Threat Feeds"
hackathon: "SANS AI Cybersecurity Hackathon"
organization: "sans"
winner: true
words: 732
team_size: 1
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/retrieval_grounding"
  - "domain/security_privacy"
  - "user/researcher"
  - "substrate/document_pdf"
  - "substrate/structured_db"
  - "substrate/web_dom"
---

# Threat Feeds

> Threat Feeds is a web application that allows users to browse, view indicators of compromise, search and ask questions about the latest threat reports published across the security industry.

[Devpost](https://devpost.com/software/threat-feeds) · hackathon [[SANS AI Cybersecurity Hackathon]]

## Facets

**mechanism** [[retrieval_grounding]]
**domain** [[security_privacy]]
**user** [[researcher]]
**substrate** [[document_pdf]] [[structured_db]] [[web_dom]]

**stack** amazon-web-services, chromadb, pinecone, postgresql, python, sqlite

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for threat feeds

## Body

Landing page Full-text search Ask AI / Question-Answering Extracted IOCs and AI-based false-positive detection Related reports Report filtering API docs Inspiration Every day, security researchers across the world publish reports and blog posts providing intelligence about the latest threats affecting users and enterprieses. Threat research teams spend a lot of time and effort reading through tens of reports every day. This poses several challenges: Manually identifying indicators of compromise (IOCs) is time-consuming and error-prone since it's easy to miss some values when reading several reports. Threat researchers' time is better spent actually analyzing malware. Security teams end up building bespoke tools to extract IOCs using regular expression pattern matching or other one-off scripts. These generate a lot of false positive IOCs, contributing to the already high levels of alert fatigue. Bespoke IOC extraction tools also miss several important indicators like threat groups, actors, tools sand techniques No existing tools support full text search and interactive question-answering over the corpus of existing threat reports. This is crucial in aggregating knowledge over multiple related reports to aid with mitigation The Threat Feeds web app attempts to address these challenges and make security researchers happier :) What it does Thread Feeds is a feed of public threat reports published by cybersecurity teams in Mandiant, Sophos, Microsoft, Google, CheckPoint Research, CISA, SANS etc. The web application allows users to interact in several ways with these threat reports: Filter threat reports by title, source and publish date Full text search across threat report contents Ask AI lets users pose detailed questions on the contents of the threat reports AI-assisted IOC extraction (hashes, IP addresses, domain names, CVEs, MITRE Attack types, YARA rules) for each threat report AI-driven, context-based false positive IOC detection for each threat report VirusTotal, NIST vulnerability and MITRE enrichments for each report AI-generated "related reports" or "more like this" feature for each threat report APIs for listing and searching reports, retrieving a particular report and the Q&A feature. Unique, shareable URLs for report details How we built it Architecture Diagram Architecture and technologies: feeds.txt contains a list of security report RSS feeds to pull from The latest reports are crawled from the feed, the contents are parsed to extract snippets that look like the following IOCs IP addresses URLs / domains YARA rules MITRE Attack entites like threat groups, actors, tactics, techniques etc. Hashes CVEs The IOCs are stored in a SQLite database, the raw page data is stored in local files and the parsed contents are indexed for search into a Whoosh search collection The Qwen2.5-14B model is used to detect false positive IOCs using the context within the threat report Hashes, CVEs and MITRE Attack entities are enriched by linking the approriate VirusTotal, NIST NVD and MITRE Attack URLs The saved pages are chunked and converted into embeddings for vector search. For the "Related Reports" feature, all-MiniLM-L6-v2 is used to generate embeddings and ChromaDB is used as the vector database For the "Ask AI" feature, Pinecone Assistant is used for Document AI All the SQLite data is migrated to a PostgreSQL instance running on AWS The web application is an AWS Elastic Beanstalk instance serving from a Flask server Challenges we ran into I didn't want to spend too much money on LLM inference, so I had to endure long iteration times on fine tuning the LLM prompts for false positive detection Read several threat reports to cross-reference the IOCs extracted from them to ensure the LLM wasn't hallucinating and was performing reasonably well Unfamilarity with UI / frontend frameworks, had to do some learning there. With the help of https://v0.dev/ I was able to cobble a basic UI together Accomplishments that we're proud of Having a full working feature-rich web app with API support What we learned Reading several threat reports has given me an even higher level of appreciation for security researchers' jobs, and rigor Learned a lot about MITRE Attack entities and vulnerabilities Understanding how Retrieval-Augmented-Generation works, and using embeddings for vector search What's next for Threat Feeds User generated content Votes and comments Upload custom, private threat reports Share threat reports privately Mark IOCs as true or false positive Support filtering and sorting by more fields AI-generated summaries, mitigation recommendations, action items Support more report types like PDFs, STIX format etc. Chatbot for longer conversations about the threat report contents Integrations - OpenCTI, SOAR enrichment plugins etc. <div