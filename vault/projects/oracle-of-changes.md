---
slug: "oracle-of-changes"
url: "https://devpost.com/software/oracle-of-changes"
title: "Oracle of Changes"
hackathon: "Chainlink Fall Hackathon 2021"
organization: "Chainlink"
winner: true
words: 272
team_size: 1
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/deterministic_policy"
  - "substrate/video_visual"
---

# Oracle of Changes

> I Ching reader using Verified Random Numbers provided by chain-link

[Devpost](https://devpost.com/software/oracle-of-changes) · hackathon [[Chainlink Fall Hackathon 2021]]

## Facets

**mechanism** [[deterministic_policy]]
**substrate** [[video_visual]]

**stack** chainlink, hardhat, ionic, machine-learning, python, react, solidity, typescript

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for oracle of changes

## Body

Home Screen Reading Screen Inspiration I researched creating an I Ching reader on chain in the past, but random number generation was always tricky considering how deterministic blockchain virtual machines tend to be. What it does Send the contract the Link Fee for a random number to receive an ERC1155 token containing your reading. How we built it I created all 65 images using Google's deep dream technology, adobe photoshop and the Unicode hexagram glyphs. I selected images relevant to the meaning of the change and applied deep style transfer to the base images. Challenges we ran into I didn't realize that on must swap pegged chain link for the usable form. I added some links to guide the user for this. I considered putting this contract on regular Ethereum but the gas fees are too high. I'm active on the AVAX network but could not find the LINK contract address for AVAX. Accomplishments that we're proud of It works! What we learned Even though name and symbol are not required for ERC1155 tokens etherscan will notice and visualize them. Uploading an entire metadata folder to IPFS is so much cooler than AWS. Next time I work with an ERC1155 or ERC721 token, especially for a bigger project I'd like to use graph-QL. What's next for Oracle of Changes My next focus is to work on a project with my friends called Telesto World, when that is operational, I think it would also be nice to explore a frontend for this contract from inside the Telesto metaverse program. I may consider building a tarot version, if this version gains enough interest. <div