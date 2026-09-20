---
slug: "o-p-t-i-m-i-z-e"
url: "https://devpost.com/software/o-p-t-i-m-i-z-e"
title: "O P T I M I Z E"
hackathon: " Play Everywhere: The Build with Snap Games Lensathon"
organization: "Snapchat"
winner: true
words: 1016
team_size: 1
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/deterministic_policy"
  - "domain/developer_tools"
  - "domain/health_clinical"
  - "user/developer"
---

# O P T I M I Z E

> A replayable, narrative-driven rhythm game for Snapchat that unfolds across multiple sessions. Persistent progression, performance-based levels, and leaderboards turn a lens into a full mobile game.

[Devpost](https://devpost.com/software/o-p-t-i-m-i-z-e) · hackathon [[Play Everywhere- The Build with Snap Games Lensathon]]

## Facets

**mechanism** [[deterministic_policy]]
**domain** [[developer_tools]] [[health_clinical]]
**user** [[developer]]

**stack** javascript, lensstudio, snap

## How they structured the write-up

- about the project
- narrative & tone
- gameplay inspiration
- longform design & persistence
- tooling & technical challenges
- feel, feedback, and ux
- visual design & polish
- what i learned
- closing thoughts

## Body

An ominous story, do you know what's happening? Gameplay with 3 objects. 2 circles and a slider. About the Project This project started very small. At the beginning of the hackathon, I was just experimenting with an osu!-style rhythm demo inside Lens Studio. I wanted to see if responsive, timing-based gameplay was even possible on a platform that isn’t designed for longform games. What began as a technical test quickly grew into something much more ambitious and passionate. My path to this project is very tied to Snapchat itself. During the pandemic, I started making lenses after seeing how creative face filters could be. Five years later, with a degree in game design and deep familiarity with Lens Studio’s quirks and constraints, I’m now able to build complex, multi-system experiences that most lenses never attempt. As the prototype came together, I realized I didn’t just want to make an arcade-style rhythm game. I wanted to make a complete game . Something with a beginning, middle, and end. Something you could return to across multiple sessions. Something intentional, unsettling, and polished rather than disposable. I don’t see many Snapchat games living in this niche, but it’s the one I get the most satisfaction building. That realization pushed the project in a new direction: a narrative-driven, longform rhythm game built specifically for Snapchat. Narrative & Tone The story is deliberately restrained and system-driven. I spent a lot of time choosing wording that felt clinical and trustworthy at first, while slowly becoming unsettling as the experience progressed. The goal was to let players feel safe on their first playthrough, and only later realize something was off. To contrast the darker tone of the narrative, I worked closely with a musician to create a parody of Carmelldansen . Using a playful, dance-heavy vocaloid track helped preserve the joy and adrenaline of rhythm games, while making the narrative tension more uncomfortable by comparison. That contrast became one of the core pillars of the experience. Gameplay Inspiration The gameplay itself is inspired by Japanese arcade rhythm games, the kind you play standing in front of a cabinet, chasing that perfect, on-the-beat hit. I wanted to recreate that physical rush of timing something just right, even on a mobile device. The game supports two main ways to play: Narrative-focused play , where the goal is simply to pass levels and experience the story Mastery-focused play , where players aim to perfect each level, maximize accuracy, and submit a cumulative score to the global leaderboard Some paths make it easier to complete the story but harder, or impossible, to achieve the highest score. This encourages replay without forcing it. Longform Design & Persistence This project was intentionally designed as a longform experience , not a short-lived lens. Players don’t need to complete everything in one sitting. Progress is saved, and the game encourages returning across multiple sessions. Difficulty increases gradually across levels, and the final outcome depends on both player performance and choices made along the way. This structure was important to me. I wanted players to feel ownership over how they engaged with the game, whether casually or competitively. Tooling & Technical Challenges One of the biggest challenges was building reliable rhythm gameplay on a platform where audio playback timing is not always accurate, at least on my machine. To solve this, I built a custom beatmap recording tool. Instead of relying on Lens Studio’s audio timing, I recorded beat placement based on a known BPM and offset. While playing the song externally, I could record hit timings in one pass, round them to musical time, and export the data into a JSON-like format that defined timing, placement, and object type (circle vs slider). { type: "circle", t: 3188, x: 352, y: 691 }, This allowed each level to load beatmaps deterministically and made iteration possible without manually placing every note by hand. It did come with tradeoffs. Recording had to be done in a single take, and editing wasn’t trivial. Still, it was a practical, scalable solution that made the game possible at all. Feel, Feedback, and UX A lot of work went into making the game feel good, even when the underlying systems weren’t perfect. I implemented techniques to smooth timing alignment so hits feel synchronized with the music, compensating for both input and device latency. These techniques are common in rhythm games, but applying them within Snapchat required careful tuning. Playtester feedback shaped many features: A “next hit” marker was added after early testers struggled to read patterns Marker clarity and slider direction were refined for accessibility Haptic feedback and audio reminders were added to improve physical feedback and first-time experience These changes didn’t add new mechanics, but they dramatically improved completion rates and player confidence. Visual Design & Polish I paid close attention to visual hierarchy, transitions, and pacing. Rather than overwhelming the screen, in-game visuals change subtly over time to reflect musical sections without interfering with gameplay. Menus, results screens, and narrative transitions were designed to feel intentional and cohesive. My goal was for the experience to feel closer to a finished mobile game than a prototype lens. What I Learned This project reinforced how important constraint-driven design is. Snapchat is not an obvious platform for longform games, but those limitations forced me to be deliberate with scope, pacing, and polish. Most of all, I learned that longform games on unconventional platforms are possible, but only if you treat them like real products rather than tech demos. This is where I feel most at home. I don’t feel satisfied until the small things are complete and the experience actually makes you feel something when you play. Closing Thoughts This project represents my goal as a game developer: to build experiences that feel complete, thoughtful, and worth returning to. It blends narrative, rhythm gameplay, and persistent progression into something that challenges both players and the platform it’s built on. I’m proud of how much care went into every layer, from tooling and systems to UX, narrative, and polish, and I hope players feel that intention when they play. <div