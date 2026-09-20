---
slug: "love-at-first-bite-kt3zca"
url: "https://devpost.com/software/love-at-first-bite-kt3zca"
title: "Love At First Bite"
hackathon: "ConUHacks X"
organization: "HackConcordia"
winner: true
words: 909
team_size: 4
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "domain/developer_tools"
  - "user/developer"
  - "substrate/geospatial"
  - "substrate/structured_db"
  - "substrate/video_visual"
---

# Love At First Bite

> Tinder, but for food — describe what you want, swipe through restaurants, and instantly match with the perfect place to eat.

[Devpost](https://devpost.com/software/love-at-first-bite-kt3zca) · hackathon [[ConUHacks X]]

## Facets

**mechanism** [[realtime_stream]]
**domain** [[developer_tools]]
**user** [[developer]]
**substrate** [[geospatial]] [[structured_db]] [[video_visual]]

**stack** framer-motion, moonshine, next.js, openai, openrouter-api, pnpm, react, tailwind-css, typescript, vercel, yelp-fusion-api, zod

## How they structured the write-up

- 💡 inspiration
- 📱 what it does
- ⚙️ how we built it
- 🚧 challenges we ran into
- 🏆 what we're proud of
- 🧠 what we learned
- 🚀 what's next

## Body

Landing Page Swipe Page Result Page Love At First Bite 💡 Inspiration We've all been there: it's Friday night, you're hungry, and the group chat spirals into "I don't know, where do you want to go?" followed by "You pick." Decision fatigue is real. Existing apps like Yelp and Google Maps excel at information density, but they're terrible at helping groups make quick decisions. We realized that the swipe mechanic—proven effective by dating apps—is fundamentally the fastest way to make binary choices. We built Love At First Bite to make finding dinner faster and more fun than the traditional restaurant browsing experience. 📱 What It Does Love At First Bite is a restaurant discovery app that prioritizes decision speed over information overload. Natural Language First : Instead of toggling 10 filters, you simply describe what you want in plain English: "I want a cozy Italian spot for a date night, under $50, within walking distance." AI Interpretation : Our LLM agent parses this request—extracting not just cuisine preferences, but vibe, budget, and context—and translates it into precise Yelp search parameters. Swipe to Decide : Results appear as full-screen "poster-style" cards optimized for mobile. Users swipe Right to like or Left to pass. Smart Matching : Our weighted ranking algorithm analyzes the matches against their original intent, balancing multiple factors to identify the optimal restaurant. ⚙️ How We Built It The Brain (AI) : OpenAI's GPT-4o-mini via OpenRouter powers intent interpretation. We engineered strict system prompts to output structured JSON SearchSpec objects, mapping subjective terms like "vibey" or "romantic" to concrete Yelp attributes and category aliases. The Data : Real-time restaurant data, reviews, and imagery from the Yelp Fusion API. The Frontend : Built on Next.js 16.1.4 (App Router) with TypeScript for type safety. The UI/UX : Tailwind CSS for the dark, modern design. Framer Motion handles the physics-based gesture recognition for swipe interactions—complex rotation and momentum calculations keep the animation feeling natural. The Logic : A custom scoring algorithm ( lib/ranking/scoreRestaurant.ts ) that weighs multiple factors: $$\text{Score} = 0.40 \times \text{Rating} + 0.25 \times \frac{1}{\text{Distance}} + 0.15 \times \text{Price Alignment} + 0.20 \times \text{Other Factors}$$ This formula ensures that user ratings drive the decision ( 40% ), but we don't ignore convenience (distance at 25% ) or budget constraints ( 15% ). 🚧 Challenges We Ran Into The "Vibe" Problem : Databases don't have a "cool vibe" column. We had to build a mapping layer between subjective human language ( hole-in-the-wall, romantic, energetic, modern ) and Yelp's category system and boolean attributes. This required careful analysis of how different adjectives map to Yelp's data model. Animation Physics : Achieving native-feeling swipe behavior on the web was harder than expected. We spent significant time tuning Framer Motion's useTransform hooks and gesture handlers to ensure cards snapped back or flew off-screen with proper inertia and rotation. The physics had to feel "right" or users would abandon the interface. Latency : Chaining an LLM call to an external API call can create compound delays. We optimized server routes to parse intent and fetch data in parallel where possible, keeping "time to first swipe" under acceptable thresholds. Critical path: LLM parse → parallel Yelp requests → rank results . Edge Cases : Natural language input is inherently messy. Users describe restaurants in wildly different ways. We implemented robust Zod schema validation to handle the variety of input patterns and gracefully fail with helpful error messages. 🏆 What We're Proud Of Seamless NLP Pipeline : Built a complete system where users can type almost anything, and the app "understands" intent and fetches valid data without crashing. The "Poster" UI : Moved away from standard list views to a full-screen, immersive card design that looks great on mobile and focuses entirely on the decision. Smart Scoring : We didn't just return random restaurants; we built a legitimate weighting system that mimics how humans actually make decisions (balancing quality, convenience, and budget). Type-Safe End-to-End : Leveraged TypeScript throughout the stack for compile-time safety and better developer experience. 🧠 What We Learned Prompt Engineering is Coding : Strict system prompts are as important as TypeScript logic when working with LLMs. The way you frame constraints and instructions directly impacts output quality. User Intent is Messy : Humans rarely speak in clear database queries. Handling edge cases in natural language required robust validation and error recovery. The Power of Limits : By showing only name, rating, and photo on each card, we actually helped users make decisions faster than if we showed all available information. Information minimalism is a feature, not a bug. Swipes Eliminate Comparison Paralysis : The binary choice format removes the cognitive overhead of comparing options. It's psychologically easier to say "yes or no" than "which of these three is better?" Parallel Processing Matters : In a production pipeline, orchestrating LLM calls and API requests in parallel can cut response time in half. 🚀 What's Next Multiplayer "Consensus" Mode : Allow two different users to swipe on their own phones; alert them when there's a mutual match. This solves the original problem (group decision-making) at scale. Taste Learning : Implement an ML model that learns individual preferences over time—e.g., realizing a user says they like "healthy" but consistently swipes right on burger joints. Direct Booking : Integrate reservation APIs (OpenTable, Resy) to book tables directly from the match screen. Multi-City Support : Expand beyond local searches to handle "best restaurants in any city" queries. <div