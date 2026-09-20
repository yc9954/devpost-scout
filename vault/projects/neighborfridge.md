---
slug: "neighborfridge"
url: "https://devpost.com/software/neighborfridge"
title: "NeighborFridge"
hackathon: "LA Hacks 2026"
organization: "LA Hacks"
winner: true
words: 971
team_size: 4
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "mechanism/simulation_digital_twin"
  - "mechanism/vision_ocr"
  - "domain/agriculture_food"
  - "domain/education"
  - "domain/labor_employment"
  - "user/educator_student"
  - "substrate/financial_record"
  - "substrate/geospatial"
  - "substrate/web_dom"
---

# NeighborFridge

> NeighborFridge tracks groceries from receipts, predicts expiration dates, reduces waste, saves money, and gamifies sustainability with tips and leaderboards.

[Devpost](https://devpost.com/software/neighborfridge) · hackathon [[LA Hacks 2026]]

## Facets

**mechanism** [[realtime_stream]] [[simulation_digital_twin]] [[vision_ocr]]
**domain** [[agriculture_food]] [[education]] [[labor_employment]]
**user** [[educator_student]]
**substrate** [[financial_record]] [[geospatial]] [[web_dom]]

**stack** amazon-web-services, django, figma, figma-make, javascript, python, react, sqlite, tailwindcss

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for neighborfridge

## Body

thumbnail Inspiration As university students, we noticed how often groceries get forgotten in the back of the fridge. Fruit goes moldy, vegetables become too ripe, and leftovers get thrown away simply because life gets busy. We realized this was not just happening to us, but to students and families everywhere. Every wasted item represents more than lost money. It also means wasted water, energy, labor, and resources used to grow, transport, and sell that food. Seeing how common this problem was made us want to create something that could help people save money while also reducing unnecessary food waste. We wanted to build a solution that makes it easier for people to keep track of their groceries, use food before it expires, and share extra items with others instead of throwing them away. That idea became NeighborFridge. What it does NeighborFridge helps reduce food waste by making it easier for students and local communities to track, share, and sell extra groceries before they go bad. Instead of letting produce expire in the back of a fridge, users can upload food items through the platform by scanning receipts or manually creating a listing. Our receipt OCR system identifies grocery items and helps estimate expiration dates based on the type of food purchased. When an item is getting close to expiring, the platform sends email reminders to users so they can use it in time or post it to the marketplace instead of wasting it. Users are encouraged to list extra food on the platform, allowing nearby neighbors, roommates, or community members to claim or purchase items for pickup. This not only reduces waste, but also gives users a chance to recover some of their grocery costs and make money from food they would have otherwise thrown away. Shared pickup locations and centralized community lockers make exchanges simple, safe, and convenient. By combining food tracking, expiration prediction, smart reminders, and local food sharing, NeighborFridge turns wasted groceries into shared resources. Saving money, reducing environmental impact, and helping build stronger community connections. How we built it The front-end was built with React and Tailwind CSS. It was mostly prototyped between using ChatGPT Codex and Figma Make, mostly using Figma to help ideate during the process. Figma was a huge tool to help us plan and moodboard our program, which we fed into ChatGPT Codex to help define our user interface. We were inspired by receipts, fruit stickers, and the grocery store experience when building our user interface. On the backend, we built a Django + Django REST Framework API split into small apps (users/households, posts/marketplace, lockers, and receipts). Auth is handled with HttpOnly JWT cookies (SimpleJWT) plus CSRF protection, and we enabled CORS credentials so the frontend can make authenticated requests cleanly. For receipts, we implemented an OCR pipeline with Pillow + Tesseract (pytesseract) (with an optional Veryfi provider if configured) to extract the raw text, detect store/total, and parse candidate line items that users can confirm. For typed addresses and map pins, we geocode/reverse-geocode with OpenStreetMap’s Nominatim (with caching) to turn locations into human-readable pickup locations and coordinates. Challenges we ran into As a marketplace, our program required the need to handle lots of different data-points, which ends up interacting with each other in different ways. Being able to design our front-end workflows with all these different goals and endpoints in mind made it difficult to build the interface. We wanted to build something visually interesting, but also modular enough where we can reapply a lot of similar components across our different pages. In the backend we also had the issue of reaching the rate limit with our first iteration of the backend analyzing the receipts. This was due to using Google Gemini free tier limiting our responses. This lead to us to change to using a local model to have unlimited tokens for testing running off Ollama using Gemma 2. Accomplishments that we're proud of We are proud of intuitive and creative UI and with how our team used AI tools to increase productivity when producing code. We are especially proud of being able to produce a fully responsive application that works with both desktops and (mostly) mobile devices. Having a MVP that simulates our lockers in real-time with scalability in mind. What we learned On the front-end, we learned a lot about how to use design inspiration and mock-ups of individual components and have AI tools fill in the gaps and help build the individual components. I felt that this time, we had a better grasp of trusting the AI agent to build our user interface components as we focused on providing as much context as possible so the design goals of our website was clearly established. Additionally, we learned to trust the agent sometimes, as the agent can bring ideas to supplement your own creative process. On the backend, we learned how strong the Django framework was doing lots of the heavy lifting due to its built in features of: apps, settings, URLs, views, serializers, and permissions. We also learned how to build fallback systems due to using third party API services like a provider fallback using the Veryfi API if possible but it that fails to use tesseract a local OCR/parser. What's next for NeighborFridge As of now we only have a website and ideally if we had more time a mobile app making the app much more accessible. Use OAuth in the future to allow email scrapping of receipts securely from users that allow access to their email. We also want to create a physical prototype of our centralized lockers as well to demonstrate this idea could work and help support communities that need it. Last we also want to review all our code and reduce and simplify any service that is taking too long to process. <div