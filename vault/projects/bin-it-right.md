---
slug: "bin-it-right"
url: "https://devpost.com/software/bin-it-right"
title: "Bin It Right"
hackathon: "Global Gamers Challenge"
organization: "Google"
winner: true
words: 568
team_size: 8
has_repo: true
has_live: true
has_video: false
tags:
  - "project"
  - "domain/transportation"
  - "substrate/code_repository"
  - "substrate/video_visual"
---

# Bin It Right

> Swipe, sort, and conquer in 'Bin It Right'! Experience the thrill of waste management in this eco-conscious game. Your actions make a difference – play now and level up your green impact!

[Devpost](https://devpost.com/software/bin-it-right) · hackathon [[Global Gamers Challenge]]

## Facets

**domain** [[transportation]]
**substrate** [[code_repository]] [[video_visual]]

**stack** dart, flame, flutter

## How they structured the write-up

- inspiration
- what it does
- what all are involved
- challenges we ran into
- accomplishments that we're proud of
- what's next for bin it right
- educational content

## Body

Green Wins Gallery Inspiration The genesis for this game was borne of a very real, everyday challenge we encounter in our daily lives – waste segregation and disposal. Despite the apparent simplicity of the chore, the real life implications and complexities of proper waste management are huge. Our objective was to craft an engaging gaming experience centered around this concept. What it does In our game, players take charge as eco-friendly waste collectors, navigating their vehicles through diverse urban landscapes. As they progress, players are prompted to make eco-conscious decisions regarding waste segregation, fostering awareness of responsible environmental practices. What all are involved The project can be divided as parts below: Loading Controllers & Persistence Game & Overlays Animations Loading The main reason of the loading page was to load all the audio assets and cache images/animation assets. Controllers & Persistence All the stored items go through a set of controllers, which are listened for changes all over the app. Game & Overlays Finding the perfect balance between in game renders and overlays was quite tricky and finally via modularizing the components, we figured the right way to balance this out. Animations Found out the power of Flutter animations while working on this project. Right from sprite animations to sprite sheet animations. Challenges we ran into The biggest hurdle was the limited time available. Discovering the competition with only a week to develop the game presented a significant challenge. Thankfully, with the power of flutter and flame things were smooth. While we had a clear vision for the animations, translating those ideas into the app proved to be another obstacle. Fortunately, we were able to leverage the power of Sprites to achieve our desired results. Accomplishments that we're proud of Many accomplishments made us proud while working on the project, right from the guide path we build from the trash icon to the truck. @override void paint(Canvas canvas, Size size) { var path = Path(); path.moveTo(leftTop.x, leftTop.y); path.lineTo(rightTop.x, rightTop.y); path.quadraticBezierTo( (rightTop.x + rightBottom.x) / 2 + ((leftBottom.x - leftTop.x) / 2), (rightTop.y + rightBottom.y) / 2, rightBottom.x, rightBottom.y); path.quadraticBezierTo( leftBottom.x - ((leftBottom.x - rightBottom.x) / 2), leftBottom.y - ((leftBottom.x - rightBottom.x) / 2), leftBottom.x, leftBottom.y, ); path.quadraticBezierTo( (leftTop.x + leftBottom.x) / 2 + ((leftBottom.x - leftTop.x) / 2), (leftTop.y + leftBottom.y) / 2, leftTop.x, leftTop.y); path.close(); canvas.drawPath( path, ... ); } Through the combined power of Path and QuadraticBezier curves, we were able to achieve the exact visual path we envisioned. What's next for Bin It Right As passionate creators of 'Bin It Right,' our vision extends beyond its current iteration. We plan to enhance user engagement by introducing dynamic levels and challenges, incorporating user-generated content to foster a sense of community, and expanding educational elements with real-world waste reduction tips. Collaborations with environmental organizations are in the pipeline to amplify our impact and encourage eco-conscious gaming. Additionally, we aim to optimize the game for accessibility and explore partnerships for wider distribution. Our commitment is not just to create a game but to drive lasting change, transforming 'Bin It Right' into a powerful catalyst for global awareness and action on waste management and sustainability. Updates Added a green wins gallery for meta progression. Responsive Multiplatform support Bug fixes Please find the refined APK here -> https://drive.google.com/file/d/1NN6NNxOaIHTFhxm_UX4_3fBFQeeSSJkR/view?usp=sharing Educational content https://medium.com/@dhanish_9850/4dab80370ef2 https://medium.com/@dhanish_9850/abfdc05a3ce8 https://medium.com/@dhanish_9850/2b9d8aa82bbb https://medium.com/@dhanish_9850/3662c28765a8 https://medium.com/@dhanish_9850/7761a143ca74 https://medium.com/@dhanish_9850/creating-a-sprite-scroller-for-vertical-infinite-scrolling-in-flutter-flame-d6ca2a868c8e https://medium.com/@dhanish_9850/d9bceba97f03 https://medium.com/@dhanish_9850/exploring-sprite-animation-and-animation-ticker-in-flutter-flame-b338a63ce9a4 Note: Now supported for screens with width of 375px and above. <div