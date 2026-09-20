---
slug: "student-focus-shield"
url: "https://devpost.com/software/student-focus-shield"
title: "Student Focus Shield"
hackathon: "Student HackPad 2025"
organization: "Student Hackpad"
winner: true
words: 388
team_size: 1
has_repo: true
has_live: false
has_video: false
tags:
  - "project"
  - "mechanism/cross_origin_web"
  - "domain/developer_tools"
  - "domain/education"
  - "domain/supply_logistics"
  - "user/educator_student"
  - "substrate/code_repository"
  - "substrate/web_dom"
---

# Student Focus Shield

> A browser extension to help students beat distractions. Features timed focus, a custom blocklist, and a motivational blocker page that turns distraction into encouragement.

[Devpost](https://devpost.com/software/student-focus-shield) · hackathon [[Student HackPad 2025]]

## Facets

**mechanism** [[cross_origin_web]]
**domain** [[developer_tools]] [[education]] [[supply_logistics]]
**user** [[educator_student]]
**substrate** [[code_repository]] [[web_dom]]

**stack** css, html, javascript

## How they structured the write-up

- inspiration
- what it does
- features
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what's next for student focus shield
- ai tools used

## Body

Inspiration As students, our biggest enemy isn't the difficulty of the subject—it's the "infinite scroll." We sit down to study, open a browser for research, and 30 minutes later, we are still scrolling through YouTube Shorts or Instagram Reels. We wanted to build a tool that doesn't just block sites but actually helps students build better habits. What it does Student Focus Shield is a Chrome Extension that acts as a "commitment device." It allows students to block distracting websites during study sessions. Features Our extension has mainly these two features. Timed Focus: Students can set a specific timer (e.g., 45 minutes). Indefinite Focus: A hard toggle for long study sessions. How we built it We built this using HTML, CSS , and JavaScript on the Manifest V3 Chrome Extension API. 1. The Brain: We used background.js with the chrome.alarms API to handle the background timer so the focus mode persists even if the popup is closed. 2. The Shield: We used the chrome.tabs.onUpdated listener to detect blocked URLs and redirect them. The UI: We built a clean, student-friendly popup interface that manages state using chrome.storage.local. Challenges we ran into The biggest technical challenge was a caching issue. Chrome was caching the "Blocker Page," which meant the motivational quotes wouldn't refresh, and the timer wouldn't update correctly. We solved that by implementing a "cache-busting" technique in the background script, appending a unique timestamp to the URL on every redirect to force a fresh page load. Accomplishments that we're proud of We are proud of creating a "soft" blocker. Instead of just saying "Access Denied," we provide a supportive nudge. We are also proud of implementing the custom blocklist feature, giving users full control over what they consider distracting. What's next for Student Focus Shield Currently, this is a desktop-only tool. Our next step is to explore mobile implementations to provide system-wide blocking across all student devices. AI Tools Used Code Debugging : I used Google Gemini to help identify specific bugs, particularly the caching issue where the blocker page wouldn't refresh. Boilerplate Generation : I used AI to generate the initial structure of the manifest.json file to ensure permissions were correct. Documentation : I used QuillBot AI to help refine the wording of my README file and this project description to ensure it was clear and professional. <div