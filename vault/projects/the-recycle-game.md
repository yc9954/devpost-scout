---
slug: "the-recycle-game"
url: "https://devpost.com/software/the-recycle-game"
title: "The Recycle Game"
hackathon: "Alexa Skills Challenge: Tech for Good"
organization: "Amazon"
winner: true
words: 1077
team_size: 0
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "domain/developer_tools"
  - "domain/education"
  - "user/developer"
  - "user/educator_student"
  - "substrate/video_visual"
---

# The Recycle Game

> The Recycle Game gets everyone in your household, classroom, company and school involved in a competition to recy

[Devpost](https://devpost.com/software/the-recycle-game) · hackathon [[Alexa Skills Challenge- Tech for Good]]

## Facets

**domain** [[developer_tools]] [[education]]
**user** [[developer]] [[educator_student]]
**substrate** [[video_visual]]

**stack** asp.net-web-api-2.0

## How they structured the write-up

- inspiration
- what it does
- how i built it
- challenges i ran into
- accomplishments that i'm proud of
- what's next?

## Body

Reporting on household recycling My Account at daysfly.com showing list of current players My Account at daysfly.com showing configuration screen for a player Inspiration The Recycle Game is a way to compete for the title Champion of the Environment within your household, extended family, neighborhood, friends, classroom, company or school. Keeping our world clean is a responsibility we learn to enjoy, with a little help. Everyone learns best when learning is fun. That's where The Recycle Game comes in! It's a game where we practice recycling to earn points to win. As we do, the world we live in wins with us. What it does When you start, just tell Alexa to add players to the game (by first name). E.g., Alexa, tell The Recycle Game to add John to the game. Or you can tell her to add a player, and Alexa will use dialogue directives to request the player's name from you. Once you are in the game, tell Alexa you want to play, and she will ask you what you are recycling. You can describe the object and how many you are putting into the recycle bin. I am recycling four soda cans. If you make a mistake, you can say, "Take it back out!" and Alexa will remove it from your score. Alexa will stop you if you try to recycle something that you shouldn't recycle from home (e.g., batteries). You can ask Alexa questions about what you can recycle, e.g., Can I recycle a pizza box? You can also ask to take a quiz on home recycling. You can ask how a player in your household is doing for any interval. How did John do last week? Alexa will tell you what they recycled and the total number of points they earned. You can also ask who was the winner for any given interval. Alexa, ask The Recycle Game who won last month. The various players will be ranked by the number of points they earned. Use The Recycle Game to challenge your kids to make smart decisions about recycling. Alexa, tell the Recycle Game that Dylan recycled two newspapers. Alexa, ask the Recycle Game who was the winner last week. Alexa, ask the Recycle Game how Dylan is doing this week. By creating and linking your account at https://daysfly.com , you will be able to see your progress on the My Account page. (As long as you have at least one player in the game linked to your account, you will see a tab appear for The Recycle Game.) If you link your account within the game by saying, "Link My Account," you can play the game across all your Alexa devices. You can then log in and run reports on your recycling, and you can upload a photo to use as an avatar within the game (assuming you have an Alexa device with a screen). Each account at Daysfly.com has a unique code that can be used to create a group (such as extended family or a classroom). If you share that code with other players, they can enter it on the My Account page and link that player to the group you created. The person who supplies the code is the group administrator. The administrator can see all associated players in their reporting. It's a way to compete with all the students in your classroom, school, or extended family! The Recycle Game is an educational game built for all ages. It can be accessed by any device that uses Amazon's Alexa voice service, and it supports devices that have a display by showing photos of items you are trying to recycle. You install the game by saying, "Alexa, enable The Recycle Game." Then you can tell Alexa to play The Recycle Game. How I built it This is an ASP.NET Web API written in C#. Challenges I ran into I discovered that display directives are not compatible with dialog directives. When I use dialog delegates for more focused follow-up questions, I lost the ability to show pictures on my Echo Show. It doesn't make much sense, and I posted this problem on the developer forums. In fact, dialog delegates are just the kind of thing you want to use with a list template so that people can either say or choose (by touch) within a narrow range of options. As soon as Amazon fixes this, I will make sure even more display directives are used throughout. I couldn't publish this in India because, apparently, Indian English doesn't accept the First Name slot for either US or GB. But it appears in the US, Canada, UK, and Australia. We're all set to recycle in English across the globe! In addition to being a software architect, I have a Ph.D. in Social Ethics. I'm proud to offer technology that benefits the world we live in. Accomplishments that I'm proud of I use dialog and display directives for greater engagement. The dialog delegates provide for a more true and accurate AI experience as Alexa "listens" contextually depending on what one would reasonably be expecting as a response in a multi-turn conversation. E.g.: "I'm ready to play." "Who is doing the recycling?" "Michael." "What object are you trying to recycle?" "A cup." "Is it paper, plastic or styrofoam?" "Styrofoam." "You can't recycle that!" I use display directives to provide a more robust experience when a screen is available. E.g., you get to see photos of the things you're trying to recycle. When you do, it becomes clear why dirty paper towels and pizza boxes shouldn't end up in the recycling bin. I also have memory persistence within a session, so that once a player is named (and in some cases, a time frame or object type) that information persists across additional queries. E.g.: "How is Michael doing this week?" followed by, "How did he do last week?" (remembers which player we're talking about) followed by, "How did Bob do?" (remembers that we're speaking in reference to last week). I developed a module for unpacking the Amazon.DATE slot-type and using it to filter results over a date range in SQL queries without losing the more casual reference point of plain English (e.g., last week, this month, yesterday, etc.). This game is available across the globe -- US, UK, AU, CA. What's Next? I plan to support the new (beta) features of the Echo Show by providing more feedback on the display, including graphs. <div