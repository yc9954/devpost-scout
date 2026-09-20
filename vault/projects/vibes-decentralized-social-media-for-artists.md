---
slug: "vibes-decentralized-social-media-for-artists"
url: "https://devpost.com/software/vibes-decentralized-social-media-for-artists"
title: "Vibes - decentralized social media and music streaming"
hackathon: "Hack the North 2023"
organization: "Techyon"
winner: true
words: 370
team_size: 2
has_repo: true
has_live: false
has_video: false
tags:
  - "project"
  - "mechanism/realtime_stream"
---

# Vibes - decentralized social media and music streaming

> It functions how you'd expect - social media meets music streaming - but under the hood it's different! Vibes enables you to own your data and is privacy-respecting, being based on IPFS and NOSTR!

[Devpost](https://devpost.com/software/vibes-decentralized-social-media-for-artists) · hackathon [[Hack the North 2023]]

## Facets

**mechanism** [[realtime_stream]]

**stack** ipfs, nextjs, node.js, nostr, raspberry-pi, strfry-nostr, tailwindcss, typescript

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for vibes - decentralized social media for artists

## Body

Vibes homepage Album modal with comment section Raspberry Pi IPFS setup IPFS & Nostr server Inspiration We were inspired by the idea of data privacy and ownership, and believe that everyone should have a choice whether they can own their own data. We heard about these two new technologies (Nostr decentralised social media protocol and Interplanetary File System decentralised CDN), and wanted to learn more and use them together. What it does It's a social media for musicians! You can upload your songs, interact with other artists, comment and most importantly listen to music. It works... just as you expect it to work. How we built it We used a protocol called Interplanetary File System (IPFS) as a decentralised CDN. Nostr serves as the backend for managing song uploads, albums uploads, comments, likes, etc. Nostr is another protocol used to communicate social media information packets over a decentralized network. The IPFS is running off a Raspberry Pi, which acts as a "relay", or one node in a potential sea of nodes. Nostr is hosted separately on this computer which acts as another node, though could theoretically be attached to the relay as well. On top of this we built a desktop web application where you can see everything in action. Challenges we ran into learning new technologies (NOSTR, IPFS, TypeScript, and Next.js) struggled a lot with integration between all the services struggled with expanding our system to multiple nodes Accomplishments that we're proud of getting the new technologies (ipfs and nostr) to work together (we ended up coining a new term for the synthesis of both systems. We call it the "solar system"!) What we learned We learned that centralisation is not the only viable design architecture any longer. As the tech behind decentralised systems keeps growing, it becomes a real alternative to "classic" social media. It enables the individual to own their own data, while also being part of a digital community. What's next for Vibes - decentralized social media for artists We would like to see vibes to continue growing and become a valuable network in the music world, while acting as an inspiration for others to build on top of Nostr and IPFS (the solar system). <div