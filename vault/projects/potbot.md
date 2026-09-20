---
slug: "potbot"
url: "https://devpost.com/software/potbot"
title: "PotBot"
hackathon: "Cal Hacks 12.0"
organization: "Cal Hacks"
winner: true
words: 309
team_size: 4
has_repo: false
has_live: false
has_video: true
tags:
  - "project"
  - "domain/civic_government"
  - "substrate/video_visual"
---

# PotBot

> Turning one photo into civic action

[Devpost](https://devpost.com/software/potbot) · hackathon [[Cal Hacks 12.0]]

## Facets

  <sub>weak: vision_ocr</sub>
**domain** [[civic_government]]
  <sub>weak: developer_tools</sub>
**substrate** [[video_visual]]
  <sub>weak: geospatial, structured_db</sub>

**stack** brightdata, fastapi, groq, javascript, nextjs, playwright, python, react, supabase, twitter

## Body

Why not make it as easy as taking a photo to get these issues noticed and fixed? Our project turns one simple photo into action. When someone uploads a picture, the system detects what kind of problem it is, like a pothole, graffiti, or fallen tree, figures out where it is using location data, and automatically files a fix request. Then it goes a step further by creating a social media post that helps bring public attention to the issue. We built the system using FastAPI for the backend that processes images, a Java-based service to handle location and tracking details, and a Supabase database to store everything. For detecting issues, we trained a computer vision model that recognizes different types of city damage. We connected everything through Supabase Edge Functions so that once the issue is identified, a short post gets created and published directly to Twitter using the Twitter API. It’s a simple flow that connects AI, data, and social media in a meaningful way — one photo turns into awareness and, hopefully, a solution. Setting it up wasn’t easy. We ran into problems making all the APIs talk to each other, and getting the serverless functions to run smoothly took a lot of debugging. Twitter’s API had its own limits, and we had to find workarounds for posting. But by the end, we had a system that could take a real photo of a city issue, identify it correctly, generate a fix request, and post about it online in just seconds. We’re proud that it actually works and that it can make a difference. The idea is simple but powerful — giving people the ability to improve their city with just one photo. It’s not just about automation; it’s about awareness and civic action, using technology to make communities better, one post at a time. <div