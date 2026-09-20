---
slug: "codeforge-pages"
url: "https://devpost.com/software/codeforge-pages"
title: "CodeForge Pages"
hackathon: "TreeHacks 2025"
organization: "TreeHacks"
winner: true
words: 589
team_size: 4
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/retrieval_grounding"
  - "mechanism/simulation_digital_twin"
  - "user/general_public"
  - "substrate/structured_db"
  - "substrate/video_visual"
  - "substrate/web_dom"
---

# CodeForge Pages

> Aesthetic React Landing Pages in Minutes – AI, Code Preview / Export, OAuth, Databases

[Devpost](https://devpost.com/software/codeforge-pages) · hackathon [[TreeHacks 2025]]

## Facets

**mechanism** [[retrieval_grounding]] [[simulation_digital_twin]]
**user** [[general_public]]
**substrate** [[structured_db]] [[video_visual]] [[web_dom]]

**stack** beautiful-soup, elasticsearch, fastapi, firebase, next.js, python, react, supabase

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for codeforge pages

## Body

Inspiration We love to build, but design is hard. To make something visually appealing, it requires a lot of experimentation and research into what needs to be added. Landing pages are often the first thing a customer sees about a business. We thought current AI tools fall short of our needs. They were either too rigid, didn't integrate well into our workflow of Next.JS, or didn't have enough complexity. So, we thought, why not automate it? What it does CodeForge Pages asks users to enter information about their company along with the name of the company. Based on this information, CodeForge generates a multi–component landing page in React that contains beautiful layout, text, and style. Users can view the rendered code in either the web-view or a simulated mobile view. When pleased with the website, they can export it–which will download a zip of all the react components. All users are also authenticated – meaning when you create a project, we associate it with your profile and it can be accessed at any time through the dashboard. How we built it CodeForge Pages is built in Next.JS. The AI pipeline is quite intricate. We first recorded the data of existing landing pages and then extracted images of every single component of that page (header, hero, feature, etc). Every landing page was then added to an Elasticsearch serverless vector database with a corresponding description generated automatically. Now, when the user prompts the app, it finds the most similar company and generates components through a section-by-section workflow. This backend operation is all coded in Python and utilizes FastAPI. To render the generated component, we use Sandpack from CodeSandbox. In order to authenticate each user, we use Supabase – allowing GitHub, Google, and verified email log-in. To save the data about each project for every user, we use Firebase. Specifically, every component is stored as a String and is rendered every time the user opens the project. Challenges we ran into It was quite difficult to render the generated React components on the screen. At first, we created an implementation using Babel. This nearly took 5 hours and was quite complicated as there were many issues with UI libraries we were using such as Tailwind. Later, we experimented with some other features and asked those at the booths for help. After some more research, we found CodeSandbox. Additionally, the model was glitching – generating white text on white background or dark text on dark backgrounds. To fix this, we utilized Tailwind to ensure the model was accurately placing classes on elements. Additionally, we improved the prompting through iteration. Accomplishments that we're proud of The app generates beautiful and aesthetic components as shown in the images. These designs can be implemented at a real business with a great level of acceptance. Additionally, the code also displays code and an accurate preview. Preview at first seemed difficult to generate accurately, but now it is quite accurate and rarely errors. What we learned We gained many insights about UI / UX automation through AI and what it takes to generate such components. Additionally, we learned more about how code rendering really works in React projects. In the future, we should check if there are any libraries to simplify our tasks. What's next for CodeForge Pages We plan to add more features to the app and ship it to the public. Some of the features we plan to add are chat to add features, an interactive no-code editor, on-demand hosting, and image generation / implementation. <div