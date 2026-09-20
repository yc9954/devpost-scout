---
slug: "drawbattle"
url: "https://devpost.com/software/drawbattle"
title: "drawBattle"
hackathon: "Meta Horizon Creator Competition: Short Loop Mobile Worlds"
organization: "Meta"
winner: true
words: 785
team_size: 2
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
---

# drawBattle

> drawBattle 👽 is a fun-filled VR and Mobile cross-play experience where crayons are your weapons and creativity is your edge! Sketch, doodle, and compete for artistic glory! Packed with cosmic charm!

[Devpost](https://devpost.com/software/drawbattle) · hackathon [[Meta Horizon Creator Competition- Short Loop Mobile Worlds]]

## Facets


**stack** blender, canva, horizon, meshy, midjourney, photoshop, substance-painter, typescript

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for drawbattle

## Body

The game play area World from overhead The game board Drawing on the board in mobile with the menu open Inspiration drawBattle was born from a love of creative competition and the vision of seamlessly connecting players across VR and mobile platforms. The concept of timed drawing challenges, combined with dynamic tools, was designed to inspire everyone to tap into their inner artist while fostering creativity, connection, and fun. The foundation of the game draws inspiration from hyperjoule's innovative interactive crayons, which became a favorite tool for creators during the beta period of Horizon Worlds. These crayons, originally scripted using code blocks, allowed players to draw and collaborate in unique ways. For drawBattle , the mechanic was reimagined and enhanced using modern TypeScript methods, adding new levels of functionality and compatibility for mobile interaction. This evolution brings a fresh approach to the original concept, creating a game experience that bridges platforms and celebrates the joy of artistic expression. What it does drawBattle is a crossplay VR and mobile game where players compete using their creativity to draw a random prompt. Players use a crayon that allows for color switching, with a time limit of two minutes. The game supports drop-in/drop-out mechanics, letting players join or leave anytime. If no one is playing, the drawing boards can still be used for general creative use. How we built it All of the scripting was done in TypeScript by hyperjoule . Game conceptualization is the original creation of PurpleWren , with 3D modeling and graphic design meticulously crafted by her using Blender, Photoshop, and Canva. Some 3D modeling, audio and graphics were produced using innovative AI technology. The VR and mobile UI required different interaction gizmos, which presented unique challenges. The crayons, which leave trail effects, always "draw" by design, but the illusion of lifting the crayon was achieved through clever scripting. The active color moves close to the surface while inactive colors are recessed, simulating the effect of a crayon break. Challenges we ran into Making the game crossplay posed considerable challenges, particularly with the UI. VR and mobile platforms required distinct interface designs, necessitating meticulous planning and iterative development to ensure a seamless experience across devices. Managing the crayons also introduced technical hurdles. Keeping them confined to a designated area and implementing a clearing mechanism required careful engineering. Simulating the traditional drawing experience by scripting the illusion of lifting the crayon added further complexity, as did designing a playboard layout that minimized crayon bleeding while maintaining a clean and functional aesthetic. Currently, the interactive menu is non-functional on desktop due to a platform bug. To accommodate desktop users, we included alternative controls for cycling colors and resetting the board, ensuring the gameplay remains accessible. Accomplishments that we're proud of We’re incredibly proud of the final design, which was the result of multiple iterations and refinements. The user interaction layout now works beautifully for both VR and mobile platforms, and the mechanics allow the game to run continuously, supporting both gameplay and general creative use. This project also marks a return to active development for both team members after a hiatus, during which we had to relearn and adapt to new tools and methods. The support from the MHCP mentor program was invaluable in overcoming these learning curves. What we learned We learned a great deal about crossplay development, particularly how to handle different interaction paradigms for VR and mobile. The project also deepened our understanding of scripting, UI design, and engineering creative solutions for trail effects and crayon mechanics. What's next for drawBattle We have exciting plans for drawBattle's future: Additional Game Modes : Introduce new gameplay experiences to keep players engaged. Spectator Sabotage Options : Add fun mechanics like "erase bombs" that allow spectators to remove colors from a player's drawing. Custom IWP Crayon Options : Create personalized crayon skins with special effects and unique colors. Expanded Themes and Aesthetics : Carry the game's artistic theme into additional worlds, broadening its appeal and scope. Themed Contests and Events : We intend to host themed contests and events and offer in-world prizes and unlockable items along with some potential real-world prizes (handmade custom crocheted hats by hyperjoule!) on our discord server. More Quests and Easter Eggs : Time constraints on the contest limited the number of world enhancement ideas we were able to implement. Future enhancements include expanding upon quests and adding fun little easter eggs to the world for the player to discover. Refine Game Time : Right now, the drawing timer is set to 2 minutes. This might need to be adjusted based on user feedback. These updates aim to make drawBattle even more immersive and enjoyable for both VR and mobile players. <div