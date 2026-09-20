---
slug: "cogni-adapt"
url: "https://devpost.com/software/cogni-adapt"
title: "COGNI-ADAPT"
hackathon: "DSH Hacks V1"
organization: "DreamWeave"
winner: true
words: 480
team_size: 1
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "domain/accessibility"
  - "domain/education"
  - "user/educator_student"
  - "user/researcher"
  - "substrate/document_pdf"
---

# COGNI-ADAPT

> Transforming how neurodiverse learners access and engage with educational content through AI-powered adaptive technology.

[Devpost](https://devpost.com/software/cogni-adapt) · hackathon [[DSH Hacks V1]]

## Facets

**mechanism** [[realtime_stream]]
  <sub>weak: revocation_withdrawal, vision_ocr</sub>
**domain** [[accessibility]] [[education]]
**user** [[educator_student]] [[researcher]]
**substrate** [[document_pdf]]
  <sub>weak: sensor_telemetry, video_visual</sub>

**stack** ai), amazon, amazon-web-services, artificial, aws), bedrock, intelligence, learning, machine, ml), scalable, services, textract, web

## Body

HOME PAGE Inspiration For 1 in 5 students, a traditional textbook isn't just boring—it's a barrier. We were inspired by the "Silent Struggle" of neurodiverse learners (ADHD, Dyslexia) who often never report their conditions to schools. With a dropout rate 3x higher for students with learning disabilities compared to their peers, we realized that the "one-size-fits-all" approach to education is failing. We wanted to build something that stops asking students to change their brains, and instead changes the content to fit them. What it does Cogni-Adapt is an AI-powered adaptive technology that democratizes education for every brain type. It takes "walls of text" from traditional educational PDFs and instantly transforms them into accessible, personalized learning experiences. Profile Matching: The user selects a cognitive profile (e.g., ADHD), and our AI analyzes their specific needs. Content Redesign: It converts dense paragraphs into bite-sized chunks, visuals, and infographics. Personalized Output: Each student gets content optimized for their unique learning style, removing barriers to entry. How we built it We leveraged a powerful, scalable technology stack centered on AWS: Ingestion: Users upload standard PDF documents. Extraction: We used AWS Textract to intelligently extract not just text, but the structure and images from the documents. Transformation: This data is passed to AWS Bedrock, where we utilize Generative AI models to match the content to the user's cognitive profile. Frontend: A "User-Centered Design" interface that presents the new, accessible content side-by-side with the original. Challenges we ran into Prompt Engineering for Neurodiversity: Tuning the LLM via AWS Bedrock to accurately distinguish between "simplifying" text (for general readers) and "optimizing" text (specifically for ADHD or Dyslexia) required deep iteration. Preserving Context: Ensuring that when the AI breaks down dense academic material into "bite-sized chunks," the core educational meaning remains accurate and doesn't lose academic rigor. Accomplishments that we're proud of Functional Pipeline: Successfully integrating AWS Textract and Bedrock to create a "scan-to-learn" workflow. Targeting Real Impact: Designing a tool that targets massive proven metrics: increasing pass rates to 94% (up from 66%) and reducing course withdrawal rates from 45% to 13% through adaptive learning. User-Centric UI: Creating an intuitive interface that adheres to accessibility standards, ensuring the tool itself isn't a barrier. What we learned We deepened our understanding of learning science—specifically that accessibility isn't just about font size, but about information architecture. We also learned the immense power of AWS Bedrock in acting as a real-time accessibility engine, capable of "translating" cognitive load in ways that static code never could. What's next for COGNI-ADAPT Market Expansion: We aim to tap into the $12.7B adaptive learning market by 2030. Institution Integration: Moving from a B2C tool to a B2B model, helping schools and universities improve retention and compliance automatically. Real-Time Feedback: Adding a layer where the AI learns from the student—if they skip a section, the AI adapts the next chapter to be even more engaging. <div