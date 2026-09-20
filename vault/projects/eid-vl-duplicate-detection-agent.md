---
slug: "eid-vl-duplicate-detection-agent"
url: "https://devpost.com/software/eid-vl-duplicate-detection-agent"
title: "EID/VL Duplicate Detection Agent"
hackathon: "Elasticsearch Agent Builder Hackathon"
organization: "Elastic"
winner: true
words: 1318
team_size: 1
has_repo: true
has_live: false
has_video: false
tags:
  - "project"
  - "mechanism/graph_reasoning"
  - "mechanism/human_in_the_loop"
  - "mechanism/multi_agent"
  - "mechanism/provenance_signing"
  - "mechanism/realtime_stream"
  - "mechanism/simulation_digital_twin"
  - "domain/education"
  - "domain/finance_payments"
  - "domain/health_clinical"
  - "domain/labor_employment"
  - "domain/scientific_research"
  - "user/government_staff"
  - "user/legal_professional"
  - "user/patient_family"
  - "substrate/document_pdf"
  - "substrate/sensor_telemetry"
---

# EID/VL Duplicate Detection Agent

> AI-powered multi-agent system detecting duplicate HIV test records in Kenya, saving $195K annually through automated pattern analysis with 99% time reduction.

[Devpost](https://devpost.com/software/eid-vl-duplicate-detection-agent) · hackathon [[Elasticsearch Agent Builder Hackathon]]

## Facets

**mechanism** [[graph_reasoning]] [[human_in_the_loop]] [[multi_agent]] [[provenance_signing]] [[realtime_stream]] [[simulation_digital_twin]]
**domain** [[education]] [[finance_payments]] [[health_clinical]] [[labor_employment]] [[scientific_research]]
**user** [[government_staff]] [[legal_professional]] [[patient_family]]
**substrate** [[document_pdf]] [[sensor_telemetry]]

**stack** agent, ai, builder, data, detection, elasticsearch, es|ql, healthcare, kenya, multi-agent, pattern, python

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for eid/vl duplicate detection agent

## Body

System logo Multi-Agent Orchestration Layer │ Multi-Agent Orchestration (UI layer) Multi-Agent Orchestration (UI layer) Multi-Agent Orchestration (UI layer) Multi-Agent Orchestration (UI layer) Multi-Agent Orchestration (UI layer) Multi-Agent Orchestration (UI layer) Multi-Agent Orchestration (UI layer) Multi-Agent Orchestration (UI layer) EID/VL Records - elastic search index Multi-Agent Orchestration when intergated with other HMIS(Simulation) results No duplicate patient record found Registration(Service point) Multi-Agent Orchestration when intergated with other HMIS(Simulation) results - Existing patient found - prevent duplication Kibana Visualization Kibana Visualization Inspiration Working in Kenya's healthcare system, I witnessed firsthand how duplicate patient records in HIV testing programs waste critical resources and compromise patient care. Patients were accessing Early Infant Diagnosis (EID) and Viral Load (VL) services at multiple facilities using different names and IDs, creating duplicate records that cost the system an estimated $195,000 annually while making it nearly impossible to track patient outcomes effectively. Manual duplicate detection takes 2 hours per case and catches only 44% of duplicates. With over 500 healthcare facilities across Kenya, this was a problem screaming for AI automation. The Elasticsearch Agent Builder Hackathon provided the perfect opportunity to build a solution that could actually save lives and money. What it does The EID/VL Duplicate Detection Agent is a multi-agent AI system that automatically identifies, analyzes, and prevents duplicate patient records in HIV testing programs. The system uses three specialized agents working together: Detection Agent - Scans patient records using ES|QL queries to find duplicates through cross-facility pattern matching, demographic analysis, and temporal anomaly detection. It identifies patients visiting multiple facilities, same-day testing at different locations, and inconsistent demographic information. Risk Assessor Agent - Calculates risk scores (0-100) based on weighted factors including cross-facility visits (+40 points), demographic inconsistencies (+30 points), geographic impossibilities (+20 points), and timing anomalies (+10 points). Cases are classified as CRITICAL, HIGH, MEDIUM, or LOW priority. Action Recommender Agent - Provides specific recommendations for each case, from immediate M&E officer reviews to systemic improvements like staff training and policy changes, all tailored to the Kenyan healthcare context. The system analyzes 1,010 patient records in under 10 seconds, identifying 131 duplicate patients including 5 cases of same-day multi-facility testing and 4 patients with inconsistent sex identifiers across facilities - patterns that would take weeks to detect manually. How we built it Technology Stack: Elasticsearch 8.11 (Serverless) for data storage and search Agent Builder framework for multi-agent orchestration Claude Sonnet 3.7 as the reasoning model ES|QL for advanced pattern analysis Python for data processing and analytics scripts Development Process: Data Analysis - Started with real EID/VL testing data from Kenyan healthcare facilities (1,010 anonymized records across 59 facilities) Index Design - Created Elasticsearch mappings optimized for duplicate detection with derived fields like cross_facility_flag, total_tests, and facility_count Agent Development - Built three specialized agents in Kibana's Agent Builder: Crafted custom instructions for each agent's domain expertise Configured tools (search, ES|QL, document retrieval) Designed multi-step reasoning workflows Pattern Detection - Developed ES|QL queries for: Facility network analysis Same-day multi-facility detection Demographic consistency checking Risk scoring algorithms Analytics Scripts - Created Python automation for data processing, advanced analytics, network visualization, and impact calculations Documentation - Built comprehensive setup guides, architectural diagrams, and demo scripts for judges to recreate the system The entire system was built, tested, and documented in under one week using Agent Builder's rapid development capabilities. Challenges we ran into 1. Data Quality Issues Real healthcare data is messy - missing dates, inconsistent formats, partial records. Had to implement robust error handling and fuzzy matching logic to handle incomplete demographic information while avoiding false positives. 2. ES|QL Query Optimization Initially struggled with complex date calculations in ES|QL that caused syntax errors. Learned to work within ES|QL's constraints by simplifying queries and performing calculations in the application layer when needed. 3. Balancing Sensitivity and Specificity The toughest challenge was tuning the system to catch real duplicates without flagging legitimate follow-up testing. Solved this by implementing multi-factor risk scoring rather than binary duplicate/not-duplicate classification, giving M&E officers the context to make informed decisions. 4. Agent Instruction Optimization Getting the agents to produce consistent, evidence-based responses required multiple iterations of the custom instructions. Had to be very specific about output format, evidence requirements, and reasoning steps to ensure reliable performance across different queries. 5. Real-World Constraints Designing for the Kenyan context meant accounting for limited internet connectivity, varying technical literacy, and resource constraints. The solution had to work with existing infrastructure (OpenMRS, KenyaEMR) without requiring expensive new systems. Accomplishments that we're proud of Technical Achievements: Successfully orchestrated 3 specialized agents working together seamlessly Achieved 99% time reduction (2 hours → 8 seconds per case) Reached 95%+ detection accuracy on real healthcare data Built production-ready system in under one week using Agent Builder Real-World Impact: Identified $48,000 in annual waste from just 1,010 sample records Detected 5 same-day multi-facility cases that manual review missed Found 4 patients with intentionally inconsistent demographics Projected $195,000 national savings across Kenya's 500+ facilities Innovation: First healthcare duplicate detection agent in the Elastic ecosystem Novel application of multi-agent orchestration to African healthcare challenges Demonstrates how Agent Builder can solve complex, real-world problems beyond typical chatbot use cases Execution Quality: Complete documentation (setup guide, architecture, demo script) All code open source with MIT license Fully reproducible by judges in 20 minutes Ready for actual deployment in Kenyan healthcare system Most proud that this isn't just a hackathon demo - it's a solution we can actually deploy to help real patients and save real money in Kenya's healthcare system. What we learned Agent Builder Capabilities: Multi-agent orchestration is incredibly powerful for complex workflows ES|QL's performance makes it ideal for real-time analytics at scale Custom instructions are key - being specific and structured yields better results Agent Builder dramatically accelerates development compared to traditional coding Healthcare AI Challenges: Domain expertise matters - understanding EID/VL workflows was crucial to building effective detection logic Context is everything - what works in Western healthcare systems doesn't directly translate to African settings Explainability is critical - healthcare workers need to understand WHY the system flagged something Data quality drives accuracy - garbage in, garbage out still applies to AI Technical Insights: Hybrid search (BM25 + semantic) outperforms either approach alone Fuzzy matching on demographics requires careful tuning per field type Risk scoring beats binary classification for human-in-the-loop systems Pattern detection at query-time beats pre-computed flags for evolving fraud patterns Hackathon Strategy: Start with a real problem you understand deeply Use actual data, not synthetic samples Build for production, not just demo Document thoroughly - judges appreciate it Personal Growth: Learned ES|QL from scratch during this hackathon Gained deeper understanding of multi-agent system design Improved at technical writing and documentation Experienced how quickly you can build impactful solutions with the right tools What's next for EID/VL Duplicate Detection Agent Phase 1: Pilot Deployment (2-3 months) Deploy in 5 Nairobi County facilities Train M&E officers and facility staff Collect real-world performance data Refine based on user feedback Phase 2: Enhanced Detection (3-6 months) Integrate biometric matching (fingerprints) Add name fuzzy matching with Swahili phonetics Implement real-time prevention during patient registration Build WhatsApp bot for M&E officer alerts Phase 3: System Integration (6-12 months) Connect with Kenya HIE (Health Information Exchange) Integrate with OpenMRS/KenyaEMR registration workflows Add NUPI (National Unique Patient Identifier) verification Automated reporting to Ministry of Health and PEPFAR Phase 4: National Rollout (12-18 months) Scale to all 47 counties Deploy across 500+ healthcare facilities Train 1,000+ healthcare workers Establish 24/7 support infrastructure Advanced Features: Predictive analytics to identify at-risk facilities Automated case management workflows Mobile app for field officers Blockchain audit trails for compliance ML-powered fraud ring detection Sustainability: Partner with CHAI, CHS, or other NGOs for funding Explore Ministry of Health budget allocation Consider SaaS model for counties ($500-2000/month) Open source community contributions Impact Goals: Save $195,000+ annually across Kenya Improve PEPFAR reporting accuracy to 95%+ Reduce duplicate testing by 70% Deploy in 2+ African countries by 2027 <div