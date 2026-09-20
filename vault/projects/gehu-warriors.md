---
slug: "gehu-warriors"
url: "https://devpost.com/software/gehu-warriors"
title: "B2 - BizElevate"
hackathon: "TiE U - Hack@thon 2024"
organization: "TiE U"
winner: true
words: 620
team_size: 2
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "user/small_business"
  - "substrate/code_repository"
  - "substrate/structured_db"
  - "substrate/web_dom"
---

# B2 - BizElevate

> A Comprehensive Solution for Business Mentorship with Personalized AI Assistance.

[Devpost](https://devpost.com/software/gehu-warriors) · hackathon [[TiE U - Hack-thon 2024]]

## Facets

**mechanism** [[realtime_stream]]
**user** [[small_business]]
**substrate** [[code_repository]] [[structured_db]] [[web_dom]]

**stack** express.js, flask, lamallm, postgresql, python, react, tailwindcss

## How they structured the write-up

- what it does
- how we built it
- how our ai model (erica) works
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for bizelevate
- note

## Body

Business Software Tools BizElevate -Intro Key Features Erica, Personalized Business AI along with AI powered Tools. Mentorship Resource Business Community App Personalized Dashboard for AI assistance. AI Powered Business Tool AI Powered Inbound SDR(Erica) AI Powered Outbound SDR(Erica) Mentorship Resource How Our AI model works. (Overview) What our Business AI provide? Our Revenue Model What it does BizElevate is a dedicated platform designed to empower business owners by providing tailored mentorship to overcome their unique challenges. We believe every business journey is personal, and BizElevate is here to support, inspire, and guide owners to unlock their full potential. Through personalized AI-driven insights, we aim to give business owners the confidence to tackle even their toughest challenges, ensuring they’re never alone on their path to success. How we built it BizElevate was created with a vision to bridge the gap between business owners and AI-backed mentorship. We integrated the Lama open-source model, carefully fine-tuning it to focus on business-specific knowledge and challenges. This model was enhanced with curated insights to make it relevant and practical for today’s business needs, offering each user mentorship that feels custom-built for them. How our AI model (Erica) works Load and Fine-Tune Lama Model:- Load Lama: We use Hugging Face’s transformers library to access the Lama model and tokenizer. Fine-Tuning: Collect data specific to business challenges and mentorship scenarios. Then, fine-tune Lama on this curated dataset to ensure the model understands business-specific language, advice patterns, and problem-solving approaches. This involves: Defining a small dataset of common challenges and solutions. Training the model to produce practical, actionable responses. Developing the Backend Using Flask and FastAPI Flask for Core Application: Set up Flask to manage the main web application interface, handling endpoints like login, signup, and user sessions. FastAPI for AI Endpoints: Use FastAPI for the AI model’s API due to its speed and asynchronous support. This setup helps handle multiple requests simultaneously and ensures responsiveness for AI queries. Integrating the AI Model with Flask and FastAPI Model Endpoint: Creating an API endpoint in FastAPI for processing user inputs, running them through the model, and returning responses. Session Management: Integrating with Flask to securely handle sessions and user data, passing inputs to the model endpoint as needed. Challenges we ran into As with any ambitious project, time was our biggest hurdle. Limited time constrained our ability to complete the full AI integration we envisioned. But these challenges only fueled our resolve, showing us just how valuable this platform could be. Accomplishments that we're proud of We’re thrilled to have brought our vision to life within a tight timeframe. From creating a fully functioning, interactive webpage to building a robust backend and implementing a business-focused AI model, each part of BizElevate is a product of dedication, teamwork, and our commitment to helping business owners succeed. What we learned Our journey with BizElevate highlighted how transformative AI can be for small businesses. By connecting business owners with tailored guidance, AI offers a helping hand in real time—helping businesses grow, adapt, and thrive in ways we hadn’t fully anticipated. This has shown us that the potential for AI-driven mentorship is boundless, especially for those passionate about growing their dreams. What's next for BizElevate Our vision for BizElevate is just getting started. Next, we plan to fully integrate a refined AI model and create a specialized ML model trained exclusively on real-world business problems and proven solutions. This will make BizElevate even more effective, reliable, and empowering—helping more businesses achieve their full potential with AI-driven guidance tailored precisely for them. Note Please be aware that the login and signup functionalities may take up to 1 minute to respond, as server is currently deployed on a free-tier infrastructure. We appreciate your understanding. <div