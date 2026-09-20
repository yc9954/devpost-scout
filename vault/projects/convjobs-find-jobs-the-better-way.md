---
slug: "convjobs-find-jobs-the-better-way"
url: "https://devpost.com/software/convjobs-find-jobs-the-better-way"
title: "ConvJobs - Find Jobs the better way"
hackathon: "Zero to One Hackathon by Convex"
organization: "Convex"
winner: true
words: 589
team_size: 1
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "mechanism/retrieval_grounding"
  - "domain/labor_employment"
  - "user/government_staff"
  - "substrate/document_pdf"
  - "substrate/structured_db"
---

# ConvJobs - Find Jobs the better way

> Where resumes come to life, conversations lead to insights, and hiring becomes an interactive experience.

[Devpost](https://devpost.com/software/convjobs-find-jobs-the-better-way) · hackathon [[Zero to One Hackathon by Convex]]

## Facets

**mechanism** [[realtime_stream]] [[retrieval_grounding]]
  <sub>weak: cross_origin_web</sub>
**domain** [[labor_employment]]
**user** [[government_staff]]
**substrate** [[document_pdf]] [[structured_db]]

**stack** clerk, convex, openai, react, tailwind

## How they structured the write-up

- inspiration:
- overview:
- tech stack:
- how we built it:
- convex in action:
- challenges we ran into:
- what we learned:
- future scope:
- what's next for convjobs:

## Body

Login page Search resume Chat with resume Profile page Resume Insights Chat History Inspiration: In the midst of navigating the complexities of the job market, we recognized a common frustration shared by both job seekers and recruiters. The traditional hiring process often felt convoluted, time-consuming, and inefficient. This inspired us to develop ConvJobs , a solution aimed at bettering the hiring experience for all parties involved. We wanted to create a platform that seamlessly connects job seekers with recruiters while leveraging cutting-edge technology to streamline the entire process. Overview: ConvJobs is an AI-powered platform designed to simplify and enhance the hiring process. At its core lies Convex , a sophisticated system that transforms resumes into embedded vectors for lightning-fast matching and search capabilities. With the integration of OpenAI's GPT-4 and GitHub data, ConvJobs offers an immersive experience, allowing recruiters to engage directly with candidates' resumes and uncover hidden talents through in-depth conversations. For job seekers, ConvJobs offers a seamless experience starting with uploading their resumes which acts as the only source of data. Additionally, candidates can gain valuable insights into their resumes through Mr. Jobs , the AI assistant. Moreover, candidates have the ability to view the chat history of their resumes, allowing them to understand what recruiters are looking for and tailor their applications accordingly. ConvJobs aims to bridge the gap between job seekers and recruiters by providing a platform that not only facilitates connections but also fosters meaningful interactions and insights, ultimately revolutionizing the hiring landscape. Tech Stack: Backend & Database: Convex Frontend: React & Tailwind Authentication - Clerk Object Storage - Convex AI: ChatGPT & Langchain How we built it: We began by conceptualizing ConvJobs with a clear vision of creating a user-friendly and efficient platform. Leveraging Convex for backend operations and React with Tailwind for frontend development, we focused on creating a sleek and intuitive interface. Integrating ChatGPT and Langchain enhanced our chat capabilities, allowing for dynamic conversations between recruiters and candidates. Convex in Action: Convex serves as the backbone of ConvJobs, enabling the transformation of resumes into embedded vectors for seamless matching and search functionalities. Its integration with OpenAI's GPT-4 through Langchain empowers recruiters to engage directly with candidates' resumes, gaining deeper insights and facilitating meaningful conversations. Convex eliminates any sort of websockets by providing updates straight from the database efficiently without loss keeping the users in sync. Challenges we ran into: Integrating chat history for Mr.Jobs our AI bot using ConvexChatMessageHistory in Langchain was challenging Embedding PDfs for vector search was a bit of a tussle What we learned: Throughout the development process, we gained valuable insights into the complexities of the hiring landscape and the importance of leveraging advanced technologies to streamline processes and enhance user experiences. We also learned how efficient Convex is as a backend system with it’s instant updates and easy to use implementation in typescript. Future Scope: Looking ahead, we envision expanding ConvJobs to include features such as resume builders and skill assessments, further enhancing its functionality and value proposition. Additionally, we aim to continuously iterate and improve the platform based on user feedback and emerging technological advancements, ensuring ConvJobs remains at the forefront of hiring technology. What's next for ConvJobs: As we continue to refine and enhance ConvJobs, our focus remains on creating a platform that not only connects job seekers and recruiters but also provides valuable insights, guidance, and opportunities for professional growth. With ConvJobs, we aspire to redefine the hiring landscape, making the process more efficient, innovative, and ultimately, successful for all parties involved. <div