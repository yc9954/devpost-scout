---
slug: "y2k-jump-avatar-outfit-xfve5r"
url: "https://devpost.com/software/y2k-jump-avatar-outfit-xfve5r"
title: "Y2K Jump"
hackathon: "Meta Horizon Creator Competition: Mobile Innovation"
organization: "Meta"
winner: true
words: 615
team_size: 3
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "user/educator_student"
  - "substrate/video_visual"
---

# Y2K Jump

> Y2K Jump is a casual portrait platform jumping game that uses Y2K fashion as powerups with simple yet addictive one-touch controls.

[Devpost](https://devpost.com/software/y2k-jump-avatar-outfit-xfve5r) · hackathon [[Meta Horizon Creator Competition- Mobile Innovation]]

## Facets

**user** [[educator_student]]
**substrate** [[video_visual]]

**stack** adobe-illustrator, audacity, blender, claude, desktop, editor, horizon, noesis, photoshop, typescript, world

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for y2k jump

## Body

Press hold to charge jump and release to move avatar Bullseye landing Buy clothing powerups Extra life powerup WorldID: 849132481620439 Inspiration Y2K Jump is a portrait platform-jumping mobile game inspired by Y2K style, turning 2000s fashion into powerups, retro tech into platforms, with a cybercore UI. What it does This casual game challenges players to score as high as possible by accurately timing jumps between platforms. Core gameplay loop : Use a simple one touch movement control—press down to charge the jump & release to move the avatar from one platform to another. Progression system : Newly spawn platform’s direction is randomized and size shrinks as the game progresses. Use avatar clothing with powerups to gain an advantage. Unique features : Customize avatar with our custom clothing traits system to apply these powerups. a. Extra life - when avatar misses platform. b. Easy bullseye - makes it easier to land in the center of platform. c. Bonus points - points multiplier for every successful landing. d. Shrink slower - enables platform to shrink at a slower rate. Custom daily claim system with avatar items as rewards. NoesisUI to quickly build beautiful and complex UI. Scripted avatar movement to rotate the avatar to face the next platform. Custom avatar animation including charging, jumping, falling forward, falling backward. Camera adjusts its angle for each clothing category to provide better visual clarity. Mobile-first features : Simple one touch control that’s intuitive to learn. Portrait mode for comfortable one-handed play. Haptic feedback for gratification to keep players engaged. Clothing creation : 80 avatar clothing (tops, bottoms, shoes, one pieces) are influenced by 2000s futuristic millennium, pop princess and streetwear fashion styles. Powerup clothing enhances gameplay through strategic customization, rewarding progression, and creating visual status. Rarity stars highlight clothing value using Digital Item Tiering in UI. Structure item tiers by sequentially reducing unique clothing counts and increasing cost & powerup value from Common to Premium to Elite. Marking clothing as Owned or Not Owned on UI, creates a visual progress tracker and collection checklist. Claim a daily gift of clothing incentivizes players to log in consistently. Camera angle provides a clear front view of the clothing on avatar. How we built it We used a hybrid UI approach combining Noesis and Custom UI. Noesis facilitated immersive animations, while Custom UI managed the avatar item scrollview (due to a Noesis bug) and integrated store purchases. Gameplay utilized the Observer pattern for scripting and a platform pooling system for efficiency. Avatar movement is driven by .applyForce, with powerups detected via avatar SKU to enable our custom traits system. Camera transitions relied on .setCameraModeAttach. We used Focused Interaction Mode for a minimalist HUD. Challenges we ran into Challenging to master Noesis due to limited tutorials for portrait overlay UI in Horizon Worlds. Creating the avatar item selection was difficult, necessitating a hybrid Noesis/Custom UI approach due to the scrollview bug. We overcame the lack of native avatar traits by creating our own system that detects clothing SKUs for power-ups. Finally, we resolved an unwanted shaky camera issue during player movement by switching from onWorldUpdate to the stable .applyForce method. Accomplishments that we're proud of 80 custom made Y2K outfits. Our custom clothing traits system and custom daily claim system as no access to these 2 features yet. How to use Noesis in a short time as a workaround for the Noesis bugs. What we learned How to use Noesis. Implement a portrait mode. Avatar clothing traits. How to use focused interaction mode. What's next for Y2K Jump Expand progression system with obstacles Increase variety of quests that can unlock avatar clothing powerups as rewards More types of powerups More clothing items Multiplayer <div