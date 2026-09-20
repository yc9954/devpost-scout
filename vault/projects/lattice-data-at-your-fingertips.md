---
slug: "lattice-data-at-your-fingertips"
url: "https://devpost.com/software/lattice-data-at-your-fingertips"
title: "Lattice: Orchestrating end-to-end web workflows at scale"
hackathon: "TreeHacks 2025"
organization: "TreeHacks"
winner: true
words: 1024
team_size: 4
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "domain/finance_payments"
  - "substrate/structured_db"
---

# Lattice: Orchestrating end-to-end web workflows at scale

> Massively parallelized agentic research workflows using spreadsheets as a primitive

[Devpost](https://devpost.com/software/lattice-data-at-your-fingertips) · hackathon [[TreeHacks 2025]]

## Facets

**domain** [[finance_payments]]
**substrate** [[structured_db]]

**stack** agents, apis, llms, typescript

## How they structured the write-up

- summary
- what is this?
- more use cases
- tech
- why spreadsheets
- what next?

## Body

Design End to end workflow Individual sheets Massively parallelized agentic research workflows using spreadsheets as a primitive Summary Over the past few months, there've been a lot of really cool agentic research products that've been released (Exa, OpenAI/Perplexity Deep Research, etc). In general, these are point solutions and relatively sequential in manner (ie, the next action is conditioned on the previous actions). But AI much more exciting if we can: Build products around end-to-end workflows Do this at scale that humans never could (ie, browse hundreds of websites at once) We want to build something that takes advantage of the parallelized nature of research agents to solve end-to-end workflows en masse (we can run hundreds of agents at once!). What is this? Lattice allows you to orchestrate complex end-to-end research workflows at scale, with complex/structured dependencies. Consider a sales representative sending cold outbound: This involves: Finding potential companies to sell to and qualifying them Finding potential points of contact at these companies Finding the right form of outreach for the best point of contact Draft + sending the email Today, Lattice solves the vast majority of this workflow – and we do this at scale, across hundreds of companies in parallel. We first find potential companies, and then for each company, find a set of defined attributes. https://imgur.com/a/bsq1S3i Then, for each company, we can find the key people we want to reach and augment this information. https://imgur.com/a/7b0FhLY Then, for each companies' list of people, we can qualify them based on attributes we defined + have researched. https://imgur.com/a/dl6gfzL Finally, we can pipe all the research information to a language model to produce a final work product. https://imgur.com/a/fAdaElA We do this at scale and save a considerable amount of time over manual research – but also existing tools that only do this for a single part of the workflow (ie, Clay)! As a page one end-to-end workflow. We let you build any workflow like this and chain spreadsheets together. More Use Cases Anything that involves scaled web research! But concretely: Insurance companies Start with a provided list of companies and find company-level information. Then for each company, find all their products, and for each product, create a grid of if they flag certain policies. Then aggregate all the violations across the products, run some risk/modeling calculation, and compile into a per-company report. Finance Find a list of recently funded startups (Series A), then for each startup catalogue all of their rounds, how much they raised, and who they raised from at each round. Across the rounds of each company, count up the number of T1 VCs. Draft emails to send outbound to companies with more than 3 T1 VCs on their cap table. Fun Example Find a list of film festivals in the past year. Then for each festival, find which films won the top prizes, the names of the movies, and the authors. Then, choose the film across with the funniest title from each of the festivals. For each of those films, then find other films created by those artists. For each of those films, then collect the Rotten Tomato and IMDB scores. Then, choose the film for each artist with the highest aggregate scores and write a congratulations emails! We know that all three (maybe two) and millions of other similar use cases are very important and significant workflows conducted by humans today. Tech We treat spreadsheets (or really tables) as a core primitive. This is how data is displayed, edited, and passed between different steps in a workflow. Most of the heavy lifting is on the frontend (Next/Typescript/Tailwind) – we build a primitive spreadsheet interface from scratch, added multiple dimension to it, then created a chain of dependencies between the different spreadsheets, and then added a bunch of agent orchestration on top of it! The cool thing is this all actually works, and works quite well! Why Spreadsheets Frankly, we thought Paradigm's challenge was really cool, and were inspired in part by what they do. We think spreadsheets are a fun primitive to build around: It's a surprisingly challenging task. Spreadsheets are one of the best ways to visualize bulk agentic outputs and enable a lot of cool things. We started with what we thought were an interesting limitation of 2D spreadsheets – we can't do a nested series of "Find a list of XYZ, then for each find a list of ABC"-style inputs. There's a lot of powerful workflows though, that depend on being able to serve multiple layers of these kinds of queries – so we designed a "3D spreadsheet" where each sheet is mapped from a row in a 2D spreadsheet. Our spreadsheet workflows, in some ways, are essentially a directed graph with dependencies. This is roughly how we treated the orchestration / execution of individual agents within our system. At any point, we can have a one-to-many relationship between incoming and outgoing edges, or many-to-one relationship. This allows us to manage state/context passing between different steps within a workflow. For example, when going from a single row into a spreadsheet -> a sheet in a 3D spreadsheet -> a single row in a spreadsheet again, we pass parts of the initial row through the entire chain so our agents have the right context. Another cool thing that comes out of this is that we provided verifiable + auditable traces into how exactly the end to end workflow was executed. As any step, you can look up the full table of data that the end considers when making decisions, all the raw attributes collected, and how they flowed in the workflow. What Next? A lot! Here's a few: Making systems and workflows more robust (prototypes are easy; building production grade agentic systems are extremely hard + painful) Make orchestration simpler (we wanted to do this but ran out of time) – describe what you want to complete, and we'll handle the orchestration itself Improve latency - our end to end workflows are slow. We think this is okay, because most of our use cases aren't latency bound. But there is definitely a lot of value in optimizing latency further <div