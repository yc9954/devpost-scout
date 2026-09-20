---
slug: "novadine"
url: "https://devpost.com/software/novadine"
title: "SonicServe"
hackathon: "Amazon Nova AI Hackathon"
organization: "Amazon"
winner: true
words: 778
team_size: 2
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/human_in_the_loop"
  - "mechanism/realtime_stream"
  - "mechanism/voice_speech"
  - "domain/health_clinical"
---

# SonicServe

> SonicServe is a highly natural conversational AI voice agent that manages restaurant calls, orders, reservations, and customer queries while seamlessly communicating with management.

[Devpost](https://devpost.com/software/novadine) · hackathon [[Amazon Nova AI Hackathon]]

## Facets

**mechanism** [[human_in_the_loop]] [[realtime_stream]] [[voice_speech]]
**domain** [[health_clinical]]
  <sub>weak: developer_tools</sub>

**stack** agents, amazon-web-services, aws-sdk, bedrock, bolt, clover, docker, ecr, ecs, fastapi, fastmcp, git, httpx, mcp

## How they structured the write-up

- the story behind sonicserve

## Body

SonicServe - An AI voice agent for restaurants seamless integration with voice model Escalates critical cases SonicServe - Architecture Design SonicServe handling automated restaurant order requests through real-time AI voice interaction. The Story Behind SonicServe SonicServe was inspired by a real experience at my uncle’s restaurant in Boston . It’s a popular place known for great food and friendly service , and on weekends the restaurant becomes incredibly busy. During peak hours the staff are constantly multitasking . Chefs are working in the kitchen, online delivery orders are coming in, customers are arriving for reservations, and the phone keeps ringing with people calling to ask questions, place orders, or reserve tables. In the middle of this chaos, it’s easy for calls to go unanswered . One particularly busy weekend, a call went unanswered because the staff were helping customers and preparing orders. A few days later, a customer called back and complained that the restaurant’s phone was unresponsive . Seeing how disappointed my uncle felt about letting a customer down made it clear how easily restaurants can lose opportunities and loyal customers simply because they are overwhelmed during their busiest times. Restaurants want to provide great service, but the reality is that during peak hours it’s impossible for staff to answer every call while also running the restaurant. That moment inspired the idea behind SonicServe : an AI-powered voice assistant that ensures every call is answered and every customer gets help , even during the busiest hours. Instead of forcing customers through frustrating IVR menus like “Press 1 for reservations” , SonicServe acts as a natural conversational agent that customers can simply talk to. When someone calls the restaurant, the AI can: Answer questions about the menu Take food orders Manage reservations Provide restaurant policies or hours Escalate complex issues to staff By connecting to restaurant systems through Model Context Protocol (MCP) tool calling , SonicServe can retrieve menus, place orders, check reservations, and access operational information in real time , allowing it to perform real actions rather than just provide static responses. The system also supports the restaurant staff behind the scenes . We built a management-side agent integrated with Slack using Strands , which allows managers to retrieve operational information, monitor requests, and respond to escalations directly from Slack. Managers can also update important information like restaurant policies, menu changes, or business hours through Slack, and those updates automatically propagate to the AI agent so future callers receive the most accurate and up-to-date information . This creates a flexible system where the AI assistant works alongside the restaurant team rather than replacing them , with human-in-the-loop support whenever a situation requires human judgment. At the core of SonicServe is Amazon Nova 2 Sonic , which made it possible to build a natural voice experience . Nova Sonic provides bidirectional streaming capabilities that allow real-time voice conversations between callers and the AI agent. Incoming calls are routed through Twilio Programmable Voice Streaming , which sends audio from the caller to our application server. The server streams the audio to Nova Sonic , which processes the speech, understands the intent, generates a conversational response, and streams the audio reply back to the caller in real time . This streaming architecture allows SonicServe to maintain smooth conversational flow while simultaneously processing speech, generating responses, and invoking backend tools during the conversation. Using Amazon Nova 2 Sonic was critical because voice interactions require extremely low latency . Even small delays can make conversations feel unnatural or robotic . Nova’s real-time streaming capabilities allow SonicServe to respond quickly and handle natural conversational behaviors like pauses, interruptions, and changing requests . This allowed us to move beyond traditional phone automation and build something that feels like talking to a helpful restaurant assistant rather than navigating a machine. Through building SonicServe, we learned that creating effective voice AI requires much more than just accurate answers. It requires thoughtful conversation design , managing real-time streaming events , and ensuring the system can interact reliably with real-world business systems like POS platforms and reservation tools. We also explored ways to incorporate conversational cues such as “mm-hmm” or “got it” to make interactions feel more human . Another challenge we explored was detecting spam or irrelevant calls while ensuring legitimate customers could always reach the restaurant. Ultimately, SonicServe demonstrates how real-time AI voice agents can support businesses during their busiest moments . By combining Amazon Nova 2 Sonic’s streaming voice capabilities , operational tool integrations , and human oversight , SonicServe helps restaurants ensure every call is answered , every customer is supported , and staff can focus on delivering great food and hospitality . <div