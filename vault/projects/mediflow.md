---
slug: "mediflow"
url: "https://devpost.com/software/mediflow"
title: "MediFlow"
hackathon: "TreeHacks 2024"
organization: "TreeHacks"
winner: true
words: 609
team_size: 4
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/voice_speech"
  - "domain/finance_payments"
  - "domain/health_clinical"
  - "domain/mental_health"
  - "user/clinician"
  - "user/government_staff"
  - "user/patient_family"
  - "user/social_worker"
  - "substrate/medical_record"
  - "substrate/structured_db"
  - "substrate/transcript_audio"
---

# MediFlow

> Automating healthcare's tedious administrative tasks to save hospitals $265.6 billion yearly and prevent the closure of over 30% of rural hospitals in America, allowing them to focus on patient care.

[Devpost](https://devpost.com/software/mediflow) · hackathon [[TreeHacks 2024]]

## Facets

**mechanism** [[voice_speech]]
**domain** [[finance_payments]] [[health_clinical]] [[mental_health]]
**user** [[clinician]] [[government_staff]] [[patient_family]] [[social_worker]]
**substrate** [[medical_record]] [[structured_db]] [[transcript_audio]]

**stack** clerk, convex, monsterapi, openai, react, typescript, vercel, whispir

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for mediflow

## Body

Inspiration We have firsthand knowledge from our close family and friends who are doctors serving in rural communities across America. They have shared with us their experiences of burnout due to the extensive manual back-office tasks they are required to handle, such as patient pre-authorization claims (PAs), in addition to their primary responsibility of serving their patients. Upon conducting further research, we have discovered that this is not just an isolated issue within our circle but rather a systemic problem that plagues the entire hospital industry. Today, administrative complexity is costing the healthcare industry a staggering $265.6 billion annually. Furthermore, over 30% of the country's rural hospitals are at risk of closure due to financial instability, with a projected increase of 16% in the year 2023. If these hospitals close down, over ~57M Americans will be without care. Moreover, according to an AMA 2022 Physician Survey, 88% of physicians say burnout associated with PA is extremely high, and 34% report that PAs led to serious adverse events for patient care due to insurance rejections preventing needed care. What it does MediFlow automates back-office administrative work for hospitals, focusing on workflow experience and exacerbated in rural hospital environments. MediFlow seeks to be both a core system of record for electronic health records and a vertical AI tool that leverages proprietary hospital data to enhance. In this vein, MediFlow currently offers tools to automate 3 hospital administration processes. Prior Authorization. MediFlow can shorten the process of requesting prior authorization from insurance companies, i.e. approval for treatment/pharmaceutical coverage, from weeks to minutes by reducing the error rate of this manual process. By taking in information from the EHR and using LLMs to generate likely treatment codes, a process that normally takes staffers 45 minutes to even complete can be done in <3 minutes. Patient-Meeting Summaries. Using OpenAI’s Whisper, MediFlow can summarize doctor meetings and store summaries in an object store for future use when initiating prior authorization requests. Patient Intake and Client Relationship Management. MediFlow enables easy patient intake for new and recurring patients as well as a top-down view of a hospital’s clientele. How we built it We used Convex as our database and its serverless functions to build the backend for our app. We finetuned llama’s 13bn parameter LLM model with 1,200 examples of doctor-patient summaries with MonsterAPI’s ML fine-tuning suite. We also used MonsterAPI’s hosted Whisper endpoint for voice transcription. To handle unstructured data for prior authorization, we used OpenAI’s GPT3 API and prompt engineering to retrieve siloed information from noisy data. We used React and TypeScript in a node environment to build out our friend end with Turbo as a tool to manage our mono repo. Finally, we used Clerk for user authentication and log in our platform. Challenges we ran into Defining the specific products we wanted to build was challenging as the medical space was large and something we were unfamiliar with. We ran into issues configuring our convex environment initially and found working with different insurance health codes extremely difficult and confusing. Additionally, it was difficult to find datasets to fine-tune our models and ensure high accuracy in our highly-context dependent environment. Accomplishments that we're proud of We’re proud of building out multiple features instead of the initial tool we set out to build. We’re proud of building a multi-modal AI solution on top of a traditional enterprise software platform and effectively resolving a challenge faced by rural hospitals. What we learned We learned how to fine-tune models, how voice diffusion and transformer models work, and the medical workflow process for doctors and rural hospitals. What's next for MediFlow Convex Cron functions Go multiproduct <div