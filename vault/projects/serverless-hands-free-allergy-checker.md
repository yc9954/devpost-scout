---
slug: "serverless-hands-free-allergy-checker"
url: "https://devpost.com/software/serverless-hands-free-allergy-checker"
title: "Serverless Hands-free Allergy Checker"
hackathon: "AWS Artificial Intelligence Hackathon"
organization: "Amazon"
winner: true
words: 615
team_size: 1
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/voice_speech"
  - "domain/health_clinical"
  - "user/clinician"
  - "user/patient_family"
---

# Serverless Hands-free Allergy Checker

> Saves and checks drug allergy information using face recognition to prevent anaphylactic shocks

[Devpost](https://devpost.com/software/serverless-hands-free-allergy-checker) · hackathon [[AWS Artificial Intelligence Hackathon]]

## Facets

**mechanism** [[voice_speech]]
**domain** [[health_clinical]]
**user** [[clinician]] [[patient_family]]

**stack** amazon-cognito, amazon-dynamodb, amazon-lambda, amazon-lex, amazon-polly, amazon-rekognition, amazon-ses, amazon-web-services, javascript

## How they structured the write-up

- inspiration
- what it does
- how i built it
- challenges i ran into
- accomplishments that i'm proud of
- what i learned
- what's next for serverless hands-free allergy checker

## Body

Create User Flow Login With Face Recognition and OTP Code Text Extraction Save Patient Allergy Information Check Patient Allergy Information Doctor login with face recognition and OTP code text detection Inspiration I was shocked when I learned that drug allergies (caused by medication like aspirin, penicillin, ibuprofen, etc) can cause fatal anaphylactic shocks, especially in the children while I was searching the Internet about the grass allergy of our twins. Then I thought that we could use the face recognition technology in emergency services to check whether a patient has a drug allergy quickly using voice recognition. What it does The system saves the allergy information with the picture of the patient and this information can be retrieved by taking another picture using face recognition later. Also, it provides a quick fully hands-free interface for the personnel (doctors, etc) for quick and safe login operation and other patient management functions using voice recognition, letting them use their hands for their job while using the system. How I built it I have used Rekognition for indexing and searching faces of the doctors to let them log in with their face. Also, OTP codes are extracted using Rekognition text detection. Again, the faces of the patients are indexed to search allergy information by their face. The voice interface is implemented using Amazon Lex with 4 intents for adding patients, checking patients, taking pictures and logging out. Amazon Polly is used for talking to the users and S3 is used for storing the pictures of the users and patients. Allergy information is saved to a DynamoDB table. In addition to Amazon SES for sending emails for OTP codes, Amazon Cognito is used for authentication. AWS Lambda is used as a trigger to index the face of the patients when a record is added to the DynamoDB table. Also, Cognito trigger Lambda functions is used for generating an OTP code and sending to the email address of the personnel. Challenges I ran into I have been already familiar to the most of the AWS services but it took some time to learn Cognito custom authentication functionality to generate a custom authentication flow for sending OTP codes to the user and to bind Lambda triggers for it. I thought that creating an installation and uninstallation script for the users of the code would be very helpful. It turned out that writing the scripts and testing many times was a challenge. Accomplishments that I'm proud of I am proud of building the whole project. From coding front end in Javascript to providing triggers to tables and to generating a custom authentication. I am proud of finding an idea about providing a quick hands-free interface to the emergency services personnel. Also, I am proud of the social responsibility side of the project that it would decrease anaphylactic shocks in situations like a medicine given to the children in emergency services. What I learned I have learned to enable a custom authentication flow for Cognito. Also, this was my first hackathon which taught to me running in a quick time frame for binding various AWS services. I have improved my Bash scripting language skills. In addition, I have learned that if you try to do something for the good of the people you can find the power to overcome the challenges. What's next for Serverless Hands-free Allergy Checker The Lex bot can be improved for more options for the name of allergens and patient names. Also, for simplicity audio is recorded for 4 seconds and if is not fully silence sent to Lex for processing. It can be improved by using silence detection continuously and stopping only when the silence is detected. <div