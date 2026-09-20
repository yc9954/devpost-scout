---
slug: "atlas-tlfpkz"
url: "https://devpost.com/software/atlas-tlfpkz"
title: "Atlas"
hackathon: "HackGT 12: Midnight at the Museum"
organization: "HexLabs"
winner: true
words: 611
team_size: 4
has_repo: false
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/retrieval_grounding"
  - "domain/developer_tools"
  - "user/developer"
  - "substrate/code_repository"
  - "substrate/document_pdf"
  - "substrate/structured_db"
---

# Atlas

> Unified memory across your entire AI stack, complete with codebase visualization, prompt libraries, and advanced context management.

[Devpost](https://devpost.com/software/atlas-tlfpkz) · hackathon [[HackGT 12- Midnight at the Museum]]

## Facets

**mechanism** [[retrieval_grounding]]
**domain** [[developer_tools]]
**user** [[developer]]
**substrate** [[code_repository]] [[document_pdf]] [[structured_db]]

**stack** betterauth, bytecode, cedaros, composio, electron, gemini, mastra, openai, react, robotjs, three.js, typescript, zod

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for atlas

## Body

Inspiration Atlas was born from that real frustration of "context amnesia" that comes with the rapidly growing AI space-- endless prompts, giant codebases, and the ever-growing complexity of onboarding and context switching (it can take 6 to 8 months for a new software engineer to become fully productive in an enterprise!) . Not to mention the rising costs of AI-powered workflows, and the limitations of existing productivity and developer tools. Drawing inspiration from the convenience of the macOS emoji picker and second brain systems, Atlas aspires to offer instant, seamless access to knowledge anywhere on the desktop, making sure you and your AI tools are always on the same page. Atlas is a unified AI memory system , unlocking rapid onboarding, smarter collaboration, and unprecedented transparency, ensuring engineers and power users never start from zero in any project or conversation. What it does Upload a repository and get a beautiful, blocked, visualized codebase: Users can either enter a link to their repository or connect to a local repository to instantly index and visualize codebases complete with summaries from individual function to repository. Use 'Ctrl/Cmd ' + '/' and access your codebase and personal context anywhere: Atlas automatically synthesizes code, documentation, and communication from platforms like GitHub, Slack, Databases, or documentation apps into unified, smart "context blocks." These blocks live at the intersection of code and conversation, allowing users to search, reference, and insert them into any workflow via the Ctrl + '/' shortcut. Store and chain your own prompts for lightning fast memory setup for any AI tool: Users can build their own AI setup prompts that they can chain and grow to access essential context anywhere, saving time, token cost, and providing unified memory to every AI agent you use. How we built it Frontend : React 19.1.1 + TypeScript + Tailwind CSS + Three.js for 3D call graphs Backend : Express.js with Electron 38.1.0 + Node.js main process, file tree analysis, context pipeline, overlay system AI Stack : Mastra AI + Vercel AI SDK + Cedar OS with OpenAI's Agents SDK, structured outputs via Zod. Authentication : Better Auth 1.3.18 with external Express backend, email/password auth Development : Electron Vite + TypeScript + Biome linting, Electron Forge packaging Challenges we ran into Analyzing massive repositories meant designing scalable chunking and parallelization techniques to process thousands of files while controlling memory usage. Building a persistent, shareable context memory demanded careful schema design for ultrafast semantic search and safe, user-friendly referencing. Shipping a truly cross-platform overlay required overcoming technical obstacles with system windowing, global shortcuts, and AI integrations. Accomplishments that we're proud of Designed a fully shippable, integrated application. No shortcuts. No corners cut. Pure functionality and beautiful UI/UX. Simply type Ctrl/Cmd + '/' and access any aspect of your work or codebase instantly. Built a persistent, context-aware memory engine that brings institutional knowledge to any chat, code review, or document. Achieved subsecond search and reference resolution for repositories with thousands of files and millions of lines of code. Unified multiple data sources and AI models into a user experience that feels natural, intuitive, and empowering. Delivered a seamless, performant overlay experience cross-compatible across macOS and Windows What we learned Building Atlas revealed the importance of balancing engineering rigor with fast iteration, especially when integrating rapidly-evolving AI APIs and cross-platform native features. We gained deep insight into the nuances of workspace privacy, structured context management, and the art of crafting delightful, instant-access UX experiences. What's next for Atlas We're exploring smarter knowledge surface mechanisms—expanding integrations, adaptive summarization, and multi-modal visualizations that go far beyond code. The roadmap includes making Atlas even more collaborative and customizable for teams of any size. <div