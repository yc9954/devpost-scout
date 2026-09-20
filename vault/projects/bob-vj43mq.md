---
slug: "bob-vj43mq"
url: "https://devpost.com/software/bob-vj43mq"
title: "Bob"
hackathon: "Cal Hacks 12.0"
organization: "Cal Hacks"
winner: true
words: 745
team_size: 3
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/measured_ablation"
  - "mechanism/on_device_local"
  - "mechanism/realtime_stream"
  - "mechanism/vision_ocr"
  - "domain/developer_tools"
  - "domain/education"
  - "domain/labor_employment"
  - "domain/transportation"
  - "user/frontline_worker"
  - "substrate/geospatial"
  - "substrate/video_visual"
---

# Bob

> AR glasses for physical work. It sees what you see, hears what you hear, and gives real-time responses to help you build anything.

[Devpost](https://devpost.com/software/bob-vj43mq) · hackathon [[Cal Hacks 12.0]]

## Facets

**mechanism** [[measured_ablation]] [[on_device_local]] [[realtime_stream]] [[vision_ocr]]
**domain** [[developer_tools]] [[education]] [[labor_employment]] [[transportation]]
**user** [[frontline_worker]]
**substrate** [[geospatial]] [[video_visual]]

**stack** agent, ar, gemini, python, spectacles, typescript, websockets, yoloe

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for bob

## Body

Inspiration Last year, the US had a shortage of 70,000 electricians and 642,000 mechanics. With one in five of these tradespeople over the age of 55 and growing demand in data centers and electric vehicles, this gap is only getting bigger. But what if everyone could become a skilled technician in under 5 minutes? This is why we built Bob. By using this AI+AR assistant, homeowners could handle simple repairs, vocational schools could train workers more efficiently, and professionals could work faster, safer, and more collaboratively. What it does Bob is a pair of agentic AR glasses that automatically watches over your actions, listens to your questions, and responds to your needs in real time. This could be instructions for your next steps, object-specific details (like a resistor's resistance), or warnings before you do something dangerous. For complex, collaborative tasks, it can also contact your teammates or highlight selected objects (in case you don't know what a “Kellum grip” is). While existing smart glasses focus on specific workflows like trivia or design, we built Bob to be a generalist from the outset. It can help you build electrical circuits, repair cars, and assemble furniture. With more tools, the variety of tasks Bob can do would be even greater. How we built it We’re using Snapchat Spectacles as our hardware and Gemini Live as our base model: the Spectacles stream video and audio data to a Python-built WebSocket server. On initial connection, we establish a new WebSocket connection to Gemini Live and store all subsequent audio and video frames in the session. Asynchronous workers handle buffering uploads, processing responses, executing tool calls, and resuming Gemini Live sessions efficiently. For tools, we used SMTP to integrate Gmail, YOLOE-11 for object detection via text prompts, the Python Slack SDK to integrate Slack, and Google Generative AI SDK for Google Search and Google Map. When voice activation detects that the user has stopped speaking, Gemini Live returns text and tool calls. These get executed and sent back to the Spectacles to update the overlay and bounding box highlights, guiding users through their project. Finally, we would like to note that all WebSockets connections are reused, minimizing the latency between Spectacles and the server. Challenges we ran into Messaging with Gemini Live over WebSocket turned out to be particularly challenging, with bugs in the asynchronous context manager and a demanding manual implementation of retry and bidirectional socket management. In addition, projecting pixel coordinates from the camera frame to the Snap Spectacle for object detection required debugging complex coordinate transformations. We solved these issues through test-driven development, A/B testing, and binary search. Accomplishments that we're proud of As far as we know, we made the first pair of AR glasses with a multimodal AI agent that can talk back and forth with the user and instruct them in completing physical tasks. Although smart glasses exist, they are incapable of maintaining coherence over a physical task while accepting real-time input, often relying on obtrusive UI like buttons. By integrating live, multimodal agent and object detection into Snap Spectacles, we turned AR glasses into an agent with memory that helps anyone build whatever they want. We’re especially proud of getting the Spectacles to work since none of us had touched AR glasses before this project. What we learned Developing AR applications with Lens Studio Working with live instead of turn-based agents State management for WebSocket What's next for Bob When we interviewed our users about what else they would like to do with Bob, they gave really creative answers: cooking, first aid, martial arts…While these tasks are far from our original goal, Bob can quickly adapt to them because of its agentic framework. Every new tool can unlock a new field for Bob. For example, if we had added Composio’s toolset, Bob would be able to manage your calendar, send Slack messages, and read Notion pages. We could even link Bob to a humanoid robot that collaborates with the user on physical tasks. The future path for Bob is to become the orchestrator directing tens, hundreds or even thousands of humans at a time concurrently on large projects. Managing and monitoring all of them towards common goals while maintaining a common state across workers which would allow for effective collaboration. In addition, Bob is limited by its base models. If we had the hardware, we would run Qwen 2.5-Omni locally to reduce latency and use GroundingDINO to detect objects with greater accuracy. <div