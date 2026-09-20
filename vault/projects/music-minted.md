---
slug: "music-minted"
url: "https://devpost.com/software/music-minted"
title: "Music Minted"
hackathon: "Chainlink Spring 2023 Hackathon"
organization: "Chainlink Labs"
winner: true
words: 382
team_size: 1
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
---

# Music Minted

> An application for minting music NFTs.

[Devpost](https://devpost.com/software/music-minted) · hackathon [[Chainlink Spring 2023 Hackathon]]

## Facets

**mechanism** [[realtime_stream]]

**stack** hardhat, javascript, next.js, solidity, yarn

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for music minted

## Body

Application front page NFT creation form Successful mint notification Inspiration The music industry has long been plagued by issues around artist remuneration and the exploitation of intellectual property rights. Observing the potential of Web3 technologies, like NFTs, to revolutionize ownership and value transfer, we were inspired to create a bridge that connects musicians directly to their fans - Music Minted. What it does Music Minted enables musicians to mint their music into NFTs, with every critical detail - audio, cover art, track info - stored securely on the blockchain. Using Chainlink price feeds, we ensure a cost-effective and transparent minting process. Musicians can now take control of their art, gaining more direct earnings and fostering a closer relationship with fans. How we built it The application leverages AWS S3 for storing audio files and cover art, and Chainlink for providing reliable, real-time price feeds. The minting process begins with the audio and cover art upload to AWS S3. We then generate a metadata JSON file containing these details and the NFT data, which we pass to the NFT contract as the token URI. Challenges we ran into Ensuring the accurate transfer of information between the AWS storage and the NFT contract was challenging. Ensuring that the user interface remained user-friendly and intuitive while integrating Web3 technologies also presented its challenges. Accomplishments that we're proud of We're immensely proud of how Music Minted empowers artists by revolutionizing how they mint, sell, and distribute their music. The ability to create NFTs directly, coupled with the transparency of our Chainlink-integrated process, fosters an environment of trust and integrity that we believe is much needed in the industry. What we learned While developing Music Minted, we deepened our understanding of AWS S3, NFT contracts, and the overall Web3 ecosystem. We also learned about the complexities of the music industry and how blockchain technologies can be utilized to create more equitable systems. What's next for Music Minted We plan to introduce more features to Music Minted, such as a marketplace for trading music NFTs, an integrated streaming service and multisig minting for collaborations. We also aim to incorporate more complex smart contract functionalities to cater to diverse artist needs, such as fractional ownership and royalty distributions. The journey has just begun, and the opportunities are endless! <div