---
slug: "ishare-platform"
url: "https://devpost.com/software/ishare-platform"
title: "iShare Donation Platform"
hackathon: "Azure AI Hackathon"
organization: "Microsoft"
winner: true
words: 1187
team_size: 5
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/vision_ocr"
  - "domain/education"
  - "domain/finance_payments"
  - "domain/labor_employment"
  - "user/educator_student"
  - "substrate/document_pdf"
  - "substrate/video_visual"
---

# iShare Donation Platform

> A platform with Azure Cognitive Services for the donation of old PC equipment and giving support to the poor students at scale like Uber and AirBnB.

[Devpost](https://devpost.com/software/ishare-platform) · hackathon [[Azure AI Hackathon]]

## Facets

**mechanism** [[vision_ocr]]
**domain** [[education]] [[finance_payments]] [[labor_employment]]
**user** [[educator_student]]
**substrate** [[document_pdf]] [[video_visual]]

**stack** azure, azure-cognitive-services, computer-vision, face, flask, form-recognizer, language-understanding, python, qna-maker, text-analytics, translator

## How they structured the write-up

- inspiration
- what it does
- how we built it
- accomplishments that we're proud of
- challenges we ran into
- what we learned
- what's next for ive cloud

## Body

Face index Sentiment Form input Q&A Chatbot iShare Platform Inspiration Due to the COVID-19 pandemic, education has to go 100% online suddenly. The disadvantaged students are suffering seriously! They do not have a PC, notebook, and even internet connection! As a result, poor children cannot learn from home and it widens the gap between the rich and the poor students. Currently, there are many charities launch old PC donation campaigns but they cannot really help a lot of students. The traditional way is generally in 3 steps: collect an old PC, store it and give it to a student. It is not effective at all and not scalable! When students get the old PC, it sometimes requires technical support such as re-install Microsoft Windows, installing Microsoft Office and setting up a network at home. Without IT supporting volunteers, students still cannot learn from home. Even if the pandemic is over, the disadvantaged students who do not have PCs for homework are a serious problem. What it does The best way is to adopt the idea of the sharing economy and decentralize the donation process like AirBnB or Uber without bottlenecks. iShare is a platform to make use of Azure Cognitive services to match donors, students and volunteers quickly with AI. How we built it What services do we use in our platform? For donation priority we mainly use the sentiment analysis and key phrases in Text Analytics for ranking. To simplify registration and application from the user. We extract data, text and key/value pairs from the identity card without manual labelling by Form Recognizer. To prevent unwanted contents/images, we use Content Moderator and Computer Vision to filter out all unwanted content or images. We create a Chatbot by QnA Maker for a conversational question-and-answer layer. User with different language also welcome to our platform, because we make use of a translator to break the language boundary. We also use Face Verification for fraud detection. The most important thing, we compare the analysis from text analytics and Perceived Emotion Recognition for our Project KPI. How do Azure Cognitive services help iShare? Problem 1: Donors and Students Matching iShare hopes to prioritize the donation to the worst condition students and we make use of Text Analytics to analyse each student case. Priority is according to the sentiment and key phrases of the student case. Problem 2: Abuse Case iShare requires students to create an account. Students must provide a student identity card with a photo and endorse a teacher in their school as a verifier. Form Recognizer extracts basic information from their ID card and their face is indexed for face verification and abuse detection. Students are required to submit a photo with the donor and the system tag their face. Abuse cases would be figured out if someone creates more than one account and gets resources the second time. Problem 3: Lack of manpower to check all kinds of contents. iShare allows donors, students and volunteers to submit contents to the platform which includes texts and images. Content Moderator and Computer Vision are used for the review of all texts and images contents. Users cannot share any potential offensive and unwanted images, possible profanity and undesirable text, adult and racy content images and spam messages. Problem 4: Lack of manpower to answer questions QnA Maker can answer users' questions anytime. For text content, Translator makes sure donors, students and volunteers can community in different languages. Problem 5: Is iShare really helpful? iShare makes use of the perceived emotion recognition to estimate the donation is a success or not. Both donors and students should express their happiness in the photo. After the donation, the student needs to write a thanks message to the donor and those messages are analysed by Text Analytics as well. Students would not be able to request further support if they do not express thankfulness to the donor. Accomplishments that we're proud of We feel grateful that our platform’s performance improved by using Azure Cognitive Services. Firstly, the accuracy of matching donor and student increase 200%, which really benefits the students in need. Secondly, the system saves time no need to handle fake case or human error, the efficiency improves 600%. The most important improvement is reduced manpower for this sharing concept, before applying the administrator of the service needs to take much time on checking the content and for now this checking done by the system automatically. And they're also no need to answer the frequently asked questions, it saves them time on support. Azure Cognitive Services Architecture The above diagram shows how the systems recognize the user's face and build an index for the platform. The above diagram shows how the Q&A chatbot answers the question from all users. The above diagram shows how the systems get the student's sentiment score from the student story and use the sentiment score of the student story to prioritize the donation. The above diagram shows how the systems build an index for the user and store index information on the platform. Challenges we ran into The challenges we ran into Azure AI service such as text Analytics, Q&A Maker, AI Translator … This service was our first time to know what AI is and how to use it. We used lots of time to research the Microsoft documents and found lots of examples to learn. When our program has some errors, we will research from Microsoft documents and AI client library to help us fix the problem. What we learned In this project, we learn how to deal with teamwork. Since we did not have the right teamwork in the first phase of the project, the division of labour among members was chaotic. It caused a lot of delays in our project process. But in the middle stage, we found this error and tried to solve it. We have prepared a clear division of labour plan to divide who is to complete the task. In the end, the result was good, and the progress of the project was faster than I expected. We also learned a lot of knowledge about Azure AI at the AI Hackathon event, this time was our first time writing Python to develop the AI service in Azure into Flask, we found a lot of information about AI service examples and we checked some functions in the AI client library to help us. What's next for IVE Cloud For the next step of IVE Cloud, we will make the program of AI service more stable and we will train more models to our AI service that can make it work and we hope it can have less error to come out. The platform will soon support multiple languages. In addition, we will cooperate with some charities to ensure that every student can learn through the online teaching platform. Finally, we expect the Project can go to worldwide for helping others know more about AI services. This project is developed by IVE Cloud, the MS learn students from IT114115 Higher Diploma in Cloud and Data Centre Administration, IVE(Lee Wai Lee) Hong Kong <div