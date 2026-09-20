---
slug: "decision-room"
url: "https://devpost.com/software/decision-room"
title: "Decision Room"
hackathon: "Amazon Nova AI Hackathon"
organization: "Amazon"
winner: true
words: 781
team_size: 1
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/multi_agent"
  - "mechanism/realtime_stream"
  - "mechanism/simulation_digital_twin"
  - "substrate/code_repository"
  - "substrate/sensor_telemetry"
  - "substrate/web_dom"
---

# Decision Room

> Practice high-stakes meetings before they happen. Present your case to an AI panel, answer tough questions, and watch how their private deliberation turns into a decision.

[Devpost](https://devpost.com/software/decision-room) · hackathon [[Amazon Nova AI Hackathon]]

## Facets

**mechanism** [[multi_agent]] [[realtime_stream]] [[simulation_digital_twin]]
**substrate** [[code_repository]] [[sensor_telemetry]] [[web_dom]]

**stack** apprunner, bedrock, nova, polly

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for decision room

## Body

Decision Room Inspiration Important decisions in organizations are rarely made by one person. Promotions, funding approvals, and major initiatives are usually evaluated by a panel of stakeholders with different priorities and perspectives. Yet most people never get to see how those conversations actually unfold behind closed doors. Preparing for these situations is difficult. You can rehearse your presentation, but you rarely get realistic practice responding to tough questions or understanding how different decision-makers interpret your answers. We built Decision Room to simulate those high-stakes conversations. The idea was simple: what if you could present your case to an AI committee, answer their questions, and then observe how they privately deliberate before making a decision? What it does Decision Room is a multi-agent simulation that stress-tests ideas before the real world does. Users present a case, such as explaining their accomplishments during a promotion review or pitching a new initiative. An AI panel representing different stakeholders listens and then begins a Q&A session where each member asks questions from their own perspective. Once the interaction ends, the panel enters a closed-door deliberation phase . Here, the user observes how the panel members interpret the answers, challenge each other’s viewpoints, and gradually form a decision. Throughout the discussion, Decision Room reveals evaluation signals such as promotion confidence, strategic leadership perception, execution ownership, decision momentum, and consensus gap. Instead of just receiving a result, users can see how the reasoning behind the decision emerges . How we built it Decision Room is a lightweight web application built with a simple but powerful architecture. The frontend is implemented with vanilla HTML, CSS, and JavaScript , allowing the interface to remain responsive and easy to deploy. Voice input is supported through the browser’s Web Speech API , enabling users to present their case naturally through speech or text. On the backend, a Node.js and Express server orchestrates the simulation. Amazon Bedrock powers the multi-agent reasoning system that generates questions, responses, and the final panel deliberation. Each panel member operates as a distinct persona with their own priorities and evaluation lens. To make the interaction more engaging, we integrated Amazon Polly to generate natural voice playback for panel questions. During the closed-door discussion, the backend streams panel dialogue in real time using Server-Sent Events (SSE) so users can watch the deliberation unfold step by step. Together, these components create the illusion of a real committee discussion happening behind the scenes. Challenges we ran into One of the biggest challenges was designing a system where multiple AI panelists behave like independent decision-makers instead of repeating similar responses. We had to carefully design prompts and roles so each agent evaluates the same information from a different perspective, such as leadership impact, cross-team collaboration, or operational execution. Another challenge was pacing the deliberation experience. If the discussion appears all at once, it feels like a summary. By streaming messages sequentially, we were able to simulate a realistic conversation where panel members react to each other’s opinions. Finally, balancing voice interaction with text visibility required careful UX decisions so users could follow the conversation clearly while still enjoying natural speech interaction. Accomplishments that we're proud of We created a system that makes organizational decision-making visible. Instead of simply generating AI responses, Decision Room shows how multiple stakeholders interpret the same message differently and how those interpretations influence a final decision. The combination of voice interaction, multi-agent reasoning, and a staged decision process creates an experience that feels surprisingly realistic. Watching the panel debate your answers reveals insights that are normally hidden from candidates and presenters. We are especially proud that the system works end-to-end: presentation, Q&A, closed-door deliberation, and evaluation metrics all flow naturally within a single session. What we learned Building Decision Room reinforced how powerful multi-agent simulations can be for understanding complex social dynamics. We discovered that decisions rarely depend on a single answer. Instead, they emerge from how different stakeholders interpret the same information and influence each other’s opinions. We also learned that showing the reasoning process is more valuable than just producing an outcome. Users gain the most insight when they can observe the discussion that leads to a decision. What's next for Decision Room We plan to expand Decision Room beyond promotion reviews into other high-stakes scenarios such as startup pitches, leadership proposals, and strategic planning sessions. Future versions could allow users to customize panel roles, simulate different organizational cultures, and compare how decisions might evolve under different stakeholder compositions. Longer term, we envision Decision Room as a tool for practicing important conversations before they happen in the real world, helping people refine their communication, anticipate tough questions, and better understand how decisions are made. <div