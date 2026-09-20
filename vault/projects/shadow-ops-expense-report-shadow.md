---
slug: "shadow-ops-expense-report-shadow"
url: "https://devpost.com/software/shadow-ops-expense-report-shadow"
title: "Shadow Ops - Expense Report Shadow"
hackathon: "Amazon Nova AI Hackathon"
organization: "Amazon"
winner: true
words: 717
team_size: 0
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/human_in_the_loop"
  - "mechanism/provenance_signing"
  - "mechanism/realtime_stream"
  - "mechanism/vision_ocr"
  - "domain/developer_tools"
  - "domain/retail_commerce"
  - "user/small_business"
  - "substrate/financial_record"
  - "substrate/video_visual"
---

# Shadow Ops - Expense Report Shadow

> Upload a receipt photo. Nova 2 Lite extracts the data and infers the workflow. Nova Act opens a cloud browser and fills the real expense form. Receipt in, expense submitted out.

[Devpost](https://devpost.com/software/shadow-ops-expense-report-shadow) · hackathon [[Amazon Nova AI Hackathon]]

## Facets

**mechanism** [[human_in_the_loop]] [[provenance_signing]] [[realtime_stream]] [[vision_ocr]]
**domain** [[developer_tools]] [[retail_commerce]]
**user** [[small_business]]
**substrate** [[financial_record]] [[video_visual]]

**stack** amazon-bedrock, amazon-cloudfront, amazon-ecr, amazon-nova-2-lite, amazon-nova-act, amazon-web-services, aws-app-runner, docker, fastapi, python, react, terraform, typescript, vite

## How they structured the write-up

- inspiration
- what it does
- how i built it
- amazon nova services used
- challenges i ran into
- accomplishments i'm proud of
- what i learned
- what's next

## Body

Inspiration Expense reporting is universally hated. Employees spend 20+ minutes per report filling the same forms with the same data that's already on their receipts. I asked: what if an AI could look at a receipt, figure out what needs to happen, and do it — filling the actual form in a real browser? What it does Shadow Ops automates the entire expense submission pipeline: Snap — Upload a receipt photo from your phone or desktop. Extract — Amazon Nova 2 Lite reads the receipt and extracts amount, merchant, date, category, and currency using multimodal AI. Infer — The same model analyzes the extracted data and infers a complete automation workflow: what fields to fill, in what order, with what values. Approve — A human reviews the inferred workflow and approves it (human-in-the-loop safety gate). Automate — Amazon Nova Act opens a cloud browser, navigates to the expense form, fills in every field, selects the right dropdown values, clicks Submit, clicks Confirm, and returns the confirmation ID. The agent is self-healing: if a UI element changes (e.g. "Submit" is renamed to "Confirm"), it detects the failure, adapts its approach, and retries automatically. How I built it Backend : FastAPI (Python 3.12) with Pydantic v2 models, structlog JSON logging, and two Nova integration layers: nova_client.py wraps Bedrock's InvokeModel for both text and multimodal Nova 2 Lite calls. act_client.py uses the Nova Act SDK with Workflow context manager for IAM-authenticated cloud browser automation. Frontend : React + TypeScript + Vite. Features a receipt upload with drag-and-drop, workflow approval flow, and an agent execution modal with live polling timer that shows real-time status as Nova Act fills forms. Infrastructure : Terraform-managed AWS stack — App Runner (backend), S3 + CloudFront (frontend), ECR (container registry), IAM roles with Bedrock + Nova Act permissions. Async pattern : Nova Act takes 2-4 minutes. I use background threads with a polling API to stay within App Runner's 120-second request timeout while showing live progress to the user. Amazon Nova services used Service Usage Mode Amazon Nova 2 Lite (Bedrock) Multimodal receipt OCR + text workflow inference Real (Bedrock InvokeModel) Amazon Nova Act Cloud browser automation — fills forms, clicks buttons, extracts results Real (SDK + Workflow/IAM auth) Challenges I ran into Nova Act parameter inconsistency : The boto3 nova-act service model uses name for CreateWorkflowDefinition but workflowDefinitionName for GetWorkflowDefinition . I built runtime introspection to detect the correct parameter per operation. App Runner 120-second timeout : Nova Act runs take 2-4 minutes. I implemented an async execution pattern with background threads and a polling API. Infinite loop bug : The inferred workflow's first step was "Navigate to the dashboard" — but the browser already starts on the form page, and the Dashboard link was a dead anchor. Nova Act kept clicking it forever. I solved this with intent-based step skipping and instruction enhancement. Date input formatting : Nova Act initially typed "2025-02-21" into a date field, but the browser expected MM/DD/YYYY. The model learned from its mistake and self-corrected to "02/21/2025" on the next attempt. Accomplishments I'm proud of Full dual-Nova pipeline : Receipt photo → Nova 2 Lite OCR → Nova 2 Lite inference → Human approval → Nova Act browser automation → Confirmation ID. Few teams use both services together. Self-healing agent : Detects and adapts to UI changes in real-time. Production deployment : Not just localhost — fully deployed on AWS with Terraform IaC. Instruction enhancement : Generic inferred steps are automatically rewritten with page-specific context before execution. What I learned Nova Act is remarkably good at understanding form layouts and making decisions about what to click/type. It handles dropdown redirects, date format conversions, and confirmation modals without explicit programming. Prompt engineering with strict output format guards (first char { , last char } ) dramatically improves JSON extraction reliability. The async execution pattern (background thread + polling) is essential for any real-world Nova Act integration behind a load balancer. What's next Recording mode : Capture real user actions in the browser to feed richer context to workflow inference. Multi-form support : Different expense systems (Concur, Expensify, custom portals) with form-specific instruction enhancement. Batch processing : Process a folder of receipt photos and submit all expenses in sequence. Audit trail : Store Nova Act browser session recordings for compliance review. <div