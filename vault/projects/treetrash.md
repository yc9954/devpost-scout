---
slug: "treetrash"
url: "https://devpost.com/software/treetrash"
title: "TreeTrash"
hackathon: "TreeHacks 2025"
organization: "TreeHacks"
winner: true
words: 580
team_size: 4
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "mechanism/retrieval_grounding"
  - "mechanism/vision_ocr"
  - "domain/agriculture_food"
  - "domain/climate_energy"
  - "substrate/structured_db"
  - "substrate/video_visual"
---

# TreeTrash

> Quantify, analyze, and improve sustainability with intelligent trash monitoring!

[Devpost](https://devpost.com/software/treetrash) · hackathon [[TreeHacks 2025]]

## Facets

**mechanism** [[realtime_stream]] [[retrieval_grounding]] [[vision_ocr]]
**domain** [[agriculture_food]] [[climate_energy]]
**substrate** [[structured_db]] [[video_visual]]

**stack** adafruit, gemini, openai, perplexity, vercel, vespa

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for treetrash

## Body

Demo Inspiration During TreeHacks, we noticed a significant number of items being placed in the wrong waste bins, which reminded us of a broader problem with tracking and understanding waste patterns, so that they could be effectively mitigated in the future. This sparked our idea to expand upon challenge #3 on the sustainability track and leverage AI to not only identify and address this issue but also take it a step further. We wanted to go beyond simply classifying waste and analyzing the weight — we aimed to develop a program that could analyze images of trash, recycling and compost and generate a report that could provide organizations like Stanford with valuable insights into food waste patterns, enabling them to implement more effective sustainability initiatives and reduce unnecessary waste. What It Does TreeTrash leverages computer vision to analyze images of a trash bin taken at regular intervals. We determine which items were misplaced and what the environmental impact of misplacing those items using a custom search pipeline. When we first notice a misplaced item, we use a display and speaker to notify the person. Then, we generate a custom report about the environmental impact of misplacing certain items, as well as specific recommendations about how to improve. How We Built It We use computer vision to list out the items in the image, compare those items to the items in the previous image, use OpenAI's GPT-4o to determine the proper placement of those items, use Perplexity search to identify the environmental impact in terms of kg of CO2e emissions, use gpt-4o-mini to parse this output into a structured output, use Vespa AI RAG to identify how this relates to the sustainability goals of a specific organization, and use Gemini to generate a report. Challenges We Ran Into Implementing RAG with Vespa was a very buggy process and it took a lot of learning about the platform. Also, Perplexity was not able to consistently output a structured output, so we had to add in a layer in the pipeline to transform it into a structured output. Accomplishments That We're Proud Of We're proud of how we improved the accuracy of predictions using grounded information retrieved by perplexity. We are also proud of how we implemented RAG to augment the report by making it specific to an organization's sustainability goals. Being able to leverage our teammates' EE skills to develop a custom monitor to display everything was also important! What We Learned We learned how to construct pipelines that incorporate multiple AI models and implement RAG with new tools (namely Vespa.ai), which we had never had exposure to before. What's Next For TreeTrash We plan to take TreeTrash beyond the hackathon by testing it with real trash bins at Stanford. Our next steps focus on key technical improvements to enhance the system’s accuracy and functionality: Enhancing Retrieval-Augmented Generation (RAG): We have already implemented a RAG system to provide real-time, context-aware explanations about waste sorting. Next, we aim to improve its retrieval accuracy and response relevance by exploring different embedding models and expanding our dataset. Advancing Computer Vision for Waste Classification: We will refine our AI model using a more diverse dataset of waste images, improving its ability to classify items and estimate food waste weight with greater precision. Integrating a Robotic Arm for Automated Sorting: As a long-term goal, we envision incorporating a robotic arm that can physically sort waste based on AI predictions, reducing human error and streamlining waste management. <div