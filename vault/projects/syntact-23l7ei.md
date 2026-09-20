---
slug: "syntact-23l7ei"
url: "https://devpost.com/software/syntact-23l7ei"
title: "Syntact"
hackathon: "H0: Hack the Zero Stack with Vercel v0 and AWS Databases"
organization: "Amazon"
winner: true
words: 1191
team_size: 1
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/deterministic_policy"
  - "mechanism/realtime_stream"
  - "mechanism/retrieval_grounding"
  - "mechanism/structural_withholding"
  - "domain/developer_tools"
  - "domain/labor_employment"
  - "user/educator_student"
  - "substrate/document_pdf"
  - "substrate/geospatial"
  - "substrate/video_visual"
  - "substrate/web_dom"
---

# Syntact

> AI-generated coding videos, inside a real IDE.

[Devpost](https://devpost.com/software/syntact-23l7ei) · hackathon [[H0- Hack the Zero Stack with Vercel v0 and AWS Databases]]

## Facets

**mechanism** [[deterministic_policy]] [[realtime_stream]] [[retrieval_grounding]] [[structural_withholding]]
**domain** [[developer_tools]] [[labor_employment]]
**user** [[educator_student]]
**substrate** [[document_pdf]] [[geospatial]] [[video_visual]] [[web_dom]]

**stack** aws-aurora-postgresql, e2b, inngest, inngest-agentkit, openai-api, react, tailwind, tanstack-start, typescript, webcontainers

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for syntact

## Body

Inspiration Learning to code, for me, started on a 7-inch tablet. No laptop. The Odin Project open in one tab, a half-broken YouTube tutorial in the other, and little Hamza pausing the video every 4 seconds to copy a line, then unpausing, then realizing he missed a step, then rewinding.. you know the loop. Tutorial hell, but small-screen edition. The thing nobody tells you is that the video and the code live in two different worlds. You watch someone build a thing you cannot touch, then you read docs that do not run. Scrimba got close - lessons you can actually pause and edit inside a real editor - but every lesson is hand-authored, which means there are only so many of them and they take forever to make. So I asked the obvious question. What if an AI could generate the whole interactive lesson - the code, the terminal, the slides, the narration - and play it back inside a real IDE you can grab at any second? Not a video. Not a static article. The next best thing to sitting next to someone while they build. That is Syntact. What it does You give Syntact a topic. An AI builds you a lesson - and instead of a video, you get a real IDE: an editor, a terminal, slides, all playing back like a recording you can scrub, pause and fork. At any frozen moment you can stop, edit the code yourself, hit run, and it actually runs - i.e. it is not a fake terminal printing canned output, it is a real environment in your browser. Under the hood every lesson is 3 streams woven onto one timeline - Code, Terminal, Slides - moving together as the narration plays. The whole thing is built out of atomic little units called stages, so the player can fold, rewind and replay any moment exactly. You are never watching. You are always one keystroke away from taking the wheel. How we built it The core idea is a two-environment model, and honestly most of the project is just that idea taken seriously. At authoring time, the AI does not pretend. It writes and runs real code inside an E2B sandbox - a real cloud machine - so every line in the lesson is grounded in something that actually executed. Then the finished lesson gets frozen and shipped to the learner, where it replays inside a WebContainer right in the browser, no server, no waiting. Author in the cloud, play in the tab. The lesson itself is a frozen timeline. A sequence of stages, each stage an atomic unit across the 3 streams, with a fold and undo/redo model so playback is deterministic - press play twice, get the exact same thing twice. Orchestration runs on Inngest, the streaming bits on the Vercel AI SDK, the API is tRPC end-to-end, and everything lives in AWS Aurora PostgreSQL. A big chunk of the work was contracts. Before writing much code I wrote 9 spec documents - the agent tools, the narration parser, the slide contract, the routes - because an AI that generates structured stuff needs structure to generate into. The slides, for example, are a strict discriminated union: type Slide = | { type: "title"; heading: string; reveals: string[] } | { type: "bullets"; heading: string; reveals: string[] } | { type: "diagram"; heading: string; src: string }; Then validation, in 2 tiers. First a structural parser - cheap, fast, catches a malformed lesson before it ever runs. Then an E2B batch harness that actually executes the code to confirm the lesson, you know, works. And on top of that there is a multimodal review pass: I feed screenshots of the generated UI to Claude through the Anthropic SDK and Inngest AgentKit, and let it critique its own lesson with eyes. A QA reviewer that can see. Challenges we ran into The two environments do not get along by default. E2B and WebContainers are different runtimes - keeping what the AI authored in one place faithful to what replays in the other was a constant fight. The bigger one was determinism. LLMs are messy by nature, and a frozen timeline is the opposite of messy - it has to be exact. Getting model output into something I could freeze, fold and replay without it drifting took way more care than I expected. Then the narration parser - aligning spoken narration to code edits, terminal events and slide reveals on a single shared clock - and validation, because a lesson that looks correct but does not run is worse than no lesson at all. ..oh and the whole thing happened on a hackathon deadline while I was also doing contract work and pretending to sleep. Crunch time is its own runtime. Accomplishments that we're proud of An AI generated a lesson. The lesson actually runs. And you can pause it mid-stream, change the code, and it stays real. That sentence is the whole reason I built this and it works. The frozen-timeline architecture held together across both environments, which for a while I genuinely was not sure it would. The validation harness catches broken lessons before a human ever sees them - it has saved me from shipping garbage more than once. And I shipped it. Spec-first, 9 documents deep, contracts before code, on the clock. (Don't call me a nerd -_-) What we learned The hard part of AI education is not generation. Models can write code all day. The hard part is grounding it in something that really executes, making it deterministic enough to freeze, and validating that it actually works - i.e. all the unglamorous stuff that happens after the model stops talking. I learned a ton about the internals of WebContainers and E2B that I never wanted to know and now cannot forget. I learned that writing the contract first is not bureaucracy, it is the only thing that keeps an AI pipeline from melting. And I learned that you can hand a model your own screenshots and it will tell you, fairly bluntly, that your UI is bad. Useful. Humbling. What's next for Syntact More languages and stacks beyond what it ships with today. Learner accounts, progress, and the ability to fork any lesson into your own playground. A way for people to author and share lessons, so it is not just me feeding it topics at 3am. And the part I actually care about. Back on that 7-inch tablet there was a kid - me, and a few hundred thousand like me in my country - who had the internet and nothing else, and for whom every coding tutorial assumed a laptop, a fast connection, and someone to ask. Syntact runs in a browser tab and teaches by building. That is the whole audience I keep thinking about. The plan I keep circling back to is "Open Course" - free, AI-built, interactive coding lessons for kids in Lebanon who learn the way I did, the hard way. ..oh and maybe one day the kid pausing the video every 4 seconds just gets to press play once. <div