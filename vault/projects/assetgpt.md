---
slug: "assetgpt"
url: "https://devpost.com/software/assetgpt"
title: "Thetune"
hackathon: "Theta Network 2024 Hackathon"
organization: "Theta Labs"
winner: true
words: 398
team_size: 1
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/vision_ocr"
  - "substrate/code_repository"
  - "substrate/structured_db"
---

# Thetune

> Finetune & Deploy LLMs on Theta EdgeCloud Easily!

[Devpost](https://devpost.com/software/assetgpt) · hackathon [[Theta Network 2024 Hackathon]]

## Facets

**mechanism** [[vision_ocr]]
**substrate** [[code_repository]] [[structured_db]]

**stack** docker, framer, gradio, llm, python, thetaedgecloud

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for thetune

## Body

Thetune Tuner Select Dataset Training on Progress Chatbot interface to preview model Deploy to ThetaEdgeCloud Deployed Model, API Ready (OpenAI Specs) Thetune's Architecture Inspiration In today's rapidly evolving tech landscape, large language models (LLMs) hold immense potential to revolutionize various industries. However, fine-tuning and deploying these models often require specialized technical skills, leaving many non-tech users at a disadvantage. The inspiration for Thetune emerged from a desire to democratize access to LLM technology, enabling anyone, regardless of their technical background, to harness the power of AI. By leveraging the capabilities of Theta EdgeCloud, Thetune aims to simplify the process and make LLM fine-tuning and deployment accessible to all. What it does Thetune is a user-friendly application designed to help users fine-tune and deploy LLMs effortlessly. With an intuitive interface, users can: Training using various datasets or using your own dataset (Huggingface datasets public or private) Configure training parameters through simple options Evaluate and Predict the trained model Get Preview by chat trained model Deploy the fine-tuned model and API on Theta EdgeCloud with a single click Thetune eliminates the need for complex coding or deep technical knowledge, providing a seamless experience from start to finish. How we built it The development of Thetune involved several key steps: User Interface Design: Built using Gradio, focused on creating an intuitive and accessible UI, clear visual cues. Landing page using Framer. Backend Development: FastAPI was used to create a robust and efficient backend that handles user requests, data processing, and interactions with the training pipeline. Containerization: Docker was employed to ensure the application is easily deployable and scalable, facilitating smooth integration with Theta EdgeCloud. Model Repository: Huggingface Hub was used to store fine-tuned model Deployment Automation: Automated the deployment process by Theta EdgeCloud and Huggingface API, enabling users to deploy their models on Theta EdgeCloud with minimal effort. Here is the Thetune's Architecture: Challenges we ran into Limited time, and resources to deploy. API integration documentation for Theta EdgeCloud does not exist yet, so to make it work need an alternative way by using x-auth-id and x-auth-token from the request header in Theta EdgeCloud's Dashboard. Accomplishments that we're proud of Completed the project and successfully deployed container to Theta EdgeCloud using API. What we learned Theta EdgeCloud, Finetuning LLM, Gradio What's next for Thetune Dataset Generator by AI, so user can generate their dataset by a single prompt on Thetune <div