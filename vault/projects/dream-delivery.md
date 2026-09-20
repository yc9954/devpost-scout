---
slug: "dream-delivery"
url: "https://devpost.com/software/dream-delivery"
title: "Dream Delivery"
hackathon: "Meta Horizon Creator Competition: Mobile Innovation"
organization: "Meta"
winner: true
words: 807
team_size: 2
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "mechanism/simulation_digital_twin"
  - "domain/transportation"
  - "substrate/geospatial"
  - "substrate/video_visual"
---

# Dream Delivery

> Become a dream sprite and soothe the world with magical dreams. Restore lost wonder, rebalance the night, and grow your powers with every dream you deliver.

[Devpost](https://devpost.com/software/dream-delivery) · hackathon [[Meta Horizon Creator Competition- Mobile Innovation]]

## Facets

**mechanism** [[realtime_stream]] [[simulation_digital_twin]]
  <sub>weak: vision_ocr</sub>
**domain** [[transportation]]
**substrate** [[geospatial]] [[video_visual]]

**stack** blender, desktopeditor, genai, maya, metaai, noesis, procreate, substancepainter, typescript, vscode

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for dream delivery

## Body

Game Logo Lunessa, game character (lead Dream Sprite) Gameplay shot, approaching window Gameplay shot, Flying mechanic Gameplay shot, unlocking stories Gameplay shot Gameplay shot, flying towards dream dust Gameplay shot, locating dream delivery Gameplay shot, delivering dreams animation pt1 Gameplay shot, delivering dreams animation pt2 Gameplay shot, dream delivery UI shot, shop display Areal shot of town with game logo Inspiration The inspiration was for the love of story telling roleplay games in a fantasy setting. Since the early horizon days I've always been drawn to making fantasy landscapes with mystical characters and creatures, leaning towards my love for RPGs like World of Warcraft or even Kingdom Hearts, and pop culture movies like Hook and Legend. We were inspired by the innovation theme, specifically the idea of freely flying without the need for any vehicles, powered only by the magic of flight. We feel this game is unique to Horizon because it showcases the player’s avatar and naturally promotes socialization throughout the experience. What it does When night falls, the villagers drift into sleep and they rely on you to help guide their dreams. Visit each window to discover the dream they’re hoping to experience, then soar into the starlit sky to gather shimmering dream dust drifting above the town. Combine the dust to craft radiant dream orbs, and deliver them to the sleepers to unveil the heartfelt stories unfolding in their minds. As you complete dream deliveries, you’ll earn enchanted XP that boosts your flying and jumping abilities, and collect stars that can be spent on customizing your avatar with clothing, and new wings. How we built it For this game, I wanted to experiment further with model optimization. For each street, I created a set of unique base shapes that allowed me to kit bash my own models into a full town. By keeping the vertex count low, I was able to build multiple unique looking buildings while maintaining great performance. I then baked everything down into just two texture maps per street, perfect for game efficiency. With this workflow, I’m inspired to create my own model sets for future game art designs. Overall, the entire world setup comes in well under a 300K vertex count (and that includes the trees!). For the color palette, I leaned into soft blues with a semi stylized approach, creating a dreamy nighttime atmosphere where the glow of street lamps and windows can take center stage. And of course, pops of color from interactive elements, like the glowing magic dream orbs, bring the world to life. PigeonNo12 worked on the scripting. One of the major challenges was learning Noesis and discovering in real time which features were available or unavailable in Horizon Worlds. Using a brand new feature comes with its own difficulties: there is no prior community knowledge, and there wasn’t any Horizon Worlds specific documentation. However, it didn’t take long to notice the huge improvement Noesis represents compared to the previous Custom UI system. Two of the biggest benefits are: Being able to see how elements are placed on the canvas in real time, without having to wait for world simulation to start, was a tremendous time saver. The performance and responsiveness are incomparable, allowing us to update the UI state and variables in real time without relying on networked data. At the time of writing, Noesis was still missing some features, but we already look forward to using it at its full potential in the future. Using AI greatly sped up our creation process. We used it for the world skydome, image generation, sounds, textures, and to prototype the clothing items. We later downloaded the assets and personalized them for the world. We decided to stay focused on a mobile only experience for now, but we look forward to improving the gameplay and making it compatible with other platforms in the future. Challenges we ran into Learning the newly released Noesis was a challenge due to the limited Horizon focused documentation, and none of us had used Noesis before. On the art side, the challenge was keeping the vertex count low while still maintaining great detail. Accomplishments that we're proud of Vertex optimization and town model variety are what I’m most proud of, and I look forward to continuing to push my skills further with my art! We were also able to create a fully functional custom UI using Noesis Studio, which integrates beautifully with the world. What we learned We learned a lot about Noesis Studio, including how to swap images dynamically, create interactive overlay displays, and communicate with the UI while using shared execution mode. What's next for Dream Delivery Further optimizing the environment to create more gameplay space, and enhancing social interactions, such as rewarding players for spending time together and adding NPC interactions. Possibly adding a VR experience, for full immersion. <div