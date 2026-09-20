---
slug: "bailao"
url: "https://devpost.com/software/bailao"
title: "Bailão dos Cria"
hackathon: "Meta Horizon Creator Competition: Open Source Champions"
organization: "Meta"
winner: true
words: 937
team_size: 2
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "mechanism/simulation_digital_twin"
  - "mechanism/vision_ocr"
  - "substrate/sensor_telemetry"
---

# Bailão dos Cria

> Bailão dos Cria provides the foundation for any musical Meta Horizon World. With the customizable drum machine asset and dynamic scoring system anyone can create their own musical social experience

[Devpost](https://devpost.com/software/bailao) · hackathon [[Meta Horizon Creator Competition- Open Source Champions]]

## Facets

**mechanism** [[realtime_stream]] [[simulation_digital_twin]] [[vision_ocr]]
**substrate** [[sensor_telemetry]]

**stack** typescript, worldsdesktopeditor

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for bailão dos cria

## Body

DJ playing view Stage and Scoreboard Starting view View from dancefloor Bailão dos Cria Inspiration Our inspiration comes directly from the heart of Brazilian culture: the "Bailes de Favela" (Funk Parties) of Rio de Janeiro. These parties are more than just events; they are powerful expressions of community, creativity, and resistance. We wanted to capture the raw energy, the powerful beat of the tamborzão (the kick drum), and the unique vibe of these gatherings. "Bailão dos Cria" is a tribute to this cultural phenomenon, aiming to democratize access to this experience and allow people from all over the world to feel, even if virtually, the contagious rhythm and the sense of community found in the favelas of Rio. What it does "Bailão dos Cria" is a social musical experience in Meta Horizon Worlds. Users are transported to a virtual environment that simulates a vibrant favela in Rio de Janeiro, complete with iconic visual elements. The core gameplay revolves around a central stage featuring a 9-button drum machine. One player at a time becomes the DJ/MC, stepping onto the stage to create music in real-time by pressing the buttons, each triggering a unique sound. The other players are on the dancefloor, socializing and dancing to the beats created by the player on stage. The performing player is scored based on two key metrics: Activity: They must press at least one button every 5 seconds to keep the energy high and avoid "losing the beat." Crowd Engagement: Their score multiplies based on the number of people present and dancing on the dancefloor. The more people they entertain, the higher their score! How we built it Environment & Art: We built the 3D environment, modeling classic favela architecture with brick walls, stacked houses, to create an authentic and immersive atmosphere. Interactive Elements: The stage, dancefloor, and boomboxes were placed as interactive objects within the world. Drum Machine Logic: The core of the experience is the custom interactive drum machine on the stage. When a button is pressed by a player: Play a specific audio sample. Trigger particle effects for feedback. Send a signal to the scoring system. Scoring System: We built a logic system that: Tracks the time since the active player's last button press. Resets a timer on each successful press. Counts the number of players within the designated "dancefloor" area. Calculates a live score based on these variables and displays it on a leaderboard or score panel. Challenges we ran into Optimization for all platforms: Creating a detailed favela environment while maintaining a stable frame rate on Web, Mobile and VR was a constant balance between visual fidelity and performance. Network Synchronization: We encountered persistent issues with network sync and client desynchronization, particularly with interactive objects like the Text Gizmo, which often required a full scene restart to resolve. World Owner CPU Load: The world owner's client experienced unexpectedly high CPU usage, creating a performance bottleneck and a less stable experience for that user. Asset Sharing Limitations: We were unable to successfully share template assets and prefabs between team members, as the "Shared with Me" folder functionality was unreliable for our project. Limited Editor Testing for Gestures: A proposed mechanic to reward the DJ based on emoji reactions (gestures) from the dance floor could not be prototyped effectively, as these social features are not supported within the World Editor. Accomplishments that we're proud of Cultural Authenticity: We are incredibly proud of successfully capturing the authentic look and feel of a Brazilian baile and translating it into a virtual space. It feels genuine. Engaging Core Gameplay Loop: The simple yet addictive loop of making music for a crowd and being rewarded for it works perfectly. Seeing a group of avatars dancing to a player's improvised beat is incredibly rewarding. Scalable World & Mechanics: The core systems of Bailão dos Cria are designed to be scalable and adaptable. The stage and dance floor mechanics can be easily re-themed to create any type of nightclub or party experience within Horizon Worlds. Efficient Art Pipeline: We established an efficient pipeline for converting and importing existing assets from other projects into Meta Horizon Worlds, successfully maintaining our established visual identity and cohesive art style. What we learned The Power of Simplicity: A project doesn't need extremely complex mechanics to be fun. A clear concept with well-executed core interactions is often more successful. Cultural Representation Matters: The positive reactions from Brazilian users who felt represented and seen in a global metaverse platform was a powerful lesson in the importance of diverse cultural projects. Meta Horizon Worlds is a platform for social game design: It shifts the focus from single-player or conventional multiplayer to facilitating community-driven experiences. This foundation allows for deeply engaging and immersive social roleplay that is actively shaped by its players. What's next for Bailão dos Cria Expanded Sound Library: Adding more drum machines with different sound sets (e.g., 90s Brazilian Funk, Samba, Pagode) to increase musical variety. In-App Purchases: Monetize new sound packs and exclusive audio samples. Implement Gesture-Based Scoring: Develop and integrate the mechanic where the DJ's score is boosted by emoji reactions from the audience, enhancing crowd interaction. Customization: Allowing players to customize their avatar with items like bucket hats, chains, and specific dance moves popular in the funk scene. Advanced DJ Features: Implementing features like a BPM (beats per minute) slider, sample volume control, and record/playback functionality for more creative control. Special Events: Hosting live events with real Brazilian DJs who would use the virtual drum machine to play sets for the Horizon Worlds community, turning "Bailão dos Cria" into a true destination for virtual music events. <div