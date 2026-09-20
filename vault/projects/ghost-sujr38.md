---
slug: "ghost-sujr38"
url: "https://devpost.com/software/ghost-sujr38"
title: "See Me Thru"
hackathon: "NexHacks"
organization: "FII"
winner: true
words: 772
team_size: 4
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/deterministic_policy"
  - "mechanism/graph_reasoning"
  - "mechanism/on_device_local"
  - "mechanism/realtime_stream"
  - "mechanism/structural_withholding"
  - "domain/accessibility"
  - "domain/developer_tools"
  - "domain/elder_child_care"
  - "domain/finance_payments"
  - "domain/health_clinical"
  - "domain/labor_employment"
  - "domain/mental_health"
  - "user/clinician"
  - "user/patient_family"
  - "user/social_worker"
  - "substrate/document_pdf"
  - "substrate/geospatial"
  - "substrate/medical_record"
  - "substrate/structured_db"
  - "substrate/video_visual"
---

# See Me Thru

> See Me thru uses Meta Glasses & a novel "Care-Mask" compression AI to turn live video into automated, accurate iMessage care logs. It cuts charting time, letting aides focus on patients, not paperwork

[Devpost](https://devpost.com/software/ghost-sujr38) · hackathon [[NexHacks]]

## Facets

**mechanism** [[deterministic_policy]] [[graph_reasoning]] [[on_device_local]] [[realtime_stream]] [[structural_withholding]]
**domain** [[accessibility]] [[developer_tools]] [[elder_child_care]] [[finance_payments]] [[health_clinical]] [[labor_employment]] [[mental_health]]
**user** [[clinician]] [[patient_family]] [[social_worker]]
**substrate** [[document_pdf]] [[geospatial]] [[medical_record]] [[structured_db]] [[video_visual]]

**stack** ai, flask, imessagekit, node.js, openai, overshoot, thetokencompany, trae

## How they structured the write-up

- 💡 inspiration
- 🤖 what it does
- 💼 business value & use case
- ⚙️ how we built it (the "alternative compression" architecture)
- 🚧 challenges we ran into
- 🏆 accomplishments that we're proud of
- 🚀 what's next for see me thru

## Body

Project Architecture UI demo picture Graph sample 💡 Inspiration This project was born from two compounding crises in home health: family anxiety and caregiver burnout . For families, the biggest fear is the "Handoff Gap." A daughter comes home and asks, "Did Mom drink enough water today?" and the tired aide, who cared for three other people, can only say, "I think so?" Families are flying blind regarding the daily well-being of their loved ones. For healthcare workers, the burden is manual charting . They spend hours every day typing redundant logs—"patient ate lunch," "patient sat in chair"—just to create a record. This administrative addon takes time away from actual care. We wanted to solve both problems not by building another app for them to tap, but by removing the interface entirely. We asked: Can we build an AI that passively watches the shift, ignores the noise, but locks onto the critical medical facts with 100% fidelity, automatically creating the log that everyone needs? 🤖 What it does See Me Thru is a "Zero-Admin" Shift Logger that turns passive observation into active reporting. Watches Live: The patient wears Meta Ray-Ban glasses , livestreaming their point-of-view during patient interactions. Overshoot converts this live video into a continuous text stream. Decides intelligently: Our system intelligently separates "lifestyle noise" (sitting on the couch) from "clinical signal" (taking medication) based on the patient's specific personalized care plan. Reports automatically: It automatically texts family members a summary via iMessage only when critical care goals are met or can be customized for hourly report (e.g., "Hydration Goal Met at 10:15 AM" ), creating a perfect memory of the shift without manual effort. 💼 Business Value & Use Case This is not just a convenience tool; it addresses a critical economic crisis in healthcare. Reclaiming Billable Hours: With a global shortage of care workers, spending 2 hours per shift on paperwork is unsustainable. See Me Thru reclaims that time for actual patient care or additional visits. Reducing Hospital Readmissions: The "Handoff Gap" leads to missed medications and dehydration, which cause expensive ER visits. By providing an accurate, real-time log to families and incoming nurses, we catch issues before they become emergencies. Verifiable Proof of Care: Insurance providers need proof that services were rendered. Our graph-based logs provide a structured, auditable trail of care activities derived directly from visual evidence. ⚙️ How we built it (The "Alternative Compression" Architecture) Please refer to the attached architecture diagram for the complete workflow. To win the Alternative Compression Model track, we couldn't just use an existing API. We had to invent a safer way to compress data for healthcare. Standard compression models are dangerous here because they might summarize "Patient did not take pills" into "Patient... pills." Our innovation is the "Care-Mask" Semantic Router . It’s a hybrid "neuro-symbolic" system: Symbolic Safety (The Graph): We use Neo4j to define the "rules" of the patient's care (e.g., vectors for "Hydration", "Fall Risk"). This is our deterministic safety layer. Neural Efficiency (The Model): We use The Token Company's bear-1 model for aggressive compression of non-essential data. Our router assesses every incoming event against the Care Plan vectors. If the similarity is high (>0.45), we treat it as a Critical Event and bypass compression entirely to ensure 100% safety. If it's low, we route it to The Token Company to crush the noise. The Stack Hardware & Vision: Meta Ray-Ban Glasses livestreaming to Overshoot RealtimeVision SDK . Image-to-Text: Overshoot Compression Engine: The Token Company Knowledge Base & Memory: Neo4j Graph Database . Alerts: iMessage kit . 🚧 Challenges we ran into The "Safety vs. Savings" Trade-off: We initially tried compressing everything to maximize token savings, but the AI began hallucinating details about medication adherence. We realized healthcare requires a deterministic safety layer (The Graph) sitting in front of the probabilistic layer (The LLM). 🏆 Accomplishments that we're proud of Achieving "Safe Compression" in Real-Time: We successfully tuned our Semantic Router to aggressively crush the majority of a typical shift's "lifestyle noise" into tiny token footprints, while proving that critical events (like medication intake) completely bypassed compression to retain perfect fidelity. Balancing extreme efficiency with clinical safety was our biggest technical win. Live iMessage Integration: Seeing the phone actually buzz with a clinical observation the moment the glasses saw it in the livestream was magical. 🚀 What's next for See Me Thru Edge Privacy Mode: Running the "Care-Mask" router locally on the glasses hardware so raw video data never leaves the device—only the sanitized text logs do. EHR Integration: Piping the structured output directly into Electronic Health Record systems like Epic or Cerner, completely automating charting. <div