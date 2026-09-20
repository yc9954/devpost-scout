---
slug: "myheartrisk"
url: "https://devpost.com/software/myheartrisk"
title: "MyHeartRisk"
hackathon: "Predictive AI In Healthcare with FHIR®"
organization: "Darena Solutions"
winner: true
words: 873
team_size: 2
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "domain/health_clinical"
  - "user/patient_family"
  - "substrate/medical_record"
---

# MyHeartRisk

> MyHeartRisk is an AI-driven tool that integrates with EHRs and functions as a standalone app or CDS Hooks to deliver personalized ACS risk scores, risk levels, and health insights in real time.

[Devpost](https://devpost.com/software/myheartrisk) · hackathon [[Predictive AI In Healthcare with FHIR-]]

## Facets

**mechanism** [[realtime_stream]]
**domain** [[health_clinical]]
  <sub>weak: elder_child_care</sub>
**user** [[patient_family]]
  <sub>weak: general_public</sub>
**substrate** [[medical_record]]

**stack** amazon-ec2, nextjs, python, s3bucket, vercel

## Body

MyHeartRisk X MeldRx EHR Launch Patient Dashboard ACS Risk Assessment Risk Adjusment Risk Factors CDS Hooks MyHeartRisk Introduction MyHeartRisk is an AI-driven tool for patients to monitor their risk of ACS, developed as part of a study in Malaysia in collaboration with Universiti Teknologi MARA (UiTM) and Universiti Malaya (UM). It leverages data from the National Cardiovascular Disease (NCVD) Malaysia registry to build an ACS risk prediction model. By integrating with MeldRx or functioning as a standalone app, MyHeartRisk delivers real-time ACS risk scores, categorized risk levels, and personalized health insights. The model is based on clinical research and data-driven methodologies, contributing to improved early detection and preventive care for cardiovascular diseases. Here are some work builds upon studies in cardiovascular risk assessment by us, including: Sazzli, S., Sorayya, M., Putri, N., Lai, H., Sun, W., Hiew, J.,Song, C. (2023). Prediction of short- and long-term mortality in Asian ACS patients using stacked ensemble learning. International Journal of Cardiology, 393, 131471. https://doi.org/10.1016/j.ijcard.2023.131471 Kasim, S., Malek, S., Ibrahim, K. S., & Kumar, D. S. (2023). Applying an interpretive machine learning algorithm to predict in-hospital mortality in elderly asian patients with acute coronary syndrome (ACS). European Heart Journal, 44(Supplement_1). https://doi.org/10.1093/eurheartj/ehac779.125 Putri, N., Sazzli, S., Sorayya, M., Nurulain, I., Nafiza, M., & Najmin, A. (2023). Comparing the performance of the FRS, machine learning, and stacked ensemble learning in estimating the 10-year CVD risk in the Asian population. International Journal of Cardiology, 393, 131483. https://doi.org/10.1016/j.ijcard.2023.131483 Why MyHeartRisk Matters in Healthcare & EHR Early Intervention Saves lifes . ACS risk prediction is crucial because Acute Coronary Syndrome (ACS) is a leading cause of heart-related emergencies and deaths, and early detection can significantly reduce mortality and complications. By leveraging AI-powered risk assessment, MyHeartRisk helps identify high-risk patients before symptoms appear, allowing for preventive strategies such as lifestyle modifications, medication adjustments, and closer monitoring. This proactive approach not only improves patient care but also reduces hospital readmissions, healthcare costs, and the burden on emergency services, making it a valuable tool for modern cardiovascular healthcare. Integrating MyHeartRisk with Meldrx enhances clinical decision-making by providing real-time ACS risk predictions directly within existing workflows. EHR integration ensures that healthcare providers have seamless access to a patient’s medical history, risk factors, and AI-driven insights without disrupting their workflow. This leads to more informed, data-driven decisions, enabling early intervention and better patient outcomes. Top Features CDS Hooks for Instant ACS Risk Assessment – Provides real-time ACS risk scores within EHR workflows using CDS Hooks integration. EHR Launch for Detailed Insights – Enables seamless EHR integration to view detailed patient risk analysis. Patient Dashboard – Displays a comprehensive risk profile, including historical data and trends. AI-Predicted ACS Risk – Uses AI-driven models to estimate personalized ACS risk levels based on patient data. Framingham Risk Score (FRS) Calculation – Computes FRS risk scores to assess long-term cardiovascular risk. Risk Factor Explanation – Provides a detailed breakdown of contributing factors Risk Adjustment – Allows customizable risk factor. Return Report and Tasks to EHR – Full connection to EHR via FHIR standard Chatbot with Agent – An AI-powered assistant that provides risk explanations and answers provider queries. Personalized Health Recommendations – Suggests lifestyle and treatment adjustments to lower cardiovascular risk. How to Try MyHeartRisk Activate the MyHeartRisk App – Search from the public extensions and enable the MyHeartRisk application within your MeldRx workspace. Import Patient XML File – Upload the provided patient XML file provided in the download link below to load sample patient data. Select and View a Patient – Choose a patient from the list to see their risk profile and health data. EHR App Launcher – Use the EHR App Launcher located at the top section to access MyHeartRisk Allow Access – Grant the necessary permissions, and you’re ready to explore ACS risk predictions and insights. Challenges and Drawbacks Developing MyHeartRisk came with several challenges, especially as I navigated new concepts and technologies: First Time Working with EHR and MeldRx – This was my first experience with Electronic Health Records (EHRs) and the MeldRx platform, requiring a steep learning curve to understand how data flows and integrates within clinical environments. Issues with Loading Provided Patient Data – The provided patient XML file did not load correctly, forcing me to manually code a patient XML file with the help of LLMs. The app might not work properly with other patient as the XML structure might be different. Please use the patient xml provided in the s3 download link below. First Time Dealing with FHIR Standard – Fast Healthcare Interoperability Resources (FHIR) is a complex framework with strict data formatting rules. Understanding FHIR resources, profiles, and how to query data required significant effort. What I've Learned Working on MyHeartRisk has been an incredible learning experience, giving me the opportunity to explore EHR integration, FHIR standards, and AI-driven risk prediction in a real-world healthcare setting. This project introduced me to the MeldRx platform, the complexities of clinical data handling, and the challenges of ensuring AI models align with medical decision-making. I’m especially grateful for the opportunity to contribute to a meaningful study that aims to improve cardiovascular risk assessment. This experience has strengthened my understanding of healthcare AI and inspired me to continue exploring innovations in this field. 🚀 <div