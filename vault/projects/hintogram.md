---
slug: "hintogram"
url: "https://devpost.com/software/hintogram"
title: "Hintogram"
hackathon: "Student HackPad 2025"
organization: "Student Hackpad"
winner: true
words: 680
team_size: 1
has_repo: true
has_live: false
has_video: false
tags:
  - "project"
  - "mechanism/cross_origin_web"
  - "domain/education"
  - "user/educator_student"
  - "substrate/document_pdf"
  - "substrate/video_visual"
  - "substrate/web_dom"
---

# Hintogram

> Want hints? This chrome extension will give you exactly what you want to help you in your homework. It will tell you some hints to solve the questions.

[Devpost](https://devpost.com/software/hintogram) · hackathon [[Student HackPad 2025]]

## Facets

**mechanism** [[cross_origin_web]]
**domain** [[education]]
  <sub>weak: supply_logistics</sub>
**user** [[educator_student]]
**substrate** [[document_pdf]] [[video_visual]] [[web_dom]]

**stack** cengage, chrome, chrome-ext, console, gemini, google-ai-studio, javascript, json, manifest-v3

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for hintogram

## Body

Hint given beside the asnwer text box json code Inspiration We were inspired by the universal frustration of STEM students using platforms like WebAssign (Cengage). When you hit a wall in a multi-step calculus or physics problem, the platform gives you a red "X" and maybe a confusing block of "Enhanced Feedback." Students are left relying on outside solvers that often give the final answer, bypassing the learning process. Our goal was to create the perfect digital tutor: one that provides the right hint at the right moment to guide the student's thinking, without robbing them of the solution. What it does Hintogram is a browser extension that integrates directly into the WebAssign homework interface. It transforms the passive learning experience into an active tutoring session powered by the Gemini AI. Instant Trigger: As soon as the student clicks into an answer box on any problem, the extension activates. Surgical Scraping: It extracts the full context of the current problem, including equations, graphs, and text descriptions. Concise AI Hint: The cleaned text is sent to the Gemini 2.5 Flash API with a strict system prompt to act as a non-solution-giving tutor. Floating Pop-up: The hint (e.g., "Start by finding the derivative of the integrand to apply the Fundamental Theorem of Calculus") appears instantly in a small, non-intrusive floating bubble next to the input field. How we built it Hintogram was built using standard web technologies integrated with the Gemini API: Front-end (Browser Extension): Built using JavaScript (content.js), HTML, and CSS to inject content and manage event listeners (focusin) directly into the WebAssign DOM. Back-end (API Handling): Managed by the background script (background.js), which uses the fetch API to make POST requests to the Gemini API endpoint. AI Model: We leveraged Gemini 2.5 Flash for its speed and its ability to process complex math descriptions while strictly adhering to the "concise tutor" system prompt, ensuring hints are immediate and pedagogically sound. Challenges we ran into The primary challenge was overcoming the highly irregular and dynamic HTML structure of the WebAssign platform. The "Invisible" Question Text: Standard CSS selectors consistently failed to isolate the math question. The text was buried deep within generic div and span tags. The Status 400 API Barrier: Once we successfully scraped the content, the Gemini API kept rejecting the request (Status 400 Bad Request). We realized this wasn't a coding error, but a data overload issue—the scraper was pulling in thousands of unwanted characters (navigation bars, score tables, and full descriptions of four different multiple-choice graph options). Accomplishments that we're proud of Our proudest accomplishment was the implementation of a truly resilient and surgical scraping solution: Anchor-Based Scraping: Instead of searching the entire page, we used the clicked input box (event.target) as an anchor. The script iteratively searched up the DOM tree until it found the nearest reliable parent container (like the .walpger problem wrapper), ensuring we only extracted text related to the problem being solved. Surgical Regex Cleaning: We developed a specialized, powerful regular expression (e.g., /A curve labeled g(x) is graphed. ?|Enhanced Feedback. $/gs) that could surgically remove massive, multi-line blocks of garbage text (like the four verbose graph option descriptions) that were causing the API to fail. This reduced the prompt size from an overwhelming document to a concise, clean question. What we learned We gained deep expertise in resilient DOM traversal and data sanitation within hostile environments. We learned that integrating an LLM into an existing, complex web application requires treating the scraped text as a major security and reliability variable. Success wasn't about the API call itself, but about controlling the quality and size of the input data fed to the model. What's next for Hintogram Multi-Language Support: Expand the system prompt to support hints in Spanish, French, or other languages for international students. Image Parsing: Integrate the Gemini Vision model to directly process and analyze mathematical graphs and equations embedded as images within the problems. Adaptive Hint Levels: Add a feature to offer escalating hint levels (e.g., "Level 1: Concept Review," "Level 2: Step-by-Step Guidance") based on student input attempts. <div