---
slug: "codecrack"
url: "https://devpost.com/software/codecrack"
title: "CodeCrack"
hackathon: "TreeHacks 2025"
organization: "TreeHacks"
winner: true
words: 791
team_size: 4
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/multi_agent"
  - "mechanism/realtime_stream"
  - "mechanism/simulation_digital_twin"
  - "domain/developer_tools"
  - "domain/education"
  - "domain/labor_employment"
  - "user/educator_student"
  - "substrate/code_repository"
  - "substrate/structured_db"
---

# CodeCrack

> Master coding interviews with CodeCrack: a voice-driven AI agent simulating dynamic, real-time mock interviews, delivering interactive feedback to sharpen your skills.

[Devpost](https://devpost.com/software/codecrack) · hackathon [[TreeHacks 2025]]

## Facets

**mechanism** [[multi_agent]] [[realtime_stream]] [[simulation_digital_twin]]
**domain** [[developer_tools]] [[education]] [[labor_employment]]
**user** [[educator_student]]
**substrate** [[code_repository]] [[structured_db]]

**stack** elevenlabs, javascript, node.js, python, vercel

## How they structured the write-up

- inspiration
- how we built it
- challenges we ran into
- what we learned
- what's next for codecrack

## Body

Inspiration Want to ace that upcoming technical interview for your dream job? LeetCode is a great place to start for developing good problem solving skills, but it lacks the interactive communication demands of a live coding interview where interviewers assess your problem-solving, debugging, and communication skills in addition to your ability to code. It’s fun to recruit your friends to help conduct a mock interview but these resources are not available to everyone. From under-resourced students to experienced builders, interview preparation materials and access to experienced coders can be an obstacle. As engineering students who have undergone Software Engineering recruiting, we wanted to build a tool that bridges this gap - allowing coders to improve their skill set while simulating the pressure of a live interview with real-time feedback. We built CodeCrack to empower anyone to crack their interview with confidence. How we built it We built CodeClack on a Vercel web platform with functional modifications made for integrating the AI agents to execute their client tasks, keep track of state, and upstream information to the voice. On top of this, we built on the user interface to reflect the various components of our project. For instance, we’ve integrated an IDE with Monaco, the code editor behind VScode, and Pyodide, a Python interpreter so users can run and execute their code. Leveraging ElevenLabs voice agents, CodeCrack offers both behavioral and technical interviews. To simulate a Software Engineering coding interview as closely as possible, In the technical coding challenge, the AI agent will introduce themselves, give an overview of the interview, give the user a moment to introduce themselves, and then will dive into the coding challenge, populating the user’s screen with the challenge and reading it outloud. The agent is designed to take on the persona of a more senior level Software Engineering interviewer, processing how the user breaks down the problem and explores various paths before diving into an approach, offering an open-ended hint if the user indicates they are stuck or asking a follow-up question if they are on the right track. Within our agentic system, there are two main flows of information sharing: agent to client and client to agent. For the coding challenge question, we retrieved leetcode questions and solutions from a HuggingFace dataset, and in the first agent to client stream, we developed a client tool, sendNewQuestion, that randomly retrieves a question within the user’s difficulty preference, upstreaming it to the voice agent to read aloud. The other mode, client to agent, is activated when the user clicks “Run Code”, so the user’s code submission can be tested for functionality and the agent can generate feedback on code style. The agentic system is keeping track of the state of interactions, making decisions to pivot the conversation to get the user closer to a functional solution without revealing too much information. After the user ends the interview, an API call is sent to ElevenLabs’ criteria evaluation feature to get the agent’s feedback on communication, problem-solving, and debugging based on the overall state of interactions. Challenges we ran into With no prior experience building with AI agents, the primary challenge we initially faced was understanding how agentic frameworks are built, and the tradeoffs between multi-agent frameworks and single agent frameworks. The next challenge we faced was learning how to influence single agent frameworks, and specifically, how to send information to it and retrieve information from it for various components of our project’s functionality. For instance, after retrieving a leetcode question we wanted to upstream this information to populate the user’s screen and have the AI agent read the problem out loud, but we faced difficulty understanding and building on the information streams that come with client tools. Expanding on this, all the builders on the team are most comfortable with Python and have no experience building extensive frontends. After realizing our Python client tools were not easily compatible with the AI agent codebase, we converted that entire part of our codebase to lay within Next.js and React, with some help from the ElevenLabs sponsor with only hours left before the deadline. What we learned Over the last 36 hours we learned how to build our first tools with AI agents. In particular, we designed an AI agent for our interviewer persona and built various client tools to handle retrieving leetcode questions, evaluating the user’s code on run, and populating the UI with the coding challenge and comprehensive feedback. Specifically in terms of new technologies, we had no prior experience working with Node.js and React, so it was an exciting challenge to focus on user interface design. What's next for CodeCrack We look forward to building a more comprehensive system including System Design, Python trivia, and resume-based questions! <div