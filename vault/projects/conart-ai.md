---
slug: "conart-ai"
url: "https://devpost.com/software/conart-ai"
title: "ConArt AI"
hackathon: "Hack the North 2024"
organization: "Hack the North"
winner: true
words: 718
team_size: 4
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "domain/civic_government"
  - "substrate/geospatial"
  - "substrate/video_visual"
  - "substrate/web_dom"
---

# ConArt AI

> gamified design experience that turns doodles to concept art

[Devpost](https://devpost.com/software/conart-ai) · hackathon [[Hack the North 2024]]

## Facets

**mechanism** [[realtime_stream]]
**domain** [[civic_government]]
**substrate** [[geospatial]] [[video_visual]] [[web_dom]]

**stack** controlnet, convex, css, react, replicateapi, tailwind, vercel, vite

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for conart ai

## Body

ConArt AI Drawing Doodles Leaderboard Conceptual Art Generated Inspiration We often found ourselves stuck at the start of the design process, not knowing where to begin or how to turn our ideas into something real. In large organisations these issues are not only inconvenient and costly, but also slow down development. That is why we created ConArt AI to make it easier. It helps teams get their ideas out quickly and turn them into something real without all the confusion. What it does ConArt AI is a gamified design application that helps artists and teams brainstorm ideas faster in the early stages of a project. Teams come together in a shared space where each person has to create a quick sketch and provide a prompt before the timer runs out. The sketches are then turned into images and everyone votes on their team's design where points are given from 1 to 5. This process encourages fast and fun brainstorming while helping teams quickly move from ideas to concepts. It makes collaboration more engaging and helps speed up the creative process. How we built it We built ConArt AI using React for the frontend to create a smooth and responsive interface that allows for real-time collaboration. On the backend, we used Convex to handle game logic and state management, ensuring seamless communication between players during the sketching, voting, and scoring phases. For the image generation, we integrated the Replicate API, which utilises AI models like ControlNet with Stable Diffusion to transform the sketches and prompts into full-fledged concept images. These API calls are managed through Convex actions, allowing for real-time updates and feedback loops. The entire project is hosted on Vercel, which is officially supported by Convex, ensuring fast deployment and scaling. Convex especially enabled us to have a serverless experience which allowed us to not worry about extra infrastructure and focus more on the functions of our app. The combination of these technologies allows ConArt AI to deliver a gamified, collaborative experience. Challenges we ran into We faced several challenges while building ConArt AI. One of the key issues was with routing in production, where we had to troubleshoot differences between development and live environments. We also encountered challenges in managing server vs. client-side actions, particularly ensuring smooth, real-time updates. Additionally, we had some difficulties with responsive design, ensuring the app looked and worked well across different devices and screen sizes. These challenges pushed us to refine our approach and improve the overall performance of the application. Accomplishments that we're proud of We’re incredibly proud of several key accomplishments from this hackathon. Nikhil: Learned how to use a new service like Convex during the hackathon, adapting quickly to integrate it into our project. Ben: Instead of just showcasing a local demo, he managed to finish and fully deploy the project by the end of the hackathon, which is a huge achievement. Shireen: Completed the UI/UX design of a website in under 36 hours for the first time, while also planning our pitch and brand identity, all during her first hackathon. Ryushen: He worked on building React components and the frontend, ensuring the UI/UX looked pretty, while also helping to craft an awesome pitch. Overall, we’re most proud of how well we worked as a team. Every person filled their role and brought the project to completion, and we’re happy to have made new friends along the way! What we learned We learned how to effectively use Convex by studying its documentation, which helped us manage real-time state and game logic for features like live sketching, voting, and scoring. We also learned how to trigger external API calls, like image generation with Replicate, through Convex actions, making the integration of AI seamless. On top of that, we improved our collaboration as a team, dividing tasks efficiently and troubleshooting together, which was key to building ConArt AI successfully. What's next for ConArt AI We plan to incorporate user profiles in order to let users personalise their experience and track their creative contributions over time. We will also be adding a feature to save concept art, allowing teams to store and revisit their designs for future reference or iteration. These updates will enhance collaboration and creativity, making ConArt AI even more valuable for artists and teams working on long-term projects. <div