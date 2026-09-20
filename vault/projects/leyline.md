---
slug: "leyline"
url: "https://devpost.com/software/leyline"
title: "Leyline"
hackathon: "Cal Hacks 11.0"
organization: "Cal Hacks"
winner: true
words: 406
team_size: 1
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "user/general_public"
  - "substrate/structured_db"
---

# Leyline

> An AI email assistant that automates form-filling, summarizes messages, and streamlines inbox tasks

[Devpost](https://devpost.com/software/leyline) · hackathon [[Cal Hacks 11.0]]

## Facets

**mechanism** [[realtime_stream]]
**user** [[general_public]]
**substrate** [[structured_db]]

**stack** drizzle, google-cloud, groq, nextjs, shadcn, supabase, tailwind, typescript

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for leyline

## Body

title home page email screen Inspiration The inspiration for Leyline came from The Interaction Company of California's challenge to design an AI agent that proactively handles emails. While Google's AI summarization features in their email app were a good start, we felt they lacked the comprehensive functionality users need. We envisioned an agent that could handle more complex tasks like filling out forms and booking flights, truly taking care of the busy work in your inbox. What it does Leyline connects to your Gmail account and parses incoming emails. It uses AI models to analyze the subject, body text, and attachments to determine the best course of action for each email. For example, if there's a form attached with instructions to fill it out, Leyline completes the form for you using information from our database. How we built it We developed Leyline as a Next.js app with Supabase as the backend. We use Google Cloud Pub/Sub to connect to Gmail accounts. A custom webhook receives emails from the Pub/Sub topic. The webhook first summarizes the email, then decides if there's a possible tool it could use. We implemented Groq's tool-calling models to determine appropriate actions, such as filling out attached forms using user data from our database. The frontend was built with Tailwind CSS and shadcn UI components. Challenges we ran into Processing Gmail messages correctly was challenging due to conflicting documentation and inconsistent data formats. We had to implement workarounds and additional API calls to fetch all the necessary information. Getting the tool-calling workflow to function properly was difficult, as it sometimes failed to call tools or missed steps in the process. Accomplishments that we're proud of We created an intuitive and visually appealing user interface. We implemented real-time email support, allowing emails to appear instantly and their processing status to update live. We developed a functional tool workflow for handling various email tasks. What we learned This was our first time using Google Cloud Pub/Sub, which taught us about the unique characteristics of cloud provider APIs compared to consumer APIs. We gained experience with tool-calling in AI models and learned about its intricacies. What's next for Leyline We plan to expand Leyline's capabilities by: Adding more tools to handle a wider variety of email-related tasks. Implementing a containerized browser to perform tasks like flight check-ins. Supporting additional email providers beyond Gmail. Developing more specialized tools for processing different types of emails and requests. <div