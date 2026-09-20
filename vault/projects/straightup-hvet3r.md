---
slug: "straightup-hvet3r"
url: "https://devpost.com/software/straightup-hvet3r"
title: "iMPOSTURE"
hackathon: "ShellHacks 2025"
organization: "init"
winner: true
words: 514
team_size: 4
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "mechanism/vision_ocr"
  - "domain/developer_tools"
  - "domain/education"
  - "domain/mental_health"
  - "user/educator_student"
  - "substrate/video_visual"
---

# iMPOSTURE

> AI powered ergonomic for healthier minds and bodies

[Devpost](https://devpost.com/software/straightup-hvet3r) · hackathon [[ShellHacks 2025]]

## Facets

**mechanism** [[realtime_stream]] [[vision_ocr]]
**domain** [[developer_tools]] [[education]] [[mental_health]]
**user** [[educator_student]]
**substrate** [[video_visual]]

**stack** google-adk, google-cloud, mediapipe, python, supabase, uv, yolov11

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for imposture

## Body

MediaPipe Powered Posture Detection Wellness Dashboard with Workspace Session Timer Phone/Distraction Detection ADK Powered Wellness Insight Flow Inspiration According to the National Institutes of Health more than 80% of Americans have experienced poor posture-related issues at some point in their lives. We noticed how students and professionals especially in the software engineering industry often spend long hours sitting in front of screens, leading to poor posture, eye strain, and decreased productivity. With wellness tools either too complicated or not engaging, we wanted to create something simple, accessible, and proactive. That’s how iMPOSTURE was born, an AI-powered posture coach designed to improve well-being in both classrooms and workplaces. What it does Uses AI-powered camera features to detect bad posture in real time. Warns you when your posture starts to slump. Logs distractions and posture trends over time. Leverages Google ADK to process raw posture and distraction data into personalized health scores, insights, and tips. Provides a wellness dashboard to track your overall focus and posture health. Dims laptop brightness during prolonged distraction to save battery life. The result: a tool that not only helps you sit straighter but also builds healthier habits and boosts productivity. How we built it Frontend: A Python-based Windows desktop app that serves as the user dashboard, displaying posture alerts, distraction logs, wellness scores, and tips. AI & Vision: MediaPipe and YOLO models track posture and detect phone usage/distractions in real time. Data Processing: Google ADK processes raw posture and distraction data from system logs and feeds it directly into the dashboard. User Accounts: Supabase is used to create and securely store user accounts. Integration: Camera input is analyzed by the AI models, logged through ADK, and surfaced instantly on the Windows app for user feedback. Challenges we ran into Getting posture detection accurate across different body types and lighting conditions. Balancing real-time performance with AI inference speed. Designing a dashboard that was both intuitive and engaging for users. Debugging cross-platform issues with camera access and model compatibility. Accomplishments that we're proud of Building a full end-to-end system (camera → AI detection → dashboard → wellness insights) within the hackathon timeframe. Achieving smooth real-time detection with clear posture feedback. Creating a solution that works in both student and corporate environments. Seeing our idea resonate with people who immediately said, “I need this!” What we learned How to integrate AI computer vision models into a real-time wellness app. How to connect external data streams (like Google ADK) with our system for richer insights. The importance of user experience — wellness tech must be non-intrusive but effective. How small design choices (like alert timing or dashboard layout) impact engagement and adoption. Teamwork and rapid prototyping under time pressure. What's next for iMPOSTURE Expanding the wellness dashboard with detailed analytics and personalized posture improvement plans. Adding gamification/rewards to encourage healthy habits. Expanding on mood detection to remind users to take breaks and avoid burnout. Building a mobile app version for portability. Integrating with corporate wellness programs and student productivity tools. Exploring partnerships with schools and workplaces to bring posture awareness to more people. <div