---
slug: "wp-dun2zt"
url: "https://devpost.com/software/wp-dun2zt"
title: "Captchains: Chainlink-powered Captchas on demand"
hackathon: "Chainlink Spring 2022 Hackathon"
organization: "Chainlink Labs"
winner: true
words: 600
team_size: 1
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "substrate/video_visual"
  - "substrate/web_dom"
---

# Captchains: Chainlink-powered Captchas on demand

> Create smartcontract powered captchas backed by IPFS, Chainlink, and Moralis on the BSC/Polygon networks.

[Devpost](https://devpost.com/software/wp-dun2zt) · hackathon [[Chainlink Spring 2022 Hackathon]]

## Facets

**substrate** [[video_visual]] [[web_dom]]

**stack** bsc, polygon, react

## How they structured the write-up

- captchains

## Body

Captchains - Home page Deployed captcha contract and interactions on BSC testnet Chainlink/Covalent API call for API-based authentication question Created Captchas main dashboard Captcha creation form Funding a live Captcha contract Logging in Moralis entries are stored for each user based on their address. Captcha Preview Remix view of a deployed Captchain contract Attempting Captcha authentication CaptChains Create Captchas on-demand backed by Chainlink API calls and smart contracts on the BSC Testnet or Polygon Mumbai chains. Captchains is a platform for validating site visitors or user actions by requiring users to validate they are human by the ability to research the answer to an API-driven question - rather than images alone. LIVE DEMO HERE: captchains.surge.sh (live deployment instance restriction is that you must be on BSC Testnet) Github: http://github.com/cbonoz/chain22 Technologies used Chainlink Services: Every Captcha is saved as a smart contract on the BSC. All login attempts (captcha successes and failures) are emitted from the contract as events. Filecoin storage and tools: Each Captcha image is hosted on IPFS. Covalent API calls: Price fetch and human validation of the price. When the captcha is loaded the user can submit a low-cost chainlink API call to update the latest value on the contract. Moralis - Captcha storage and lookup per user (based on active metamask address). Each Captcha: Requests the user to identify a keyword based on an image you specify (not autoselect of images). Second, requires the user state the latest price of ethereum, but this could be in theory any API-call based question that requires user research in order to correctly answer. Attempts (successes and failures) are logged to the contract. The captcha is also self-driving, operating based on the gas fees of the network in order to process the authentication. This makes Captchain work well with lower-cost networks such as Polygon/BSC. How it works Dynamic/API-call driven captchas that have character, or have dynamic questions based on the app you're visiting. Have an auditable history of successes, fails, and interactions with every Captcha stored on the blockchain network. Create a platform managing captchas across many different apps, all for the cost of gas on low cost BSC testnet and polygon chains. How to run Define the following environment variables: REACT_APP_MORALIS_ID={YOUR_MORALIS_APP_ID} # Moralis app id REACT_APP_MORALIS_SERVER={YOUR_MORALIS_SERVER_URL} # Moralis server url REACT_APP_COVALENT_KEY={YOUR COVALENT KEY} # This is passed in as an arg to the chainlink contract. Covalent then issues an API call on each captcha to update the record (Ethereum) price which is used for authentication. App is currently configured to run against Polygon / Mumbai using Moralis as the Web3 RPC client and storage provider. yarn; yarn start Changing networks (local deployment) Update job/oracle/fee in Captchain.sol to new node provider. Update ACTIVE_CHAIN_ID in constants.js to the chain id of your target network. For Polygon Mumbai, use chain id 80001. For BSC testnet use chain id 97. Recompile Captchain.sol and add the new code to metadata.json . Update moralis credentials above to new target server. Updating the Captchain smart contract Make any changes to Captchain.sol in the contracts directory. cd contracts; yarn; npx hardhat compile If unable to estimate gas when completing a captcha, check that you're on a supported network - BSC testnet (default) or Polygon Mumbai, followed by confirming that your contract has been successfully funded; a gas estimation fee can result from calling loadValue on the contract without any LINK balance on it. Future work Production deployment. Custom branding of the Captcha widget. Export of the Captcha widget to other apps as a react component as a per-usage model. Ability to configure the API-call based authentication mechanism. <div