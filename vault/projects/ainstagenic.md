---
slug: "ainstagenic"
url: "https://devpost.com/software/ainstagenic"
title: "aInstagenic"
hackathon: "Azure AI Hackathon"
organization: "Microsoft"
winner: true
words: 327
team_size: 1
has_repo: false
has_live: false
has_video: true
tags:
  - "project"
  - "user/general_public"
  - "substrate/structured_db"
  - "substrate/video_visual"
---

# aInstagenic

> On Instagram, there’s no room for “good enough” shots. Time to level up using AI.

[Devpost](https://devpost.com/software/ainstagenic) · hackathon [[Azure AI Hackathon]]

## Facets

**user** [[general_public]]
**substrate** [[structured_db]] [[video_visual]]

**stack** azure, bash, cognitive, instagram, instaloader, python, streamlit

## How they structured the write-up

- inspiration
- what it does
- how i built it
- challenges we ran into
- what we learned
- what's next for ainstagenic

## Body

Inspiration The conception of aInstagenic is driven by personal experience. A few weeks back, I wanted to post something on Instagram but there were many contenders in my Gallery awaiting to make it to my timeline. For someone who is trying to up his Insta game, this is a stressful situation. Can't I have a way to estimate the likability of these images and post the one which aligns best with my audience? This problem is very critical for branding and marketing experts who are constantly involved in customer engagement through social media. What it does aInstagenuc is a web application which rates your images by learning the relationship between an image's visual characteristics and the likings pattern of the general Instagram audience. How I built it Step 1: Crawled Instagram to download 8000+ public images and their likes using Instaloader . These images were corresponding to some set of pre-defined hashtags like photoshoot, selfie, etc. Step 2: Used Azure's Face Cognitive service to only select images that contained faces. Step 3: Used histogram analysis to bucket the number of likes to 5 buckets. Step 4: Uploaded the curated dataset on Azure's Custom Vision and train it. Step 5: Using streamlit , created the web application. Challenges we ran into One of the biggest challenges was dataset curation and cleansing. People tend to post anything and everything on Instagram and associate irrelevant hashtags to boosts the post's likes and reach. This motivated me to only consider images that had faces. What we learned Discovery of some inherent biases prevalent in society reflected in the likes on the public posts on Instagram, primarily weight, age and race. What's next for aInstagenic The following can be some of the interesting problems to tackle: Instead of just considering the image's visual characteristics, consider caption and hashtags too to predict a rating. Suggest image filters that could help boost an image's activity. Recommend hashtags based on visual characteristics and popularity. <div