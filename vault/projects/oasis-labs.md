---
slug: "oasis-labs"
url: "https://devpost.com/software/oasis-labs"
title: "Oasis Labs"
hackathon: "Chainlink Fall 2022 Hackathon"
organization: "Chainlink Labs"
winner: true
words: 343
team_size: 1
has_repo: false
has_live: false
has_video: false
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "substrate/geospatial"
  - "substrate/video_visual"
---

# Oasis Labs

> Oasis is an open augmented reality cloud that maps the physical world as a living canvas - letting anyone anchor persistent digital content to real places, visible to anyone who walks by.

[Devpost](https://devpost.com/software/oasis-labs) · hackathon [[Chainlink Fall 2022 Hackathon]]

## Facets

**mechanism** [[realtime_stream]]
**substrate** [[geospatial]] [[video_visual]]

**stack** google-ar-core

## How they structured the write-up

- inspiration
- what it does
- how i built it
- challenges
- what's next for neopolis

## Body

Inspiration As smart glasses and spatial computing devices move toward mass adoption, we saw a fundamental problem: every AR app creates its own isolated reality. We wanted to build the open infrastructure layer - the equivalent of the World Wide Web for augmented space - where anyone can contribute content and anyone nearby can experience it, regardless of device or platform. What it does Oasis is an open AR cloud that lets creators anchor persistent digital content - 3D objects, images, audio, and interactive experiences - to specific real-world GPS coordinates. When users point their devices at those locations, the content appears spatially locked to the environment and visible to everyone nearby. The network has two modes: open public spaces where anyone can add content, and registered spaces where creators maintain curated persistent experiences. How I built it The core scene anchoring and real-world geometry detection runs on Google ARCore, using its Cloud Anchors API to create persistent, multi-user spatial anchors that survive across sessions and devices. Content is stored and retrieved via IPFS (Protocol Labs), making the content layer decentralized and censorship-resistant - no single server controls what exists in a given space. We built a lightweight edge AR cloud middleware layer that resolves spatial queries by GPS bounding box, fetches the relevant IPFS content hashes, and passes them to the ARCore rendering pipeline. This gives users sub-second load times for nearby content without centralized infrastructure. Challenges The hardest problem was spatial persistence - making sure a 3D object anchored by one user appears in exactly the right position for another user on a different device, days later. ARCore Cloud Anchors partially solves this, but we had to build a reconciliation layer to handle GPS drift and anchor degradation over time. What's next for Neopolis Launch the AR Commons - a governance-owned shared spatial layer for cities. Expand beyond ARCore to support Apple Vision Pro and WebXR. Develop no-code creator tools so anyone can anchor content without writing code. Partner with hardware manufacturers to ship Oasis as a default spatial browser. <div