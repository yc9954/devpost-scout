---
slug: "match-3-remix-world"
url: "https://devpost.com/software/match-3-remix-world"
title: "Match-3 Ultimate Remix"
hackathon: "Meta Horizon Creator Competition: Open Source Champions"
organization: "Meta"
winner: true
words: 1181
team_size: 1
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "domain/developer_tools"
  - "user/developer"
  - "substrate/code_repository"
  - "substrate/video_visual"
---

# Match-3 Ultimate Remix

> Everything you need to start building your own Match-3 style mobile game. Built with remixing and learning in mind with fully commented code, plug & play modular assets, a full readme, and more.

[Devpost](https://devpost.com/software/match-3-remix-world) · hackathon [[Meta Horizon Creator Competition- Open Source Champions]]

## Facets

**domain** [[developer_tools]]
**user** [[developer]]
**substrate** [[code_repository]] [[video_visual]]

**stack** metahorizondesktopeditor, typescript

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for match-3 ultimate remix

## Body

Screenshot of the Web Version of the Game Screenshot of The Mobile Version Inspiration We have always been fans of match-3 style games and felt like these types of games are under-represented right now on the Meta Horizon platform. We thought this would be a great opportunity to inspire other creators to start making games in our favorite genre. We really are enjoying the MHCP and the community around it so we were very excited to be able to give something back to the community. What it does Match-3 Ultimate Remix is a plug and play remixable world made to replicate the standard match-3 style gameplay. It gives game developers a great jumping off point when starting to build a matching game. It also is a place to learn how to build a 3d-as-2d style game in Horizon Worlds Desktop Editor that supports both web and mobile form factors easily. Key Features A commented Codebase that is easy to learn from and customize for your game. Plug and Play assets and entities can be used as a whole or pulled out of the remixable world and used on their own to speed up development of your project. Fully functional traditional match-3 game that can be enjoyed right out of the box. Matchable Object assets are automatically sized to fit whatever gameboard size you pick and can easily be swapped out for other models. Customizable gameboard that can be updated to be any size and shape to perfectly fit your idea. Easily increase the number of objects required as a “match” without any code changes. Functions have been separated out so they can easily be adjusted to fit your needs. I.e. Calculating score based on type of matched object, or the formula that you wish to use can easily be adjusted in a single place. Fully functional entity pools reduce any hitching while the player is playing the game and help optimize performance. Easy to add or remove matchable objects and adjust them to your specific game’s needs. Built in menu and UI system ready to easily add additional features to. Custom camera controls that keep the player’s avatar in view while allowing them to play what feels like a traditional mobile game. Simple VFX And SFX have been included as a jumping off point to get you started “Juicing” up the game. Everything is clearly labeled and built to work out of the box. How we built it We built around the idea of modular functionality. Each module is built to handle a specific task that can easily be connected with other modules as needed to complete certain game actions. This means that each entity has limited scope in what it is responsible for and can be fairly simple to understand. The game has two main phases. Settling and Matching. In the Settling phase the board pieces fall into place and calculate matches on the board. This will continue until we reach a board state where there are no matches. Then we enter into the Matching phase where we wait for the player to make a move by swapping two pieces on the board. If the swap results in a match then we re-enter the Settling phase. Otherwise we move the two pieces back and the player can try again to find a match. We spent a long time working on the flow of the game to make sure that it would be easy to add and remove elements as needed. It took a lot of trial and error but we think that we got it to a good place in the end. Read more about the world in the README Challenges we ran into There were two main challenges that we ran into. The first was game feel. We really struggled with getting the game to feel smooth. There are so many moving parts that making the game feel natural to play and not like a chore was really difficult and took a while adjusting all the different number settings. I'm sure some remixer will come along and make them even better. The second and bigger challenge that we ran into was getting the order of events to all first correctly all of the time. This is a big reason we think that this starting off point will be so helpful to other creators like us. Promise based architecture is incredibly useful, but also can be really difficult to get right. We constantly were running into issues of match-able pieces doing things out of order or thinking they were in a place they weren't. It took a while to get it all to the point where it just works correctly. Accomplishments that we're proud of We're really proud that we were able to get to a point where we were able to add polish and juice to the game. The week before this was due we were still struggling to get everything working correctly. But then everything just came together with some elbow grease and hard work. That allowed us to add custom models, VFX, and SFX to the game. And that really brought everything together. We're also just incredibly proud to finish the project. This is our first time entering a timed project like this and it was definitely a learning experience. The fact that we were able to finish something and submit it on time is something we are so excited about. The base game is also just fun to play. Which isn't too surprising since Match-3 games are incredibly popular. But, it is nice to see that our variation on the base version of it still makes the dopamine tick in the brain and make you want to keep finding that next match. What we learned We learned a lot about time management when it comes to projects with a quick turn-around. Correctly organizing what work to do when is not an easy thing and we definitely know how we would approach it differently next time. We learned that building a framework that someone else can build on top of is important and hard work. You have to really think about what would be useful in any given scenario, and try to predict ones you don't even know exist. Also writing code so that other people can read it is it's own beast entirely. But I think it really forces you to think critically about what you are doing, and you definitely end up writing better code because of it. We will definitely be able to take all of these learnings into our next projects and feel really prepared for what ever comes our way. What's next for Match-3 Ultimate Remix I can't wait to get in there and remix my own world! I want to try adding high-scores, and changing how the scores are calculated. Maybe adding some custom explosions when you get really big matches that clear our a large part of the gameboard. I was also thinking it could be fun to add in a multiplayer option! There are so many different possibilities! <div