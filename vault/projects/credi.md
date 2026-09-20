---
slug: "credi"
url: "https://devpost.com/software/credi"
title: "Credi"
hackathon: "Code with Kiro Hackathon"
organization: "Kiro"
winner: true
words: 658
team_size: 1
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/multi_agent"
  - "domain/legal_justice"
  - "substrate/sensor_telemetry"
---

# Credi

> In this information age, anyone can seem like an authority figure on social media. Credi helps you cut through the noise and find which voices are actually credible and worth trusting.

[Devpost](https://devpost.com/software/credi) · hackathon [[Code with Kiro Hackathon]]

## Facets

**mechanism** [[multi_agent]]
  <sub>weak: cross_origin_web</sub>
**domain** [[legal_justice]]
**substrate** [[sensor_telemetry]]

**stack** claude, langchain, llm, mcp, next.js, node-tap, sqlite, typescript

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for credi

## Body

Main Page Credi Score Representative Posts Section Score Justification Section Inspiration I noticed my social media feed (LinkedIn, Instagram, Twitter) is now full of people who are all experts in something. So many of them are covered in technical jargon, reference some scientific paper that supposedly supports their claims, some are AI generated, copy pasted contents, aggregated content from other creators, or even promotional posts with links to their digital products, trying to get more reach using previously viral methods. I've been constantly facing different types of advice and educational content on my social media account but I don't know who to trust. What it does Credi does a thorough investigation of a social media profile in order to assess their credibility, originiality, intent, correctness, and usefulness of their content. It looks for things like: Is the message clear or overly complicated? Are they just trying to sell something? Do they pit people against each other? Are they promising way too much? Do they rely more on feelings than facts? Do they share their sources? Are their sources credible and strong? Are they always going against the crowd just for the sake of it? And finally, do they act like a know-it-all guru? How we built it It uses a combination of scrapers, AI automation workflows, and a multi-agent consensus framework, Structured and strongly-typed LLM output with Zod and LangChain, (planned to be) fine-tuned with existing well-known and trusted experts in social media as reference and examples in order to provide unbiased response. Challenges we ran into Different agents have different opinions about the same data. It needed to provide a less biased response, as a result, decided to implement on a consensus system that aggregates the responses from multiple agents. Another challenge was the prompt engineering in order to fine tune the criteria to a point where the results are consistent with a high probability. Since we are defining a scoring system based on qualitative metrics, I needed to provide very accurate descriptions of what I were looking for and how this scoring should work, otherwise the results were not trustworthy. Also in order for the app to reliably work, I had to implement strong typing with Zod and LangChain's structuredOutput feature, and proper retry mechanisms so that I could receive reliable outputs from the LLMs. All that aside, popular social media accounts such as LinkedIn and X are now strictly gated, expensive, and require enterprise-grade verification to access even their public data programmatically. I experimented with multiple approaches and had to make thoughtful considerations to avoid legal repercussions. Accomplishments that we're proud of I built this product for myself, to resolve a pain and confusion I was experiencing. I'm are proud of it growing into a product that I find useful and has helped me to curate a much more useful social media feed and weed out highly promotional content. Even if someone tries to game this system, they will end up with content that is more useful, so that's a win. What we learned Building anything useful is hard, even in the age of AI. It takes a lot of sweat and tears to get all the details right. But they are worth it, because there's nothing more fulfilling than building something useful. There's a lot more to building a product than coding. The most time and energy-consuming part of this project was getting the requirements right, and solving non-coding problems like how to write a trustworthy analysis and evaluation prompt, or how do I programmatically get access to publicly available social media posts. What's next for Credi I plan to share it to other forums and product channels to receive feedback from others. I will be polishing it and launching it on Product Hunt as well. My dream for Credi is to become the driving force that shifts the mindset of content creation from low-effort, viral content to useful and well-thought out content. <div