---
slug: "blink-blockchain-link-for-ai"
url: "https://devpost.com/software/blink-blockchain-link-for-ai"
title: "Blink - Blockchain Link for AI"
hackathon: "TRON Grand Hackathon - HackaTRON Season 6"
organization: "TRON DAO"
winner: true
words: 760
team_size: 1
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "domain/developer_tools"
  - "domain/finance_payments"
  - "domain/housing_homeless"
  - "user/developer"
  - "substrate/financial_record"
  - "substrate/video_visual"
  - "substrate/web_dom"
---

# Blink - Blockchain Link for AI

> A crypto wallet for AI. Unleash payments, escrow, actions, minting, etc

[Devpost](https://devpost.com/software/blink-blockchain-link-for-ai) · hackathon [[TRON Grand Hackathon - HackaTRON Season 6]]

## Facets

**domain** [[developer_tools]] [[finance_payments]] [[housing_homeless]]
**user** [[developer]]
**substrate** [[financial_record]] [[video_visual]] [[web_dom]]

**stack** .net, azure, bittorrent, blazor, bttc, c#, javascript, node.js, toolblox, walletconnect, web3auth, xara

## How they structured the write-up

- inspiration
- what it does
- how it works?
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what's next for blink - blockchain link for ai

## Body

Home page of www.blinkai.xyz Add a wallets to your GPTs Configure wallet capabilities. Smart-contracts include payment, minting, escrow, auctions, donations, and more Ask GPT to prepare a blockchain transaction. Blink button is shown to review the transaction and sign. Reviewing and signing the prepared transaction using WalletConnect Ask GPT to execute transactions. Blink button is shown and can be clicked to view a summary of the transaction Inspiration Web3 UX is still a challenge. Onboarding is cumbersome and smart-contracts are difficult to operate: lots of dapps and new concepts. AI assistants today lack the power to make meaningful contributions and take action. They talk the talk but don’t walk the walk. Blink aims to fix both aspects. Instead of creating new UX frameworks for Web3 we propose that AI can be a better handler of crypto wallets . AI can replace the interface and help users achieve things they otherwise would not be able to. Furthermore, this would bring AI assistants to the next level - being able to trade, buy, sell, escrow, prepare, execute, agree, confirm, etc on behalf of the user would make them much more valuable. What it does Blink gives a crypto wallet for AI in the form of an AI API. AI can use the Blink API to prepare transactions for the user, execute blockchain transactions itself or query data from blockchain. This simplifies blockchain usage for everyone and makes AI assistants order of magnitude more valuable. Blink has a utility token called BLINK token which is used to enable developers purchase API quota and capabilities. In the second phase it will be also used for end-user engagement. The Blink button is the interface which users will see when interacting with AI. The aim is to make it as powerful as the PayPal button was 20 years ago - it aims to be an easy and secure way for individuals and businesses to handle blockchain transactions with the help of AI. How it works? Developer needs to create a new AI wallet in www.blinkai.xyz and assign smart-contracts it can use. Developer needs to also fund the wallet. The ChatGPT (or some other AI/LLM) needs to be configured to use the Blink API. The end-user can converse with the AI and have it execute or prepare blockchain transactions. When transactions are prepared the user can open them to sign them themselves. Currently possible to use auctions, charity, escrow, mint nfts and diplomas, rent items and as a bonus, arrange marriages on blockchain :) How we built it Exclusively built for the Tron hackathon and BitTorrent Chain . Web3Auth used to create a wallet for each GPT IPFS for uploading images (for minting NFTs) WalletConnect for executing/confirming blockchain transactions NodeJS used for creating the Blink API Blazor (.net) used for creating the front end interface Deployed on Azure and Xara used for graphics, Toolblox.net used for creating the smart-contracts, Clipchamp for video Challenges we ran into Getting AI to show the Blink button was not straightforward and there are still some quirks. There were some issues with BTTC not supporting some newer Solidity op codes from past 0.8.20 compiler version, so I had to revert to 0.8.19. Issue with ChatGPT to give out generated image URLs - solution was to ask user to give URLs of images to mint as NFTs. Accomplishments that we're proud of The Blink button! The PayPal button became ubiquitous around 2004 as an easy and secure way for individuals and businesses to handle transactions online. The Blink button in 2024 aims to be an easy and secure way for individuals and businesses to handle blockchain transactions. The Blink button aims to take us into the Web3 era, finally. Easy integration for all developers Just put checkboxes to the smart-contract you wish to support and copy paste the API key into ChatGPT GPT buider ( https://chatgpt.com/gpts/mine ). AI itself will take care of the rest. More than just an AI website Blink is not just an AI enhanced website, but instead it is a developer tool to enable any AI to have blockchain capabilities . The goal of this project is to start a revolution, not a tiny AI website! What's next for Blink - Blockchain Link for AI Enable custom smart contracts. For the initial entry and for the sake of smoother demo’s/testing, it only supports a finite set of smart-contracts. ERC20 support Example/reference implementations like AI wallets, example GPTs, to show what is possible with Blink. To show how AI assistants would bring more value with blockchain integration. Token launch <div