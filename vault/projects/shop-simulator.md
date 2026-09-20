---
slug: "shop-simulator"
url: "https://devpost.com/software/shop-simulator"
title: "The Merchant"
hackathon: "Meta Horizon Creator Competition: Mobile Innovation"
organization: "Meta"
winner: true
words: 1043
team_size: 1
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "domain/civic_government"
  - "domain/labor_employment"
  - "domain/retail_commerce"
  - "domain/supply_logistics"
  - "domain/transportation"
  - "user/small_business"
  - "substrate/code_repository"
  - "substrate/geospatial"
  - "substrate/video_visual"
---

# The Merchant

> Craft items. Sell them to customers. Hire workers. Customize your shop. Become The Merchant

[Devpost](https://devpost.com/software/shop-simulator) · hackathon [[Meta Horizon Creator Competition- Mobile Innovation]]

## Facets

**domain** [[civic_government]] [[labor_employment]] [[retail_commerce]] [[supply_logistics]] [[transportation]]
**user** [[small_business]]
**substrate** [[code_repository]] [[geospatial]] [[video_visual]]

**stack** genai, horizon, horizonworlds, meta, ts, typescript

## How they structured the write-up

- inspiration
- what it does
- how i built it
- challenges i ran into
- accomplishments that i'm proud of
- what i've learned
- what’s next for the merchant

## Body

World Id: 799885093215507 Youtube: https://www.youtube.com/watch?v=5xCAhIs8gNU Vimeo: https://vimeo.com/1144592855 Play now: https://horizon.meta.com/world/799885093215507/ Inspiration With The Merchant, I wanted to revisit the foundation of an older game of mine, Hantverk Village, and take it in a new direction. It keeps a simple, satisfying crafting loop at its center and builds it into a full shopkeeping world where you run your own shop, fulfill customer requests, customize your space, hire workers with personality, and grow through progression that feels genuinely earned What it does The Merchant is a mobile-first and portrait-oriented cozy fantasy shopkeeping and crafting game built primarily around Noesis where players are guided by Julia , the games AI Mentor, as they craft items using simple taps , fulfill customer requests, hire workers, customize their space, and steadily grow their shop over time . With World Broadcast , aspiring shopkeepers can peek into the big leagues and see how seasoned owners run their shops Core Gameplay Loop Receive customer requests based on unlocked item recipes Craft items using taps and gain crafting XP Fulfill customer requests for gold and gain shop XP Unlock higher tier item recipes, hire workers, and customize the shop The cycle repeats Early game feels quick and approachable, while full progression unfolds over time, rewarding steady play as you work toward unlocking everything Core Features New User Experience (NUX) A short, image-driven introduction to the game with voiceover from Julia appears for new players Automatically disables itself after a few visits Julia, the game's AI Mentor , can be visited and chatted with at any time and her guidebook expands on key gameplay elements with voiceover Customer Requests NPCs arrive throughout the day asking for specific items Request pools scale with the player’s unlocked tiers Customers form lines at each individual active worker and exit through dynamic routing Traffic changes based on the current time of day Day/Night Cycle World transitions through Sunrise, Daytime, Sunset, and Night Each phase shifts lighting, mood, and customer activity Inventory and Currency Players earn gold from vendor-selling crafted items, fulfilling customer requests, and through playtime rewards Gold is used to unlock new item recipes, workers, shop colors, furnishings, and decorations Crafted items are stored and can be automatically used by workers Crafting Tap based crafting Simple crafting loop with deep stat-driven outcomes Items can be Perfect, Good, or Poor quality based on the player's crafting level Each tier has its own threshold before Perfects become possible, with lower tiers unlocking early and higher tiers requiring deeper progression Once past the threshold, Perfect chance increases steadily until it reaches 100 percent at that tier’s cap Workers Hire up to three workers, each with their own rating that affects performance Workers automatically fulfill customer requests They craft missing items if the player doesn’t have them Each worker manages their own dedicated customer line Unique voice lines Shop Customization Unlock furnishings that visually expand the shop Place decorations for personalization Change shop colors for floors and walls Chest Minigame Three chests randomly spawn outside of the shop every few minutes Walking over a chest grants a gold reward that scales with shop level and remains valuable throughout progression Progression and Rewards Crafting XP, shop XP Many unlocks Item recipes, colors, furnishings, decorations, workers, and more Daily login rewards and milestone-based playtime rewards A steady gold economy that scales with shop growth Fifteen quests and six leaderboards to compete against other players on Persistent Save Inventory, currency, stats, furnishings, workers, shop colors, and customization all save automatically Players always return to the shop exactly as they left it How I built it I built The Merchant by starting small and expanding the world one system at a time. The crafting loop came first, anchoring everything, then customer requests, then workers as the shop took shape. Progression grew alongside each new feature. Once the core was solid, the day-night cycle brought the world together. Each major feature was built as its own clean, independent component, which let the shop slowly wake up without breaking anything Challenges I ran into Learning Noesis and working through the depth inside each core system, from customers to crafting to workers, took a lot of iteration to make everything feel responsive, cohesive, and fully integrated Accomplishments that I'm proud of I'm proud of how much the project grew. The Merchant became the largest game I have ever built, with over sixty handcrafted scripts working together to create a world that's fun and looks good. It pushed me into deeper system design, more thoughtful structuring, and a level of polish I had not reached before. Seeing all of my work come into the playable experience that it is feels like a genuine milestone, both in scope and in what I learned while building it What I've learned Building The Merchant showed me how essential structure and iteration are on a large project. Modular systems made complex behavior manageable, and constant tuning shaped the feel of the world. Designing for long-term progression pushed me to think more carefully about pacing. The whole project became a crash course in building for scale and stability without getting overwhelmed What’s next for The Merchant I am committed to bringing the following to The Merchant as time permits: IWP (In-world purchases) Including clothing with traits More tiers for each category of item recipes More furnishings and decorations Shop expansions with larger layouts and rooms Expand on customer interaction & behaviors Expand on worker personality and depth Including specializations (traits of sorts) and randomized voice lines Expand on rewards to include more than just time played Including achievements/milestones for taps, items crafted, requests completed, etc. Enable multiplayer support (once it can be properly tested) with multiple areas/players Every system was built to support multiplayer, but I have not been able to properly test it before the deadline Alternatively, keep the game 1P to be able to go beyond the limits of having multiplayer, allowing me to offer more to the single person playing Exploring swipes and a more interactive tap sequence Enhanced Web gameplay Enhanced UI design Enhanced World Broadcasting Adding seasonal and always-active time-based events Adding app migration support for Facebook & Instagram users Adding customer and worker feedback For workers, "Waiting..", "Crafting", "Selling", etc. For customers, "Pleased", "Dissatisfied", etc. <div