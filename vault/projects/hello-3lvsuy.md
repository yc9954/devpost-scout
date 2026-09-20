---
slug: "hello-3lvsuy"
url: "https://devpost.com/software/hello-3lvsuy"
title: "MedShare"
hackathon: "NexHacks"
organization: "FII"
winner: true
words: 712
team_size: 4
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "mechanism/vision_ocr"
  - "domain/civic_government"
  - "domain/developer_tools"
  - "domain/health_clinical"
  - "domain/supply_logistics"
  - "user/developer"
  - "substrate/document_pdf"
  - "substrate/structured_db"
  - "substrate/transcript_audio"
---

# MedShare

> Expired meds cost hospitals millions. MedShare catches them first.

[Devpost](https://devpost.com/software/hello-3lvsuy) · hackathon [[NexHacks]]

## Facets

**mechanism** [[realtime_stream]] [[vision_ocr]]
**domain** [[civic_government]] [[developer_tools]] [[health_clinical]] [[supply_logistics]]
**user** [[developer]]
**substrate** [[document_pdf]] [[structured_db]] [[transcript_audio]]

**stack** chatgpt, claude, cursor, python, sql, supabase, typescript, woodwideai

## How they structured the write-up

- turn hospital pharmacy waste into savings
- the problem
- the solution
- key features
- what makes it revolutionary

## Body

MedShare Turn Hospital Pharmacy Waste Into Savings AI-powered pharmacy analytics that transforms spreadsheets into actionable intelligence — helping hospitals save thousands monthly on expired medications. The Problem Hospital pharmacies are hemorrhaging money on expired medications. Statistic Impact * $800 billion wasted annually on expired medications in US hospitals 20-50% of prepared anesthesia drugs discarded unused 72% of all drug returns are expired inventory 4x increase in drug shortages over the past 5 years The root cause? Pharmacy directors manage millions in inventory using spreadsheets and gut instinct. No visibility into what's expiring until it's too late No demand forecasting — just over-ordering "to be safe" No FIFO compliance tracking — newer lots get used first, older lots expire No analytics layer between inventory systems and decisions "I manage 2,000+ medications in Excel. I don't know what's expiring until it's too late." — Hospital Pharmacist The Solution MedShare transforms pharmacy spreadsheets into actionable intelligence. Upload CSV → See What's At Risk → Get AI Recommendations → Save Money Upload your existing inventory export (CSV/Excel) — takes 5 seconds Instantly see expiring medications ranked by dollars at risk AI analyzes your usage patterns and forecasts 30-day demand Get specific recommendations: "Reduce Propofol order by 15%" Real-time voice alerts for critical expirations One hospital. One upload. $4,200/month saved. Key Features Dashboard and Analytics Real-time inventory overview with 4 key stat cards Usage trend charts with 8-week historical data visualization Department breakdown showing medication usage by OR, ICU, ER 30-day demand forecasting with confidence intervals Expiration Alert System Smart prioritization by urgency (High/Medium/Low) Dollar impact calculation showing exact value at risk FIFO violation detection preventing avoidable waste CSV export for compliance and pharmacy director review Voice Alerts Dynamic voice announcements using Web Speech API Live transcript display with word-by-word animation Medicine-specific alerts with quantities and expiration dates AI Drug Scanner Webcam-based label recognition with computer vision Automatic OCR for drug names, NDC codes, lot numbers Quick inventory addition from physical labels Multi-Hospital Support Hospital selector with 3 demo locations (Metro General, St. Mary's, County Medical) Distance-based matching for potential transfers Network view showing nearby facility inventory Reports and Exports 5 report types: Inventory, Expiration, FIFO, Forecast, Insights PDF generation with professional formatting CSV exports for all data views What Makes It Revolutionary Compound Intelligence Pipeline (Wood Wide AI) We chain three ML models to create insights no single model could produce: API Function Output Cluster Segments medications into risk profiles High Risk, Stable, Volatile groupings Predict Forecasts demand per cluster 30-day usage with confidence intervals Anomaly Detects patterns within clusters FIFO violations, usage spikes Each output feeds the next — true compound reasoning, not sequential calls. The insight loop: Clusters tell you WHERE to look Predictions tell you HOW MUCH is at risk Anomalies tell you WHY waste is happening Together: one actionable decision with dollar impact Challenges We Ran Into During development, one of the major challenges we encountered was integrating MongoDB with Atlas. Despite correctly configuring IP whitelisting and attempting multiple troubleshooting approaches—including switching networks, using mobile hotspots, and revalidating access rules—we were consistently blocked from establishing a stable connection. We escalated the issue to MLH representatives, who also attempted to diagnose the problem but were ultimately unable to resolve it due to the underlying nature of the Atlas networking constraints. This obstacle significantly hindered our progress, as MongoDB was a core architectural choice intended to support a dynamic NoSQL schema for scalable ingestion of CSV-based pharmaceutical medicine inventory data. The flexibility of MongoDB would have allowed us to seamlessly accommodate varying data types and evolving inventory attributes. However, the persistent integration issues consumed valuable development time and began to impact our ability to deliver other planned features. Rather than allowing this setback to stall the project, we demonstrated resilience and adaptability by pivoting our database strategy. We transitioned to Supabase, leveraging its PostgreSQL foundation and developer-friendly tooling to quickly restore momentum. Supabase integrated smoothly with our existing tech stack, provided reliable authentication and database access, and allowed us to model our inventory data with strong typing and relational integrity while still maintaining flexibility through JSON fields where needed. This strategic shift enabled us to unblock development, refocus on feature implementation, and deliver a stable, scalable backend solution despite the earlier infrastructure challenges. <div