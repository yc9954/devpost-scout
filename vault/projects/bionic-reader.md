---
slug: "bionic-reader"
url: "https://devpost.com/software/bionic-reader"
title: "Bionic Reader"
hackathon: "Student Innovators Without Borders Hacks (Students; Open Ended)"
organization: "Batch 09"
winner: true
words: 408
team_size: 1
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/cross_origin_web"
  - "mechanism/realtime_stream"
  - "domain/supply_logistics"
  - "substrate/web_dom"
---

# Bionic Reader

> This is a project that uses the strategy of Bionic reading through an extension to allow anyone to read faster.

[Devpost](https://devpost.com/software/bionic-reader) · hackathon [[Student Innovators Without Borders Hacks -Students- Open Ended-]]

## Facets

**mechanism** [[cross_origin_web]] [[realtime_stream]]
**domain** [[supply_logistics]]
**substrate** [[web_dom]]

**stack** babel, css3, edge, es6+, eslint, extensions, git, github, html5, husky, javascript, jest, json, languages:**

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for bionic reader

## Body

Inspiration I needed a project for the Summer of Making Project hosted by Hack Club during the summer, but I only realized about SOM at the end of the summer and made this project around September. I thought up of this idea because I was reading a lot of articles on code development and wanted to read them faster while retaining the same amount of knowledge. That's when I remembered a paragraph that I saw that showed how Bionic Reading was great for this job. What it does Bionic Reader transforms text on any website by bolding portions of words to give the eye an auto-complete like feature and it improves reading flow. It uses linguistic algorithms that are able to distinguish between function words (articles, prepositions) and content words (nouns, verbs), and applying different bold ratios for optimal readability. Users can adjust the intensity in real-time and toggle the feature on/off with a keyboard shortcut (Ctrl+Shift+B) in the Edge browser. How we built it I developed the extension in four phases: Core Algorithm (word classification), Security Architecture (message validation and rate limiting), Performance Engineering for at least 3,000 batch nodes, and User Experience to make the project look good and have a great experience for the user. Challenges we ran into The biggest challenges were handling dynamic content on modern websites (SPAs, infinite scroll), and ensuring that transformed text remains selectable and copyable, along with maintaining performance while processing thousands of DOM nodes in real-time, and implementing security measures to prevent injection attacks while working across all websites. Accomplishments that we're proud of I successfully created an algorithm that intelligently categorizes words for optimal bionic reading. This also includes a personally formed and tested formula for getting the best amount of a word to bold. I also achieved a high level of security with zero external requests and local-only processing. Built a performant system that handles 1,000+ nodes per second with batch processing and memory management using WeakMaps. What we learned Developing modern web extensions with Manifest V3, advanced DOM manipulation techniques, programming for text analysis, security development with complete validation, performance optimization for real-time processing, and cross-browser compatibility. What's next for Bionic Reader I plan to release Bionic Reader to the Chrome Web Store, in addition to the current Edge store. Developing mobile app versions and exploring a chance to partner with popular reading apps and e-book platforms to increase the reach of this product. <div