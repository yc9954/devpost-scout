---
slug: "un-helpful-bot"
url: "https://devpost.com/software/un-helpful-bot"
title: "(Un)helpful bot"
hackathon: "Hack the Northeast: Beyond"
winner: true
words: 454
team_size: 3
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "domain/education"
  - "user/educator_student"
---

# (Un)helpful bot

> A bot that will never give you up (unless you politely ask)

[Devpost](https://devpost.com/software/un-helpful-bot) · hackathon [[Hack the Northeast- Beyond]]

## Facets

**domain** [[education]]
**user** [[educator_student]]

**stack** discord.js, javascript, node.js

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for (un)helpful bot

## Body

Inspiration Making a usable bot be as annoying as possible without preventing use. Taking particular inspiration from Rick Astley's Never Gonna Give You Up Further, annoyingness is greatest when the nuisance is only just as small as to warrant further action. This is captured by the ease of relaxing annoyingness through a couple of variables. What it does All non-bot messages have a chance of being deleted at a random time in the future. - Messages deleted within 100ms are followed by a helpful explanatory message. All messages sent by the bot are embedded with a link to Rick Astley's Never Gonna Give You Up By messaging !kick @user, the user mentioned has a 50% chance of being kicked. The other 50% of the time, the author gets kicked By partaking in a voice channel chat, you will have the good fortune of being joined by the bot. This occurs after a random time interval. Upon doing so, all users in the channel will become server muted, and the rickroll will commence. You must remain in the channel until the bot finishes to lose the server mute. Any time your message contains "I'm", a classic dad joke comes your way. Any time your message contains "dad", a dad joke follows. Any message that is above 100 characters is followed by a snarky response. At 02:00, everyone will be messaged. If you ask a question, expect a link to be sent your way to help you use google. How we built it We used node.js for the code, utilizing the discord.js api The embed is done by adding a wrapper to the Discord.TextChannel.send() function The bot is run on a server which is possible due to the Cambridge University Student-Run Computing Facility Challenges we ran into Time zones became an issue with 3 out of 4 members residing in the US & Canada, and the final member being located in the UK. Further, the server on which the bot is run by the UK member so this decreased usability somewhat. This was fixed through the loss of a sleep schedule. Separation obviously makes things difficult. By using git and discord, the issues arising from this were reduced None of us have much experience with node.js or discord, with only one member having made a discord bot before. The server we were using does not allow for python to be run directly requiring node.js to be used. Accomplishments that we're proud of Making a bot that annoyed even us in production. What we learned Discord API classes and methods. Function wrapping What's next for (Un)helpful bot An overarching annoyance variable that can be set upon installation. This would simply adjust the probabilities of events happening. <div