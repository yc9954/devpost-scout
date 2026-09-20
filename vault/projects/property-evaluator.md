---
slug: "property-evaluator"
url: "https://devpost.com/software/property-evaluator"
title: "EcoLens"
hackathon: "HackUTD 2024: Ripple Effect"
organization: "hackutd"
winner: true
words: 401
team_size: 4
has_repo: false
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "mechanism/sensor_fusion"
  - "mechanism/vision_ocr"
  - "domain/developer_tools"
  - "substrate/sensor_telemetry"
  - "substrate/structured_db"
  - "substrate/video_visual"
---

# EcoLens

> EcoLens helps property managers create sustainable spaces by analyzing room videos to provide eco-friendly suggestions and improve energy efficiency—saving costs and reducing carbon impact.

[Devpost](https://devpost.com/software/property-evaluator) · hackathon [[HackUTD 2024- Ripple Effect]]

## Facets

**mechanism** [[realtime_stream]] [[sensor_fusion]] [[vision_ocr]]
**domain** [[developer_tools]]
**substrate** [[sensor_telemetry]] [[structured_db]] [[video_visual]]

**stack** googlevisionapi, llama, python, swift

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for ecolens

## Body

Inspiration Introducing sustainability within offices and other properties is crucial to reduce operational costs while minimizing environmental impact. We wanted to develop a solution that optimized resource usage by prioritizing repair and maintenance over frequent replacements. What it does Our app allows users to upload a video of a space and analyzes the video to detect and classify furniture and assess their condition. It highlights specific signs of wear and tear, including rips or stains, and provides suggestions to sustainably manage and repair any issues. How we built it We built EcoLense using Swift for the frontend to create a smooth, user-friendly interface. The backend integrates advanced APIs for video frame analysis and object detection. Video frames are extracted and securely uploaded to cloud storage services like Pinata. We used the Google Vision API to identify and label furniture in the video frames and LLMs for contextual analysis, delivering tailored sustainability insights. The seamless connection between the frontend and backend ensures accurate data processing and real-time results. This tech stack ensures a robust, scalable, and efficient platform for users. Challenges we ran into We faced challenges integrating various APIs, including compatibility issues with Google Cloud and handling the serialization of JSON data. Incorporating Llama for contextual analysis also required fine-tuning and troubleshooting. Ensuring seamless communication between services was a complex process, but we resolved these issues through iterative debugging and testing. Accomplishments that we're proud of We are super proud of learning multiple new technologies throughout the experience, including the Pinata database management system, Google Cloud Vision API, and Llama text to text and image to text models. We are also proud of our collective effort collaborating as a team in order to integrate multiple features within our app. What we learned We learned how to work with a comprehensive tech stack, including Swift for the frontend, backend integration, and API handling. We gained valuable experience with video processing, object detection using AI, and integrating tools like Llama for contextual analysis. Time management and effective teamwork were crucial as we balanced multiple tasks, debugged issues, and iteratively improved the app. These lessons strengthened our technical and collaboration skills. What's next for EcoLens Next steps for EcoLens include incorporating real time metrics to track conditions as they change for on the spot evaluations. We also would like to include IoT sensors for live tracking of furniture usage and condition over time. <div