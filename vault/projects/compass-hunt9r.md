---
slug: "compass-hunt9r"
url: "https://devpost.com/software/compass-hunt9r"
title: "Compass"
hackathon: "USAII® Global AI Hackathon 2026"
organization: "USAII"
winner: true
words: 1176
team_size: 3
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/human_in_the_loop"
  - "domain/developer_tools"
  - "domain/education"
  - "domain/legal_justice"
  - "user/social_worker"
  - "substrate/document_pdf"
  - "substrate/geospatial"
---

# Compass

> A parent receives an electricity shutoff notice and doesn't know where to start. Compass turns a crisis described in plain words into a ready to file packet of local aid. You decide when to file.

[Devpost](https://devpost.com/software/compass-hunt9r) · hackathon [[USAII- Global AI Hackathon 2026]]

## Facets

**mechanism** [[human_in_the_loop]]
**domain** [[developer_tools]] [[education]] [[legal_justice]]
**user** [[social_worker]]
**substrate** [[document_pdf]] [[geospatial]]

**stack** anthropic, claude-agent-sdk, drizzle-orm, gpt-oss, groq, neon, next.js, react, typescript, vercel

## How they structured the write-up

- inspiration
- what it does
- why an agent, and not a web search
- how we built it
- responsible ai
- challenges we ran into
- accomplishments we're proud of
- what we learned
- what's next for compass

## Body

From a crisis described in plain words to a ready-to-file packet of local aid. Inspiration Marisol is a parent in Jersey City. Her hours at work were just cut. An electricity shutoff notice arrived in the mail, the fridge is almost empty, and her two kids are home. Help exists for situations like these: utility relief, SNAP (food assistance), WIC, and a food pantry a few blocks away. The challenging part is finding that help. It's split across agencies, buried in eligibility rules, and written for people who aren't already panicking. By the time she tracks down the right office, the lights might already be off. That gap, between help existing and help being findable, is the whole reason Compass exists. Marisol is a stand-in, not someone we interviewed, but her situation is one that 211 NJ fields across Hudson County every week. We built Compass around one specific person at one specific moment, rather than a vague "everyone." What it does You tell Compass what's going on in plain words, in English or Spanish. It does the time-consuming part: Understand. An AI agent reads what you wrote and plans what to look up. It reasons about your situation instead of matching keywords, and if something important is missing, it asks a question or two and waits. Match. It searches a real Hudson and Bergen County aid directory and weighs whether you roughly qualify for each program it finds. Explain. Every match comes with why it fits, how sure that guess is, the documents to bring, where to go and when, and a cover email that you can use. Act. You walk away with one packet you can use the same day, plus a private link to hand the plan to a relative or caseworker. Nothing gets sent until you send it. Start to finish, it's the same simple shape: you describe the situation, the AI plans and reasons over a real directory, you get a packet, you file it. Why an agent, and not a web search A search gives you ten links and keeps the hard part for you: which programs apply, whether you qualify, and what each one wants. Compass does that part. It plans the lookups, checks a real directory, weighs rough eligibility, and turns the scatter into one next step. That's the work a search box can't do, and it's the reason an agent is the right tool here. How we built it The core is a small, locked-down agent loop with three tools: one to search the directory, one to pull the exact documents a program needs, and one to assemble the final plan. Everything else, shell, files, the open web, is switched off, so the agent can only ever work from our directory. Grounding is checked twice. The agent may only recommend programs the search actually returned, and the interface re-checks every program ID against the directory and drops anything it can't verify before it reaches the screen. In practice the AI can't slip a made-up program or phone number into a packet. The app is Next.js on Vercel. The live demo runs on Groq's free tier with openai/gpt-oss-120b through the Vercel AI SDK. We also built a second, interchangeable backend on the Anthropic Claude Agent SDK (Sonnet 4.6 or Opus 4.8) that runs inside a Vercel Sandbox. Both produce the same reasoning steps and the same final plan, so the experience doesn't change with the model. Packets render to PDF with pdf-lib, the "help near you" map uses Leaflet, and an optional account can save a plan or, only if you turn it on, remember a few stripped-down facts so it doesn't re-ask next time. Responsible AI We were most worried about one thing, so we named it and built around it. Risk: an automated eligibility guess can be wrong, and someone mid-crisis is likely to trust it more than they should. Mitigation: Every recommendation is grounded and shows its work. Each match displays its reasoning, a confidence level, and its source in the directory, and low-confidence, child-benefit, or cross-agency cases get flagged for a human. Human in the loop: Compass never submits an application and never issues an eligibility decision. It prepares; a person reviews, edits, and files. It doesn't make legal or medical calls, and in a crisis, it puts the 988 lifeline up front. Personal information gets the same care. An account is optional, and the guest demo saves nothing. Once you sign in, everything identifying, your name, address, the words you type, and the answers that fill a packet, is encrypted at rest with AES-256-GCM, and the profile Compass uses to auto-fill forms is never sent to the AI. Long-term memory stays off until you turn it on, and even then it keeps only a few stripped-down facts, never an SSN, date of birth, or account number. You can read or delete any of it, and erase your whole account, from Settings. Challenges we ran into Keeping the AI honest was the hard one. Getting a model to never invent a program took locked-down tools, a strict "only cite what the search returned" rule, and that second verification pass in the UI. Eligibility was a close second. We had to let it estimate, "you likely qualify," "confirm with the office," without ever sounding like an official verdict, because it's comparing a situation to plain-language rules, not making a ruling. The rest was plumbing. Driving a multi-step tool loop on a free tier meant trimming what each tool returns to stay under rate limits and cleaning up the occasional malformed JSON. And the Agent SDK spawns a subprocess that plain serverless can't host, which is what pushed us to a Sandbox backend and the lighter Groq path for the demo. Accomplishments we're proud of A complete flow from a plain-language crisis to a packet you can act on today. Real, cited data: 12 actual Hudson and Bergen programs from 211 NJ and agency sources, not synthetic placeholders. Responsible AI that's part of the product instead of a slide, down to the hard line that it never submits. And full English and Spanish, the interface and the plan, for a community where that's not a nice-to-have. What we learned The hard part of "help is hard to find" turned out not to be retrieval. It's trust. An answer you can't check is worse than no answer when what's at stake is your lights or your kids' food. Building for that, putting the reasoning, the source, and the uncertainty on every single match, shaped Compass more than any model choice did. What's next for Compass More counties beyond Hudson and Bergen, with an honest "we don't cover that yet" message outside our area. A dedicated safety check that surfaces crisis hotlines before the normal flow. Voice input, so someone can say their situation instead of typing it. And a way to keep the directory current as program details change. Built for USAII's Global AI Hackathon 2026, High School Track, Challenge 1: Help is Hard to Find. <div