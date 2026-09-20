---
slug: "nameseekr"
url: "https://devpost.com/software/nameseekr"
title: "NameSeekr"
hackathon: "World’s Largest Hackathon presented by Bolt"
organization: "StackBlitz / Bolt"
winner: true
words: 264
team_size: 1
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
---

# NameSeekr

> Create the perfect domain name for your brand with our ai powered name generator.

[Devpost](https://devpost.com/software/nameseekr) · hackathon [[World-s Largest Hackathon presented by Bolt]]

## Facets


**stack** google-dns, netlify, openai, whoxy

## How they structured the write-up

- inspiration
- what it does
- how i built it
- challenges i ran into
- accomplishments that we're proud of
- what we learned
- what's next for nameseekr

## Body

NameSeekr - Domain Name Generator Inspiration When looking for new brand names my go-to strategy was to prompt ChatGPT for names and manually checking the domain availablility of each generated name one by one. So when this hackathon came up I thought it was a good time to automate this process. What it does Select a pre-made prompt or write your own and then have OpenAI GPT-4 generate unique domain names for you. The tool will automatically check if the domain names are still available. How I built it The entire app works client-side and the user provides their own API keys, which allows the user to pay for their own AI and WHOIS Lookup costs. To keep the cost for the user as as low as possible we first do a free Google DNS Lookup of every generated domain, and only if the domain is not in use (no DNS entries), then we send the domain to Whoxy for a WHOIS Lookup. Challenges I ran into None, everything worked really well and Bolt built the app just like I envisioned it. It worked so well that i started over and tried to build the entire app in just one prompt so i can enter the One-Shot challenge, and Bolt mastered that as well. Accomplishments that we're proud of Ease of use of the app and the fact that we can provide the tool for free. What we learned Bolt is pretty cool. What's next for NameSeekr Maybe add more prompt templates for different brand name styles to get even better generation results. <div