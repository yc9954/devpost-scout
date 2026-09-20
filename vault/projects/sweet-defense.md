---
slug: "sweet-defense"
url: "https://devpost.com/software/sweet-defense"
title: "Sweet Defense"
hackathon: "Meta Horizon Creator Competition: Short Loop Mobile Worlds"
organization: "Meta"
winner: true
words: 494
team_size: 1
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
---

# Sweet Defense

> Sweet! Storm or protect the chocolate chip castle!

[Devpost](https://devpost.com/software/sweet-defense) · hackathon [[Meta Horizon Creator Competition- Short Loop Mobile Worlds]]

## Facets

  <sub>weak: video_visual</sub>

**stack** horizon/camera, horizon/core, horizon/ui, typescript

## Body

SWEET DEFENSE_Web_4_3.jpg SWEET DEFENSE_QuestSquare.jpg SWEET DEFENSE_Web_16_9.jpg SWEET DEFENSE_Quest_16_9.jpg One of my favorite TV shows when I was a kid was American Gladiators. On the show there was a gauntlet style course called Assault where the Gladiator would try to stop contenders from completing the course by firing tennis balls at them. It was a dream of mine to compete on American Gladiators, so this was the closest experience that I have to the game show. The theme was inspired by the holiday season. Around this time of year, I tend to develop a sweet tooth starting with Halloween candy and transitioning into cookies, cakes, and pies for the Thanksgiving and Christmas holidays. It was only fitting to use a variety of desserts as the main theme. There was a lot of trial and error when it came to optimizing the game loop and in every iteration I was able to get the players in and out of the game faster. The world was created using Blender, Horizon VR editor, and the Horizon desktop editor. I first grey boxed using the VR editor and then exported it with the desktop editor where I imported it into Blender to correct my UVs and optimize the shapes. Once my UVs were set and shapes were optimized, I textured them in Adobe Substance. The scripting was done using VS code with some help from the Horizon AI tool in in the desktop editor. The most difficulty I encountered was trying to test on mobile. The Horizon app links weren’t allowing me access the world, so I had to rely on the desktop editor mobile preview, which didn’t give me the same feel as actually being on mobile. Another challenge was sending my script events in the correct order to transfer weapon ownership to the runners. Because of the speed of the game, my original method of setting ownership when the weapon was grabbed and dropping ownership when the weapon was fired wasn’t registering in the event that the runner would hit the target. I was able to overcome this by setting the runner’s weapon ownership to all runner weapons as soon as the game started. I’m most proud of the fast-paced game loop itself in which players can seamlessly play multiple games without a hassle. Since the roles are randomly assigned, there is an anticipation from the players before the game starts to see who will be the defenders and who will be the runner. I’m also proud of the replay ability. When testing the world, it made me excited to see players wouldn’t just settle for a single game. This project really allowed me to polish my scripting and troubleshooting skills. As the project progressed, I found myself getting faster at figuring out bugs and where there was a break in my logic. With Sweet Defense, I really want to have interchangeable scenes where players could select from multiple themes instead of just the dessert theme. <div