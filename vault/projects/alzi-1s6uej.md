---
slug: "alzi-1s6uej"
url: "https://devpost.com/software/alzi-1s6uej"
title: "Alzi"
hackathon: "DeveloperWeek 2024 Hackathon"
organization: "DevNetwork"
winner: true
words: 546
team_size: 4
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/voice_speech"
  - "domain/elder_child_care"
  - "domain/health_clinical"
  - "domain/labor_employment"
  - "domain/mental_health"
  - "user/clinician"
  - "user/educator_student"
  - "user/patient_family"
  - "user/social_worker"
  - "substrate/geospatial"
---

# Alzi

> Designed to assist individuals with Alzheimer's and their caregivers.

[Devpost](https://devpost.com/software/alzi-1s6uej) · hackathon [[DeveloperWeek 2024 Hackathon]]

## Facets

**mechanism** [[voice_speech]]
**domain** [[elder_child_care]] [[health_clinical]] [[labor_employment]] [[mental_health]]
**user** [[clinician]] [[educator_student]] [[patient_family]] [[social_worker]]
**substrate** [[geospatial]]

**stack** api, azure, django, openai, react

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for alzi

## Body

Inspiration The financial impact of Alzheimer's and other dementias is staggering, costing the nation an estimated $345 billion in 2023. Despite the growing prevalence and economic burden, there is a notable lack of specialized training among professionals, with only 4% of social workers holding certification in geriatric social work and a concerning trend where 97% of physicians report relying on patients or their families to initiate discussions about symptoms. This situation underscores the urgent need for comprehensive interventions and forward-thinking approaches. Such strategies should aim to enhance the quality of life for those with Alzheimer's and provide effective, informed support for their caregivers, whose role is indispensable yet under-recognized and under-supported in the current healthcare paradigm. What it does Alzi is a digital solution designed to revolutionize care for individuals with Alzheimer's and their caregivers. It features an AI-powered chatbot that tracks patients' behavior and mental health, offering regular updates on disease progression. This innovative app includes a voice assistant for easy interaction, tailored therapy schedules for cognitive exercises, and sophisticated chatbot interactions for patient engagement. Additionally, Alzi provides data-driven health analytics to assist caregivers in making informed decisions. Targeted at both Alzheimer's patients for cognitive support and caregivers for resources and guidance, Alzi aims to significantly enhance the management and quality of life in Alzheimer's care. How we built it We used React + Django to build the web app. Following is the tech used for Patient's and Caregiver's Interface: 1} Chatbot Prompt Engineering: Integrate increasingly detailed patient information and essential common sense as prompts in conversations and aid in memory improvement therapy Azure OpenAI (GPT-4, GPT-3.5) Azure AI Bot Voice Assistant Support: Transcribe speech to text, produce natural-sounding text-to-speech voices Azure Speech 2} Data-driven Health Analytics: Leverage textual data from chatbot conversations with patients to update the symptoms of Alzheimer and analyze therapy progression. Azure Stream Analytics Azure OpenAI Personalized Therapy Schedules: Develop subsequent therapy plans based on medical theories and analysis results. Azure Stream Analytics Azure OpenAI Regular Behavior Tracking: Track patient’s location when necessary Azure Maps Challenges we ran into Alzheimer's disease affects individuals differently, and understanding the diverse needs of patients, families, and caregivers is crucial. Developing an app that effectively addresses the varying symptoms, stages, and challenges of Alzheimer's requires thorough research and user feedback. Accomplishments that we're proud of Alzi is designed as a digital solution to revolutionize care for individuals with Alzheimer's and their caregivers, featuring an AI-powered chatbot for tracking patients' behavior and mental health status. It includes a voice assistant for easy interaction, tailored therapy schedules, and sophisticated chatbot interactions for patient engagement, aiming to enhance both the management and quality of life in Alzheimer's care. What we learned Understanding the diverse needs, abilities, and limitations of individuals with Alzheimer's and their caregivers is paramount. Designing solutions with a user-centric approach, incorporating usability testing, and gathering continuous feedback can ensure that the app addresses real-world challenges and meets the unique needs of its users effectively. What's next for Alzi Focusing on strategy development, partner establishment, content creation and dissemination, introducing in-app tutorials, enhancing user support, and initiating a free trial period. The plan includes evaluating feedback, iterative improvements, and planning for future expansion to ensure a methodical and impactful rollout of the Alzheimer's care app <div