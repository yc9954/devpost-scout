---
slug: "phishy-d8ua1t"
url: "https://devpost.com/software/phishy-d8ua1t"
title: "phishy"
hackathon: "Nosu AI Hackathon $11,300+ in prizes"
organization: "nosu"
winner: true
words: 466
team_size: 1
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "domain/developer_tools"
  - "domain/security_privacy"
---

# phishy

> Protect yourself from phishing attacks without the complexity. Phishy provides real-time phishing detection and alerts. Get peace of mind knowing Phishy is silently watching out for you

[Devpost](https://devpost.com/software/phishy-d8ua1t) · hackathon [[Nosu AI Hackathon -11-300- in prizes]]

## Facets

**mechanism** [[realtime_stream]]
**domain** [[developer_tools]] [[security_privacy]]
  <sub>weak: developer</sub>
  <sub>weak: code_repository</sub>

**stack** .net, firebase, gemini, swift

## Body

Inspiration "With phishing attacks becoming increasingly common, especially in Ireland where many people unintentionally click on malicious links in SMS and emails, I wanted to build a solution that empowers users to protect themselves and their data. Phishy was inspired by the critical need to provide a comprehensive and user-friendly tool that not only detects phishing attempts in real-time but also educates and informs users through personalized security recommendations." What it does "Phishy leverages Google Gemini to analyze potential phishing messages and scam information. Additionally, it notifies users if their email has been compromised in a data breach, providing detailed information about the incident. With user consent, the app also analyzes their data to offer tailored security recommendations, including reminders to update passwords frequently." How we built it "Phishy is a macOS application developed using SwiftUI. It integrates Google Gemini alongside Google Cloud functionalities such as Google Cloud IAM, Firebase, Firebase Firestore, Google Cloud Run, Google Cloud Secret Manager, and Cloud Scheduler. The app was designed for macOS, making it adaptable for iOS and iPadOS due to the ARM architecture. Moreover, I integrated GitHub Actions for building and deploying the macOS app as a release. This action was further integrated with Google Gemini to analyze previous commits and messages, automatically generating release descriptions. The backend, hosted on Google Cloud Run, is triggered when a user interacts with phishing-related content or a breach attempt. If a user opts in for monitoring, Cloud Scheduler processes their data hourly, sending it to Gemini for recommendations via a request to GCP Cloud Run endpoint." Challenges we ran into "Determining the most effective ways to integrate Google Gemini within the app was challenging initially. Getting Gemini to return the exact data I needed through prompt engineering required some trial and error. Additionally, on the architectural side, managing complex data storage and processing proved more difficult than expected. I initially started with Swift for the backend in Google Cloud Run but moved to .NET after struggling with debugging, causing some initial setbacks." Accomplishments that we're proud of "I'm proud of completing a working prototype of the app, even with a few known bugs. Specifically, while Firebase sign-in is still a bit buggy, Google Sign-in works flawlessly." What we learned "I learned how to effectively use Gemini to create a powerful phishing detection app, including the integration and optimization of GCP services such as Cloud Run and Cloud Scheduler. This process helped me create a monitoring feature that uses user phishing data to provide personalized security recommendations." What's next for Phishy "My immediate focus is on fixing existing bugs and enhancing the UI of the macOS app. As a primarily backend developer, I recognize the importance of a user-friendly interface. Improvements will be made to streamline the app experience for the end-user." <div