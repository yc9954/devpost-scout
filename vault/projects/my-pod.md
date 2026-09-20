---
slug: "my-pod"
url: "https://devpost.com/software/my-pod"
title: "My Pod (mypodapp.com)"
hackathon: "Alexa Skills Challenge: Life Hacks"
organization: "Amazon"
winner: true
words: 645
team_size: 1
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/on_device_local"
  - "domain/accessibility"
  - "domain/immigration_refugee"
  - "substrate/web_dom"
---

# My Pod (mypodapp.com)

> Play any podcast, audio links, RSS and Google Drive links and read any web page through your Amazon Echo.

[Devpost](https://devpost.com/software/my-pod) · hackathon [[Alexa Skills Challenge- Life Hacks]]

## Facets

**mechanism** [[on_device_local]]
**domain** [[accessibility]] [[immigration_refugee]]
**substrate** [[web_dom]]

**stack** amazon-ec2, amazon-web-services, c#, lambda, razor

## How they structured the write-up

- inspiration
- what it does
- how i built it
- challenges i ran into
- accomplishments that i'm proud of
- what i learned
- what's next for my pod

## Body

mypodapp.com homepage Podcast search. Add link form. Link details with web audio player. My Pod skill in the Alexa store. Inspiration I was inspired to develop this skill as I wanted to be able to listen to a subscription only podcast through my Amazon Echo. Although there were skills for individual podcasts and some that played most podcasts. The ability to play custom feeds and/or links did not exist. What it does Once the skill is enabled and your account is linked on your Amazon device, you simply log-in to https://mypodapp.com . You can then create a playlist and start adding links. Call your link something and hit save. You can then immediately ask Alexa to play that link through the skill. You can link to individual audio links, podcast RSS / Atom feeds, textual RSS feeds and text based websites (My Pod will extract the text and get Alexa to read it out to you). The most popular podcasts are available via a search facility, making adding podcasts really quick. How I built it I built everything in c# .Net Core. The skill logic is hosted on AWS Lambda and the main website is hosted on Amazon EC2. Challenges I ran into Nuances and slight differences with links, audio formats and RSS feeds. Having a support channel for users really helped in the early days in order to bottom out the issues. Accomplishments that I'm proud of I'm most proud of some of the feedback I have received from my users around the world which has made a real difference is some cases to their quality of life: _"Can I just say thanks for this app - can I explain why. I am in Sussex, England, my Dad is in Swansea, Wales, 250 miles away from me. He is 89 years old and now nearly blind. When he was 80 I convinced him to get an iPad and he loved it - he still had enough sight at that time. In recent years he sight failed and then I discovered the Echo and bought him 2. By setting up his echos through my Amazon account I can manage most things remotely for him when needed. The one thing he really wanted was to be able to play the Sunday sermons from his Church as he can’t get out any more through other health reasons as well (stroke). I tried to get the church to upload their services to Tunedin but that proved a bit much for them even though they publish the podcasts on their web every week. And then I discovered My Pod - it is just fantastic within a few minutes I had loaded a whole sermon series for him from Sussex and he could use it even with his limited sight and speech (stroke). I have not stopped there now loading other podcasts for him (rugby and soccer). I have even tried loading a link from my Google drive and it worked perfectly. I love this app - I have rated it of course through the feedback but I just wanted to say well done for this little gem - this is making a real difference to the quality of life of my dad. Many many thanks"_ _"As I would use this skill for digitalised audio books of my seven year old son, I would like to have 20 playlists... if possible... You would make a german boy very happy. My son is really happy with this Skill!!!"_ What I learned Getting a support channel for your users is the most important thing. People always use things in ways you didn't envisage so giving them a way to feed that back to you is paramount. What's next for My Pod More refinements and functionality. I have a stack of feedback requests and suggestions in my backlog to work through :) <div