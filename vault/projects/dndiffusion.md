---
slug: "dndiffusion"
url: "https://devpost.com/software/dndiffusion"
title: "D&D Diffusion"
hackathon: "Chainlink Fall 2022 Hackathon"
organization: "Chainlink Labs"
winner: true
words: 734
team_size: 3
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "substrate/document_pdf"
  - "substrate/geospatial"
  - "substrate/video_visual"
---

# D&D Diffusion

> Jump into the game faster, with an AI generated hero image from your character sheet. Simply upload a character sheet .pdf, and our Stable Diffusion instance will do the rest! Want NFT? No problem!

[Devpost](https://devpost.com/software/dndiffusion) · hackathon [[Chainlink Fall 2022 Hackathon]]

## Facets

  <sub>weak: legal_professional</sub>
**substrate** [[document_pdf]] [[geospatial]] [[video_visual]]

**stack** chainlink, ipfs, next-js, nft.storage, scaffold-eth, stable-diffusion

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for dndiffusion

## Body

Be random. Save time. Look cool. Get playing. Link to our detailed document with images for judges Everything you need right here to qualify our project: Live demo of our Flask Scraper where you can upload your own character sheet and try it out. Sponsor technology proof of using it nice Our D&D Diffusion avatars may not be perfect, but like our hackathon project, they are a great way to springboard creativity and play faster. Given sufficient development time and AI training our platform will allow for incredible, inscrutable, stylistically interesting visual results based on a range of character inputs. For the demo we have created something that makes great results for a wide array of uploadable PDF character sheets, but we can aim for far greater success at creating random, unique and interesting visualizations for new characters and new players. Inspiration Every year, millions of people joining a new campaign of D&D make a character sheet and then begin the inevitable search through duck duck and google for an image to go with it. Instead of scrolling through dozens of drawings by artists, use DnDiffusion for a unique avatar image generated from your character sheet! Start playing faster with DnDiffusion, for all the D&D Degens. What it does After uploading the character sheet from FastCharacter.com , DnDiffusion will take in a created character and pump out a sick ai avatar. There will be 4 images for you to choose from, you can pick out your favorite one and enjoy playing D&D with your folks without a fuss searching for a perfect avatar. How we built it Getting the user-uploaded character sheet PDF and extracting its text Using NLP techniques to form a good prompt for the text-to-image AI model input Sending this generated text to the Stable Diffusion AI model Using the Stable-diffusion-webui from automatic111 AI model generates 4 images, these images are rendered to the user on the front end Challenges we ran into Faces and hands Training the specific “races” Thinking about diversity and inclusion (roadmapped!) Some of the team members had never worked with the Stable Diffusion-advanced model before resulted in requiring some time to get familiar with it Cloud GPU - Creating a cloud GPU and experimenting with different prompts/models Difficulty in connecting the shared cloud Connecting to a stable diffusion endpoint that the app can use Figuring out the most cost and time-effective way with RunPod and our workflow Doing GET/POST requests in Flask Accomplishments that we're proud of We've got to learn something new! - the AI, the Stable Diffusion, and how to make it aligns with what we want to build. Definitely a challenge with the time limit but we've made it through. What we learned How to Use DreamBooth to Fine-Tune Stable Diffusion (we used this to train Dragonborn, and Artificer, and Cleric.) Building REST APIs using Flask Testing APIs Using Postman Get a Random Number Training the AI to generate 2500 manually labelled images! What's next for DnDiffusion Our team aims to make DnDiffusion an application DnD players would enjoy using - no matter whether they are first-time or advanced players! By creating the artistic ai avatar, we believe this will make DnD sessions more enjoyable for them without having to spend some time browsing through the internet. We also would love to use this app to get people together, whether it’s a game night at home, an online gaming session, or even a team building! Here are the visions for the future of DnDiffusion from our team members: Somya’s: “Even I have decided to complete the project end to end after the exams because I want that people actually use it to play DnD” Tippi’s : “Expand the feature set to include my experiments with map generation, and thematic overlays, and figure out a way to pay for all that Cloud GPU server uptime, and use D&D Diffusion for teambuilding in the upcoming metaHackathon(0)!” Aire’s : “I would love this to be another regular step we need to do before the first DnD session, people create a character sheet and then come generating their avatars with DnDiffusion” Earl’s: “I want to implement a plug-in and expand the scope to include all kinds of documents that we create AI images of to save time and inspire fun” Mark’s: “I look forward to a career at Protocol Labs and opportunities to practice my teamwork.” <div