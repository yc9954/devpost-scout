---
slug: "mein-strand-der-strandmanager"
url: "https://devpost.com/software/mein-strand-der-strandmanager"
title: "Mein Strand - Der Strandmanager (Beach Manager)"
hackathon: "Alexa Skills Challenge: In-Skill Purchasing"
organization: "Amazon"
winner: true
words: 993
team_size: 1
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "domain/developer_tools"
  - "user/developer"
  - "substrate/structured_db"
  - "substrate/video_visual"
---

# Mein Strand - Der Strandmanager (Beach Manager)

> Mein Strand is a real-time strategy game. The goal is to turn a small beach into a beach paradise. Achieve this by investing in new buildings and increasing the popularity of your beach.

[Devpost](https://devpost.com/software/mein-strand-der-strandmanager) · hackathon [[Alexa Skills Challenge- In-Skill Purchasing]]

## Facets

**mechanism** [[realtime_stream]]
**domain** [[developer_tools]]
  <sub>weak: education</sub>
**user** [[developer]]
**substrate** [[structured_db]] [[video_visual]]

**stack** alexapresentationlanguage, amazon-web-services, ask-sdk, dynamodb, lambda, node.js, s3, unity

## How they structured the write-up

- inspiration
- what it does
- in skill products
- how i built it
- challenges i ran into
- accomplishments that i'm proud of
- what i learned
- what's next for mein strand - der strandmanager

## Body

The splash screen of Mein Strand The skill on a device with display. The bus station is one of the first buildings that can be built. The beach can for example be extended with a souvenir shop and an ice cream parlour. If the cruise pier is built, many tourists will come to the beach. A surf school can also be built on the beach. The beach in level 7 The beach in level 14 The beach in level 20 Inspiration I'm a big fan of classic strategy games, like Sim City or Roller Coaster Tycoon. I was wondering if such a strategy game could work on an Alexa device. I also didn't find any more complex strategy games in the German Skill Store. Thinking of games with features like for example realtime functionality, which means they continue to run while the skill is inactive. (In the case of my beach this means that visitors come to the beach even when the skill is inactive). So I wanted to develop a game that would entertain the player not only for one session, but for a longer time. That was the inspiration for me to develop the strategy game 'Mein Strand'. What it does 'Mein Strand' is a real-time strategy game. The goal is to turn a boring small beach into a trendy beach paradise. Invest in beach chairs to get more visitors to your beach and increase the popularity of your beach by constructing buildings. Make sure you clean your beach regularly, as more or less visitors come to the beach depending on how clean it is. Visitors pay entrance fees for the beach. In addition to the entrance fee, you can earn money by selling ice cream. You receive the proceeds at the end of each beach day. Make the right investments and your beach will soon be at the top of the ranking. All that would be quite a lot of work alone, so you have three employees supporting you on your way to becoming a top manager: Günther, the owner of the building yard, supports you in investing in buildings and beach chairs. Luigi is the owner of the ice cream parlour, he takes care of the ice cream business. Carmen is the owner of the beach bar. At the beach bar you can play bar games and win money with a little luck. The skill is also optimized for devices with display. The beach is visualized, which gives the player an even better experience. In Skill Products Currently the game contains two In Skill Products: The first In Skill Product is the full version of the game. In the trial version the beach can be upgraded up to level 6. After that you can continue playing, but no more buildings can be constructed. Only after the purchase of the full version the beach can be extended unlimited. The second In Skill Product is the automatic cleaning robot . This product has the following purpose: Normally the beach is polluted over a few beach days. Depending on the level of pollution, more or less visitors come to the beach, which affects the revenue. The automatic cleaning robot keeps the beach clean at all times. This means that a lot of visitors are always coming to the beach and the income is maximized. How I built it I developed the skill using node.js and ASK SDK. As development environment I used Visual Studio code. All media files like audio and images are on Amazon S3. As database I use Dynamo DB and for Logs i use Amazon Cloudwatch. For the visualization I used the APL Toolkit in the Alexa Developer Console. The beach, the game scenes and the buildings were modeled using Unity. Challenges I ran into One challenge was the implementation of In Skill Purchasing. I have never worked with the API before. Another challenge was the implementation of the game loop. The calculations of the game progress, even if the skill is inactive. Calculate how many visitors are visiting the beach over a longer period of time, taking into account the popularity and the increasing pollution of the beach if the player does not clean it. The implementation the sale of ice cream depending on various parameters such as ice cream expiration date. These were partly very complex functionalities, which I thought would be easier. Also the modelling of the beach in Unity was very demanding, because I had hardly any experience with Unity before. Accomplishments that I'm proud of I am very proud of the game-loop that really works very well. I'm also proud of the support for display devices. The designed game scenes and the modelling of the beach and the resulting experience that players can experience on Alexa devices with display. It gives me great pleasure to see that players enjoy the game and to see that players are willing to invest in In Skill Products. What I learned Developing a rather complex strategy game is more time consuming than I thought. ;-) I have learned to use ISP and APL and will definitely use these APIs in other skills. What's next for Mein Strand - Der Strandmanager I will continue to expand the game functionalities. Implement new functionalities such as additional employees and buildings. The existing employees should also get more functionalities, e.g. the ice cream parlour can be expanded with additional equipment, it should be possible to advertise the sale of ice cream. In the beach bar the sale of beverages should be possible. Additional In Skill products will also follow. I would like to roll out the skill in other Skill Stores as well. And I would like to transfer the concept of 'Mein Strand' to other strategy games. I could imagine a strategy game similar to Roller Coaster Tycoon, a game in which an entertainment park is to be built. Or a game where you have to manage a beer brewery. <div