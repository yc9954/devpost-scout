---
slug: "deadly-questions"
url: "https://devpost.com/software/deadly-questions"
title: "Deadly Questions / Alexa"
hackathon: "Amazon Alexa Skills Challenge: Multimodal"
organization: "Amazon"
winner: true
words: 535
team_size: 3
has_repo: false
has_live: true
has_video: false
tags:
  - "project"
  - "domain/developer_tools"
  - "user/developer"
  - "user/general_public"
  - "substrate/code_repository"
  - "substrate/structured_db"
  - "substrate/web_dom"
---

# Deadly Questions / Alexa

> You ask. Aboriginal Victorians answer.

[Devpost](https://devpost.com/software/deadly-questions) · hackathon [[Amazon Alexa Skills Challenge- Multimodal]]

## Facets

**domain** [[developer_tools]]
**user** [[developer]] [[general_public]]
**substrate** [[code_repository]] [[structured_db]] [[web_dom]]

**stack** alexa-presentation-language-(apl), amazon-alexa, amazon-web-services, apl, aws-lambda, lambda, node.js

## How they structured the write-up

- project summary
- problem identification
- solution design
- technical breakdown
- challenges
- accomplishments

## Body

Project summary Deadly Questions provides a public space for Aboriginal Victorians to discuss history and how it affects their lives today, as well as to share the strength and vibrancy of their cultures, with the aim of building understanding between Aboriginal and non-Aboriginal people. Problem identification Many Victorians feel they know little about their State’s Aboriginal heritage or Aboriginal affairs in general. But along with their lack of knowledge, Victorians also don’t feel comfortable asking questions for fear of offending or appearing ignorant. As Victoria is the first Australian state to commit to negotiating a treaty with First Peoples, we thought, “how can we provide a platform for people to ask difficult questions, and provide them with meaningful answers?” Solution design We created a bespoke web platform for Victorians to get much needed answers and opens up a conversation between non-Aboriginal Victorians and the Victorian Aboriginal community. With such a rich library of questions from the public, and answers from our various champions, we created an Alexa Skill to be a companion app to the web platform. The voice experience emphasises discovery of content, allowing you to browse the questions asked and answered by our champions. As conversational interfaces work differently from visual interfaces, we reimagined how audiences access the content. This is how we ended up with 2 different paths: a quick and easy question of the day, and questions organised by topic to emphasise discovery. Technical breakdown The question of the day is served to Alexa users based on their local device time. From a technical standpoint, we use a database to keep track of the questions already served to each individuals, so people get fresh new content every day. The whole platform is built around an API-centric architecture, offering different endpoints for the public facing website, the custom administration interface used to moderate the content, and the voice experience. To deliver on a rich and engaging user experience, we’ve decided to make use of the new Alexa Presentation Language (or APL), allowing us to deliver on things like graphics, and touch events to complement the overall experience where we thought it was necessary. Challenges From a user experience perspective, finding the right amount of topics and questions to highlight in the skill was probably the most challenging part. The human brain is only trained to remember a limited number of choices. So we had to undergo several user testing sessions, to adjust and find the right balance of topics. Creatively, understanding how to write for conversation required rigorous testing with users, and regular sessions with developers, designers, writers and users to understand their needs and provide them a robust exchange with the skill. Accomplishments With the Deadly Questions campaign, we’ve been able to reach 110 million impressions in the first 4 weeks, an increase by 52% in positive sentiment towards Aboriginal people, and have the Victorian Parliament to vote a law to negotiate Australia's first Aboriginal treaty. With the Deadly Questions Alexa Skill, our aim is to bring this campaign to life from a different perspective, and allowing users to explore what has already been asked by other Australians. Giving them an opportunity to listen and learn more about first peoples. <div