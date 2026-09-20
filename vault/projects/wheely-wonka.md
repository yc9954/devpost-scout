---
slug: "wheely-wonka"
url: "https://devpost.com/software/wheely-wonka"
title: "BenzGPT"
hackathon: "Google Chrome Built-in AI Challenge"
organization: "Google"
winner: true
words: 430
team_size: 1
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "mechanism/voice_speech"
  - "domain/finance_payments"
---

# BenzGPT

> "BenzGPT" is an little car that can be controlled via natural language from a webapplication.

[Devpost](https://devpost.com/software/wheely-wonka) · hackathon [[Google Chrome Built-in AI Challenge]]

## Facets

**mechanism** [[realtime_stream]] [[voice_speech]]
**domain** [[finance_payments]]

**stack** promptapi, speechrecognitionapi, webbluetooth, webspeechapi

## How they structured the write-up

- inspiration
- what it does
- how i built it
- challenges i ran into
- accomplishments that i am proud of
- what i learned
- what's next for benzgpt

## Body

Inspiration LLMs are best known for their most boring usecase: Chatbots. Beyond that, LLMs can be so much more. With Prompt engineering we can tweak each interaction exactly the way we want it and can even achieve things like function calling, where the LLM decides if it is time to trigger a certain function. Unfortunately, the PromptAPI is not yet ready to do classic function calling. But that got me thinking. Can we achieve function calling with only a very structured way of prompt engineering? Let's figure it out. On top of that I also wanted to built a speech interface, where we can interact with the LLM using natural language. What it does BenzGPT is am AI Agent that uses the PromptAPI to understand a given command and then decide what it should do next. Should it just chat? Or should it move? More than that you can actually talk to BenzGPT! To round it all off, of course, it's not just a virtual conversation. A toy car can also be controlled via WebBluetooth. How I built it It uses the WebSpeechAPI to transcribe spoken words into text and then uses the SpeechSynthesisAPI to speak back to the user. The core of BenzGPT is the FunctionCallingPromptAPI. It is an abstraction layer to convert any LLM (in this case the PromptAPI) into a function calling API: github.com/nico-martin/benz-gpt?tab=readme-ov-file#function-calling Challenges I ran into The biggest challenge was definitely to find the right prompt to make sure the LLM understand the functions and also sticks to the instructions when it generates the answer. I figured out that most existing function calling frameworks use an XML-like syntaxt to have a structured output. Unfortunately this did not work well with the PromptAPI, since XML often produced an "untested language" error. So I had to use JSON, which did work quite well if I added some checks before the parsing. And since I am also using SpeechSynthesis I wasn't able to use streaming anyway. Accomplishments that I am proud of I think I solved the prompt engineering part quite good, so the FunctionCallingPromptAPI can be used with different LLMs as well. Also the Speech-to-text and Text-to-speech works incredible good. What I learned A lot about how function calling works and how we can use LLM for tasks that require a very strict output format. What's next for BenzGPT Being able to move is quite cool, but its only one part of what makes an robot "human". I am also thinking about different functions, where the LLM actually acts as an Agent that orchestrates different (machine-learning?)-operations. <div