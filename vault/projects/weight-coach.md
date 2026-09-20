---
slug: "weight-coach"
url: "https://devpost.com/software/weight-coach"
title: "Weight Coach"
hackathon: "World’s Largest Hackathon presented by Bolt"
organization: "StackBlitz / Bolt"
winner: true
words: 1271
team_size: 1
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "mechanism/sensor_fusion"
  - "mechanism/voice_speech"
  - "domain/agriculture_food"
  - "domain/retail_commerce"
  - "domain/scientific_research"
  - "domain/supply_logistics"
  - "substrate/genomic_bio"
  - "substrate/sensor_telemetry"
  - "substrate/structured_db"
  - "substrate/video_visual"
  - "substrate/web_dom"
---

# Weight Coach

> AI-powered meal planner with voice cooking assistant. Turns your inventory into personalized recipes, smart grocery lists, and hands-free cooking guidance to reduce waste and simplify healthy eating

[Devpost](https://devpost.com/software/weight-coach) · hackathon [[World-s Largest Hackathon presented by Bolt]]

## Facets

**mechanism** [[realtime_stream]] [[sensor_fusion]] [[voice_speech]]
**domain** [[agriculture_food]] [[retail_commerce]] [[scientific_research]] [[supply_logistics]]
**substrate** [[genomic_bio]] [[sensor_telemetry]] [[structured_db]] [[video_visual]] [[web_dom]]

**stack** amazon-web-services, bolt, elevenlabs, expo.io, netlify, openai, react-native, revenuecat, supabase, typescript

## How they structured the write-up

- inspiration
- what it does
- accomplishments that i'm proud of
- what i learned
- what's next for weight coach

## Body

Landing page Dynamic input modes for camera, voice and text to keep track of your inventory effortlessly Cooking modes Smart inventory management that keeps track of items that are expiring and everything else Chat interface with a nutritionist that has all the context of what you have in your kitchen and your meal plans Dashboard keeping track of daily goals Inspiration Food waste is a massive problem - Americans throw away 40% of their food, worth over $1,500 per household annually. At the same time, meal planning feels overwhelming and most people struggle with healthy eating. I realized these problems are connected: what if AI could eliminate food waste while making healthy eating effortless? The breakthrough moment came when I thought about how a personal chef would work - they know what's in your kitchen, plan meals around available ingredients, and guide you through cooking. But more than that, I kept coming back to this idea: what if your kitchen could think? Most nutrition apps focus on tracking what you've already eaten - take a photo of your finished meal, log calories, move on. But that's backwards. The real opportunity is at the beginning of the process: helping you manage what's actually in your kitchen, planning meals around real ingredients you own, and preventing food from going to waste in the first place. Weight Coach isn't another calorie tracker. It's kitchen intelligence - AI that understands your inventory, knows what's expiring, and helps you make better decisions before you even start cooking. What it does Weight Coach is an AI nutrition coach that knows what's in your kitchen and helps you eat better while preventing food waste. Unlike calorie tracking apps that photograph finished meals, Weight Coach manages your entire kitchen ecosystem from ingredients to final dish. Smart Inventory Management : Add ingredients by voice ("3 apples and 2 bananas"), scan any food items with your camera for instant recognition, or type manually. The app tracks expiration dates and sends alerts before food goes bad - preventing waste before it happens. AI Meal Planning : Generate personalized meal plans based on your actual inventory, dietary goals, and preferences. Watch your meal plan create in real-time instead of staring at loading screens. The AI prioritizes ingredients that are expiring soon. Voice Cooking Assistant : Get hands-free recipe guidance while cooking. Ask questions, set timers, get temperature conversions - all through natural conversation powered by ElevenLabs. Proactive Nutrition Coaching : Instead of tracking calories after eating, the AI coach helps you make better decisions upfront. It understands your goals and current inventory to give contextual advice like "Based on your inventory, you could make a protein-rich snack with those eggs and spinach." Smart Grocery Lists : Automatically generate shopping lists from meal plans or low inventory items, ensuring you buy only what you need. This isn't about logging what you ate - it's about making your kitchen smarter so you eat better and waste less from the start. ## How I built it Primary Development : Built the core application in Bolt.new, which accelerated development massively. The AI-assisted coding let me focus on complex features rather than boilerplate. Backend Architecture : Supabase handles the database, authentication, and real-time features. Edge Functions process AI requests and handle complex meal plan generation. AI Integration : AWS Bedrock powers meal planning and nutrition advice with Claude Sonnet 4. ElevenLabs provides the conversational voice assistant for hands-free cooking. Monetization : RevenueCat manages the freemium subscription model - basic features free, advanced AI features require subscription. Tech Stack : React Native with Expo for cross-platform mobile, TypeScript throughout, custom UI components with smooth animations. Deployment : Netlify handles deployment with automatic builds and global CDN distribution for the marketing website The app syncs everything in real-time - add ingredients and meal plans update instantly, log meals and nutrition tracking updates live. ## Challenges I ran into Real-Time AI Generation : Making meal plan generation feel engaging rather than slow. Instead of loading screens, I built streaming components that show the meal plan being created step-by-step in real-time. Complex Data Relationships : Managing the connections between users, inventory, meal plans, recipes, and nutrition goals required careful database design and real-time synchronization. Multi-Modal Input Processing : Combining voice, camera, and text input with AI processing. Users can speak naturally, scan any food items with the camera, or type - all need to work seamlessly together. Cross-Platform Voice : Getting ElevenLabs voice synthesis and Expo Speech Recognition working consistently across iOS, Android, and web platforms. Accomplishments that I'm proud of Progressive Generation UI : Instead of boring loading screens, users watch their meal plans generate in real-time. This simple change made the AI feel alive and engaging. True Hands-Free Cooking : Complete recipe guidance through voice with smart timer management. You never need to touch your phone while cooking. Context-Aware AI : The nutrition coach actually knows what's in your kitchen and your goals. It gives advice like "You have chicken expiring tomorrow - want me to suggest some recipes?" Production-Ready Architecture : Built on Supabase to scale to millions of users, complete error handling with Sentry, analytics with PostHog, and seamless subscription management. Multi-Modal Intelligence : Voice, camera recognition of any food items, and text input all work together naturally. Say "3 apples", scan ingredients with your camera, or type manually - the AI understands it all. Proactive vs Reactive Approach : While other apps track what you've eaten, Weight Coach prevents problems before they happen - suggesting recipes for expiring ingredients and optimizing nutrition from your actual inventory. What I learned Bolt.new is a Game Changer : AI-assisted development dramatically speeds up full-stack development. I could focus on complex AI orchestration instead of writing boilerplate code. And the fact that you can create native applications right in bolt is HUGE! Real-Time Makes Everything Better : Users expect instant updates now. When you add ingredients, meal plans should update immediately. When you log a meal, progress tracking should reflect instantly. Voice Changes the Kitchen Experience : Hands-free interaction isn't just convenient - it transforms cooking from frustrating to magical. No more touching your phone with messy hands. Context is Everything for AI : Generic AI advice is useless. AI becomes incredibly valuable when it understands your real situation - your inventory, goals, cooking experience, and dietary restrictions. Progressive Generation Beats Loading : Showing users the AI working in real-time creates engagement instead of frustration. People love watching their meal plan generate step by step. Prevention Beats Tracking : Most nutrition apps are reactive - they track what you've already eaten. The real opportunity is being proactive - helping people make better decisions before they cook and eat. What's next for Weight Coach Instacart integration : Give users the ability to order all the necessary groceries without leaving the app or their home Gamifying progress : How does Weight Coach become the DuoLingo for smart cooking/eating. Social Features : Share successful meals with friends, get recipe recommendations from your network, and compete on waste reduction goals. Advanced Nutrition Analysis : Integrate with health apps and wearables to provide more personalized nutrition advice based on activity levels, sleep, and health metrics. Better AI Capabilities : Training the models on better recognition. Integrating with existing APIs for meal plans, groceries, etc for a more accurate tracking. The vision is to make Weight Coach the central hub for all nutrition decisions - whether you're grocery shopping, cooking at home, or eating out. A truly intelligent kitchen that thinks ahead, prevents waste, and helps you live healthier without the hassle of traditional food tracking. <div