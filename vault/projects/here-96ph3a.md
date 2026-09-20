---
slug: "here-96ph3a"
url: "https://devpost.com/software/here-96ph3a"
title: "Here"
hackathon: "Google Cloud Gemini Hackathon"
organization: "Google"
winner: true
words: 880
team_size: 1
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/cross_origin_web"
  - "mechanism/realtime_stream"
  - "domain/developer_tools"
  - "domain/finance_payments"
  - "domain/security_privacy"
  - "user/developer"
  - "user/general_public"
  - "substrate/document_pdf"
  - "substrate/web_dom"
---

# Here

> A Chrome extension to help users navigate complex loan applications, offering timely tips, simple summaries, and a chatbot to support confident, informed choices—even in life’s toughest moments

[Devpost](https://devpost.com/software/here-96ph3a) · hackathon [[Google Cloud Gemini Hackathon]]

## Facets

**mechanism** [[cross_origin_web]] [[realtime_stream]]
**domain** [[developer_tools]] [[finance_payments]] [[security_privacy]]
**user** [[developer]] [[general_public]]
**substrate** [[document_pdf]] [[web_dom]]

**stack** gemini, nestjs, react, typescript, vertexai

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- what's next for "here"

## Body

GIF Chat for On-Demand Assistance GIF Instant Summarisation for Key Insights Inspiration As a software developer in finance, I've witnessed firsthand how a car loan or mortgage can significantly shape a person’s life, sometimes for better, sometimes for worse. It’s clear that these decisions require careful consideration, yet vulnerable users often struggle with the complexity of loan applications. With the recent FCA consumer duty standards, the responsibility to support all customers—especially those who face unique challenges—has only grown. I've long been inspired to create a tool that could empower people to make better, more informed loan decisions. What it does Here is a Chrome extension, easily accessible with a single installation. Once installed, it seamlessly integrates with any websites to provide real-time support throughout the loan application process. Detecting Vulnerable Interactions and Generating Insights To assist users effectively, Here monitors interactions to identify signs of vulnerability—like repeated clicks on the same content or frequent backtracking in input fields. When Here detects these patterns, it interprets the selected content and also web context to offer helpful insights with the help of Gemini. Instant Summarisation for Key Insights The second feature of Here is its powerful summarisation tool. With just a quick highlight of any part of a website—like offer documents, mortgage illustration or terms and conditions, etc—users can generate clear, concise summaries. This feature is especially helpful for those who find it challenging to focus on dense information, allowing them to grasp the essentials quickly. By breaking down complex details, Here helps users understand key points at a glance, making it easier to seek advice and make informed decisions when needed. Chat for On-Demand Assistance Here also includes a built-in chatbot for times when users need deeper insight. After receiving tips or a summary, if the user feels they need more information, they can simply start a chat with Here to ask specific questions. This feature allows users to explore topics further, clarify uncertainties, and gain the additional guidance they need to make well-informed choices confidently. 👀 Watch the demo here How we built it How I Built the Extension with Vertex AI To create Here , I focused on generating clear, helpful outputs for users. I used two types of system prompts: one to generate targeted tips based on user interactions and another to produce concise summaries for highlighted content. To give the prompts additional context, I included relevant HTML code from the website, allowing Here to interpret and respond more accurately based on the page’s content. Additionally, I implemented a markdown output as part of the system prompt, allowing Here to deliver responses in a cleaner, more user-friendly format. This markdown formatting improves readability and enhances the user experience by making complex information easier to digest at a glance. Tech Stack Backend Google Vertex AI: Generate insights and summaries for selected content NestJS: To interact efficiently with the Vertex AI API, enabling real-time responses and accurate information retrieval Frontend React: For the content scripts that handle vulnerability detection, insight generation, and chat assistance, ensuring a seamless user experience on the frontend Repo Structure I also adopted monorepo pattern, allowing me to create and share reusable functions across various parts of the project. This setup not only streamlined development but also made maintenance and scaling more efficient. Challenges we ran into Building Here came with a few key challenges. One major hurdle was detecting vulnerabilities, as each user’s interaction patterns are unique. It was difficult to create a perfect system for identifying vulnerable users, so I focused on the most common indicators—such as repeatedly clicking on the same content or frequently editing and deleting within an input. Another challenge was designing a user interface that feels seamless across various websites. Different sites come with distinct layouts and styles, making it tough to ensure a consistent, smooth experience. Additionally, I didn’t have enough user data to fully drive the experience, which meant relying on assumptions and early-stage testing to refine how Here could best serve vulnerable users. Overcoming these challenges required iterative testing and refinement to make Here as effective and user-friendly as possible. What's next for "Here" Looking ahead, we plan to enhance the Here Chrome extension in several impactful ways: Data Collection and Analysis Integrate features to collect anonymous interaction data, helping to refine insights into user behaviour and needs. This data will guide the enhancement of vulnerability detection and the customisation of assistive features. Prediction of Vulnerable Behaviours Collaborate with Vertex AI to leverage predictive analytics, using data to better anticipate and respond to vulnerable behaviours, enhancing the overall user experience. SDK Extension for Banks and Lenders Develop Here as a SDK, enabling seamless integration with banks and lenders. This adaptation will support financial institutions in offering tailored assistance to their vulnerable customers, aligning with the FCA consumer duty standards for responsible and supportive financial guidance. Custom Model Development Work alongside financial partners to create custom models based on institution-specific data. This will enhance the relevance of insights for vulnerable users, improving decision-making support in alignment with the unique policies and products offered by each institution. Refinement of Prompting and Model Customisation Continue to refine prompts and, ideally, establish a custom model to more accurately support vulnerable users in making critical financial decisions with clarity and confidence. <div