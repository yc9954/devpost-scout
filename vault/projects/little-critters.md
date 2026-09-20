---
slug: "little-critters"
url: "https://devpost.com/software/little-critters"
title: "Little Critters - Advanced hand tracking update"
hackathon: "Meta Horizon Start Developer Competition"
organization: "Meta"
winner: true
words: 536
team_size: 1
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "substrate/video_visual"
---

# Little Critters - Advanced hand tracking update

> Advanced hand tracking update for our mixed reality tower defense game Little Critters. Focuses on interactions and response based on hand shape and gestures using the context of real-world surfaces

[Devpost](https://devpost.com/software/little-critters) · hackathon [[Meta Horizon Start Developer Competition]]

## Facets

**substrate** [[video_visual]]

**stack** meta, mruk, quest, unity

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for little critters

## Body

GIF Hand tracking is combined with physics and scene tracking GIF Context of the real world surface orientation affects hands interaction response GIF Multiple grab techniques are supported Some interactions can only be achieved with hands Inspiration Last month we released Little Critters , a casual tower defense game built from the ground up for mixed reality. We designed the game around cutting edge mixed reality features including scene tracking to drive the gameplay and depth occlusion to blend the virtual with the real. Hand tracking is a great tool for immersing players in mixed reality. For the Meta Horizon Start competition we chose to build an advanced hand tracking update that refines and extends the hand tracking support in Little Critters. Our aim was to make it a showcase of what is possible and one of the best examples of hand tracking on the Meta platform. What it does This update to Little Critters improves hand tracking support, taking things to the next level: Scene tracked surfaces including walls, floors and ceilings are used for extra context, e.g. players can squash enemies between their hands and a real world surface. Hitting at a grazing angle to the surface will knock enemies off the surface instead of squashing them. We reworked all hand interactions including picking up, grabbing and throwing to be more accurate and responsive. Added gestures and interactions that are only available when playing with hand tracking. How we built it We developed a custom gesture recognition system for greater accuracy to support the needs of the game. The system is calibrated with multiple different hand poses which then drives the game's general input system. Special rules cater to tracking loss, so that carried items aren't dropped if the player's hands go out of view of the tracking cameras. In addition, we developed different responses to physics collisions between the player's fingers and the enemy critters. The orientation of nearby real world surfaces from scene tracking and the velocity of the player's hand are combined to provide the appropriate response in the critter's behaviour. Challenges we ran into In playtesting we noticed that when players pick up virtual objects, they use different hand poses, e.g. a thumb + index finger pinch, closing the fingers in a 'crab claw' pose, or a full fist grab. We initially expected played to use a pinch gesture, so we needed to refine our grab system to support these multiple different hand shapes. Accomplishments that we're proud of We are especially proud of how we have managed to combine hand tracking with scene tracking to build an extensive range of new interactions that goes beyond the standard pinch and poke gestures. What we learned Our team learned to look beyond simply creating a drop in replacement to controllers, looking at ways to explore how hand tracking can offer new, unique interactions for the player. We also learned how to adapt to player's needs as they have different expectations for how they should be able to use their hands to interact with virtual objects. What's next for Little Critters We are continuing to build content updates for Little Critters and will be regularly updating the title on the store! <div