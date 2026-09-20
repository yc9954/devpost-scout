---
slug: "punjab-sabak-portal"
url: "https://devpost.com/software/punjab-sabak-portal"
title: "Punjab sabak portal"
hackathon: "DSH Hacks V1"
organization: "DreamWeave"
winner: true
words: 1217
team_size: 1
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "mechanism/retrieval_grounding"
  - "mechanism/sensor_fusion"
  - "mechanism/simulation_digital_twin"
  - "mechanism/vision_ocr"
  - "domain/developer_tools"
  - "domain/education"
  - "domain/media_journalism"
  - "user/developer"
  - "user/educator_student"
  - "substrate/document_pdf"
  - "substrate/sensor_telemetry"
  - "substrate/structured_db"
  - "substrate/video_visual"
---

# Punjab sabak portal

> A safe AI study platform with course-locked guardrails. Generates targeted MCQs, checks handwritten papers via photo upload, exports parental analytics PDFs, and features gesture-mouse control.

[Devpost](https://devpost.com/software/punjab-sabak-portal) · hackathon [[DSH Hacks V1]]

## Facets

**mechanism** [[realtime_stream]] [[retrieval_grounding]] [[sensor_fusion]] [[simulation_digital_twin]] [[vision_ocr]]
**domain** [[developer_tools]] [[education]] [[media_journalism]]
**user** [[developer]] [[educator_student]]
**substrate** [[document_pdf]] [[sensor_telemetry]] [[structured_db]] [[video_visual]]

**stack** ai, api

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for punjab sabak portal

## Body

Inspiration As an intermediate student myself, this project comes from my own personal struggles. Back in high school, my priority was always to get the best possible education while spending as little money as possible. Yet, I still ended up paying out of pocket for static, boring model papers just to prepare for exams. I realized we need something better to replace these outdated resources—something students would actually find worth investing their time and money into. Another huge issue is classroom learning. When we don't understand a concept and ask a human teacher to explain it again, they can get frustrated. Even if they try, their explanation is often exactly the same every time, which doesn't help if you didn't get it the first first time. I wanted to build an AI teacher that has infinite patience—one that will explain a concept a hundred times, changing its approach and trying different ways until the student finally gets it. During my own exams, I tried studying with Gemini and ChatGPT, but I ran into a massive problem: they constantly hallucinated chapters and topics that didn't even exist in my syllabus. I had to keep my textbook PDF open in another tab just to fact-check the AI. It was exhausting, you lose track easily, and if you don't know how to write a perfect prompt, the AI doesn't teach you well anyway. That is why I decided to build a system that locks the AI strictly to the actual textbooks. It doesn't just teach; it generates targeted MCQs, creates subjective exam questions, and tracks study time. For students who hate typing answers on a computer, they can simply solve the questions on real paper, snap a photo, and upload it for the AI to grade and store their marks. We also wanted a parent portal that automatically sends study reports over WhatsApp, but due to budget constraints for this hackathon, we built it to generate a clean PDF report instead—and I am incredibly proud that every single one of these features is fully working in our shared prototype link right now! Looking ahead, we are ready to launch our production-ready RAG system. While building this prototype, I pushed myself to learn how vector databases work, how to chunk data properly, and how to use specialized libraries to convert PDF textbooks into Markdown format before storing them in databases like Chroma. I’ve practiced this workflow thoroughly, and I’m ready to scale it up or try even better databases to take this platform global. What it does Our goal is to build the ultimate AI teacher—one with infinite patience that can explain a concept a hundred different ways until a student truly gets it. The entire platform is fully working, interactive, and testable right now. While it currently features 12th-class textbooks for this prototype phase, the flawless execution of these features proves that a full, production-ready version covering all grade levels is right around the corner. Sabak Portal is built around three core pillars and an innovative accessibility framework: Course-Locked AI Tutor: Students select their class and subject from a clean sidebar to open the learning screen. The underlying AI is strictly restricted to the textbook content. It focuses entirely on the syllabus at hand, and if a student asks an off-topic question, the AI safely blocks it and replies, "No, this is not in your course." Automated Evaluation Pipeline: The portal instantly generates targeted MCQs or subjective questions for a specific chapter or the entire book. It doesn't just create tests; it evaluates them, scores them, and logs the marks. For subjective exams, students who prefer not to type on a keyboard can simply write their answers on real paper, snap a photo, and upload the image for the AI to grade. Parental Telemetry Dashboard: The system tracks user engagement metrics and study time to generate comprehensive PDF reports for parents. While it currently exports as a PDF, our future roadmap includes sending these updates directly over WhatsApp. As we scale and secure a larger budget, we plan to integrate services like Twilio and ElevenLabs to deliver automated, real-time audio phone calls directly to parents. Hands-Free Gesture Navigation: To ensure digital accessibility, we integrated a computer-vision hand-gesture mouse control for desktop users. Currently in a fully functional beta, this feature uses the device's camera to track hand movements across the screen. Users can navigate the entire interface and trigger standard mouse clicks simply by pinching their thumb and index finger together. How we built it The platform is fully working, interactive, and testable. AI Backend: Powered by Google AI Studio , utilizing advanced system instructions and context caching to strictly enforce course boundaries without relying on heavy external database lag. Frontend Ecosystem: Built with a responsive sidebar-to-main-view architecture allowing seamless subject shifting. Vision & Accessibility: Integrated specialized web-camera tracking libraries to capture hand movements in real-time, translating coordinate shifts into standard mouse clicks. Challenges we ran into Enforcing absolute strictness on the AI model to prevent it from answering out-of-course questions was our biggest hurdle. Without a formal RAG database backend fully configured, we had to rely heavily on precise, rigid prompting frameworks within Google AI Studio. Ensuring that the system maintained a flawless "guardrail" state while simultaneously handling complex image OCR uploads and checking handwritten subjective answers required deep architectural experimentation, but we successfully built it into a fully testable state. Because my ultimate goal for this platform is to implement full RAG technology, this hackathon pushed me to dive deep into vector databases. I learned so many advanced concepts and grew as a developer entirely because of this competition, and I truly enjoyed every bit of the challenge. Accomplishments that we're proud of I am incredibly proud that every single feature described is fully operational in my prototype. Building a multi-faceted application that successfully handles visual camera streams for accessibility, image uploads for handwritten evaluation, and strict course-locking guardrails within a short hackathon window is a massive milestone for me. What we learned We learned how to maximize the raw power of Google AI Studio's logic parameters to simulate production-grade security boundaries. We also deeper understood the importance of universal design—adding the gesture-controlled mouse taught us that the future of educational technology must be accessible to students of all physical abilities. What's next for Punjab sabak portal While our prototype is fully testable, our next immediate step is migrating our prompt-guardrails into a dedicated Vector Database infrastructure using a production-ready Retrieval-Augmented Generation (RAG) architecture. We also plan to optimize our handwritten OCR pipeline to recognize varying qualities of handwriting and regional languages, eventually rolling out the application to schools across the region. Our vision extends beyond Pakistan; we are developing this platform for a global market. This international scale allows us to offset API server costs efficiently while generating the initial revenue needed to launch our careers. This project is not a get-rich-quick scheme; it is a focused solution to a real problem designed to establish a steady cash flow. Achieving success here will grant us the financial freedom to pursue a vast ocean of future opportunities. We are currently at the dawn of the AI era—much like the early days of personal computing—and we plan to leverage this technology to bring our biggest ideas to life. <div