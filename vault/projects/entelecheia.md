---
slug: "entelecheia"
url: "https://devpost.com/software/entelecheia"
title: "Overseer.exe"
hackathon: "LA Hacks 2026"
organization: "LA Hacks"
winner: true
words: 603
team_size: 2
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/simulation_digital_twin"
  - "domain/education"
  - "domain/housing_homeless"
  - "domain/immigration_refugee"
  - "user/patient_family"
---

# Overseer.exe

> Online child exploitation cases jumped from 675 to 24,000+ since 2019. Overseer.exe is a Roblox game that teaches kids to spot grooming and scams in-game, before they meet them in real chats.

[Devpost](https://devpost.com/software/entelecheia) · hackathon [[LA Hacks 2026]]

## Facets

**mechanism** [[simulation_digital_twin]]
**domain** [[education]] [[housing_homeless]] [[immigration_refugee]]
**user** [[patient_family]]

**stack** gemini, httpservice, humanoiddescription, luau, openrouter-api, proximitypromptservice, remoteevent, replicatedstorage, roblox-engine, roblox-studio, runservice, tweenservice, userinputservice, viewportframe

## How they structured the write-up

- inspiration
- the problem
- the solution: overseer.exe
- challenges we ran into
- accomplishments that we’re proud of

## Body

Overseer.exe Inspiration Growing up in digital worlds, we learned that understanding online safety is just as important as mastering the game itself. While platforms today have strong safety features, we wanted to build an experience that actively teaches players why those rules exist — like why you should never share passwords or move conversations to unmoderated, third-party apps. We built Overseer.exe , a game where recognizing digital boundaries is the core mechanic. Unsafe requests — like asking for a username or trying to bypass safe chat — are disguised as in-game survival scenarios. By using a dynamic educational simulator to generate roleplay scenarios, players don’t just memorize static safety warnings — they learn to recognize the underlying patterns of manipulation. We’re giving young players the instincts they need to navigate the internet safely and confidently. The Problem As digital ecosystems grow, empowering young players to protect their personal information is a top priority. Often, safety education relies on static warnings or quizzes. How can we teach players to recognize and prevent unsafe online behavior before it happens, using the medium they love most? The Solution: Overseer.exe Overseer.exe is a sci-fi strategy game set in 2031, after a cyborg infection has overrun Earth. The player serves as the last Overseer at Checkpoint 7 , a fortified survivor base at the edge of the wasteland. Refugees arrive seeking shelter — but some are infected impostors trying to infiltrate. The player must inspect each visitor and decide who gets through. The core gameplay loop consists of three connected phases : Gate Inspection Players analyze each visitor’s credentials and appearance (glowing eyes, robotic limbs, glitched textures). Through branching dialogue, they must classify each character. Impostors look believable — teaching players the importance of verifying information and asking the right questions. Hangout Zone Approved survivors enter a shared space where a dynamic roleplay system generates live dialogue between NPCs. These interactions mimic real-world safety scenarios, such as: Requests for secure codes Attempts to move conversations off-platform Players must monitor behavior, detect unsafe requests, and remove bad actors before the infection spreads. Boss Fight Payoff Surviving the round unlocks a boss fight where every protected NPC returns as a combat ally. Your social decisions directly affect combat difficulty. The result is a tight gameplay loop where pattern recognition isn’t optional — it’s how you win. Challenges We Ran Into Scope Creep vs. Cohesion Initially planned a multi-round system Pivoted to a single high-stakes 5-minute loop Result: tighter, more focused gameplay Mid-Hack Boss Rebuild Original boss felt disconnected from the core experience Rebuilt into a unified combat system with integrated mechanics Technical Polish Procedural rendering caused visual pop-in issues Fixed with a pre-load overlay + seamless fade transition Version Control Merge conflicts broke dialogue systems mid-hack Overcoming them ultimately improved stability By prioritizing cohesion over scale, we delivered a polished vertical slice instead of a fragmented system. Accomplishments That We’re Proud Of Despite the challenges, we built a complete, polished experience in just 36 hours using Roblox Studio: A five-room playable facility 26 hand-crafted visitor archetypes with branching dialogue Dynamic, educational safety and roleplay scenarios A social-deduction infection system An upgrade shop and boss fight system Key accomplishments include: Creating a fully connected gameplay loop where decisions impact outcomes Teaching real online safety patterns through engaging gameplay Safely generating dynamic roleplay scenarios that make learning feel like gaming, not instruction Games already teach players economies and complex social systems. There’s no reason they can’t teach digital literacy the exact same way. We hope Overseer.exe becomes an early example of what this empowering new genre can look like on Roblox. <div