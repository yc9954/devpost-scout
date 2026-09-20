---
slug: "room-wars-home-defense"
url: "https://devpost.com/software/room-wars-home-defense"
title: "'Room Wars' - Castle Defense"
hackathon: "Meta Quest Presence Platform Hackathon 2024"
organization: "Meta"
winner: true
words: 1091
team_size: 1
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "domain/developer_tools"
  - "user/developer"
  - "substrate/video_visual"
---

# 'Room Wars' - Castle Defense

> An MR game where you defend a castle against attacks that burst through your walls & ceiling. It becomes totally carnage as your room is destroyed and is completely wrecked in the battle!

[Devpost](https://devpost.com/software/room-wars-home-defense) · hackathon [[Meta Quest Presence Platform Hackathon 2024]]

## Facets

**mechanism** [[realtime_stream]]
**domain** [[developer_tools]]
**user** [[developer]]
**substrate** [[video_visual]]

**stack** c#, meta-all-in-one, normcore, unity

## How they structured the write-up

- inspiration
- what it does
- how i built it
- challenges i ran into
- accomplishments that i'm proud of
- what i learned
- what's next for room wars: castle defense

## Body

Made for the Meta Quest Presence Platform Hackathon 2024. Inspiration I was inspired to make a game that I've not yet seen in MR and also push the limits of MR to blur the line between what's real & virtual and also have fun destroying your own room virtually without having to clean up afterwards! This project aims to set a new bar in Mixed Reality realism. What it does Room Wars: Castle Defense is an MR game where you defend a castle against attacks from various enemies that burst through the walls and ceiling and destroy your room as they go. As the battle continues, it becomes total carnage as your room is continually destroyed and looks completed wrecked after the battle. You must defend your castle at all costs using you tactile weapons mounted on the castle. The game can be played either with the controllers or your hands As you progress, you collect crystals which are used to upgrade your castle where additional weapons are added to your castle. This is a feature that has a huge amount of scope , the current game made in the limited time upgrades the castle by adding more weapons so you can deal with the more frantic enemy waves. In multiplayer mode , you can fight against another player in a real-time battle. A portal appears where you can both shoot through and have one-on-one battle together. Another focus on this project was to make the virtual objects look as real as possible against the passthrough view. A lot of work has gone into the custom shaders and tweakable parameters that allows the player to 'match' their world view. Down to various lighting parameters, desaturation and even subtle noise has been added to the virtual objects to match the passthrough camera output . Also, there is lighting placement by the player, which allows the game to look even more realistic as the virtual objects respond to this. The MR room environment can have unlimited damage applied to it... where walls, ceilings and floors can be cracked, broken and damaged to the core beneath and enemies crash through . This progressive damage system is applied to the breakable parts of the room and the whole room can be destroyed without limits. How I built it I am a solo developer on this project and I used Unity, Meta's All-in-One SDK, Blender and Substance Painter. I plan on making a 'making of...' video on my YouTube channel containing all the details, however here's a brief on how it was made. First I created the shaders and rendering techniques to make objects fit the real world more when looking through the passthrough mode. I then created a progressive damage system using custom shaders which make a custom model from the global mesh and process the triangles into game friendly formats so that elements can be destroyed. I then added the gameplay elements, such as the castle, the enemy logic and the overall gameflow Portals were then added using a stencil approach, and a system where objects can travel through portals and resolve the gameplay collisions. Normcore was used to add multiplayer and a multiplayer mode was added where a battle could take place through a portal. I then added a character and did my own voice over (yeah, sorry about that - he might become annoying after a while, lol). ...and finally, lots of game testing, polish, modelling, texturing with sound effects and music to wrap it all up! Challenges I ran into One of the main challenges was dealing with potentially infinite an amount of different environments in MR. Having code robust enough to cater for different room configurations and still keep the gameplay exciting and playable. Almost the opposite from traditional methods were you make levels and environments, you have to flip it on it's head and add procedural gameplay into a unknown envionment - that's quite a challenge! This was especially tricky within a month's deadline, and I'm sure this could be extended on given the current implementation. Another challenge was to have quite an ambitious idea implemented within the time frame, where almost everything was made bespoke for the game, from all the artwork, 3d models and custom shaders. The only 3rd party asset was the music and SFX - as a solo developer on this project, time was a massive factor in making the game. However, it was great fun to make and MR is such an exciting feature to work on. Accomplishments that I'm proud of I feel I made a great progressive damage system for the room in MR and also pushed the boundaries for blurring the line between the virtual and real objects in passthrough using the rendering technique I've not seen before in any other MR game. Also, I'm happy that multiplayer made it in to the implementation - still work to be done on that side of things, but I'm glad it proved the concept. Also, the best thing was how real the destruction of the room ended up looking, even in a month long small project. I still feel there's lots more that can be done with that, but there's times in the game where it's really convincing that you've actually destroyed the place! What I learned I mainly learned how to use Meta's SDK and Normcore's multiplayer system too. Another big thing was how to cater for an infinitely different environments and how to make procedural game designs fit this concept. I've been in the game's industry for over 25 years, and this was quite a challenge - but really enjoyed it! I have a few friends play test it (especially those new to VR/MR) and it's great to see their reactions - it was hilarious. Especially when the battles really kicked off! What's next for Room Wars: Castle Defense I would love to continue with the project and it would be amazing if Meta picked this up for funding too. I can see the concept has a lot of scope and even though the current implementation has taken it part way there, there is so much more than can be added too - different enemy types, different castle types and upgrades, more characters and story and especially more can be done to add more realism to the progressive destruction system and custom shaders for realism in the game. It's an exciting time for MR and I really wanted to make one of the best and most realistic experiences out there. <div