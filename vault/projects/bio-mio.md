---
slug: "bio-mio"
url: "https://devpost.com/software/bio-mio"
title: "Bio Mio"
hackathon: "Nosu AI Hackathon $11,300+ in prizes"
organization: "nosu"
winner: true
words: 831
team_size: 1
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/voice_speech"
  - "user/legal_professional"
  - "substrate/structured_db"
  - "substrate/video_visual"
---

# Bio Mio

> Bio Mio is a biomimicry app that helps you relax and de-stress using landscape photos.

[Devpost](https://devpost.com/software/bio-mio) · hackathon [[Nosu AI Hackathon -11-300- in prizes]]

## Facets

**mechanism** [[voice_speech]]
**user** [[legal_professional]]
**substrate** [[structured_db]] [[video_visual]]

**stack** dall-e, gradio, mistral-nemo, nebius-ai-studio, pillow, prompt-engineering, python3.12, qwen-vision, tenacity

## How they structured the write-up

- inspiration
- what it does
- how i built it
- challenges i ran into
- accomplishments that i'm proud of
- what i learned
- what's next for bio mio

## Body

Bio Mio - generates abstract artwork inspired by your landscape photo Bio Mio - generates a calming passage based on your landscape photo Bio Mio - creates a collage of your landscape photo and the generated artwork Each generated abstract artwork is unique Another Bio Mio collage Yet another Bio Mio collage Bio Mio Home Bio Mio sample landscape selection Inspiration Bio Mio is a biomimicry app that helps you relax and de-stress using landscape photos. It was inspired by the calmness I felt when I travelled to Switzerland and gazed at the landscapes of mountains and lakes in summertime. What it does You can upload a landscape photo of your own to Bio Mio or select one from the 100 included sample photos. Bio Mio will analyze the photo and generate an abstract artwork based on the features of the landscape. It will also generate a calming passage about the landscape and read it aloud to you. By listening to the passage and gazing at the artwork, the goal is for you to experience a relaxing, calming moment inspired by features and patterns from nature. To save your experience, you can create a collage of the landscape photo and the abstract artwork to download, or simply download the artwork. You can also copy and paste the calming passage which was generated for example into a daily relaxation reminder, attaching the collage. Each time you select a landscape, a unique abstract artwork will be generated for you, even with the same photo. If you upload a photo which is not a landscape, Bio Mio will silently ignore it. If you don't want the generated passage to be read aloud to you, simply select the mute checkbox before selecting a landscape. How I built it I used 2 LLMs from Nebius AI Studio : Qwen2 Vision Mistral Nemo I also used the latest LLM for image generation from OpenAI: DALL-E 3 The Flow Qwen2 Vision analyzes the landscape photo to generate a description, focusing on the calming and serene aspects. The landscape description is then used by DALL-E 3 to generate an abstract artwork, focusing on calmness and tranquility. The description is also used by Mistral Nemo to generate a calming, relaxing passage for reading aloud. A collage of the landscape photo and abstract artwork is optionally created at the user's request. Challenges I ran into I chose the LLMs based on comparing the model cards at studio.nebius.ai to balance cost, performance, and quality. For the Vision LLM I first tried Llava (llava-hf/llava-1.5-7b-hf) but the quality was poor, so I switched to Qwen (Qwen/Qwen2-VL-7B-Instruct) which I found had superior quality at similar speed. For the text LLM I first tried Meta Llama (meta-llama/Meta-Llama-3.1-70B-Instruct) , but I switched to Mistral Nemo (mistralai/Mistral-Nemo-Instruct-2407) for lower cost and faster speed, with quality not a major concern for the use case of summarization. Switching between LLMs on Nebius was simple because all models support the OpenAI Python library for access and use. I only had to change environment variables when switching to a different LLM. For the image generation LLM I chose DALL-E (dall-e-3) for its established quality and the ability to use the OpenAI library with it, with no need to add another dependency. I had challenges with engineering the prompts sent to these 3 LLMs to get the results I wanted. After tweaking the prompts many times, I finally achieved success for all the LLMs I chose. I also had a challenge getting the text-to-speech feature of reading the calming passage to work smoothly in multiple browsers, especially and surprisingly Chrome. You can judge if I succeeded :) Accomplishments that I'm proud of I'm proud that I could build a relaxation app inspired by biomimicry to recreate the calm I felt years ago when I was travelling in Switzerland and experiencing its beautiful mountains and lakes reflecting summertime landscapes. What I learned I learned that Nebius AI Studio is a cost-effective and easy way to integrate a wide variety of leading open source AI models in an AI project like Bio Mio . What's next for Bio Mio For the sample landscape photos, I used this dataset from Kaggle , taking the first 100 images. For v2 of Bio Mio I want to add other public domain image sets to give the user more variety in choosing landscapes to enjoy and generate calming artwork from. There will be an image preview feature added as well to give you an idea of what to expect. For v2 I also want to allow the user to choose the voice the app uses to read aloud the generated calming passage. Also since Dylan the GTM Lead for Nebius AI Studio said that image gen LLMs would be added soon, I want to switch to a Nebius-hosted LLM in v2 to generate the calming artwork and reduce my costs (and thus stress :). The tease looks cool: https://x.com/nebiusaistudio/status/1876305827658858774 Proof I registered on nosu.io: https://take.ms/8wAhb Discord handle: wcheung <div