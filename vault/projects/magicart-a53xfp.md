---
slug: "magicart-a53xfp"
url: "https://devpost.com/software/magicart-a53xfp"
title: "MagiCart"
hackathon: "Google Maps Platform Awards"
organization: "Google"
winner: true
words: 667
team_size: 3
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "domain/agriculture_food"
  - "domain/education"
  - "domain/retail_commerce"
  - "domain/supply_logistics"
  - "domain/transportation"
  - "user/educator_student"
  - "substrate/geospatial"
---

# MagiCart

> What if your grocery cart could plan your route, lower your bill, and make you healthier, all before you even left the house? sounds too good to be true right? Well... MagiCart does exactly that!

[Devpost](https://devpost.com/software/magicart-a53xfp) · hackathon [[Google Maps Platform Awards]]

## Facets

**mechanism** [[realtime_stream]]
**domain** [[agriculture_food]] [[education]] [[retail_commerce]] [[supply_logistics]] [[transportation]]
**user** [[educator_student]]
**substrate** [[geospatial]]

**stack** firebase, gemini, google-directions, google-geocoding, google-play, java, jsx, locator-api, react, supabase, typescript

## How they structured the write-up

- 💡 inspiration
- 🧠 what it does
- 🛠️ how we built it
- 😅 challenges we ran into
- 🏆 accomplishments we're proud of
- 📚 what we learned
- 🚀 what’s next for magicart

## Body

Order summary Cart view 2 Extra feature: optimized route (connects 2 locations to the store such as work -> store -> home, so you could stop on the way home! Maps route to store and back Cart View AI Health recommendations (with Gemini) Home Page Shopping Options 🛒 MagiCart: Smart Grocery Shopping for Real Life 💡 Inspiration All of us are — or recently were — students. So, naturally, we can all agree on three simple facts: We wish we had more money (especially in this economy). We all need to eat a little healthier… ramen just isn’t cutting it. We wish we had more time — to study, to chill, or let’s be honest… to play video games. But grocery shopping? It's the enemy of all three: expensive, time-consuming, overwhelming. So we asked: What if your grocery cart could think? What if it could plan smarter routes, find cheaper options, and help you eat better — all before you even left the house? That’s why we built MagiCart : To save people time, money, and stress — all while making healthier decisions easier. 🧠 What It Does MagiCart is a smart grocery assistant designed for students and budget-conscious shoppers. ✅ Core Features 🛒 Smart cart comparison : Find the cheapest combo across multiple stores. 🧠 AI-powered store + product recommendations : Personalized based on your diet, allergies, budget, and store proximity. 📍 Optimized grocery route : Thanks to Google Maps Platform, we plan the fastest, most efficient shopping path. 💳 Affiliate-ready checkout : Auto-generated ready-to-shop carts that include affiliate links for monetization — without compromising UX. It’s like Google Maps + Instacart + a nutritionist in your pocket — built for broke, busy people. 🛠️ How We Built It 🔧 Core Technologies React + Tailwind CSS – For a clean, responsive, mobile-first UI. Redux – To manage global state for cart items, users, and store data. Supabase – For real-time syncing, authentication, and backend magic. Algolia – For blazing-fast product search and smart filtering. Gemini API – Built-in AI assistant helps plan meals, understand nutrition, and give store tips. 📍 Google Maps Platform APIs Geocoding API – Turn user addresses into coordinates. Directions API – Plot optimal multi-store shopping routes. Distance Matrix API – Calculate ETAs and rank route efficiency. 😅 Challenges We Ran Into 🧭 Multi-store route optimization Balancing cost, time, store hours, and user convenience across multiple locations? Not plug-and-play. 🔗 Affiliate integration Making checkout smooth while monetizing — without annoying users or breaking UX — took tricky logic. 🍽️ Health + nutrition personalization Matching preferences (keto, vegan, allergies, low-budget) in real time… while keeping suggestions helpful. 🏆 Accomplishments We're Proud Of 🔥 Built an AI engine that analyzes carts and gives real, personalized nutrition advice — in real time. 🗺️ Multi-store route optimization is seamless and helpful — goodbye, store-hopping chaos. 💰 Affiliate checkout that doesn’t hurt UX — users save money, we stay sustainable. ⚙️ Backend performance tuned to O(1)–O(log n) time/space complexity. 🎓 We actually use it IRL — and it’s already saving us time and money. 📚 What We Learned Real-world problems are messy — grocery logic is harder than it looks when factoring in real prices, stock, and preferences. Building for actual humans forces you to prioritize speed, simplicity, and trust. API orchestration is doable (Gemini, Maps, Supabase, Algolia) — if you keep your architecture clean. Great products aren’t just built — they’re shaped by real user feedback. 🚀 What’s Next for MagiCart 🌱 Add cultural + dietary filters (halal, kosher, vegan, low-FODMAP, etc.) 👥 Add social sharing (shopping plans, meal tips, budget hacks) 🚦 Add deeper route logic : traffic, delivery time windows, stock availability 🛍️ Partner with retailers for real-time inventory + price tracking 📦 Add delivery + rideshare integrations (Maps + Gemini FTW) 📲 Launch mobile-native version for even faster, seamless access We also hope to present MagiCart live at an upcoming tech event — and evolve it into a full platform for smart shopping. <div