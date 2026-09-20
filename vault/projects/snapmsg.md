---
slug: "snapmsg"
url: "https://devpost.com/software/snapmsg"
title: "SnapMsg"
hackathon: "EthCC Hack 2022"
organization: "EthCC"
winner: true
words: 317
team_size: 1
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
---

# SnapMsg

> MetaMask messenger with MetaMask snaps encrypted with Privy

[Devpost](https://devpost.com/software/snapmsg) · hackathon [[EthCC Hack 2022]]

## Facets


**stack** metamask, next.js, privy, react, typescript

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for snapmsg

## Body

GIF Using SnapMsg as a notes to self app GIF Using SnapMsg to message another person PoC for SnapMsg directly in MetaMask (in the future???) Inspiration We wanted to build a MetaMask snap, and looked at all the sponsors to see what technologies looked cool to use with it. Being aware of the contacts feature in MetaMask, we thought that messaging would work well with that feature and that a messaging application within MetaMask would be cool. What it does A MetaMask Snap that uses Privy to message others via their wallet address. Currently, we can't find MetaMask's contact list easily nor edit the UI of MetaMask itself, but we thought using Snap to create a messaging service would be cool. With a PoC, we thought that a messaging service directly implemented in MetaMask would be cool and because of the extensibility of Snaps, it would be possible to message people across other blockchains as well. How we built it Using MetaMask Flask, we built the barebones for the Snap We used Privy to encrypt and save data, and to be able to retrieve it later on We used React and TypeScript to build the frontend Challenges we ran into How to use schema our data for the messages to use in Privy Privy schema only accepts strings No dynamic field creation Setting up MetaMask Flask (lot of errors/problems trying to start it up) Determining what features to build and what to leave for "What's next" Accomplishments that we're proud of Decent looking frontend Used Privy to create a messaging service between two wallets What we learned How to build MetaMask snaps How to use Privy for encrypting messages and saving data What's next for SnapMsg Add group chat features Add profile pictures Add/remove friends Block wallet addresses Different types of messages to send (files, pictures, videos, audios) Depending on future Snap features, a whole lot!!! <div