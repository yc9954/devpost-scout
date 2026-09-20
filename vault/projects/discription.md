---
slug: "discription"
url: "https://devpost.com/software/discription"
title: "Discription"
hackathon: "Hack the Northeast: Beyond"
winner: true
words: 451
team_size: 1
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/vision_ocr"
  - "mechanism/voice_speech"
  - "substrate/video_visual"
  - "substrate/web_dom"
---

# Discription

> "Making memes inclusive." This is a bot for the popular text and voice messaging program Discord, which uses Azure's Cognitive Services to provide descriptions for memes and images.

[Devpost](https://devpost.com/software/discription) · hackathon [[Hack the Northeast- Beyond]]

## Facets

**mechanism** [[vision_ocr]] [[voice_speech]]
**substrate** [[video_visual]] [[web_dom]]

**stack** azure, computer-vision, discordjs, node.js, npm, visual-studio

## How they structured the write-up

- inspiration
- what it does
- how i built it
- challenges i ran into
- accomplishments that i'm proud of
- what i learned
- what's next for discription

## Body

The async function that uses the computerVisionClient to get the description and text. It can even recognize faces! Discription describing the original meme. Notice how it even picks up the imgflip watermark! Inspiration My inspiration came from a voice chat in Discord I had with a few of my friends. After I sent in a meme (a horribly unfunny one -- it's this project's thumbnail), I was told by a friend with slow internet that it wasn't loading for them. This got my wheels turning, and I realized that, even though Discord _has_ a text-to-speech function, it doesn't really have that for images. For the visually impaired, or even for those with just slow internet, the only way to know about a meme is to have another user either join a voice channel, or have another user describe it with a TTS message. This works, yes, but laziness is the mother of invention, and some times we'd rather have a robot do something for us. That's what Discription is. What it does Discription is a bot for Discord that provides captions for images and memes in text-to-speech messages. How I built it Discription is built in one of my favorite languages, JavaScript, using my favorite framework for that language, Node.js. My reason for using Node.js, besides personal preference, is because I already had some experience writing Discord bots in it, and Discord has a great module already ready to go for it. This is what allows the bot to function on Discord, but in order to do its job and actually caption the images, it uses Azure's Cognitive Services -- Microsoft's very own artificial intelligence. The bot waits for a message, and, if it includes and attached image, it sends the image URL to Azure's endpoint. Azure then returns back a description, and text from the image (if any is found.) It was built in Visual Studio, and tested with Git Bash and my private Discord channel. Challenges I ran into My biggest challenge was definitely learning how the Cognitive Services worked, but with a few hours with the documentation, I was able to overcome it. Accomplishments that I'm proud of I'm very proud to have some understanding of the Cognitive Services, but I'm especially proud of getting the bot to read text in an image. What I learned How Azure's "Computer Vision" works under the hood, and more about machine learning in general. What's next for Discription In the future, I'd like to buy hosting for the bot and actually have it publicly available. I'm hoping to eventually have it be able to create more detailed descriptions, and maybe even join a voice channel and give descriptions there, too. <div