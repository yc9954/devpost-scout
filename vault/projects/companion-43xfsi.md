---
slug: "companion-43xfsi"
url: "https://devpost.com/software/companion-43xfsi"
title: "Companion"
hackathon: "Cal Hacks 11.0"
organization: "Cal Hacks"
winner: true
words: 588
team_size: 3
has_repo: false
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "mechanism/voice_speech"
  - "domain/accessibility"
  - "domain/elder_child_care"
  - "user/general_public"
  - "substrate/structured_db"
  - "substrate/video_visual"
  - "substrate/web_dom"
---

# Companion

> Companion is a voice-powered web AI agent that can autonomously execute web tasks based on user requests, made for seniors/people with disabilities who are unfamiliar with technology.

[Devpost](https://devpost.com/software/companion-43xfsi) · hackathon [[Cal Hacks 11.0]]

## Facets

**mechanism** [[realtime_stream]] [[voice_speech]]
  <sub>weak: cross_origin_web</sub>
**domain** [[accessibility]] [[elder_child_care]]
**user** [[general_public]]
**substrate** [[structured_db]] [[video_visual]] [[web_dom]]

**stack** flask, gpt, openai, opencv, pinecone, python, react, selenium, vapi

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for companion

## Body

main page where user can enter in requests manually or speak to the user user can view all their past automations demonstrating interactive view where user can look at each step the agent took Inspiration A study recently done in the UK learned that 69% of people above the age of 65 lack the IT skills needed to use the internet. Our world's largest resource for information, communication, and so much more is shut off to such a large population. We realized that we can leverage artificial intelligence to simplify completing online tasks for senior citizens or people with disabilities. Thus, we decided to build a voice-powered web agent that can execute user requests (such as booking a flight or ordering an iPad). What it does The first part of Companion is a conversation between the user and a voice AI agent in which the agent understands the user's request and asks follow up questions for specific details. After this call, the web agent generates a plan of attack and executes the task by navigating the to the appropriate website and typing in relevant search details/clicking buttons. While the agent is navigating the web, we stream the agent's actions to the user in real time, allowing the user to monitor how it is browsing/using the web. In addition, each user request is stored in a Pinecone database, to the agent has context about similar past user requests/preferences. The user can also see the live state of the web agent navigation on the app. How we built it We developed Companion using a combination of modern web technologies and tools to create an accessible and user-friendly experience: For the frontend, we used React, providing a responsive and interactive user interface. We utilized components for input fields, buttons, and real-time feedback to enhance usability as well as integrated VAPI, a voice recognition API, to enable voice commands, making it easier for users with accessibility needs. For the Backend we used Flask to handle API requests and manage the server-side logic. For web automation tasks we leveraged Selenium, allowing the agent to navigate websites and perform actions like filling forms and clicking buttons. We stored user interactions in a Pinecone database to maintain context and improve future interactions by learning user preferences over time, and the user can also view past flows. We hosted the application on a local server during development, with plans for cloud deployment to ensure scalability and accessibility. Thus, Companion can effectively assist users in navigating the web, particularly benefiting seniors and individuals with disabilities. Challenges we ran into We ran into difficulties getting the agent to accurately complete each task. Getting it to take the right steps and always execute the task efficiently was a hard but fun problem. It was also challenging to prompt the voice agent such to effectively communicate with the user and understand their request. Accomplishments that we're proud of Building a complete, end-to-end agentic flow that is able to navigate the web in real time. We think that this project is socially impactful and can make a difference for those with accessibility needs. What we learned The small things that can make or break an AI agent such as the way we display memory, how we ask it to reflect, and what supplemental info we give it (images, annotations, etc.) What's next for Companion Making it work without CSS selectors; training a model to highlight all the places the computer can click because certain buttons can be unreachable for Companion. <div