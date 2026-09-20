---
slug: "foicedetect"
url: "https://devpost.com/software/foicedetect"
title: "Foicedetect"
hackathon: "Nosu AI Hackathon $11,300+ in prizes"
organization: "nosu"
winner: true
words: 437
team_size: 4
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "domain/finance_payments"
  - "user/patient_family"
  - "substrate/code_repository"
  - "substrate/document_pdf"
---

# Foicedetect

> Fake Voice Detect uses Nebius AI to spot deepfake voices, protect against scams, offer cybersecurity solutions, suggest witty replies to scammers, and securely store evidence for future use.

[Devpost](https://devpost.com/software/foicedetect) · hackathon [[Nosu AI Hackathon -11-300- in prizes]]

## Facets

**mechanism** [[realtime_stream]]
**domain** [[finance_payments]]
**user** [[patient_family]]
**substrate** [[code_repository]] [[document_pdf]]
  <sub>weak: web_dom</sub>

**stack** assemblyai, css, django, html, javascript, ml, nebius, python, react

## How they structured the write-up

- project overview
- tracks:
- 🚀 technologies stack
- 🛠 installation and setup
- 💡 inspiration, learning, and challenges

## Body

Detect Page Storage Generation2 Home Page Generation1 FoiceDetect: AI-Powered Voice Detection and Classification Project Overview We developed Fake Voice Detect, a platform leveraging Nebius AI to identify fake voices (deepfakes) and protect users from scams. As scammers increasingly use AI-generated voices to impersonate friends and request money, our platform evaluates how fake a voice is, provides Nebius AI-driven cybersecurity solutions, and even suggests humorous responses to outsmart scammers. Additionally, we securely store information for future use, including reports, evidence, and identification, empowering users to stay safe and take action against fraud. Tracks: Cybersecurity Track (WithSandra) $325 Most Technically Impressive - Modal (Series A company) $2,000 credits grand prize Nethenoob spinning cat ($65 cash) Nebius Exploratory Use of LLMs and Vision Models: 1st Place: $2,000 credits 2nd Place: $1,000 credits 3rd Place: $500 credits $1625 CASH (STATSIG GRAND PRIZE) Magic loops $325 CASH Beginner tracks (20 winners) ($10 each credits) 🚀 Technologies Stack Frontend React.js React Bootstrap Axios JavaScript ES6+ Backend Python Django Machine Learning Libraries ### Backend Machine Learning Libraries NumPy Scikit-learn SVC (Support Vector Classification) train_test_split StandardScaler Librosa (Audio feature extraction) Joblib (Model serialization) AssemblyAI Integration Key Features Voice Detection Voice Classification Real-time Audio Analysis Machine Learning Model Training 🛠 Installation and Setup Prerequisites Python 3.8+ Node.js 14+ pip git Repository Clone git clone https://github.com/dahomita/foicedetect.git cd foicedetect API Key Setup Environment Configuration Create a .env file in the project root directory Add the following API keys to the .env file: NEBIUS_API_KEY=eyJhbGciOiJIUzI1NiIsImtpZCI6IlV6SXJWd1h0dnprLVRvdzlLZWstc0M1akptWXBvX1VaVkxUZlpnMDRlOFUiLCJ0eXAiOiJKV1QifQ.eyJzdWIiOiJnb29nbGUtb2F1dGgyfDExMTY5ODA4MDkyNDAxNzkyMjcxOSIsInNjb3BlIjoib3BlbmlkIG9mZmxpbmVfYWNjZXNzIiwiaXNzIjoiYXBpX2tleV9pc3N1ZXIiLCJhdWQiOlsiaHR0cHM6Ly9uZWJpdXMtaW5mZXJlbmNlLmV1LmF1dGgwLmNvbS9hcGkvdjIvIl0sImV4cCI6MTg5NDY1NTAyMCwidXVpZCI6Ijc2NGNlOTc1LWI4ZjUtNDNkNi1hMTI1LTgzNDQwY2Y5MWVmYSIsIm5hbWUiOiJVbm5hbWVkIGtleSIsImV4cGlyZXNfYXQiOiIyMDMwLTAxLTE0VDIxOjAzOjQwKzAwMDAifQ.UXQkWATEndFFSgnZss62eQ9c7S64AfGLy2qOLJtDKQ8 ASSEMBLY_API_KEY=e98e3dcc13624e2c846c6de74a34809e ⚠️ Security Warning: Please don't use our key too much Backend Setup And Run cd backend python -m venv venv venv\Scripts\activate cd foicedetect_backend pip install -r requirements.txt pip install assemblyai python manage.py makemigrations python manage.py migrate python manage.py runserver Frontend Setup And Run npm install npm start 💡 Inspiration, Learning, and Challenges What Inspired Us We were inspired by personal experiences, as many of our friends and family members have been scammed through fake voice phone calls. Scammers impersonated their voices to deceive loved ones into sending money. This motivated us to create a platform that helps people like us by providing cybersecurity solutions to enhance not only their safety but also their knowledge. What We Learned How to use React for a dynamic frontend. How to use Django and Python for a flexible backend. How to implement User Authentication and Document Saving. Training Machine Learning models effectively. Integrating AI APIs for advanced functionality. Using Nebius to generate text and improve AI prompting. Seamlessly combining frontend and backend technologies. Challenges Faced Insufficient data for effective machine learning training. Managing secure storage and retrieval of user voice data. Generating accurate analysis and actionable solutions. <div