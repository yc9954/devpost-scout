---
slug: "rehearsal"
url: "https://devpost.com/software/rehearsal"
title: "Rehearsal"
hackathon: "Cloud Run Hackathon"
organization: "Google"
winner: true
words: 792
team_size: 1
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/voice_speech"
  - "domain/developer_tools"
  - "domain/finance_payments"
  - "domain/health_clinical"
  - "user/patient_family"
  - "substrate/geospatial"
  - "substrate/video_visual"
  - "substrate/web_dom"
---

# Rehearsal

> Street View + Gemini = Your safe space to mess up in 37 languages.

[Devpost](https://devpost.com/software/rehearsal) · hackathon [[Cloud Run Hackathon]]

## Facets

**mechanism** [[voice_speech]]
**domain** [[developer_tools]] [[finance_payments]] [[health_clinical]]
**user** [[patient_family]]
**substrate** [[geospatial]] [[video_visual]] [[web_dom]]

**stack** cloudrun, firebase, gemini, google-maps, google-web-speech-api, googleaistudio

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for rehearsal

## Body

Inspiration It started during a work trip to Cairo. Every day, my local colleagues would teach me a few words or phrases (usually things I had failed to say the day before, or ones I might need for tomorrow). I really enjoyed using these words to communicate with locals, I even said “Good morning” in Arabic about 800 times. Even if I messed up (and that happened quite often), I could just try again and learn it instantly. But not everyone can do that. Most people freeze or hesitate, and when they travel abroad, they find it hard to fit in. That made me realize: people need a safe space to rehearse and build confidence before diving into a foreign language environment. Then I discovered something weirdly perfect — Google Street View. Sometimes when you drop into a location, you don’t know where you’ll land. Once, I ended up inside a restaurant, sitting across from a man holding a drink and looking right at me. It was accidentally the most immersive language learning moment ever. That randomness, that sense of “I shouldn’t be here but I am”, inspired Rehearsal. What it does Rehearsal turns Google Maps into an interactive language playground. Drop Pegman anywhere and start talking to AI-generated locals — each with their own accent, language ability, and personality. Yes, I know you might think: “Oh no, not another language learning tool.” But look, this one couldn’t exist without Google Maps. Street View gives a sense of place that no other platform can, because you actually feel the environment you’re trying to speak in. That’s where learning happens. Rehearsal isn’t about learning words, it's about learning the world. It’s about recreating the real-world confusion and magic of landing somewhere new, encouraging you to explore, make mistakes, and keep talking. How we built it Honestly, I still have no idea what I'm doing. This project started life as my entry for the Google Chrome Built-in AI hackathon (still waiting for results - fingers crossed!). But when I saw this hackathon, I thought it would be a good chance for some updates. The biggest upgrade: Now it's a fully deployed web app that anyone can access! The new feature that changed everything: Map markers that track your conversation history. Every time you practice, a little pin appears saying "You ordered coffee here!" or "You got lost here!" However, everything lives in your session for now - refresh and you start your journey fresh (hey every day is a new adventure!). The tech stack (according to my patient AI assistant): Google Maps API – For that "wait, am I really here?" feeling Gemini API – Powering surprisingly understanding local NPCs Speech-to-text / text-to-speech – So you can practice your pronunciation crimes Session storage – Your stories last as long as your browser tab courage Deployment on Firebase – Because just deploy from ai studio doesn't work (learned that the hard way) Challenges we ran into Deployment hell — Turns out "it works on my machine" isn't a valid deployment strategy. As someone whose previous coding experience was "Hello World" and aggressive Googling, suddenly dealing with CORS, environment variables, and "build failed" messages was... character building. Location accuracy — I thought it’d be easy to let the AI “see” my screen and read the place name in the corner, but apparently AI doesn’t work that way. Voice timing & realism — Teaching AI to react as a human being with a foreigner is not that easy, maybe because it basically knows everything. One-person dev life — Thought would have a rest after the last hackathon, then found this one a week ago. That’s… totally not great for sleep. Accomplishments that we're proud of I built a working prototype that actually talks back. It’s buggy, unpredictable, and occasionally existential. But hey, it's alive. And somehow, it captures the exact feeling of being lost in a new country but trying anyway (and I laughed a lot while testing, which wasn’t planned but felt right.). What we learned Everything. Literally everything. From APIs and rate limits to Markdown syntax, including debugging panic attacks, every step was a crash course. But most importantly, I learned that you don’t have to know everything to start building something that feels right. What's next for Rehearsal As partly mentioned before, I want to push immersion further including adding ambient sounds, enabling more real-data-based interactions (e.g., showing actual shop photos instead of AI-generated ones), or even creating mini-scripts with local characters. On the marketing side, I’d love to see collaborations: celebrity cameos, pop-up stores, or virtual events hidden in real-world map spots. There’s a huge space between learning a language and living in one. That’s the space Rehearsal wants to play in. <div