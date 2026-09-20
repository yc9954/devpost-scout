---
slug: "memory-playground"
url: "https://devpost.com/software/memory-playground"
title: "Memory Playground"
hackathon: "TreeHacks 2024"
organization: "TreeHacks"
winner: true
words: 660
team_size: 4
has_repo: false
has_live: false
has_video: false
tags:
  - "project"
  - "mechanism/structural_withholding"
  - "mechanism/voice_speech"
  - "domain/elder_child_care"
  - "domain/finance_payments"
  - "domain/health_clinical"
  - "user/general_public"
  - "user/patient_family"
  - "substrate/video_visual"
  - "substrate/web_dom"
---

# Memory Playground

> Build a digital Memory Playground to help boost memory recall and retention.

[Devpost](https://devpost.com/software/memory-playground) · hackathon [[TreeHacks 2024]]

## Facets

**mechanism** [[structural_withholding]] [[voice_speech]]
**domain** [[elder_child_care]] [[finance_payments]] [[health_clinical]]
**user** [[general_public]] [[patient_family]]
**substrate** [[video_visual]] [[web_dom]]

**stack** chatgpt, openai, react, togetherai

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for memory playground

## Body

Inspiration According to the Alzheimer’s Association, 6.7 million Americans age 65 and older are living with Alzheimer's in 2023. Alzheimer’s is a gradually progressive brain disorder involving memory loss. It is the most common form of dementia; people forget who their loved ones are and cannot carry out daily tasks anymore. Alzheimer’s and dementia is not only a personal health crisis but impacts family, friends, and caregivers. It is important to focus on the prevention and slow progression of symptoms related to memory loss. How can we use the Memory Palace – a psychology-based technique where people can associate mnemonic images in their mind to places they know – to help prevent and ease the lives of those with Alzheimer’s and dementia? There is a lot of psychology research focused on memory and learning that can be used to guide technical applications and enhance memory performance. Our team is very interested in memory and learning mechanisms, which have inspired our idea to use scientific background to improve memory. What it does Memory Playground is a web application that helps boost memory recall and retention through the Memory Palace technique, especially for senior citizens and those with Alzheimer’s and dementia. The application allows users to pick a setting/environment and list out words that are related. Then, we create broad yet distinct categories for the words. From here, we have users practice classifying objects, allowing them to create visual mappings of images physically and mentally. This allows them to strengthen memory connections and enhance memory performance. We also give them other words that fall into those categories to expand on the established mental connections. Memory Playground also uses an integration of zero-knowledge proofs. It stores uploaded data securely on servers and allows users to anonymously interact with the application without revealing personally identifiable information, which is ideal for those concerned about privacy. How we built it We used the OpenAI API to prompt their GPT-4 model for category groupings and new objects. Then we used Together.AI's stable diffusion model for image generation. From there we connected the Python components to the web side using Fetch API. We built the web application with React, HTML, CSS, and JS. We used Flask to integrate the Python backend with the frontend. Challenges we ran into 1) Working with multiple servers 2) Integrating Flask with React 3) Learning to use multiple APIs to integrate various services 4) Implementing drag and drop functionality using use states 5) Limited credit and GPU usage 6) Utilizing multimodal machine learning models Accomplishments that we're proud of We are proud of how we efficiently and quickly were able to understand and implement new technologies and concepts. We were new to Flask and a lot of the recent AI technology. We are also proud of how we worked as a team, ideation stages to product creation. Additionally, we are proud of how we were able to integrate multiple varying technologies. What we learned We developed a lot of technical skills involving using APIs, prompt engineering, model optimization, Flask, managing multiple server applications, and web development. We also learned a lot about the practical applications of AI in healthcare towards a potential treatment of Alzheimer's and dementia. It is critical for us as a society to consider how we can prevent , not just treat, such diseases. We also learned a lot about the engineering design process. Throughout the hackathon we went through research, ideation, designing, prototyping, and building phases. We gained a lot of skills through this process that helped us as we adapted to new technologies and grew our knowledge base. What's next for Memory Playground 1) Scaling: We are looking to make our application public and available to the community. This would involve cloud data storage (ex. Firestore) and increased efficiency to manage larger requests. 2) Speech-to-text recognition: We would like to implement a speech to text recognition model so that we can utilize verbal connections and improve accessibility. <div