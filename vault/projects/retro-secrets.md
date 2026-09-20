---
slug: "retro-secrets"
url: "https://devpost.com/software/retro-secrets"
title: "retro secrets"
hackathon: "ConUHacks X"
organization: "HackConcordia"
winner: true
words: 419
team_size: 4
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/privacy_tech"
  - "substrate/document_pdf"
  - "substrate/financial_record"
  - "substrate/sensor_telemetry"
  - "substrate/video_visual"
---

# retro secrets

> social steganography platform which uses ai-generated ascii art to hide encrypted secret messages in plain sight stored on the solana blockchain

[Devpost](https://devpost.com/software/retro-secrets) · hackathon [[ConUHacks X]]

## Facets

**mechanism** [[privacy_tech]]
**substrate** [[document_pdf]] [[financial_record]] [[sensor_telemetry]] [[video_visual]]

**stack** aes-encryption, gemini, mongodb, next.js, solana, typescript

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for retro secrets

## Body

w ascii mountain generate ascii page social matches re-hash of ASCII to original hash to determine authenticity phantom wallet solana verification bye :) Inspiration ascii art is quite fascinating and nfts could be cooler so we decided to hide messages in plain sight using stenography with custom encryption and build a social platform What it does you get to create ANY ai-generated ascii art which you can then hide a secret message in for your friends and followers gemini produces an artwork from the user's prompt and our prompt augmentation to produce a consistent fun aesthetic theme and an ascii-conversion optimized image art is stored on the solana blockchain for verifiability of creation and release times and proof of ownership the hidden message gets put into the colours of the ascii characters using LSB encoding and our custom AES encryption for symmetric message hiding and revealing the nft art can serve a variety of purposes whether it be a GTA 6 game teaser or a postcard to your friend social platform lets you doomscroll creations from friends and public accounts where you can interact with comments and get recommended art based on your interests from our clustering algorithm the countdown timer adds suspense before the secret is shown and users can subscribe to interesting countdowns and return when they are unlocked secure message transfer through nfts allows for true visible end to end encryption between friends How we built it frontend: next.js, ts, tailwind css, backend: fastapi (python), mongodb image generation: gemini 2.5 flash image, ascii-magic message hiding: AES encryption, LSB (least significant bit) encoding web3 integration: solana and the blockchain Challenges we ran into finding a method to generate ascii art, setting up the google ai studio, setting up the solana block chain coming up with an encryption formula that preserves the image and hides messages in plain sight Accomplishments that we're proud of successfully completed the platform with verifiable block chain transaction What we learned integration is hard but rewarding What's next for retro secrets after building this tech, we realized that beyond our social platform, there are many applications for our hidden in plain sight time activated message hiding. examples: a scavenger hunt or escape room could leave up prepared hints for lost players that get released at preset times. Rock Star could release GTA 6 teasers with hidden messages dangling right in front of fans, which they can only see next year. document memories, send postcards, create unchangeable new years resolutions for accountability Cheers! <div