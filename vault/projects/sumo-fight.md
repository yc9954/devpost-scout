---
slug: "sumo-fight"
url: "https://devpost.com/software/sumo-fight"
title: "Sumo Fight"
hackathon: "Meta Horizon Creator Competition: Mobile Innovation"
organization: "Meta"
winner: true
words: 580
team_size: 4
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "user/developer"
  - "substrate/geospatial"
---

# Sumo Fight

> Mobile K.O. Mayhem! Quick 2-min rounds! Dash & headbutt friends off the platform. Easy to master controls and an addictive game loop. Chain together multiple hits for epic knockback finishes!

[Devpost](https://devpost.com/software/sumo-fight) · hackathon [[Meta Horizon Creator Competition- Mobile Innovation]]

## Facets

  <sub>weak: realtime_stream, vision_ocr</sub>
  <sub>weak: finance_payments</sub>
**user** [[developer]]
**substrate** [[geospatial]]

**stack** horizon

## Body

Mobile Thumbnail - Winter Event World Broadcast - Live updates in game Leaderboards & UI Winter Event - Map Elimination - Tap to Move kill World Broadcast - Base Map Sumo Fight is a high-intensity, social arena brawler that reinvents platform fighting mechanics for mobile play. It utilizes a unique Knockback Scaling Factor system to reward aggressive, short-session engagements. We implemented multiple, accessible control schemes, ensuring every mobile player finds a comfortable layout. These options include: Joystick & Dash Tap to Dash Tap to Move, Swipe to Dash We also utilize World Broadcast with live in-world correspondent commentary reacting to ongoing game events. Leveraging Enemy NPCs , we create an even more epic viewing experience no matter the player count! Inspiration Inspired by the high-intensity mechanics of Super Smash Bros , we recognized a gap for a competitive, mobile-first social brawler . Sumo Fight democratizes the genre, removing expensive hardware barriers to create a game where the core loop is accessible, sessions are short (2-3 minutes), and the fun hinges on chaotic social interaction. What it Does Players compete to knock each other off a platform using only a Headbutt input. The unique Knockback Scaling Factor (KSF) increases launch distance with every hit, providing the escalating gratification necessary for quick mobile sessions: $$\text{Launch Distance} = (\text{Base Force} * \text{KSF})$$ How We Built It Built explicitly for mobile, we prioritized visual clarity with a high-contrast Tron-like aesthetic and restricted UI to minimize small-screen clutter. We designed intuitive, adjustable controls supporting multiple input types (Joystick, Tap-to-Move, etc.). Our core logic features custom physics calculations for accurate collision detection. Using the NPC API, we were able to create engaging enemy NPCs who double as engaging elements for the World Broadcast feature. Finally, we leveraged Generative AI for game assets and our Epic Announcer NPCs . Challenges We Ran Into Designing for on-the-go play with sound off was critical. We created a strong visual feedback loop (particles, screen shake & haptics) so players never miss events without audio. We also simplified complex movement into a single, responsive Dash mechanic, solving the lack of VR or keyboard inputs while maintaining competitive depth. Accomplishments That We're Proud Of We are proudest of optimizing a deep competitive loop into a single-button experience. The Epic Announcer adds immediate positive reinforcement, ensuring the "early and frequent gratification" essential for mobile retention. NPCs feel natural and adapt to the changing environment, also joining and leaving to remain at a constant player count of four. We are proud also of starting a prototype of this project from scratch at the Barcelona SensAI Hackathon, where we took second place for the Horizon Worlds category and were encouraged to continue to develop the experience and submit it to this larger competition. What We Learned We learned to balance simplicity with depth. Lighthearted humor is vital to drive social fun , making quick mobile sessions satisfying without being overwhelming. Dropping in and out was important, and NPCs help fill in the gaps when friends are offline. What's Next for Sumo Fight We are building a Progression System with unlockable cosmetics to encourage return visits. We will also integrate custom emotes to enhance nonverbal communication for players in public environments. Team and Development This world was developed by a dedicated four-person team leveraging a wide array of skills to deliver a polished, mobile-optimized experience: Ektor Zoidis - Gameplay Programmer Lewis McIntyre - Gameplay Programmer Lewis Banks - 3D Art Brian Allen - Studio Director <div