---
slug: "remixify"
url: "https://devpost.com/software/remixify"
title: "Remixify"
hackathon: "Cal Hacks 12.0"
organization: "Cal Hacks"
winner: true
words: 939
team_size: 3
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "user/general_public"
  - "substrate/geospatial"
  - "substrate/sensor_telemetry"
  - "substrate/structured_db"
  - "substrate/video_visual"
---

# Remixify

> Don't scroll Reels, scroll Remixify.

[Devpost](https://devpost.com/software/remixify) · hackathon [[Cal Hacks 12.0]]

## Facets

**mechanism** [[realtime_stream]]
**user** [[general_public]]
**substrate** [[geospatial]] [[sensor_telemetry]] [[structured_db]] [[video_visual]]

**stack** claude, css, gemini, javascript, letta, python, supabase, typescript, veo3

## How they structured the write-up

- ✨ inspiration
- what it does
- 🛠️ how we built it
- 🧗 challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for remixify

## Body

landing brand dashboard leaderboard dubai chocolate ad edited with Gemini Burger King video Ad with Google's Veo3 ✨ Inspiration Remixify revolutionizes the way users interact with companies to create a better and more engaging experience for viewers. Remixify was inspired by the growing need for brands to create more engaging, personalized, and data-driven advertising content. We also thought it'd be really funny to edit videos and images with AI for people to explore their creativity and have fun collaborating together. The main idea for our app is that: Advertisers rarely know what consumers wish their ads looked like or what made their ad so viral beyond surface-level metrics Creative users, especially young creators, want a way to express themselves, win rewards, and actually be heard by the brands they engage with. Remixify creates a platform where creativity and product discovery meet. What it does Remixify is an innovative platform that transforms traditional advertising into an interactive, fun, community-driven experience. Users can also scroll a feed of real ads and remix them using advanced AI image and video generation ( fully Gemini powered! ), with style presets and creative prompts, for example, “Add a cat mascot” or “turn the sky to night”. User can share, earn likes, comments & win brand-sponsored rewards based on the remixes they make. Users can also upload an image, and we use Gemini to label and tag the company automatically. Remixify then provides real-time insights into ad performance, audience engagement, and creative trends using Letta's Deep Research Agents to extract insights from every remix + interaction, and memory blocks that accumulate key information such as: Most remixed ad elements and which remixes improve engagement or virality And organize all this information into an Analytics page, so companies finally see what people actually want, including specific information about demographics, top aesthetics, and more. Finally, we help predict ad performance through Signal Extraction. We built a model to analyze user behavior (prompts summarized by Claude ), commenting patterns, and performance metrics to provide actionable insights for the company. For example, we extract context clues like references to TikTok, Instagram, or specific trends to see platforms that users are most active on to target ad spend. 🛠️ How We Built It Tech stack: Frontend: Next.js for the web application framework Tailwind CSS for styling Shadcn UI components for a modern, accessible interface TypeScript Backend & AI: Supabase for database and authentication Custom API routes for handling image generation and analysis Integration with Google's Gemini API extensively for image editing (Nano Banana 🍌) Integration with Google’s Veo3 for video editing Real-time data processing for analytics and signal extraction Analytics: Custom analytics engine ( Letta ) for user insights and analytics Claude for creative insights and trend analysis Real-time performance metrics and behavioral pattern recognition Opportunities for Conversion integration to automatically reach out to leads. Letta Deep Research Agents Integration: We use Letta’s agents and their Memory Blocks to track: Most remixed ad elements Popular user modifications Letta Deep Research Agents extract overall sentiments and advice, helping brands understand how users feel about the brand as a whole Which remixes improve engagement or virality 🧗 Challenges We Ran Into Real-time Video and Image Generation: Implementing fast and reliable AI-powered image generation while maintaining quality and brand consistency. Although calling the API for video generation was not that difficult, it was very hard to get it to maintain the same theme as the original video as well as ensure that the generation didn't take too long. Performance Optimization: Handling large-scale data processing for analytics while maintaining a responsive UI. Making the comments hierarchical so people's edits could affect each other was a little bit difficult since we had to handle storing data in Supabase and pulling it very quickly in order to apply different comments. Data Analysis: Building Letta Agents with Deep Research and Memory Blocks to extract meaningful signals from user behavior and ad performance, not just noise. Overall, we coordinating multiple AI services and ensuring seamless communication between frontend and backend was pretty difficult but we got it to work. Accomplishments that we're proud of Built a sophisticated AI-powered creative platform in a short timeframe Created an intuitive and engaging user interface for complex features and a full-fledged social platform. Implemented advanced analytics with real-time analysis. Successfully integrated multiple AI models for different aspects of the platform in a way that is invisible but still valuable to the user. What we learned We learned more about real-time Analytics, especially how to process and visualize large amounts of data efficiently. We also focused a lot on user experience and design, and discovered how to make complex features accessible to users in a way that was easy to understand. Prompt engineering is critical: Specificity, tone, and structure determine the output, especially for the video models. Design matters: We spent time creating chat panes, responsive cards, and leaderboards, all small things that made the platform intuitive and engaging. What's next for Remixify Our main idea is to expand from just ads and provide a platform where users can remix and create funny videos and photos, but also maintain this idea of campaigns, where companies can incentivize users to remix their specific ads by providing prizes. We also want: Bettter Analytics: more detailed audience segmentation and possibly suggestions for the company to figure out where/who to market to, or creating marketing assets just from these analytics. Expansion into mobile app form to better reflect TikTok or Instagram feeds, as well as API access for third-party integrations (ex: Download video of a TikTok and remix that), support for more ad formats and platforms <div