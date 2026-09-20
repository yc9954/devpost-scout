---
slug: "ic-map-collector"
url: "https://devpost.com/software/ic-map-collector"
title: "ICMaps"
hackathon: "Supernova "
organization: "DFINITY Foundation"
winner: true
words: 710
team_size: 1
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "domain/climate_energy"
  - "substrate/geospatial"
  - "substrate/video_visual"
---

# ICMaps

> ICMaps brings maps to the internet computer. With the ICMaps frontend you can install your own map server provided by ICMaps on Canister and integrate maps into Web3, Web2 and even desktop GIS apps.

[Devpost](https://devpost.com/software/ic-map-collector) · hackathon [[Supernova]]

## Facets

**domain** [[climate_energy]]
**substrate** [[geospatial]] [[video_visual]]

**stack** motoko, ogc, openlayers, openstreetmap, svelte, wmts

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for icmaps

## Body

ICMaps start screen Climate change visualized Useful examples show the possible uses of maps Inspiration Maps are needed everywhere, for leisure, for research and for information exchange. Large tech companies recognized the value of maps long ago and earn money with them. Many maps are available as opendata and can be used freely. It's time for maps to be truly free. Time that maps can be made available as a Web3 Dapp and offered as a scalable, decentralized map server on the Internet computer. Maps can be used to clearly visualize many facts that are important for society. That is why maps have been an important means of communication since time immemorial. It is therefore all the more important that maps can also be offered with Web3 and are thus free from censorship and privatization. In order to show that Web3 can contribute a lot to Public Good, special examples for natural hazards and climate change were set up with ICMaps. Further very useful examples will surely follow through the community. What it does With ICMaps you can create your own map servers and thus integrate map layers into Web3 Dapps, Web2 applications and even desktop GIS. ICMaps is on the one hand the software that can be installed on own canisters and enables a decentralized, scalable map server that is fully compatible with the standard WMTS. On the other hand, the ICMaps.org frontend provides a user-friendly interface to create custom map servers and load map tiles from existing maps into the blockchain. This allows maps to be created with just a few clicks. Many examples show the potential of Web3 maps. One example impressively shows the effects of climate change by directly comparing two glacier levels. How we built it The first step was to write the WMTS software. Can a canister support the WMTS specifications. For this, all WMTS requests had to be implemented. Additionally, a decentralized image storage was implemented based on the open source project Motoko-CDN. When the first Web3 map could be displayed it was clear that ICMaps will close an important gap in Internet computing. Afterwards the frontend was developed. Based on the Motoko Svelte Starter project and the open source Notus Svelte template a functional and professional frontend was developed, which allows to create map servers and to upload map data in a user friendly way. On the one hand, XYZ map layers like Open Street Map or existing WMTS map servers can be parsed and map tiles can be seeded. As a last step, examples were provided to show the potential of the maps. Challenges we ran into In order for the map server to support all requirements of the OGC standard, various Http requests had to be supported. The Mini BigMap project was integrated so that the maps can be stored in a scalable way. So as many maps can be stored as Cycles are available. The frontend had to understand existing map sources like XYZ Server or WMTS Server and had to be presented in a user-friendly interface. To keep the map data under control of the creator, the idea of the Managed Canister was invented: The user provides the canister and ICMaps makes sure that the right software is installed on it. This way the user always has the rights to the canister and the associated map data, but always has the latest software available. Accomplishments that we're proud of Implementation of a fully OGC-compliant WMTS server in Motoko Introducing the idea of managed canisters: the user retains full control over his canister, ICMaps ensures that the latest software is installed Create a professional frontend in Svelte for map server management. Impressive examples show that Web3 Maps are very important to show facts, for example to show the effect of climate change. To show that the connection of Internet Computer and professional desktop GIS systems works. Everything is open source What we learned How to build a scalable map server so that canisters can create new canisters, store images in them, and manage the cycles Interaction of Motoko, Svelte and Openlayers How to optimize the speed of queries in Motoko What's next for ICMaps Create more examples Improved error handling Further speed optimizations Integration of further data sources <div