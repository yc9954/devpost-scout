---
slug: "visualize-with-aws-atlassian-forge"
url: "https://devpost.com/software/visualize-with-aws-atlassian-forge"
title: "Visualize with AWS (Atlassian Forge)"
hackathon: "Codegeist 2020"
organization: "Atlassian"
winner: true
words: 893
team_size: 2
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/cross_origin_web"
  - "domain/education"
  - "user/general_public"
  - "substrate/video_visual"
  - "substrate/web_dom"
---

# Visualize with AWS (Atlassian Forge)

> Visualize data via declarative chart and diagram engines such as Vega/Vega-Lite, PlantUML, Mermaid, and Graphviz

[Devpost](https://devpost.com/software/visualize-with-aws-atlassian-forge) · hackathon [[Codegeist 2020]]

## Facets

**mechanism** [[cross_origin_web]]
**domain** [[education]]
**user** [[general_public]]
**substrate** [[video_visual]] [[web_dom]]

**stack** amazon-web-services, atlassian, confluence, forge, jira, svg

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for visualize with aws (atlassian forge)

## Body

Visualize with AWS - app benefits Visualize with AWS - Jira issue panel with PlantUML AWS diagram Visualize with AWS - Confluence macros with Vega diagrams Visualize with AWS - Confluence macros with Vega-Lite diagrams Visualize with AWS - Confluence macros with Mermaid diagrams Visualize with AWS - Confluence macros with PlantUML C4 and AWS diagrams Visualize with AWS - Confluence macro editor (diagram source via inline JSON) Visualize with AWS - Confluence macro editor (diagram source via URL) Visualize with AWS - Confluence macro editor and preview Inspiration Our initial inspiration was the excellent Charts.xkcd library, which we both found appealing and funny, and we wanted to integrate it into Jira and/or Confluence via an AWS based rendering backend. Alas, that specific library requires a bit more work to use outside of a browser DOM, so we switched to a couple of other powerful chart and diagramming engines first, hoping to get back to the original plan and add XKCD style diagrams as another option later on. What it does Visualize with AWS allows you to use a variety of declarative diagram rendering engines to visualize any kind of data. It provides a Jira issue panel to render a single diagram (for example an architecture diagram via Mermaid or PlantUML (incl. AWS and C4 modes), and a Confluence macro to go wild with as many visualizations as you can fit on a page (notably via Vega and Vega-lite ). Diagrams can be provided and edited inline, or referenced via URL for more complex or dynamically updating charts and diagrams (down the road we want to separate the so far combined visualization and data source declaration) – meet Visualize with AWS (Atlassian Forge) . How we built it We used the Forge CLI to quickly explore the various Forge modules to determine the applicable UI components for the use case. We then started over with the app itself and have refined it since, which mostly meant finding sufficiently usable workarounds for encountered UX issues based on Forge UI limitations. The Forge CLI's excellent DX makes all this a breeze, so it is a great prototyping tool for Atlassian apps in general. The rendering engines are primarily provisioned on serverless infrastructure via Docker containers on AWS Fargate right now, though we intend to migrate most to AWS Lambda functions for even better scalability and utilization. Challenges we ran into The special circumstances of the Forge execution model, namely the combination of React style components with a Lambda based backend invocation cycle made managing state and async calls a bit irritating at first, but mentally 'translating' this to a kind of old school, page cycle based web application model helped a lot to overcome this. Also, the mentioned Forge UI limitations force some workarounds to prevent obvious usability flaws, but we are confident that the Atlassian Team will iterate quickly on providing additional layout and design options so that elements can be presented in more flexible ways in dialogs, forms, and tables. Accomplishments that we're proud of We are really happy that the app is cross-product from the get go and works conceptually similar in Jira and Confluence. We are also happy about the well scalable and easily extensible serverless API that will allow us to add new rendering engines quickly, with the most intriguing missing candidate being Charts.xkcd to visualize data via “sketchy”, “cartoony” or “hand-drawn” styled charts . What we learned We learnt a lot about Scalable Vector Graphics (SVG), a technology we have always been fond of, but never had the need to dive into from a development perspective. So far crafting applicable SVG images seems to be the most versatile workaround for Forge UI limitations. Of course, it still can't replace JavaScript based interactions with diagrams for example. Based on the excellent Forge CLI DX, we also intent to use a 'Forge first' development approach for our Cloud apps going forward, because the limitations force you to stay laser focused on the customer value, while ignoring UI/UX bells and whistles during the prototyping phase. This eases developing a domain model and the backing API/SPI so that the app core remains independent from the frontend technology. Whether or not an app still requires the currently superior UI versatility of Connect then depends on how the Atlassian Cloud platform evolves over the coming months and years. What's next for Visualize with AWS (Atlassian Forge) We would very much like to make this app available to users via the Atlassian Marketplace, so depending on the ETA for the public distribution of Forge based apps, we might need to migrate the app to Atlassian Connect on the short term. That's no big deal given its static characteristics, but still a pity, because once we do and need to create a likely more appealing AtlasKit based UI anyway, migrating back without disrupting users will be difficult. Feature wise we primarily need to separate the so far embedded remote data sources as a separate entity so that diagrams are easier to use and maintain, and more importantly, to provide live local data via JQL and CQL. We also need to rethink the prototype domain model for Jira in terms of how to best store and present more than one diagram eventually. Finally, we would also like to add an XKCD style rendering engine via Charts.xkcd . <div