---
slug: "food-inspector"
url: "https://devpost.com/software/food-inspector"
title: "Food Inspector"
hackathon: "Youth Code x AI"
organization: "Youth Code Foundation"
winner: true
words: 406
team_size: 1
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/vision_ocr"
  - "mechanism/voice_speech"
  - "domain/agriculture_food"
  - "user/government_staff"
  - "user/patient_family"
  - "substrate/video_visual"
---

# Food Inspector

> Analyze ingredients, nutrition, and food safety instantly using AI

[Devpost](https://devpost.com/software/food-inspector) · hackathon [[Youth Code x AI]]

## Facets

**mechanism** [[vision_ocr]] [[voice_speech]]
**domain** [[agriculture_food]]
**user** [[government_staff]] [[patient_family]]
**substrate** [[video_visual]]

**stack** azure, github, python, react

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for food inspector

## Body

Inspiration In today's fast-paced world, processed food has become an integral part of our daily lives. However, with its increasing consumption comes a growing risk of health issues. The rise in processed foods has been accompanied by an increase in conditions such as diabetes, hypertension, and other lifestyle-related diseases that are directly or indirectly linked to our eating habits. What it does Food Inspector is an AI-powered application that evaluates packaged food products by analyzing their ingredients alongside a user's basic health information. Users provide details such as their age, gender, allergies, dietary preferences, and existing medical conditions, then upload an image of the product's ingredient list. The application extracts the text using OCR, analyzes the ingredients with AI, and generates a personalized report that includes: A safety assessment indicating whether the product is suitable for the user. A detailed ingredient analysis with potential health concerns. Interactive charts to visualize nutritional information. Healthier alternative recommendations. An AI-generated voice summary for quick and convenient insights. How we built it I built the frontend using React and developed the backend using Python Flask . The application leverages several Azure AI services: Azure AI Vision OCR to extract text from ingredient labels. Azure OpenAI to analyze ingredients and generate personalized recommendations. Azure AI Speech Service to convert the generated summary into natural-sounding speech. Challenges we ran into One of the biggest challenges was integrating the backend services, especially implementing text-to-speech functionality using Azure AI Speech Service. I also spent considerable time designing prompts that consistently produced structured JSON responses. Another challenge was integrating interactive charts that present nutritional information in a clear and user-friendly way. Accomplishments that we're proud of I'm proud that I was able to build a complete end-to-end application within the hackathon timeline. Integrating OCR, generative AI, speech synthesis, and an interactive React frontend into a single seamless experience was both challenging and rewarding. What we learned This project gave me hands-on experience with React Router, Flask, Azure AI services, and integrating multiple AI-powered APIs into a production-style application. I also improved my understanding of prompt engineering, backend architecture, and building AI-powered user experiences. What's next for Food Inspector I plan to add a report-sharing feature so users can easily share their food analysis with family members or healthcare professionals. In the future, I'd also like to introduce barcode scanning, multilingual ingredient analysis, and personalized long-term dietary recommendations to make Food Inspector even more useful. <div