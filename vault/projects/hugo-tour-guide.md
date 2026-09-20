---
slug: "hugo-tour-guide"
url: "https://devpost.com/software/hugo-tour-guide"
title: "Hugo Tour Guide"
hackathon: "ElevenLabs x 16z Worldwide Hackathon"
organization: "ElevenLabs"
winner: true
words: 1120
team_size: 4
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "mechanism/sensor_fusion"
  - "mechanism/voice_speech"
  - "domain/labor_employment"
  - "user/developer"
  - "user/general_public"
  - "substrate/code_repository"
  - "substrate/geospatial"
---

# Hugo Tour Guide

> Hugo is your AI travel companion—it plans routes, provides local-like insights, and maps your journey, saving you from constant research while answering cultural and historical questions on the go.

[Devpost](https://devpost.com/software/hugo-tour-guide) · hackathon [[ElevenLabs x 16z Worldwide Hackathon]]

## Facets

**mechanism** [[realtime_stream]] [[sensor_fusion]] [[voice_speech]]
**domain** [[labor_employment]]
**user** [[developer]] [[general_public]]
  <sub>weak: legal_professional</sub>
**substrate** [[code_repository]] [[geospatial]]

**stack** agents, ai, asr, eleven-labs, google-maps, google-places, llm, ml, openai, python, speech-to-text, text-to-speech, text-to-text

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for hugo tour guide
- team information(happy to connect in linkedin!)：
- technical details

## Body

Technical Details Hugo Tour Guide A next-generation AI travel companion designed to offer personalized, immersive experiences while you explore new cities and cultures. By combining state-of-the-art natural language processing, voice interactivity, and intelligent route planning, Hugo Tour Guide transforms the way you travel. Give it a try! Update: We are thrilled to have received recognition from the judges and hope to turn this into a real startup with commercial value. If you're interested in the future development of our product, you can register your email here as one of our seed users. Looking forward to seeing you again! Inspiration We are passionate travelers who spend up to two months each year exploring the world. However, traditional travel guides and packaged tours often fall short when it comes to truly personalized, in-depth experiences. We frequently find ourselves piecing together recommendations from diverse sources such as Reddit, Google Reviews, and local forums—resulting in disjointed itineraries and inefficient planning. Moreover, the idea of hiring a local guide, though appealing, is often cost-prohibitive (typically over $200 per day) and can be hindered by language barriers. With experiential travel on the rise—72% of consumers in a Booking.com survey expressed a preference for immersive, culturally rich experiences over generic sightseeing tours—we saw an opportunity. We envisioned an AI that could serve as a knowledgeable, interactive, and multilingual travel companion, effectively replacing the traditional local guide. What it Does Hugo Tour Guide is your personal AI travel companion that adapts to your interests and journey in real time. Key features include: Dynamic Preference Capture: Through voice or text interactions, the AI gathers details such as age group, occupation, hobbies, culinary interests, art, history, and even the planned duration of your city walk. Personalized Itinerary Planning: Combining your preferences, current travel history, and external data sources (e.g., top Reddit recommendations, popular forum posts, and Google Maps reviews), Hugo Tour Guide generates one or more tailored route options. Interactive Route Adjustment: Whether before or during your journey, you can adjust your itinerary using voice or text commands—adding, removing, or swapping out points of interest. The AI learns from these adjustments to refine future recommendations. Guided Tour Mode: Once you confirm your route, the AI maps out the itinerary and provides live, interactive explanations. You can click on any mapped location for detailed information and follow up with additional questions during the tour. Multilingual Support: To accommodate international travelers, the app supports multiple languages including Chinese, English, Japanese, and Korean. How We Built It Our development process leveraged modern web and AI technologies: Front-end: Built with React for a responsive and intuitive user interface. Integrated with ElevenLabs API for high-quality text-to-speech conversion. Utilized OpenAI API for accurate and natural speech-to-text conversion. Back-end: Developed in Python with seamless integration of OpenAI API and Google Maps API . Multiple intelligent agents were created to handle distinct tasks such as route planning and attraction introduction. Personalization: The AI model, based on OpenAI, was fine-tuned with extensive prompt engineering to ensure recommendations feel natural and deeply personalized to each traveler. Challenges We Ran Into Two primary challenges shaped our development: Prompting is hard: We aimed for simplistic design, yet with only a few logics and guidelines, but with a large amount of context data, we find it hard to make the LLM follow instruction properly, we had to cut guidelines and reduce scope to make it work properly. Given more time and resources, we would fine-tune LLMs with data collected through user usage or synthetically generated examples to fulfill all kinds of scenarios. Tricky UI integration with Speech Interface: Delivering a voice experience that mimics natural human conversation was challenging. We tested various speech synthesis APIs to find one that offered a smooth, natural, and comfortable interaction—vital for an engaging travel companion. Being able to quickly response and being able to deliver response in the correct language is crucial. Accomplishments That We're Proud Of Within just two days, we successfully built a prototype that delivers precise and personalized travel recommendations. We continually optimized the voice centric human–AI interaction experience by refining recommendation logic and enhancing voice interactivity. The result is a system that not only meets but exceeds user expectations in delivering seamless, real-time travel guidance. We started with a very large scope and we quickly scoped down to identify the core value then we delivered this very streamlined experience. What We Learned Our journey reinforced that while modern AI tools are incredibly powerful, they require meticulous fine-tuning and optimization to meet real user needs. Key insights include: Guiding User Input: People often provide vague descriptions of their preferences. Our AI needs to prompt and guide users to articulate their true needs, leveraging both prompt engineering and interactive design. Needs can then be collected by inferring on explicit and implicit needs. Building Trust Through Transparency: Users are more likely to trust the AI’s recommendations if they understand the decision-making process. Clearly conveying how choices are made helps build confidence in the system. We achive this in multiple ways, notably assuring the user we analyzed the data from large amount of reputation sources, and we also make recommendations based on user expressed preferences. What's Next for Hugo Tour Guide Looking ahead, our focus is on evolving the MVP into a fully market-ready product. Planned improvements include: Product Optimization: Streamlining front-end and back-end code by removing temporary implementations. Enhancing UI design and integrating a user account system. Data-Driven Personalization: Recording historical dialogues and user interactions to deliver increasingly personalized experiences. Data collected can then by used to sythensis more data for finetuning, so we can have a better aligned LLM for our usecase. Connect to even more data sources, for example wikidata to gather more relevant data. We can use it to answer questions, and guide user better on what to discover should they be interested. Better UI Experience, UI experience could be even better, perhaps we could also leverage GPS and Gyroscope to help guide the user during walking and trigger talking points along the way. Focus on targeted types of point of interests in different period to source even more data and tailor experiences for common and niche groups. Team Information(Happy to connect in Linkedin!)： Yilun Sun (Product Manager and Designer) Qiang Fang (Backend Engineer) David Chen (Frontend Engineer) Aiden Zhao (AI Engineer) Technical Details Tech Stack: Front-end: React, EleventLabs API, OpenAI API Back-end: Python, OpenAI API, Google Maps API Repository Links: Front-end Repository Back-end Repository Product Flow: View our agent workflow for an in-depth look at our architecture and design process. Hugo Tour Guide is committed to revolutionizing the travel experience by combining the best of AI and human interaction. We look forward to helping you explore the world like never before. <div