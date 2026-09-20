---
slug: "british-poetry"
url: "https://devpost.com/software/british-poetry"
title: "British Poetry"
hackathon: "Alexa Skills Challenge: Life Hacks"
organization: "Amazon"
winner: true
words: 803
team_size: 1
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "domain/developer_tools"
  - "domain/mental_health"
  - "substrate/code_repository"
  - "substrate/structured_db"
---

# British Poetry

> My British Poetry Alexa skill recites beautiful verse on demand.

[Devpost](https://devpost.com/software/british-poetry) · hackathon [[Alexa Skills Challenge- Life Hacks]]

## Facets

**domain** [[developer_tools]] [[mental_health]]
**substrate** [[code_repository]] [[structured_db]]

**stack** mysql, node.js, php

## How they structured the write-up

- inspiration
- what it does
- how i built it
- challenges i ran into
- accomplishments that i'm proud of
- what i learned
- what's next for british poetry
- extra

## Body

British Poetry by Adam Krell Help screen Sonnet 18 Alexa Challenge Inspiration I heard a friend recite Rudyard Kipling's famous poem "If" one day. Its incisive message struck me as a piece of timeless wisdom I had to commit to memory. So I copied it to my phone and began memorizing it between activities in my day. I was surprised how renewing and transforming that experience was, and I hungered for more. A world of beautiful prose and wisdom opened up to me as I began to really explore poetry for first time in my life. I usually read non-fiction and enjoy the hard sciences. But here was a world of literature and beauty and I knew I had to make it a part of my daily life. And so, the idea was born. Why not program our new Amazon Echo to read me poetry on demand? What it does British Poetry recruits Lady Alexa to recite poems from a vast collection of British bards throughout history. She can serve up a random poem from her storehouse of manuscripts or you can make a request to her ladyship for a specific poem or poet. How I built it I used the Alexa SDK, lambda, node.js and a LEMP backend powered by an EC2 server. Challenges I ran into I wanted to make Lady Alexa's reading of verse approximate the grace of a human reader. I had to program the delivery system to format and use Amazon's Speech Synthesis Markup Language (SSML) on the fly to provide a pleasing reading experience for the user. Creating the database of poetry was no small feat, which came down to a lot of typing on my part. After first publishing my app I noticed that users were sometimes having a difficulty finding the exact poem they desired or correctly pronouncing the poet's name. I developed a language model and search technique that corrected for mispronunciations or the incorrect matching of author with poem title. Accomplishments that I'm proud of From the start I made the skill take advantage of a screen display. While not necessary to enjoy the skill, a screen allows the user to scroll through the poem and see a picture of the poet while Lady Alexa elegantly speaks the verse. Using the display templates allowed me to format the content for the screen using design patterns from William Morris, a famous Victorian artist. The search technique I developed does a pretty good job of finding the poems and poets. And when a poem or poet can't be found, Lady Alexa will let the user down gently as she reads to them a variety of error messages put to verse. I was even able to add a bit of humor as Lady Alexa will chide a user for requesting a non-British poet, but still graciously fufill their request. What I learned I learned to listen to the users in order to make their experience as frictionless as possible. Also, taking time to put the extra details in, for example using artwork, speechcons and a variety of error messages, enables the user to have a delightful and uplifing experience. Using this technology stack provided a great opportunity to explore the AWS world and see how those technologies can be used. Of course, I was able to dive into a wealth of beautiful poetry full of sublime wisdom and insight. What's next for British Poetry I plan on making the poets and their poems available as a scrollable list for the user to explore. And I will be adding more content. Extra British Poetry can be used by anyone. Children love it. My friends find it as inspiring and renewing as when I first memorized Kipling's poem. British Poetry is a voice app on the Amazon Alexa platform. Imagine the wealth and beauty of British poetry available to by simply asking. I pretty much start my day being renewed from a counsel of wise and thoughtful poets dating back hundreds of years. It's important to learn from the past. Everyone is a child of their own time but we can easily forget that, and dimiss people because of ideas they held that we find offensive. But they had wisdom, too. And we can as, discrening listeners, exact that wisdom to make our world a better place. It was fun using this avatar, Lady Alexa, as the one the user is interacting with. I think it gives the experience a more human touch and draws the listener into the world of British life, much like a BBC period drama does. I designed, created, and deployed both front and back ends of the app. I have experience with database management as well as UI design. This project allowed me to employ diverse skills to bring the project together. <div