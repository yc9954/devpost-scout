---
slug: "mediscan-p7uzrv"
url: "https://devpost.com/software/mediscan-p7uzrv"
title: "MediScan"
hackathon: "AWS Health AI Hackathon"
organization: "Amazon"
winner: true
words: 987
team_size: 2
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/benchmark_measured"
  - "mechanism/realtime_stream"
  - "mechanism/vision_ocr"
  - "domain/finance_payments"
  - "domain/health_clinical"
  - "user/clinician"
  - "user/patient_family"
  - "substrate/structured_db"
---

# MediScan

> Making healthcare accessible for all, one step at a time

[Devpost](https://devpost.com/software/mediscan-p7uzrv) · hackathon [[AWS Health AI Hackathon]]

## Facets

**mechanism** [[benchmark_measured]] [[realtime_stream]] [[vision_ocr]]
**domain** [[finance_payments]] [[health_clinical]]
**user** [[clinician]] [[patient_family]]
**substrate** [[structured_db]]
  <sub>weak: document_pdf</sub>

**stack** amazon-web-services, amplify, boto3, ec2, firebase, flask, flutter, medical-comprehend, python, s3, texttract

## How they structured the write-up

- inspiration
- what it does
- how it addresses the issues in health organization
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for mediscan

## Body

Login Screen Uploading Documents Results Page Book Appointments with Doctors Inspiration Coming into a post-pandemic world, we all have experienced how distant medical services and education can change our lives. This was our starting point; we wanted to build tools and aid remote doctors and nurses to be able to serve better healthcare. We believe that provided better tools using the latest technology, we will be able to reach more people and provide better healthcare facilities where traditional systems cannot go. We understand that the tools we build could potentially save a human life, which is the biggest inspiration. What it does We are building tools to help patients and doctors understand the medical history and summarise medical reports. We use AWS medical comprehend to achieve this. Using these tools, patients can easily upload their past medical information and then any remote doctor would have easily summarised sheets to quickly and effectively come to speed with the patient's health record. We also built ML flags to identify potentially crucial cases to reach out quickly and provide effective treatment. How it addresses the issues in Health organization health equity, bias in healthcare, predicting healthcare outcomes in populations, and improving care quality We ensure we do not collect any information about the patients race, or ethnic origins. This is in a bid to both ensure health equity and that ML models aren't trained on it. The only parameters the ML models use are medical in nature. The app is in essence free to use for medical reports. This is to ensure there is no financial barrier to entry, Allowing people of all income classes access to these tools. The app also helps people with little or no access to education be able to communicate with the doctor effectively. The medical reports are stored safely on remote servers ensuring anonymity helping a more safe environment for patients. How we built it We used Amazon Medical comprehend textract to generate Training data from the MTSamples. We used a data set with 792 samples belonging to the category 'Surgery' and 400 samples belonging to the category 'Consult' . We used Flutter for the app because of its cross-platform and quick prototyping nature. We were able to build both an android and an IOS app. We then used the MTsamples dataset as a corpus to start testing out medical comprehend. We quickly created datasets for ML models to train on to detect severe medical conditions from the processed data.We used SMOTE oversampling technique to handle the imbalance in the dataset . We used Sagemaker for initial testing but quickly decided we wanted to build our custom machine-learning model. We tried many different models like SVM, Random Forests and many more, but a fine-tuned XGBoost gave us the best model with an accuracy of 95%. We were cautious to ensure we didn't have false negatives, which would defeat the purpose. We used Amplify as a backend for our application, but we needed some more functionality built into Flutter through firebase. So we ended us using A combination of both storing medical reports of s3 from amplify and authentication. We use Stream builders in the flutter app to update the app data in real-time. We then used AWS texttract and comprehend to create a pipeline on python. We used boto3 as our interface with AWSCLI for everything else. We connected an EC2 instance to S3 and read API requests. We plan to use flask to create the API server where we host the code. Challenges we ran into We could generate samples from only 2 categories i.e 'Surgery' and 'Consult' due to limited AWS credits . We had trouble creating our data flow APIs. We were using a combination of Firebase FireStore, and Amplify S3. We were able to come to an amicable solution that worked eventually. We had issues with AWS free tier as it wasn't sufficient to create enough data for a complex model. We settled for XGBoost for a balanced result minimising overfitting and false negatives. We had an issue with our texttract function in Sydney, Australia. We were later able to figure out that it was rare one-off thing from this thread link . We changed our region and were able to solve the problem. Accomplishments that we're proud of We are proud to solve a problem that can save someone's life, both literally and figuratively. Of course, we also learned a lot along the way. As a team, we could navigate the challenges we faced at every step and find solutions in the most unlikely of places. Learning new things and building tools that can potentially help save people's lives isn't something ordinary. As a team, we are very grateful to work on this. What we learned We learned a lot, especially appreciating the effort of making full-stack apps. Coming from an ML background, we also understand the background processing that medical-comprehend and texttract provide. We are building this application as proof that the tools that medical professionals use for remote consultation can be vastly improved and that there's much scope for improvement here. What's next for MediScan We have a few plans for MediScan going forward. The goal is to fully get the app to the standards of the NCBI telemedicine guidelines. Once we achieve that, we want to see how users and doctors react to these tools. This feedback will prove critical as we iterate and improve our tools. Plans for more tools and ideas: Real-time health monitoring and alert system using AI Data storage democracy and global ownership of Blockchain Tools for doctors to understand the physical living space of the patient in cases - relevant. AR tools to assist patients with self-medication guidance. We believe there is open space for growth and converting this project into a startup or company. This idea has immense social value, and we intend to contribute as much as possible. <div