---
slug: "scamscammer"
url: "https://devpost.com/software/scamscammer"
title: "ScamScanner"
hackathon: "UC Berkeley AI Hackathon 2024"
organization: "Cal Hacks"
winner: true
words: 494
team_size: 4
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "domain/finance_payments"
  - "substrate/structured_db"
---

# ScamScanner

> Introducing ScamScanner: an AI-powered solution to detect and block scam calls in real-time. Stay protected from fraud with our cutting-edge technology and user-friendly app. Your phone, safeguarded.

[Devpost](https://devpost.com/software/scamscammer) · hackathon [[UC Berkeley AI Hackathon 2024]]

## Facets

**mechanism** [[realtime_stream]]
**domain** [[finance_payments]]
**substrate** [[structured_db]]

**stack** amazon-web-services, flask, groq, hume, humeai, next, tailwindcss, typescript

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for scamscanner

## Body

Inspiration The inspiration for ScamScanner came from the increasing prevalence of scam calls, which have become a significant nuisance and security risk for individuals and businesses alike. With advancements in AI technology, we saw an opportunity to create a solution that can effectively detect and prevent scam calls, providing peace of mind and protecting people from potential fraud. What it does ScamScanner is an innovative application that leverages advanced AI models to detect and block scam calls in real-time. By analyzing call metadata and voice patterns, ScamScanner can identify suspicious activities and notify users of potential scams. The app also provides detailed reports and insights, helping users understand and manage their call security better. How we built it Frontend: Developed using Next.js to create a responsive and user-friendly interface. Backend: Implemented with Flask to handle API requests and integrate various AI models. AI Models: Utilized Groq, Llama 3 (8 billion parameters), Hume AI EVI, Hume AI EM, and a custom model from Hume AI to analyze voice data and detect scam patterns. Natural Language Processing: Integrated Anthropic Claude 3.5 Sonnit for advanced language understanding and contextual analysis. Data Storage: Employed AWS S3 for secure and scalable data storage. Dataset: Used the FTC Phone dataset to train and validate our models, ensuring they can accurately identify scam calls. Challenges we ran into Data Quality: Ensuring the FTC Phone dataset was clean, balanced, and representative of real-world scenarios. Model Integration: Integrating multiple AI models with different specializations and ensuring they work harmoniously. Real-Time Processing: Achieving low-latency processing to detect scam calls in real-time. Scalability: Designing the system to handle a large volume of calls without compromising performance. Accomplishments that we're proud of Successfully integrating state-of-the-art AI models to create a highly effective scam detection system. Developing a seamless and intuitive user interface that makes it easy for users to manage their call security. Achieving high accuracy in detecting scam calls, significantly reducing the number of successful scam attempts. Building a scalable solution that can handle large volumes of data and calls efficiently. What we learned The importance of high-quality datasets in training effective AI models. The complexities involved in integrating multiple AI technologies and ensuring they work together seamlessly. Best practices in designing real-time processing systems that can handle high loads without performance degradation. Insights into user behavior and needs regarding call security, which helped refine our product. What's next for ScamScanner Enhanced Features: Adding more features such as spam SMS detection, integration with other communication platforms, and personalized scam prevention tips. Global Expansion: Adapting the models to recognize scam patterns in different regions and languages, making ScamScanner a global solution. User Feedback Loop: Implementing a feedback mechanism where users can report false positives and negatives to continuously improve the system. Partnerships: Collaborating with telecom providers and regulatory bodies to enhance scam prevention at a broader level. Advanced Analytics: Offering detailed analytics and reporting tools for businesses to monitor and manage scam call threats effectively. <div