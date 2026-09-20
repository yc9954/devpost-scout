---
slug: "spell-swiper"
url: "https://devpost.com/software/spell-swiper"
title: "Spell Swiper: Defend the Kingdom!"
hackathon: "Meta Horizon Creator Competition: Mobile Innovation"
organization: "Meta"
winner: true
words: 771
team_size: 6
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "domain/disaster_emergency"
  - "domain/education"
  - "substrate/video_visual"
---

# Spell Swiper: Defend the Kingdom!

> Spell Swiper is an arcade-style, pick up and play mobile game where you trace shapes with your finger to cast spells. Use this power to pop balloon-riding monsters, and protect the castle!

[Devpost](https://devpost.com/software/spell-swiper) · hackathon [[Meta Horizon Creator Competition- Mobile Innovation]]

## Facets

**domain** [[disaster_emergency]] [[education]]
**substrate** [[video_visual]]

**stack** blender, horizon, noesis

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for spell swiper

## Body

Our Logo and Landscape World Image Spell Swiper Main Menu - you get assigned a special wizard robe when you join! Gameplay in action! More enemies approach! Game Over Screen Leaderboard in action! Can you get in the top ten? Behind the scenes look at our world! Another behind the scenes look at our world! Our first world blockout. Enemy Models An early version of the game Another early version of the game Yet another early version of the game! Inspiration Spell Swiper: Defend the Kingdom! started with a simple question: What if spell-casting was as satisfying as slicing fruit? We wanted a game that anyone could instantly understand: draw the shape, cast the spell, save the castle, but with enough hidden depth to reward skill and mastery. Mixing the kinetic fun of Fruit Ninja with the nostalgia of old-school rune-drawing games, we focused on creating a one-handed mobile experience that still makes you feel powerful. Examples of our iteration progress: What it does In Spell Swiper: Defend the Kingdom! monsters drift toward your castle on enchanted balloons after being launched in the air by a nearby catapult. Each balloon has a weakness though, a shape that you can cast to pop them! This could be a circle, line, or zigzag shape, for instance. The core loop becomes a quick, satisfying rhythm of gesture → feedback → explosion as enemies flood in faster and faster. It’s simple to learn, but as more shapes and enemy variations appear, it transforms into a game of timing, awareness, and mastery. Tip: If you're having issues registering the straight line, vertical or horizontal, make sure that you make a longer line. It doesn't register short gestures very well. How we built it The game was developed entirely using Horizon Worlds’ World Editor, with Noesis UI powering the title screen and leaderboard. Our earliest prototype was hilariously forgiving, any scribble counted as a “spell,” which was fun for a minute but not a real game. So we built a custom gesture recognizer from scratch and iterated over it dozens of times until it felt fair, readable, and reliable. Once the core mechanic clicked, we layered in particle effects, floating animations, polished hit reactions, and a difficulty curve that moves from relaxing to chaotic. Light, optimized scripting kept things smooth on mobile, and we designed the entire experience around portrait mode for a true mobile-first feel. Challenges we ran into Gesture recognition was our biggest boss battle. Tiny differences in line curvature or stroke order could make the game feel too strict or too easy. Balancing that element took a lot of playtesting. We also had to rethink traditional VR-friendly Horizon Worlds layouts because portrait mode compresses everything vertically. Reading action and incoming threats in a tall, narrow frame required major adjustments to camera placement, enemy spacing, and timing. Keeping the game visually exciting without tanking mobile performance is another ongoing challenge. Accomplishments that we're proud of We created a spell casting system that feels magical. Shapes read cleanly, spells fire instantly, and enemies burst with satisfying feedback. New players can "swipe-mash" and survive for a while, but skilled players can hit a flowing rhythm that feels almost like drawing calligraphy. We’re also proud of pushing Horizon Worlds into a more mobile-native, portrait-optimized experience. It’s a platform where this type of game isn’t common, and seeing it run smoothly feels like opening a new door. We're eager to continue to explore the possibilities there. What we learned We learned that gesture-based gameplay is incredibly sensitive; changing a circle’s tolerance by even a few pixels changes how “fair” the game feels. We discovered how critical animation timing is, especially when players only have a small window of time to take in the input and react to it. Our biggest lesson? Simple ideas become great when you cut away the noise and sharpen the core fun, and hackathons should keep a focused scope in mind. Our previous submissions were larger in scope, but this time we focused on a tight, instantly enjoyable mechanic and that shift made a huge difference. What's next for Spell Swiper We have a lot of ideas queued up: new enemy types, advanced shapes, and boss encounters that require chained gestures or multi-step spell combos. A progression system with unlockable spells and cosmetic upgrades is high on our list, as well as daily challenges and score competitions to keep players returning. Long term, we’d love to explore co-op spell slinging or competitive swipe battles. Spell Swiper: Defend the Kingdom! was intentionally built small and clean, which makes it the perfect foundation for future expansions. <div