---
slug: "pull-the-pitcher"
url: "https://devpost.com/software/pull-the-pitcher"
title: "MLB Pitcher Mechanics Scorecard"
hackathon: "Google Cloud x MLB(TM) Hackathon – Building with Gemini Models"
organization: "Google"
winner: true
words: 841
team_size: 1
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/benchmark_measured"
  - "mechanism/realtime_stream"
  - "mechanism/vision_ocr"
  - "user/researcher"
  - "substrate/video_visual"
---

# MLB Pitcher Mechanics Scorecard

> Should the manager pull the pitcher? Let's find out. With machine learning and computer vision we evaluate each pitch to see if a pitcher is ready to be pulled!

[Devpost](https://devpost.com/software/pull-the-pitcher) · hackathon [[Google Cloud x MLB-TM- Hackathon - Building with Gemini Models]]

## Facets

**mechanism** [[benchmark_measured]] [[realtime_stream]] [[vision_ocr]]
**user** [[researcher]]
**substrate** [[video_visual]]

**stack** google-cloud, python, vertex-ai

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for pull the pitcher

## Body

Zach Wheeler 2021 Slider Analysis Clayton Kershaw 2022 "Almost Perfect" Game Slider Analysis Inspiration As a former college shot putter, I was always taught to focus on key mechanical cues—leg drive, hip drive, balance—rather than just outcomes. However, when watching Major League Baseball, I noticed that most overlays and analyses focus on pitch velocity and other results rather than the mechanics that produce them. This got me thinking: what if we could shift the focus from outputs to inputs? I wanted to create a tool that could analyze pitcher mechanics in real-time, helping coaches and analysts make more informed decisions about performance, fatigue, and mechanical consistency. What it does Pitcher Scorecard is an AI-powered tool that analyzes baseball pitcher mechanics using Vertex AI’s Gemini Pro Vision model. Unlike traditional single-frame analysis, it evaluates an entire pitching motion to detect mechanical deviations, fatigue, and consistency. The system leverages MLB data to build ideal pitcher profiles by incorporating historical performance, biomechanical benchmarks, and pitch-specific mechanics. These profiles define the optimal form for each pitcher and pitch type, allowing the AI to compare video clips against an established baseline. By processing multiple frames simultaneously, Pitcher Scorecard provides real-time, context-aware insights, helping coaches and analysts refine mechanics and make informed decisions. How we built it To bring this idea to life, I leveraged Vertex AI’s Gemini Pro Vision model for multi-frame processing, allowing for a more holistic analysis of a pitcher’s motion. The process included several key steps: 1. Video Processing – I uploaded pitching clips to Google Cloud, trimmed them to isolate the pitch sequence, and extracted key frames. 2. AI-Powered Analysis – Using Vertex AI, I prompted the model to evaluate the extracted frames as a pitching coach, identifying key mechanical features like arm slot, leg drive, and balance. 3. Overlay Generation – The AI-generated analysis was overlaid onto the video, providing a pitcher score and identifying deviations from ideal mechanics calibrated from MLB player profiles and game situations. 4. Iterating on Feedback – I tested my model using Clayton Kershaw’s near-perfect game in 2022 to determine if fatigue played a role in the decision to pull him from the game. Challenges we ran into One of the biggest challenges was quantifying fatigue and mechanical breakdown in a way that made sense to users. Early iterations of the model produced number-based fatigue scores, but these were often unclear—what does a “4 out of 10 arm” really mean? Through feedback, I learned that comparing a pitcher’s form to their ideal mechanics was a much clearer and more actionable insight than assigning an arbitrary fatigue score. Accomplishments that we're proud of When I applied my model to Zack Wheeler’s slider, a pitch widely recognized as elite, the analysis correctly identified it as mechanically sound without any adjustments needed (besides Wheeler's player ID and Game ID). This real-world testing helped confirm that the system could differentiate between ideal mechanics and subtle breakdowns. What we learned Using this approach, I analyzed Clayton Kershaw’s final pitches in his 2022 near-perfect game. My model suggested that while there were some signs of fatigue, his mechanics were still strong, making the decision to pull him more of a strategic choice rather than a mechanical necessity. Ultimately, Pitcher Scorecard demonstrates how AI can go beyond simple outcome-based analysis to provide deeper insights into pitcher mechanics. By leveraging multi-frame processing with Vertex AI, this system offers a real-time, context-aware approach to evaluating pitcher performance, potentially transforming how coaches and analysts assess fatigue, consistency, and mechanical efficiency. What's next for Pull the Pitcher With the foundation of Pitcher Scorecard in place, the next step is refining and expanding its capabilities to make it an even more powerful tool for pitchers, coaches, and analysts. One key focus is collaborating with coaches and sports medicine experts to better identify critical mechanics that impact performance and injury risk. By integrating expert knowledge, we can fine-tune the AI’s ability to detect subtle mechanical breakdowns that might not be obvious to the naked eye but are crucial for maintaining consistency and preventing fatigue-related injuries. Another major improvement is optimizing Vertex AI for baseball-specific image analysis. Right now, the model processes frames based on general vision capabilities. By refining its training to focus on pitching-specific movement patterns, such as release point stability, arm slot changes, and stride consistency, we can enhance its accuracy and ensure that its insights align with real-world pitching mechanics. Finally, real-time trend tracking is a crucial next step. Instead of analyzing just isolated pitches, the system will monitor mechanical trends over the course of a game. For example, if a pitcher’s arm slot has been dropping for the last four pitches, the AI can flag this as a potential fatigue or mechanical breakdown issue, allowing coaches to intervene before performance declines or injury risk increases. By continuing to refine the model, incorporating expert input, and expanding real-time tracking capabilities, Pitcher Scorecard has the potential to become a game-changing tool for baseball, helping pitchers stay healthy, improve performance, and make data-driven adjustments on the fly. <div