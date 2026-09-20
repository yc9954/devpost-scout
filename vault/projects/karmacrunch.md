---
slug: "karmacrunch"
url: "https://devpost.com/software/karmacrunch"
title: "KarmaCrunch"
hackathon: "Hack Reddit 2025"
organization: "reddit"
winner: true
words: 312
team_size: 1
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
---

# KarmaCrunch

> An AI-powered tool that analyzes Reddit activity and generates a post with a report on specific subreddits or users.

[Devpost](https://devpost.com/software/karmacrunch) · hackathon [[Hack Reddit 2025]]

## Facets

  <sub>weak: cross_origin_web</sub>

**stack** devvit, react, typescript

## How they structured the write-up

- inspiration
- what it does
- how i built it
- challenges
- accomplishments
- what i learned
- what's next for karmacrunch

## Body

Main page to generate reports User report home page Subreddit report home hape Inspiration I wanted to build an app that integrates AI tools, and Reddit's API and Devvit provided the perfect opportunity. What It Does Run a Report User Report : Analyzes a user's Reddit activity, including post history, comment trends, and karma accumulation. Subreddit Report : Analyzes subreddit content, trends, top posts, and community behavior. AI-Powered Analysis Reports are generated using OpenAI's GPT-4o mini model, delivering fun, insightful, and sometimes humorous summaries. Report Preview After generation, the personalized report can be viewed in preview mode, where the user can choose to either post it to r/KarmaCrunch or delete it. Post Frequency User Reports : A user can run a report on themselves up to 3 times a day. Subreddit Reports : A user can run a report on a subreddit up to 5 times per day. Data Deletion If a user chose to post their report, and the decide they want to remove their data, they can simply delete their post, it automatically triggers an action to remove any associated report data stored for that user. How I Built It The app uses the Reddit API to gather top posts and comments, which are formatted into prompts for the LLM. The LLM returns structured responses for easy UI presentation. Challenges Controlling the LLM’s output for consistent report formatting was tricky, given the unpredictability of AI-generated text. Ran in to timeout limitations on Android. Accomplishments I’m proud of the app's layout and the AI output, some of the AI-generated summaries have been genuinely entertaining. What I Learned I gained experience working with the OpenAI API and structuring prompts to get structured JSON responses. What's Next for KarmaCrunch Refining prompts for better outputs. Adding customization options, like letting users choose the report sarcasm level. Adding support for Android Generating AI portrait <div