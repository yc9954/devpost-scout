---
slug: "studiolingo"
url: "https://devpost.com/software/studiolingo"
title: "Studylingo"
hackathon: "Hack the North 2024"
organization: "Hack the North"
winner: true
words: 379
team_size: 4
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/cross_origin_web"
  - "domain/education"
  - "user/educator_student"
  - "user/researcher"
  - "substrate/web_dom"
---

# Studylingo

> A Pomodoro timer that keeps you on track, summarizes your browsing, and turns study time into a fun quiz challenge.

[Devpost](https://devpost.com/software/studiolingo) · hackathon [[Hack the North 2024]]

## Facets

**mechanism** [[cross_origin_web]]
**domain** [[education]]
**user** [[educator_student]] [[researcher]]
**substrate** [[web_dom]]

**stack** cohere, defang, fastapi, javascript, mongodb, python, react, vite

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for studylingo

## Body

Website Studylingo Chrome Extension Studylingo summarizing AWS documentations Quiz page Quiz page with answers Inspiration We were inspired to build a tool that addresses the everyday struggle of staying focused while studying or browsing the web. We wanted to turn passive reading into an active learning experience while helping students manage their time efficiently. Integrating a Pomodoro timer, web summarization, and quiz generation into a single Chrome extension emerged as a creative way to keep learning fun and engaging. What it does Studylingo is a Chrome extension with three main features: Web Page Summarization: This feature automatically summarizes the content of any web page the user is browsing, making it easier to absorb key points quickly. Pomodoro Timer: Helps users stay focused using timed study sessions with customizable work and break intervals. Quiz: Turns the summarized content into interactive quizzes, making the learning experience fun and reinforcing the material meaningfully. How we built it We built Studylingo using React for the Chrome extension and Python FastAPI for the backend. Cohere’s AI helps us summarize web pages and turn them into quizzes. It works through a Chrome extension, so you can learn and quiz yourself while browsing seamlessly. We deployed the backend using Defang. Challenges we ran into It was tricky to get all the features to work smoothly in one Chrome extension. The Chrome extension library we used, CRXJS, was no longer actively maintained, so documentation was minimal. Accomplishments that we're proud of We’re proud of creating a Chrome extension for the first time, something we’ve never tried before, and getting all the features to work together. We are also proud of leveraging LLMs like Cohere to help others further themselves, in this case, academically. Plus, being part of Hack the North!!! What we learned We learned how to combine browser APIs with AI-driven content generation, building an efficient Chrome extension. In addition, we learned how to build AI-driven APIs and the different ways data gets transferred when using LLMs on APIs. What's next for Studylingo We plan to enhance the quiz generation feature by introducing more question formats and difficulty levels. Additionally, we want to expand the summarization capabilities to handle more complex web pages while offering users personalized study analytics and progress tracking within the extension. <div