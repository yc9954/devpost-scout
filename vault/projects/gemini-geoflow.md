---
slug: "gemini-geoflow"
url: "https://devpost.com/software/gemini-geoflow"
title: "Gemini GeoFlow"
hackathon: "Gemini 3 Hackathon"
organization: "Google"
winner: true
words: 1238
team_size: 2
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "mechanism/vision_ocr"
  - "domain/agriculture_food"
  - "domain/media_journalism"
  - "domain/scientific_research"
  - "user/researcher"
  - "substrate/document_pdf"
  - "substrate/geospatial"
  - "substrate/structured_db"
  - "substrate/video_visual"
---

# Gemini GeoFlow

> Fusing Text and Terrain: An LLM-Powered Pipeline for Preparing Archaeological Datasets

[Devpost](https://devpost.com/software/gemini-geoflow) · hackathon [[Gemini 3 Hackathon]]

## Facets

**mechanism** [[realtime_stream]] [[vision_ocr]]
**domain** [[agriculture_food]] [[media_journalism]] [[scientific_research]]
**user** [[researcher]]
**substrate** [[document_pdf]] [[geospatial]] [[structured_db]] [[video_visual]]
  <sub>weak: web_dom</sub>

**stack** css, gemini, google-earth, google-maps, html, javascript, python

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we’re proud of
- what we learned
- what’s next for gemini geoflow

## Body

demo page Inspiration The idea for this project started during a conversation with a close friend who works as an archaeologist. She described how detecting archaeological sites is still one of the most fascinating and frustrating challenges in the field. Even with access to massive amounts of remote sensing data, researchers often depend on traditional, time-consuming methods to locate and evaluate potential sites. That conversation stuck with me. It felt like a problem that was waiting for a more interdisciplinary approach. Why not bring different areas of expertise together? I reached out to another friend with a background in AI, and soon we had a small team that combined archaeological knowledge with artificial intelligence expertise. Our goal was straightforward: use our complementary skills to address a problem that has limited archaeological research for decades. The urgency of this problem becomes even clearer in places like the Amazon rainforest. Dense vegetation, difficult terrain, and limited accessibility make physical surveys extremely challenging. Yet these regions likely contain countless undiscovered archaeological sites. Traditional methods simply do not scale well enough to meet that challenge. From the beginning, we wanted to build something bigger than a single use case. By creating an open-source pipeline based on globally accessible satellite data, our aim is to give researchers around the world the tools to generate their own datasets and train custom models tailored to their regions of interest. What it does Gemini GeoFlow is an intelligent web application that automates archaeological site extraction and analysis. When a user uploads an archaeological research paper in PDF format, the system: Extracts site information using Gemini 3’s multimodal capabilities to pull coordinates, dating, cultural periods, and site characteristics from unstructured text Retrieves satellite imagery from Google Earth Engine, including Sentinel-2 RGB, NDVI, NDWI, BSI, SRTM DEM, and slope data Analyzes satellite imagery with Gemini 3 Vision to identify archaeological indicators such as earthworks, vegetation anomalies, and terrain patterns Performs contextual research using Gemini 3 with search grounding to find comparable sites worldwide, recent research, and conservation status, all backed by verifiable citations Visualizes results on interactive Google Maps, with satellite data available for download for further analysis The entire workflow runs on Gemini 3 Flash, taking advantage of its strong reasoning, multimodal understanding, structured outputs, and real-time search capabilities. How we built it Phase 1: Domain Research & Requirement Gathering We began by having in-depth conversations with my archaeology expert friend to understand how archaeological site detection actually works in practice. We discussed existing workflows, how different data sources are used, common data formats, and the major pain points researchers face today. This helped ground the project in real-world needs rather than assumptions. Phase 2: Technical Architecture Design With that domain knowledge in hand, I worked closely with my teammate who specializes in AI to design a system centered around multi-channel data, such as Sentinel-2 RGB, NDVI, NDWI, BSI, SRTM DEM, and slope. At every step, we included validation, confidence scoring, and structured outputs. Carefully documented prompts and standardized JSON responses ensure the pipeline remains reproducible and reliable. Phase 3: Gemini 3 Integration Gemini 3 Flash powers the entire AI workflow: PDF extraction : Archaeological papers are processed to extract site metadata, coordinates (supporting DMS, decimal degrees, and UTM formats), dating information, and site characteristics using structured JSON outputs Satellite analysis : Gemini 3 Vision analyzes six-panel satellite composites to detect potential archaeological features Contextual research : Search grounding is used to identify similar sites and recent research, complete with source citations Phase 4: Data Infrastructure The pipeline is built on Google Earth Engine, which provides unified access to Sentinel-2 and SRTM data. Docker and Docker Compose are used to ensure reproducible deployment. Technical Stack Backend : Python, Flask AI : Gemini 3 Flash (multimodal input, vision, search grounding, structured outputs) Geospatial : Google Earth Engine, Google Maps Deployment : Docker, Docker Compose Challenges we ran into The Data Source Dilemma One of the biggest challenges was dealing with fragmented data sources. Early on, we tried pulling Sentinel-2 optical imagery from ESA’s Copernicus Hub and elevation data like FABDEM from University of Bristol. This approach quickly revealed several issues: Fragmented authentication : Each data source required separate credentials High learning curve : Future users would need to learn and manage multiple APIs Lack of programmatic access : Some data sources did not provide APIs, making automation and large-scale workflows impractical After extensive exploration, we realized that Google Earth Engine provides access to both Sentinel-2 and SRTM elevation data with accuracy suitable for archaeological analysis. This discovery simplified everything. A single API, unified authentication, and consistent data formats dramatically lowered the barrier to entry and improved reproducibility. While the early exploration was time-consuming, consolidating the pipeline around Earth Engine ultimately saved significant complexity. Other Technical Hurdles Coordinate parsing : Archaeological papers use a wide range of coordinate formats. We implemented robust parsing logic to handle DMS, decimal degrees, UTM, and various edge cases Prompt engineering : Designing prompts that reliably produce structured outputs from highly variable PDF layouts required extensive iteration Performance optimization : We had to carefully balance image resolution and processing speed to keep the application responsive without sacrificing analytical value Accomplishments that we’re proud of We are proud of building a genuinely interdisciplinary system that bridges AI and archaeology. The project showcases Gemini 3’s multimodal strengths by seamlessly processing PDFs, analyzing complex satellite imagery, and performing grounded research within a single workflow. Gemini 3 consistently extracts detailed archaeological metadata from unstructured papers, handling ambiguous descriptions, varied coordinate formats, and confidence estimation with impressive accuracy. The vision analysis provides real value for archaeologists. By identifying vegetation anomalies, earthwork patterns, and soil indicators associated with known sites, the system generates actionable insights that can guide future field surveys. Most importantly, we have created an open-source foundation that democratizes archaeological discovery. By relying on globally accessible data through Google Earth Engine and open APIs via Gemini 3, we have lowered barriers for researchers working in remote or under-resourced regions. What we learned This project was an excellent learning experience on multiple levels. Domain Knowledge Immersing myself in archaeology was eye-opening. I learned how archaeological datasets are structured, how researchers interpret different data sources, and how subtle patterns distinguish human-made features from natural formations. Conversations with my archaeologist friend provided invaluable insight into how archaeologists think, reason, and validate findings in practice. The Power of Interdisciplinary Innovation One key takeaway is how much potential exists at the intersection of traditional fields and modern AI. Many disciplines have not yet fully integrated advanced artificial intelligence techniques, and bridging that gap can dramatically amplify research efficiency without replacing domain expertise. What’s next for Gemini GeoFlow Short-term Goals We are currently building a large archaeological site dataset using this pipeline. The extracted sites and satellite imagery will be used to train specialized deep learning models for automated feature detection, moving beyond LLM-based analysis toward dedicated computer vision models. We also plan to incorporate additional data sources, including historical Landsat archives for temporal analysis and SAR imagery for vegetation-penetrating, all-weather observation. Long-term Vision Our long-term goal is to create a collaborative platform where archaeologists worldwide can contribute papers, validate AI-detected sites, and share discoveries. A crowdsourced validation workflow would accelerate discovery while preserving scientific rigor. We also envision tight integration with field survey tools. Researchers could plan expeditions around high-probability sites, upload ground-truth data, and continuously improve model accuracy through active learning. <div