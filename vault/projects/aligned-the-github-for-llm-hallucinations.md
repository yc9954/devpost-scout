---
slug: "aligned-the-github-for-llm-hallucinations"
url: "https://devpost.com/software/aligned-the-github-for-llm-hallucinations"
title: "ALIGNED: The Github for LLM Hallucinations"
hackathon: "UC Berkeley AI Hackathon"
organization: "Cal Hacks"
winner: true
words: 451
team_size: 3
has_repo: true
has_live: true
has_video: false
tags:
  - "project"
  - "mechanism/vision_ocr"
  - "domain/developer_tools"
  - "domain/education"
  - "user/developer"
  - "user/educator_student"
  - "substrate/code_repository"
---

# ALIGNED: The Github for LLM Hallucinations

> The GitHub for Hallucinations. Democratic, transparent LLM development is a must. ALIGNED is a GitHub-like platform to report model issues, and then use AI to help OpenAI & others fix them with RLHF.

[Devpost](https://devpost.com/software/aligned-the-github-for-llm-hallucinations) · hackathon [[UC Berkeley AI Hackathon]]

## Facets

**mechanism** [[vision_ocr]]
**domain** [[developer_tools]] [[education]]
**user** [[developer]] [[educator_student]]
**substrate** [[code_repository]]

**stack** argocd, argoworkflow, azure, coder, falcon-40b, huggingface, kubernetes, nextjs, nvidia, openai, prisma, ray, shadcn, terraform

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for aligned: the github for llm hallucinations

## Body

"Repositories" for GPT-4, Llama, and more. Issues Reported for Llama-7B. Submit your own issue, or contribute to others! This is no GPT-4 wrapper. ALIGNED is the future of LLM transparency -- a new ecosystem for aligning AI. Inspiration OpenAI just released their $1M grant program for building democratic AI. Language models have the power to control our world's discourse. We need to ensure they are properly monitored and maintained for bias, hallucinations, and more. What it does Just like any coder today can find open source code, contribute, and report issues with a repository, any person in the world can report hallucinations and bias they've observed, contributing to the platform. We are more than a platform: we then use this data, use GPT-4 to generate more human preference data for model developers, and then use TRLX to run Reinforcement Learning with Human Feedback to align the model and fix the issue. Not only do we host the community discourse on model behaviors, but we also provide actionable insights and data for OpenAI, Anthropic, and open source developers to then re-align their models. How we built it Our backend uses 2x NVIDIA A100 GPUs, Ray + HuggingFace for Reward Model Training, CarperAI's trlX (the RL PPO library), and OpenAI's GPT-4. Our frontend uses React, Vercel, and a custom-built API. Training the Falcon-40B RLHF-instructed model took several hours. Challenges we ran into Training the Reward Model, and then using that Model for PPO was difficult. Ray and trlX were helpful for informing better practices for more efficient training. This was also a highly ambitious project. Accomplishments that we're proud of Not only have we built an entire working community for collecting RLHF data (like ScaleAI but open-sourced), but we then RLHF-fine tuned an entire Falcon-40B with 8bit quantization ... in 36 hours! We have also fully deployed our platform in CI, including our entire data, model training and fine-tuning pipelines using ArgoWorkflow and Kubernetes, provisioned by Terraform. What we learned NVIDIA A100s reign supreme. On a more serious note, there are many issues with our current language models. As an example, just ask GPT "In the sentence "The professor married the graduate student because she was pregnant", who was pregnant?" and you'll see flagrant problems. We'd like to partner with OpenAI, Anthropic, and more to help them align their models away from such behaviors. What's next for ALIGNED: The Github for LLM Hallucinations Join our platform and contribute to the discussion! https://calhacks23.vercel.app/ We'll be rolling out more community features to foster dialogue and discussion over raised issues. We believe this is very valuable data for private model developers like OpenAI, Anthropic, and Cohere to help RLHF their models. Reach out at: aligned.vercel.app. <div