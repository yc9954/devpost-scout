---
slug: "diffuji"
url: "https://devpost.com/software/diffuji"
title: "diffuji"
hackathon: "TreeHacks 2026"
organization: "TreeHacks"
winner: true
words: 750
team_size: 4
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/on_device_local"
  - "domain/transportation"
  - "substrate/financial_record"
  - "substrate/regulation_legal_text"
  - "substrate/video_visual"
---

# diffuji

> a diffusion-powered instant camera

[Devpost](https://devpost.com/software/diffuji) · hackathon [[TreeHacks 2026]]

## Facets

**mechanism** [[on_device_local]]
**domain** [[transportation]]
**substrate** [[financial_record]] [[regulation_legal_text]] [[video_visual]]

**stack** python, raspberry-pi

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for diffuji

## Body

GIF Project site Actual device Infinite reels Many stickers Muscle mode Taking photos Raw image, image after diffusion, printed 1900s image Components laid flat Inspiration The world needs a bit more silliness. Instant cams are fun, and there’s something special about memorializing a moment through physical media. But what if these moments were … part dream, part hallucination of reality? Introducing Diffuji - a diffusion-powered instant camera that turns half-real, half-dreamed moments into physical prints. What it does You can take a picture and choose from a range of filters to apply to your image. However, these filters aren’t your typical color grades, but can completely reimagine the context the photo was taken in - whether turning back time to the 19th century, having the best six-pack you’ve never had, or simply becoming a duck. These filters process the captured image using image-to-image diffusion models, granting us creativity to transform the image however we wish. The picture is subsequently printed using a thermal printer onto receipt paper / stickers, which allows for inkless printing. Additionally, a teammate’s experience working at a thrift store led to another feature: the ability to take a pic of an object and use perplexity to quickly search the internet for competitive prices for it, and print a reference-backed price for it. How we built it Hardware Parts Raspberry pi 2w for its low power draw, wifi capabilities, decent memory (512mb), and low cost ($15). Also with a arducam Cheap TTL Aliexpress thermal printer along with sticker thermal paper Rotary encoder for switching modes, push button for our shutter, and tactile switch for our power switch I2C OLED display for display our modes and settings 2 18650 batteries and a 3amp 5v UPS supply, enabling good battery life and regulation. We also add a 1000uF capacity to guard against current spikes from the printer. We designed a shell in fusion 360 and printed it out at the treehacks makerspace. We soldered our components together and hotglued and screwed them into our shell. Software On device We have a python script that manages inputs, displays animations and state on the screen, and prints pictures. We experimented with lots of dithering algorithms to convert images into a bitmap that looks aesthetic on the sticker. We settled on ordered bayer dithering with custom gamma / contrast adjustments. The script either processes the images on device or sends them to the cloud depending on the mode. Cloud We developed our own public API server for the camera that is hosted on Railway. This is the interface for how the camera learns what modes it has access to, server that processes images and applies diffusion to them using various APIs for the different modes, along with custom prompting to ensure alignment with the mode. The client can select which type of model and API to use for the image generation. It has access to the following: Gemini / Google Cloud We used Gemini 2.5 Flash Image as our primary provider, powering most of our filters, from reimagining scenes to be in 1846 to turning everyone into ducks or giving everyone huge muscles. OpenAI We used gpt-image-1.5 via the Images Edit API for our Studio Ghibli filter, which we found produced more faithful style transfers for this style. We also used it for our Sam mode, which merges a Sam Altman into a scene, as it was the best at composing people naturally. Modal We hosted Black Forest Labs' FLUX.1-Kontext-dev on an H100 GPU through Modal's serverless infra, giving us our own diffusion pipeline with 20-step inference at bfloat16 precision using an open-sourced model. Challenges we ran into We had jamming issues where the paper would bunch up. We found that by peeling back some of the sticker, it helped We had issues prompting the model to consistently apply a style. It turns out when you give a diffusion model the image upside down they suck - must be too out of distribution. On device diffusion takes forever when you only have 512MB ram. Accomplishments that we're proud of We made a very sleek and functional product, which was so fun to play with. We hope everyone at the hackathon enjoyed getting custom sticker prints! What we learned We learned about inference platforms for extremely low ram system Prompt engineering lol Dithering / good image processing thermal printers are cool Design Glue is permanent What's next for diffuji Continuing to make progress on performance for on-device diffusion. Mass produce?? more modes <div