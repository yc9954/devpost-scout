---
slug: "edugrc-shield-interactive-ai-safety-governance-lab"
url: "https://devpost.com/software/edugrc-shield-interactive-ai-safety-governance-lab"
title: "EduGRC-Shield: Interactive AI Safety & Governance Lab"
hackathon: "DSH Hacks V1"
organization: "DreamWeave"
winner: true
words: 438
team_size: 1
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/cross_origin_web"
  - "mechanism/deterministic_policy"
  - "mechanism/realtime_stream"
  - "mechanism/simulation_digital_twin"
  - "mechanism/structural_withholding"
  - "mechanism/vision_ocr"
  - "domain/accessibility"
  - "domain/education"
  - "domain/labor_employment"
  - "domain/legal_justice"
  - "domain/security_privacy"
  - "user/educator_student"
  - "user/researcher"
  - "substrate/geospatial"
  - "substrate/web_dom"
---

# EduGRC-Shield: Interactive AI Safety & Governance Lab

> "EduGRC-Shield: An interactive simulation lab training the next generation of STEM innovators to secure and govern High-Risk AI systems against global regulatory frameworks."

[Devpost](https://devpost.com/software/edugrc-shield-interactive-ai-safety-governance-lab) · hackathon [[DSH Hacks V1]]

## Facets

**mechanism** [[cross_origin_web]] [[deterministic_policy]] [[realtime_stream]] [[simulation_digital_twin]] [[structural_withholding]] [[vision_ocr]]
**domain** [[accessibility]] [[education]] [[labor_employment]] [[legal_justice]] [[security_privacy]]
  <sub>weak: developer_tools</sub>
**user** [[educator_student]] [[researcher]]
**substrate** [[geospatial]] [[web_dom]]
  <sub>weak: structured_db</sub>

**stack** amazon-s3-(object-storage)-platform-as-a-service:-vercel-(frontend-deployment)-apis-&-integrations:-google-gemini-api-(generative-ai-capabilities)-canva-api-(design-and-media-management-workflows)-tools-&-platforms:-github-actions-(ci/cd), docker, fastapi, javascript-(typescript)-frameworks-&-libraries:-react.js, languages:-python, numpy-databases:-postgresql-(relational), pandas, redis-(caching-&-session-management)-cloud-services-&-infrastructure:-aws:-amazon-ec2-(hosting)

## How they structured the write-up

- 🔬 inspiration
- 🛠️ how we built it
- 🛑 challenges we faced
- 📚 what we learned

## Body

🔬 Inspiration As artificial intelligence transitions from academic curiosity to a foundational pillar of global infrastructure, the focus in STEM has overwhelmingly leaned toward optimization, processing power, and model deployment. However, a critical systemic vulnerability has been largely ignored in standard tech education: AI Governance, Risk, and Compliance (GRC). Engineering and data science students regularly build sophisticated neural networks but graduate completely blind to the legal, security, and ethical boundaries governing them—such as the EU AI Act , GDPR , and global data sovereignty mandates. We were inspired to bridge this dangerous gap. We built EduGRC-Shield to democratize technical risk architecture, transforming dry legislative articles into a hands-on, interactive simulation lab where students can actively mitigate compliance vulnerabilities. 🛠️ How We Built It EduGRC-Shield was engineered to run seamlessly in any browser environment to ensure zero-friction accessibility for students globally. State Management Architecture: Built using a responsive frontend logic framework where system parameters are governed by a real-time state machine. Dynamic IaC Processing Engine: When a user toggles a compliance control, the internal state updates and a dynamic script synthesizer evaluates the active vectors. It instantly compiles and outputs compliant infrastructure configurations (e.g., matching AWS S3 Bucket policy structures). Framework Mapping Matrix: We structurally cross-referenced user control states directly with official regulatory articles (such as EU AI Act Article 10 for Data Governance and Article 13 for Transparency/Explainability). 🛑 Challenges We Faced Our primary challenge was designing a system that accurately represents the mathematical and regulatory complexity of compliance mapping without overwhelming a beginner student. For instance, true AI trust requires quantifying explainability. In a production environment, this involves computing cooperative game theory values via SHAP (SHapley Additive exPlanations). To illustrate the mathematical weight of the control, we mapped the classic Shapley marginal contribution formula into our conceptual lab framework: $$\phi_i(v) = \sum_{S \subseteq N \setminus {i}} \frac{|S|!(|N| - |S| - 1)!}{|N|!} \left( v(S \cup {i}) - v(S) \right)$$ Translating this heavy mathematical logic and complex statutory requirements into clean, instantaneous web visuals required highly strict DOM manipulation optimization to prevent lag and preserve an intuitive user interface. 📚 What We Learned This project deepened our understanding of the deep intersection between hard-coded software architectures and international digital policy . We learned that compliance shouldn't be an afterthought handled by legal teams after a product is built. True security requires building data pipelines that are legally compliant and secure by design . Furthermore, we proved that gamifying enterprise-grade compliance controls is one of the most effective ways to arm the next generation of STEM innovators with the technical risk management skills they need for the future workforce. <div