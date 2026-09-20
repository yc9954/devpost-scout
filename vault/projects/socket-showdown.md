---
slug: "socket-showdown"
url: "https://devpost.com/software/socket-showdown"
title: "Socket Tower"
hackathon: "Global Gamers Challenge"
organization: "Google"
winner: true
words: 462
team_size: 1
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "mechanism/simulation_digital_twin"
  - "user/educator_student"
  - "user/general_public"
---

# Socket Tower

> Build a tower made out of household items! Can you reach the top? Find out how much electricity you consume everyday without even knowing it with Socket Tower!

[Devpost](https://devpost.com/software/socket-showdown) · hackathon [[Global Gamers Challenge]]

## Facets

**mechanism** [[realtime_stream]] [[simulation_digital_twin]]
**user** [[educator_student]] [[general_public]]

**stack** blender, firebase, flame, flutter, google-wallet, inkscape, rive

## How they structured the write-up

- 🚀 features 🚀
- 🌿 community impact 🌿
- 🛠️ google wallet 🛠️
- 💡 inspiration 💡
- 🤔 challenges 🤔

## Body

Socket Tower is a game where you stack up home appliances on top of each other while trying not to tip your creation over. Find out just how much electricity these everyday items consume and better visualize them with the collectible system powered by Google Wallet! 🚀 Features 🚀 3D design : Stack up different electrical appliances and find out average consumption for each one; Real-time leaderboard : powered by Firestore DB; Collectible system : powered by Google Wallet - collect unique cards and unlock secret videos through QR codes; Cross platform support : available on Android, Web, Desktop and MacOS; Original assets : all characters and music were made during the hackathon. All 3D assets were initially built in Blender, exported as SVG files in Inkscape and then animated using Rive. 🌿 Community Impact 🌿 Socket Tower aims to encourage reduction in home energy use by making the players aware of just how much electricity common household objects consume. The game was shared with the flutter communities via Reddit here and here . The posts ended up getting decent traction with over 1k impressions. I've also took the opportunity to share my story of building a flutter game using a 3D perspective in my very first article: "How to make a 2.5D game using flutter" , as well as providing a simplified open source project as a tutorial for beginners who want to build similar 3D games: here . 🛠️ Google Wallet 🛠️ Unlock collectible cards for each playable house appliance; Better visualize electrical consumption for each character in the game; Unlock secret Youtube videos for each card you collect (powered by Google Wallet QRs!). Due to time limitations, my approval for Google Wallet production access is still pending at this time and therefore is only accessible in demo mode. You can request access by sending me an email at: hup.hubspace@gmail.com 💡 Inspiration 💡 Checking out the Global Citizen resources made me realize I don't know how much electricity everyday items use. So I took the opportunity to refine an idea to shed some light on high electrical consumers! #TurnOffTheToaster. As for the game concept itself, Tower Bloxx was my main inspiration, a classic retro mobile game phone from way back in the day which you might already be familiar with. 🤔 Challenges 🤔 Creating a "3D game" powered by a 2D physics engine raised some interesting problems such as: Rendering the tower components at runtime in different order each frame to give the illusion of a 3D space; Supporting dynamic resolutions was a challenge at first due to some limitations in the Flame engine; Caching the Rive animations for each tower block to improve performance. In the end, nothing that couldn't be solved with a little bit of math! <div