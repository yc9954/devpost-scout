---
slug: "5vid-co"
url: "https://devpost.com/software/5vid-co"
title: "5vid.co"
hackathon: "COVID-19 Global Hackathon 1.0"
winner: true
words: 1189
team_size: 13
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/vision_ocr"
  - "domain/health_clinical"
  - "domain/labor_employment"
  - "user/clinician"
  - "user/general_public"
  - "user/patient_family"
  - "user/researcher"
  - "substrate/document_pdf"
  - "substrate/geospatial"
  - "substrate/video_visual"
---

# 5vid.co

> 5vid.co provides at-home Covid-19 screenings via web application. We use CV, video-chat, and a symptom scoring system to assess Covid-19 risk and escalate critical patients to local health volunteers.

[Devpost](https://devpost.com/software/5vid-co) · hackathon [[COVID-19 Global Hackathon 1.0]]

## Facets

**mechanism** [[vision_ocr]]
**domain** [[health_clinical]] [[labor_employment]]
**user** [[clinician]] [[general_public]] [[patient_family]] [[researcher]]
**substrate** [[document_pdf]] [[geospatial]] [[video_visual]]
  <sub>weak: web_dom</sub>

**stack** amazon-web-services, beanstalk, ec2, flask, html, lambda, mongodb, node.js, opencv, postgresql, python, react, s3, webrtc

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we are proud of:
- what we learned
- what's next for 5vid.co

## Body

Features of the web app. Users fill in a survey so that the web app can make a risk assessment of him. Doctors are able to see the health report of the users. Users upload a 20-sec video of the finger as well, so that the automated scoring system also inputs the user's vital signs. Doctors can call the users from the web application once they review their symptoms and vital signs to schedule them for a videochat. Inspiration Our inspiration is to help local health professionals, and concerned citizens, avoid overwhelming the already clogged local hospitals with non-critically ill patients looking to receive primary Covid-19 screenings. We set out to create an application that will allow patients to submit their symptoms and get a high-quality medical risk assessment designed with experienced doctors, from the safety of their own homes, without creating additional pressure for our already stretched healthcare workers. In addition to providing patients with critical screening and peace of mind, we also want to reduce the operational burden on medical personnel by allowing them to access data-driven information for pre-screened patients, based on their personal condition and symptoms, enabling doctors to focus on those patients who are most in need of critical attention. 5vid.co was designed primarily for Spanish-speaking patients because we found a big gap when researching solutions and information for this demographic. The name of our app is a play on words that in Spanish means (“without Covid”). We worked with local doctors in Medellin, Colombia to design the patient screening process, but our application can easily be localized for other languages and locations. We would in principle only need to connect the communication features of this application to local doctors in other locations. What it does 5vid.co is an online medical triage platform delivered through a web application. It uses computer vision and rules-based data algorithms to help potential Covid-19 patients screen their symptoms without leaving their homes. If the severity of their symptoms is concerning, it automatically escalates their risk-profile and connects them to local qualified medical personnel via a built in webchat feature. By uploading a 20-second video of their finger (to check for vital signs like their pulse and oxygen levels), and answering some questions about their symptoms and medical condition, patients will be scored using a screening process that we designed with doctors for the identification of Covid-19. If the individualized score shows low risk, the patient will receive best-practices and advice on how to minimize the chance of being infected. If the patient’s risk-assessment is determined to have a high-probability of having tested positive for Covid-19, the patient’s information will be automatically submitted to a local health provider who can organize a video call to perform a more precise diagnostic of the patient’s health. The doctor can then determine whether the patient needs to be monitored frequently or referred to the local ER. How we built it We first consulted with doctors to learn more about the early symptoms of COVID-19 and how they go about screening their patients in person. To ensure that our online triage scoring system is as accurate and effective as possible, we took careful consideration of the real-world processes that doctors follow when assessing patients. We then built two web applications. The first is focused on patients, allowing them to answer screening questions and upload a video of their finger so that our app can use computer vision technology to monitor their vital signs (pulse and oxygenation levels). This combined data is then automatically analyzed to generate a risk-score for that particular user. The second part of the application is focused on doctors and medical personnel, so that they can review a list of users that have submitted the diagnostic form, see them ranked by risk/priority, analyze an automatically-generated health report, and request a live video consultation based on a specific patient’s condition. Challenges we ran into Collecting the necessary questions and a concise list of risk factors to build the doctor’s scoring system: for this, we researched the questions that local and international health providers have gathered to get an accurate risk assessment of COVID infection on patients. (Medical Information - literature and doctors), and we consulted with local doctors. Implemented a system so that the users can upload easily a video of the finger to check their vital signs using infrared light refracted off their finger. We implemented this system from scratch after researching the following academic paper: https://www.iiitd.edu.in/noc/wp-content/uploads/2017/11/06959086.pdf Built a web rtc system, so that doctors can communicate with high-risk infection patients, and have a better understanding of the patient’s state. Organized all the members of the team (13 people working remotely) so that they could do all the tasks needed to design and implement 2 web applications, 4 APIs, 2 algorithms and a web video call system in just 2 days of work. Accomplishments that we are proud of: The accomplishments we are most proud of are: Focusing on our local community, in Latin America, which is often underserved and where doctors welcomed our help given their heavy case-load. We had multiple meetings with local doctors from hospitals in Medellin, Colombia, where they guided us through official Covid-19 risk assessments. Mapping those studies, questionnaires, and risk assessments, we were quickly able to develop a screening system that can accurately determine whether a patient is infected or not. Implemented the algorithm that computes oxygen saturation level and heart rate based on a quick video of the user’s finger. This algorithm was based on the following academic paper: https://www.iiitd.edu.in/noc/wp-content/uploads/2017/11/06959086.pdf . Implemented video file handling, and web rtc systems that allow a) the user to upload a quick video to check for vital signs, from their web browser, and b) the doctor to contact the user via a webchat in order to extend the medical review. What we learned We learned that even without extensive lab tests, doctors already know how to assess whether patients have been infected with Covid-19 with a good enough degree of certainty based on their symptoms. Using their knowledge and enabling it to be distributed at scale via a simple web app does not require expensive medical equipment and can help screen patients and save lives. Through the application of technology, we can help leverage the early knowledge gained about this virus and set up a triage system that can help combat the pandemic--maximizing the safety of the population from their own homes, and optimizing the efficiency of local health resources who are short on staff and equipment. What's next for 5vid.co There are other features that we’d like to add (different health and body measurements, in addition to the 20-sec video, to measure other vital signs, perhaps also using other smart devices). We’d also like to improve the doctor’s interface and provide more feedback from the doctor to the patient. While this project was designed for Colombia, with local healthcare providers, we would love to extend it to other locations and geographies. Our goal is to partner with other countries so that they too can implement this system and protect both the communities and their doctors. <div