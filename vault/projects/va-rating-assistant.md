---
slug: "va-rating-assistant"
url: "https://devpost.com/software/va-rating-assistant"
title: "VA Rating Assistant - Lambda"
hackathon: "AWS Lambda Hackathon"
organization: "Amazon"
winner: true
words: 572
team_size: 1
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/privacy_tech"
  - "mechanism/realtime_stream"
  - "mechanism/retrieval_grounding"
  - "domain/accessibility"
  - "domain/health_clinical"
  - "substrate/document_pdf"
  - "substrate/geospatial"
  - "substrate/structured_db"
  - "substrate/web_dom"
---

# VA Rating Assistant - Lambda

> VA Rating Assistant: Upload medical docs & our AI scanner identifies potential VA disability claims & ratings. Get the benefits you deserve, faster & more accurately.

[Devpost](https://devpost.com/software/va-rating-assistant) · hackathon [[AWS Lambda Hackathon]]

## Facets

**mechanism** [[privacy_tech]] [[realtime_stream]] [[retrieval_grounding]]
**domain** [[accessibility]] [[health_clinical]]
**substrate** [[document_pdf]] [[geospatial]] [[structured_db]] [[web_dom]]

**stack** amazon-web-services, api-calls, javascript, lambda, learning, machine, react, supabase-database, textract, typescript

## How they structured the write-up

- inspiration
- what i learned
- how i built it
- challenges i ran into
- accomplishments i'm proud of
- what's next for va rating assistant - bolt.new

## Body

About the Project: VA Rating Assistant - Lambda Inspiration As a passionate advocate for veterans' welfare and an active-duty Navy Chief, I was inspired to create VA Rating Assistant after hearing countless stories of frustration from veterans navigating the VA disability claims process. The VA process can feel overwhelming, confusing, and slow. I wanted to build a tool that empowers veterans to take control of their disability rating journey with speed, clarity, and AI-driven insights. What I Learned I gained valuable insights into the complexities of the VA disability claims process and the real-life struggles veterans face. I deepened my skills in Natural Language Processing (NLP) , serverless backend development , and machine learning . I learned the importance of accessibility , user experience (UX) , and clear communication when building tools for a diverse user base like veterans. How I Built It 🔨 Technologies Used Frontend Development: Built with Bolt.new (React + TypeScript) for a fast, responsive, and mobile-friendly user interface. Backend Development: Built using multiple AWS services for scalability and cost efficiency: Service Purpose AWS Lambda Serverless compute for API endpoints and document processing Amazon API Gateway Exposes secure REST API endpoints for frontend communication Amazon S3 Secure file storage for uploaded medical documents Amazon Textract Document text and data extraction Amazon Bedrock + Bedrock Agent Runs AI-driven tasks like condition detection and RAG workflows Amazon SQS / SNS Handles async event processing and notifications Amazon Cognito Manages user authentication and authorization AWS X-Ray Provides distributed tracing and backend performance monitoring Database: I used Supabase (Postgres) for storing users, document metadata, and extracted analysis results. Deployment: Automated using AWS CLI and SAM , triggered via PowerShell deployment scripts located in each Lambda directory. Challenges I Ran Into Document Format Variability: Medical documents came in various formats (PDFs, scans, handwritten notes). Fine-tuning Textract and AI prompts was critical. AI Accuracy & Validation: Tuning the Bedrock RAG Agent and AI logic to accurately map medical findings to VA disability criteria took several iterations. Scalability: Ensuring the system could process large document uploads without timeouts or failures required building a chunked and queue-driven backend flow . Security & HIPAA Compliance: I worked hard to implement end-to-end encryption , data minimization , and secure storage practices to protect veteran data. Accomplishments I'm Proud Of Built a fully serverless, production-ready system using AWS Lambda , Textract , S3 , Bedrock , and Supabase . Delivered AI-powered VA disability rating estimates for veterans in near real-time. Successfully integrated distributed tracing (X-Ray) and event-driven workflows (SQS, SNS) for scalable backend processing. Created an accessible, veteran-friendly UI that works on both desktop and mobile. What's Next for VA Rating Assistant - Bolt.new Public Launch: Launch the production version at https://www.varatingassistant.com . Deeper VA API Integrations: Integrate with VA Benefits APIs for live service history and claim status checks. Auto-Fill VA Forms: Let users download pre-filled VA disability forms (e.g., 21-526EZ) based on detected conditions. AI Appeals Helper: Develop an AI-driven assistant to help veterans understand why their claim was rated a certain way and how to appeal. Mobile App: Begin building a React Native app for iOS and Android users. Advanced AI Features: Roll out a paid tier with features like symptom trend tracking , AI-guided form prep , and VA citation mapping . Visit my website to learn more about how VA Rating Assistant helps veterans navigate the VA disability claims process with confidence and clarity. <div