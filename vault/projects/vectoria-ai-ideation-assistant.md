---
slug: "vectoria-ai-ideation-assistant"
url: "https://devpost.com/software/vectoria-ai-ideation-assistant"
title: "VectorIA - AI Ideation Assistant"
hackathon: "Codegeist Unleashed"
organization: "Atlassian"
winner: true
words: 1081
team_size: 13
has_repo: false
has_live: false
has_video: true
tags:
  - "project"
  - "domain/developer_tools"
  - "domain/finance_payments"
  - "user/developer"
---

# VectorIA - AI Ideation Assistant

> Meet VectorIA, your innovation ally! We simplify complex idea creation and evaluation in Confluence. Powered by AI, we streamline ideation and evaluation. Drive innovation with VectorIA!

[Devpost](https://devpost.com/software/vectoria-ai-ideation-assistant) · hackathon [[Codegeist Unleashed]]

## Facets

**domain** [[developer_tools]] [[finance_payments]]
**user** [[developer]]

**stack** forge, graphql, javascript, openai, react, rest

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for vectoria

## Body

Sample and easy to navigate ideas listing available globally in Confluence Let VectorIA evaluate your idea based on criterias and Sentimental analysis Add you idea and get help from VectorIA to review syntax and category Inspiration At Vectors, we’ve already had an Ideation app for Confluence written via Connect, and that was kind of our inspiration in a way (or our starting point). Ever since Chat-gpt burst into the scene a while back, we’ve always thought of ways to include AI within the whole ideation process. It wasn’t a move to simply jump on the AI bandwagon, but rather to find ways to turn AI into an active collaborative partner (or an ideation catalyst of some sort). And that’s because we realized two important findings through studying usage patterns and performing client interviews. First, the process of turning a thought into an idea and properly categorizing it can be challenging for some. The process often gets hindered by the complexities of turning a vague notion into a structured concept. Second, the initial evaluation process could quickly become tiring and time consuming. This was a crucial pain point for teams, and it was clear that there was an opportunity to make this process more efficient and data-driven. We saw an opportunity to bridge this gap by leveraging AI technology to assist both creators and evaluators in the ideation process. What it does VectorIA is designed to facilitate the process of creating, categorizing and evaluating ideas inside Confluence. During the idea creation process, VectorIA acts as an ideation assistant helping users generate idea titles, correct grammar & spelling mistakes, automatically associate ideas with predefined categories and more. When it comes to idea evaluation, we’ve decided to equip evaluators with AI generated scores based on criteria such as feasibility, sentiment, competition, etc. These scores will help evaluators grasp an initial understanding of a given idea, but the final evaluation score depends on their own assessment. How we built it VectorIA was developed using Forge, Confluence Cloud RestAPI, GraphQL, and the OpenAI layer. The product design team drafted a couple of mock-ups that more or less mirror what we had in mind. Then, all the involved parties came together to discuss the designs and share their feedback. Once the decision was made for the entire user experience and feel of the app, development started shortly after. With Forge and Confluence Cloud RestAPI, We’ve built a global interface accessible via the Apps Menu. This is where users can create and submit their ideas, which are then transformed and converted into Confluence pages within selected spaces. Idea pages act as blank canvases (or templates) that can be enriched over time with comments and insights by idea contributors. Ideas can also be voted upon, commented, and shared. During idea creation, VectorIA becomes the companion of creators, carefully reviewing syntax and offering suggestions to enhance the idea's structure. For this, we’ve leveraged OpenAI APIs to convert specific fields into prompts that AI can go through and check for potential enhancements. The results will then be visible by selecting Enhance AI. The AI also plays a role in validating the selection of the appropriate category, ensuring that each idea finds its perfect place. When it comes to idea evaluation, we’ve also relied on OpenAI APIs to evaluate ideas based on various criteria including feasibility, innovation, impact, and more. Challenges we ran into One of the main challenges we faced when developing VectorIA was how to make it intuitive, simple, and really handy. For this, our product team, developers and designers brainstormed a variety of UX and UI options. Our goal was to ensure that Confluence users of all levels could easily navigate and utilize the app. Additionally, most of our team has never worked on Forge (for a project of this scale at least). This meant that transitioning to Forge from Atlassian Connect was a learning curve for our team due to the different development environment and framework. This was an exciting yet challenging phase in our journey. When it comes to AI, the challenge was to ensure that AI seamlessly integrated into the app without causing any significant delays during the creation and evaluation processes. Also we needed to design the App in a way that keep the human creativity in a center of the App and as the main goal. Accomplishments that we're proud of The way we built the App: an amazing team work example. We had a "hackathon in the hackathon". From brainstorming to find the idea, embark several developers in technologies that they do not know or used before to managing code reviews and merges.. All this done in less than 10 days. What we learned Teamwork makes the dream work The first thing we’ve learned during this challenging journey is: teamwork makes the dream work. It might seem like a boring cliché, but it is true nonetheless. The fact that all team members from different backgrounds came together to develop VectorIA (even marketing) brought the team closer. This hackathon brought the best in each one of us and that’s what helped us get over the line and develop VectorIA. Build an app from scratch using Forge Although our team is familiar in some capacity with Forge, most of us have never developed an app of this scale using it. This hackathon was the perfect opportunity for us to get up and running with Forge. The framework is extremely rich and allowed us to put our ideas into reality. Prompt engineering Working with AI for the first time, we learned all about prompt engineering, studied and tested how the AI model reacts to the different instructions we give and leveraged the best possible results we can get for our AI usage in VectorIA. This took a lot of trial and error but was a great learning experience for the whole team. What's next for VectorIA We hope this hackathon paves the way for us to further explore AI powered apps. As for VectorIA, the major next step is to further enhance performance, AI integration, add new features and publish it in Atlassian Marketplace. Gamification, recognition and leaderboards: For the upcoming versions of VectorIA, our aim is to build a gamification engine that will allow users to gain points based on their contributions. Users will then be listed within leaderboards promoting engagement and open participation. Further improve AI configuration: We are looking to continuously improve AI configuration during both the creation and evaluation processes. Translation <div