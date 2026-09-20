---
slug: "health-story"
url: "https://devpost.com/software/health-story"
title: "Health Story"
hackathon: "TreeHacks 2023"
organization: "Stanford TreeHacks"
winner: true
words: 1046
team_size: 4
has_repo: true
has_live: false
has_video: false
tags:
  - "project"
  - "mechanism/voice_speech"
  - "domain/developer_tools"
  - "domain/health_clinical"
  - "user/clinician"
  - "user/developer"
  - "user/patient_family"
  - "substrate/code_repository"
  - "substrate/document_pdf"
  - "substrate/sensor_telemetry"
  - "substrate/structured_db"
  - "substrate/transcript_audio"
  - "substrate/web_dom"
---

# Health Story

> Introducing Health Story, our revolutionary app for hypertension management - a game-changer for doctors and patients alike. Say goodbye to piles of notes and medical errors!

[Devpost](https://devpost.com/software/health-story) · hackathon [[TreeHacks 2023]]

## Facets

**mechanism** [[voice_speech]]
**domain** [[developer_tools]] [[health_clinical]]
**user** [[clinician]] [[developer]] [[patient_family]]
**substrate** [[code_repository]] [[document_pdf]] [[sensor_telemetry]] [[structured_db]] [[transcript_audio]] [[web_dom]]

**stack** amazon-web-services, flask, python, vue

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- references and sources

## Body

Inspiration The inspiration behind building this app was to address the critical issue of medical errors in healthcare. According to a study by Johns Hopkins, medical errors are the third leading cause of death in the United States, after heart disease and cancer, with an estimated 250,000 deaths per year. These errors can occur due to various factors, including miscommunication and lack of complete patient information. Doctors have to go through piles of notes and patient histories, leading to time-consuming processes and increased risk of medical errors. By streamlining the conversation between doctors and patients and providing a clear overview of the patient's health status other relevant diagnosis information, Health Story aims to reduce the risk of medical errors and ultimately improve patient outcomes. Our mission is to make health management more efficient, effective, and safe for both doctors and patients. The following are the facts that show how extreme this problem is: Having hypertension puts you at risk for heart disease and stroke, which are leading causes of death in the United States. In 2020, more than 670,000 deaths in the United States had hypertension as a primary or contributing cause Only about 1 in 4 adults (24%) with hypertension have their condition under control. What It Does We built Health Story, a web app that combines cutting-edge tech with a human-centered approach to address the common challenges faced by doctors by providing a comprehensive overview of a patient's medical history in one place. Our app consists of multiple features as outlined below. Speech2SOAP Doctors and nurses spend countless hours in writing medical notes, and summarizing them into the SOAP format (S-Subjective, O-Objective, A-Assessment, P-Plan). With a live transcription feature, doctors can now focus on their patients instead of taking notes. This feature not only transcribes the conversation, but also converts the conversation into a medical SOAP format which summarizes the patient's history over the last few visits, providing doctors with a quick and clear understanding of the patient's health status. We are different from existing solutions as we help the doctors find correlations and information that they need but cant find easily. We solve the 'tell me something I didn't know' problem. Health Analyzer We also integrate an analytics dashboard into our app which depicts a trend in vital health metrics (blood pressure, heart rate, etc), and provide "smart" comments on the inflection points in the patient's health trend over time. This enables the doctors to make more informed decisions and improve patient outcomes without having to sift through countless pages of notes. Drugs It is crucial for the doctors to assess whether the patient is taking the right kind of medication in the right amount and at regular intervals. To help doctors make this assessment, we build a tracker which displays whether or not they have been taking the medications as prescribed based on the patient doctor conversation. Tests In this component, we display information regarding diagnostic tests that were conducted on the patient by different medical providers. Along with displaying test results, we also extract the reason behind why a test was ordered, when was the test conducted, or why wasn't the test performed in spite of being ordered. How We Built It Our application consists of a main front end built with Vue and a backend built with Python, with Flask as our server. We used AWS Transcribe to convert speech to text, while for summarizing the doctor patient conversation into a medical SOAP format, we used OpenAI's GPT-3 to extract meaningful and relevant insights from the dialogue. Challenges we ran into The main challenge for us was to learn deeply about the medical industry and specifically about hypertension. We spent a lot of time talking to the organizers, sponsors, doctors and nurses around the world and listened to their opinions on our ideas. Secondly, we also found it difficult to come to a conclusion regarding what specific features we wanted in our final product. To do so, we talked to doctors and nurses to get feedback on our proposal, learn about their actual needs, and finally refine the scope of our idea. Accomplishments that we're proud of We are proud of our idea and commitment - the amount of energy and passion that we put into this project to solve a real-world problem was something special and close to our hearts. The accomplishment that we are most proud about is the impact that this product could have on elevating the efficiency of the healthcare system and thereby saving more lives. What we learned Building this app for the hackathon has been a tremendous learning experience for us. We learned how to work under tight deadlines, collaborate effectively with a team, and solve problems creatively. Specifically, we learned about the challenges faced by doctors and how extracting relevant information from medical conversations and presenting them in a meaningful manner can help reduce medical errors. Through this hackathon, we also had the opportunity to learn from other developers and mentors, who provided valuable feedback and insights on our app. We learned about the latest trends and best practices in the field, as well as strategies for improving the user experience and increasing the app's value proposition. Overall, this hackathon has been an enriching learning experience, and we look forward to applying the lessons and skills we gained to future projects. References and Sources Centers for Disease Control and Prevention, National Center for Health Statistics. About Multiple Cause of Death, 1999–2020. CDC WONDER Online Database website. Atlanta, GA: Centers for Disease Control and Prevention; 2022. Accessed February 21, 2022. Whelton PK, Carey RM, Aronow WS, Casey DE, Collins KJ, Dennison C, et al. 2017 ACC/AHA/AAPA/ABC/ACPM/AGS/APhA/ASH/ASPC/NMA/PCNA Guideline for the prevention, detection, evaluation, and management of high blood pressure in adults. Hypertension. 2018;71(19):e13–115. Centers for Disease Control and Prevention. Hypertension Cascade: Hypertension Prevalence, Treatment and Control Estimates Among U.S. Adults Aged 18 Years and Older Applying the Criteria from the American College of Cardiology and American Heart Association’s 2017 Hypertension Guideline—NHANES 2015–2018. Atlanta, GA: U.S. Department of Health and Human Services; 2021. Accessed March 12, 2021. Farley TA, Dalal MA, Mostashari F, Frieden TR. Deaths preventable in the U.S. by improvements in the use of clinical preventive services. Am J Prev Med. 2010;38(6):600–609 https://www.corhealthontario.ca/HTN-Follow-Up-Protocol-(2018).pdf <div