---
slug: "homeworthai"
url: "https://devpost.com/software/homeworthai"
title: "HomeWorthAI"
hackathon: "Nosu AI Hackathon $11,300+ in prizes"
organization: "nosu"
winner: true
words: 414
team_size: 2
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/retrieval_grounding"
  - "domain/disaster_emergency"
  - "domain/education"
  - "domain/finance_payments"
  - "domain/supply_logistics"
  - "substrate/video_visual"
---

# HomeWorthAI

> A web app that helps California fire victims jog their memory to make insurance claims

[Devpost](https://devpost.com/software/homeworthai) · hackathon [[Nosu AI Hackathon -11-300- in prizes]]

## Facets

**mechanism** [[retrieval_grounding]]
**domain** [[disaster_emergency]] [[education]] [[finance_payments]] [[supply_logistics]]
**substrate** [[video_visual]]

**stack** ai, fastapi, pinecone, python, rag, typescript

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for homeworthai

## Body

codebuff 2 codebuff 1 Inspiration The tragic fire in California gave us an idea to help out victims file insurance claims, considering the overwhelming emotional toll of losing a house and just being in shock will make the insurance claiming process very difficult. What it does We developed a web app that analyzes your iMessage chat logs/images to help you locate and recall important items. With an integrated chatbot, the app engages in a conversation to jog your memory and provide insights about where your belongings might be. How we built it We built it using RAG converting the important messages with key words of valuable/important items into embeddings which the RAG AI can look through when you ask it one of those key words. The cool thing with RAG is that it uses various contexts by cross-referencing authoritative knowledge sources . We implemented a FastAPI backend to integrate with the AI using Python. For the frontend we used Vite, shadcn, Tailwind , and CodeBuff to assist us in making the UI/UX as beautiful and responsive as possible. Challenges we ran into Our biggest challenge was figuring out how to jog someone’s memory about items when they don’t have clear information. Our solution was to analyze iMessage data; why iMessage, you ask? Because it often contains everyday conversations like, “Hey, can you lower the TV? I can hear it from upstairs,” or a parent texting, “Did you turn on the microwave in the kitchen?”. However due to Apple's privacy, we couldn't simply extract chatlog/image information from an iPhone, we had to make a backup and upload the manifest.db which then gave us the location to sms.db, which then had the chatlogs we were looking for. Accomplishments that we're proud of Finishing this project was something we're super proud of since we put a lot of time and effort into it, we also stayed up till 3am over the past few days just to get this done. Working on this alongside school and applying for internships was pretty difficult but we're proud of the final product and how seamless everything works even when we thought it was cooked. What we learned Building with an RAG AI taught us so much about embeddings, vectors and much more. What's next for HomeWorthAI We're thinking about making this a stronger and better app to eventually propose to others and help out victims of wildfires. We're also going to try and deploy this for others to test out! <div