---
slug: "resqlink-app"
url: "https://devpost.com/software/resqlink-app"
title: "Gen shield App"
hackathon: "DSH Hacks V1"
organization: "DreamWeave"
winner: true
words: 582
team_size: 2
has_repo: false
has_live: false
has_video: false
tags:
  - "project"
  - "domain/health_clinical"
  - "domain/scientific_research"
  - "user/clinician"
  - "substrate/document_pdf"
  - "substrate/genomic_bio"
  - "substrate/structured_db"
---

# Gen shield App

> GenShield AI — Empowering early breast cancer detection in Egyptian women through AI-powered genomic risk assessment and precision medicine.

[Devpost](https://devpost.com/software/resqlink-app) · hackathon [[DSH Hacks V1]]

## Facets

**domain** [[health_clinical]] [[scientific_research]]
  <sub>weak: mental_health</sub>
**user** [[clinician]]
**substrate** [[document_pdf]] [[genomic_bio]] [[structured_db]]

**stack** android, brca1/brca2-analysis, dart, database, firebase-authentication, flutter, genomic-risk-assessment, kotlin, local, machine-learning, modified-gail-model, pdf-report-generation, population-specific-genomic-data

## How they structured the write-up

- what is next

## Body

GenShield uses AI and genomic insights to predict breast cancer risk early, enabling smarter screening and personalized prevention. Inspiration Breast cancer remains one of the most common and life-threatening diseases affecting women in Egypt. Many women are diagnosed at later stages due to limited awareness, expensive genetic testing, and the lack of population-specific screening tools. Most existing AI and genomic risk assessment systems are designed using European genetic datasets, which do not accurately represent Egyptian genetic profiles and BRCA mutation patterns. We wanted to build a solution that combines artificial intelligence, genomics, and accessibility to help Egyptian women detect risks earlier and make informed healthcare decisions before symptoms appear. What it does GenShield AI is an AI-powered genomic risk assessment platform designed specifically for Egyptian women. The platform analyzes genetic mutations, family history, lifestyle factors, and clinical data to estimate breast cancer risk levels. The system provides: Personalized risk scores Risk classification (Low, Moderate, High, Very High) Early screening recommendations Clinical guidance and preventive suggestions Secure assessment history tracking Downloadable medical-style PDF reports Arabic and English support for accessibility GenShield acts as an early warning and decision-support system that helps prioritize high-risk individuals for further medical screening and genetic counseling. How we built it We developed GenShield using a modern full-stack architecture. Frontend: React 19 Tailwind CSS 4 Backend: Express.js tRPC 11 Database: MySQL with Drizzle ORM AI & Data Science: Modified Gail Model Population-specific BRCA mutation analysis Egyptian genetic prevalence adjustments Risk classification algorithms using 25+ weighted risk factors Additional features: OAuth secure authentication PDF report generation using ReportLab and WeasyPrint Cloud-ready scalable architecture Multi-language RTL support We also integrated research from Egyptian BRCA studies, international cancer databases, and clinical screening guidelines to ensure scientific reliability. Challenges we ran into One of the biggest challenges was the lack of accessible Egyptian genomic datasets compared to Western databases. Most publicly available breast cancer prediction tools are trained on European populations, which creates accuracy limitations for Egyptian women. Another challenge was balancing medical accuracy with user accessibility. We needed to simplify complex genetic and clinical concepts into a user-friendly experience without losing scientific value. Building a culturally appropriate bilingual interface and ensuring secure healthcare data handling were also important technical and ethical challenges. Accomplishments that we're proud of Creating one of the first AI-powered breast cancer risk assessment tools tailored specifically for Egyptian women Successfully combining genomics, machine learning, and healthcare into a practical real-world solution Designing a fully bilingual Arabic-English platform Building a scalable cloud-ready architecture Developing personalized clinical recommendations instead of generic outputs Raising awareness about precision medicine and early cancer detection in underserved communities Most importantly, we are proud that GenShield has the potential to help save lives through early detection and informed medical decisions. What we learned Through this project, we learned that AI in healthcare is not only about building accurate models, but also about accessibility, ethics, trust, and localization. We gained experience in: Healthcare AI development Medical data analysis Population-specific machine learning Full-stack system architecture Scientific research integration User-centered healthcare design We also learned the importance of building technology that solves real regional problems instead of relying entirely on global solutions. What is next Expanding Egyptian genomic datasets to improve accuracy Adding advanced AI models for better risk prediction Clinical validation with healthcare professionals Integrating imaging (mammography) data Developing a mobile app for wider access Improving explainability (XAI) for doctors and users Expanding to MENA region in the future Partnering with hospitals for early detection programs <div