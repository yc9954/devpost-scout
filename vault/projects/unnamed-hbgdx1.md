---
slug: "unnamed-hbgdx1"
url: "https://devpost.com/software/unnamed-hbgdx1"
title: "NymDrive"
hackathon: "Cosmos HackAtom VI "
organization: "Cosmos"
winner: true
words: 200
team_size: 1
has_repo: true
has_live: false
has_video: false
tags:
  - "project"
  - "mechanism/on_device_local"
---

# NymDrive

> An open-source, decentralized, E2E encrypted, privacy friendly alternative to Google Drive/Dropbox.

[Devpost](https://devpost.com/software/unnamed-hbgdx1) · hackathon [[Cosmos HackAtom VI]]

## Facets

**mechanism** [[on_device_local]]
  <sub>weak: realtime_stream</sub>

**stack** electron, node.js, nym, react, websockets

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what's next for nymdrive

## Body

NymDrive Mac Mac tray bar NymDrive Ubuntu NymDrive Windows Inspiration IPFS is an amazing technology but it is ideally meant for public data. In order to use IPFS for personal data we need to address encryption and privacy on the network layer. Encrypting files locally and using NYM mixnet to upload files to IPFS gives a certain amount of anonymity to end users. What it does Allow users to upload/store their files in a secure and decentralized manner. How we built it Client - An Electron app which can be built in to Mac, Linux and Windows. The UI part is done in React using the Photon UI Kit. Service Provider - Using NodeJs Challenges we ran into I had challenges in running the nym web-sockets client. Had to run multiple time to get it started, and sometimes stops working after few minutes. Accomplishments that we're proud of Multi-device sync Native File Manager look and feel. Make use privacy friendly Nym mixnet. Implement encrypted file storage in IPFS. File sharing between NymDrive users. What's next for NymDrive Use nym web-assembly client for UI when its ready Option for publishing Public un-encrypted files to nym blockchain UI to match Windows/Linux <div