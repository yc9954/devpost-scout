---
slug: "snap-and-swing"
url: "https://devpost.com/software/snap-and-swing"
title: "Snap and Swing"
hackathon: " Play Everywhere: The Build with Snap Games Lensathon"
organization: "Snapchat"
winner: true
words: 1152
team_size: 1
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/simulation_digital_twin"
---

# Snap and Swing

> This is a 2D AR game where players swing their bitmoji on a rope from island to island, gaining points and collecting coins. They must avoid birds and colliding with islands as they do so.

[Devpost](https://devpost.com/software/snap-and-swing) · hackathon [[Play Everywhere- The Build with Snap Games Lensathon]]

## Facets

**mechanism** [[simulation_digital_twin]]

**stack** blender, snaplensstudio, typescript

## How they structured the write-up

- inspiration
- what it does
- how i built it
- challenges i ran into
- accomplishments that i'm proud of
- what i learned
- what's next for snap and swing

## Body

Inspiration The idea was inspired by games such as the mobile game Stickman hook or Marvel's Spider-Man which both heavily rely upon swinging mechanics in game. I was also heavily inspired by Snapchat adaptations of the game Flappy Bird which I had seen on the app. What it does In Snap and Swing the goal is for the player to swing their Bitmoji to as many islands as possible. When the user taps the screen, a rope will extend from the player to the nearest island. When the player lets go of the screen, their character will fly off in whatever direction they have momentum in. This allows the player to swing from island to island. As they do so, coins will be randomly generated underneath each platform, touching these gives the user a slight score boost. In addition, birds are randomly generated which fly across the screen from right to left. If the player comes in contact with these birds, any of the islands or the bottom of the screen, the game ends. Once the game is finished the user can see how their performance stacks up against others on a global scale How I built it Unlike some games with built in swing mechanics, in Snap and Swing the player is able to swing from multiple points across the edges of every island. To accomplish this I wrote two TypeScript functions. These take in a scene object containing all the platforms and then loop through its children. It keeps track of the platform with the nearest distance to the player and the choice of platform was weighted towards platforms that are in front of the player by adding extra distance to platform behind the user in the calculation. This was done to keep the game fast and prevent the user from being stuck on one platform. A similar method was used to identify the closest pivot point but without the weighting. In order to get the swing mechanics working, I created a scene object that I named "Player Hinge" and I gave it a physics body. I wrote a function that was triggered when the player touched the screen. It took in the nearest pivot point and created a hinge object located at the pivot point with Player Hinge as its parent. This allowed the Player Hinge to swing back and forth in a swing-like way. In addition, I created a permanent hinge constraint as a child of the Player Hinge whose target was the player Bitmoji. The reason for this extra hinge was to prevent the player from flipping backwards and forwards as a result of the swing rotation. It ensured the player remained in an almost upright position during the game. To make it look like the player was swinging from a rope, I used a cylinder object. I wrote a function which made it so, upon the user tapping the screen, this rope would be placed at the pivot and scaled to the distance between the player and the pivot point. I also wrote code so that, in each frame, the rotation of the rope would be changed so that it aligned with the player's position. This was done using simple trigonometry. To have an infinite number of islands for the player to swing to, I used pooling. I wrote a function which finds the platform which is the furthest distance behind the player. Once the player reaches a certain distance away from this platform, the platform is moved in front of the player. I added a random variance in the vertical and horizontal gaps between platforms to make the game more unpredictable. I also ensured that new platforms would be placed within a certain vertical distance of the player to prevent the game from becoming impossible. I also added coins which generate below the platforms and trees which generate above. These are children of the island they appear with and each have a random chance of being enabled when the platforms are moved. The bird was generated in a similar way, being randomly placed in front of the player when platforms were generated with a constant velocity going from right to left on the screen. Lastly, I implemented the leaderboard feature using the leaderboard info asset on Snap Lens Studio. I found the game assets for the islands, the bird and the coin sound effect online and I ensured the creator had given permission for them to be used in commercial works without attribution. All other assets were sourced from Lens Studio. Challenges I ran into The largest challenge I ran into was getting the swing physics correct. I initially tried a large number of methods including creating a swing physics engine myself using TypeScript however I eventually settled on using hinge constraints as it was the simplest and best performing method I tested. Once this was completed, however, I faced another issue as the player would flip forwards whenever they disconnected from the last pivot point. As a result, the rope would then appear to pass through the player's head. My solution to solve this was introducing a new pivot point but this took a lot of trial and error when choosing which object should be its parent and its target. Accomplishments that I'm proud of Prior to this project, I had no experience with Snap Lens Studio or game development as a whole. I am extremely proud that I managed to create a working game and I really enjoy seeing Snapchat users playing the game. In particular, I am proud of my solutions to the issues with the swing physics because I think this is a unique solution that I haven't seen used elsewhere. What I learned Over the course of the project, my skills with Snap Lens Studio increased exponentially. Initially, I had struggled to work with physics inside the software and this difficulty was increased due to my lack of experience in game development. By the end of the project, I found I had a great understanding of the game engine and I was able to use some of its features in unique ways to improve my project. In addition, I think my TypeScript skills grew a great deal over the course of the project because I had no experience with the language prior to the project. What's next for Snap and Swing I would like to improve the way platforms are generated to make the game more interesting and challenging. The trees which are spawned in above the platforms are currently only decorations because the player never really has an opportunity to collide with them. I would love to make these assets fully functional parts of the game by placing the islands below the player's height. I will also be making slight tweaks to the size of assets and the speed of the game to make it easier to play. <div