---
slug: "inbox-invaders"
url: "https://devpost.com/software/inbox-invaders"
title: "Inbox Invaders"
hackathon: "LA Hacks 2026"
organization: "LA Hacks"
winner: true
words: 1073
team_size: 4
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "domain/finance_payments"
  - "domain/security_privacy"
  - "domain/transportation"
  - "user/educator_student"
  - "substrate/geospatial"
---

# Inbox Invaders

> Inbox Invaders is a Roblox tower-defense adventure where players protect their computer from alien scammers, phishing emails, fake links, and malware, which allows them to enhance their defenses!

[Devpost](https://devpost.com/software/inbox-invaders) · hackathon [[LA Hacks 2026]]

## Facets

**domain** [[finance_payments]] [[security_privacy]] [[transportation]]
**user** [[educator_student]]
**substrate** [[geospatial]]

**stack** claudeapi, luau, robloxstudio

## How they structured the write-up

- inspiration
- what it does
- how we built it
- how it applies to the company challenge
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for inbox invaders

## Body

Home Screen GIF VPN Tower GIF GIF Antivirus Turret GIF GIF Orbit (our friendly Alien) guiding us through the tutorial GIF Learning About Phishing Learning About Privacy Settings Inspiration Online scams are becoming harder to recognize, especially for younger users who engage with various potential attack vectors such as emails, pop-ups, downloads, and messages. We wanted to create a game that teaches digital etiquette and online safety in a fun and engaging format. By building a controlled platform for kids to gain a safe, hands-on learning experience, we aim to cement the concepts of cyber safety and increase retention through active decision-making. What it does Inbox Invaders is a Roblox online safety training game in which aliens attack Earth through social engineering tactics, targeting the player through malicious emails, suspicious files, privacy breaches, distracting notifications, and more. The player must inspect messages and complete various mini-games to earn credits, while mistakes cost credits. In between these activities, players use their credits to build defense turrets against the alien fleet in a tower defense game that teaches about personal cybersecurity mechanisms (VPN, antivirus, firewall, etc.) How we built it We built the project in Roblox Studio using Luau for gameplay systems, UI interactions, scoring, mini-games, player progression, and storyline. We designed the experience around a loop of computer interaction and combat. Players first analyze online threats and play educational mini-games, then use their performance to power the tower defense portion of the game. The result is cybersecurity education that is integrated into traditional Roblox gameplay mechanics. The game is targeted toward a younger audience. Because of this, the UI and tutorial are intentionally simple and easy to follow. We also implemented data persistence, so player progress is saved across sessions. This allows the game to remember important information like player progression, credits, gameplay state, turrets, and more. We also integrated the Claude API into the password generation mini-game so the strength of the user-generated password could be evaluated intelligently by a large language model. Lastly, we split our server/client responsibilities so that the server handles aiming physics and damage, while client-side batching of shot effects at 20 Hz, limiting network traffic to around 14 KB/s. How it applies to the company challenge Our project directly fits Track 3: Safety because it is an interactive Roblox experience that teaches players how to navigate the online world safely. Inbox Invaders focuses on building practical digital safety skills like identifying scams, creating strong passwords, protecting personal information, and understanding common online risks. The password generation mini-game also connects directly to the track's focus on password security. A portion of the mini-game makes players create their own passwords and receive a score based on defined security criteria, passing only when they reach a strong enough threshold. This makes password security an active learning challenge instead of a boring lesson. Challenges we ran into One major challenge was making the inbox and tower-defense systems feel like one game instead of two separate prototypes. By interweaving these two sections through the story and gameplay function, we were able to create one cohesive game. The player’s inbox performance affects their credits, and those credits power the tower defense, so we had to constantly retune the economy and progression to maintain balance. Another challenge was the mini-games. We wanted the inbox to pause in certain moments and send the player into a learning mini-game, but we did not want those moments to feel like interruptions. We had to strategically connect the mini-games to the story and then return the player cleanly to the inbox. Creating a tutorial posed many challenges. Since there is a lot to learn about the computer and tower defense ecosystem, we had to make a comprehensive tutorial. Orbit (our friendly alien friend) onboards the player with step-by-step instructions, guiding them through the interface with UI highlighting and directing them to certain parts of the map with path indicators. We made this to ensure anyone can follow along with the story and learn the game’s environment. Accomplishments that we're proud of We are proud that Inbox Invaders feels like a real dual-layer game. The inbox learning loop and the tower-defense loop run in parallel, sharing a single credit economy and supporting the same storyline. We are also proud of the inline red-flag feedback. When players correctly detect a scam, they must also explain their reasoning and learn about any signs of maliciousness that they missed. The four mini-games also helped us cover online safety from multiple angles instead of only focusing on phishing: password security, downloads, privacy, and more became their own interactive challenges. We are especially proud of Orbit, the alien cat guide that makes the game feel more playful and story-driven while also guiding the player through important safety lessons. Finally, we are proud of the technical optimization work. We were able to reduce network traffic from around 500 KB/s to 14 KB/s by batching shots at 20 Hz instead of sending one remote event per shot, which made the game much more efficient and scalable. What we learned We learned that educational games work best when feedback is immediate and specific. A generic “wrong” message does not teach much, but showing the exact red flag helps players understand what to look for next time. On the technical side, we learned that Roblox UI needs careful handling, especially when windows move and resize. We also learned how important it is to fine-tune the in-game economy and power of combat elements to ensure balance. Lastly, we learned that data persistence needs to be tested constantly. A feature that works in a fresh session can still break when a player leaves, rejoins, and expects the game to keep track of their progress. What's next for Inbox Invaders Next, we want to expand Inbox Invaders with more mini-games, more varied scams, and a more in-depth storyline arc. Future scam types could include deepfaked videos and voice messages, QR-code phishing, OAuth consent scams, and other social engineering scenarios. We also want to add multiplayer functionality, so players can work together to process inbox threats, defend the house, and coordinate tower placement. Another addition we want is support for other platforms, particularly mobile and console, to make the game and learning experience more accessible. The last major goal is adding more towers and upgrades. New towers will still be tied to cybersecurity concepts; examples could include spam filters, encryption, and more. <div