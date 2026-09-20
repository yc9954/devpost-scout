---
slug: "smart-meeting-assistant"
url: "https://devpost.com/software/smart-meeting-assistant"
title: "Smart Meeting Assistant"
hackathon: "AWS Lambda Hackathon"
organization: "Amazon"
winner: true
words: 453
team_size: 1
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/voice_speech"
  - "domain/developer_tools"
  - "substrate/transcript_audio"
  - "substrate/web_dom"
---

# Smart Meeting Assistant

> Upload audio recordings to automatically create and manage Jira tasks

[Devpost](https://devpost.com/software/smart-meeting-assistant) · hackathon [[AWS Lambda Hackathon]]

## Facets

**mechanism** [[voice_speech]]
**domain** [[developer_tools]]
**substrate** [[transcript_audio]] [[web_dom]]

**stack** amazon-dynamodb, amazon-web-services, bedrock, claude, css, html, javascript, node.js, npm, react, s3, sam, vite

## How they structured the write-up

- inspiration
- what it does
- how i built it
- challenges i ran into
- accomplishments that we're proud of
- what i learned
- what's next for smart meeting assistant

## Body

diagram Inspiration During my university projects this last semester, I kept running into the same frustrating issue. We'd have team meetings, discuss who was doing what, and everyone would leave feeling like we were on the same page. But days later, we'd discover tasks were forgotten, duplicated, or assigned to the wrong people. The hardest thing to keep track of during and after meetings was who was doing what. What it does Smart Meeting Assistant solves this confusion by letting you upload an audio or video file of your meeting, then automatically: Transcribes the entire conversation Extracts actionable tasks with assignees and priorities Creates properly formatted Jira tickets No more post-meeting confusion or the necessity to actively write tasks mid-meeting. How I built it I built this as a serverless event-driven system using AWS Lambda functions that communicate through EventBridge events: Frontend : React app where users upload meeting recordings File Processing : Lambda functions handle secure S3 uploads using presigned URLs Transcription : Amazon Transcribe converts audio to text AI Analysis : Amazon Bedrock with Claude 3.5 Sonnet extracts tasks and analyzes existing work Jira Integration : Automatic ticket creation and updates via Jira API The entire workflow is orchestrated through 10 different Lambda functions, each handling a specific part of the pipeline from upload to final Jira ticket creation. Challenges I ran into The hardest part was learning Event Driven Architecture and AWS. Coming from simple university projects, I suddenly needed to understand how Lambda functions trigger other Lambda functions, how EventBridge orchestrates workflows, and how all these services talk to each other asynchronously. Accomplishments that we're proud of I'm proud that I persevered through the learning curve, even when I had thoughts of giving up while tackling the complexity of AWS Lambda. I'm proud that I built a fully serverless system that scales automatically, successfully integrated 6 different AWS services into a cohesive workflow, and implemented an application that solves a real-world problem affecting teams everywhere. What I learned This project taught me that building distributed systems is completely different from building simple web apps. You have to think in events, async processing, and plan for things to fail. While building the project, I tried to follow AWS Lambda's best practices and serverless design patterns, while also debugging and monitoring serverless applications with CloudWatch. What's next for Smart Meeting Assistant I built my architecture on the principle of extensibility, as illustrated in the system diagram. Next, I want to add multi-platform integration for Teams and Slack. A big component that I haven't had time to master is comprehensive testing. Another dream would be to extend this system further by analyzing sentiments from visual input to improve task extraction accuracy. <div