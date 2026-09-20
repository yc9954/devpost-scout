---
slug: "d3-music"
url: "https://devpost.com/software/d3-music"
title: "D3 Music"
hackathon: "NEAR MetaBUILD III Hackathon"
organization: "NEAR Protocol"
winner: true
words: 458
team_size: 2
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/cross_origin_web"
  - "mechanism/realtime_stream"
---

# D3 Music

> Next-Generation Music Platform Built For Musician to share Music and earn Near in Fully Decentralized Platform

[Devpost](https://devpost.com/software/d3-music) · hackathon [[NEAR MetaBUILD III Hackathon]]

## Facets

**mechanism** [[cross_origin_web]] [[realtime_stream]]

**stack** next, react, rust

## How they structured the write-up

- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what's next for d3 music

## Body

Home Page Music Playlist Account Info Mint song Next Generation Web-3 streaming platform D3 Music is a brand-new streaming platform built for all musicians, not just those signed to labels. Build a fanbase, share your works in progress, and then publish your completed tracks for all the world to hear. Create, grow, and monetize, all without the need to graduate off the platform or sign a record deal. What it does D3 Music is a fully decentralized platform for music (like Spotify) where people can listen or post music and artists can earn NEAR from their listeners. There are 2 main problems that we try to address with this project: 1) Artists should have ownership of their music and be able to freely trade their ownership of their music. 2) Listeners should be able to listen to high-quality music and be able to directly support their favorite artists. How does our application solve these problems? Artists can upload their music as an NFT which gives them ownership of their music which then can be freely traded on any NFT marketplace. They can also attach royalties to their music so that when ownership of the song is traded between owners, they get a portion of the revenue. The music is also uploaded as lossless .wav files thanks to IPFS and Filecoin providing a safe and easy way to store large files. This allows listeners to have access to the original audio that the artist intended for them to hear. The platform also supports tipping your favorite artists with NEAR tokens, so listeners support their favorite artists directly. How we built it There are two parts to the applications. The frontend was built using NextJS to support a faster and easier development workflow. The backend was obviously built using NEAR protocol and I did not require any 3rd party backend. For the front-end, I used next-js-api to make RPC calls from my application. Challenges we ran into The biggest technical challenge of the project was creating the custom player component from scratch. It implements the logic that allows you to play, queue, skip, and shuffle songs from the dashboard Accomplishments that we're proud of having deployed a live application on the testnet within the span of just over 1 month! What's next for D3 Music Recreate the front-end in Svelte Kit while working out bugs and modifying the UI making it more compatible and responsive for all kinds of devices. Add new features to the smart contract for tracking song plays/interactions to better display songs on the main page of the application. Update the front-end to allow querying pages for individual artists/songs. Create a marketplace contract where users can buy/sell and trade their music. Deploy everything to the mainnet! <div