---
slug: "retention"
url: "https://devpost.com/software/retention"
title: "Retention"
hackathon: "UC Berkeley AI Hackathon 2026"
organization: "Cal Hacks"
winner: true
words: 830
team_size: 4
has_repo: false
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/measured_ablation"
  - "mechanism/multi_agent"
  - "mechanism/simulation_digital_twin"
  - "mechanism/voice_speech"
  - "domain/education"
  - "user/educator_student"
  - "user/legal_professional"
  - "substrate/transcript_audio"
---

# Retention

> Retention uses Meta's brain-simulation model to optimize educational videos for students of all ages, automatically editing clips and maximizing retention with a multi-agent generator/evaluator loop

[Devpost](https://devpost.com/software/retention) · hackathon [[UC Berkeley AI Hackathon 2026]]

## Facets

**mechanism** [[measured_ablation]] [[multi_agent]] [[simulation_digital_twin]] [[voice_speech]]
  <sub>weak: realtime_stream</sub>
**domain** [[education]]
**user** [[educator_student]] [[legal_professional]]
**substrate** [[transcript_audio]]
  <sub>weak: geospatial</sub>

**stack** claude, deepgram, lightningai, microsoft-band, pika, python, react, tokenrouter

## How they structured the write-up

- inspiration
- what it does
- tech stack
- challenges we ran into
- what we learned
- what's next for retention

## Body

Architecture Architecture diagram for our Retention Tribe V2 pipelineDiagram Real-time cortical heat map of brain activation during educational video, red means engaged, blue means less engaged BEFORE Retention: "mathantics" common denominators for YouTube Kids AFTER Retention: Visualizing fractions as pizza pies, AI-powered via Pika FOR SPONSORS: Specific tool usage is outlined in the Tech stack section. Retention Maximize student retention of lecture materials! Given an educational video, Retention uses Meta's brain-simulation model to test how students react. It then uses a closed agent loop with a generator and evaluator to iteratively edit the video until neural engagement peaks. Inspiration Every student has experienced one class that they just can't seem to understand. Between confusing lectures and poorly-written assignments, some concepts just won't click. Teachers and professors often struggle to identify these problem areas since it is hard for the student to articulate where they are struggling. We sought to close this gap for educators with a simple idea: have a digital test audience whose brain you can read directly. Meta's open-sourced TRIBE v2 model does just that by predicting the brain's fMRI response to multimodal input. What it does Retention takes an instructional video and makes it more engaging, automatically, by treating a simulated brain as the judge: Input A user inputs an educational video with optional instructions through text/voice. Evaluator Agent Retention runs the inputted video through an evaluator agent, which utilizes Meta's TRIBE v2 brain-encoding model to predict the viewer's neural response across the brain and surface low-engagement segments. It then uses multiple LLMs (through OpenRouter) to analyze brain activity alongside the video transcript to identify timestamps when focus and retention are lost. This is done by tracking activity in two regions: the association cortex, responsible for thinking and understanding, and the primary sensory cortex, which processes raw visual and audio input. After an LLM-generated analysis is created, the evaluator passes this information to the generator agent. Generator Agent The generator uses the information passed by the evaluator and the user instructions to create new video and audio segments for the video with Pika and DeepGram. Loop The edited video goes back to the evaluator agent, so a generator-evaluator multi-agent pattern can be used for video generation improvement. In total, the generator-evaluator loop is run 5 times. Visualize Retention. After the final video is created, an interactive 3D brain is rendered to demonstrate the neural activation in both the original video and the final generated video. Tech stack Meta TRIBE v2 (brain model) hosted on Lightning AI. We use TRIBE v2, Meta's open source model, to predict the brain's fMRI response to multimodal input in our evaluator. We host it on an A100 GPU through Lightning AI. We expose a callable endpoint on Lightning, which takes in an MP4 video and returns predicted fMRI brain responses. Pika. We use Pika to generate the video clips, sound effects, and ambiance from the feedback created by our evaluator and the user's instructions. Our pipeline iteratively uses TRIBE to evaluate Pika's output, maximizing user retention. Deepgram. We leveraged both. the speech-to-text and text-to-speech capabilities of Deepgram. Speech-to-text allows the user to voice any concerns about the educational video before the pipeline is run. Within the pipeline, Deepgram provides the audio for each video created by the generator agent. This audio is evaluated by TRIBE alongside the video to gauge efficacy. TokenRouter We use TokenRouter to call three different LLMs to act as a panel of judges: Claude, Gemini, and GPT. Each LLM takes a video's TRIBEv2 engagement signal, and the previously generated video, outputting specific directives for video edits based on the signal. We then summarize the outputs from all three LLMs using TokenRouter to call Claude. Band We use Band to visualize the interactions between our evaluator and generator agents. We added the agents to a Band chat session where they show their outputs, allowing us to evaluate agent performance and optimize prompts. Challenges we ran into Running TRIBE v2 TRIBE needs a GPU and downloads several large foundation models. None of the sponsors offered free compute, so we found lightning AI to run the model and expose an endpoint we could hit from our local devices. Latency. The agent iteration loop and the calls to TRIBE both take significant time (~20 minutes for a full loop), making it difficult to demo our product live. What we learned Research-grade tooling is becoming more accessible Brain-encoding foundation models like TRIBE can stand in for parts of an fMRI study, enabling anyone with a laptop to run tests. GANs don't need gradients to be useful. Treating a frozen model as a discriminator and running a selection loop around it is a surprisingly powerful pattern. What's next for Retention Per-viewer specialization. TRIBE predicts an average brain. We want to condition on specific user profiles instead of optimizing for a generic one. Validate against real humans. Close the loop on reality by A/B testing optimized vs. original videos against actual engagement and recall. <div