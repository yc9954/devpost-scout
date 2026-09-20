---
slug: "sign-clarity"
url: "https://devpost.com/software/sign-clarity"
title: "Sign-Clarity"
hackathon: "Dropbox Sign AI-Powered Agreements Hackathon"
organization: "Dropbox"
winner: true
words: 622
team_size: 1
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/cross_origin_web"
  - "mechanism/on_device_local"
  - "mechanism/realtime_stream"
  - "mechanism/vision_ocr"
  - "domain/legal_justice"
  - "substrate/document_pdf"
  - "substrate/web_dom"
---

# Sign-Clarity

> AI powered Chrome extension that simplifies complex legal document

[Devpost](https://devpost.com/software/sign-clarity) · hackathon [[Dropbox Sign AI-Powered Agreements Hackathon]]

## Facets

**mechanism** [[cross_origin_web]] [[on_device_local]] [[realtime_stream]] [[vision_ocr]]
**domain** [[legal_justice]]
**substrate** [[document_pdf]] [[web_dom]]

**stack** bulmacss, css, html, huggingface, javascript, llama2, sanic, textparsing

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for sign-clarity

## Body

If you open sign-clarity on any other page than dropbox sign page Option to analyse document using Sign-Clarity when you are on document signing page Simplified summary of the document using AI with button to analyse clauses in the document List of tags to analyse with AI Simplified version of the clause using AI Ask a question to the clause to get clarity Get answer of the question using AI Simplified version of the clause using AI Make sure you have reviewed all the clauses You have reviewed the document page Inspiration The inspiration behind Sign-Clarity was the realisation that complex legal agreements often pose challenges for individuals trying to understand them fully before signing. We wanted to create a tool that simplifies these agreements and provides users with the clarity they need to make informed decisions. What it does Sign-Clarity is a chrome extension designed to assist users in understanding and reviewing complex legal documents before signing them. It offers the following functionalities: Contextual Awareness: When the user is on any webpage other than the Dropbox signing document page, Sign-Clarity prompts them to open a Dropbox Sign document and click on SignClarity. Document Analysis: When the user is on a signing document page, Sign-Clarity detects this and presents a "Analyze with Sign Clarity" button. Clicking this button initiates the document analysis. Clause Simplification: After document analysis, Sign-Clarity breaks down the document into clickable tags representing individual legal clauses. Clicking on a tag provides a simplified explanation of the clause. AI Interaction: Users can ask questions/chat about specific clauses to the integrated AI. The AI provides clear and concise answers, enhancing the user's understanding of the agreement. Completion and Signing: Once the user is satisfied with their understanding of the document, they can indicate their satisfaction and proceed to sign the agreement. How we built it Sign-Clarity was built by leveraging our expertise in Chrome extension development, AI, backend, and frontend technologies. The tech stack includes: Frontend: HTML, CSS, and JavaScript for the user interface. Backend: Python(Sanic) for handling AI interactions and document analysis. AI: Text preprocessing, OCR recognition from pdf, Natural Language Processing (NLP) and Machine Learning (ML) to simplify legal clauses and provide accurate responses to user queries. Used llama2 open source model. Integration: Integration with the Dropbox Sign API for document access and signing. Challenges we ran into Developing Sign-Clarity presented several challenges: AI Integration: Ensuring the AI accurately understood and simplified legal clauses required prompt engineering. Real-time Interaction: Implementing real-time AI interactions within a browser extension demanded seamless integration. User Experience: Designing an intuitive user interface that guides users effectively was crucial. Struggled a lot to make the extension look pleasing to the eye Deployment: Various free hosting platforms have different restrictions for response time, api calls etc So I decided to host it locally only and provide clear instructions for the use. Accomplishments that we're proud of We are proud of the following accomplishments: Developing a robust AI-powered system that simplifies complex legal language. Creating a user-friendly chrome extension that seamlessly integrates with Dropbox Sign. Enhancing user trust and confidence in signing agreements by providing clear explanations. What we learned The development of Sign-Clarity taught us valuable lessons in: AI/NLP model usage and prompt engineering for legal document understanding. Browser extension development for a smooth user experience. The importance of clear and concise communication in legal agreements. What's next for Sign-Clarity Enhance the AI's ability to handle more diverse legal documents. Implement user feedback mechanisms for continuous improvement. Explore options for mobile device compatibility to extend accessibility. May be create an app. Sign-Clarity is poised to revolutionize the way individuals interact with and understand legal agreements, making online document signing a more informed and transparent process. <div