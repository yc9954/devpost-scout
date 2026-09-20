---
slug: "livertracker-com"
url: "https://devpost.com/software/livertracker-com"
title: "LiverTracker.com"
hackathon: "Code with Kiro Hackathon"
organization: "Kiro"
winner: true
words: 958
team_size: 1
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "domain/health_clinical"
  - "user/clinician"
  - "user/patient_family"
  - "user/researcher"
  - "substrate/document_pdf"
  - "substrate/structured_db"
  - "substrate/video_visual"
---

# LiverTracker.com

> AI-powered app that helps liver disease patients track labs, trends & MELD score over time. Turning data into defense, so you can fight smarter, live longer, and never lose a report again.

[Devpost](https://devpost.com/software/livertracker-com) · hackathon [[Code with Kiro Hackathon]]

## Facets

**domain** [[health_clinical]]
**user** [[clinician]] [[patient_family]] [[researcher]]
**substrate** [[document_pdf]] [[structured_db]] [[video_visual]]

**stack** gmail-smtp, google-cloud, google-oauth, neon, next.js, nextauth.js, node.js, openai-api, postgresql, react, rest, typescript, vercel

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of

## Body

Home Page Patient Dashboard Checking Single Parameter Trends Report Library Report Upload Area Single Report Page AI Personalized Recommendation AI Summary AI Predictive Analysis AI Smart Insight MELD Score Child Pugh Doctor access area Consolidated shared report with doctor Inspiration In 2020, I was told I had advanced liver disease. I’d never even heard the word “cirrhosis” before. My doctor said: “You have maybe 2 years before you need a transplant — if you’re lucky.” I asked, “Why ‘lucky’?” He said: “Because for every liver that becomes available, 15 people are waiting. Every day, hundreds die… not from disease… but from waiting.” I refused to be a statistic. I started tracking every single lab report — manually, with spreadsheets and paper folders. Because I tracked — I caught small changes. I asked better questions. I showed my doctor what was happening. I’m still here today. My numbers are stable. Some are even better. I built LiverTracker so no patient has to go through this alone, scared, or lost in paperwork. What it does You take a photo or upload a PDF of your lab report — from any hospital, anywhere in the world. The app reads it for you — pulls out the key numbers: bilirubin, platelets, INR, creatinine, albumin, sodium, and more. It automatically calculates your MELD score — the number that decides your place on the transplant list — using the formula: ( \text{MELD} = 3.78 \times \ln(\text{Bilirubin}) + 11.2 \times \ln(\text{INR}) + 9.57 \times \ln(\text{Creatinine}) + 6.43 ) It shows you simple, clear charts — so you can see how your liver is changing over months or years. It warns you if something is going in the wrong direction: “Your platelets dropped — time to talk to your doctor.” It creates a clean, one-page summary you can share with your doctor — with your trends, scores, and notes. It saves your original report — so you never lose it, even after 10 years. How we built it I started by using my own 5 years of lab reports — I knew what I needed because I lived it. I didn’t know how to build an app — so I learned by doing, one small step at a time. My wife (a medical biologist) sat with me for months — she taught me what every number meant, why it mattered, and how doctors use it. We showed early versions to 3 liver specialists — they helped us make sure everything was accurate, safe, and useful. I tested every feature with real patients — people just like me — to make sure it was simple enough to use on your worst day. I designed it around one rule: “If you’re tired, scared, or overwhelmed — you should still be able to understand your health in 30 seconds.” Every button, every alert, every chart was built for the patient — not for the tech. Challenges we ran into I had no medical background — learning liver disease felt like learning a new language. Lab reports are messy — handwritten, blurry, sideways, full of stamps and notes — teaching the app to read them was hard. Every country does labs differently — units, ranges, formats — we had to make it work everywhere. Making sure doctors would trust it — and patients would understand it — was the biggest challenge. Balancing simplicity with accuracy — it had to be easy for a 70-year-old, but precise enough for a specialist. Building this while managing my own health — every feature was built between doctor visits and lab tests. Accomplishments that we're proud of I built this as a patient — with no team, no funding, no medical degree — and made something real people can use. The app can read messy, real-world lab reports — and pull out the right numbers — with high accuracy. Real patients used it — and caught warning signs early — leading to faster doctor visits and better care. Doctors who saw it said: “This is exactly what my patients need.” My wife — a scientist — reviewed every detail — so you know it’s not just an app… it’s medically sound. Most of all — I proved that patients can build the best tools for patients — because we live the problem every day. What we learned Liver disease is silent — but deadly. ** 2 million people die every year. 15 people die every day just waiting for a liver**. Tracking your labs isn’t just helpful — it’s life-saving. Studies show it can add 5+ years to your life. Your MELD score isn’t just a number — it’s your lifeline. It decides if you get a liver… or not. Technology in healthcare must be simple, kind, and human — not flashy or complicated. Collaboration is everything — my wife’s knowledge + doctors’ guidance + patient feedback made this real. Patients are the most powerful innovators — because our lives depend on getting it right. What's next for LiverTracker.com We’re building a mobile app — so you can track your labs from your phone, anywhere. We’ll add daily activity tracking — so you can see how walking, sleeping, or diet affects your liver. We’re creating a recipe section — with liver-friendly meals (like low-sodium Indian dishes) that actually help. We’ll add an “AI Health Coach” — to give you gentle, personalized tips based on your labs and habits. We’ll build a version for doctors and hospitals — so they can follow their patients’ progress easily. We’re going global — with support for Hindi, Spanish, Arabic, and local lab formats. Long-term — we want LiverTracker to be the reason why, in 10 years, fewer people die waiting… and more people live longer, better lives. <div