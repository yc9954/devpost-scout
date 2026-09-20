---
slug: "theramind"
url: "https://devpost.com/software/theramind"
title: "TheraMind"
hackathon: "TreeHacks 2025"
organization: "TreeHacks"
winner: true
words: 1074
team_size: 4
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "domain/developer_tools"
  - "domain/health_clinical"
  - "domain/mental_health"
  - "user/patient_family"
  - "substrate/document_pdf"
  - "substrate/sensor_telemetry"
  - "substrate/structured_db"
---

# TheraMind

> Less paperwork, more patient care: the AI therapist's assistant.

[Devpost](https://devpost.com/software/theramind) · hackathon [[TreeHacks 2025]]

## Facets

**mechanism** [[realtime_stream]]
**domain** [[developer_tools]] [[health_clinical]] [[mental_health]]
**user** [[patient_family]]
**substrate** [[document_pdf]] [[sensor_telemetry]] [[structured_db]]

**stack** dain, python, scrapybara, typescript

## How they structured the write-up

- inspiration
- what theramind does
- how we built theramind
- challenges we faced
- accomplishments that we're proud of
- what we learned
- what's next for theramind

## Body

Inspiration Our inspiration for TheraMind stems from the growing mental health crisis and the challenges therapists face in meeting patient demand. 1 in 5 US adults experiences mental illness annually. Source — National Institute of Mental Health NIMH 46% of psychologists couldn't meet patient demand in 2022. Source — American Psychological Association (APA) 2022 COVID-19 Practitioner Impact Survey via APA Report 52% of therapists reported experiencing burnout in 2023. Source — SimplePractice 2023 Therapist Well-Being Report via Fierce Healthcare Burnout-related turnover costs healthcare organizations millions. Source — American Medical Association (AMA)via AMA Report Administrative burdens are a top burnout factor for 55% of therapists. Source — SimplePractice 2023 Therapist Well-Being Report via Fierce Healthcare Our guiding question, "How do we help therapists help their patients?" , emphasizes the dual focus of TheraMind: empowering therapists while enhancing patient care. By addressing the challenges therapists face—such as administrative burdens, burnout, and time constraints—TheraMind enables them to dedicate more energy to their patients. Through tools like data visualization, sentiment analysis, and streamlined meeting preparation, TheraMind bridges the gap between therapist efficiency and patient outcomes. What TheraMind Does Our AI workflow automator is designed to streamline therapists' daily tasks, reducing the cognitive load of managing appointments, patient communication, and progress tracking. With a simple prompt, therapists can instantly retrieve their upcoming appointments, ensuring they stay organized without sifting through calendars. The system also automates patient reminders, sending timely emails to reduce no-shows and keep clients engaged. Additionally, our tool provides a comprehensive summary of patient progress by analyzing survey responses and visualizing historical data, offering valuable insights at a glance. By handling these essential but time-consuming tasks, our solution allows therapists to focus on what truly matters—providing quality care to their patients. How We Built TheraMind DAIN — We used DAIN as our framework to tie together all the components into an integrated workflow. DAIN helped trigger various service tools, such as checking the therapist's appointment database, automatically sending reminder emails, and retrieving detailed patient information. By streamlining these tasks, our DAIN service allows for seamless data management and communication between systems. This automation greatly reduces the cognitive load on therapists, allowing them to easily track patient progress, manage contexts between different patients, and quickly identify necessary treatments by analyzing large amounts of data efficiently. This implementation not only improves efficiency but also contributes to a more organized and manageable workflow for therapists. Data Driven Insights with Scrapybara — We used Scrapybara as an AI agent to automate data scraping from therapists' Google Drive, specifically extracting patient survey files. By leveraging summarization and sentiment analysis, it helped therapists sift through large amounts of journal entries and survey responses, identifying key emotional patterns and helpful data-driven insights. This allows for more efficient workflow management and improved mental health support by highlighting trends in patient well-being without the therapist ever having to touch a line of code to deduce those insights. Sentiment Analysis — We applied sentiment analysis to patient journal entries by processing text data to detect emotional tone and classify sentiment. Using natural language processing (NLP) techniques, we extracted key mood indicators, assigning numerical mood scores based on word choice, context, and emotional intensity. These scores were aggregated to generate quantitative metrics, allowing therapists to track fluctuations in patient mood in between sessions. The data was then visualized in the DAIN framework through intuitive graphs and dashboards, enabling therapists to quickly identify trends, detect potential concerns, and make informed decisions about patient care. Perplexity — We conducted extensive background research on mental health to better understand the challenges faced by both patients and therapists. This research, which we conducted largely with Perplexity, highlighted the growing demand for mental health services, particularly in the face of rising stress, burnout, and other mental health issues among healthcare professionals. We explored existing mental health frameworks and tools, identifying gaps in support, especially in the way therapists manage patient data and track progress. Additionally, we investigated the needs of therapists, including the increasing pressure to manage large volumes of patient information and the need for effective tools to monitor patient well-being in real-time. Our findings reinforced the importance of creating solutions that can automate time-consuming tasks, reduce mental load, and provide personalized, actionable insights for both therapists and patients. This background research streamlined by Perplexity’s efficient search methods quickly got us up to speed with the problem space and laid the foundation for our work in integrating AI agents to streamline workflows and enhance mental health. Challenges We Faced One of the main challenges we encountered was slow performance, which would require further optimization to run efficiently in real time. Additionally, integrating the AI agent, understanding its capabilities, and interfacing with different systems proved to be complex, as we wanted to ensure seamless communication and data flow across various platforms. These challenges highlighted our focus on improved optimization strategies of AI agents and better interoperability between systems to achieve smoother and faster execution in the future. Accomplishments that We're Proud Of We’re proud of creating an intuitive and user-friendly interface that makes mental health support accessible. Successfully implementing AI-driven sentiment analysis and personalized journaling features was a major achievement. Seeing our idea come to life and knowing it could positively impact people’s well-being made the late-night debugging session worth it. What We Learned Through our exploration of AI agents in automated workflows applied to healthcare, we discovered the potential to significantly enhance efficiency by automating qualitative and quantitative data analysis tasks and supporting human collaboration. These agents can optimize decision-making and provide real-time insights, improving both productivity and well-being. We learned that AI can assist professions prone to burnout that greatly impact a wide range of patients, ultimately creating more accessible, inclusive, and balanced work environments. This integration of AI into workflows is transforming healthcare and workplaces at large, having a profound social impact on well-being by enabling smarter, more efficient processes that support professionals and improve lives. What's next for TheraMind Our vision for TheraMind is to expand its reach and impact by catering to new user groups who experience high levels of stress and emotional burnout. In the near future, we aim to tailor our AI-driven mental health support for medical professionals, project managers, educators, and more. By refining our AI’s ability to provide industry-specific emotional support and wellness insights, we can help these professionals navigate their daily lives more effectively and allow them to achieve peace of mind. <div