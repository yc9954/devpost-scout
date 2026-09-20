---
slug: "zomath"
url: "https://devpost.com/software/zomath"
title: "Zomath"
hackathon: "DSH Hacks V1"
organization: "DreamWeave"
winner: true
words: 777
team_size: 1
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "domain/developer_tools"
  - "domain/education"
  - "user/educator_student"
  - "substrate/code_repository"
  - "substrate/document_pdf"
  - "substrate/financial_record"
  - "substrate/structured_db"
---

# Zomath

> Math that makes sense Unlike traditional math apps that just give answers, Zomath builds genuine understanding through personalized explanations, visual learning, and adaptive practice.

[Devpost](https://devpost.com/software/zomath) · hackathon [[DSH Hacks V1]]

## Facets

**mechanism** [[realtime_stream]]
**domain** [[developer_tools]] [[education]]
**user** [[educator_student]]
**substrate** [[code_repository]] [[document_pdf]] [[financial_record]] [[structured_db]]

**stack** better-auth, drizzle-orm, elevenlabs, lexical, next.js, openrouter, radix-ui, react, shadcn/ui, tailwind-css, tavily, turso, typescript, vercel

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for zomath

## Body

Zomath Inspiration Every student knows the feeling: you're staring at a blank page the night before an exam, your notes are scattered across three apps, and the one tool that could actually explain what you don't understand is buried behind a paywall or a Google search rabbit hole. I wanted to build the study assistant I wished I had, one that doesn't just hand you answers but actually helps you understand. Not a chatbot, but a tutor named Newton that walks with you through problems, connects new concepts to things you already know, and turns your study sessions into something that actually sticks. What it does Zomath is an AI-powered study platform built around a tutor called Newton. You can have conversations with Newton to get explanations on any subject including math, science, history, literature, economics. You can ask Newton to write study notes directly into a Journal , a rich text editor where Newton's suggestions appear as inline blocks you can accept or deny one at a time. The Practice feature generates quizzes, match-up activities, and flash cards on any topic. Projects act as workspaces where you can group journals, uploaded files (PDFs, slides, videos), links, notes, and questions together around a single course or unit. Zomath Plus unlocks higher usage limits via a subscription. How we built it The frontend is Next.js with Tailwind CSS and shadcn/ui, deployed on Vercel. The editor is built on Lexical (Meta's extensible editor framework), extended with custom DecoratorNode implementations that render AI suggestion cards directly inside the editor's node tree. The backend uses Turso (edge SQLite) with Drizzle ORM for the database, Better Auth for authentication, and Vercel Blob for file storage. AI runs through the Vercel AI SDK with models accessed via OpenRouter. When you ask Newton to edit a journal, a parallel generateText call (max 3 tokens, yes/no) classifies whether the request is an edit intent while the main response streams with no added latency. If it is an edit, Newton returns only the changed blocks separated by blank lines, and each block is inserted into Lexical as a SuggestionNode the user can accept or deny. Web search uses Tavily for real-time sources. Math is rendered with KaTeX, streamed incrementally via Streamdown. Challenges we ran into Lexical's learning curve. Getting DecoratorNode right registering nodes, handling insertBefore + remove inside a single editor.update() transaction, tracking node counts with registerUpdateListener required a lot of digging through source code since the documentation is sparse. Stream parsing. Mixing text content with out-of-band control signals ( data:suggest:true , data:sources:... ) in the same SSE stream was fragile. The line buffer would merge the last text chunk with the next control line if a \n separator wasn't explicit. The fix was prepending every control line with a newline in the API so it always lands on its own line. LLM honesty about editing. Early versions of the prompt caused Newton to say "I can't directly edit your journal" because the model interpreted the instruction as a file system operation it lacked access to. The fix was being explicit in the prompt: just return the changed text the system handles everything else. Accurate quiz generation. LLMs have a tendency to mark wrong answers as correct when generating multiple-choice content. The practice prompt now instructs Newton to solve every problem itself first, then write the options, and back-substitute the answer into the original equation before finalizing. Accomplishments that we're proud of The inline suggestion system in the journal editor. Newton's edits appear as green suggestion cards rendered directly inside Lexical's node tree not in a side panel, not as an overlay each one independently accept-able or deny-able. Getting that to work with Lexical's immutable state model and proper undo/redo support felt like a real win. The parallel AI classification that decides whether to trigger suggestions also runs with zero added latency to the user. What we learned How to extend Lexical properly with DecoratorNode for custom React components inside the editor. How to design SSE streams that carry both content and control signals without corrupting either. That LLM prompts for structured output need to describe what the system does with the output, not just the format the model needs context to behave correctly. How to use Drizzle ORM with Turso for edge-native relational SQLite. Streaming math rendering with KaTeX mid-generation and why complete delimiters matter for partial renders. What's next for Zomath Newton-powered project chat that reasons across all journals, files, and notes in a project at once. Collaborative projects for study groups. Equation graph visualizations linked to journal content. Spaced repetition scheduling for flash cards based on how you've performed on practice sessions. <div