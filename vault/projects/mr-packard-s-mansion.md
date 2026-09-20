---
slug: "mr-packard-s-mansion"
url: "https://devpost.com/software/mr-packard-s-mansion"
title: "Mr. Packard's Mansion"
hackathon: "Meta Horizon Creator Competition: Elevate Your Mobile World"
organization: "Meta"
winner: true
words: 1251
team_size: 1
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "domain/immigration_refugee"
  - "user/educator_student"
  - "substrate/video_visual"
---

# Mr. Packard's Mansion

> Play as either a treasure-hunting Intruder or a protective Ghost in this classic arcade-style game. Level up your Hall Pass and unlock new Skins, Perks, and more!

[Devpost](https://devpost.com/software/mr-packard-s-mansion) · hackathon [[Meta Horizon Creator Competition- Elevate Your Mobile World]]

## Facets

**mechanism** [[realtime_stream]]
**domain** [[immigration_refugee]]
**user** [[educator_student]]
**substrate** [[video_visual]]

**stack** typescript, unity, worlds

## How they structured the write-up

- mobile optimization
- technical updates
- npcs
- mr. packard's hall pass (progression)
- quests and leaderboards
- onboarding
- sharability
- miscellaneous
- how i built it & challenges
- accomplishments
- what's next for mr. packard's mansion

## Body

Onboarding: The player lobby, grab a cart to get started Onboarding: The new Animatronics will guide you into the mansion Progression: Upgrade your Hall Pass to unlock all sorts of things! Progression: Unlock and utilize Perks as an Intruder Progression: Unlock new Ghost Classes to play as Progression: Complete Quests to earn Tokens and Skins Shop: Purchase and use new Ghost skins At least the NPCs will keep you company now In Mr. Packard's Mansion, players can choose to play as Intruders who are attempting to escape from a haunted mansion (perhaps with some valuables in tow), or a Ghost defending their master's home. It features a short core loop focused at mobile players, instant action, and satisfying progression via a player's Hall Pass which unlocks Ghost Classes, Intruder Perks, and cosmetics. I created Mr. Packard's Mansion for the last game jam, Meta Horizon Creator Competition: Mobile Genre Showdown. I was not a winner, unfortunately, but I was excited to have an opportunity to expand upon the experience I was developing. The previous iteration was riddled with bugs and had only the concepts of a game. With this new update I've brought a whole new refresh to the game. You can pretty easily compare it to where it was just a few weeks ago by checking my previous game jam entry . ALL updates were done between the beginning and end of this jam. Read on to see what's changed... Mobile Optimization The original version of the game was geared toward VR versus Mobile. While that was an okay idea, one of the main things I wanted to change was that I wanted the entire game to be fully playable and optimized for mobile devices. Mobile can now play as Intruder or Ghost All world interactions and quest interactions have been redone to use mobile-activatable trigger zones VR still works and is being kept at parity with the mobile version The game's core loop of Intruders solving multiple puzzles and escaping the mansion can be completed in less than 5 minutes while Ghosts are instant and continuous action. Technical Updates The Teams API is utilized for all decisions on whether players are Intruders/Ghosts/Other (also, see auto-balancing notes under NPCs) The Camera API is utilized for many different perspectives: first-person, third-person, and top-down depending on the context Asset pooling is used to distribute local player UIs and other systems Dozens of sound effects, voice-overs, and multiple pieces of music added NPCs The game simply felt too empty without constantly having players in it, so I developed NPCs to play both Ghosts and Intruders. These NPCs are auto-balanced up to 7 NPCs total currently (i.e. 1 real Intruder, 3 NPC intruders, 4 NPC ghosts). This means that the game should feel fun to play with anywhere from 1 to 10 players. Ghost NPCs: The Ghosts will wander between quest locations and hiding spots, occasionally hiding for a brief period of time. If they see an Intruder they will chase after them until they lose Line of Sight. Intruder NPCs: The Intruders will act as real players and run around the mansion grabbing items and attempting to solve their puzzles in order to escape. They will occasionally divert to grab traps and set them up. They flee from Ghosts and attempt to recalculate new paths. They have basic unstuck logic for jumping and re-pathing. Each NPC Intruder has its own Avatar, name, and individual speeds and logic for their personality. Mr. Packard's Hall Pass (Progression) This is the main form of progression in Mr. Packard's Mansion. You can gain XP on your Hall Pass by: Running over Intruders as a Ghost Collecting relics as an Intruder Completing puzzles and escaping as an Intruder Loadouts Gaining levels on your Hall Pass will unlock Ghost Classes and Intruder Perks. Trap Expert (Level 5): Traps last longer and trap Ghosts for longer. Bookworm (Level 10): Can open bookshelves without books on cooldown. Acrobat (Level 15): Can make a giant leap on cooldown. The Painter (Level 20): Can paint over Ghost Hiding Spots on cooldown and make them unusable. Caffeine Addict (Level 25): Moves faster, coffee gives double speed but half duration. Master Thief (Level 30): Hide inside Ghost hiding spots. Jail time reduced by half. Move 25% faster when holding a quest item. 10% chance when completing a quest objective to skip to the key escape objective. Basic: Has a dash ability on cooldown. Trickster (Level 10): Disguise as an Intruder on cooldown. Boogieman (Level 20): Can turn off some lights. Has no ghost light. Has 1.5x move speed. Banshee (Level 30): Scream at Intruders in a straight line, slowing those who are hit. Ghost Shop And you'll also gain tokens that you can use in the Ghost Skin shop. Quests and Leaderboards There are now Quests that reward either Ghost Tokens or even Ghost Skins! Leaderboards have been updated and added for the two main stats. Onboarding There is now a dedicated onboarding sequence using custom animatronics in a theme-park style environment to give a quick tutorial to new players. The entire experience takes only a minute or so, but you can skip it and enter the game nearly instantly, of course. Sharability Intruders that successfully escape the Mansion find themselves exiting the ride back to the lobby while Confetti goes off and Mr. Packard congratulates them. This allows players to have a moment to show off to anyone else in the lobby, or to take some pictures. Miscellaneous Apart from the stuff listed above, the entire Mansion has been redesigned to have less areas that players can get trapped, more quest item spawns, and more rooms in general. Hundreds of bug fixes, tweaks, etc. How I Built It & Challenges Many long nights were spent in TypeScript, but overall it's amazing how much you can get done with the tools provided in Worlds. All of my unlockable Ghost skins are 3d models generated directly in the editor and they turned out great. The biggest challenge was finding enough time to work on this while also working full-time as a game-dev in my day job, I even took PTO to finish this all in time. Accomplishments I'm very proud of almost everything I have built for this game jam. The project has come from a simple tech demo to a game that I'm quite proud of. The NPCs work well and are pretty robust, I have fun progression systems in place, and I have spent a good amount of time fixing bugs and testing everything. What's next for Mr. Packard's Mansion There's still so much I'd like to mess around with. But some of the main things I'd like to try out: Seasonal events. Especially with Halloween coming up, it would be a lot of fun to host special events with a special ghost skin (I've already got one made!) Having a GenAI announcer (Mr. Packard) who talks about what's happening around the mansion Different levels. I would like to use world streaming to be able to both randomize worlds and do different ones (think a haunted carnival, asylum, or ancient pyramids with mummies). Maybe different levels could have different Ghost Skins More in-depth puzzles. Maybe the final key is locked in a safe and you have to find the numbers for the combination to open it and it's random per player per game It would be nice to upgrade the escape sequence to have even more pizzazz like fireworks shooting off and VFX playing <div