---
slug: "adblend"
url: "https://devpost.com/software/adblend"
title: "AdBlend."
hackathon: "2024 TikTok TechJam"
organization: "TikTok"
winner: true
words: 557
team_size: 5
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "mechanism/vision_ocr"
  - "domain/developer_tools"
  - "user/developer"
  - "substrate/video_visual"
---

# AdBlend.

> Transform your TikTok feed with AdBlend 🧩 🌟 Seamlessly integrate ads using generative AI ✨ Say hello to a non-invasive experience that flows with your content

[Devpost](https://devpost.com/software/adblend) · hackathon [[2024 TikTok TechJam]]

## Facets

**mechanism** [[realtime_stream]] [[vision_ocr]]
**domain** [[developer_tools]]
**user** [[developer]]
**substrate** [[video_visual]]
  <sub>weak: financial_record</sub>

**stack** absl, android-studio, jetpack, kotlin, no-external-apis-are-integrated, numpy, opencv, python, pytorch

## How they structured the write-up

- problem statement
- inspiration
- what it does
- features and functionality
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned

## Body

Problem statement Inspiring creativity with Generative AI 🌟 Inspiration 📱 The inspiration for AdBlend came from observing the growing trend of sponsored content on social media platforms, particularly TikTok. 🎨 Content creators often face challenges integrating sponsored images into their videos seamlessly, resulting in content that looks disjointed and unprofessional. We wanted to create a tool that simplifies this process, making it easy for creators to produce engaging, monetizable content without sacrificing quality. What it does 🧩 AdBlend is an innovative application that leverages advanced generative AI to seamlessly incorporate sponsored images into TikTok videos. The application uses real-time object detection to identify key areas within a video, where the sponsored content can be naturally integrated. Then it generates an advertisement that seamlessly fits into TikTok. This ensures that the final output looks professional and engaging, allowing creators to effortlessly blend sponsorships into their content. Features and Functionality Seamless Sponsored Content Integration: AdBlend uses generative AI to blend sponsored images into TikTok videos naturally and seamlessly, ensuring that the final content looks professional and engaging. User-Friendly Interface: Developed with Jetpack Compose, the application offers a modern and intuitive interface that simplifies the content creation process. Real-Time Object Detection: Leveraging the YOLOv9 object detection model, AdBlend accurately identifies key areas within the video for optimal placement of sponsored content and isolates that area. Enhanced Video Processing: With the power of OpenCV, AdBlend is able to replace the identified area with the image of the ad, ensuring the integrated content blends seamlessly with the original footage. How we built it Development Tools Jetpack Compose: For building a responsive and intuitive UI. Android Studio: As the primary integrated development environment. YOLOv9: For high-accuracy real-time object detection. Langchain: Integrating Dall-E API with our remote flask server APIs Used Currently, no external APIs are integrated, focusing on leveraging local processing capabilities. Assets Used Custom-designed UI components to ensure a smooth user experience. Sample images and video data sets for model training and testing. Libraries Used Android Developer Library: Ensures compatibility and optimal performance across a wide range of Android devices. OpenAI: Enabling smooth blending of ads with video background OpenCV: For advanced image and video processing. PyTorch: For implementing the YOLOv9 object detection model and other machine learning tasks. NumPy: For efficient numerical computations and data handling. Absl: For defining and parsing command-line arguments. Deep SORT Realtime: For accurate and efficient tracking of objects within videos. Challenges we ran into One of the primary challenges we faced was ensuring that the generative AI seamlessly integrated sponsored images into the videos without compromising the quality or natural appearance of the content. Additionally, optimizing the real-time object detection to accurately detect areas to place the advertisements required significant effort and testing. Accomplishments that we're proud of We are proud of creating a user-friendly application that leverages advanced AI generation capabilities to solve a real-world problem faced by content creators. Our successful integration of generative AI with real-time object detection and video processing showcases the potential of combining these technologies to enhance content creation. What we learned Through this project, we learned the importance of optimizing AI models and processing techniques for mobile platforms. We gained valuable experience in integrating multiple advanced technologies, such as YOLOv9 and OpenCV, to create a seamless user experience. Additionally, we deepened our understanding of the challenges and opportunity. <div