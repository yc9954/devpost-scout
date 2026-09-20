---
slug: "type-to-death"
url: "https://devpost.com/software/type-to-death"
title: "Type To Death"
hackathon: "Kiroween"
organization: "Kiro"
winner: true
words: 1184
team_size: 2
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/deterministic_policy"
  - "mechanism/realtime_stream"
  - "domain/developer_tools"
  - "domain/health_clinical"
  - "domain/immigration_refugee"
  - "user/patient_family"
  - "substrate/code_repository"
  - "substrate/document_pdf"
  - "substrate/video_visual"
---

# Type To Death

> Strengthen your typing ability through immersive, pressure-based learning.

[Devpost](https://devpost.com/software/type-to-death) · hackathon [[Kiroween]]

## Facets

**mechanism** [[deterministic_policy]] [[realtime_stream]]
**domain** [[developer_tools]] [[health_clinical]] [[immigration_refugee]]
**user** [[patient_family]]
**substrate** [[code_repository]] [[document_pdf]] [[video_visual]]

**stack** anthropic-ai-sdk, convex, fmod, googlemediapipe, kiro-ide, nextjs, react, recraft, shadcn, tailwind, typescript, unity, zustand

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for type to death

## Body

Main Menu Daily AI generated cases Bone-chilling stories Calibrate face detection Compete on the leaderboard Game introduction Game Boo! You win or lose... Inspiration We were brainstorming ways to create a horror experience that felt unique and meaningful, and that could offer real value beyond just scares. That was when the idea of using eye tracking and blinking came to us. We were inspired by the popular 'Weeping Angel' mechanic, where a monster moves closer whenever you are not looking. We wanted to build on that idea and combine it with a simple, skill-based UI experience. A typing game felt like the perfect fit. It is fun, replayable, and something that can genuinely help improve typing skills while still delivering tension and excitement. What it does Type To Death is a horror typing game where every blink brings you closer to death. This game is designed to strengthen your typing ability through immersive, pressure-based learning. By eliminating the habit of looking at the keyboard and encouraging rapid, accurate input, it helps you develop true touch-typing proficiency in a way traditional tools don’t. The game features: Real-time blink detection using Google MediaPipe face mesh analysis Personalized calibration that adapts to each player's unique eye characteristics Daily AI-generated horror cases with progressive chapters of increasing difficulty Character-by-character typing validation with natural error correction A 3D Unity horror scene with atmospheric lighting and a terrifying monster Immersive FMOD audio design that intensifies as the monster approaches Global leaderboards showing real-time high scores When you run out of lives, the monster sprints toward you for a final jumpscare. Survive all chapters, and you escape. Your typing speed and accuracy are recorded for the leaderboard. How we built it We built Type To Death using a modern full-stack architecture with a Unity WebGL game embedded in a Next.js application. Frontend: Next.js 15 with React 19, TypeScript, Tailwind CSS v4, and shadcn/ui components. We used Zustand for state management and the react-unity-webgl package to embed the Unity game. Blink Detection: Google MediaPipe Face Mesh provides 468 facial landmarks in real-time. We calculate the Eye Aspect Ratio (EAR) using specific landmark indices for each eye, then run it through a state machine that distinguishes real blinks from noise. A calibration system measures each player's baseline EAR to ensure accurate detection across different faces and lighting conditions. Game Engine: Unity 6 handles the 3D horror scene. The monster uses a state machine with Idle, Teleport, and Sprint states. Two-way communication between React and Unity happens through a custom interop system using JavaScript plugins and window events. Audio: FMOD Studio powers the sound design with dynamic audio that responds to game state. Proximity-based mixing intensifies the atmosphere as the monster gets closer. Backend: Convex handles authentication, leaderboards, and story storage. Daily story generation uses the Anthropic Claude API with structured tool use to ensure consistent story formatting. Development Approach: We used Kiro IDE with a spec-driven methodology. Every major feature started as a three-document spec: requirements (what to build), design (how to build it), and tasks (implementation steps). Steering rules maintained consistent coding standards across the project, and agent hooks automated spec validation. We started to work on the hackathon very late, with only 18 days left, Kiro made it absolutely easy for us. Challenges we ran into Our original vision used full eye-tracking to detect where players were looking. We tried webgazer.js, which proved too outdated and unreliable. Even with Claude's help implementing Google MediaPipe gaze detection, we could not achieve the accuracy needed for gameplay in this short amount of time. Since we started the hackathon late, we made the strategic decision to pivot to blink detection, which proved far more reliable and created equally compelling gameplay tension. Audio presented unexpected challenges. We encountered stuttering issues on keystrokes because of React re-renders and general audio glitches that broke immersion. Debugging FMOD integration in a WebGL context required careful attention to audio buffer management and event timing. Getting Unity and React to communicate reliably was another hurdle. WebGL builds behave differently than editor builds, and we had to design a robust interop system that handled initialization timing, event dispatching, and state synchronization between two very different runtime environments. On the final day, we added a "Cases" feature with patient portraits, but our basic prompts generated similar-looking images. In a race against time, we built a prompt enhancement pipeline that randomizes character traits (age, gender, ethnicity, build), facial features (eyes, nose, hair, etc.), and story-contextual backgrounds to ensure each patient portrait is unique. Accomplishments that we're proud of We are proud that we were able to build the experience we originally envisioned. Even though we had to adapt our initial idea along the way, we still delivered something polished thanks to our meticulous approach. We are especially proud of the immersive atmosphere and sound design we achieved, and of getting all the different pieces to work together, from accurately detecting blinks to sending that data into the game to make the monster move. We also went the extra mile with small details, such as handling cases where a face is not detected by giving the player a few seconds to return, generating unique images for each patient, offering a patient browser where players can read about them, and ensuring stories do not repeat by tracking used titles and patient identifiers, among other things. We feel good about how well the final result captures the spirit and brief of the hackathon. Creating something creative, immersive, and distinct was very important to us. What we learned AI tooling is advancing remarkably fast. Features that would have taken days to research and implement can now be prototyped in hours with the right approach. Kiro proved to be incredibly powerful for complex projects. The spec-driven methodology forced us to think through problems before coding, which saved significant debugging time. Steering documents were excellent for maintaining context and establishing consistent patterns across the codebase. This was our first time using MCP (Model Context Protocol), and it opened up new possibilities for AI-assisted development. We were able to integrate challenging features with unfamiliar technologies much more easily than expected. The biggest lesson: structured thinking scales. When you are sleep-deprived at 2 AM and something breaks, having documented requirements and design decisions is invaluable. What's next for Type To Death If the interest grows, there are many directions we would love to explore. We might add traditional typing challenges, including tailored difficulty levels that adapt to each player’s skill, and that do not require a webcam so more people can join in. We are also considering new story premises, 3D environments, different monsters, and additional visual themes to keep the experience fresh. They could all still be related to the asylum theme, or not. Gamification features such as streaks, reward points, and progression systems are possibilities we would like to explore as well. On the competitive side, we may look into more advanced leaderboards, tournaments, and stronger anti-cheat mechanisms. There is a lot of potential for expansion, and we are looking forward to seeing where the project can go. <div