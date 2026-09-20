---
slug: "blobble-qu2fak"
url: "https://devpost.com/software/blobble-qu2fak"
title: "Blobble"
hackathon: "Meta Quest Presence Platform Hackathon 2024"
organization: "Meta"
winner: true
words: 635
team_size: 1
has_repo: false
has_live: false
has_video: true
tags:
  - "project"
  - "domain/developer_tools"
---

# Blobble

> Blobble: Billiards meets Puzzle Bubble in your living room! With dynamic physics and environment interaction, create unique trick shots in your own space.

[Devpost](https://devpost.com/software/blobble-qu2fak) · hackathon [[Meta Quest Presence Platform Hackathon 2024]]

## Facets

**domain** [[developer_tools]]

**stack** c#, meta, oculus, unity

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for blobble

## Body

How to Play Inspiration Blobble is a game inspired by arcade classics like Puzzle Bobble and real-life ball-based games like billiards and pool. With this concept, our aim was to create a mixed reality experience that can be played and mastered, but also to provide an introductory experience to MR for first-time users. What it does In essence, Blobble spawns blobs (balls) in your scanned mixed reality environment. The challenge is to then use your environment to bounce these balls off and combine them to create blobbles. How we built it Blobble was created in Unity, using the Oculus Interaction SDK and building blocks. Challenges we ran into The first and major challenge was underestimating game-play difficulty. Originally, the idea was to make spatial pool, with the same rules as traditional pool. It was hard to aim and didn’t feel intuitive to use. We first started with a cue that hit the balls. Not only was this hard to aim, but it also made it difficult to hit objects out of reach. Objects in this 3D space quickly became unreachable without a ladder. This led to the creation of a sling shot, which solved the issue of hitting balls out of reach but again posed challenges, as you can’t hit the ball from all angles, adding a handicap to a 3D space. The solution we created was to pinch anywhere and use that local rotation and distance to apply the effect on a selected ball. This allows the player to hit the ball from any angle, no matter where the ball is positioned. It also allows for great ambiguity and, in essence, accessibility, allowing players to play the game how they want. Developing on a Mac was somewhat frustrating as you had to build it to test it on the device each time. Accomplishments that we're proud of Our interaction system The trajectory system is mostly accurate some smaller surfaces on furniture can give a false prediction but 95% of the time it works. Likewise, intuitive pinch and pull system allows ease of use and ambiguity. Our soft bodies and Blobble system. The softbodies bounce, jiggle, and feel nice. It is fun and satisfying to see them connect into a blobble. The general theme and style I feel like the style of this mixed reality game is somewhat unique in most part due to the posterization effect and colour effect. What we learned Test test test, always test in VR on the device. What is seen in the editor is not always the same as a deployed build. Additionally iterating on interactions is important an idea may not work or may run into a problem, with mixed reality it's important to test in a multitude of different environments. Fortunatley, for me I had a room with a high ceiling so it quickly became apparent that the interaction system needed to change. What's next for Blobble Accessibility and useability features Make a fully seated/ "Pillow" mode. Both controller and hands. A setting where it’s not pinch and release, but allows you to place your shot and then trigger it. This would be a great feature for those will low mobility or for those in a dark environment where there is poor hand tracking. Features to add depth Local turn-based multiplayer. In this case taking the headset off and passing it to the other player keeping the objects anchored in spatial space. Actual game tracking mechanics like score, time, combo for hitting off the wall allowing for skill expression. Spatially smart spawning with room understanding. Vfx that add tangibility to game objects interacting with objects from the real world, perhaps with further meta updates with Llama we can do some amazing stuff with furniture and room understanding. Full unedited gameplay can be seen here - https://youtu.be/0FXdn0t55PI <div