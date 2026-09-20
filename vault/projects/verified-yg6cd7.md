---
slug: "verified-yg6cd7"
url: "https://devpost.com/software/verified-yg6cd7"
title: "OpenAPI Operations"
hackathon: "The Postman API Hack"
organization: "Postman"
winner: true
words: 567
team_size: 1
has_repo: false
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/benchmark_measured"
  - "domain/developer_tools"
  - "user/developer"
  - "user/general_public"
  - "substrate/web_dom"
---

# OpenAPI Operations

> A workspace which enables you to analyse and benchmark your OpenAPI specifications.

[Devpost](https://devpost.com/software/verified-yg6cd7) · hackathon [[The Postman API Hack]]

## Facets

**mechanism** [[benchmark_measured]]
**domain** [[developer_tools]]
**user** [[developer]] [[general_public]]
**substrate** [[web_dom]]

**stack** github, google-natural-language, grammarbot, javascript, mailjet, postman

## How they structured the write-up

- inspiration
- what it does
- how we built
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for openapi operations

## Body

Inspiration OpenAPI specifications are an integral part for many modern APIs. The problem is that multiple people work on these files at the same time. As a result, they can grow quite numerous and contain many lines. In order to gain control over the evolution of specifications, this project provides a number of tools. What it does Currently, the provided functionality is split into two groups: benchmarking and Analysis . Using MailJet , you can be alerted of any findings when running the collection periodically. For more manual operations, Postman's visualization is used to provide beautiful insights. Benchmarking The Benchmarking toolset aids you in comparing your specifications to those of many specifications published by the industry. Using APIs.guru , it retrieves a large number of OpenAPI Specification (OAS) files. With this, you can do two things: Custom key search : See what fields outside of the OAS other developers are using. That is, any field prepended by "x-". Benchmark fields : Within the test script is a framework that allows you to specify which fields you want to benchmark. For example, the average readability of your descriptions, or the average amount of parameters per endpoint. See how your specs compare to others in the industry! Analysis The Analysis toolset aids you in maintaining the quality of your OAS files. It uses Google's Natural Language and GrammarBot for sentiment analysis and grammar/spelling checking, and a text diff _ and broken link checker to be aware of any changes or broken links. Grammar checking : Detect potential grammar and spellling mistakes. Includes functionality to reduce the number of false positives. Sentiment analysis : Gain an overview of descriptions or summaries with potentially negative sentiment. This provides you insight into which sentences could use improvement. Text diff : Detect and visualize the differences between two OAS files. Useful for version control. Broken link checker : Detects links in your OAS files and checks if they are still working. How we built At its core is a lot of (Java)scripting done in the test section, in combination with the functionality provided by some of the aforementioned APIs. Everything has been kept Postman Collection native, in order to make usage and contribution as easy as possible. Challenges we ran into Purely using Postman for a project that is scripting heavy can be difficult at times. Postman is mostly API request oriented, with scripts as second class citizens. However, using Postman's variable system, most tasks could be achieved. Notably, when iterating over multiple URLs, using the script to make requests, as opposed to Postman directly, was easier. Mainly because making requests from the script left you with direct and intuitive access to any date structures/variables that were needed. Accomplishments that we're proud of This project enables smaller companies to start using DevOp functionality without dedicating a lot of development time. It's a direct contribution, with little needed effort from the using company. Also, since it is in a public Postman workspace, there is a potential for growth. What we learned Using Postman and APIs you can create powerful toolsets in relatively little time. And a number of Postman specific features, such as the requests and tests that you can make in the test script section. What's next for OpenAPI Operations Get other people to contribute. I hope this collection shows the potential and gets others to use the idea in different ways. <div