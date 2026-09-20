---
slug: "kpop-academy"
url: "https://devpost.com/software/kpop-academy"
title: "Kpop Fever – Dance Challenge"
hackathon: "Meta Horizon Creator Competition: Mobile Genre Showdown - Reloaded"
organization: "Meta"
winner: true
words: 1091
team_size: 2
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "domain/developer_tools"
  - "domain/education"
  - "user/educator_student"
  - "substrate/geospatial"
  - "substrate/structured_db"
---

# Kpop Fever – Dance Challenge

> DROP IN! Hit the stage in this beautiful Dance World, nail the choreo, and form the ultimate band. Level up and become an IDOL. LET'S GOOO!

[Devpost](https://devpost.com/software/kpop-academy) · hackathon [[Meta Horizon Creator Competition- Mobile Genre Showdown - Reloaded]]

## Facets

**domain** [[developer_tools]] [[education]]
**user** [[educator_student]]
**substrate** [[geospatial]] [[structured_db]]
  <sub>weak: video_visual</sub>

**stack** blender, custom, gemini, horizon, metaai, needle, photopea, suno, typescript, vscode, worlds

## How they structured the write-up

- inspiration
- the game
- how we built it
- challenges we ran into
- accomplishments we’re proud of
- future plans

## Body

Team Bonus! Become the Best - Hit the Rhythm! Three powerfull KOP Songs in easy, medium and hard! AI-based KPOP Mentors powered by Meta AI Sign Autographs Aura Farming XOXO AI generated Content Blender 3D Modeling InGame Greenscreen Studio for capturing the silhouettes for custom UI Buttons InGame Greenscreen Studio for capturing the silhouettes for custom UI Buttons First draft key image for Feedback Fest Custom Songs generated with Suno AI - lyrics with Gemini & ChatGPT Inspiration In our family, we love dancing and music! And we set out for a super ambitious challenge: creating a multiplayer dancing game in Horizon Worlds, where you can dress up, dance, relax and level up to become a star. The result is Kpop Fever – Dance Challenge, a world unlike any other, full of fun experiences and little details. It was super fun to make and test. Kpop has become a global phenomenon that we experience first-hand through our daughter, so this project is dedicated to creating a glamorous, challenging, and vibrant world where that energy can be channeled. We hope you’ll like it as much as we do! The Game In Kpop Fever, you train to become an Idol. The core part is dancing and matching poses to the beat! But there’s so much more: signing autographs, learning about the history of Kpop from AI NPCs, practicing dance moves, a shop and dancing gear, a recording studio with greenscreen, and even aura farming in Kpop heaven. How we built it The World We designed a circular map with floating islands for various activities. The 3D assets in the world use a mix of Generative AI and hand-modelling. We also extracted some of the generated models and improved their textures and materials, for example to make them metallic or emissive. There’s also a few Public Assets in the mix! Dancing on the Stage The stage leverages numerous gizmos for lighting, NPCs, player slots, song UIs, audio, … and more! We experimented a lot with different options, and were pleasantly surprised that Horizon Worlds actually allowed us to create a fun dance challenge with low enough latency. For this, we used Local CustomUI with animated bindings, pooling, and buttons with beautiful feedback. Song Selection We designed the song selection as a beautiful, diegetic in-world experience – walk up to a song, listen to a preview, and then choose which one you want to play. There’s even dynamic spotlights for the selected song! Avatar animations We created new animations, tuned for beat-based gaming. As a base, we used single poses from a mocap database that seemed to be a good starting point. The animation speeds are synchronized to the beat of each song, which felt much better than just playing them back. XP System We wanted the path to being an idol to be beautiful, snappy, and animated. We ended up using CustomUI with player-based bindings, and lots and lots of animated bindings for the reactiveness and feeling. As part of that, we designed a layered texture system for different UI states, so that each level has its own beautiful look. AI-powered NPC teachers A big part of becoming an Idol is the right training! And so we added AI-powered teachers to our world, which tell you everything about Kpop, how to move, how to sing, and even how to eat! They are powered by Meta AI right in the world. You also gain XP by talking to them! Autograph Signing This was a fun one to get right! We combined focus-based interactions and touch trails in a fun and novel way, and let you actually hand-sign autographs to gain extra XP. The Songs The song lyrics are part AI, part human – we wanted them to be both great to listen to and impactful in their lyrics. “Doom Doom Doom”, for example, is about doom scrolling and the desire to break free of digital chains. The music is generated with Suno, and we leveraged AI models to separate voices from instruments so we could also use them for our world ambience when no performance is ongoing. The skybox and environment The background is made with Skybox Generation and a few human touchups. And after experimenting with the existing skyboxes we weren’t quite satisfied with the reflection/PBR quality, so we ended up making our own tools for the particular radiance/irradiance format Horizon uses. Here’s how the textures look: In-World Purchases We created several cool Kpop-based clothing designs just for our world, that you can buy via the IAP system. We also made in-world items – hats, wings, headphones and more – that you can either get via “Idol Tokens” or grab from the Shop Area. It turned out to be super fun to dress up and Challenges we ran into Multiplayer games are always hard to develop, but the Horizon APIs made it possible in the end, thanks to the helpful docs and samples. The desktop editor is … challenging. We bit our way through a good number of crashes, script resets, and evenings filled with CustomUI debugging. Talking to others in the Horizon Worlds Discord was a bit of a relief to see we’re not the only ones! We’re happy that we persisted though! Accomplishments we’re proud of From the start we were absolutely not sure if we could make the game we dreamed of. So many things to get right! Timing, music, world design, animations, look & feel, and learning a new editor and API at the same time. We’re incredibly happy that this worked out, and especially proud that our daughter loves the game, doesn’t stop listening to the songs, and tells her friends about it. Design-wise we’re super happy all the complex animated UIs worked out as we wanted, and that we were able to get so much done in such a short time thanks to various generative AI systems, both the impressive integrated ones by Meta and external ones like Nano Banana and Copilot. Also, we dug deep into Horizon's material system, and ultimately were able to create beautiful materials, metals, emissive areas and more. Future Plans We’d love to improve the item and IAP system – we got the basics in, but the in-world XP and Idol Token system are definitely just a start. And talking to the AI-based NPCs is already fun, much more so than we initially thought, but there is definitely room for improvement when it comes to reacting in specific ways, showing the player new dance moves, or talking about the latest Kpop gossip. <div