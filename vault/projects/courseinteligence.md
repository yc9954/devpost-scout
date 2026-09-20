---
slug: "courseinteligence"
url: "https://devpost.com/software/courseinteligence"
title: "CourseIntelligence"
hackathon: "Hack the North 2025"
organization: "Hack the North"
winner: true
words: 390
team_size: 3
has_repo: true
has_live: false
has_video: false
tags:
  - "project"
  - "domain/education"
  - "domain/labor_employment"
  - "user/educator_student"
  - "user/researcher"
  - "substrate/sensor_telemetry"
  - "substrate/web_dom"
---

# CourseIntelligence

> Making academic and professional lives easier for students around the world! Our project scrapes community data to provide students with valuable information to simplify the course selection process.

[Devpost](https://devpost.com/software/courseinteligence) · hackathon [[Hack the North 2025]]

## Facets

**domain** [[education]] [[labor_employment]]
**user** [[educator_student]] [[researcher]]
**substrate** [[sensor_telemetry]] [[web_dom]]
  <sub>weak: structured_db</sub>

**stack** css, databricks, html, llama, openai, python, sql

## How they structured the write-up

- inspiration

## Body

Website Homepage Webscraping Reddit (250k + words) Databricks data dashboard Augmented database using AI Get data straight from student opinions Inspiration What it does CourseIntelligence scrapes Reddit communities like r/uwaterloo and r/UCalgary for course-related discussions, combines them with official university catalog data, and aggregates the results into structured metrics: • How hard is this course? • Is it time-consuming? • Lab-based or theory-heavy? • Which professors are recommended? • Resume/industry value. The processed data is uploaded into Databricks, where we use AI models to summarize and standardize student experiences into comparable course profiles. How we built it • Web scraping & Reddit API (PRAW): Pulled posts and comments from multiple subreddits. • Data pipelines (Python + JSON): Stored scraped discussions in structured JSON with partial-save fail-safes. • Databricks: Used bronze → silver → gold layered processing to clean, aggregate, and query the data. • AI integration: Leveraged LLMs via Databricks model serving to summarize free-form Reddit text into structured course evaluation metrics. • Frontend (Dash app): Simple interface to search for a course and instantly see summarized insights. Challenges we ran into • Reddit data is noisy and unstructured, requiring heavy cleaning. • API rate limits slowed scraping significantly. • Getting Databricks files API to properly accept uploads was tricky. • Designing consistent JSON schemas so AI outputs could be queried easily. Accomplishments that we’re proud of • Built a scalable pipeline that continuously scrapes, saves partial progress, and avoids total data loss. • Summarized thousands of Reddit comments into clean, comparable insights. • Integrated Databricks model serving to directly run AI queries on Reddit data. • Proved that students can make better-informed course choices using aggregated real-world feedback. What we learned • How to connect real-world unstructured data into a structured analytics workflow. • The power of Databricks bronze → silver → gold pipelines for data cleaning and aggregation. • Best practices for fault-tolerant scraping pipelines (e.g., partial JSON saving). • How to balance Reddit’s raw opinions with AI summarization without losing nuance. What’s next for CourseIntelligence • Expand beyond Waterloo and Calgary to other universities worldwide. • Add sentiment analysis dashboards to capture positive/negative trends. • Build a recommendation engine that suggests courses based on a student’s career goals. • Release as a student-facing web app where anyone can search for courses and instantly get community-driven insights. <div