---
slug: "ai-mental-health-chatbot-jimyr9"
url: "https://devpost.com/software/ai-mental-health-chatbot-jimyr9"
title: "AI Mental Health Chatbot"
hackathon: "Frostbyte Hackathon"
organization: "FrostByte Club"
winner: true
words: 1221
team_size: 1
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/deterministic_policy"
  - "mechanism/on_device_local"
  - "mechanism/realtime_stream"
  - "mechanism/vision_ocr"
  - "mechanism/voice_speech"
  - "domain/education"
  - "domain/mental_health"
  - "user/educator_student"
  - "substrate/geospatial"
---

# AI Mental Health Chatbot

> AI-Powered Care, Human-Centered Support

[Devpost](https://devpost.com/software/ai-mental-health-chatbot-jimyr9) · hackathon [[Frostbyte Hackathon]]

## Facets

**mechanism** [[deterministic_policy]] [[on_device_local]] [[realtime_stream]] [[vision_ocr]] [[voice_speech]]
**domain** [[education]] [[mental_health]]
**user** [[educator_student]]
**substrate** [[geospatial]]
  <sub>weak: code_repository, financial_record, web_dom</sub>

**stack** css3, html, javascript, json, jsx, markdown, node.js, python

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for ai mental health chatbot
- mathematical model: response generation
- impact statement
- repository & demo

## Body

Home Page Mood Tracker Emergency Resources Inspiration Mental health is a silent crisis affecting millions worldwide. According to the WHO, approximately 1 in 5 adults experiences mental illness each year, yet access to support remains limited by high costs, long waiting lists, and social stigma. We were inspired by the countless stories of people suffering in silence—students struggling with exam anxiety at 2 AM, professionals overwhelmed by workplace stress, individuals hesitant to seek help due to stigma. We asked ourselves: What if everyone had access to a compassionate, judgment-free companion available 24/7? That question led us to build MindCare AI —a mental health chatbot that breaks down barriers to support, making empathetic care accessible to anyone, anywhere, at any time. What it does MindCare AI is a comprehensive mental health support web application powered by local artificial intelligence. It provides four core features: 1. AI-Powered Chat 🤖 Engages in empathetic, context-aware conversations Uses the Mistral language model running locally via Ollama Generates personalized responses tailored to each user's unique situation Understands emotional nuance and provides evidence-based coping strategies 2. Mood Tracking 📊 Allows users to log their emotional state over time Helps identify patterns and triggers in mental health Provides insights into what affects wellbeing Empowers users to understand their emotional journey 3. Smart Resources 💡 Curated library of mental health articles and coping strategies AI-powered personalized recommendations : users describe their struggle (stress, sleep, anxiety), and the AI generates tailored guidance instantly Matches users with relevant resources from the library 4. Emergency Support 🚨 Instant access to crisis helplines and suicide prevention resources Safety-first approach for mental health emergencies Direct links to professional help when needed How we built it Tech Stack Backend: Node.js with Express.js for RESTful API Ollama framework for running local AI models Mistral 7B language model for natural language understanding Axios for HTTP requests to Ollama Modular routing structure (chat, mood, resources) Frontend: React.js for dynamic, component-based UI Custom CSS with gradient designs and animations Responsive layout optimized for desktop and mobile Tab-based navigation for seamless user experience AI Integration: Configured Ollama to serve Mistral model locally on port 11434 Created system prompts to guide the AI toward empathetic, mental health-focused responses Implemented fallback pattern matching for offline scenarios Temperature tuning ($\tau = 0.7$) for balanced creativity and consistency Architecture ┌─────────────┐ ┌──────────────┐ ┌──────────────┐ │ React │ HTTP │ Express │ HTTP │ Ollama │ │ Frontend ├────────►│ Backend ├────────►│ (Mistral) │ │ (Port 3000)│ │ (Port 5000) │ │ (Port 11434) │ └─────────────┘ └──────────────┘ └──────────────┘ Key Implementation Details Chat Endpoint ( /api/chat ): Receives user message Constructs prompt with system context Calls Ollama API with POST /api/generate Returns AI-generated response Resources Recommendation ( /api/resources/personalized ): Accepts user's topic, mood, or concern Generates personalized advice using AI Matches with relevant static resources Returns both AI recommendation and resource links Local AI Configuration : No API keys required—fully offline capable Model size: ~4.1 GB (Mistral) Average response time: 2-5 seconds depending on hardware Challenges we ran into 1. AI Integration Complexity Initially, we planned to use OpenAI's API, but API key management and costs posed barriers. We pivoted to Ollama for local AI, which required: Learning Ollama's API structure Optimizing prompts for mental health context Balancing model size vs. response quality 2. Webpack Configuration Issues React's webpack-dev-server had dependency conflicts causing compilation failures: Module not found: webpack-dev-server/client/index.js Solution: Clean reinstall of dependencies and explicit installation of webpack-dev-server . 3. AI Response Latency Running AI locally on CPU introduced latency ($\approx$ 3-7 seconds per response). We optimized: Limited max_tokens to 500 Reduced num_predict to 250 Implemented loading states in UI 4. Context Understanding Early responses lacked empathy and felt robotic. We refined the system prompt to emphasize: Active listening Validation of emotions Actionable coping strategies Safety-first approach Accomplishments that we're proud of ✅ Privacy-First AI : Built a fully local AI solution—conversations never leave the user's device. No cloud dependencies, no data tracking. ✅ Real AI, Not Pattern Matching : Transitioned from simple keyword-based responses to genuine AI-powered conversations with context understanding. ✅ Personalized Resources : Integrated AI into the resources section, allowing users to get instant, tailored mental health guidance. ✅ Seamless UX : Created an intuitive, calming interface with smooth animations and responsive design. ✅ Emergency Awareness : Implemented crisis detection and immediate resource provision—safety is paramount. ✅ Zero Cost, Maximum Impact : No subscription fees, no API costs—accessible to anyone with a computer. What we learned Technical Lessons Local AI is viable : Tools like Ollama democratize AI access without cloud dependencies Prompt engineering matters : System prompts drastically affect AI behavior and empathy React state management : Handling async AI calls and loading states effectively Error handling : Graceful degradation when AI fails (fallback to pattern matching) Domain Knowledge Mental health support requires empathy first, solutions second Crisis situations demand immediate, clear pathways to professional help Privacy concerns are critical—users need assurance their conversations are confidential We are not therapists : Our role is to bridge the gap, not replace professionals Soft Skills Iterating rapidly based on testing feedback Balancing technical ambition with time constraints Prioritizing features: MVP vs. "nice-to-have" Communicating complex AI concepts simply What's next for AI Mental Health Chatbot Short-Term Enhancements Conversation History 💬 Store chat history locally (localStorage/IndexedDB) Enable AI to reference previous conversations for continuity Privacy-preserving: encrypted on-device storage Sentiment Analysis 📈 Real-time emotion detection during conversations Visual sentiment timeline in mood tracker Alert system for concerning patterns (e.g., persistent negative sentiment) Guided Exercises 🧘 Interactive breathing exercises with animations Progressive muscle relaxation guides Mindfulness meditation sessions Medium-Term Goals Multi-Language Support 🌍 Translate UI and AI responses Support underserved communities globally Voice Interaction 🎤 Speech-to-text for voice input Text-to-speech for AI responses Accessibility for visually impaired users Advanced AI Models 🚀 Upgrade to Llama 3 or Mistral-Large for improved understanding Fine-tune models on mental health datasets (e.g., Counsel Chat) Long-Term Vision Professional Integration 🏥 Connect users to licensed therapists via teletherapy platforms Share anonymized mood data with therapists (with user consent) Bridge gap between self-help and professional care Community Features 🤝 Anonymous peer support forums Group coping sessions (moderated) Shared resources and success stories Research Contribution 📚 Anonymized, aggregated data for mental health research Partner with universities and mental health organizations Evidence-based impact studies Mobile Application 📱 Native iOS/Android apps Push notifications for mood check-ins Offline-first architecture Mathematical Model: Response Generation The AI generates responses using a probabilistic language model: $$P(\text{response} | \text{user_message}, \text{context}) = \prod_{i=1}^{n} P(w_i | w_1, \ldots, w_{i-1}, \text{context})$$ Where: $w_i$ = $i$-th word in the response $\text{context}$ = system prompt + conversation history Temperature $\tau = 0.7$ controls randomness: $$P'(w_i) = \frac{\exp(\text{logit}_i / \tau)}{\sum_j \exp(\text{logit}_j / \tau)}$$ Higher $\tau$ = more creative, lower $\tau$ = more deterministic. Impact Statement MindCare AI is not a replacement for professional therapy—it's a bridge. We envision a world where: Mental health support is accessible to all, regardless of income or location Conversations are private and judgment-free Help is immediate , available at 2 AM when crisis strikes Technology empowers individuals on their mental health journey This project is our contribution to dismantling barriers in mental health care. Because everyone deserves support , and your mental health matters . Repository & Demo GitHub : AI-Powered-Mental-Health-Chatbot Video Demo : YouTube Link Live Demo : Run locally with Ollama—see README for setup <div