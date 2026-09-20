---
slug: "telescopium"
url: "https://devpost.com/software/telescopium"
title: "Telescopium"
hackathon: "Azure AI Hackathon"
organization: "Microsoft"
winner: true
words: 725
team_size: 3
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/privacy_tech"
  - "mechanism/realtime_stream"
  - "mechanism/vision_ocr"
  - "domain/health_clinical"
  - "domain/scientific_research"
  - "domain/security_privacy"
  - "user/clinician"
  - "user/patient_family"
  - "substrate/structured_db"
  - "substrate/video_visual"
---

# Telescopium

> AI that looks to the eye.!

[Devpost](https://devpost.com/software/telescopium) · hackathon [[Azure AI Hackathon]]

## Facets

**mechanism** [[privacy_tech]] [[realtime_stream]] [[vision_ocr]]
**domain** [[health_clinical]] [[scientific_research]] [[security_privacy]]
**user** [[clinician]] [[patient_family]]
**substrate** [[structured_db]] [[video_visual]]

**stack** azure, flutter, ml, wordpress

## How they structured the write-up

- inspiration
- medical ground
- goals
- what it does
- how we built it
- challenges we ran into
- accomplishments that we are proud of
- what we learned
- what's next for telescopium

## Body

Logo Color Code Cover Inspiration Our eyes are windows to the soul. Eye exams are not just about vision, they are about our overall health and quality of life. Our eyes are a window to the live action of blood vessels, nerves, and connective tissues throughout our body. So problems spotted in our eyes are often the first signs of a disease lurking elsewhere. Telescopium is the next-generation mobile app that utilizes the high potential of computer vision techniques to enhance the healthcare industry via making eye analysis easier and more accessible Medical Ground According to the American Academy of Ophthalmology, there are more than twenty health problems an eye exam can catch. Eye exams are important not only for the health of the eye but also to determine if there are issues affecting multiple organs or the entire body that need attention. Because of their delicate structures, including nerves, blood vessels, and connective tissues, the eyes can show signs of many significant health risks in the early stages. That can be critically important to patients because catching diseases early is often the key to preventing severe outcomes. Goals Accessible Diagnostic Tool : Because healthcare is not quite available and accessible in vulnerable rural areas around the world, especially in third world countries, we aim to provide easier access to healthcare by creating an easy means to the detection of some of the diseases that eye exams can catch through images of eyes at zero cost. Leverage AI to Tackle Non-Communicable Diseases : Artificial intelligence techniques have proven amazing successes in detecting diseases. For example, breast cancer can be verified through CT images. We aim to create a similar system that combats diseases in a more modern way. What it does Telescopium is a mobile application that applies high-level computer vision techniques to do real-time diagnostics based on eye situations. The application supports the user experience, through which the doctor or nurse takes pictures of the patient's eyes in a specific way and inappropriate lighting. The images are then sent to our servers for processing and analysis, and the results are displayed after a few minutes. It is necessary to secure patient data in order to comply with GDPR and HIPPA. The differential privacy model will be implemented with our partners so that they can share their patient data. How we built it Basically, the ML endpoint is deployed on Azure App Service via RESTful API and it is connected to the mobile app which is developed using flutter. Also, we created an eye-tracking model on edge to ensure data quality. Mobile Application The application is specially designed to suit the use of the physician during a clinical examination. Many features and instructions have been added to obtain the best results and to ensure data quality. In addition, we integrated an eye-detection model in order to avoid violations of patient privacy, so we only get the desired image. Real-Time Eye Detection This model is built with OpenCV and running on edge so that we can detect and track the patient's eyes. Thus, we can guide the doctor to get a correct image of the eye to perform the diagnostic step without getting unwanted data. Eye Disease Multi-Classifier This model is the main pillar of the project. In which, the eye is analyzed and classified to detect various diseases. This model is trained periodically on Azure Machine Learning and the saved model is used to create an ML endpoint that is connected to the mobile app. Data Initially, we used the Helen Eye Dataset from Kagel to build a proof of concept. We are planning to collect clinically verified data from official clinical trials at hospitals and universities to get medical approval. We apply the differential privacy concept so that our hospital partners can use the app while preserving patient data. Challenges we ran into Integrating all different pieces together. Accomplishments that we are proud of We have successfully created a full prototype during the Hackathon. Moreover, our system has been deployed as a real-life proof of concept, and it could be used easily. Furthermore, we made a business model, so that we can commercialize our app. What we learned We learned more about Azure cloud services while building the application. What's next for Telescopium Collect an appropriate dataset to re-train the model for real-deployment. <div