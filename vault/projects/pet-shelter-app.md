---
slug: "pet-shelter-app"
url: "https://devpost.com/software/pet-shelter-app"
title: "Pet Shelter App"
hackathon: "Google Chrome Built-in AI Challenge 2025 "
organization: "Google"
winner: true
words: 704
team_size: 1
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/vision_ocr"
  - "domain/housing_homeless"
  - "substrate/video_visual"
---

# Pet Shelter App

> Helping under-resourced shelters find forever homes for more pets, powered by free, private, client-side AI.

[Devpost](https://devpost.com/software/pet-shelter-app) · hackathon [[Google Chrome Built-in AI Challenge 2025]]

## Facets

**mechanism** [[vision_ocr]]
**domain** [[housing_homeless]]
**substrate** [[video_visual]]

**stack** angular.js, chrome, firebase, node.js, typescript

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for pet shelter app

## Body

Inspiration Our inspiration came from seeing local animal shelters struggle. They often rely on manual social media posts, lacking the time and resources to write compelling profiles for every pet. This leads to generic listings and missed adoption opportunities. We saw a critical gap: shelters can't afford expensive, cloud-based AI APIs for tasks like image recognition or content generation. We were inspired to build a platform that brings state-of-the-art AI to them for free , running entirely inside the Chrome browser. By eliminating server costs, we can provide a powerful tool that helps volunteers save time and, most importantly, save more lives. What it does Pet Shelter App is a full-stack platform that transforms a time-consuming manual task into a simple, AI-powered workflow: List & Filter: Shelters get a professional, filterable web gallery of all available pets, a huge step up from scattered social media posts. AI-Powered Profile Creation: This is the core of our solution. When adding a new pet, staff simply upload a photo. Chrome's Prompt API analyzes the image and instantly suggests the pet's animal type, breed, estimated age, and even a potential name, auto-filling the form. Compelling Descriptions: Staff can write a quick note (e.g., "friendly, loves sun"), and the Writer API expands it into a warm, engaging adoption description. The Proofreader API ensures it's grammatically perfect. Reach More Adopters: Potential adopters can use the Translator API to read any pet's story in their native language (EN, ES, FR), breaking down language barriers to adoption. How we built it We built a full-stack solution to be a complete, standalone product. Frontend: An Angular single-page application (SPA) styled with Tailwind CSS . This is where all the AI magic happens. Backend: A Node.js/Express API responsible for basic CRUD operations (creating, reading pets data). Infrastructure: Firebase Storage is used for hosting the pet images that are uploaded. The core of our project is the deep, client-side integration of Chrome's Built-in AI APIs into our Angular components: It uses the Prompt API 's multimodal (image + text) capabilities to parse the uploaded photo and return structured JSON. The pet's description content is enhanced by the Writer API and Proofreader API . It uses the Translator API to provide on-demand, in-browser translation of the pet's bio. Challenges we ran into Our main challenge was ensuring graceful degradation . Since the AI APIs are client-side and depend on user hardware, we couldn't guarantee their availability. We had to build robust checks to detect if the built-in APIs and its methods were available. If an API is missing, the corresponding feature (e.g., the "Auto-fill from Image" button) is cleanly disabled, but the form remains 100% functional for manual entry. This ensures the app is useful for all shelters, while providing a "magical," time-saving experience for those with compatible browsers. Accomplishments that we're proud of We are incredibly proud of the "Add Pet" workflow. Seeing the Prompt API - multimodal analyze a pet's photo and return structured JSON with its breed, age, and gender is a "wow" moment. It’s the core of our solution: taking a complex task that required manual research and data entry and making it instant and free. We're also proud to have built a complete application, not just a feature demo. It's a tool that a shelter could genuinely use today . What we learned We learned that client-side AI isn't just a novelty; it's a powerful tool for accessibility and equity . By using Chrome's built-in APIs, we can deliver sophisticated AI features to non-profits and small organizations who would otherwise be priced out of cloud-based solutions. Privacy, network resilience, and cost-efficiency aren't just technical benefits; they are the keys to unlocking new, more equitable applications for users who need them most. What's next for Pet Shelter App We're excited to integrate more of Chrome's AI suite to further reduce manual work for shelters. Our next steps include: Using the Rewriter API to give shelters multiple-choice options for a pet's description tone (e.g., "Make it funnier," "Make it more urgent," "Focus on a calm home"). Integrating the Summarizer API to help shelters condense long veterinary notes or previous owner surrenders into a clear, adopter-friendly summary of the pet's health and history. <div