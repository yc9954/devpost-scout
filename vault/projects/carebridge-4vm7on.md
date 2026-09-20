---
slug: "carebridge-4vm7on"
url: "https://devpost.com/software/carebridge-4vm7on"
title: "Handoff"
hackathon: "Slack Agent Builder Challenge"
organization: "Salesforce"
winner: true
words: 1121
team_size: 1
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "mechanism/runtime_tool_creation"
  - "domain/developer_tools"
  - "domain/elder_child_care"
  - "domain/health_clinical"
  - "domain/labor_employment"
  - "domain/mental_health"
  - "user/clinician"
  - "user/general_public"
  - "user/patient_family"
  - "user/social_worker"
  - "substrate/document_pdf"
  - "substrate/medical_record"
  - "substrate/structured_db"
---

# Handoff

> Handoff is your Care Home Coordinator built inside Slack. It replaces sticky notes, binders, and text messages used in coordinating elderly care, where missed care handoffs cost a lot more than time.

[Devpost](https://devpost.com/software/carebridge-4vm7on) · hackathon [[Slack Agent Builder Challenge]]

## Facets

**mechanism** [[realtime_stream]] [[runtime_tool_creation]]
**domain** [[developer_tools]] [[elder_child_care]] [[health_clinical]] [[labor_employment]] [[mental_health]]
**user** [[clinician]] [[general_public]] [[patient_family]] [[social_worker]]
**substrate** [[document_pdf]] [[medical_record]] [[structured_db]]

**stack** amazon-web-services, anthropic-sdk, apscheduler, aws-ecr, aws-ecs-fargate, claude, docker, ecr, github-actions, google-calendar, google-drive-api, model-context-protocol-(mcp), python, slack-agents

## How they structured the write-up

- what it does
- why?
- inspiration
- how i built it
- challenges i ran into
- accomplishments that i am proud of
- what i learned
- what's next for handoff

## Body

What it does Handoff is an AI-powered care coordination assistant for residential elder care homes, built inside Slack. Personal support workers, nurses, and care coordinators, interact with it the same way they'd message a colleague. They log care events in natural language - for example, "Angela seemed confused this morning, she kept asking where she was", and Handoff structures, stores, and surfaces that information intelligently. At the end of a shift, staff can handoff their day of events to the incoming staff so that they have up-to-date info on their patients. Why? To improve quality of care, reduce critical errors, like medication mistakes, and make coordination easier among care workers. Care homes need a coordination layer that exists where care home staff already communicate. They need one place that actually remembers, thinks, and acts so the staff don't have to hold everything in their heads. What if that one place was Slack, enhanced with the right app? Key capabilities: Intelligent care logging : staff post naturally in #care-updates. Handoff converts those into structured records (medications, symptoms, appointments, incidents, observations) and reacts with an emoji to confirm. Staff can continue having a conversation afterwards, and Handoff will respond intelligently. Shift handoff as a Canvas : /handoff generates a structured, per-resident handoff document posted as a persistent Slack Canvas, so incoming staff always have a complete picture of the previous days' events. Staff Q&A : staff ask natural language questions and Handoff searches channel history across several channels via the Slack RTS API and combines it with database records to provide a detailed search. Resident intake : /intake accepts a Google Drive discharge PDF and extracts diagnosis, medications, care requirements, and appointments, and auto-books everything in Google Calendar. Family notifications : staff can ask Handoff to notify 1) a resident's family, 2) on-call staff and will draft a compassionate or clinical message respectively, as well as initialize a triage channel. These interactions are all orchestrated via an agentic Slack MCP workflow between Slack and Anthropic. Reminder system : natural language reminders with escalation to the charge nurse if unacknowledged Role-aware agent panel : built on Slack's native AI Agent feature. Staff get shift summaries and Q&A, family members get a scoped view of only their loved one. Resident dashboard : a live Home tab showing all residents, flagged concerns first, refreshed on every visit Inspiration Large health systems have deep pockets and are able to use modern electronic medical records systems. They can easily and reliably record everything related to their patients' care. At the other end of that spectrum are care homes. My grandparents spent their last days in care homes that needed my presence all the time to ensure appointments weren't missed and medications were correct. It filled me with anxiety constantly. It was an illuminating experience. After many years though, what struck me wasn't really negligence of anyone. The staff were caring people, all working a brutal shift under real pressure. Could it have been the system they were using? Sticky notes, verbal hand-offs at the end of the (tiring) day, and no one source of truth for what had happened and what still needed to happen. Care homes need a coordination layer that exists where care home staff already communicate. They need one place that actually remembers, thinks, and acts so the staff don't have to hold everything in their heads. What if that one place was Slack, enhanced with the right app? How I built it Handoff is a Python application using Slack Bolt in socket mode. It uses Supabase (Postgres) and is deployed to AWS ECS Fargate via GitHub Actions. The AI layer uses the Claude API, with structured tool-use for logging events, answering questions, setting reminders, and orchestrating workflows. The Slack MCP sever used is used via a fully agentic notification workflow where Claude Haiku discovers and sequences Slack tools at runtime from their descriptions alone. For example, Haiku determines which Slack tools to use and interacts back and forth with the Slack MCP server via Handoff to start chats, write messages to Slack users, or create and post to channels - no hardcoding. Slack AI features used: Slack MCP As noted above, the Slack MCP server is used for orchestration of activities during broad notification sequences. When a staff member wants to notify "everyone" (which could be configurable, as a next step), interactions between Claude and Slack MCP control the creation of chats and channels and posting of messages. Native AI Agent / Assistant panel with role-aware suggested prompts Real-Time Search API for keyword search over channel history (#care-updates and #incidents, but more could be added) to surface informal staff notes that structured DB queries would miss. Challenges I ran into I strongly considered concerns around PHI/PII handling in this context but in a hackathon setting, assumed we could defer those. I built all of this myself. I had SO much fun - but I had to learn how to use video editing software and how to record my voice too. I'm happy I entered. Role-aware access had to be implemented without adding friction for the demo. The solution was treating users as staff and only scoping family members based on a family_members table. This required careful gating across slash commands/Q&A/Assistant panel simultaneously. Accomplishments that I am proud of Getting AI-driven reasoning agentically over live tool descriptions for the Slack MCP, felt like a real demonstration of what MCP makes possible. Nothing was hard-coded to make the "@handoff notify everyone about <...>" workflow work. The shift handoff is a feature I'm pretty proud of and is what this app is centered around, hence the name. The /handoff command reads eight hours of care events, checks pending reminders, grabs today's calendar appointments, and creates a structured per-resident summary a formatted Canvas document, is the kind of thing that could genuinely change someone's last ten minutes of a difficult shift. What I learned Frankly, I learned a lot about building Slack agents, and what features Slack as. The organization I work for full-time uses Slack, and I'm now much more equipped to lead my teams in building Slack integrations. What's next for Handoff I see the following as logical next steps: EHR integration : connect to Epic or other EHRs via their APIs, so Handoff becomes a Slack interface to the system of record rather than a parallel one. Expanded family access : a daily digest, appointment notifications, and the ability for family to respond to Handoff's messages and have their questions answered. I'm thinking not just read-only, but a two-way channel between families and the care team. I really enjoyed working on this hackathon project and thank you for the opportunity to demonstrate my skills! <div