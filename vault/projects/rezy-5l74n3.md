---
slug: "rezy-5l74n3"
url: "https://devpost.com/software/rezy-5l74n3"
title: "Rezy"
hackathon: "Fantom Hackathon Q1 2023"
organization: "Fantom Foundation"
winner: true
words: 585
team_size: 1
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "domain/developer_tools"
  - "substrate/web_dom"
---

# Rezy

> Rezy is a project that focuses on rewarding people for reciclying PET bottles using Fantom Blockchain

[Devpost](https://devpost.com/software/rezy-5l74n3) · hackathon [[Fantom Hackathon Q1 2023]]

## Facets

**domain** [[developer_tools]]
**substrate** [[web_dom]]
  <sub>weak: video_visual</sub>

**stack** arduino, fantom, javascript, node.js, solidity, thirdweb

## How they structured the write-up

- my inspiration was
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- technologies used
- what's next for rezy

## Body

Rezy logo Thirdweb deployed token prototype machine ready Scan this bottle using using your camera at https://unrivaled-tiramisu-65f7ad.netlify.app and claim your USDC token My inspiration was Ecuador is a country that only recycles 11% of PET bottles. We need to avoid more contamination due to plastic botles made of PET(Polyethylene terephthalate, also called PET), and I also had this idea since 2022, when I participate in a local challenge in Ecuador and I got to the finals last year :). I did not develop an app just the idea and now I have the oportunity to develop and build it. What it does Rezy rewards with 1 PET token per each PET recycled bottle, basically provides an interface for this purpose using a small machine with a LCD screen that interacts directly with the Fantom network. The person just scan the bottle and , drops it inside when the light turns green, and finally claim the PET token using fantom wallet or metamask. Afterwards if it is needed, the user can exchange PET tokens for stablecoins using swapstation website. A major detail is that recycling companies are eager to buy plastic bottles , but there is a lack of product available. It can also track the origin and the end of each PET bottle registered on the Fantom Testnet network. Companies funds the Swapping contract that also acts like a Treasury in order to have enough balance to exchange PET for fUSD , or any other possible stable coin on Fantom. How we built it I built this using a cardboard box , an old bus validator (android and QR) , an arduino esp32 board ,some leds on the harware side. On the software side I used thirdweb for smart contracts ERC20 (PET and fUSD) and solidity for swaping contract. I also built a frontend and a backend that interacts with a remote LAMP for Arduino control ( led on, and of) , and a backend and middleware for interacting with Thirdweb SDK and finally of course fantom network ( testnet). Last but not least a forked fantom wallet for receiving the tokens and a swaping website for exchanging PET Tokens for fUSD tokens. All the repositories are based on open projects and some are developed from scratch Challenges we ran into Some smart contracts were a little bit tricky to make them to work QR code libraries for the frontend To design the box for fitting all the elements that integrates the demo device The new Thirdweb SDK makes me spend some time looking for the new methods Sinchronizing the arduino with the rest of the development was a hard thing To build a simple but efective web interface on the machine side. Accomplishments that we're proud of This idea was awarded with finalist in enviromental challenges in Guayaquil -Ecuador under the name of reciclachain ( I am the author). I built a basic prototipe that could be used in the real world Technologies Used Thirdweb(Smart contracts and minting api) Arduino(Led control ) Solidity(Smart contracts on Fantom) Metamask(Wallet) Render(Servers) Gitpod (development) What's next for Rezy The next step is to get investment in order to build a better MVP and , develop a flutter wallet for easier interaction and deliver this device in local communities for a increasing the recycling process in the neighborhoods. Another milestone would be to design a business model to make it sustainable and generate enviromental campaings for people. This project could also recicle Aluminum cans and other reciclable materials. <div