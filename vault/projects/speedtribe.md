---
slug: "speedtribe"
url: "https://devpost.com/software/speedtribe"
title: "Speedtribe"
hackathon: "Junction 2016"
winner: true
words: 594
team_size: 4
has_repo: true
has_live: false
has_video: false
tags:
  - "project"
  - "domain/health_clinical"
  - "substrate/geospatial"
---

# Speedtribe

> Coolest location-based game ever, gamification of intelligent buildings, retail conversions, mobility and whatnot

[Devpost](https://devpost.com/software/speedtribe) · hackathon [[Junction 2016]]

## Facets

**domain** [[health_clinical]]
  <sub>weak: developer_tools</sub>
  <sub>weak: patient_family</sub>
**substrate** [[geospatial]]

**stack** 3ds-max, adobe-illustrator, azure, documentdb, github, java, node.js, nosql, photoshop, photshop, proximi.io, unity

## Body

Speedtribe is a fast-paced and location-based player vs. player game. Uniquely, only the opponent of the player is shown on the map — the player can figure out he's own location by himself. State-of-the-art microlocation technology is used to make this possible. The story is about a tribe of skilled demon-hunters hunting poor persons occupied by the resurrecting demons. The match-making is done by the server. The player's goal is to get near the opponent undetected, and fire the weapon (no aiming required) first when near enough. The trick is to detect the opponent from the crowd as early as possible (the one looking around & at his mobile is a good candidate). Then, just approach the target casually (and definitely not staring at the mobile), and BOOM. The firing of the weapon causes the weapon, er, I mean the mobile phone to emit a loud BANG, and start a reload timer. Were you too far away? Too bad: you are definitely detected now! Time for some running... If you were near enough (and first to fire), a satisfying "AAargh!!" is emitted from the victim's phone, and you emerge as the winner. Alas, the demon is going to resurrect in some other body soon. Get ready for a new fight! The game mechanic allows for server-side tracking of players, and, through dynamic match-making, guiding people around. The mobility- and data driven gamification possibilities are innumerable. Want to know what route people choose between points A and B? Check, just give the player at A an opponent near B. (The opponent need not exist to begin with, but do not tell this to the player). Want to get a payer out of your player? Check, just give him a target near the goods he desires. Want to entertain, follow and guide small patients around a hospital. Check, just reskin the app to show a little less killing. We made the game with Unity engine on the client, and Cloud Function -microservice-based server in the Azure cloud. The microlocation tech was provided by proximi.io. The biggest challenge (for which we are very proud of) was the development of a Unity plugin for proximi.io service. We are also extremely proud of the novel game mechanic. It allows for inaccurate positioning (not to make finding the opponent too easy) and bad connections (ditto, and in the case of complete failure of opponent connection, the demon just resurrects into some other player nearby). The story, the tech challenges & possibilities, the theme of the jam and the game mechanic support each other uniquely! The same goes for (commercial) gamification possibilities: the story supports dynamic changing of opponents to satisfy the needs of the service provider. Of course, building a complete client-server architecture for a location-based PvP game in such a short timeframe is quite a feat in itself. Not to mention writing these pitches last-minute, staying awake overnight or whatnot. While there were many technologies we were familiar with to begin with (e.g. Unity, Azure cloud services), we had to learn some Android coding, proximi.io SDK and how to code & build challenging Unity plugins with native components. Above all, we had great fun and feeling of accomplishment. We formed a great team; although most of the team works for the same company (Next Games), our roles have not allowed for us to work together this intensely before. Next, we go on working in our regular jobs (4/5 at Next). We acquired new skills and developed some interesting tech, that might find novel usages in our future products. <div