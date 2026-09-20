---
slug: "image-crawler"
url: "https://devpost.com/software/image-crawler"
title: "Image Crawler"
hackathon: "Code with Kiro Hackathon"
organization: "Kiro"
winner: true
words: 344
team_size: 1
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "domain/developer_tools"
  - "user/developer"
  - "user/researcher"
  - "substrate/video_visual"
  - "substrate/web_dom"
---

# Image Crawler

> Image Crawler ethically automates bulk image discovery, respecting robots.txt to download all images from any site. It's the responsible tool for designers, researchers, and developers.

[Devpost](https://devpost.com/software/image-crawler) · hackathon [[Code with Kiro Hackathon]]

## Facets

**domain** [[developer_tools]]
  <sub>weak: labor_employment, retail_commerce, security_privacy</sub>
**user** [[developer]] [[researcher]]
**substrate** [[video_visual]] [[web_dom]]
  <sub>weak: document_pdf, sensor_telemetry</sub>

**stack** axios, cheerio, material-ui, node.js/express, typescript

## Body

Image Crawling from Intented website Scrolling Images Selected Image Generated Blened Images Inspiration Section: Personal story about the frustrating manual image collection process Looking for a simple solution to have Printing store, to print the generative AI images on Poster, T-shirt, mugs etc. Connection to Kiro.dev and spec-driven development approach What it does: It allow users to Pass their favorite website url to collect images from it. It respect the robot.txt, nofollow for the website. It does 3 things: -- Users able to build Collage from images they found from the website. -- Users able to download images from the website(currently I restrict to max 50 and dept 1) for performance and simplicity. -- Users able to select few images, add text description and generate AI Blended images. For this I am using Google Generatvie AI. Currently it's mocked, however imagan model is configuriable. How we built it: Detailed architecture breakdown Step-by-step Kiro development workflow Technology stack with justifications Emphasis on structured AI-assisted development Challenges: In the start Kiro started with spec development mode, that generate specs, design and tasks, but the task list was too big to follow along. Kiro keep loosing the token created while development and needs to wait for few days to resume work. Real-world problems like CORS, security, memory management Not able to automate the deployment on Vercel, and automate with github actions. Accomplishments: Organized into Technical, Architecture, Development Process, and Ethical categories Specific metrics (85% test coverage, sub-2-second load times, zero security vulnerabilities) Demonstrates both technical excellence and responsible development I also refactor the code as per SOLID design principle, Kiro adapt and refactor the code very easily What we learned: Specification driven development vs Vibe Codig by Kiro IDE Technical lessons about web crawling and security User experience and accessibility learnings About Project Steering documents Kiro Agent hooks feature, really like this feature. What's next: Could integrate with Image/Video Generating API, and seed these images to get something awesome Platform expansion possibilities, to scale from 50 images to thousands Can make it a realtime ecommerce store. <div