---
slug: "tldr-this-issue"
url: "https://devpost.com/software/tldr-this-issue"
title: "TLDR This Issue"
hackathon: "Codegeist Unleashed"
organization: "Atlassian"
winner: true
words: 947
team_size: 5
has_repo: false
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/cross_origin_web"
  - "domain/developer_tools"
  - "domain/health_clinical"
  - "user/developer"
  - "substrate/code_repository"
  - "substrate/document_pdf"
  - "substrate/web_dom"
---

# TLDR This Issue

> The app consolidates information from various sources available within a Jira issue by providing a brief summary and proposing actionable insights for the user, while bringing data privacy into focus.

[Devpost](https://devpost.com/software/tldr-this-issue) · hackathon [[Codegeist Unleashed]]

## Facets

**mechanism** [[cross_origin_web]]
**domain** [[developer_tools]] [[health_clinical]]
**user** [[developer]]
**substrate** [[code_repository]] [[document_pdf]] [[web_dom]]

**stack** atlassian-design-tokens, atlassian-ui-kit, atlassian-xcss, css, forge, forge-async-events-api, forge-storage-api, jira-cloud-api, lottiefiles, openai-gpt-api-3.5, typescript

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for tldr this issue

## Body

TLDR This Issue (app logo) TLDR This Issue (app logo, dark) GIF TLDR This Issue loop dark theme (issue summarizer job) Inspiration It all started with a few provocative questions: Have you ever struggled with gaining insight into bulky Jira issues, especially into never-ending and excursive development tickets or into Jira Service Management requests carrying long dialogue with the customer sometimes losing focus? Or, have you ever wished to instantly know whether you are concerned with the issue at hand, and if so, what's the current status and the next relevant step after obtaining details? Some colleagues of us have long complained about the above-mentioned symptoms affecting our work on a daily basis. For instance, if a developer gets looped into some incident as part of the L2/L3 support process, she will likely learn about a verbose dialogue with the customer, at which point it is hard to pick up the thread and obtain relevant information from the many comments that sometimes already have lost focus. Our mission was to build a solution that is able to summarize all the issue history and provide (personalized) insights about the current state of affairs and the subsequent actions to be taken. What it does The TLDR This Issue app attempts to tackle the problem by leveraging pre-trained Large Language Models, or more concretely, OpenAI's GPT 3.5 model via its associated API. The app consolidates data from various sources available within a Jira issue, such as issue summary, issue description, the comment history, linked issues, subtasks and attached text documents. With the help of a well-crafted prompt, we try to merge all these raw data and yield a brief overview featuring the essential details only. Besides this, we also added a second prompt to transform the aggregate data into actionable insights, or in other words, into suggestions that might be potentially converted into subtasks at a whim. Of course, the already existing subtasks are taken into account, while proposing new action items. In spite of all that automatism, the user still has control over what issue fields shall be processed, may specify the output language and also might provide keywords that shall not be passed to the GPT API for any case (names or expressions conveying proprietary or sensitive information). To increase transparency and build trust, data privacy was always in our focus. As a consequence, we applied various types of data anonymization to avoid exposing any Jira usernames, email addresses or the above-mentioned custom keywords to the GPT API. For contenting your cost-aware self, the most important statistical data (e.g. prompt token usage) was made accessible, too. How we built it We executed npm run build in the project directory. 😄 Jokes apart, a group of four people - accompanied by some enthusiastic peer volunteers - had a dream. Then, once we started to work on it, practically right after the announcement of this year's hackathon... One of us had a bit deeper knowledge in Forge and TypeScript, the other three of us were little familiar with the platform. Regarding LLMs or any other machine learning skills, we all started from ground zero. After getting some basic ideas from the sample AI apps provided by Atlassian, we kicked things off. However, witnessing some of our great - even if trivial - initial ideas partially reflected in these sample apps made us a bit disappointed at the same time. Basically, after setting up the application's frame, we broke down tasks based on different areas of knowledge (like AI prompting, Jira API communication, UI design, administrative tasks). But later on, we just jumped into everywhere on demand to help each other out. Technically speaking, we tried to limit our app's external dependencies as much as possible, sticking to solutions and techniques natively available in the Forge platform (despite all the limitations). Challenges we ran into Among the several difficulties, we would highlight the following aspects: cross-platform limitations, missing Forge support for Bitbucket apps (made partially available in the meantime) put a compatible, working HTML DOM parser into operation (in the sandboxed Node.js backend) living with the 25 sec lambda execution limit (increased to 50 sec in the meantime) missing OpenAI stream support of the old Forge runtime async type-safe programming in TypeScript (as beginner/mid-level JS/React/TypeScript programmers, since being mostly versed in Java programming) Accomplishments that we're proud of First of all, we managed to deliver something operable before the deadline. From the technical point of view, we are also proud of the ways we: used of async queue with React hooks created and embedded amazing app animations and provided seamless UX shot a marketing-focused, fancy demo video investigated and implemented various anonymization and de-anonymization techniques to provide a comprehensive service for protecting your privacy and your business interests What we learned Many-many things, among others: learn TypeScript the hard way various features of the Forge ecosystem working together basic AI prompting But most of all, we had a great experience again, how much fun it may make to work together. 😄 What's next for TLDR This Issue We have numerous ideas, how we could extend out app's capabilities and make it a fully-fledged app from the fundamentals we already built: incorporate further sources of information (e.g. linked Confluence pages, integrate with Bitbucket repository to retrieve development-related information, process external web links), potentially traversing multiple (2-3) levels of depth refine our AI prompting technique, by applying dedicated, more sophisticated tools (e.g. LangChain) to effectively aggregate a large amount of potentially inhomogeneous data in multiple phases (e.g. employing domain-specific agents) test our solution with other LLMs a bunch of other, still-confidential ideas on how we could deliver more value by further integrations <div