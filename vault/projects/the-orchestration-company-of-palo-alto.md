---
slug: "the-orchestration-company-of-palo-alto"
url: "https://devpost.com/software/the-orchestration-company-of-palo-alto"
title: "The Orchestration Company of Palo Alto"
hackathon: "TreeHacks 2026"
organization: "TreeHacks"
winner: true
words: 1679
team_size: 4
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/multi_agent"
  - "mechanism/realtime_stream"
  - "mechanism/simulation_digital_twin"
  - "mechanism/voice_speech"
  - "domain/developer_tools"
  - "user/developer"
  - "substrate/code_repository"
  - "substrate/sensor_telemetry"
  - "substrate/video_visual"
  - "substrate/web_dom"
---

# The Orchestration Company of Palo Alto

> OS of tomorrow, Claude Code of today

[Devpost](https://devpost.com/software/the-orchestration-company-of-palo-alto) · hackathon [[TreeHacks 2026]]

## Facets

**mechanism** [[multi_agent]] [[realtime_stream]] [[simulation_digital_twin]] [[voice_speech]]
**domain** [[developer_tools]]
**user** [[developer]]
  <sub>weak: legal_professional</sub>
**substrate** [[code_repository]] [[sensor_telemetry]] [[video_visual]] [[web_dom]]

**stack** browserbase, claude, cloudflare, docker, elevenlabs, express.js, fastapi, groq, javascript, mcp, modal, next.js, openai, python

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for the orchestration company of palo alto
- openai: artificial intelligence track
- anthropic: human flourishing track
- modal: sandbox challenge
- anthropic: claude agent sdk
- human capital: fellowship prize
- greylock: best multi-turn agent
- interaction: build with poke
- decagon: best conversation assistant
- browserbase: best web automation with stagehand

## Body

The Orchestration Company of Palo Alto Technical Diagram Outdoor Running Agents FOR SPONSOR JUDGES, PLEASE SCROLL TO THE BOTTOM FOR TRACK-SPECIFIC INFO Inspiration Have you ever had to manage 6 or 7 Claude Code instances at once? Have you ever felt like there's not enough space on your screen for all of the apps you need to code? Fear no more, introducing the Orchestration Company of Palo Alto! What It Does We allow you to manage all of your coding agents through a brand-new AR interface. Instead of having to constantly switch tabs, babysit Claude Code instances, and doomscrolling Twitter until your Cursor prompt finished, we allow you to hyper-accelerate your productivity through this new coding interface in using Apple Vision Pro. How We Built It For a technical diagram, please refer to the last photo. It helps better explain what is going on in our app. Apple Vision Pro is integrated into this simulator on visionOS: the user is placed in an office environment - floor, cubicles, and desks - and a set of agents is represented by spawning one desk per agent. The 3D world grows on demand: one agent at one desk at launch, and requesting another background task spawns one more agent at a new desk. The immersive experience is built with Xcode, SwiftUI, and an app-wide state model (AppModel) that holds agentCount and immersiveSpaceState. ContentView provides the 2D UI (Enter immersive space and Build an AI agent), while ImmersiveView renders the 3D office and dynamically allocates desks. This single source of truth both defines how many agents exist and ensures actions like adding agents are only available when the user is in the immersive space, so the simulation stays in sync with the Vision Pro session state. We have a TreeHacks Fix Agent MCP (Model Context Protocol) server. It’s implemented with FastMCP and exposes tools such as run_fix, run_analysis, and run_fix_default_repo so callers can trigger Modal sandbox runs and Claude Agent SDK fixes over the network. The server listens on localhost (and tunnels to Poke UI) and uses the streamable HTTP transport : clients send HTTP requests to /mcp and the MCP protocol runs over HTTP with Server-Sent Events (SSE) for streaming. So communication is HTTP/SSE, not WebSockets - one HTTP request can open a stream for server-to-client updates (e.g. tool progress or long agent output). The test client uses mcp to get a read/write pair and a ClientSession for initialize(), list_tools(), and call_tool(). The FastAPI backend acts as an MCP client: it connects to an MCP server (e.g. MCP_HTTP_URL, possibly a separate process or the same poke-mcp on another port) via mcp.client.http.http_client, then calls the run_fix tool with the user’s instruction and optional repo URL and returns the tool result as text. visionOS or any client → FastAPI /fix → MCP client session (HTTP) → poke-mcp (streamable HTTP on 8765) → FastMCP tools → Modal sandbox + Claude Agent. The streaming is handled by the MCP streamable HTTP/SSE transport. Challenges We Ran Into Working with VisionOS is very non-linear - we were very new to it, didn't know how to properly implement some of the more complicated aspects of our hack (and had to opt-in for hackier solutions), and didn't properly understand some of the technical limitations we might run into later on. Accomplishments That We're Proud Of This required learning a lot of brand-new tech that we'd never worked with before - working with multi-turn agents and building what (for most of us) was our first-ever AR hack. We also wanted to make the design feel warm and inviting. We designed animated assets to give the hack a whimsical feel, and we hope that it makes you feel at home :) What We Learned We learned that building hacks for the fun of it all is awesome, and we'll definitely doing it again. VisionOS is also really difficult to work with - we should budget more time to iron out technical issues. What's Next for The Orchestration Company of Palo Alto Build, break, ship, and dream :) Also go back to Waterloo and lock in for exams after TreeHacks is over. Sponsor Tracks Please review our technical diagram (last photo) to check out the technical complexity of our hack! OpenAI: Artificial Intelligence Track We used OpenAI models for speech-to-text and text-to-speech which allows for communication between the user and the multi-turn agent. The multi-agent system itself is run by an orchestrator agent, which uses a custom MCP to spin up code sandboxes for remote code execution. Inside the sandboxes, we run a coding agent in a harness to be able to make changes to the codebase and put up a PR. Finally, we use AI to validate that the changes made by the agent were valid - the AI traverses the webpage for frontend fixes and tests expected behaviour. Anthropic: Human Flourishing Track It's evident that humans are reaching a limit where we receive more signals than we can handle. Engineer switch tabs 24/7 to supervise their coding agents. Employees report that they feel "more overstimulated than ever". The need is clear - we need a way to scale the way we process signals. This project is a first attempt on that - we implemented a thesis we had about the future of software engineering (that most engineers will be product engineers, and this medium creates enough space for folks to easily supervise their agents), and created this MVP project to demonstrate it. Modal: Sandbox Challenge As we spin up coding agents to modify new/existing parts of the codebase, we need to be able to apply these changes in an isolated environment. We use sandboxes to create a brand new coding environment, spin up a coding agent inside of it, clone the existing repo, apply the engineering fix, put up a PR, and double check that the expected behaviour is met through browser automations. Sandboxes are a central piece of this - without them, we wouldn't be able to make changes in isolation,. Anthropic: Claude Agent SDK It's evident that humans are reaching a limit where we receive more signals than we can handle. Engineer switch tabs 24/7 to supervise their coding agents. Employees report that they feel "more overstimulated than ever". The need is clear - we need a way to scale the way we process signals, and we started by reimagining what an agent orchestration interface might look like. For this project, we needed to spin up coding agents that make large scale changes to the codebase. To implement these agents, we used the Claude Agent SDK to create an agent, which would implement the requested change, and then put up a PR showcasing it. Human Capital: Fellowship Prize It's evident that humans are reaching a limit where we receive more signals than we can handle. Engineer switch tabs 24/7 to supervise their coding agents. Employees report that they feel "more overstimulated than ever". The need is clear - we need a way to scale the way we process signals. This project is a first attempt on that - we implemented a thesis we had about the future of software engineering (that most engineers will be product engineers, and this medium creates enough space for folks to easily supervise their agents), and created this MVP project to demonstrate it. We're a team of four Waterloo friends with varying backgrounds, and we'd be open to potentially continuing this project through the fellowship! Greylock: Best Multi-Turn Agent In order to make this project work, we needed an orchestrator. The orchestrator is a multi-turn agent with persistent context across terms, consistent personality, and the ability to make educated decisions on what to do. We were able to create a system where a persistent, multi-turn agent, uses MCPs to spin up sandboxes with coding agents inside, which are able to act on instructions and implement fixes to an existing codebase. Interaction: Build With Poke Most Useful: It's evident that humans are reaching a limit where we receive more signals than we can handle. Engineer switch tabs 24/7 to supervise their coding agents. Employees report that they feel "more overstimulated than ever". The need is clear - we need a way to scale the way we process signals, so we took a first-pass at what a coding IDE run by a conversational assistant (Poke) would look like. Most Technically Complex: Please take a look at the technical diagram (last photo). It shows how complex our system really is :) Most Viral: We did everything we could to make the project go viral. PFA the platforms which we posted / interacted on, and the metrics we reached: In-Person: ran into a bunch of people, got them to try our product! Twitter/X: 6,200+ interactions LinkedIn: 13,000+ impressions, 153 likes, 16 comments, 2 reposts Decagon: Best Conversation Assistant Our project is an implementation of what a coding interface would look like if it was a conversational assistant. We implemented a multi-turn agent with persistent context across terms, consistent personality, and the ability to make educated decisions on what to do. It helps you with your tasks, and can refer to previous conversions (either relevantly, or to make fun of you). We were able to create a system where this persistent, multi-turn agent, uses MCPs to spin up sandboxes with coding agents inside, which are able to act on instructions and implement fixes to an existing codebase, and then the multi-turn agent can discuss their results. Browserbase: Best Web Automation with Stagehand The biggest engineering problem at startups is that the pace at which senior engineers review code is much slower than the speed at which junior engineers can generate it using AI. To tackle this problem, we used Browserbase to tackle this issue by implementing fix validation. Using Stagehand, we are able to automatically traverse websites, and validate that the intended result was achieved. We also show the Browserbase recording of the agentic testing of a user's changes once the PR is put up by the agent, and this helps validate that the agent's changes are legit. <div