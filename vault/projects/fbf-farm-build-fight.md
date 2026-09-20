---
slug: "fbf-farm-build-fight"
url: "https://devpost.com/software/fbf-farm-build-fight"
title: "FBF: Farm, Build, Fight!"
hackathon: "AWS Game Builder Challenge "
organization: "Amazon"
winner: true
words: 626
team_size: 2
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/simulation_digital_twin"
  - "domain/agriculture_food"
  - "domain/developer_tools"
  - "user/developer"
  - "substrate/geospatial"
---

# FBF: Farm, Build, Fight!

> How long will you survive? 🌱🏰⚔️

[Devpost](https://devpost.com/software/fbf-farm-build-fight) · hackathon [[AWS Game Builder Challenge]]

## Facets

**mechanism** [[simulation_digital_twin]]
**domain** [[agriculture_food]] [[developer_tools]]
  <sub>weak: finance_payments</sub>
**user** [[developer]]
**substrate** [[geospatial]]
  <sub>weak: web_dom</sub>

**stack** amazon-cloudfront-cdn, amazon-dynamodb, amazon-nova, amazon-q, api-gatweay, aws-cdk, bedrock, bedrock)-tools:-amazon-q-developer, c#, cloudfront, cognito, dynamodb, html, javascript

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for fbf: farm, build, fight!
- credits
- extras

## Body

Main Menu Controls - PC Controls - Mobile Begin your adventure! Farm! Build! Fight! Encounter challenging enemies! Protect your farms! Battle hordes of dangerous mobs! Put your skills to the test! Climb to the top of the leaderboard! About the Project: FBF - Farm, Build, Fight! tl;dr - Try out FBF from your PC\mobile using the link below! Inspiration Our childhood dream was to create a video game, and when the AWS Game Builder Challenge came along, we knew it was the perfect opportunity. Combining our passion for gaming with our skills as developers, we aimed to craft an immersive survival RPG that balances strategy, action, and creativity. What it does FBF is a role-playing survival simulator where players must farm, build, and fight to survive on a mysterious island. Players are equipped with three basic tools - a sword, hammer, and hoe - and must make strategic use of limited daytime hours to prepare for increasingly challenging enemies that appear at night. The game features: Secure account system with username/email login Global leaderboard tracking days survived and time played Cross-platform save system AI-powered NPCs that provide contextual tips based on game state Dynamic day-night cycle with strategic resource management Progressive difficulty through increasingly challenging enemies How we built it We developed the game using Unity and leveraged several AWS services to create a robust cloud infrastructure: Amazon Q Developer for rapid code development and implementation AWS Cognito for user authentication DynamoDB for storing user data, saves, and scores AWS Bedrock with Nova Lite for AI-generated NPC interactions AWS Lambda functions for backend processing API Gateway for managing requests CloudFront and S3 for hosting and content delivery Route 53 for domain management Challenges we ran into Creating a full-scale game while working full-time jobs in just two months demanded efficient use of tools and workflows. Creating AI-generated NPC advice that felt relevant and helpful required careful prompt engineering with AWS Bedrock. Ensuring seamless gameplay across devices involved managing save data and synchronization challenges. Balancing game mechanics and progression difficulty required many playtests and consulting. Accomplishments that we're proud of Completed development in less than two months, with coding only taking 20% of the time Crafted a game that is actually fun and enjoyed by all of our playtesters Created a secure, scalable cloud infrastructure supporting cross-platform gameplay Successfully implemented AI-powered NPCs that provide dynamic, context-aware tips Developed an engaging game loop with multiple strategic elements Built a complete user account system with global leaderboard functionality Achieved our childhood dream of creating our own video game What we learned The power of modern AI tools in game development Practical experience with AWS services and cloud architecture Efficient development practices using Amazon Q Developer Implementation of serverless architectures for gaming The importance of user experience in game design How to balance technical development with creative elements What's next for FBF: Farm, Build, Fight! We’re looking forward to expanding the game with: Online Co-Op Mode : Enabling players to team up with friends for a shared survival experience using AWS GameLift. New Features : Adding more enemies, weapons, character customizations, game modes and activities to keep gameplay fresh and exciting. Player Feedback : Continuously improving the game based on suggestions from our hopefully growing community. We’re thrilled to have brought FBF to life and can’t wait to see where the journey takes us next. Join the adventure and show everyone how long you can survive! Credits Most visual assets by Kenmi Virtual Mobile Keyboard by Lilly Games Gamer font by memesbruh03 SFX by pixabay Background Music by Suno.ai (all sources used are under commercially royalty-free licence) Extras If you want to learn more about how we added AWS features to our game, check out our AWS community BlogPost <div