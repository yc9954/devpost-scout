---
slug: "deverywhere"
url: "https://devpost.com/software/deverywhere"
title: "Docagram"
hackathon: "Google Chrome Built-in AI Challenge"
organization: "Google"
winner: true
words: 612
team_size: 1
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/cross_origin_web"
  - "domain/developer_tools"
  - "user/developer"
  - "user/educator_student"
  - "substrate/geospatial"
  - "substrate/web_dom"
---

# Docagram

> Visualize everything with Built-In AI

[Devpost](https://devpost.com/software/deverywhere) · hackathon [[Google Chrome Built-in AI Challenge]]

## Facets

**mechanism** [[cross_origin_web]]
**domain** [[developer_tools]]
**user** [[developer]] [[educator_student]]
**substrate** [[geospatial]] [[web_dom]]

**stack** gemini, prompt-api, react, shadcn, summary-api, tailwind, vite

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for docagram

## Body

Docagram explainer diagrams Section summary and diagram Combined diagram for all sections Single entity extraction from combined diagram Inspiration I have always been a visual learner and many of my personal notes look more like drawings than bullet points. In college, diagraming concepts as I learned them proved to be extremely useful in subjects related to biology since many of the concepts involved sequential or spatial relationships. Diagrams were so useful that I started using them everywhere: for planning software projects, for mapping out life plans, and for taking general notes as I browsed the web. I created Docagram to accelerate my own note taking and understanding of concepts I read about online. What it does Docagram is a Chrome extension that uses Chrome's built-in AI to generate diagrams of web content. It is designed to provide high level, visual overviews of textual data. How we built it This Chrome extension was built with React, Vite, TailwindCSS, ShadCN, the Built-In AI APIs, and the Gemini API. Diagrams are generated using the following process: Web page is broken up into sections Each section is passed to the Summary API to create a summary Each section summary is passed to the Prompt API to create a list of relationships Relationships are converted into Mermaid diagrams The Prompt API is used to convert section summaries into a list of "relationships" that consist of 2 entities and the relationship between them. These text-based relationships are then converted into Mermaid diagrams. Web pages are summarized and diagramed in sections so that the output retains as much information as possible without being overwhelming. Diagrams from all sections can be combined into a single diagram that can be filtered by entity. Challenges we ran into The most difficult challenge in this project was crafting a prompt for the Prompt API that would consistently output "structured" text. In order to generate relationships that would eventually be used to create Mermaid diagrams, the Prompt API needed to output single-line relationships that followed a consistent format (e.g. "Entity 1 to Entity 2 (description of relationship)"). I used several prompting tricks, including providing examples, in order to get this to work. Some of the built-in AI APIs were finicky and did not always return consistent results. The Writer and Rewriter APIs, for example, only seemed to work for simple prompts and repeatedly failed if the prompt became too complicated. I ended up abandoning these altogether in favor of the Prompt API. Accomplishments that we're proud of The Chrome extension can easily be made to use more powerful Gemini models, like the Flash and Pro models, to generate diagrams. If this extension were to be published, it would be fairly easy to offer plan upgrades because of this hybrid model. What we learned While each built-in AI API is useful by itself, they are even more powerful when used together. In this extension specifically, I found it beneficial to use the summary API to pre-process my text before sending it to the Prompt API. In an indirect way, this allowed me to extract some of the most important relationships from the content without much technical difficulty. The Built-in AI models are small and fast. Developers need to adjust their thinking to optimize their usage of these models. For example, this could mean passing in less data or using the models for simpler tasks. What's next for Docagram I would like to improve the Docagram extension by allowing it to work across web pages. Ideally, users could pin entities and relationships to carry them with them to new URLs. This would allow users to construct more robust diagrams to aid them in their research. <div