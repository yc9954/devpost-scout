---
slug: "eco-toss"
url: "https://devpost.com/software/eco-toss"
title: "Eco Toss"
hackathon: "Global Gamers Challenge"
organization: "Google"
winner: true
words: 1171
team_size: 4
has_repo: false
has_live: false
has_video: true
tags:
  - "project"
  - "substrate/geospatial"
  - "substrate/video_visual"
---

# Eco Toss

> Ever wondered whether you should recycle kitchen rolls, crisp packets, or used tissues? Find out by playing EcoToss, where players must throw various recyclable objects into the correct recycling bin!

[Devpost](https://devpost.com/software/eco-toss) · hackathon [[Global Gamers Challenge]]

## Facets

**substrate** [[geospatial]] [[video_visual]]

**stack** blender, dart, firebase, flame, flutter

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for eco toss

## Body

Brainstorming Ideas for visualising the ball in 3D space in 2D How to update the position of the ball GIF Scrapped proof of concept for drawing 3D shapes manually using canvas painter class GIF Proof of concept for visualising the ball in 3D space GIF Proof of concept for collision and gravity Inspiration The Eco Toss team are a group of friends who were interested in how recycling works in the UK. Around the UK recycling rules are complicated and vary for each borough, causing people to often sort their recycling incorrectly. This can lead to contaminated recycling bins which often cause the content to be sent to landfills or incinerated as a result! All of our team members were huge fans of the original Paper Toss games, so to spread awareness and educate people on how to sort recycling, our team built an addictive, aesthetically pleasing game that we hope people will enjoy and learn from! What it does Eco Toss is a game with beautiful 3D graphics, featuring minimalist mechanics - the player throws an object to be recycled into a bin by swiping up on their screen. With each throw, the object to be recycled changes randomly, and with it the user will see a new recycling bin appear on the screen representing the correct one to sort into. In this way, the user will effortlessly learn how to sort their recycling subconsciously while enjoying the gameplay! Careful not to trip up, because missing one shot will reset your game! Thankfully the bins in the UK have a big opening allowing for a sizeable margin for error. Despite the generous bin sizes in the UK, the windy conditions lately can throw off the course of the object in the air, and the random wind strength left and right can make the gameplay both challenging and addictive! How we built it Our entire app was built with Flutter, Dart and Flame., and there were two main steps to our plan: Creating two separate coordinate systems Rendering 3D objects as 2D assets Creating two separate coordinate systems with an interface We realised that we would need to distinguish into two coordinate systems, and create an interface between them: The 3D spatial coordinate system, with units in metres, was used to track the position of the items in the game, as well as the bin. It is used for the game's logic, e.g. checking whether the item has gone into the bin, or if it has hit the bin's rim. The 2D rendering coordinate system, with units in pixels, was used to render the game on the screen. This is the coordinate system that Flame uses. The mapping interface is used to convert values between the two coordinate systems, i.e. given a 3D spatial coordinate, where should it be rendered on the screen? Rendering 3D objects as 2D assets For the throwable items, we rendered scenes of 3D items spinning, generating a sequence of images that we could use to animate the items with Flame's SpriteAnimationComponent. With these concepts, we built Eco Toss! (You can see all diagrams, code, and more details here ) Challenges we ran into Apart from figuring out how to render 3D in 2D, the biggest challenge we ran into at the later stages of the hackathon was the dependency of the game physics on the render cycle. Flame uses an update callback with a time delta argument, which describes the amount of time that has passed between each frame. We used this callback to update the position/velocity of the throwable between each frame, which worked perfectly fine in the earlier stages. However, this led to two issues down the line: inconsistent collision when throttling and inconsistent physics between different frame rates. Firstly, inconsistent collision happens when rendering slows down due to throttling etc. We created a rim in physical space, and when the thrown item comes into proximity to the rim, we know that it has collided. However, when rendering slows i.e. time between frames increases, the distance the object has travelled between the two frames can increase to the point where it overshoots the rim, and no collision is detected. Secondly, inconsistent physics can happen between different frame rates because we used some constant values to characterise the physics of the throwable. For example, consider the following formula for air resistance: xVelocityMps += -xVelocityMps * EcoTossThrow.airResistanceVelocityMultiplier; If the frame rate changes for any reason, the rate at which air resistance is applied also changes, i.e. smaller time delta = more air resistance over some fixed time, larger time delta = less air resistance over some fixed time. Accomplishments that we're proud of On a more positive note, we are proud of how far we've come from ideation to a functioning game! We set ourselves the challenge of creating a pseudo-3D game with the limitations of a 2D game engine, and our team has smashed it despite our personal and work responsibilities. We are also really proud of the graphics and art style! Sofia created "2D pastel" styled graphics, using Blender to create the illusion of an object being thrown in 3D space, and yet maintaining 2D visuals with consistent lighting, shadows and perspective. What we learned Flame is versatile: We were able to build a pseudo-3D game with Flame, despite it being a 2D game engine. This is a testament to the versatility of the library. Converting 3D space to 2D pixels: We learned how to map 3D spatial coordinates to 2D rendering coordinates, and how to scale the size of objects as they move further away. We oversimplified a lot of the vector transformations involved with realistic perspective rendering, but we found that the linear transformations discussed in this article were sufficient for our game. Implementing 3D logic in a 2D game engine is hard: You can't use Flame's collision detection, since it's 2D. We had to implement custom collision detection logic, which was a bit of a headache. Separating physics from rendering is critical: As mentioned above, inconsistencies in physics and collisions can happen when the physics is dependent on the rendering cycle, leading to undesirable gameplay. What's next for Eco Toss In the future, the Eco Toss team would love to implement a much bigger range of recyclable objects, and new mechanics in the game to teach players about the various recycling schemes around the world! To make the gameplay more challenging, our team would also love to create a "hard mode" where the user is shown multiple bins of different sizes, in random positions on the screen. In this mode, the user would have to consciously recall which bin is the correct one to sort the object on the screen into before throwing the rubbish away! Additionally, the Eco Toss team is very keen to add a competitive aspect to the game to increase user interaction! We envision a game mode where users go head-to-head on their throwing skills and compete to win glory in the form of virtual points. <div