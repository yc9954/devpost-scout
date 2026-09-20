---
slug: "video-upscaler"
url: "https://devpost.com/software/video-upscaler"
title: "Video Upscaler"
hackathon: "Canva AI and Integrations Hackathon"
organization: "Canva"
winner: true
words: 512
team_size: 2
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "domain/developer_tools"
  - "substrate/video_visual"
---

# Video Upscaler

> Convert low-quality videos into stunning HD or 4K with AI. Enhance resolution, restore details, reduce noise, and correct colors—ideal for both personal and professional content creation.

[Devpost](https://devpost.com/software/video-upscaler) · hackathon [[Canva AI and Integrations Hackathon]]

## Facets

**mechanism** [[realtime_stream]]
**domain** [[developer_tools]]
**substrate** [[video_visual]]

**stack** amazon-cloudfront-cdn, amazon-cloudwatch, amazon-dynamodb, amazon-lambda, amazon-sqs, amazon-web-services, canva, gan, vsr, websocket

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for video upscaler

## Body

App feature image 1 App feature image 2 Screenshot for the App We are a small US team called AIGC Hacker House, and we saw an opportunity to expand upon the common AI image upscaling technology to videos in Canva. Inspiration 🎥 Rise of low-quality videos : AI-generated content, Older footage, and social media compression. 📈 Need for high-quality content : Increasing demand for HD and 4K videos across online platforms. 💡 Opportunity : Extend the concept of AI image upscaling to video, empowering creators to elevate their content. What it does 🛠️ Video Upscaling : Transforms low-resolution videos into HD or 4K. ✨ Enhancements : Restores details, reduces noise, and corrects colors. 🖥️ Seamless Integration : Built on Canva’s SDK for easy use within the Canva platform. 📈 Use Cases : Ideal for both personal and professional content creation. How we built it 🖇️ Tech Stack : AWS Lambda for scalable, serverless backend. WebSocket API for real-time processing feedback. Cloudfront CDN for fast global file transfer. 🎛️ AI Models : Tailored for different content types (Portrait, Landscape, Anime and General); based on VSR techniques and GAN networks. ⚙️ Canva SDK : Deep integration for a smooth user experience. Used cache to make the waiting less painful. Challenges we ran into 🛠️ Real-time Feedback : Integrating real-time progress updates since the wait for loading can be long. 🎞️ Model Optimization : Ensuring efficiency across various video content and resolutions since no single model does perfect job for all. 🌐 Scalability : Handling large video files for Canva's global user base. 🤑 Cost : running GPU jobs for video are way more expensive than images for small teams like us, so we have to limit the size and duration of videos. As for using Canva SDK 🚨 API Error : The video selection API is still not working so well for us after couple posts on forum. 🎛️ Preview Panel Limitation : The video preview panel lacks before-and-after comparison functionality, requiring our custom implementation with support for both light and dark themes. 📊 Tracking Limitation : Third-party JS (e.g. GA) and event tracking are not supported, so we build our a custom API specifically for tracking user behavior events. Accomplishments that we're proud of 🚀 Successful Integration : Smooth integration with Canva’s ecosystem and quickly get it released to public. 🎥 High-Quality Upscaling Production : Built and served in production with scalable architecture for Canva's global users 💻 Innovative AI Use : Effective application of AI models across diverse content types. What we learned 🤖 AI & Video Processing : In-depth knowledge of AI’s potential in video enhancement. 🔄 Serverless Optimization : Efficient handling of intensive tasks in a scalable, serverless environment. 🛠️ SDK Mastery : Leveraged Canva’s SDK to build a user-centric, high-performance app. What's next for Video Upscaler 🔧 Feature Expansion : Support for more formats and longer videos. But that's more of a cost issue. 🚀 AI Model Refinement : Enhance processing speed and output quality. 🆕 Advanced Features : Exploring video stabilization and style transfer for future updates. <div