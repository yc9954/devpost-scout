---
slug: "smart-dance"
url: "https://devpost.com/software/smart-dance"
title: "Smart Dance"
hackathon: "Hack the North 2021"
organization: "Techyon"
winner: true
words: 473
team_size: 3
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "mechanism/vision_ocr"
  - "user/developer"
  - "substrate/geospatial"
  - "substrate/sensor_telemetry"
  - "substrate/web_dom"
---

# Smart Dance

> Can you dance as well as Addison Rae? Let's find out!

[Devpost](https://devpost.com/software/smart-dance) · hackathon [[Hack the North 2021]]

## Facets

**mechanism** [[realtime_stream]] [[vision_ocr]]
**user** [[developer]]
**substrate** [[geospatial]] [[sensor_telemetry]] [[web_dom]]

**stack** bootsrap, css, flask, html, mediapipe, mongodb, opencv

## How they structured the write-up

- inspiration 💭
- what it does 👀
- how we built it 💡
- challenges we ran into 🌋
- what we learned 🤠
- what's next for smart dance 🚀

## Body

Login screen showing the pose estimation technology we used. Home page. Choose from one of the trending dances. Start Dancing! Follow the blue lines. Inspiration 💭 We have always been fascinated with the rise of popular dances springing from TikTok and other parts of the internet. They inform a lot of our modern culture and unite everyone through a language as old and gold as any, dancing. The obvious question we had to ask ourselves is what would it take to use our skills as programmers to contribute to this culture of our generation. So we set out to answer the question: Can you dance as well as Addison Rae? What it does 👀 Smart Dance uses pose estimation to store the key points of dances from popular dance videos and use those poses to guide the user on how to move their body to do the dance. Through our intuitive UI, users can find trending dances and learn or assess how well they're dancing when compared to their friends or internet stars that also do these dances. The score function we've made allows users to determine whether their pose is similar or different to the videos they are dancing along with. This makes dancing (and learning to dance) much more engaging as well as opens the door to the gamification of dancing with real-time feedback and encouragement (much like how the classic dance arcade games used to work). The only difference is our solution is not just enjoyable but is portable, easy to play and can be integrated with a lot more going forward! How we built it 💡 Smart-Dance uses Python on the backend, Mediapipe for real time pose estimation on CPUs and GPUs paired with OpenCV, as well as Flask, HTML / CSS, and MongoDB for the frontend-backend-integration. Challenges we ran into 🌋 Some challenges we ran into included calibrating the TikTok dances to the user's position. After wracking our brains for a while and doing some linear algebra, we came up with a mechanism to transform the coordinates of the poses so the keypoints of the dancer the user is following is where the user's pose is within frame. Another challenge was constructing a metric to compare the two poses in a meaningful manner and we discovered that l2_normalization was a very effective way of doing this comparison (we also explored using dynamic time warping matching as a metric and believe there is potential in applying this in the future). What we learned 🤠 How to perform computer vision analysis on the web through a user's webcam. What's next for Smart Dance 🚀 A lot of dances are paired with famous songs. Although users can certainly play these songs themselves right now, we hope to synchronize the dances and the displayed pose to the appropriate music going forward. <div