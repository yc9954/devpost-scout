---
slug: "modulearn"
url: "https://devpost.com/software/modulearn"
title: "ModuLearn"
hackathon: "HackUTD X"
organization: "hackutd"
winner: true
words: 575
team_size: 4
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/cross_origin_web"
  - "domain/education"
  - "user/educator_student"
---

# ModuLearn

> ModuLearn curates step-by-step interactive learning lessons just for you, transforming the infinite web of knowledge into a focused path that guides you to your learning destination.

[Devpost](https://devpost.com/software/modulearn) · hackathon [[HackUTD X]]

## Facets

**mechanism** [[cross_origin_web]]
**domain** [[education]]
**user** [[educator_student]]

**stack** firebase, next.js, openai, react.js

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- what's next for modulearn

## Body

Landing page Create an individual lesson or a larger roadmap for learning dense topics that consist of several lessons Lessons and their completeness can be viewed in the lessons page Roadmaps, their included lessons, and their completeness can be viewed in the roadmaps page A lesson begins with the teacher, our system, telling you about the given lesson You can respond by asking clarifying questions and the teacher will respond in context If you understand a topic you can move on to the next step of the lesson You can even search for roadmaps created by other users rather than creating your own Inspiration The internet is overflowing information about a wide variety of topics, but it can often be difficult to pick up a new skill or learn about a new topic objectively as learners have to wade through a wealth of knowledge. Modulearn makes learning any topic you can think of as easy as possible by stripping away the need to compile resources manually and deciding in what form or fashion to teach yourself. What it does Simply ask Modulearn about a topic or skill that interests you and you want to learn about and Modulearn will generate a comprehensive roadmap that includes individual lesson plans for topics critical to learning that skill or concept. No need to search through Google for lesson plans, crash courses, or resources. Modulearn compiles it all for you by leveraging generative AI in combination with a clean user-friendly Next.js interface. You can even search for roadmaps created by other users for the topic of your choice so you don't have to create one. How we built it The platform is built with Next.js & React.js for the front end, Google Firebase for the backend, and the OpenAI api to leverage the newest generation GPT4 LLM. GPT4 allows us to gather and process information about extremely dense topics and render lessons plans with React almost instantaneously. Challenges we ran into Prompt engineering was our biggest challenge. We spent a lot of time designing several prompts for each use case that would provide the most consistent and reliable results. In addition to prompt engineering we contended with reducing latency. Ingesting and processing large amounts of data like we are means long wait times but through some clever api tricks and the magic of GPT4 we reduced the latency in lesson plan generation considerably. What's next for ModuLearn Considering the concept of ModuLearn, our AI-generated learning roadmap web app, there are numerous directions for growth and expansion that could enhance user experience and value proposition. Here's what could be next: A chrome extension that allows users to highlight content to create lesson plans rather than explicitly ask ing Modulearn Expand the community aspect by adding features for learners to connect, collaborate, and form study groups or mentoring relationships. Introduce gamification to motivate users through rewards, badges, leaderboards, and challenges that encourage progress and completion of learning milestones. Integrate predictive analytics to suggest future learning topics or skills users might be interested in, based on industry trends and job market demands. Integrate predictive analytics to suggest future learning topics or skills users might be interested in, based on industry trends and job market demands. Invite experts from various fields to contribute to the learning roadmaps, ensuring that the content remains cutting-edge and authoritative. Allow users to create and share their own learning modules or roadmaps, fostering a crowdsourced knowledge base. <div