---
slug: "hospital-inpatient-discharge-journey"
url: "https://devpost.com/software/hospital-inpatient-discharge-journey"
title: "Transparency in Treatment"
hackathon: "Tableau Next Virtual Hackathon"
organization: "Tableau"
winner: true
words: 826
team_size: 2
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/retrieval_grounding"
  - "mechanism/simulation_digital_twin"
  - "domain/elder_child_care"
  - "domain/health_clinical"
  - "user/clinician"
  - "user/patient_family"
  - "substrate/medical_record"
  - "substrate/regulation_legal_text"
  - "substrate/structured_db"
  - "substrate/video_visual"
---

# Transparency in Treatment

> Being stuck in a hospital room without answers is more than annoying, it erodes trust. Our solution brings transparency to the discharge process, improving patient satisfaction and care team morale.

[Devpost](https://devpost.com/software/hospital-inpatient-discharge-journey) · hackathon [[Tableau Next Virtual Hackathon]]

## Facets

**mechanism** [[retrieval_grounding]] [[simulation_digital_twin]]
**domain** [[elder_child_care]] [[health_clinical]]
**user** [[clinician]] [[patient_family]]
**substrate** [[medical_record]] [[regulation_legal_text]] [[structured_db]] [[video_visual]]

**stack** agentforceapi, datacloudapi, faker, modelsapi, next.js, python, shadcn, tableaunextrestapi, tailwindcss, typescript, vercel

## How they structured the write-up

- inspiration
- assumptions / constraints
- what it does
- how we built it
- challenges we ran into
- accomplishments we're proud of
- what we learned
- what's next for transparency in treatment
- test out our app!

## Body

Patient Portal Dashboard shows patient demographics, care team, treatment progress, diagnosis, and department status. Agentforce Health Assistant summarizes imaging results, diagnosis, and treatment. Agentforce Health Assistant is aware of the hospital's department capacity, providing insight into how that impacts the patient's care. Patient Care Team Dashboard Overview - pinging AI agent for summary stats. Patient Care Team Department Details Inspiration This project was inspired by a recent hospitalization of a loved one, where we endured a confusing and delayed inpatient discharge process. As family members, we often felt lost and unsure: What are we waiting for? Who needs to sign off? What’s happening behind the scenes? We weren’t alone as other patients around us shared the same frustration. At times, it felt like we had been forgotten. Our goal with this project is to establish transparency and restore trust for the patient. Most of the tools and platforms built in Healthcare are focused on the clinical care team so we built a solution that brings transparency to the patient regarding their hospital inpatient journey. By leveraging Agentforce, Data Cloud, and Tableau Next APIs, we show how the patient experience can be elevated. Additionally, we show how hospital care teams can anticipate staffing needs with Tableau Next dashboards. Assumptions / Constraints All data was simulated and does not reflect any real individuals or hospital systems. Data was generated solely for demonstration purposes. Hospital discharge process and workflows have been modeled in a linear fashion for clarity (real-world workflows are non-linear, involving much more complex dependencies and intricacies). Solution models two core user perspectives for demonstration purposes: 1. Patient or their family/caregiver 2. Care team member (nurse, case manager, unit manager combined) Solution is intentionally focused on patient-facing uncertainties, not on clinical decision-making or clinical use of AI. What it does For patients and their families: Sets clear expectations of what's happening during treatment and what's up next via step-by-step "Treatment Progress" tracker AI Assistance in drafting messages / questions to care teams regarding imaging/lab results and procedures Context-aware AI assistant offering plain-language explanations of diagnoses, procedures, and discharge criteria for better understanding For care teams: Snapshot summary of incoming patients and those ready to be discharged Forecast of staffing needs per department and by readmission risk How we built it The Patient Portal was built with Next.js, Tailwindcss, Vercel, and Typescript. The Healthcare AI assistant uses the Agentforce/Models API to generate health-related summaries, descriptions, and context. The Patient Portal is connected with Data Cloud API to display the simulated data, and uses the Tableau Next REST API to show a static image of the Tableau Next dashboard. Challenges we ran into Challenge Resolution Embedding API limitations Since the embedding API doesn't support Tableau Next dashboards yet, we pivoted to use a static image from the Tableau Next REST API. Visualization limitations & errors Tableau Next doesn't yet support all chart types (e.g., full Gantt or dynamic timeline visuals). We worked around these gaps using calculated fields, stacked bars, and labels to simulate timing and flow. Realistic synthetic data generation It was tricky to generate patient data that reflected the nuances of a hospital discharge process. We went through multiple schema iterations to ensure the data supported meaningful and accurate visualizations. Balancing user needs Patients need more visibility in the hospital process whereas care teams need less disruptions to work with. With this in mind, we designed primarily for patient visibility and care team simplicity. Confusion with project requirements Since this was our first Hackathon, we felt confused about what the Hackathon's project guidelines and requirements were asking for. We ended up building our vision and incorporating Tableau Next elements where appropriate. Accomplishments we're proud of Our project is anchored in a real-life hospitalization experience where we wished we had an app or tool to give us visibility during the inpatient stay. We implemented a context-aware AI assistant with Agentforce, transforming mundane interactions into personalized, encouraging conversations. Our AI assistant is aware of the patient's history regardless of what view/page they're on, and is able to generate summaries and trends for the patient. We built something that we'd actually want to use as a patient or caregiver in a real hospital setting. What we learned Capabilities of Agentforce and Salesforce Data Cloud Connecting our external web app with Salesforce Data Cloud and Agentforce APIs & Tableau Next REST APIs What's next for Transparency in Treatment Import more data and connect to a robust database to simulate realistic hospital setting where data comes from multiple hospital management systems, e.g. OpenEMR Leverage embedding API in the future when it is available for use with Tableau Next Build out more detailed dashboard / user journey for the patient care team to perform forecasting of staffing needs Build out Agent Flows for patient care team to interact with Dashboards Review HIPAA guidelines and regulations to confirm compliance Test out our app! Try out our patient view application! user: patient-demo pw: 3EV7zfIAJvpC*@u <div