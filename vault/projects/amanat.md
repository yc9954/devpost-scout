---
slug: "amanat"
url: "https://devpost.com/software/amanat"
title: "Amanat: Data Governance AI Agent"
hackathon: "Authorized to Act: Auth0 for AI Agents"
organization: "Okta"
winner: true
words: 5360
team_size: 1
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/benchmark_measured"
  - "mechanism/deterministic_policy"
  - "mechanism/human_in_the_loop"
  - "mechanism/on_device_local"
  - "mechanism/privacy_tech"
  - "mechanism/provenance_signing"
  - "mechanism/realtime_stream"
  - "mechanism/retrieval_grounding"
  - "mechanism/revocation_withdrawal"
  - "mechanism/structural_withholding"
  - "mechanism/vision_ocr"
  - "mechanism/voice_speech"
  - "domain/civic_government"
  - "domain/developer_tools"
  - "domain/disaster_emergency"
  - "domain/education"
  - "domain/health_clinical"
  - "domain/housing_homeless"
  - "domain/immigration_refugee"
  - "domain/labor_employment"
  - "domain/security_privacy"
  - "domain/transportation"
  - "user/frontline_worker"
  - "user/government_staff"
  - "user/social_worker"
  - "substrate/code_repository"
  - "substrate/document_pdf"
  - "substrate/geospatial"
  - "substrate/medical_record"
  - "substrate/regulation_legal_text"
  - "substrate/sensor_telemetry"
  - "substrate/structured_db"
  - "substrate/video_visual"
  - "substrate/web_dom"
---

# Amanat: Data Governance AI Agent

> Privacy-first AI agent for humanitarian organizations that scans cloud services for sensitive data exposure and fixes it, powered by Auth0 Token Vault and IBM Granite 4.

[Devpost](https://devpost.com/software/amanat) · hackathon [[Authorized to Act- Auth0 for AI Agents]]

## Facets

**mechanism** [[benchmark_measured]] [[deterministic_policy]] [[human_in_the_loop]] [[on_device_local]] [[privacy_tech]] [[provenance_signing]] [[realtime_stream]] [[retrieval_grounding]] [[revocation_withdrawal]] [[structural_withholding]] [[vision_ocr]] [[voice_speech]]
**domain** [[civic_government]] [[developer_tools]] [[disaster_emergency]] [[education]] [[health_clinical]] [[housing_homeless]] [[immigration_refugee]] [[labor_employment]] [[security_privacy]] [[transportation]]
**user** [[frontline_worker]] [[government_staff]] [[social_worker]]
**substrate** [[code_repository]] [[document_pdf]] [[geospatial]] [[medical_record]] [[regulation_legal_text]] [[sensor_telemetry]] [[structured_db]] [[video_visual]] [[web_dom]]

**stack** auth0, chainlit, granite, strands

## How they structured the write-up

- demo video
- screenshots
- published app
- auth0 features used
- inspiration
- what it does
- how i built it
- challenges i ran into
- accomplishments i'm proud of
- what i learned
- why this matters beyond the demo
- what's next for amanat
- scope and limitations
- tech stack
- references
- bonus blog post: three days, three token vault breakthroughs, one invalid_auth that changed everything

## Body

Auth0 Universal Login with MFA. Users authenticate once, then connect OneDrive, Outlook, and Slack individually via Token Vault. Scanned Outlook for emails with beneficiary data sent externally. Found violations, sent data protection alerts to sender and recipient. Slack scan found PII across 3 public channels. Table shows affected channels, PII types detected, and alerts posted to each one. Full scan output: names, case numbers, medical data, GPS coordinates, and file attachments flagged. Recommendations and tool calls shown. CIBA step-up for permissions revoking Redacted 47 PII instances from the displaced persons registry. Uploaded REDACTED copy to OneDrive and notified #data-governance. Tool call details: scan found the file, redact_file replaced all PII with labels, uploaded clean copy to the same OneDrive folder. After redaction, the agent posted a summary to #data-governance via notify_channel. JSON response confirms successful delivery. Asked about ICRC retention rules for biometric data. Agent cited the actual Handbook text, retrieved via BM25 from parsed PDFs. The Remediate workflow profile with starter actions: lock down files, prepare redacted copies for donors, alert Slack, download locally. Amanat: Privacy-First Data Governance Agent for Humanitarian NGOs Author: Adam Munawar Rahman, April 2026 Amanat connects to your OneDrive, Slack, and Outlook through Auth0 Token Vault, scans for sensitive beneficiary data that's been overshared or exposed, and helps fix it. Token Vault handles multi-service credential management so the agent acts across all three without storing raw tokens. IBM Granite 4 Micro runs the analysis locally, so beneficiary data never leaves the device. For organizations handling refugee case files and GBV reports, you need both of those things or the tool is unusable. Amanat (Arabic: trust, stewardship), the concept that what is entrusted to you must be protected and returned faithfully. Demo Video The 3-minute demo video shows Amanat running locally against my personal Microsoft 365 and Slack accounts, connected via Auth0 Token Vault. The OneDrive folders, Outlook inbox, and Slack workspace shown in the video are real accounts populated with synthetic humanitarian data from the Waqwaq scenario. All scans, remediations, CIBA step-up auth, and alerts execute live against the Microsoft Graph and Slack APIs. The video is sped up in places to fit the 3-minute window. Screenshots Slack scan: PII detected across public channels, alerts posted automatically Redaction: 47 PII instances removed, clean copy uploaded to OneDrive Policy RAG: ICRC Handbook cited on biometric data retention CIBA step-up auth: Guardian push notification for destructive actions Published App The published app at https://msradam-amanat.hf.space uses IBM watsonx.ai to host the same Granite 4 model that runs locally via llama-server in the video demo. watsonx is used here for deployment convenience (GPU inference without self-hosting), but the architecture is identical: Strands agent with tool calling, same system prompt, same 14 tools. Auth0 login works. Tools return synthetic demo data (the full experience requires the user's own OneDrive, Slack, and Outlook connected via Token Vault). All synthetic data is open and auditable in the repo . To run locally against live services, clone the repo and follow the setup instructions in the README. Auth0 Features Used Feature How Amanat Uses It Universal Login Single sign-on with Guardian MFA push notifications Token Vault (Connected Accounts) Federated token exchange for OneDrive, Slack, Outlook. Per-service scoping. MRRT across My Account API and all providers CIBA (Backchannel Authentication) Guardian push to user's phone before revoking sharing or deleting files. POST /bc-authorize with binding message. Agent polls until approved Guardian MFA Push notifications for both login MFA and CIBA step-up auth on destructive actions Inspiration In 2021, UNHCR collected biometric data (fingerprints and iris scans) from 830,000 Rohingya refugees in Bangladesh. The refugees were told registration was required to receive food. What they weren't told was that their data would be shared with the Myanmar government, the very regime they had fled. Some discovered their names on Myanmar's repatriation lists. Biometric data is immutable. Once shared, it can never be taken back (Human Rights Watch, 2021). Nobody hacked UNHCR. The data was shared through internal processes, on shared drives, with default settings that nobody reviewed. A governance failure. UNHCR's own data protection policy requires telling people, in a language they understand, why their data is being collected and whether it will be transferred. Of 24 refugees HRW interviewed, all but one said they were never informed of potential data sharing with Myanmar. UNHCR never carried out a data impact assessment, breaching its own rules (HRW, 2021). This keeps happening. In 2016, the UN's Office of Internal Oversight Services found that three of five UNHCR missions they investigated had shared refugees' personal data with host governments without assessing data protection or establishing transfer agreements (OIOS, 2016). In January 2022, attackers exploited an unpatched vulnerability to access personal data of 515,000 people in the ICRC's Restoring Family Links programme, which helps people separated from families by conflict, migration, and disaster. The attackers were inside for 70 days before anyone noticed. The programme had to be shut down entirely (ICRC, 2022). Humanitarian organizations handle refugee case files, GBV incident reports, biometric enrollment logs, medical records of displaced persons. And field teams routinely store this data on cloud services with default sharing settings. A GBV report shared with "anyone with the link." Case numbers posted in public Slack channels. Beneficiary names and HIV status in a donor report email. "The Data of the Most Vulnerable People is the Least Protected" — Human Rights Watch, 2023 The ICRC published a 400-page Handbook on Data Protection in Humanitarian Action. The IASC published Operational Guidance on Data Responsibility (2023). The Sphere Standards include Protection Principles for sensitive information handling. The policy documents exist. Nobody has built software that enforces them. The tools humanitarian organizations actually use (KoBoToolbox for data collection, DHIS2 for health data, Microsoft 365 for everything else) have baseline security (encryption in transit, optional encryption at rest, basic RBAC) but no automated data classification, no sensitivity detection, no cross-platform governance, no policy enforcement. A CyberPeace Institute study found that 41% of NGOs had been attacked in the past three years, only 4% had actionable cybersecurity policies, and 56% had no cybersecurity budget at all (CyberPeace, 2024). A Dalberg/ICRC joint study found fewer than half of humanitarian organizations had data protection policies meeting international standards (ICRC Handbook, 2020). I built Amanat to fill that gap. What It Does You log in through Auth0, connect your OneDrive, Slack, and Outlook via Token Vault, and tell the agent what to look for. It scans your files, messages, and emails for PII, checks what's publicly shared, cites the relevant ICRC or GDPR section, and can revoke sharing links or redact files on the spot. Why These Three Services UNHCR deployed Microsoft 365 across its field operations, making OneDrive and Outlook the default file storage and email for the world's largest refugee agency. WFP, UNICEF, and dozens of implementing partners followed. Slack (and increasingly Teams) became the coordination layer. The NetHope consortium, which provides IT infrastructure for 60+ major international NGOs, has documented the shift to cloud messaging platforms across the sector. Sensitive data flows across all three every day, and nothing watches the gap between them. Amanat connects to all three via Token Vault because that's where the data actually is. Capabilities Capability Description Multi-service scanning Recursively crawls OneDrive folders, searches Slack messages and file attachments, scans Outlook emails Hybrid PII detection Two-layer approach: deterministic regex for structural patterns + Granite 4 Micro for contextual/multilingual extraction Policy grounding RAG pipeline with BM25 retrieval over 1,059 chunks extracted from actual ICRC Handbook, IASC Guidance, GDPR, and Sphere Handbook PDFs Remediation Revoke sharing links, redact PII for safe sharing, download before delete, generate DPIAs, check consent documentation CIBA step-up auth Destructive actions trigger a Guardian push notification via CIBA; user approves on their phone before the agent proceeds. Falls back to in-UI dialog if Guardian unavailable Document parsing Upload scanned PDFs/DOCX/XLSX; Docling with granite-docling-258M VLM extracts text via OCR, then scans for PII Slack alerting Posts data protection warnings to channels where PII leaks are detected Encrypted audit trail Every scan and remediation action logged, encrypted at rest with Fernet/PBKDF2 Tools 14 functions the agent can call: Tool Purpose Example Query scan_files Scan OneDrive files for PII and sharing violations "Scan my files for sensitive data" search_messages Search Slack/Outlook for PII in messages "Search Slack for case numbers" detect_pii Deep PII scan on a specific file "What PII is in the displaced registry?" check_sharing Check who has access to a file "Who can see the GBV reports?" revoke_sharing Remove public/link-based sharing "Lock down the biometric files" redact_file Redact PII and upload clean copy to OneDrive "Redact the registry and upload the safe version" download_file Download to local storage "Download the GBV reports locally" delete_file Move to trash (with pre-delete download) "Remove the biometric data from cloud" retention_scan Check for retention policy violations "Which files have exceeded retention?" generate_dpia Generate Data Protection Impact Assessment "DPIA for our biometric enrollment" check_consent Verify consent documentation "Is our consent compliant?" notify_channel Post data protection alert to Slack "Warn the team about the PII leak" send_email Send data protection alert email "Email the sender about the violation" parse_document OCR and scan uploaded documents Drag-and-drop a scanned PDF Demo Scenario The demo uses a fictional humanitarian scenario: Post-Cataclysm Waqwaq. The Waqwaq Relief Authority (WRA) responds to a displacement crisis on a fictional archipelago. The setting is fictional but the data governance patterns are real. All synthetic demo data is committed to the GitHub repo at demo-data/drive/ , organized into the same folder structure used on OneDrive. Demo files across OneDrive ( /WRA Operations/ ): Folder Files Violations /Beneficiary Records/ Cataclysm_Displaced_Registry_2026.csv PII: names, case IDs, medical history, GPS /Protection/ GBV_Incident_Reports_2026.csv, GBV scanned PDF PUBLIC sharing — CRITICAL /Biometric Data/ Enrollment log, consent form, verification log PUBLIC sharing — CRITICAL ; special category data /Field Operations/ Staff contacts, site register Staff PII /Donor Relations/ Donor report Cross-references beneficiary case IDs /Scanned Documents/ Registration form (image-only PDF) Requires Docling OCR to extract PII How I Built It Full technical breakdown in ARCHITECTURE.md . Key sections below. Auth0 Integration Token Vault (Connected Accounts) The user authenticates once via Auth0 Universal Login, then connects each service separately through Connected Accounts. Each connection is its own OAuth consent screen, so the user sees exactly which permissions they're granting, and can disconnect any service without affecting the others. Amanat exchanges Auth0 refresh tokens for service-specific access tokens via federated token exchange: POST /oauth/token grant_type=urn:auth0:params:oauth:grant-type:token-ex