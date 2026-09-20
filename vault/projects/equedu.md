---
slug: "equedu"
url: "https://devpost.com/software/equedu"
title: "EquEdu"
hackathon: "Microsoft AI Classroom Hackathon"
organization: "Microsoft"
winner: true
words: 686
team_size: 2
has_repo: true
has_live: true
has_video: false
tags:
  - "project"
  - "mechanism/vision_ocr"
  - "domain/accessibility"
  - "domain/developer_tools"
  - "domain/education"
  - "user/developer"
  - "user/educator_student"
  - "substrate/structured_db"
---

# EquEdu

> Make your training videos accessible for the visually impaired!

[Devpost](https://devpost.com/software/equedu) · hackathon [[Microsoft AI Classroom Hackathon]]

## Facets

**mechanism** [[vision_ocr]]
**domain** [[accessibility]] [[developer_tools]] [[education]]
**user** [[developer]] [[educator_student]]
**substrate** [[structured_db]]

**stack** azure, node.js, react, typescript

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for equedu

## Body

Inspiration Did you know that there are 253 million visually impaired and 360 million hearing impaired people in the world? 66% of people with disabilities think that educational content is not accessible to them. I am Atakan. I'm visually impaired person and a product developer. Since the age of 13, I have been developing software and I try to benefit from a lot of online training content both in my school life and in my software development process. However, since there is no audio description for the visually impaired, I am often faced with sentences like "we will click here, you see it on the screen" and I cannot benefit from the trainings. As someone who frequently uses AI in his daily life, when I realized that the problem I mentioned is not only my problem, but there are millions of people like me around the world, we started to develop EquEdu, which is powered by AI. What it does EquEdu: is a content accessibility tool that allows you to make online educational content accessible for the visually impaired. With EquEdu You can add descriptions for the visually impaired while watching your video content, Can determine whether the descriptions will be added by stopping the video or by superimposing them, At the point where you don't know how to describe it, you can describe it with the AI assistant that reveals its power with Microsoft AI services to describe it faster. You can make your content accessible to 253 million visually impaired people. You can watch how it is done in the demo video with the process of making a speech of Microsoft CEO Satya nadella accessible. How we built it We developed the frontend of the project with React + TypeScript. We preferred to use NodeJS for the backend. We found it appropriate to manage all databases of the project with Microsoft Azure dB services. We use Microsoft Azure TTS services to voice the descriptions of video tutorials. We use the computer vision API in Microsoft Azure Cognative services to facilitate the entire description process for users. ( https://azure.microsoft.com/en-us/products/ai-services/ai-vision ) Challenges we ran into Our first chalenge was to make these descriptions easy for everyone to do. We found that the educators we met with had difficulties in this regard and we have planned a Training section that explains how it can be done and includes examples to facilitate this process. We are waiting for it to be opened in the future. The second was to quickly create accessible versions of the videos. At this stage, we solved this by not waiting for the video to be uploaded, but by allowing the user to select the video and start adding descriptions while the process is loading in the background. In this process, the videos had to be optimized and descriptions had to be added, which we solved with FFMPEG. In order to create the description we wanted to provide in Microsoft Azure Computer vision services, we needed to use several different services together. However, after the last update in July, one of the answers that the service returned to us made the process of adding descriptions very easy. Accomplishments that we're proud of One of the things that made us proud was when the educators we interviewed during this process said "let's use this for the videos we record" when the product was finalized, maybe there are disabled people among our followers. I imagine that a visually impaired person watching video trainings like me would not have the problems I had, and the fact that EquEdu can solve this issue makes us proud. What we learned During this whole process, we learned how to work with video projects technically and learned many devops processes while trying to take the product we developed live. In addition, the customer interviews we conducted in order to use the product in the most efficient way improved our product management skills. What's next for EquEdu In the future Creating subtitles using Microsoft AI services, Improving audio descriptions We are planning a training section on how to make audio descriptions. <div