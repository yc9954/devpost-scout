---
slug: "canva-magic-transform"
url: "https://devpost.com/software/canva-magic-transform"
title: "Magic Transform"
hackathon: "Canva AI and Integrations Hackathon"
organization: "Canva"
winner: true
words: 574
team_size: 2
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "domain/developer_tools"
  - "domain/finance_payments"
  - "substrate/code_repository"
  - "substrate/geospatial"
  - "substrate/video_visual"
  - "substrate/web_dom"
---

# Magic Transform

> Unify diverse images into a stylish masterpiece with AI-powered style transfer!

[Devpost](https://devpost.com/software/canva-magic-transform) · hackathon [[Canva AI and Integrations Hackathon]]

## Facets

**domain** [[developer_tools]] [[finance_payments]]
**substrate** [[code_repository]] [[geospatial]] [[video_visual]] [[web_dom]]

**stack** azure, canva, canvasdk, docker, javascript, node.js, openai, react, typescript

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for canva magic transform

## Body

Canva Magic Transform Icon GIF Slow Loading Bar GIF Initial Loading Bar Implementation GIF CORS Error Demo CORS Error psychedelic wood block anime paper-cut pencil sketch photo-realistic stained glass Inspiration Image generators like DALL-E are impressive, but many people struggle with engineering effective image prompts. We wanted to create an app that allows users to easily assemble their own images, even in disparate styles. With our app, users can add elements to a canvas, and AI will generate a prompt from the image to recreate it in a consistent style. This approach shifts from text-to-image generation to a more intuitive image-to-image generation, making image generation with AI more accessible. What it does Using the Canva SDK requestExport method , we export the current canvas and pass it to OpenAI's GPT Omni model to retrieve a description of the exported image. We then pass the generated description from GPT Omni to DALLE-3 using the OpenAI API's Image Generations Endpoint . How we built it The Magic Transform backend is built using Node.js and the OpenAI API. We built two routes in the backend: /api/describe , which passes an image URL to GPT Omni (via the OpenAI API) /api/transform , which passes the generated image description and a user-selected style to DALLE-3 The backend was containerized using Docker , and the container image was deployed to a Microsoft Azure Container App . Assets like images are hosted on a Cloudinary folder. Magic Transform is built with React and TypeScript, using Canva's app UI kit assets to build the front-end. We use React's built-in fetch() function to make API calls to our backend deployment on Azure. React's state management controls which components to show and hide during certain steps. Challenges we ran into We encountered several challenges, including working with the export SDK component, optimizing the loading bar speed, and maintaining image format consistency between user requests and DALL-E generation. Another challenge was exporting images. We want users to only press the "Transform" button, but the requestExport forces users to select through a second menu. We hope to work with the Canva Team to find alternatives. A final challenge we had was getting our frontend build small enough to be submitted for review in the Canva App Marketplace. When submitting the app into Canva, we noticed our asset images were too large to be bundled into the build. So we hosted these assets onto a Cloudinary folder. Accomplishments that we're proud of We are particularly proud of successfully creating a Canva App and deploying a functional back-end. We are also proud of successfully deploying and integrating third-party services like the OpenAI API, Azure, and Cloudinary. What we learned Joshua gained valuable experience in collaborating effectively with a team using Git, applying essential GitHub skills. He also learned how to make proper API calls to the back-end and display information on the front-end. Roy gained experience debugging frontend issues, writing a backend using Node.js, how to containerize a backend with Docker, and how to deploy and use Cloud services like Azure Container Apps and Cloudinary. What's next for Canva Magic Transform Moving forward, we plan to improve the codebase to enhance readability and optimization. Additionally, we aim to add new UI elements to improve the user interface and user experience. We are also exploring the possibility of adding features that allow users to easily share their creations, as well as implementing a payment model to accept payments. <div