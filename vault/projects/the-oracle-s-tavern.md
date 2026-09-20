---
slug: "the-oracle-s-tavern"
url: "https://devpost.com/software/the-oracle-s-tavern"
title: "The Oracle's Tavern"
hackathon: "DeveloperWeek 2025 Hackathon"
organization: "DevNetwork"
winner: true
words: 546
team_size: 1
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/voice_speech"
  - "domain/mental_health"
  - "domain/retail_commerce"
  - "user/small_business"
  - "user/social_worker"
  - "substrate/financial_record"
---

# The Oracle's Tavern

> Imagine being an LLM in the Dark Ages—guiding medieval travelers with wisdom and wit? Welcome to The Oracle's Tavern!

[Devpost](https://devpost.com/software/the-oracle-s-tavern) · hackathon [[DeveloperWeek 2025 Hackathon]]

## Facets

**mechanism** [[voice_speech]]
**domain** [[mental_health]] [[retail_commerce]]
**user** [[small_business]] [[social_worker]]
**substrate** [[financial_record]]

**stack** deepseekv3, express.js, fingerprintjs, meta-llama, mongodb, nebiusai, node.js, phaserjs, react, tears, twilio

## How they structured the write-up

- inspiration
- what it does
- how i built it
- challenges i ran into
- accomplishments that im proud of
- what i learned
- what's next for the oracle's tavern

## Body

FingerprintJS enabled browser-specific questions / also how questions look like GIF All our character cards! Evaluation of thy answers with deepseek v3 GIF 10 unique characters all with their unique questions and problems! Twilio summaries and hints when requested :) MongoDB to showcase how visitorID is used to track users' points without any login whatsover Inspiration The Oracle's Tavern was born from a whimsical "what if" scenario: What if large language models (LLMs) like ChatGPT existed in the dark ages? What kind of questions would it be asked? Furthermore, how would it feel to BE one of these LLMs? Well "The Oracle's Tavern" is your answer to these (important) questions. I wanted to blend the mystique of such a world with modern AI, creating a playful yet immersive experience where travelers, knights , merchants and even Kings seek wisdom from you, the Oracle that knows all. What it does The Oracle's Tavern is an interactive game where players step into a medieval tavern filled with quirky characters like knights, merchants, and grave diggers. Each NPC presents unique, AI-generated dilemmas (e.g., A valiant knight asking how he can hide his treasures or a merchant puzzling about where to bury a body). Players type in their advice, which is evaluated by AI, scored and they can earn titles like "Royal Counselor" as they progress further and answer more questions. Features include dynamic voice acting powered by Elevenlabs, SMS hints and summaries every 5 rounds via Twilio, player identification (without login!) ,easter eggs and browser-specific questions powered by fingerprint and a responsive world with animations and soundscapes powered by phaserJs. It’s part choose-your-own-adventure, part AI playground, wrapped in a medieval aesthetic. How I built it Frontend: React and Phaser.js created the tavern environment with pixel-art animations and touch-friendly UI. Backend: Node.js/Express handled AI integrations, storing player progress in MongoDB. LLMs: Nebius AI generated character-specific questions with meta llama instruct and evaluated answers using deepseek v3, while ElevenLabs gave voices to each NPC. SMS: Twilio sent humorous, medieval-themed hints when requested and summaries of the player's progress every 5 rounds of questioning. FingerprintJS: Browser-specific questions and easter eggs and visitor tracking to reward ranks and keep track of players without storing sensitive information (or even logging in!) . Audio: sound effects for all interactions and music! Challenges I ran into Syncing ElevenLabs’ text-to-speech with Phaser.js animations without lag. Designing mobile-responsive Phaser.js scenes that retained detail on smaller screens. Balancing AI-generated questions to fit medieval themes while avoiding anachronisms. Accomplishments that Im proud of Seamlessly integrating four distinct APIs (ElevenLabs, Nebius, Twilio, FingerprintJS) into a cohesive experience. Trying to get this to make sense and actually work Designing a responsive Phaser.js environment that works flawlessly on desktop and mobile. What I learned Technical: Combining game engines (Phaser.js) with React for complex state management. AI Limitations: Fine-tuning prompts to keep generated content historically consistent and archaic. User Experience: The importance of audio-visual feedback (e.g., subtle tavern sounds, transaction completion jingle) for immersion. What's next for The Oracle's Tavern Multiplayer Mode: Let players collaborate or compete in guilds. Expanded Storylines: Quests spanning multiple tavern visits, with consequences for advice given. Custom Avatars: Allow users to create their own medieval traveler. Localization: Offer dialogues in Old English or other languages for deeper roleplay. <div