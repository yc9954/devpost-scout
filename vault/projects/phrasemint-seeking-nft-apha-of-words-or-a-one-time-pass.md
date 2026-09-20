---
slug: "phrasemint-seeking-nft-apha-of-words-or-a-one-time-pass"
url: "https://devpost.com/software/phrasemint-seeking-nft-apha-of-words-or-a-one-time-pass"
title: "PhraseMint - Seeking NFT apha of words or a one time pass?"
hackathon: "Fantom Hackathon Q2 2023"
organization: "Fantom Foundation"
winner: true
words: 706
team_size: 1
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "domain/developer_tools"
  - "substrate/financial_record"
  - "substrate/structured_db"
  - "substrate/video_visual"
---

# PhraseMint - Seeking NFT apha of words or a one time pass?

> Digital content is revered only as images (NFT's), imagine if you could create a digital asset by simply coining a new phrase. It could be your pass phrase or even a unique word just invented by you.

[Devpost](https://devpost.com/software/phrasemint-seeking-nft-apha-of-words-or-a-one-time-pass) · hackathon [[Fantom Hackathon Q2 2023]]

## Facets

**domain** [[developer_tools]]
**substrate** [[financial_record]] [[structured_db]] [[video_visual]]

**stack** amazon-web-services, covalent, css3, erc1155, hardhat, javascript, next.js, sdk, solidity, thirdweb

## How they structured the write-up

- inspiration
- what it does
- how we build it
- challenges we ran into
- accomplishments that we’re proud of
- what we learned
- whats next for phrasemint?

## Body

Result of the testnet word check after being minted in the videos Inspiration This project is inspired by the ability to make token creation as simple as typing out words, so that even a child maybe able to do it and serve as a platform for both security and education, The ability to have ownership of a newly minted phrase or to be able to use it as a one time password to log into any system that supports smart contracts. What it does PhraseMint gives you the ability to simply "mint" a new phrase or word as metadata of an NFT into the blockchain. This action is associated with your wallet ID and the transaction address. The DApp requires you to first log in using your wallet address and then input a phrase, by checking that it does not already exist on the smart contract. This allows each word to be unique irrelevant of wallet address. How we build it PhraseMint was built using the third web sdk based on next.js (javascript) and css programming languages for web3 DApps. The DApp sits on top of a ERC1155 smart contract deployed on the fantom opera network which allows the DApp to push phrases onto the blockchain. ERC1155 was used because of its fungibility agnostic nature which will allow PhraseMint to be extended even as a gaming DApp that will reward users with platform specific tokens for minting new words. Further Covalent API, a third party API was used to validate the uniqueness of the phrase minted within the smart contract. The application prototype was deployed on an AWS platform (AWS Amplify) for general use and testing. Challenges we ran into Thirdweb SDK gives an end to end experience right from creation of a standard smart contract and web3 DApp to deploying them, thus enabling easy integration between the DApp and smart contract. The main challenges faced were with the integration of the third party API (Covalent) as many of the functions provided by it are not supported on the fantom network. Other challenges faced were making data feeds from dictionary databases available through API’s recognised on the fantom network (eg, API3, Covalent, etc). Offchain data like dictionary or attack databases will enhance the experience of the user by increasing the uniqueness and reliability of PhraseMint across multiple platforms. Accomplishments that we’re proud of We are confident that PhraseMint, even though in its nascent stages today will serve as a platform for both security and education. With its ability to facilitate for One time password token generation and NFT Metadata feeds available through Covalent API it will allow the decentralisation of the normal centralised password databases that are now commonly used today on Web2 platforms. Further for people like us that cannot keep track of our passwords, it will once and for all remove the need to remember them. This is possible if other platforms can utilise PhraseMint smart contract data to serve as decentralised ledgers along with user wallet addresses for their login systems (possible by Covalent API integration). We do not earn any fee for this application, except for the gas fees paid by users for the platform. We are also proud of PhraseMint’s future vision in education as users will mint unique phrases for which they can be recognised and rewarded by the platform. What we learned Writing and deploying smart contracts using solidity and hardhat. Writing and deploying a web3 DApp using next.js and css. Integrating third party API’s like Covalent for on chain data feeds. JSON string search for NFT metadata as opposed to database querying. Whats next for PhraseMint? We would like PhraseMint to detect phrases from other dictionary attack databases that are available off chain to increase the reliability and uniqueness for one time password generation. This would mean that other applications that are hosted on Web3 will be able to integrate with contract data available from PhraseMint using API services like Covalent for add-on security apart from the usual wallet addresses. We would also like to develop the platform further as a gaming environment where users are able to mint new phrases by integrating it with other literary / dictionary databases and co-create the dictionary of the future. <div