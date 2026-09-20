---
slug: "beatbridge"
url: "https://devpost.com/software/beatbridge"
title: "BeatBridge"
hackathon: "Chainlink Spring 2023 Hackathon"
organization: "Chainlink Labs"
winner: true
words: 470
team_size: 3
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
---

# BeatBridge

> BeatBridge: Transcend ordinary music fandom. Connect, promote, and support your favorite artists while earning unique rewards. Experience music on a whole new level.

[Devpost](https://devpost.com/software/beatbridge) · hackathon [[Chainlink Spring 2023 Hackathon]]

## Facets


**stack** amazon-web-services, chainlink, evm, react, solidity

## Body

Landing page Landing page Landing page User facing artist page User facing artist page - mint/claim interface User facing artist page - mint/claim interface artist dashboard artist dashboard - changing metadata 🌟 Inspiration Music connects people worldwide. Recognizing the power of this universal language and the crucial role fans play in an artist's journey, we created BeatBridge. We sought to empower fans to become active participants, not just passive listeners. 🎵 What it does BeatBridge allows fans to support their favorite artists directly. By engaging with music, sharing, and promoting it, fans earn tokens redeemable for exclusive rewards. It's a unique platform where every beat builds bridges between artists and fans. 💻 How we built it In our project, we leveraged the Chainlink Oracles to bring off-chain data on-chain securely. The Spotify API allowed us to collect various user-related data (such as favorite songs, playlists, time spent on music, etc.), but this data inherently resided off-chain, meaning outside of the blockchain network. This is where Chainlink came in. We used the oracles to make the data accessible to our blockchain-based reward system. Specifically, whenever a user interacted with music on Spotify, the Chainlink Oracle would process and validate that interaction's data and then transmit it to our blockchain. This system ensured that our blockchain was always updated with the latest user interaction data, which in turn allowed us to calculate rewards accurately. AWS and Rating System: As for the rating system, we used Amazon Web Services (AWS) for its versatility and power. Our rating system needed to be robust and capable of handling large amounts of data since we were dealing with potentially millions of data points from the Spotify API. To cross-reference the endpoint data, we employed AWS API Gateway. This service helped us create, manage, and secure our APIs, allowing us to effectively compare the data we received from both Spotify API and Chainlink Oracles. As a result, we could ensure the accuracy of our rating system and the legitimacy of the data, ultimately creating a trustworthy and rewarding user experience. 🚧 Challenges we ran into Balancing seamless usability with robust security was a primary challenge. Furthermore, developing a rewarding algorithm that accurately reflects user engagement required rigorous testing and refinement. 🏆 Accomplishments that we're proud of Successfully integrating blockchain technology into our platform is an accomplishment we're immensely proud of. Additionally, the positive feedback from early adopters has been incredibly gratifying. 🎓 What we learned We learned the importance of user feedback and iterative development. It has been an enlightening journey, diving into the complexities of API integrations, blockchain technology, and UI/UX design. 🚀 What's next for BeatBridge We're looking to partner with more artists and music platforms to broaden our scope. We're also planning to introduce more reward categories, amplifying our users' engagement and experiences. <div