---
slug: "interview-edge"
url: "https://devpost.com/software/interview-edge"
title: "Interview Edge"
hackathon: "Amazon Nova AI Hackathon"
organization: "Amazon"
winner: true
words: 536
team_size: 2
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "domain/education"
  - "user/educator_student"
  - "substrate/code_repository"
  - "substrate/document_pdf"
  - "substrate/geospatial"
  - "substrate/structured_db"
  - "substrate/transcript_audio"
---

# Interview Edge

> Interview Edge – Your personal AI interview coach

[Devpost](https://devpost.com/software/interview-edge) · hackathon [[Amazon Nova AI Hackathon]]

## Facets

**domain** [[education]]
**user** [[educator_student]]
**substrate** [[code_repository]] [[document_pdf]] [[geospatial]] [[structured_db]] [[transcript_audio]]

**stack** amazon-web-services, amplify, api-gateway, css, javascript, lambda, python, yaml

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for interview edge

## Body

Inspiration The inspiration came from a simple idea: how do students and professionals prepare for interviews? Most candidates walk into interviews underprepared, not because they lack ability, but because they've never had a safe space to practice. We wanted to build something that gives everyone, regardless of background or budget, access to a realistic, personalised mock interview experience. What it does Interview Edge is AI powered mock interview application. You upload your CV and the job description for the role you're applying to, and the app conducts a tailored interview. It generates questions specific to your background and the role using Amazon Nova, reads them aloud, listens to your spoken answers via the browser's speech recognition, and produces personalised feedback at the end. How we built it The frontend is a React app hosted on AWS Amplify, using the browser's built-in Web Speech API for voice interaction. The backend is a FastAPI application running on AWS Lambda, wrapped with Mangum, so it can handle API Gateway proxy requests. Amazon API Gateway routes all HTTP calls from the frontend to Lambda. The AI layer uses Amazon Bedrock with the Nova Lite model for both question generation and feedback. We built a Lambda layer with Linux-compatible binaries to support PDF parsing (PyPDF2) and DOCX parsing (python-docx), so users can upload job descriptions and CVs in any common format. Challenges we ran into A few things did slow us down. Getting the lambda layer ready for PDF/DOCX parsing was quite difficult. We had to use specific pip commands to download the libraries and create a compatible layer. During user testing, we noticed that users found it difficult to end the interview session. Based on this feedback, we improved the interaction by updating our JavaScript and CSS to make the session exit more intuitive. We also hit an issue where the feedback was penalising users for the last generated question, which was being included in the transcript even when the user ended the interview before answering it. We had fixed it by tweaking our logic in the lambda function code. Accomplishments that we're proud of Getting a fully serverless, voice-driven interview app working end-to-end with no persistent storage is something we're genuinely pleased with. The fact that Nova never repeats a question within a session, because we pass the full question history in every prompt, makes the experience feel much more like a real interview. We're also proud of the privacy architecture: no database, no S3, no user data retained anywhere. It's a meaningful commitment for an app that handles sensitive career documents. What we learned We learned how much prompt engineering matters for LLM-powered features. The difference between a vague feedback prompt and one that gives Nova the job description and CV context and an instruction to be fair to speech transcripts, was significant in output quality. In addition, we gained hands-on experience with AWS Amplify, which enabled us to seamlessly host and deploy the application. What's next for Interview Edge We would like to add question categories: behavioural, technical, situational - so users can focus on specific areas. Multilingual support is a natural next step, given that the Web Speech API and Bedrock both support multiple languages. <div