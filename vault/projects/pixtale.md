---
slug: "pixtale"
url: "https://devpost.com/software/pixtale"
title: "Pixtale"
hackathon: "Google AI Hackathon"
organization: "Google"
winner: true
words: 679
team_size: 2
has_repo: true
has_live: false
has_video: false
tags:
  - "project"
  - "mechanism/voice_speech"
  - "substrate/geospatial"
  - "substrate/video_visual"
---

# Pixtale

> From trip pics to narrated videos in minutes. Share travel stories with AI magic.

[Devpost](https://devpost.com/software/pixtale) · hackathon [[Google AI Hackathon]]

## Facets

**mechanism** [[voice_speech]]
**substrate** [[geospatial]] [[video_visual]]

**stack** flask, gcp, gemini, python

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for pixtale

## Body

High level flow Inspiration Wouldn't it be great to have a video of our entire trip narrated and generated with the click of a button? Pixtale aims to achieve this by leveraging the power of AI and various Google Cloud services. What it does With Pixtale, users can get videos of their trips narrated by Gemini AI. The process involves uploading a zip file containing photos and videos from the trip or selecting a Google Photos album. Pixtale then extracts metadata, generates descriptions using Gemini AI, creates a narrative script, converts the narration to audio, and combines everything into a final video. Additionally, Pixtale generates captions, hashtags, and a mini blog post to share on social media. How we built it The process of building Pixtale involved several steps: Metadata Extraction : First, metadata like date, time, and GPS data is extracted from the uploaded photos or videos. AI-Powered Descriptions : With the Vertex AI API, Gemini Pro Vision and Gemini 1.5 Pro are used to generate descriptions for photos and videos, respectively. Narrative Script Generation : All the descriptions are passed as a JSON list into a mega prompt for Gemini 1.5 Pro to create a narrative script scene by scene. Narration and Audio Generation : For each scene, narration text is generated and converted into audio using Google's Text-to-Speech services (Cloud Text-to-Speech API). Video Creation : The narrated audio and media items are combined using FFmpeg to create the final video. Blog Post Generation : A mini blog post is also generated using Gemini 1.5 Pro, providing a written summary of the trip. User Interaction : Users can edit the places for each scene using the Google Maps API and initially download media items from a particular Google Photos album using the Google Photos Library API. The app is built with Flask and uses Tailwind CSS and Flowbite for styling. Challenges we ran into While working on this project, we faced a few challenges: Gemini 1.5 Pro Rate Limits : One of the main challenges was dealing with the rate limits imposed on Gemini 1.5 Pro, which restricted the number of requests that could be made per day. Video Processing : Learning and implementing video processing techniques with FFmpeg was a significant hurdle, as it required a deep understanding of video encoding, formats, and processing pipelines. Accomplishments that we're proud of We are proud to have created a seamless and automated solution for generating narrated trip videos leveraging AI and cloud services. The integration of various technologies and services, such as Gemini AI, Google Cloud APIs, and FFmpeg, allowed us to create a unique and engaging experience for users. What we learned This project allowed us to learn and work with several exciting technologies: Gemini AI : We utilized Gemini AI's capabilities for vision (Gemini Pro Vision for photos) and language generation (Gemini 1.5 Pro for videos and creating narrative scripts). Google Cloud Services : We learned to use various Google Cloud services, including Google Maps API, Google Photos Library API, and Google's Text-to-Speech services. Video Processing : We gained knowledge in video processing using FFmpeg, which was crucial for stringing together the narrated scenes. Web Development : The app is built with Flask, a Python web framework, allowing us to enhance our web development skills. What's next for Pixtale Pixtale has the potential to be a valuable addition to the Google Photos product line. Future developments could include: Improved Rate Limiting Handling : Implementing better strategies to handle Gemini 1.5 Pro's rate limits, ensuring a smoother user experience. Advanced Video Editing : Introducing more advanced video editing features, such as transitions, overlays, and visual effects, to enhance the final video. Integration with Google Photos : Deeper integration with Google Photos, enabling users to seamlessly access and manage their albums and media items within Pixtale. Additional Customization Options : Providing users with more customization options for the narrative script, audio narration, and video styles. With continuous improvement and integration with existing Google services, Pixtale could become a powerful tool for creating personalized and engaging trip memories. <div