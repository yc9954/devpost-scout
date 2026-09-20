---
slug: "lecture-noted"
url: "https://devpost.com/software/lecture-noted"
title: "Lecture Noted."
hackathon: "HooHacks 2021"
organization: "HooHacks"
winner: true
words: 434
team_size: 3
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/cross_origin_web"
  - "mechanism/deterministic_policy"
  - "domain/accessibility"
  - "domain/education"
  - "user/educator_student"
  - "substrate/document_pdf"
  - "substrate/transcript_audio"
  - "substrate/web_dom"
---

# Lecture Noted.

> AI-Generated Notes for Online Lectures

[Devpost](https://devpost.com/software/lecture-noted) · hackathon [[HooHacks 2021]]

## Facets

**mechanism** [[cross_origin_web]] [[deterministic_policy]]
**domain** [[accessibility]] [[education]]
**user** [[educator_student]]
**substrate** [[document_pdf]] [[transcript_audio]] [[web_dom]]
  <sub>weak: code_repository</sub>

**stack** css, html, javascript, ml, natural-language-processing, openai, python

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- what we learned
- what's next for lecture noted.

## Body

Landing Page Generated Notes Generated Word Document Try it out for yourself at https://lecturenoted.tech ! Check out the source code here: https://github.com/Pranav-Wadhwa/Lecture-Noted . Inspiration Notes are super helpful for lectures, but oftentimes it is hard to multitask. When a student tries to watch a lecture and take notes at the same time, typically neither process is done effectively. This particularly impacts students with learning disabilities (LD) as we found that 72% of college students with LD reported difficulty in taking adequate notes. What it does Our platform uses OpenAI and machine-learning powered solutions to summarize YouTube videos and uploaded media into concise and enriching bullet points. Lectures are easy and quick to upload and create non-deterministic notes based on the video transcripts. Users can download the bullet points as a Word Document so that they can add their own annotations. We believe that this is extremely applicable to students with learning disabilities, as well as expandable as a tool for meetings, tutorials, and teachers alike. How we built it The frontend is built using HTML, CSS, and JavaScript and is hosted using Firebase hosting. The backend is a Flask Python server that uses GPT-3 AI (OpenAI) to generate the notes. Challenges we ran into We had issues involving exchanging information on the front-end and backend. One problem of interest that we ran into was something called Cross-Origin Resource Sharing being blocked, which led us to do even more research. We also had to experiment with multiple machine learning models and natural learning processing techniques to devise the most effective solution that provides notes within a reasonable time that are also accurate. What we learned We learned about how to develop effective machine learning solutions that integrate natural language processing. Overall, we’re really proud of how the application we developed because it works just as intended! What's next for Lecture Noted. First and foremost, we want to optimize the NLP process to make it faster and more effective. While the notes are of high quality right now, it can take 15-20 seconds to generate the bullet points. We want to speed up this process while ensuring that the quality of the notes is the same, if not better. We also hope to allow more customization, such as different video types and options for the type/length of notes. Most importantly, we want to transform Lecture Noted to an actual platform, where students can not only generate notes but also save them, edit them, and collaborate with other students. We feel like this will enrich the overall learning experience and help students succeed across the world. <div