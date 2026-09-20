---
slug: "fragments-gmleoj"
url: "https://devpost.com/software/fragments-gmleoj"
title: "Fragments"
hackathon: "Hack the North 2025"
organization: "Hack the North"
winner: true
words: 670
team_size: 4
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/cross_origin_web"
  - "mechanism/realtime_stream"
  - "mechanism/vision_ocr"
  - "domain/agriculture_food"
  - "domain/developer_tools"
  - "user/general_public"
  - "substrate/document_pdf"
  - "substrate/web_dom"
---

# Fragments

> Clip, save, and organize the exact moments that spark your ideas.

[Devpost](https://devpost.com/software/fragments-gmleoj) · hackathon [[Hack the North 2025]]

## Facets

**mechanism** [[cross_origin_web]] [[realtime_stream]] [[vision_ocr]]
**domain** [[agriculture_food]] [[developer_tools]]
**user** [[general_public]]
**substrate** [[document_pdf]] [[web_dom]]

**stack** amazon-web-services, cohere, css, figma, html, javascript, nextjs, opencv, python

## How they structured the write-up

- inspiration
- core features
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for fragments

## Body

Landing Page Chrome extension for screen recording Chrome extension for clip submission Collection of saved clips Saved clip with AI generated tags and instructions Architecture Diagram Inspiration Great work is connected. Anything you ever make is produced by drawing on everything you've ever consumed. Being a better creator, whether in video production, frontend development, or freestyle dance, begins with being a better consumer. So how can we be better consumers? By leaving precise fragments of the best work we find across the internet for our future selves -- all in one place. Truth is, in most creative domains, a video is worth a million words. That's why we built Fragments, your second brain for video that helps you clip, save, and organize the exact moments that spark your ideas. Core Features 1. Cross-Platform Clipping System Chrome Extension Integration : Hover-to-record button appears on all video elements across the web (instagram, tiktok, youtube, netflix etc.) Smart Recording UI : Dark overlay with timer, stop/delete controls, and a metadata form that enables you to leave specific tags and notes for every clip (fragment). 2. AI-Powered Video Analysis & Tagging Frame Extraction : Frames are extracted every 2 seconds for fragments using OpenCV Cohere Vision AI Integration : Based on extracted frames, Cohere's vision AI model generates video summaries and intelligent tags 3. Multi-Format Video Processing Pipeline Format Optimization : The original WebM video files are converted using FFmpeg to GIFs & MP4s, stored in S3, and then stored with the video metadata in DynamoDB. 4. Interactive Video Gallery GIF Preview Gallery : Quick browsing of all fragments with various filters Metadata Display : Upon drill-down, tags, notes, source URLs, and AI-generated descriptions are shown next to each fragment Privacy Controls : Each fragment has a public/private visibility setting 5. Real-Time Second Brain Search OpenSearch Integration : All data in DynamoDB is indexed to enable global fuzzy search across titles, descriptions, tags, notes, and AI-generated content to enable quick finding of any fragment Real-Time Sync : DynamoDB streams automatically update search index 6. Content Discovery Community Curation : Find popular collections and fragments from the community Social Network : Follow creators you like to see their latest fragments in a feed How we built it Tech Stack Frontend : Next.js 15, React 19, TypeScript, Tailwind CSS, Chrome Extension API, MediaRecorder API, MutationObserver API Backend : Python, FastAPI, DynamoDB, Boto3 (AWS SDK), OpenCV, FFmpeg Infrastructure : AWS (S3, Lambda, DynamoDB, OpenSearch, CloudWatch, MediaConvert), Vercel, Auth0 AI : Cohere AI (c4ai-aya-vision-32b), Computer Vision (OpenCV) Challenges we ran into Screen recording videos on different sites Debugging auth0 Setting up AWS permissions (across team and aws services) Latency and load times Using Cohere to analyze clips for instructions Accomplishments that we're proud of Finishing the MVP and having a working demo Chrome extension has a smooth UI and actually works across platforms! Landing page visual hook OpenSearch indexing + DynamoDB Streams integration AWS Infrastructure stack What we learned Technical Learnings By default, all aws services have no permissions. Service-to-service delegation requires even more permissions! Lambda default timeout is 3s, which is way too short for most cases OpenSearch automatically creates inverse indices for each field in a document (and thus DynamoDB table if indexing on one), which helps make search really quick! Personal Learnings A great idea requires going deep in a field. This is best done when at least one person on the team already has a lot of context in that field! What's next for Fragments Most importantly, we'll be working on this in our free time to get a beta version out to early users! Here are a few features we'd like to add: add quick video editing tools to crop and trim clips before saving introduce an algorithmic feed of recommendations with two sections: a "for you" page, and a following page add collaborative Collections, letting friends and teams build shared libraries of inspiration together convert WebM files to WebP on top of GIF + add lazy loading for quicker load times <div