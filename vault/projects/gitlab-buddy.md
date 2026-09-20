---
slug: "gitlab-buddy"
url: "https://devpost.com/software/gitlab-buddy"
title: "GitLab Buddy"
hackathon: "GitLab Innovation Pitch Competition"
organization: "GitLab"
winner: true
words: 621
team_size: 3
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "domain/developer_tools"
  - "user/developer"
  - "substrate/code_repository"
  - "substrate/financial_record"
---

# GitLab Buddy

> GitLab Buddy is a low-code/no-code solution with AI helpers that will help you learn how to use GitLab and craft, adjust, and debug awesome pipelines right away.

[Devpost](https://devpost.com/software/gitlab-buddy) · hackathon [[GitLab Innovation Pitch Competition]]

## Facets

**mechanism** [[realtime_stream]]
**domain** [[developer_tools]]
**user** [[developer]]
**substrate** [[code_repository]] [[financial_record]]

**stack** ffmpeg, gpt, lambda, next.js, obs, python, react, tailwind, vercel

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for gitlab buddy
- text description for hackathon requirement

## Body

Inspiration GitLab users, whether veterans or beginners, often encounter challenges while designing, deploying, and debugging their CI/CD pipelines due to GitLab's (sometimes) complex nature and error-prone coding. This issue is time-consuming, decreases productivity, and restricts users from completely leveraging GitLab's capabilities, creating a need for a solution that eases these challenges and accelerates pipeline crafting. What it does GitLab Buddy is a low-code/no-code solution with intelligent AI helpers designed to effectively alleviate these problems. By simply clicking a series of buttons and typing out details into modals, one can quickly configure pipeline elements while the AI helpers continuously fix, adjust, and explain the code in real-time. How we built it Miro for mockups Tailwind for utility classes and as a component framework React/Next.js as the web development framework Python, OpenAI API for GPT/AI integrations AWS Lambda for serverless API Vercel to publish and host the site OBS, ffmpeg for video editing Challenges we ran into CORS error while setting up the API with AWS - turns out after "Enabling CORS" in the AWS console, one must make sure to also "Deploy API" again despite the success notifications that may be displayed that CORS has been enabled on your endpoints... Accomplishments that we're proud of Intuitive and responsive design of our application AI component integrations Being able to realize our vision for the project What we learned How to utilize OpenAI's API after creating a custom AWS Lambda Layer What's next for GitLab Buddy Integrating more features of GitLab Text Description For Hackathon Requirement Problem Statement: GitLab users, whether veterans or beginners, often encounter challenges while designing, deploying, and debugging their CI/CD pipelines due to GitLab's (sometimes) complex nature and error-prone coding. This issue is time-consuming, decreases productivity, and restricts users from completely leveraging GitLab's capabilities, creating a need for a solution that eases these challenges and accelerates pipeline crafting. Our Solution - GitLab Buddy: GitLab Buddy is an innovative, low-code/no-code solution with intelligent AI helpers designed to effectively alleviate these problems. By clicking a series of buttons and typing out in modals, you can quickly select pipeline elements while the AI helpers continuously fix and explain the code in real-time. a) GitLab User Problems: GitLab Buddy takes a multi-faceted approach to solve technical and learning problems of GitLab users. It caters to beginners by offering a simplified learning journey and also aids veterans by offering quick pipeline crafting and debugging features. b) Innovativeness: GitLab Buddy is unique in transforming GitLab usage. Its innovative AI helpers not only fix the code but also adjust and explain it in real-time. It efficiently reduces error occurrence and time consumption, consequently enhancing the overall user experience. c) Quality: With a modern, user-friendly, and responsive design made possible by Tailwind utility classes, GitLab Buddy offers excellent UX. It leverages technologies like React.js and Next.js to deliver a smooth, interactive interface that guides users through their workflows. d) Scalability: GitLab Buddy is a fully serverless solution, built on reputable technologies including Vercel and AWS Lambda. This allows it to scale significantly in terms of user base, revenue, and operations without any loss in performance or quality. It also assures reliable, uninterrupted service with effective uptime. e) Total Addressable Market (TAM): The opportunity for GitLab Buddy is massive. With millions of DevOps engineers worldwide struggling with pipeline designs and numerous beginners aspiring to learn, it has the potential to capture a substantial market. f) Feasibility: GitLab Buddy is a practical solution leveraging readily available technology stack and an extremely cost-effective AI API. It enhances the learning curve, reduces time-to-market, and simplifies the GitLab ecosystem navigation. GitLab Buddy removes barriers to technical learning and debugging, making it a very valuable tool in the DevOps field. Repository Link https://gitlab.com/zkpservices1/gitlab-buddy <div