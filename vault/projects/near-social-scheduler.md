---
slug: "near-social-scheduler"
url: "https://devpost.com/software/near-social-scheduler"
title: "NEAR AI Social Scheduler"
hackathon: "One Trillion Agents Hackathon"
organization: "NEAR Protocol"
winner: true
words: 403
team_size: 1
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/provenance_signing"
---

# NEAR AI Social Scheduler

> Gathers social media content, using NEAR AI to customize, translate, edit, and schedule posts.Great for groups to catch up on crypto news and research in a personalized, accessible way

[Devpost](https://devpost.com/software/near-social-scheduler) · hackathon [[One Trillion Agents Hackathon]]

## Facets

**mechanism** [[provenance_signing]]

**stack** near, nearai, node.js

## How they structured the write-up

- inspiration
- what it does
- how it works
- accomplishments we're proud of
- what we learned
- what's next for near ai social scheduler

## Body

NEARAI Social Scheduler source channels screen Create Post and scheduled post screen setting screen Distribution channels screen the bot in action: Translate and post news from many source channels into Vietnamese Inspiration I've been running local communities on NEAR for a long time and noticed that many members struggle with English, making it hard for them to access important information. To solve this, we need to localize and translate content—making it more engaging and accessible for everyone. However, this process is often slow and time-consuming. With NEAR AI infrastructure, we can automate and customize this process for local communities, allowing them to quickly access new information without language barriers. This saves both time and effort! What it does Our system lets users pull content from various social media sources—like Telegram channels—and use AI inference powered by NEAR AI to process and customize it. The content is then automatically scheduled for posting to their chosen distribution channels. How it works 1. Authentication: Users authenticate with their NEAR wallet. The system verifies their signature and identity via the NEAR blockchain, creating a secure JWT session token. 2. Subscribe to Content Sources: Users set up content sources, like popular Telegram channels, to monitor. For each source, users can customize: Translation preferences (auto-translate or custom prompts): Powered by NEAR AI, users can fine-tune translation outputs with custom prompts. Posting schedule frequency: By default, content is fetched every 30 minutes. 3. Set Up Distribution Channels: Users add their destination channels, such as personal or group Telegram channels, where they want to post content. 4. Content Processing: The system automatically: Fetches new content from subscribed sources Translates and modifies content using NEAR AI, following user prompts 5. Post Management: Users can: View scheduled and upcoming posts Manually create scheduled posts for their channels Delete unsent posts 6. Automated Publishing: The scheduler publishes content to users’ distribution channels according to their set schedule. Accomplishments we're proud of We built a fully functional system that's ready to use! We're excited about how it can help users and groups easily access information in their language with a high level of customization and localization. No more language barriers! What we learned NEAR provides a powerful AI infrastructure that enabled us to build this system efficiently. What's next for NEAR AI Social Scheduler Support additional content sources beyond Telegram, like X and Medium Add more customization options and improvements based on user feedback <div