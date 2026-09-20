---
slug: "trustybite"
url: "https://devpost.com/software/trustybite"
title: "TrustyBite"
hackathon: "[REDACTED] Hackathon"
organization: "NEAR Protocol"
winner: true
words: 651
team_size: 4
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "mechanism/sensor_fusion"
  - "mechanism/structural_withholding"
  - "mechanism/vision_ocr"
  - "substrate/sensor_telemetry"
  - "substrate/video_visual"
---

# TrustyBite

> Transparency you can trust. Our on-site devices capture sensor data and computer vision insights, secured on blockchain to verify cleanliness and food freshness. Trust what you see with TrustyBite.

[Devpost](https://devpost.com/software/trustybite) · hackathon [[-REDACTED- Hackathon]]

## Facets

**mechanism** [[realtime_stream]] [[sensor_fusion]] [[structural_withholding]] [[vision_ocr]]
**substrate** [[sensor_telemetry]] [[video_visual]]

**stack** arduino, c, javascript, near, nextjs, node.js, raspberry-pi, react, typescript

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for trustybite

## Body

screenshot of the web application register first restaurant : veggiehaven TrustyBite Activity diagram Inspiration TrustyBite started with a personal frustration. My family and I love exploring new restaurants and cuisines, but too often, we found ourselves feeling unwell after eating out. As much as we wanted to verify a restaurant’s hygiene and freshness standards, it wasn’t practical to request a kitchen tour every time. This left us relying on generic online reviews, which rarely provided the reassurance we needed. That’s when I began to think: what if diners could access real-time data on a restaurant’s cleanliness and freshness, backed by something unchangeable and secure? Blockchain technology stood out as the perfect solution for transparency and trust. When my team and I spotted the opportunity to bring this idea to life at the [REDACTED] Hackathon, we took the leap. What it does Our MVP for TrustyBite integrates IoT and blockchain to provide a robust food safety solution. We used Raspberry Pi devices equipped with MQ-series gas sensors to monitor conditions related to food spoilage , like temperature and humidity. We also began training computer vision algorithms to recognize hygiene practices , such as proper handwashing and workspace cleanliness, in real time. These devices, complete with sensors and a camera, are installed in participating restaurants. Each device registers on the TrustyBite platform with a unique private key, allowing it to kick off continuous, real-time monitoring that users can access. In addition to the freshness monitoring, we created a blockchain-backed review system where user reviews are permanently stored, further building transparency and accountability. To make TrustyBite seamless for users, we implemented account abstraction and a relayer, meaning users don’t need to create a wallet to leave reviews or book tables. This ensures easy access for everyone. How we built it During the development of TrustyBite, we dove into creating and deploying smart contracts on the NEAR testnet, which was a fantastic learning experience for us. We focused on designing a version of the project that would help us gather the right data for our use case and made sure to conduct thorough unit testing. While we were getting the hardware up and running, we also worked on building the web application, aiming to create a smooth user experience. We chose Next.js for its seamless integration with NEAR Web3 APIs, which helped us connect everything together effectively. Balancing both the hardware and software sides of the project was a challenge, but it was rewarding to see our ideas come to life! Challenges we ran into Our main challenges included training the AI to accurately detect hygiene practices, working within the time constraints, and navigating the limited research available on IoT-based food spoilage detection. Despite these hurdles, we developed a working MVP that validates our concept and sets the foundation for future growth. Accomplishments that we're proud of We’re proud to have built a working first version of TrustyBite that runs at home, providing real-time sensor data integrated with the NEAR blockchain. Additionally, we’re thrilled to have launched our web app, trustybite.com, live on the NEAR testnet, making it accessible for users to explore our platform’s capabilities. What we learned Working on TrustyBite was a rewarding experience, particularly given the intense one-month timeline. We gained hands-on experience with integrating the NEAR blockchain into our web application and learned to use relayer and account abstraction protocols to streamline the process. Coordinating entirely online was another valuable lesson, as it required precise communication across our team’s various specialties. What's next for TrustyBite Next, we’ll focus on enhancing the AI components to detect cleanliness practices and refine our food spoilage metrics. We’ll also implement email authentication, onboard new users, and initiate a targeted marketing campaign to kickstart a test phase with real restaurants. Looking ahead, we’re excited to develop the TrustyBite AI Assistant, which will recommend and book restaurants based on users’ dining preferences and verified hygiene data. <div