---
slug: "traid-h6db5a"
url: "https://devpost.com/software/traid-h6db5a"
title: "Traide: Sell Anything, Anywhere"
hackathon: "UC Berkeley AI Hackathon 2026"
organization: "Cal Hacks"
winner: true
words: 894
team_size: 3
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/retrieval_grounding"
  - "domain/developer_tools"
  - "domain/education"
  - "substrate/video_visual"
---

# Traide: Sell Anything, Anywhere

> TrAIde is the AI agent that sells your stuff for you. Just text a photo and price range and it lists, prices, and negotiates the sale across marketplaces. Turn your clutter into cash!

[Devpost](https://devpost.com/software/traid-h6db5a) · hackathon [[UC Berkeley AI Hackathon 2026]]

## Facets

**mechanism** [[retrieval_grounding]]
**domain** [[developer_tools]] [[education]]
**substrate** [[video_visual]]

**stack** browserbase, claude, cloudflare, javascript, orkes, poke, python, redis, stagehand, tailwind, typescript

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for traide: sell anything, anywhere

## Body

User Analytics stored through Redis User POV Succesful listing Poke being Sassy Agent navigating eBay in browserbase Inspiration We all have busy lives juggling work, school, and everything in between, and none of us actually enjoy the part of selling online where you fight off scammers, dodge lowball offers, and answer the same "is this still available?" message ten times a day. Reselling something should be easy, but the marketplace grind makes people leave money on the table or just never list their stuff at all. So we decided to take the fighting off your hands. trAIde does the haggling, the pricing, and the busywork for you, so you get the value of your items without the headache of the negotiation. What it does trAIde is an AI agent that buys and sells on online marketplaces automatically, starting with eBay. You text it a picture of your item, a quick product description, and answer a couple of questions about your price range and how fast you want it gone. From there it takes over: it researches what comparable items are actually selling for, sets a smart price point, writes and publishes the listing, and then negotiates with buyers on your behalf, accepting fair offers and pushing back on lowballers. The entire experience happens over text, so there is no app to download and no dashboard you are forced to babysit. You just send a photo and let the agent close the deal. How we built it We built trAIde as a texting-native autonomous reselling agent, wiring together four services around a Claude reasoning core. The front door is Poke: a user just texts a photo and a casual note like "sell this, want it gone fast," and our Python backend, a stateless MCP server that Poke connects to, picks it up and replies back through a Poke webhook, so the whole experience lives in chat. Behind that, we used Orkes (Conductor-style orchestration, run via the AgentSpan runtime) to model the agent's work as durable, multi-step tool workflows covering identify, research, price, draft, publish, and negotiate, so each stage is tracked and resumable rather than one fragile script. The hands-on work happens in Browserbase, a real cloud browser that the agent drives with Stagehand to scrape eBay comparables, fill out the listing wizard, and message buyers, with each run exposed as a live, embeddable session. Everything is persisted in Redis as the single source of truth, with RedisVL powering vector search over comparable listings and Redis Agent Memory holding durable seller preferences. Finally, we built a standalone dashboard that reads Redis and Browserbase directly (read-only) to visualize the agent live without touching that backend. Challenges we ran into Getting Browserbase to reliably find and click the correct buttons on eBay's constantly shifting UI was harder than expected, since the listing flow does not always render the same way twice. We worked through it by debugging interactively with Claude Code until we landed on a reliable approach. Our second big hurdle was getting Poke to communicate with the rest of the agent, because the MCP server kept failing to connect. The root cause was a complicated monorepo with a lot of moving ports, so we unified everything behind a single start file that manages all of the ports for us, which made the connection stable. Finally, bypassing captchas and logging into online marketplaces was a real blocker, and we got past it by consulting a Browserbase representative for guidance on the right way to handle authenticated sessions. Accomplishments that we're proud of We are proud that we used multiple sponsor technologies in a way that genuinely fit the product, rather than bolting on features just to check a box. Every integration, from Poke to Orkes to Browserbase to Redis, earns its place in the workflow. We are also happy with how clean the user interface and the text-based input system turned out, making a fairly complex agent feel simple to use. Most of all, we are proud that we can take an item from a single text message all the way to a real, live eBay listing, which is the core promise of the whole project working end to end. What we learned This project pushed us to pick up a lot of new tools quickly. We learned how to work with Claude Code as a development partner, how to orchestrate multi-step agent workflows with Orkes, how to use Redis (along with RedisVL and Agent Memory) as both a state store and a search layer, how to drive real browsers at scale with Browserbase, and how to build a texting-native interface on top of Poke. On top of the infrastructure, we also sharpened our UI design skills to turn all of that backend complexity into something clean and approachable. What's next for trAIde: Sell Anything, Anywhere Because we built on Browserbase instead of relying on a single eBay integration, there is huge room to scale: the same agent that drives a real browser can be pointed at almost any marketplace. Next up is expanding beyond eBay to platforms like Facebook Marketplace and Depop, so users can list once and reach buyers everywhere. We also want to round out the experience by adding buying on top of selling, letting the agent hunt for deals and negotiate purchases for you the same way it already handles sales. <div