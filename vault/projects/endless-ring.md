---
slug: "endless-ring"
url: "https://devpost.com/software/endless-ring"
title: "Endless Ring"
hackathon: "Polygon BUIDL IT : Summer 2022"
organization: "Polygon"
winner: true
words: 519
team_size: 1
has_repo: false
has_live: false
has_video: true
tags:
  - "project"
  - "substrate/web_dom"
---

# Endless Ring

> A physical piece of jewellery that stores a voice message. An NFC-enabled ring that links to an IPFS-hosted NFT audio file and graphic on minted Polygon. Minting is webapp-based.

[Devpost](https://devpost.com/software/endless-ring) · hackathon [[Polygon BUIDL IT - Summer 2022]]

## Facets

  <sub>weak: realtime_stream, retrieval_grounding</sub>
  <sub>weak: finance_payments</sub>
**substrate** [[web_dom]]
  <sub>weak: financial_record</sub>

**stack** alipinejs, flask, github, heroku, ipfs, metamask, nft, polygon, python, tailwind, three.js, vantajs

## Body

Inspiration This inspiration was the idea of future-proof storage and the tamper-free nature of the blockchain. Although these are very technical terms, the ideas of eternity and immutability have been with us since the dawn of civilisation. These are also key concepts of love, whether it's affectionate, familiar, brotherly, or romantic love. To express it to family, a friend, or a romantic partner in an eternal and immutable way seems very valuable. There where three nudges for us. 1) Hugo having gifted his (non-imaginary) gf a QR code with an IPFS-stored message. 2) A common fraud and extortion technique of changing the underlying URL of an NFT or QR code. Many QR code generator sites wait for you to start using the QR code and then ask for very high sums to keep hosting the URL (e.g. once you've already printed your posters or gear), threating you to show ads otherwise. Dirty. 3) IPFS being absolutely interplanetarily and eternally awesome. What it does This web app connects to your wallet, lets you record your voice, and mint that voice as an NFT rendition of your voice wave on IPFS. The physical ring is an NFC-enabled ring, which will point to the IPFS. You don't need to charge it. You don't need any special app. Simply get your phone close to the ring and it will play your message. Oh, the web app also shows you some cool 3d floating rings and fog. I know it's hard to miss, but just wanted to mention that again （￣︶￣）↗ How we built it Website For the frontend, we used flask, tailwind, vanilla js, threejs, vantajs, On the backend, we used: web3.js, eth-brownie to interact with blockchain numpy, matploblib and pydub to manipulate the voice data flask, gunicorn, werkzeug to run server-side stuff Physical ring We contacted 8 different suppliers and chose the best looking desings, which are being prototyped right now. Unfortunately, due to the difficulty of soldering around copper wire, there have been delays, but the first prototypes work. We made them work by embedding them in an temperature-absorant plastic inlay, which then gets coated with ceramic. The ring is compatible with all modern smartphones. It can be easily programmed. It has about 100k cycles. It is based on ISO 14443A, 13.56MHz NDEF. Challenges we ran into Largest challenge: Hardware getting the physical ring to work with soldering. Any kind of jewellery making process in proximity to copper wire will break the wire. Very hard to get the shape right, so for prototype we skipped that part. Smart contract & IPFS: integrating IPFS storage with recording a voice message on the site and also minting an NFT, all in real time. Time management! What we learned Hugo has learnt how to easily integrate IPFS Hugo has learnt how to integrate crypto transactions on frontend with metamask and web3.js Konrad has learnt ThreeJS and a lot of frontend stuff. Konrad has learnt a lot about NFC technology and jewellery manufacturing What's next for Endless.place Finalizing ring design & launching! Also, expanding our tech-jewelry lineup to include pendants, bracelets and other stuff. <div