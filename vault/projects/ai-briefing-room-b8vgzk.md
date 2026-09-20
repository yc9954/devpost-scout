---
slug: "ai-briefing-room-b8vgzk"
url: "https://devpost.com/software/ai-briefing-room-b8vgzk"
title: "AI Briefing Room"
hackathon: "Microsoft Generative AI Hackathon"
organization: "Microsoft"
winner: true
words: 487
team_size: 5
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/voice_speech"
---

# AI Briefing Room

> Bridge the gap between complex tech news and everyday understanding! We transform the most essential tech news into neat trilingual podcasts. Join our community of 1000+ listeners spanning 10 nations!

[Devpost](https://devpost.com/software/ai-briefing-room-b8vgzk) · hackathon [[Microsoft Generative AI Hackathon]]

## Facets

**mechanism** [[voice_speech]]

**stack** azure, azure-ai, azure-openai-chat-completion, azure-openai-text-to-speech, copilot, microsoft, python, selenium

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments we're proud of
- what we learned
- what's next for ai briefing room

## Body

Design Diagram English Podcast on Spotify and sample auto-generated titles Spanish Podcast on Spotify Chinese Podcast on Spotify Sample auto-generated podcast description on Apple podcast Sample Newsletter Inspiration Our quest for a succinct yet substantive tech news source was the seed for AI Briefing Room. The existing sources were either too verbose or misaligned with our interests. We aimed to craft a solution that was just right. What it Does AI Briefing Room offers two-minute podcast summaries of today’s tech news, meticulously curated by AI. We sift through numerous sources to bring you the top five tech stories that matter most, ensuring you stay informed quickly and efficiently. How We Built It Data Gathering: We start by collecting the day's headlines from major tech news websites. Content Selection: Using advanced prompt engineering, we identify the five most compelling stories based on criteria like frequency, importance, and relevance. Content Aggregation: We retrieve detailed reports for these top stories by sourcing the original articles. Script Generation: A one-shot prompt engineering technique helps us craft the podcast script, title, and description, ensuring the style is consistent and engaging. Audio Production: The script is then converted into audio using text-to-speech. The background music is dynamically cut—fixed at the beginning and end, looped in the middle, and the volume is lowered during the narration—to match the podcast's length perfectly. Distribution: We automate the upload of the podcast using a Selenium script to Anchor for consistent daily updates, Newsletter: We distribute a curated newsletter to provide additional insights and news summaries directly to our subscribers’ inboxes. Language Support: We repeat the whole process for English, Chinese, and Spanish versions. Automation: The entire process runs on a virtual machine to ensure new episodes are available daily without manual intervention. Challenges We Ran Into We encountered numerous obstacles, one of the main ones being the inconsistency in the output of our generative models. We leveraged one-shot prompting to refine and guide the content style effectively. We've repeatedly fine-tune using prompt engineering to ensure interesting and concise news being delievered. Accomplishments We're Proud Of Our project quickly resonated, attracting over 1000 listeners in the first week alone—a testament to the demand for concise, relevant tech news. Furthermore, we have a median retention rate of 100%, which means more than 50% of users(70% according to our data), has listened completely from start to end. Furthermore, The inclusion of multiple languages fostered greater community impact by making technology news accessible to a diverse audience from different cultural backgrounds. What We Learned The project was a deep dive into several technologies and processes including Selenium, text-to-speech synthesis, chat completions, and the podcasting ecosystem. Most importantly, we discovered the capabilities and benefits of Azure’s OpenAI service. What's Next for AI Briefing Room Looking ahead, we might expand our offerings beyond just tech news, exploring additional sectors and themes to bring a wider array of important news to our audience. <div