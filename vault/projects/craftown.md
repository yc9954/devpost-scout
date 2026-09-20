---
slug: "craftown"
url: "https://devpost.com/software/craftown"
title: "Craftown"
hackathon: "Global Gamers Challenge"
organization: "Google"
winner: true
words: 933
team_size: 1
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "domain/agriculture_food"
  - "domain/developer_tools"
  - "user/developer"
  - "user/frontline_worker"
---

# Craftown

> Craftown is a retro survival & automation game. Begin with basics, scavenge for resources, and thrive sustainably in a challenging world.

[Devpost](https://devpost.com/software/craftown) · hackathon [[Global Gamers Challenge]]

## Facets

**domain** [[agriculture_food]] [[developer_tools]]
  <sub>weak: supply_logistics</sub>
**user** [[developer]] [[frontline_worker]]

**stack** dart, flame, flutter, riverpod

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for craftown
- notes

## Body

Craftown Cover Craft resources Automate construction of resources Change your tools for different actions Store items when inventory gets full Research and unlock abilities Automate smelting Menu system with saving/loading games Inspiration The inspiration behind Craftown stemmed from a desire to offer a gaming experience centered around crafting and automation with a touch of casual enjoyment. Drawing from the complexity of titles like Factorio and Satisfactory, yet aiming for a more relaxed atmosphere akin to Stardew Valley, I envisioned a game where players could immerse themselves in resource management and sustainability without feeling overwhelmed, fostering a balance between challenge and playful exploration. Craftown embodies this vision, inviting players to embark on a journey of creativity and ingenuity in a uniquely charming world. What it does Craftown is a captivating retro survival and automation game where players embark on a quest to thrive in a challenging environment. Begin with a modest set of tools and venture into the vast landscape, scavenging for valuable resources while honing your sustainability skills. With each success, you're rewarded, empowering you to expand your capabilities and conquer the wilderness. Dive into Craftown and uncover the secrets of survival in a richly immersive experience that blends nostalgia with innovation. How we built it Craftown was crafted using Flutter alongside the dynamic Flame game engine, with a significant portion of the game logic housed within Riverpod providers. Leveraging Flutter's versatility, the game seamlessly extends across desktop platforms (MacOS, Windows, Linux) and the web, catering to both casual and more seasoned players with support for keyboard shortcuts. This multi-platform approach ensures accessibility, allowing mobile gamers to delve into the experience via touch-based interaction. In addition to Flame and Riverpod, the game utilizes flame_tiled for world building, flame_audio for immersive soundscapes, flame_riverpod for bridging the state between game components and the app, sembast for game state saving and loading, and freezed for data serialization. I also live streamed about 60% of the development of this game on my Youtube channel and had a lot of fun chatting with other flutter devs, and even occasionally getting suggestions from my viewers about the game and/or software design patterns. Please note that most of the graphics were purchased from a creator on itch.io as I am not much of a pixel artist. Challenges we ran into One of the most significant challenges we faced was restraining the project's scope within the confines of a tight deadline. Balancing the desire to enhance functionality, incorporate a compelling narrative, and introduce new game mechanics post-submission with the need to deliver a polished, playable game was a delicate task. While I'm well-versed in Flutter development, delving into the realm of Flame presented a learning curve, particularly as someone primarily focused on web and app development. Additionally, implementing save/load functionality proved to be intricate yet essential, not only for gameplay but also for facilitating efficient development processes. Despite these challenges, navigating through them has been instrumental in refining Craftown into an engaging gaming experience. Accomplishments that we're proud of I take pride in creating a complex and enjoyable experience with Craftown, achieving a blend of functionality and aesthetic appeal that surpasses my initial expectations. Overcoming the challenge of implementing saving/loading mechanics was a significant triumph, ensuring the game's integrity and enhancing the player experience. Moreover, integrating Riverpod "generators" marked a milestone in my skill development, empowering me to leverage this powerful tool with confidence and efficiency. Craftown stands as a testament to perseverance and growth, embodying the culmination of hard work and dedication in game development. What we learned Craftown has been a journey of discovery, where I've gained invaluable insights into game development and honed my skills with Flame. Embracing the iterative process, I found immense joy in bringing ideas to life and experimenting with game mechanics organically. This approach not only sparked creativity but also deepened my understanding of modern Riverpod techniques, breaking free from old habits and embracing best practices in local storage and data serialization. Craftown stands as a testament to the rewarding nature of learning through hands-on exploration, reflecting both my growth as a developer and the boundless possibilities of game design. What's next for Craftown The current iteration of Craftown serves as a glimpse into its potential, with plans for expansion already in motion. One exciting avenue is the introduction of "conveyor belts" or a similar system akin to Factorio's robots, facilitating automated item transportation via hired Craftown community members (NPCs). This addition promises to deepen gameplay mechanics and enhance player engagement. Moreover, the journey in Craftown is far from over. Future updates will unlock new realms for exploration, offering players opportunities to traverse vast landscapes, engage in activities like fishing and visiting farmers markets, and unearth hidden treasures scattered throughout the world. In line with the game's target audience, our focus will initially be on releasing Craftown as a mobile game, tapping into the widespread accessibility of mobile platforms. However, multiplayer functionality is on the horizon, with plans to leverage Serverpod for seamless online interactions. While this feature may come post-release, it holds immense promise for fostering a vibrant community within Craftown's evolving world. Stay tuned as we continue to shape Craftown into an immersive and dynamic gaming experience. Notes I plan to release the game for mobile (Android+iOS) and Desktop (Windows+MacOS+Linux). While there's a web build for convenience, Flutter web isn't fully optimized yet. Future enhancements like WebAssembly support may improve performance. For a proper evaluation, please run the game on a device. The MacOS app is included, but since it's open source, you can build and run it on any device. <div