---
slug: "autogear"
url: "https://devpost.com/software/autogear"
title: "autoGear"
hackathon: "LA Hacks 2026"
organization: "LA Hacks"
winner: true
words: 507
team_size: 1
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/deterministic_policy"
  - "mechanism/realtime_stream"
  - "mechanism/retrieval_grounding"
  - "domain/education"
  - "domain/labor_employment"
  - "domain/retail_commerce"
  - "domain/supply_logistics"
  - "user/educator_student"
  - "user/government_staff"
---

# autoGear

> Personalized recommendations for office improvements

[Devpost](https://devpost.com/software/autogear) · hackathon [[LA Hacks 2026]]

## Facets

**mechanism** [[deterministic_policy]] [[realtime_stream]] [[retrieval_grounding]]
**domain** [[education]] [[labor_employment]] [[retail_commerce]] [[supply_logistics]]
**user** [[educator_student]] [[government_staff]]
  <sub>weak: web_dom</sub>

**stack** best-buy, clerk, coco-ssd, css, gemma, html, mongodb, next.js, node.js, prices-api, prisma, react, tailwind-css, tensorflow.js

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for autogear

## Body

Inspiration We live in a world filled with technologies nowdays. With work styles leaning more and more towards spending time in front of laptops, a comfortable office space is crucial for maintaining long-term health and well being. However, people often waste money upgrading the wrong thing first, or has too many options to decide. As a student on a budget, it was tedious and gruesome to look through all the available options for office equipment that can help fix my posture, avoid straining my eyes, and fits my body. I wanted a quick way to personalize and determine the best upgrade to get to maximize the value money gets while still satisfying my requirements. What it does AutoGear is a web application that helps people figure out the next office equipment upgrade that will improve their setup and pain points that the user has, recommending the most compatible products the user may not even know about. How we built it Inventory capture: Manual device lookup that merges MongoDB-backed rated catalog entries with up-to-date Best Buy search results, or browser-based video scan using TensorFlow.js COCO-SSD Explainable ranking: every recommendation is backed by deterministic scoring using a math formula, and Gemma-based reasonings to verbally explain why each recommendation is made Live value updates: Best buy API for products, pricesAPI for lowest prices Privacy: MongoDB to store all sensitive data the user inputed, and login authentication through Clerk for user protection Challenges we ran into One of the biggest challenges was balancing personalized recommendations with practical, real-world availability. A product might score well ergonomically, but it still needs to fit the user's budget, preferences, and current market options. I also had to make the recommendation system explainable. I wanted users to understand why a certain upgrade mattered, what pain point it addressed, and why it should be prioritized over other upgrades. The recommendation scores is open-ended and difficult to come up with a formula for. Another challenge was combining multiple data sources, including manual inventory input, catalog data, Best Buy results, and AI-generated explanations, while keeping the experience fast and simple for users. Accomplishments that we're proud of Storing sensitive user data in MongoDB for security purposes Heavy personalized recommendation algorithm that is transparent and explainable Live updates on prices and new devices creating a practical tool that solves a real problem many students, remote workers, and desk users face: improving comfort and health without wasting money on the wrong upgrade. What we learned How to combine AI with deterministic logic. AI is useful for generating natural explanations, but scoring and ranking need to be consistent, predictable, and grounded in user constraints. How difficult product recommendation can be when real users have different budgets, body types, work habits, and priorities. What's next for autoGear Expand the product catalog beyond office equipment into other lifestyle categories, such as dorm rooms, gaming setups, home organization, and accessibility tools. AutoGear could become a full personal upgrade assistant that helps users make smarter purchasing decisions across their daily life using highly personalized recommendations <div