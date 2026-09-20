---
slug: "lifelink-dzeyha"
url: "https://devpost.com/software/lifelink-dzeyha"
title: "LifeLink"
hackathon: "Hack for Humanity | 2025"
organization: "Kuba Apps"
winner: true
words: 645
team_size: 2
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/privacy_tech"
  - "domain/health_clinical"
  - "user/patient_family"
  - "substrate/medical_record"
  - "substrate/video_visual"
  - "substrate/web_dom"
---

# LifeLink

> Linking You to a Healthier Tomorrow

[Devpost](https://devpost.com/software/lifelink-dzeyha) · hackathon [[Hack for Humanity - 2025]]

## Facets

**mechanism** [[privacy_tech]]
**domain** [[health_clinical]]
**user** [[patient_family]]
**substrate** [[medical_record]] [[video_visual]] [[web_dom]]

**stack** djangorestframework, expo.io, express.js, mongodb, numpy, opencv, react, react-native

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for lifelink
- lastly

## Body

Home Page Search User by Image or Fullname Users User Details Sign In on Mobile Sign Up on Mobile Profile Page on Mobile Inspiration Medical emergencies demand swift action and seamless access to critical patient information. Lifelink was born out of the need to streamline patient identification and medical record retrieval, ensuring that hospitals can provide timely and effective care. What it does Lifelink is a mobile and web app designed to improve the speed and efficiency of medical care in emergencies. It allows hospitals to upload patient information after diagnosis or treatment, including medical history, test results, and treatment details. In case of an emergency, any hospital can quickly access a patient's complete medical records on the app. This eliminates the need to question a patient who may be unable to communicate or repeat tests that have already been done, saving critical time and resources. Lifelink ensures that healthcare providers have the right information when they need it most, helping to deliver faster and more accurate care. How we built it Firstly, we agreed on the project we were going to be working on. Then, we split the tasks and set deadlines for ourselves. While Mayowa handled the Backend using NodeJS, Image Comparer using OpenCV and Django, Blessing worked on the Frontend to bring the vision of the app to life. We collaborated closely via WhatsApp and Google Meet throughout the course of the project, ensuring that every step was aligned with our goals. Challenges we ran into Our primary challenge during the research phase was understanding the standard processes and protocols across various hospitals. This required extensive communication and data collection, which proved to be highly time-consuming. Each hospital often operated with distinct workflows and systems, making it essential for us to ensure that our solution could effectively adapt to these diverse practices. Accomplishments that we're proud of Seamless Integration: We are proud of how Lifelink integrates easily with different hospital systems, providing quick access to patient data without disrupting existing workflows. Security Features: Implementing strong security measures like end-to-end encryption to protect sensitive medical data was a significant accomplishment. User Experience: The app’s intuitive design ensures that healthcare professionals can access critical patient information with just a few clicks, making the process faster and more efficient. Custom Image Analyzer: One of our biggest achievements was building our own AI-powered image analyzer for facial recognition. Since we couldn’t find an existing API that met our needs, we developed our own solution using Django, OpenCV and NumPy, allowing hospitals to match patient headshots against their records with high accuracy. What we learned This project deepened our understanding of hospital workflows and the challenges of adapting technology to diverse healthcare environments. We also gained valuable insights into the power of AI-driven image search for patient identification and the necessity of strong security measures to safeguard medical data. What's next for LifeLink Our goal is to continue innovating and expanding Lifelink to transform the future of healthcare. We're working to integrate predictive analytics that will enable Lifelink to forecast potential illnesses and recommend personalized medications. We'll also continue to refine our AI-powered image search functionality to achieve even greater accuracy and speed. Additionally, we're exploring innovative ways to support better patient outcomes and improved healthcare efficiency. Furthermore, we plan to integrate Lifelink with additional hospital systems and electronic health records, ensuring seamless connectivity and data exchange. Lastly We've decided to open source the Image Comparison API It can be accessed here: POST https://lifelink.pythonanywhere.com/api/compare-images/ { "target_image": "https://images.pexels.com/photos/1139743/pexels-photo-1139743.jpeg?auto=compress&cs=tinysrgb&dpr=1&w=500,", "people": [ { "name": "John", "image": "<john image live url>" }, { "name": "Jane", "image": "<jane image live url>" }, { "name": "Bob", "image": "<bob image live url>" } ] } Lifelink is more than just an app—it’s a step toward the future of efficient, AI-powered emergency healthcare. 🚀 (Please download the app and open Lifelink to test app <div