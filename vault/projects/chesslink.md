---
slug: "chesslink"
url: "https://devpost.com/software/chesslink"
title: "ChessLink"
hackathon: "Chainlink Fall Hackathon 2021"
organization: "Chainlink"
winner: true
words: 620
team_size: 2
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/cross_origin_web"
  - "substrate/web_dom"
---

# ChessLink

> ChainkLink extention for chess streamers to mint NFTs

[Devpost](https://devpost.com/software/chesslink) · hackathon [[Chainlink Fall Hackathon 2021]]

## Facets

**mechanism** [[cross_origin_web]]
**substrate** [[web_dom]]

**stack** blockchain, chainlink, nextjs, solidity

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for chesslink

## Body

Logo Architecture Diagram Inspiration ChessLink was inspired by the team’s love and involvement in chess. The chess community has been a huge positive influence on the team members. The two team members of ChessLink actually met at their university chess club! Seeing the recent explosion of chess on twitch, the team wondered if they could provide a tool to help assist the chess expansion on twitch and landed on the idea of ChessLink. ChessLink aims to help viewers support their favorite streamers through NFTs. The team hopes that ChessLink will help the growth of chess and be a great way to give back to the chess community. What it does ChessLink allows streamers and non-streamers to mint NFTs of the critical positions of their latest played chess games. Streamers can sell their minted NFTs on the polygon blockchain to their viewers. These sold NFTs can operate as a channel for viewers to directly support their favorite streamers while also receiving a product similar to a chess position virtually autographed by their favorite streamers. This secondary channel of support has advantages over traditional twitch subscriptions by giving twitch streamers a larger cut of the donations and twitch donations by giving the viewers a tangible product from their support. Non-streamer users can utilize ChessLink to mint their own games for their personal collection to keep a cool memento of their games. How we built it We built ChessLink using the chain link and the polygon blockchain to handle NFT interactions. The front end of our app was developed using next.js, and our backend is handled by node.js. The way that our minting flow works is We have a chrome extension that can be used at any time and website to upload a data packet of chess info as a hex string to an ipfs address. Chainlink calls the ipfs address and returns the data packet as a regular string That data packet is then parsed and displayed to the user for the user to pick which positions they want to mint if any The minted NFTs are sent to the polygon blockchain The chrome extension element of ChessLink allows for users to send chess games they want minted straight from the chess website where they are playing instead of having to visit our website to search for the chess game that they want minted. Challenges we ran into The main challenge that we had when developing ChessLink was finding a good chess library for the UI. A lot of the available chess javascript libraries were incompatible with Next.js, and we constantly ran into issues with webpack because of this. Accomplishments that we're proud of We have made a fully functioning chess app that users and streamers can use to mint NFTs on a public blockchain. We are also very proud of the fact that prior to this hackathon, the team had minimal experience with UI and no experience with chrome extensions, but we managed to develop a user-friendly UI as well as a chrome extension for our app to make it easy to use for everyone. What we learned From this hackathon, we learned how to create chrome extensions, how to interact with chainlink and gained a lot of UI experience. We hope that this accumulated experience will help us in the future to develop more user-friendly apps that can utilize blockchain and its advantages nicely. What's next for ChessLink In the future, we have a few key targets that we want to focus on to make ChessLink better: continue to improve the UI to make it more streamer and user friendly implement better separation on our website between regular users and streamers gather and implement streamer feedback for our website <div