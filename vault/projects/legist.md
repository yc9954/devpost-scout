---
slug: "legist"
url: "https://devpost.com/software/legist"
title: "Legist"
hackathon: "Hack the North 2020++"
winner: true
words: 674
team_size: 4
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "mechanism/vision_ocr"
  - "domain/civic_government"
  - "substrate/document_pdf"
  - "substrate/regulation_legal_text"
---

# Legist

> Putting the gist in legislation: summarizing policy for democracy

[Devpost](https://devpost.com/software/legist) · hackathon [[Hack the North 2020-]]

## Facets

**mechanism** [[realtime_stream]] [[vision_ocr]]
**domain** [[civic_government]]
**substrate** [[document_pdf]] [[regulation_legal_text]]

**stack** adobe-illustrator, docker, figma, firebase, flask, graphql, node.js, react, swr, typescript

## How they structured the write-up

- 🏛 inspiration
- 🔎 what it does
- 🚧 how we built it
- 🛑 challenges we ran into
- ✅ accomplishments that we're proud of
- 💡 what we learned
- 💭 what's next for legist

## Body

Mockups of the UI Our issue Introducing Legist Main features Why it matters Techstack Architecture 🏛 Inspiration Through news media, social networking platforms, and polarizing discussions, we have become a population that is increasingly obsessed with politics. We are regularly reminded to make informed decisions and hold ourselves accountable, but when it comes to actual policy, even some of the most socially active individuals know close to nothing. Why are so many people poorly informed about the actual policies that shape our lives? For starters, policy is often extremely inaccessible. To those who are unfamiliar with how policies are developed, it is difficult to determine where to find necessary documents and reports. Even with the correct readings in hand, the average person would likely not want to read through page after page of dense language to understand a policy. How can we truly understand our place in society without understanding the policies that shape it? In order to understand these policies, how can we overcome the boring and inaccessible ways in which policies are currently presented? With these questions in mind, we ultimately arrived at our solution: Legist. A portmanteau of the word legislature, and the French for “the gist.” Baseline 3-minute pitch: https://z.rishi.cx/legist 🔎 What it does Legist is a web platform that allows users to digest policies in an efficient and accessible manner. There are three main features of Legist: summarize, deliver, and reimagine. Summarize: users will have access to a significantly reduced summary of a policy and legislation, breaking down 4000 words to ~150 (a 96.25% reduction in length) while still maintaining the key meaning behind documents. We also perform named entity recognition along with our 5 other large models supplied through our serverless webhook engine to create a data graph surrounding every single legislation, adding in rich relationships. Deliver: have relevant content delivered straight to Twitter & custom feeds in-app. In order to minimize the extra overhead associated with viewing these monstrous documents, we also use our webhook engine to stream live updates of the most popular documents to people's inboxes. Reimagine: Government data is not just made up of documents on their own; each piece of legislation is part of a larger network of societal constructs. Full Feature List Fully featured platform to view, filter, and follow updates from topics you're interested in Join mailing list to get periodic roll-ups of policy updates Full data processing pipeline from PDF to summarized text Effective Text Summarization Named-entity recognition and Zero-shot text categorical classification 🚧 How we built it Frontend: built in React with extensive use of SWR and Chakra UI, deployed to Vercel and Google Cloud Backend: authentication with Firebase, Typescript and GraphQL used to power a serverless async Webhook engine, Apollo editor to wrap CockroachDB in GraphQL Infrastructure: Dockerized Flask application to serve our machine learning models (all three of them!), text parsing from PDF done from scratch using Node. Email system done using MailGun. Machine learning: DistilBART-CNN for summarizing text, BERT-Large for Named Entity Recognition, and BART-Large for Zero-shot text categorization. Branding, design and UI: Figma, Adobe Illustrator, Adobe Photoshop, and select elements created in Procreate Pitch video: An AfterEffects, Final Cut Pro, and Adobe Photoshop production 🛑 Challenges we ran into building an interface with so many different elements and functions within the given time constraint processing large amounts of data and actual policy documents successfully learning GraphQL in a short time frame s c o p e ✅ Accomplishments that we're proud of Implementing nearly EVERYTHING we could've thought of in the span of 36 hours; webhooks, realtime GraphQL APIs, stale-while-revalidate loops, BART, NLP for sentient entity recognition. We somehow managed to do it all! 💡 What we learned Aiming high is surprisingly good! 💭 What's next for Legist Implementation in the real world! We aim to push this out to real life users soon We would love to work with users from different age categories and levels of political activity to experience how political views, biases, and personal experiences can affect the user journey. <div