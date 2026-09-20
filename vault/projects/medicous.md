---
slug: "medicous"
url: "https://devpost.com/software/medicous"
title: "Medicus"
hackathon: "HackGT 12: Midnight at the Museum"
organization: "HexLabs"
winner: true
words: 513
team_size: 4
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "domain/health_clinical"
  - "user/clinician"
  - "user/patient_family"
  - "substrate/structured_db"
---

# Medicus

> We’re revolutionizing how medical technology companies connect with healthcare providers: delivering the right information, to the right provider, at the right time.

[Devpost](https://devpost.com/software/medicous) · hackathon [[HackGT 12- Midnight at the Museum]]

## Facets

**domain** [[health_clinical]]
**user** [[clinician]] [[patient_family]]
**substrate** [[structured_db]]

**stack** cedar, docker, mastra, openai, perplexity, postgresql, python, react, react-email, schema-validation, typescript, zod

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of:
- what we learned
- what's next for medicus

## Body

Inspiration We were inspired by the challenge of improving HCP (Healthcare Provider) engagement. Doctors are often overwhelmed by irrelevant information, while sales reps spend time and money traveling to hospitals without knowing if their visit will add value. We wanted to create a solution that is smarter, more efficient, and more equitable: one that delivers the right information, to the right provider, at the right time. What it does Medicus is a digital platform that allows medical device sales reps to upload their products, complete with clinical research, safety data, and use cases. Using an AI search engine, doctors can easily preview relevant information before a sales visit. This helps doctors get the right information at the right time, while sales reps save resources and focus their visits on the hospitals that will truly benefit. How we built it We built Medicus with a modern, reliable stack that balances speed, scalability, and security. On the backend, we used Python for data processing and TypeScript for type-safe development, with PostgreSQL as our main database to manage device information, clinical research, and user data. We containerized everything with Docker to ensure smooth deployment and consistency across environments, while leveraging Cedar to define fine-grained access control policies for sensitive medical data. On the frontend, we built a responsive React application with Zod and schema validation to guarantee robust data integrity and API safety. To enhance engagement, we integrated React Email to deliver personalized device insights directly to healthcare providers. This stack enabled us to rapidly prototype while still building toward a system that can scale in real-world healthcare environments. Challenges we ran into A challenge we ran into was that we wanted to do something similar to what Impiricus does where they do not spam the doctors with a jargon of information and we also wanted to make sure they have the resources to benefit from this platform and it was hard to find a balance for it. We had to ideate different workflows that work equally well for sales reps and doctors, who have very different needs. Accomplishments that we're proud of: Built a functional prototype in under 36 hours. Designed a workflow that supports both reps and doctors while keeping patient impact at the center. Developed a socially impactful solution that could expand access to rural and underfunded hospitals. What we learned One of the most important things we learned was that the healthcare system is quite complex and due to its complexity navigating it to create a tool that can be used effectively is quite difficult. If the time constraint wasn't an issue having some user input or feedback would have been quite instrumental and we would like to thank the team at Impiricus for assisting us with feedback and ideas to add to our site. What's next for Medicus We think there are countless possibilities for our product, and one of the biggest things we would be excited for would be pitching it to med tech companies like Medtronic or J&J who might be interested in optimizing their current sales strategy. <div