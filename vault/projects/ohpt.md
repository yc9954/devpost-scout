---
slug: "ohpt"
url: "https://devpost.com/software/ohpt"
title: "OHPT"
hackathon: "UC Berkeley AI Hackathon"
organization: "Cal Hacks"
winner: true
words: 284
team_size: 4
has_repo: false
has_live: false
has_video: false
tags:
  - "project"
  - "mechanism/retrieval_grounding"
  - "domain/education"
  - "domain/supply_logistics"
  - "user/educator_student"
  - "substrate/structured_db"
---

# OHPT

> Empower students with instant answers to questions, saving time for students and teachers. Our advanced support tool, trained on course content and posts, provides reliable assistance for inquiries.

[Devpost](https://devpost.com/software/ohpt) · hackathon [[UC Berkeley AI Hackathon]]

## Facets

**mechanism** [[retrieval_grounding]]
**domain** [[education]] [[supply_logistics]]
**user** [[educator_student]]
**substrate** [[structured_db]]

**stack** featureform, huggingface, jupyter, openai, pinecone, python

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for ohpt

## Body

Inspiration We were inspired by the teacher assistant (TA) strike that occurred at UC Berkeley in Fall 2022. The strike brought to light a major issue in UC Berkeley's education system: departments were being insufficiently funded, leading to less available TAs to help students. This led to long office hour (OH) queues, with many students having their questions unanswered. To address this problem, we decided to work on OHPT! What it does OHPT is a chatbot that answers conceptual and logistical questions for courses. How we built it We built OHPT using a Jupyter Notebook initially as our environment, and leveraged softwares such as OpenAI (chatting), FeatureForm (orchestration), Pinecone (vector database), and HuggingFace (embedding). We also added course content (i.e. course textbook) and logistical posts on EdStem in the form of .csv files to serve as context for the chatbot to use when answering questions. This way, the answers will be personalized to the class and be much more accurate. Challenges we ran into Our main challenges involved balancing a relatively new software with challenging WiFi network capabilities. Accomplishments that we're proud of We are very proud of building a full-stack pipeline using new softwares to inject context to improve upon OpenAIs chatting capabilities. What we learned Primarily, we gained valuable experience in using different softwares and learning how to orchestrate them together to build a functioning and improved assistant. What's next for OHPT Next, we will work on making OHPT include more functions, training it to be able to help students with homework as a tutor rather than giving answers. This will involve making our system more robust to students cheating by adding functions that prevent the chatbot from directly giving answers. <div