---
slug: "radar_cyberone"
url: "https://devpost.com/software/radar_cyberone"
title: "Radar_CyberOne"
hackathon: "Amazon Nova AI Hackathon"
organization: "Amazon"
winner: true
words: 667
team_size: 4
has_repo: false
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/on_device_local"
  - "mechanism/realtime_stream"
  - "substrate/document_pdf"
  - "substrate/structured_db"
  - "substrate/video_visual"
---

# Radar_CyberOne

> Radar_CyberOne is the first 100% Moroccan next-generation platform designed to predict threats before they become problems. It combines CTI, DRP, and EASM, powered by Amazon AI-driven intelligence.

[Devpost](https://devpost.com/software/radar_cyberone) · hackathon [[Amazon Nova AI Hackathon]]

## Facets

**mechanism** [[on_device_local]] [[realtime_stream]]
**substrate** [[document_pdf]] [[structured_db]] [[video_visual]]

**stack** api, elasticsearch, laravel, mysql, nova, python

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for radar_cyberone

## Body

Inspiration In 2025, Morocco recorded over 20 million cyberattack attempts . Behind this number lies a critical reality: most companies don’t truly understand the risks they face. Even when they invest heavily in securing their networks or internal systems, the solutions they deploy only detect attacks at the final stage, the damage itself. In Morocco, there is no cybersecurity solution like Radar_CyberOne that is specifically designed to reflect the structure and culture of Moroccan companies , and to predict threats before they occur. This gap inspired us to create a platform tailored to the local business environment . What it does Radar_CyberOne is a 100% Moroccan platform that predicts threats before they occur by aligning with the culture and specific requirements of Moroccan companies , helping to reduce risk within organizations. It combines Cyber Threat Intelligence (CTI), Digital Risk Protection (DRP), and External Attack Surface Management (EASM). The platform is powered by Amazon Nova* , from scraping data to generating structured threat reports, enabling **real-time analysis * and actionable insights. How we built it We built Radar_CyberOne as a full-stack AI platform tailored for Moroccan companies, using Amazon Nova Lite as the core AI engine throughout the entire workflow: 1- Data Collection & Scraping We scrape cybersecurity blogs, news sites, and threat reports relevant to Morocco. Nova Lite processes this raw data immediately, identifying key information even during scraping. 2- AI Processing & Analysis Nova Lite performs summarization, entity extraction, and threat identification. It detects threat actors, target Morocco, sectors, and dates from unstructured text. Using Nova at this stage ensures real-time, structured intelligence from all collected sources. 3- Report Generation After processing, Nova Lite generates structured reports aligned with the culture and requirements of Moroccan companies. Reports include actionable insights and risk assessments to help companies prevent attacks. 4- Backend & Database Python backend manages workflows, stores results, and integrates outputs from Nova Lite. 5- Frontend Dashboard A React-based interface lets companies visualize threats, track trends, and access reports easily. Summary: From scraping raw data to generating actionable reports, Nova Lite powers of Radar_CyberOne, making the platform highly automated, locally relevant, and AI-driven. Challenges we ran into Building Radar_CyberOne came with several challenges: Token Management and Costs Using Nova Lite from scraping to report generation meant processing large amounts of text. We had to optimize prompts and pipeline efficiency to keep API token usage and costs manageable. Local Context Adaptation Moroccan companies have unique structures, workflows, and cultural considerations. Customizing Nova Lite outputs to reflect this local context required iterative testing and fine-tuning via the API. Automation Reliability Combining CTI, DRP, and EASM data streams into a fully automated pipeline was complex. Ensuring Nova Lite’s summaries and extractions were consistent and actionable took several rounds of refinement. Accomplishments that we're proud of Successfully built Radar_CyberOne, the first 100% Moroccan AI platform that predicts cyber threats before they occur. Integrated Nova Lite end-to-end, from scraping raw data to generating structured reports, automating about 99% of the intelligence workflow. Developed a dashboard that visualizes threats, trends, and risk assessments in real time, making cybersecurity accessible to Moroccan companies. Demonstrated that an AI platform can adapt to local company culture and requirements, a gap not addressed by existing solutions. What we learned Working with Amazon Nova Lite end-to-end taught us how to extract structured information from unstructured text, including threat actors, sectors, and Morocco country. We learned the importance of adapting AI outputs to local context, ensuring the platform reflects the culture and needs of Moroccan companies. What's next for Radar_CyberOne Complete the full platform as soon as possible before GITEX 2026 in Marrakech to showcase it at our stand . Expand Nova Lite integration to fully automate report generation for all collected data. Improve the dashboard and analytics with alerts, trends, and actionable insights. Add multilingual support and further tailor outputs to the culture and structure of Moroccan companies. Explore Nova Act or multimodal AI to include PDFs, images, and other document types in the intelligence workflow. <div