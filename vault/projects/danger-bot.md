---
slug: "danger-bot"
url: "https://devpost.com/software/danger-bot"
title: "Danger Bot"
hackathon: "Snap AR Lensathon 2022"
organization: "Snap Inc."
winner: true
words: 736
team_size: 1
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/on_device_local"
  - "mechanism/structural_withholding"
  - "domain/developer_tools"
  - "domain/education"
  - "user/developer"
---

# Danger Bot

> A multiplayer mashup between a basketball game and a SHMUP. Players attempt to toss bombs into a robot’s head while dodging waves of bullets! It focuses on physicality and intense coop team play

[Devpost](https://devpost.com/software/danger-bot) · hackathon [[Snap AR Lensathon 2022]]

## Facets

**mechanism** [[on_device_local]] [[structural_withholding]]
**domain** [[developer_tools]] [[education]]
**user** [[developer]]

**stack** javascript, lensstudio, multiplayer, physics

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for danger bot

## Body

Dodge the bullets by moving at the right time when Danger Bot fires! Toss bombs into the robot's head to defeat him! Cooperate with your friends to beat Danger Bot! Danger Bot Inspiration We love Augmented Reality, we love old-school SHMUPS, we love Basketball, and we love playing games with our friends. So we decided to put all that into a game! What it does Players attempt to toss bombs into a robot’s head while dodging waves of bullets! It focuses on physicality and intense coop team play. You can play solo, remotely from your friends or within the same room! How we built it The team behind Danger Bot is composed by one art director and three developers. Every little tweak of the game was tested and approved by every member of Flat Pixel. We knew in just a few brainstorms what would be our entry for this Lensathon. The idea is simple, but we knew that the development would be the real deal. We had a pretty good knowledge of Lens Studio and the Connected Lens Module already since we released our first multiplayer Lens " Piggy Smash " just a few months before. Challenges we ran into Technical challenges As we previously created a multiplayer game with Lens Studio, we knew that one of the challenges was the synchronization of all the data between the players . For example, how can we sync the bullet position and rotation to be exactly the same on all devices connected to the same session? We ended up optimizing that part to fit into one unique message sent by the host to the other players when a bullet is created. In fact, by sending the server timer when a bullet is instantiated, the other players can calculate the rest of the logic locally by moving the bullet taking account of the delay between sending and receiving the message. Workflow challenges We're used to versioning tools like Git but unfortunately it does not mix well with Lens Studio. Having that in mind, we decided to divide very separate tasks between each Flat Pixel's member in order to merge as smoothly as possible when someone completed its task. So only one person had the total control of the project and was in charge of integrating the exported work of the others. We merged files and prefabs as soon as possible to keep everyone up to date of the last version of the project. Accomplishments that we're proud of We're very proud of the control of the bomb . We iterated a few times on what input the player should do to toss the bomb. At first we naively do just a Tap control and the bomb was thrown with the exact same force at each attempt. It was very hard to master this so we added a reticle but it was not so helpful. So we then decided to draw the trajectory path of the bomb before the player throws it, and giving them more control by changing the force accordingly to the duration of the touch control . Our third attempt was to use a drag control and the player was able to also choose the direction of the trajectory. However we thought that the control should be simple enough for the player to understand what to do. The final recipe was to " aim assist " the player if they are at the right distance of the robot and they're targeting correctly enough the ears targets on the robot's head. This gives the player a good feeling about what to do and how to master it. What we learned We learned what we learn every time we make a game, but never seem to remember: Keep it simple! There are so many features we had to cut, and so many little tweaks and bits of polish we would've loved to include. Always make room in your schedule for unpredictable bugs. What's next for Danger Bot Our next move for Danger Bot is to add a hand tracking input to create either a shield that the player can use for a few seconds only to be immune from the bullets or to trigger a blank bullets (but only one per player) to destroy all bullets at once! We'd like to also polish some Gfxs and balance a little the difficulty between a solo and a coop mode. <div