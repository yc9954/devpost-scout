---
slug: "mindful-moments-8h09cq"
url: "https://devpost.com/software/mindful-moments-8h09cq"
title: "Mindful Moments"
hackathon: "DeveloperWeek 2024 Hackathon"
organization: "DevNetwork"
winner: true
words: 762
team_size: 2
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/retrieval_grounding"
  - "domain/civic_government"
  - "domain/mental_health"
  - "substrate/code_repository"
  - "substrate/geospatial"
  - "substrate/web_dom"
---

# Mindful Moments

> Mindful Moments is a coaching/journaling app that uses AI & 7 sacred texts for guidance on issues like anxiety & depression, promoting self-awareness & emotional healing.

[Devpost](https://devpost.com/software/mindful-moments-8h09cq) · hackathon [[DeveloperWeek 2024 Hackathon]]

## Facets

**mechanism** [[retrieval_grounding]]
**domain** [[civic_government]] [[mental_health]]
**substrate** [[code_repository]] [[geospatial]] [[web_dom]]

**stack** convex, descope, mongodb, openai, radixui, react, vite, vonage

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for mindful moments

## Body

Home Page Responsive: Home Page Reason for journaling Mobile: Reason for journaling Sacred Texts to Reference Mobile: Sacred Texts to Reference Identify Feelings Mobile: Identify Feelings Tell me about it Retrieving response based on using RAG based on vectorized sacred texts selected Codacy: Issues + Coverage Descope: Authentication Vonage Flow for SMS Inspiration Mindful Moments was inspired by the collaboration of Alan Helmick, Natalie Pan and Melissa Pan. Alan's love of AI and his goal to make the world a place with more love instigated the idea to leverage sacred texts and ai to create soulful advice that soothes and comforts people. Natalie's previous work on her last startup Facets, focused on solving loneliness by helping people build self-awareness using ACT (Acceptance Commitment Therapy). Melissa's background in design and her atheist background made us come up with a product that anyone could use to soothe their soul. What it does Mindful Moments uses AI & 7 sacred texts for guidance on issues like anxiety & depression, promoting self-awareness & emotional healing. Users are guided to explore a topic of concern for them, what their sacred text preferences are, and how they're feeling. By identifying feelings we guide users to elaborate on the context around the issue before offering soulful advice based on what they told us. The app also has a simple ask anything prompt for those wishing to just ask questions in relation to sacred texts. Our goal is create a journaling app that helps the user reflect inwardly as well as get soulful advice to provide them loving advice. Inward reflection such as identifying one's feelings helps people build self awareness and is key in developing long term happiness. The format which invites them to journal daily, enables a habit of self reflection. The use of sacred texts can provide solace and comfort. The advice given through the text provides wisdom and inspiration. How we built it Frontend: Convex using Vite (React) SMS: Vonage : We also setup a flow such that you can text with our Sacred GPT watch demo here Backend: Azure PaaS scalable app service API Python/Javascript/Html RAG: Segment and vectorize 7 sacred texts stored in a vectorized MongoDB AI: GPT 4 via Pulze.ai, utilizes a 12 model LLM ops backbone for reliability Challenges we ran into It was the first time working together as a team. A lot of tooling and packages were all new. It was the first time to use any of the sponsors products. While Natalie is familiar with react, using Vite and radix UI was a first for her. Alan found the circular nature of the new Vonage interface to be challenging, the help pages do not have direct links to the pages they discuss, such as AI Studio, for example. However, the intuitive nature of their drag and drop flows and parameters was elegant and drives me back to create more. We will likely test out voice, sms and video flows, as time permits. I found Convex and DeScope to be useful and easy to implement and Ian was extremely helpful. We will continue on with the Convex project and implementing our onboarding wizards with Descope. A challenge we ran into use github pages for deployment was that it needed a base url to matched the repo. This messed with routing. Descope redirect also broke due to this. We didn't have time to solve this during production. Accomplishments that we're proud of The flow of the app is very smooth and inviting to users. We were able to get responses back based on the selected sacred texts. It actually works! We completed our first hackathon, as a team, and built out an entire solution. What we learned We learned that task planning is challenging when you are unfamiliar with the tools. I learned that Natalie is very adaptable. Alan learned that Convex is easy to use, as is Descope and that Vonage's intuitive Ai Studio, although elusive to find, is a treasure once you arrive there. We learned about each other and ways to improve our interactions also, which is invaluable for co-founders and... we had a good time! What's next for Mindful Moments We're continuing to develop out Mindful Moments to see what people would like from it. We will be creating user profiles that will have there own personalized RAG, such that the ai will remember their preferences and previous discussions. Using Descope to validate authentication will make this easier. We will also continue with scheduled interactions via Vonage and push notifications that give reminders, journaling and advice. <div