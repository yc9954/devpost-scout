---
slug: "speak-to-learn-japanese"
url: "https://devpost.com/software/speak-to-learn-japanese"
title: "Speak to Learn Japanese"
hackathon: "HackAI - Dell and NVIDIA Challenge"
organization: "Dell"
winner: true
words: 439
team_size: 1
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/retrieval_grounding"
  - "mechanism/voice_speech"
  - "domain/accessibility"
  - "domain/developer_tools"
  - "domain/education"
  - "user/developer"
  - "user/educator_student"
  - "substrate/transcript_audio"
---

# Speak to Learn Japanese

> You learn by saying the Japanese words

[Devpost](https://devpost.com/software/speak-to-learn-japanese) · hackathon [[HackAI - Dell and NVIDIA Challenge]]

## Facets

**mechanism** [[retrieval_grounding]] [[voice_speech]]
**domain** [[accessibility]] [[developer_tools]] [[education]]
**user** [[developer]] [[educator_student]]
**substrate** [[transcript_audio]]

**stack** ffmpeg, flask, huggingface, whisper

## How they structured the write-up

- inspiration
- what it does
- how i built it
- challenges i ran into
- accomplishments that we're proud of
- what i learned
- what's next for speak to learn japanese
- considerations

## Body

Inspiration I'm taking Japanese lessons with a teacher and I need to practice speaking so I built this app to be used in my studies. I also had to consider what I could do handle with my Geforce RTX 3060 and and my 7th Generation Intel® Core™ i5 Processor. I know my machine struggles with small LLMs, so I had to leave it LLM and RAG but I wrote what I could do with it in my Coding Challenges section. What it does You have a collection of Japanese words, you record, and the app returns back the transcription so you can see how close you got. How I built it Whisper + Hugging Face, I fully documented the details in Github Markdown file. I also recorded the 75% of the process. I always record everything. I thought I wasn't going to finish so I stopped recording at that 75% mark. Challenges I ran into Ports configurations Limitations of JupterLabs editing files and poor terminal controls Confusion of the architecture of JupterLabs projects Lack of existing examples or too complex examples to reference from when building from the Nvidia AI Workbench example projects Specific issues with flask vague errors, and figuring out the best way to log and debug app-to-app communication, This one was the hardest. updating CUDA and installing WSL2 Accomplishments that we're proud of The app works! What I learned CUDA configuration, I didn't know about how CUDA versions the featuresets avaliable for workloads CUDA monitoring, so now I know how to monitor usage via the nvidia-smi command Some Japanese words! I'm getting better everyday. I did explore NIM and NeMo offerings but since I have limited hardware I decided against an enterprise workload. I did explore the NGC Catalog but I did not see any ASR models I was familiar with for my use case, and was uncertain of my machine capabilities to experiment with available catalog models. What's next for Speak to Learn Japanese I made a bunch of challenge in the Github Doc so if people wanted to know what would be next to add to the project they can read that list. I will probably developer it further for personal use. I am likely to repurpose the code for my upcoming Free Community GenAI Bootcamp in January. I say repurpose because I don't think I could stream and use Nvidia AI Workbench at the same time due to my previous generation hardware. Considerations I am dyslexic, and I entered this hackathon late so I did not have time to do 2-3 passes to correct any documentation. I may fix in the future. <div