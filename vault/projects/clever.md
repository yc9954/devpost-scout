---
slug: "clever"
url: "https://devpost.com/software/clever"
title: "Clever"
hackathon: "TiDB Future App Hackathon 2024"
organization: "PingCAP"
winner: true
words: 710
team_size: 0
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/retrieval_grounding"
  - "mechanism/voice_speech"
  - "domain/education"
  - "user/educator_student"
  - "substrate/document_pdf"
  - "substrate/structured_db"
  - "substrate/video_visual"
---

# Clever

> Clever makes studying easy by turning documents into flashcards, answering questions, and finding quiz answers—powered by AI and TiDB Serverless for seamless learning.

[Devpost](https://devpost.com/software/clever) · hackathon [[TiDB Future App Hackathon 2024]]

## Facets

**mechanism** [[retrieval_grounding]] [[voice_speech]]
**domain** [[education]]
**user** [[educator_student]]
**substrate** [[document_pdf]] [[structured_db]] [[video_visual]]
  <sub>weak: financial_record</sub>

**stack** argocd, fastapi, kubernetes, llama-index, minio, mongodb, openai, postgresql, raspberry-pi, swift, tidb

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for clever

## Body

Problem Statement Clever App Features Key Feature Key Feature Key Feature Key Feature ArgoCD - Continuous Delivery Tool Trulens Evaluation Architecture Tech Stack Thank you! Inspiration The modern education landscape is full of challenges—complex course materials, inefficient study methods, and overwhelming test preparation. We realized that students and lifelong learners need a tool that simplifies these processes, making learning more accessible, efficient, and engaging. The inspiration for Clever came from our own struggles and those of countless others who have faced the stress of mastering difficult content. We aimed to create a solution that leverages cutting-edge AI and vector databases to make learning not just easier but more intuitive and effective. What it does Clever is an AI-powered educational tool designed to simplify and enhance the learning experience. It allows users to upload documents, images, or quizzes and instantly break down complex content into manageable pieces. Key features include: Flashcard Generation : Automatically create flashcards from your notes or course materials with a single tap. Question & Answer System : Ask questions directly to your uploaded content, and Clever will provide accurate answers based on the material. Text-to-Speech : Convert your notes or any text content into audio, allowing you to listen to your study materials on the go. Quiz Assistance : Upload a picture of your quiz, and Clever will analyze it and provide the correct answers based on the content you’ve uploaded. How we built it Clever was built using a blend of advanced AI and robust backend technologies. The core of the application leverages: TiDB Serverless with Vector Search : Used to store and efficiently retrieve vectorized representations of user-uploaded content, enabling powerful and accurate question-answering capabilities. OpenAI models : For content understanding and text generation, enabling the creation of flashcards and answering complex questions. Raspberry Pi Cluster : Hosting the Clever API and managing the backend processes, ensuring scalability and resilience. MongoDB and PostgreSQL : These databases are used to manage general data and specific records related to our TrueLens monitoring tool, respectively. Minio : For storing and retrieving user-uploaded PDFs, images, and other artifacts. Helm, YAML Index, and Docker : These were utilized for containerization and orchestration, ensuring the application is scalable and easy to deploy. Challenges we ran into Developing Clever came with its own set of challenges. One of the significant hurdles was optimizing the context relevance of the answers provided by the vector database. This required fine-tuning sentence-splitting techniques and adjusting the model’s training parameters to ensure the content's accuracy and relevance. Another challenge was integrating the various components—like TiDB Serverless, OpenAI models, and the Raspberry Pi cluster—into a cohesive, scalable solution without compromising on performance or user experience. Accomplishments that we're proud of We are incredibly proud of the seamless integration of TiDB Serverless and Vector Search, which has allowed us to create a highly responsive and intelligent learning tool. The fact that Clever can turn any document or image into an interactive study session is a testament to the power of the technologies we used. Additionally, deploying the backend on a Raspberry Pi cluster was an innovative step that demonstrates the flexibility and resilience of our application. Finally, the user-friendly design that blends advanced AI with an intuitive interface is something we’re very proud of. What we learned Throughout this project, we learned the immense value of leveraging advanced AI models in conjunction with vector databases like TiDB. The experience highlighted the importance of context relevance in AI-driven educational tools, and how crucial it is to ensure that the answers generated are not only correct but also contextually appropriate. We also gained insights into the challenges of deploying AI-driven applications on limited hardware resources, and how to overcome them with effective containerization and orchestration strategies. What's next for Clever Moving forward, we plan to expand Clever's capabilities by integrating more advanced multimodal search features and enhancing the personalization of the learning experience. We also aim to explore deeper integrations with learning management systems (LMS) and educational platforms, making Clever a comprehensive tool for both students and educators. Additionally, we will continue to refine our vector search algorithms to improve the accuracy and relevance of the answers provided, and explore scaling the backend infrastructure to handle a larger user base. <div