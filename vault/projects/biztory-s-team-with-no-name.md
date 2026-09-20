---
slug: "biztory-s-team-with-no-name"
url: "https://devpost.com/software/biztory-s-team-with-no-name"
title: "(Tableau) Next Question"
hackathon: "Tableau Next Virtual Hackathon"
organization: "Tableau"
winner: true
words: 660
team_size: 4
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
---

# (Tableau) Next Question

> Slack is the place to be. (Tableau) Next Question removes barriers to get to your data in that context. Insights from Tableau Next and Tableau Core come to Slack and to each other, seamlessly.

[Devpost](https://devpost.com/software/biztory-s-team-with-no-name) · hackathon [[Tableau Next Virtual Hackathon]]

## Facets


**stack** django, openai, python, tableau

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for biztory's team with no name

## Body

TNQ answering a question directly from Tableau Next TNQ having migrated a view from Tableau Core to Tableau Next Welcome! This is (Tableau) Next Question . Inspiration Slack is increasingly regarded as the place where people work . At the same time, analytics platforms are growing and new ones, such as Tableau Next, are bringing new capabilities to the market. Some might find it challenging to keep up with all of that information, and all those capabilities, in all those places. (Tableau) Next Question (or "TNQ") strives to remove any hurdles between those three platforms, by making them and their insights accessible seamlessly centrally: in Slack! What it does (Tableau) Next Question connects to Tableau Next and Tableau Core (Server/Cloud) to answer data questions more dynamically and effectively than ever, from wherever. Slack is the starting place: users can formulate questions in Slack, directed to the app specifically or in any channel, and that we use assets on either Tableau platform to provide an answer. But we'll go one step further. In an effort to reduce any possible gaps between the "old" Tableau Core and the "new" Tableau Next, TNQ can compare available data on both platforms and migrate things like Visualizations from Core to Next, thereby unlocking Next's agentic capabilities and more. How we built it The central component of TNQ is a Django Web App. While it (currently) has not real front-end, it is the entrypoint for any relevant event coming from Slack. That is, any type of data question! When receiving such an event, e.g. someone inquiring about "Superstore Sales of tables in the East", TNQ goes to work. It has connections to Tableau Next, Tableau Core (Server/Cloud), and OpenAI. Those three tools will be used to identify the analytics assets that can potentially be used to answer the question. When that asset has been found, the answer is formulated and both are shared with the person asking the question, and possibly their team. Challenges we ran into What a journey it was to discover the new Tableau Next platform and its API. But even more so, how this is part of Salesforce's ecosystem and the fact that it, in turn, has many APIs, capabilities to connect, etc. Whereas we initially explore this whole universe of Tableau Next, Salesforce Orgs, Data Cloud, their APIs, etc., we started seeing the bigger picture and understanding this ecosystem. Accomplishments that we're proud of One of the most fun challenges to tackle, was to align the representation of analytics assets between Tableau Core and Tableau Next. After some research, looking for the right asset to answer data questions, we settled on the View or dashboard (in Tableau) and the Visualization in Tableau Next. We know we can expand this to Published Data Sources with the VizQL Data Service (and/or Tableau MCP etc.), but that will be easier when Orgs that support connecting Tableau Next to Tableau Cloud Published Data Sources become available. Then maybe the bit we're actually most proud of, is the fact that we effectively enable someone to automatically recreate (basic) a Tableau Core visualization (i.e. sheet) in Tableau Next, as a Visualization. (Tableau) Next Question already understands the concept of rows, columns, marks, and can translate those to automatically migrate a viz! There's much more to be added to this after the Hackathon, potentially... What we learned A ton of things about Tableau Next, and Salesforce more broadly. What's next for Biztory's Team With No Name If there is a decent interest for a combined solution like this, it can definitely be extended. Is there a demand for answering data questions through an IM client? We can start supporting more platforms! Is there a need to answer questions not only from vizzes but also from data sources? VizQL Data Service + Semantic Layer integration, here we come! Do people want to migrate assets from Tableau Core to Tableau Next? We have the foundation for this in place! <div