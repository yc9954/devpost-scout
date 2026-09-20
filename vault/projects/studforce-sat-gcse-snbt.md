---
slug: "studforce-sat-gcse-snbt"
url: "https://devpost.com/software/studforce-sat-gcse-snbt"
title: "StudForce - SAT,GCSE,SNBT"
hackathon: "Student HackPad 2025"
organization: "Student Hackpad"
winner: true
words: 906
team_size: 1
has_repo: true
has_live: true
has_video: false
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "domain/education"
  - "user/educator_student"
  - "user/researcher"
  - "substrate/structured_db"
---

# StudForce - SAT,GCSE,SNBT

> Study like you compete in a ranked game.

[Devpost](https://devpost.com/software/studforce-sat-gcse-snbt) · hackathon [[Student HackPad 2025]]

## Facets

**mechanism** [[realtime_stream]]
  <sub>weak: vision_ocr</sub>
**domain** [[education]]
  <sub>weak: finance_payments, transportation</sub>
**user** [[educator_student]] [[researcher]]
**substrate** [[structured_db]]

**stack** css, firebase, react, tlx

## Body

Menu Progress Analytics TryOuts and Events/ Simulations Submission Forum Inspiration StudForce was born from a real-world observation of the challenges faced by high school students in Indonesia, particularly 12th graders, in preparing for university entrance exams. Tests like TKA (Academic Competency Test) and the current SNBT (National Test-Based Selection) demand comprehensive preparation. However, students often feel overwhelmed, lacking structured guidance and access to in-depth explanations. This issue extends globally, where many students also struggle with preparations for international exams like the SAT and GCSE. We recognized that effective preparation requires not only a large question bank but also a supportive community and personalized guidance. We identified a gap between students' deep need to understand the concepts and the availability of tools that can explain every step of the answer, are adaptive, and easily accessible. What it does StudForce is an integrated learning platform designed to democratize academic exam preparation. The application focuses on four main pillars: Adaptive Learning and Deep Analytics: Students can start practicing from the easiest to the advanced difficulty levels. Each practice session is accompanied by detailed performance analysis, identifying their weaknesses and strengths in specific topics. Exclusive AI Assistant: Utilizing AI technology, StudForce provides intuitive and easy-to-understand step-by-step answer explanations for every question. This AI Assistant acts as a 24/7 personal tutor, ensuring students don't just memorize answers but truly master the concepts. Interactive Community Forum: The platform includes a forum where students can help each other, share tips, and discuss challenging questions in real-time, fostering a supportive ecosystem among peers. Multi-Exam Try Outs: We provide practice materials for national (TKA/SNBT) and international (SAT, GCSE) exams, making StudForce a comprehensive exam preparation solution. How we built it We built StudForce with a focus on scalability, a smooth user experience (UX), and advanced artificial intelligence integration. Initial Attempt & Pivot: The project initially began as a Flutter mobile application to leverage its cross-platform capabilities. However, due to hackathon time constraints and to ensure maximum accessibility across various devices without app store deployment issues, we made a crucial decision to pivot and develop it as a pure web application. Current Stack: The Frontend is built using React and Tailwind CSS to ensure a responsive, modern, and quickly accessible interface across devices. The Backend & Database utilizes Node.js with Firebase Firestore for real-time data management, crucial for the forum functionality and storing user performance data. The Core AI Assistant feature is powered by the Gemini API, which enables us to generate accurate, narrative, step-by-step explanations. We designed a specific system instruction for the AI model to ensure its explanations are always educational, supportive, and relevant to the respective exam curricula. For Data Architecture, we implemented a flexible database schema to categorize questions based on subject, difficulty level (Easy, Medium, Advanced), and exam type, which forms the basis of our adaptive learning system. Challenges ran into The biggest challenge we faced was creating an accurate and consistent AI explanation system for a diverse range of questions, from mathematics to verbal comprehension. Optimizing the prompting and configuration of the Gemini API to ensure responses were always in a pedagogical, step-by-step format required extensive iteration. Additionally, managing real-time data traffic for the community forum feature was a significant technical hurdle to ensure low latency and a smooth user experience. Finally, the mid-hackathon pivot from Flutter to a web application added time pressure and required a complete re-implementation of the user interface. It is made worse when we werent able to fully implement backend and Authentication Accomplishments that we're proud of We are most proud of the immediate, real-world validation of StudForce: seeing our friends and peers actively use and gain tangible value from the app. A highlight was seeing users rely on StudForce to successfully tackle a large 50-question Math assignment with a tight deadline, proving the platform's reliability as a critical study tool under pressure. This positive peer adoption confirms that we've built something truly useful. Beyond adoption, we are incredibly proud of successfully integrating the AI Assistant as a runnable and reliable core feature. The ability to click any question and instantly receive a clear, step-by-step explanation is a key achievement that fundamentally differentiates StudForce from traditional practice platforms. We also successfully designed and implemented a concise yet informative analytics interface, allowing students to clearly visualize their progress. Furthermore, we are proud to have completed the entire project, including the pivot, within the hackathon timeframe, demonstrating our team's capability for rapid and focused execution. What we learned This project provided valuable lessons on the power of Artificial Intelligence API integration in creating personalized learning experiences. We learned that careful data modeling is crucial for a functional adaptive learning system. We also strengthened our understanding of developing full-stack applications that prioritize low latency for real-time collaborative features, and the importance of early user feedback in refining the quality of AI explanations. The experience of making a decisive technical pivot (from Flutter to web) highlighted the necessity of agility and prioritizing Minimum Viable Product (MVP) delivery over initial platform preference. What's next for StudForce - SAT, GCSE, SNBT Moving forward, we have ambitious plans for StudForce: Full Adaptive Testing Feature, Developing a more sophisticated adaptive learning algorithm where the system automatically adjusts the difficulty of the next question based on the student's live responses. StudForce will continue to evolve into a tool that not only helps students pass exams but also builds genuine confidence and subject mastery. <div