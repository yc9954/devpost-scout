---
slug: "story-world"
url: "https://devpost.com/software/story-world"
title: "Story World"
hackathon: "Amazon Alexa Skills Challenge: Multimodal"
organization: "Amazon"
winner: true
words: 740
team_size: 1
has_repo: false
has_live: false
has_video: true
tags:
  - "project"
  - "substrate/video_visual"
---

# Story World

> You choose the story. You choose the character names. You end up with your own little Story World.

[Devpost](https://devpost.com/software/story-world) · hackathon [[Amazon Alexa Skills Challenge- Multimodal]]

## Facets

**substrate** [[video_visual]]

**stack** alexa, amazon-dynamodb, amazon-web-services, apl, node.js

## How they structured the write-up

- inspiration
- what it does
- how i built it
- challenges i ran into
- accomplishments that i'm proud of
- what's next for story world
- improvements
- thank you

## Body

story world logo 1 example characters spaceman story example characters robot story end of story select screen reading the story story world logo 2 story world logo 3 story world logo 4 Inspiration I have built a few skills and learnt that Alexa is a particularly good story teller. Children are particularly engaged with Alexa. When I was younger I particularly enjoyed the Mr Men short stories and when APL came out I thought fun illustrations and Alexa telling the story could be a good idea. What it does My thinking is that you should be able to ask Alexa for any type of story from a Princess Story to a Detective Story and get a short story back from Alexa (told by Alexa). Even better with Alexa it is easy to have dynamic stories. You can give the main character in the story your own name. So the detective in the story is now called Hugo (my name) or bob (random name I could choose). APL was another great addition to Alexa and means that you can add illustrations to the stories. Karaoke style reading for the story and auto page as the story is told. How I built it A solid few days looking at the APL docs. Followed by a solid few days working on the project. Content creation was the main time killer. I only started building in January, so deadline has come round very quickly. AWS, Lambda, node.js, APL, dynamoDB (x3) Challenges I ran into Sound effects don't work in karaoke mode (think it is a bug and will be fixed at some point) You can only have 5 sound effects in a story. Quality of sound you can use with alexa is quite low. APL documentation is pretty new and still being improved. Size of stories had to be short due to the the max size of information that can be sent. Alexa in the UK says things quite differently to Alexa in the US. Had to test speech cons for both languages and some sound great in the uk and really bad in the US (and other way round). I need more content and I didn't have enough time to do all I wanted for this comp. But at least I can still keep adding content. Accomplishments that I'm proud of On the fire TV it looks like a pretty cool selection screen and its nice to be able to select a story with the remote. On Echo Show the touch elements work nicely. For the home screen It would have been easier to just copy the Alexa demo skills which have one sequence, but my original sketches has three and I decided to stick to the challenge. The skill is well organised with each handler having its own file. This should make it easier to manage as the project grows and if I need to expand with more team members they should be able to pick up my code pretty quickly. I added a cool little animation effect (GIF) on the screen when the story is over. Its a cool work around as you currently can't use a gif. It uses a pager quickly changing between two images to create the gif effect. What's next for Story World Loads more stories! I am also planning a couple of meetings with publishers of children's books. I think adding ISP (in skill purchasing) and giving the user the ability to buy slightly longer stories from Alexa would be really cool and could be a killer skill for Alexa. Maybe even a subscription model. Imagine if you could have Alexa read Mr men stories!! Now that would be cool !! Improvements I spent more time on the character selection images than the theme selection images. I would like to bring them up to the same quality and same style of design. Book covers to select the story (I did not have enough time to get these done) Another row to show your favourite stories (if you have any) on the home screen. Plan was to make animations relevant to the story that was just told, but time meant I just went for a cute one the children liked. Thank you Thanks for reading all the way to the bottom. I hope using the skill will be a lot more exciting than reading all that waffle. Happy to get any feedback on the skill. @hugocatchpole <div