---
slug: "rewise-ai-powered-revision-bot"
url: "https://devpost.com/software/rewise-ai-powered-revision-bot"
title: "ReWise: AI-powered revision bot."
hackathon: "Facebook Hackathon: Messaging"
organization: "Facebook"
winner: true
words: 422
team_size: 1
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/vision_ocr"
  - "domain/education"
  - "user/educator_student"
  - "user/legal_professional"
  - "substrate/document_pdf"
  - "substrate/video_visual"
---

# ReWise: AI-powered revision bot.

> An interactive and powerful messenger bot to be your revision buddy.

[Devpost](https://devpost.com/software/rewise-ai-powered-revision-bot) · hackathon [[Facebook Hackathon- Messaging]]

## Facets

**mechanism** [[vision_ocr]]
**domain** [[education]]
**user** [[educator_student]] [[legal_professional]]
**substrate** [[document_pdf]] [[video_visual]]

**stack** facebook-messenger, flask, node.js, ocr, quillionz, tesseract

## How they structured the write-up

- inspiration
- what it does
- how i built it
- challenges i ran into
- accomplishments that i'm proud of
- what i learned
- what's next for rewise: ai-powered revision bot.

## Body

Inspiration Being a beginner to web development, I was excited to work on a project involving a lot of web-related concepts, leveraging APIs, computer vision and at the same time making something that I could use every day. What it does Exam time can be stressful for students and teachers who are bogged down with cramming material or setting questions. ReWise is a messenger bot that works in a super-easy and friendly manner to solve this problem. One can click a picture of the notes/study material and then generate a bunch of quiz questions to assess how well one has assimilated the material. The quiz once generated can either be taken live or can be mailed around to your email address. This allows for not just students but for educators to also catch a break! Making a bot for this use case makes sense as we all would love to get an experience as close to the exam scenario as possible without consequences and the fear of being judged. Having a personal bot at your disposal solves exactly that! How I built it Used the messenger platform, with Node.js for the backend. To extract the text from the images sent, I have hosted a simple OCR Flask app that does some pre-processing in OpenCV and uses the tesseract engine. The text extracted is then stored and passed to the Quillionz API which generates questions based on the text sent. Used node mailer for emailing. Used PDFkit library for generating PDFs of the question paper and answer key. Maintained user state in SQLite. Challenges I ran into It got tedious to maintain and update the state of the user as the messenger platform uses webhooks. Callbacks got pretty nested. Connecting all the APIs and making everything work smoothly. (PS: The mailer option is not available due to a security issue. However, the main code for the feature is available in the repo.) Accomplishments that I'm proud of I'm really satisfied with the amount of code I could churn out in a short amount of time. Learnt lots of nitty-gritty details of web development. Glad that I could put up an end to end product. What I learned Learned how to make an interactive messenger bot. Learned how to host web apps and make API calls in and around. What's next for ReWise: AI-powered revision bot. Incorporate NLP to make the conversation more natural. Allow for customizable quiz formats and time them too. Extend functionality to even topics like mathematics, visual subjects etc. <div