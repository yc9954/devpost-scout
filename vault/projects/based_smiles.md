---
slug: "based_smiles"
url: "https://devpost.com/software/based_smiles"
title: "Better Web"
hackathon: "Frostbyte Hackathon"
organization: "FrostByte Club"
winner: true
words: 962
team_size: 1
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/cross_origin_web"
  - "mechanism/on_device_local"
  - "mechanism/realtime_stream"
  - "mechanism/retrieval_grounding"
  - "mechanism/voice_speech"
  - "domain/accessibility"
  - "domain/developer_tools"
  - "domain/education"
  - "domain/finance_payments"
  - "domain/labor_employment"
  - "domain/retail_commerce"
  - "domain/supply_logistics"
  - "user/developer"
  - "user/educator_student"
  - "substrate/video_visual"
  - "substrate/web_dom"
---

# Better Web

> AI-powered Chrome extension that adapts websites in real-time for users with ADHD, dyslexia, and sensory disabilities—making the web accessible for everyone.

[Devpost](https://devpost.com/software/based_smiles) · hackathon [[Frostbyte Hackathon]]

## Facets

**mechanism** [[cross_origin_web]] [[on_device_local]] [[realtime_stream]] [[retrieval_grounding]] [[voice_speech]]
**domain** [[accessibility]] [[developer_tools]] [[education]] [[finance_payments]] [[labor_employment]] [[retail_commerce]] [[supply_logistics]]
**user** [[developer]] [[educator_student]]
**substrate** [[video_visual]] [[web_dom]]

**stack** chrome, cohere, generative-ai, javascript, langchain, machine-learning, natural-language-processing, opencv, python, react, tensorflow

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for better web

## Body

AI agent working of ai agent Dyslexia people applying customisation like color grading, letter spacing to any website on google Inspiration 15% of the global population lives with some form of disability, yet 70% of websites fail basic accessibility standards. We were inspired after speaking with students with dyslexia who avoided online learning, professionals with ADHD who described the web as "sensory chaos," and users with visual impairments who struggled with everyday tasks like shopping or banking online. We realized the internet—meant to connect everyone—was leaving millions behind. BetterWeb was born from a simple belief: everyone deserves equal access to information. What it does BetterWeb is an AI-powered Chrome extension that adapts websites in real-time to match each user's accessibility needs: Personalized Accessibility Profiles : Quick 3-step setup for ADHD, dyslexia, visual impairments, photosensitivity, and cognitive needs Intelligent Text-to-Speech : Highlight any text and have it read aloud with natural voices Sensory-Friendly Theming : Soft pastel themes (lavender, mint, peach) designed to reduce overstimulation for autism spectrum users AI Voice Assistant : Natural language chatbot for hands-free navigation and feature control Motion-Sensitive Navigation : Head-tracking using TensorFlow.js for users with motor disabilities AI Color Correction : Generative AI adapts image contrast for various types of color blindness (prototype phase) Smart Content Adaptation : Automatic adjustments for font size, spacing, and contrast based on user profiles How we built it Frontend & Extension Architecture: Chrome Manifest V3 for secure, modern extension framework React.js + TailwindCSS for responsive, accessible UI Chrome Storage API for persistent cross-session preferences DOM manipulation engine for real-time page transformation AI & Machine Learning Stack: Cohere API v2 : Powers our conversational AI assistant with natural language understanding Google Text-to-Speech : High-quality voice synthesis for content reading TensorFlow.js + MediaPipe : Real-time head tracking for hands-free navigation OpenCV + PyTesseract : Image analysis, text extraction, and color correction Custom AI Agent : Built with Streamlit, web scraping, and generative embeddings for intelligent content adaptation Integration Layer: Chrome context menus for seamless right-click functionality Background service workers for persistent AI processing Content scripts for non-intrusive page modification PyQt5 for advanced image processing workflows Challenges we ran into Real-time DOM Manipulation Without Breaking Sites : Websites have wildly different structures. We had to develop intelligent CSS injection and MutationObserver patterns that adapt pages without causing layout breaks or functionality loss. AI Response Latency : Early versions had 3-5 second delays for voice commands. We optimized Cohere prompts, implemented smart caching, and built a prediction engine to anticipate user needs—reducing response time by 70%. Head-Tracking Accuracy : MediaPipe worked well in ideal conditions but failed in low light or with glasses. We trained custom calibration routines and added fallback controls. Color Correction Complexity : Adapting images for 8+ types of color blindness while preserving content meaning required extensive OpenCV experimentation. Our prototype works but needs more training data for production. Extension Performance : Loading heavy AI models slowed browsing. We implemented lazy loading, web workers for background processing, and optimized bundle size from 12MB to 2.3MB. User Privacy : Processing accessibility data is sensitive. We built everything locally-first with optional cloud sync, ensuring zero data leaves the user's device by default. Accomplishments that we're proud of ✨ Multi-Modal AI Integration : Successfully combined voice, vision, and NLP AI into one cohesive experience—something we haven't seen in accessibility tools 🎯 Real Users Testing : Got feedback from 12 beta testers with various disabilities—their reactions validated every late night of coding ⚡ Performance : Despite heavy AI processing, BetterWeb adds less than 50ms page load time 🛡️ Privacy-First Design : All processing happens locally; we never send user data to external servers 🎨 Inclusive Design : Our theming system was co-designed with neurodiverse users, not just for them 📦 Production-Ready : Not just a demo—fully functional Chrome extension ready for the web store What we learned Technical Lessons: How to architect Chrome extensions for AI workloads without killing performance The intricacies of DOM manipulation across thousands of different website structures Optimizing TensorFlow.js models for browser environments Building conversational AI that actually helps rather than frustrates users Human Lessons: Accessibility is deeply personal —what works for one dyslexic user may not work for another "Accessible design" isn't a checkbox —it's an ongoing conversation with users AI is a tool, not a solution —technology must serve human needs, not showcase capability The immense frustration users with disabilities face daily when the web fails them Product Lessons: Start with one persona, nail it, then expand Performance matters more than features User testing with actual disabled users is non-negotiable Privacy and trust are everything in assistive technology What's next for Better Web **Immediate Production-Grade Color Correction : Move from prototype to fully trained models for all color blindness types Firefox & Edge Support : Expand beyond Chrome using WebExtensions API Accessibility Dashboard : Analytics showing how BetterWeb improved browsing time and reduced frustration **Medium-Term Real-Time Accessibility Audit Engine : Score websites on accessibility and auto-fix common issues Cloud Sync with Privacy : Encrypted profile backup across devices Mobile App Version : Consistent accessibility on smartphones and tablets Learning Platform Integration : Auto-adaptive course delivery for educational institutions **Long-Term Vision API for Developers : Let websites integrate BetterWeb's accessibility engine natively Enterprise Partnerships : Work with universities and corporations for inclusive digital experiences Community-Driven Profiles : Let users share and customize accessibility presets Global Language Support : Expand TTS and AI assistance to 20+ languages Impact Goal : Within 3 years, we want BetterWeb powering accessible browsing for 1 million users globally—removing barriers to education, employment, and opportunity for people who've been excluded by inaccessible web design. BetterWeb doesn't just make browsing easier. It tears down barriers that have excluded millions from the digital world. Because everyone deserves access. <div