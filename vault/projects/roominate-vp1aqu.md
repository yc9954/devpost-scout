---
slug: "roominate-vp1aqu"
url: "https://devpost.com/software/roominate-vp1aqu"
title: "Roominate"
hackathon: "Cal Hacks 12.0"
organization: "Cal Hacks"
winner: true
words: 709
team_size: 4
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/vision_ocr"
  - "domain/agriculture_food"
  - "substrate/web_dom"
---

# Roominate

> Ever stuck procrastinating on important tasks? Roominate breaks down your tasks into smaller steps, and incentivizes completing them by allowing you to decorate a home just for you!

[Devpost](https://devpost.com/software/roominate-vp1aqu) · hackathon [[Cal Hacks 12.0]]

## Facets

**mechanism** [[vision_ocr]]
**domain** [[agriculture_food]]
**substrate** [[web_dom]]

**stack** asi:one, claude, godot, python

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- what's next for roominate

## Body

Inspiration Studies have shown gamification has psychological benefits in one's ability to complete tasks. Your to-do's can feel daunting, and the "reward" feels too far away, especially for people with ADHD or chronic procrastination. We conducted research on spatial memory, discovering visualizing and attaching progress tracking to object formation helps users develop engagement and desire to complete tasks, decreasing the chance of dropping out and giving up tasks. Breaking tasks into smaller steps decreases the mental barrier of starting tasks and bringing in rewards with gamification drives it further. What it does Roominate gamifies and offers incentives for completing your tasks by rewarding completion with the ability to decorate a cozy home. Place Your Task: Instead of "adding a task" to an endless list, you are provided with a personal space and "place a task" in a room. This turns an abstract chore ("Write Essay") into a concrete "ghosted" object (like a Bookshelf or a plant) in a specific spot where you could categorize and recall it based on spatial memory. AI Task Breakdown: Have trouble breaking down your complex task into steps? Our AI assistant breaks that intimidating task into small, non-threatening, actionable subtasks (e.g., "Research topic," "Write outline," "Write first draft"). The "blank page" problem is gone. Create Your Space: Completing a task solidifies the “Bookshelf” as a permanent, beautiful object. As you complete tasks, you unlock new rooms and more opportunities for different furniture, building a home you’re genuinely attached to. Get Motivated: The friendly cat inside your home gives you advice and motivation to complete your tasks. psst Crater... there may be a secret cow as well, but I wouldn't follow its advice! How we built it We built Roominate in Godot 4.5 focusing on seamless UI/UX design. The global logic is managed through signals to synchronize updates across all scenes. Each major system; task creation, to-do management, room layout, all communicate through these signals to ensure smooth, event-driven updates without manual dependencies. Our AI system, powered by ASI:One implemented in cat.gd and cow.gd as well as OpenRouter with Claude shown in our task step generator. In terms of the assistants, they receive updates about the latest edited task, sent through HTTP requests, and respond with a short and personality-driven feedback. The dialog appears dynamically in-game and an automatic timer, creating natural conversational flow without blocking gameplay. The room system ties task progress directly to world building. Completed tasks instantiate corresponding furniture objects within room_layout.gd , while furniture.gd manages placement. Tasks are tracked globally enabling players to unlock rooms and better interactions with the cow and cat assistants. Challenges we ran into One of the biggest challenges we faced was standing out in a space where productivity tools and gamified tasks have already been explored. We didn’t want to make something that simply looked different, we wanted it to feel different, with real emotional engagement and long-term growth potential. Finding that balance between familiar and innovate required a lot of iteration and design restraint. Integrating AI added another layer of complexity. We wanted the AI assistants (like our cat and cow personalities) to feel dynamic and responsive, but not intrusive or repetitive. Tuning their tone, behavior, and timing so they were motivating (well, at least the cat is) rather than distracting was a careful balancing act. We also faced the usual hackathon time pressure, merging design, code, and polish under tight deadlines while keeping our vision cohesive. The biggest challenge wasn’t just technical; it was staying focused on our core idea: making productivity something players would want to return to, again and again. What's next for Roominate We believe Roominate is an innovative new tool for productivity. Our roadmap for continuation includes: Multiplayer & Social Rooms: We did some user interviews and concept testing, and found that social aspects are also incentives for many people to accomplish tasks. Imagine visiting a friend's "Sweet Home" to see the objects they've built, or even tackling a "group project" that builds a shared object in a community space. Deeper Customization: Select from an option of themes such as pirate, farm, and sci-fi to make every space truly unique and personalized. Application Integration: Launch the programs or open the web pages needed for your task directly from Roominate. <div