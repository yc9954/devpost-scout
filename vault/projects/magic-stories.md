---
slug: "magic-stories"
url: "https://devpost.com/software/magic-stories"
title: "Magic Stories"
hackathon: "Codegeist Unleashed"
organization: "Atlassian"
winner: true
words: 791
team_size: 2
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "domain/developer_tools"
  - "user/developer"
---

# Magic Stories

> Supercharge development with Magic Stories: AI created user stories from Jira, includes Figma integration, boosting productivity and teamwork

[Devpost](https://devpost.com/software/magic-stories) · hackathon [[Codegeist Unleashed]]

## Facets

  <sub>weak: voice_speech</sub>
**domain** [[developer_tools]]
**user** [[developer]]
  <sub>weak: transcript_audio, video_visual</sub>

**stack** atlassian, cli/api, figma, forge, git, https://www.ai21.com/, node.js, vscode

## Body

Supercharge your software development process with Magic Stories Launch the app from your created 'issue' After generating prompt, review and add to description! You can edit your user story and acceptance criteria in your description. Lead Software Engineer - I make the stuff Jobless Product Designer - I work and design within constraints. The ‘Magic Stories’ Story Check out the story that we submitted to win: Read it on LinkedIn Being at startups, speed in development is an important factor. And there can be hurdles to that software development process. AI can help us expedite the work. Loom does it with AI detecting noise, speech gaps in our videos, creating automated transcription and even automatic titles. Notion does it with their AI assisting in creating outlines. ChatGPT does it with help creating social media posts, outline and more. Possibilities are endless. With Jira and Confluence - the possibilities are endless. With the amount of time we had, we started with Jira and the focus on one pain point we’ve experienced working in the software development process. The Problem One of the challenges we face in the software development process is creating user stories. This can be a daunting experience for product managers, software developers, QA, and designers who are all involved in writing or even updating user stories. This requires time to be written and in highly regulated industries like finance, real estate and healthcare, this process takes a substantial amount of time per week. There are a lot of individuals involved. A fleshed out user story helps the process ship out faster. The Challenges Some of the challenges and constraints we faced in the development of this project: Development Factors - Limited amount of time. We started on October 21, 2023. API are free but with limitations. Cost of API calls over a limit concerns Limited Forge capabilities Design Factors Design constraints User experience concerns We know that an ideal AI experience that is native to Atlassian would work better if we wanted to leverage a lot of the design components. The Process After going back and forth on what to build we narrowed on one thing we’d love to solve. We chose to use Jira and how to leverage AI to create user stories from the “title” or summary of an issue. And we wanted an ability to also add a Figma Preview if there was an attachment. In our development process, we attach a lot of images and write stories around that all the time. Having our problem focused and we completed requirement gathering, it was time to create a solution for it. We debated between doing a modal or showing it inline. Because of the time constraint, we decided that having it inline down below made more sense. The Solution After a ticket is created, there is usually a title or summary already created. To generate a user story, a user, can click on ‘Magic Stories’ and launch the app by generating a prompt from the description as seen. Once it’s added, you can simply refresh and see the page. Learnings This took many quick wireframe iterations. We haven't user tested it. If we had more time we would have done this. Built With To kickstart our project, we leveraged Figjam for initial brainstorming. Subsequently, we transitioned to Figma to gain a comprehensive understanding of the user experience. For the foundation of our app, we sought the following essentials: An integrated development environment (IDE): We opted for VS Code. To collaborate effectively with the Atlassian Forge CLI, we required the following tools: Docker Desktop Node Git GitHub Virtual Machine (VM) enabled. As we commenced app development, we identified the following critical dependencies and elucidated their significance: @forge/api fetch: Vital for making API calls to Figma and Ai21. storage: Necessary for securely storing API keys, should users choose to do so. @forge/ui The cornerstone of our app's user interface, encompassing everything from buttons to modals. In terms of our API interactions: The core functionality of our app relies on Ai21. We simply send a prompt text to their API, and in response, receive AI-generated text precisely tailored to our request. An intriguing feature involves interfacing with Figma. If a user incorporates a Figma link in their prompt, our custom listener seamlessly processes it through Figma's API, creating a dedicated section for it. What’s next for Magic Stories Improved user experience in Jira Ability to do more than user stories and incorporate into Confluence leveraging ChatGPT. About Jenearly is a Software Developer Lead at Mint Mobile and Yenith is a Senior Product Designer that was recently laid off from Medable’s 3rd round of layoffs. We are sisters that both come from a non-traditional background to be in tech. <div