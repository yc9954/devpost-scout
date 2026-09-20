---
slug: "ma-2yohxn"
url: "https://devpost.com/software/ma-2yohxn"
title: "Motion Effect Kit"
hackathon: "Facebook Hackathons: AR"
organization: "Facebook"
winner: true
words: 600
team_size: 2
has_repo: false
has_live: false
has_video: true
tags:
  - "project"
---

# Motion Effect Kit

> A set of effects for Instagram Reels with custom patches to extract movement directions and areas.

[Devpost](https://devpost.com/software/ma-2yohxn) · hackathon [[Facebook Hackathons- AR]]

## Facets


**stack** shader, sparkar

## How they structured the write-up

- inspiration
- what it does
- how we built it
- accomplishments that we're proud of
- what we learned
- what's next for „motion effect kit“

## Body

Inspiration A huge amount of Reels are focused on dancing. We wondered: How can we make the expression of dancing in Reels more interesting. We were inspired by motion amplification that shows micro movements in machines. The tool finds the moving areas, the direction they're moving in and enhances those movement to become visible. What it does While dance movements are already visible, we enhance them by extracting their directions and create different effects that dancers can use to make their dancing look more exciting. Arrows, the first effect we created for this Hackathon The filter understands which part of the dancer is moving up, down, left or right and translates those movements into the separated edges of the silhouette. After the SegmentDirection Tool was created we came up with four different filters that use that new function in fun ways. Our ideas came from manga, kirakira and... Rihanna. 0. Line Ripples The dancer's movements are translated into graphical ripples around them. They emphasize the current dance moves and also, by slowly fading away, show the past moves. 1. Energetic Steam This effect is created to give more energy to the dancer's performance in Reels. The divided edge area of the segmentation balances the amount of steam and its direction. 2. Kirakira Trail The fascination of kirakira effects is undeniable. We wanted to bring kirakira to the next level by making them particles that react to your movements. 3. When the Sun Shines We Shine Together The dance moves create water that travels, as if it got momentum. So rather than just upwards "falling" water, the movement's direction is shown in the direction the water flies away. How we built it The core system of all effects, the SegmentDirection Tool, is based on the extraction of the segmentation alpha channel's travel direction. This is achieved by acquiring the adjacent pixels and the delay frame. We have generated segmentation alphas for each direction of movement and created a patch asset that can retrieve them. A Patch Asset to split the segmentation we created The SegmentDirection Tool allows you to create more complex segmentation effects that are based on the movement's direction. We created the four different effects to show the potential of this idea and its advantage for Reels filters. The filters will be published separately, but for demonstration purpose we combined them into one. Eventual fps lacking doesn't happen in the separated filters. Accomplishments that we're proud of We started our team for the first Hackathon this year. Unfortunately, our black hole filter didn't make any place at that time, but the teamwork was perfect. We appreciate each other's talents and we are proud that we were able to participate in this Hackathon again with the same team. This time we took the hacking part more literal and "hacked" a new function into Spark AR, while also focusing on making useful and fun filters. We hope other creators benefit from the SegmentDirection Tool and create beautiful filters. Adrian Steckeweh @omega.c + Hayato Kuno @kuno.fell.asleep What we learned We've gained a better understanding of new features like delay frames and render passes. What's next for „Motion Effect Kit“ With the SegmentDirection Tool it is now possible to track motions and their direction. It's an idea that's only possible because of the latest Spark AR Studio, and we think it's going to be the helpful for other creators. We'd love to see what kind of filters other people can create by distributing the patch. We also hope to create more effects that take advantage of this feature ourselves in the future. <div