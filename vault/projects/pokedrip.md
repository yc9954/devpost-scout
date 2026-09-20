---
slug: "pokedrip"
url: "https://devpost.com/software/pokedrip"
title: "MemeDrip"
hackathon: "brainrot jia.seed hackathon ($5,772) in prizes "
organization: "audrey chen host"
winner: true
words: 247
team_size: 1
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
---

# MemeDrip

> Express yourself in style—add quotes to your outfits and make fashion your voice!

[Devpost](https://devpost.com/software/pokedrip) · hackathon [[brainrot jia.seed hackathon -5-772- in prizes]]

## Facets


**stack** flask, huggingface, python, replicate

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for memedrip

## Body

Examples See the attached Loom video to listen audio from the demo I am a Beginner Hacker Tracks I am going for: best overall yay :3 ($100 + snack boxes and random swag) most likely meme startup ($50 + snack boxes and random swag) (LAKOG) lowkey actually kind of good ($50 + a snack) my drip >;D ($100) i laughed. (new hackers prize) (10 winning teams) (10) i’m just a chill guy sponsored by Build City ($200) codedex i wanna learn stuff prize ($1041 value) UI/UX most kawaii ($100) PearAI (YC24) prize ($750) Inspiration I like to wear clothes with InsPiRaTiOnAl Quotes. Why not do it with GenAI? What it does You upload a picture -> Select the clothing piece you want to write the Quote on -> Complete the Prompt Template -> Press Generate. How we built it I used Flask to build the App and used ideogram-v2-turbo model from Replicate API for inpainting and used Hugging Face segformer_b2_clothes model for automatically segmenting the clothes and generating masks for the inpainting task. Challenges we ran into Had challenges with integrating the masks from the segformer_b2_clothes model with the Replicate API. Bad output quality. Utilized Negative prompts to increase output quality. Accomplishments that we're proud of Being able to complete the project on time. What we learned Learnt how to use Hugging Face models and Replicate API's What's next for MemeDrip I want to create my own fine-tuned Inpainting models for creating memes on the clothes. <div