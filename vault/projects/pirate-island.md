---
slug: "pirate-island"
url: "https://devpost.com/software/pirate-island"
title: "Pirate Island"
hackathon: "Alexa Skills Challenge: In-Skill Purchasing"
organization: "Amazon"
winner: true
words: 859
team_size: 2
has_repo: false
has_live: false
has_video: true
tags:
  - "project"
  - "domain/supply_logistics"
  - "substrate/code_repository"
  - "substrate/geospatial"
  - "substrate/sensor_telemetry"
  - "substrate/video_visual"
---

# Pirate Island

> Play as a wanna-be Pirate and complete challenges to earn respect an infamous pirate Captain by testing wit and memory. Players can purchase in-game coins to access extra content and mini-games.

[Devpost](https://devpost.com/software/pirate-island) · hackathon [[Alexa Skills Challenge- In-Skill Purchasing]]

## Facets

**domain** [[supply_logistics]]
**substrate** [[code_repository]] [[geospatial]] [[sensor_telemetry]] [[video_visual]]

**stack** amazon-web-services, ask, lambda, node.js, s3

## How they structured the write-up

- inspiration
- what it does.
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for pirate island

## Body

Inspiration Pirate Island is an adventure voice game that allows the players to be the protagonists of a thrilling treasure hunt. The inspiration was to develop an interactive game that captured the essence of simplicity, fun and humorous. The game uses a voice-first philosophy to allow the player to control the outcomes at the same time being lead by a cast of exciting characters that serve as guides, mentors, adversaries and threats. What it does. The voice user experience is designed not only to teach the players how to interact and play by voice-first but also to explain to them how to purchase Gold Coins - the game currency. The main idea of this pirate adventure game is to engage the player with challenges, and some of then will reward them with Gold Coins. However, these Gold Coins are limited, but the player can purchase it with ISP. This purchasing system will allow them to progress on the adventure and searching for more Gold Coins in the game. The players can pay to learn sword and fighting skills, to challenge the game characters in dice or card games and maybe to pay to a pirate to escape from being thrown to the sharks. All this wrapped around an engaging story with interesting characters that allows the player to lose themselves from (the sometimes) daily grind of life and even though it's a voice-first game, we created customised beautiful visual images that aim to further stimulate and engage. How we built it The development was using ASK framework and Node.js. We used AWS services such as lambda to code and S3 for asset storage. We also developed a master JSON file that controlled most of the experience. It is fully extensible and provides an excellent foundation to build upon the story quickly. The code checks the intent for each turn and if it gets back it expects, then it moves to the next turn/level, otherwise, it handles the turn correctly until it gets what it expects. So we can simply add a new story in a new level/turn with no need to update the intents (for existing intents). Like on-demand series, the game will be released in seasons. All we need to do is add a new section for each level and include sub-sections for each turn, and it's managed via the story configuration file. Customised experiences such as the mini-games and sword fighting scenes need some custom development but to add a new narrative, add an APL screen it's as simple as adding in a section and the code does the rest. We used APL and created customised scenery and visual command prompts to help draw the player in and prompt them along the journey. Challenges we ran into The audio restriction of a maximum of 5 files was quite challenging to produce engaging sound ambience. This forced us to split scenes into multi-turns (which wasn't a bad thing as it made the dialogue short and sharp). Also, Polly voices could be better. However, with the game intended for significant growth and development over the next 2-3 months, the following enhancements will include recording actors voices to play the game characters and invest in sound and music to immerse the user in an engaging experience into the pirate world. We will add further engagement through additional metrics into the game within the inventory and player skill score like new swords, jewels and sword/thief/intelligence points etc. Accomplishments that we're proud of Although we started the development almost a month into the challenge I think the effort we put in as individuals who came together for the challenge is immerse and the commit and complementary skillsets. We were able to create some beautiful visual elements that are unique and the way we set the story/level/configuration file, extending the story is made so much easier. End-to-end we have almost 30 minutes of gameplay (not counting if the player further explores unexpected and intention disobeys commands etc. ). This is with the fact that we started a month into the competition and work around our day jobs. What we learned Creating the skill in ASK is not technically difficult as Amazon has made it quite straight forward with templates and a great band of evangelists. It does, however, require hard work and dedication. ISP can be daunting before you crack it open, but when I finally added it, using templates, it was very easier to do! What's next for Pirate Island Content and fun. We ended the season with our young protagonist sailing away with the pirate crew looking for unknown riches, after escaping from a ruthless pirate from whom he stollen a map. Development of bonus content and additional mini-games are our strategies to reach new and current players, also advertise it through social media and engage the players to use their in-game Gold Coins and also to buy or top-up using ISP. We are planning an extensive season 2 where the players will continue to meet new characters that will help them to face more challenges and puzzles that have cognitive and memory benefits and also lots of fun. AmazonAlexaISPChallenge <div