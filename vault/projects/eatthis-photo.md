---
slug: "eatthis-photo"
url: "https://devpost.com/software/eatthis-photo"
title: "EatThis.photo"
hackathon: "SpurHacks"
organization: "SPUR & Konfer"
winner: true
words: 526
team_size: 2
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/runtime_tool_creation"
  - "mechanism/vision_ocr"
  - "mechanism/voice_speech"
  - "domain/agriculture_food"
  - "substrate/geospatial"
  - "substrate/video_visual"
  - "substrate/web_dom"
---

# EatThis.photo

> EatThis.Photo AI-powered food detection that instantly creates stunning, sharable menu experiences from a single snap.

[Devpost](https://devpost.com/software/eatthis-photo) · hackathon [[SpurHacks]]

## Facets

**mechanism** [[runtime_tool_creation]] [[vision_ocr]] [[voice_speech]]
**domain** [[agriculture_food]]
**substrate** [[geospatial]] [[video_visual]] [[web_dom]]

**stack** api, base64, blob/file, gemini, godaddy, javascript, ml, netlify

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for eatthis.photo

## Body

Eat this photo now you gotta eat this photo Man, I really want to eat this photo Eat this photo I would eat this photo Eat this photo too Eat this fire photo Inspiration Sometimes you're traveling in a new country, exploring a night market, or just sitting in front of an unfamiliar dish thinking: “What am I about to eat?” We realized that people (including us) often snap food photos out of curiosity, not just aesthetics. But photos don’t tell you what the food actually is — especially if you're not fluent in the cuisine or language. That’s where EatThis.Photo comes in — inspired by the idea of making food more understandable, accessible, and interactive. Whether you're a tourist, a food blogger, or just someone who doesn’t know what’s on their plate (guilty), this tool helps you identify and turn any meal into a beautiful digital menu — automatically. What it does EatThis.Photo uses AI to detect, recognize, and beautify your food photos — turning them into responsive, sharable web menus in seconds. Just upload a picture of your meal, and we’ll: Identify food items using computer vision Auto-generate a sleek menu layout Let you edit or re-style the items before publishing Export it as a standalone site or embeddable widget Perfect for chefs, food trucks, home bakers, or anyone who eats with their camera first. How we built it We built EatThis.Photo using good old HTML, CSS, and JavaScript for the frontend, keeping things lightweight and fast. The real magic, though, happens thanks to Gemini’s API. When a user uploads a photo, we send it to Gemini’s multimodal model, which analyzes the image and extracts descriptive keywords — like “sushi,” “ramen,” or “mystery meat with confidence issues.” We then pass those keywords to Gemini’s image generation API, which creates crisp, stylized versions of each food item. From there, we dynamically generate a clean, customizable menu interface using JavaScript and CSS animations, ready to share or embed. Challenges we ran into Getting food recognition to work well on low-light or cluttered images Finding a balance between automation and giving users customization options Deploying and optimizing the generated menus to look great on all screen sizes We also ran into the classic “demo-gods hate us” bug that came 10 minutes before our first pitch 😅 Accomplishments that we're proud of Detecting and labeling food photos with over 90% accuracy Creating a menu-building interface that's simple, beautiful, and fun Making something genuinely useful and sharable in under 36 hours Actually getting hungry looking at our own demos (yes, seriously) What we learned How to work fast and smart under pressure How powerful image AI can be when paired with thoughtful UX How to pitch and iterate quickly based on user feedback That you can absolutely ship a product that feels polished, even in a hackathon What's next for EatThis.photo We’re just getting started. Here's what's coming: Multi-photo batch uploads for full menu generation Ingredient breakdowns + nutrition estimation AI voice assistant for hands-free editing Integration with Instagram and Google Maps for real-world menu sharing Pitching to pop-ups, food creators, and festivals to go live this summer <div