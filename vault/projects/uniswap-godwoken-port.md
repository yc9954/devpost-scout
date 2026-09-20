---
slug: "uniswap-godwoken-port"
url: "https://devpost.com/software/uniswap-godwoken-port"
title: "Uniswap Godwoken Port"
hackathon: "Web3 World Championship"
organization: "Nervos Network"
winner: true
words: 287
team_size: 1
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "domain/developer_tools"
  - "substrate/financial_record"
---

# Uniswap Godwoken Port

> Uniswap ported to Godwoken Testnet v1 Ethereum compatible rollup

[Devpost](https://devpost.com/software/uniswap-godwoken-port) · hackathon [[Web3 World Championship]]

## Facets

**domain** [[developer_tools]]
**substrate** [[financial_record]]

**stack** javascript, react, solidity, typescript

## How they structured the write-up

- inspiration
- what it does
- how i built it
- challenges i ran into
- accomplishments that i am proud of
- smart contract addresses on godwoken testnet v1

## Body

Inspiration I have been learning web3 development for quite some time now and wanted to test my abilities to not just develop software but also in the shortest time possible. The 100m dash event brought the opportunity I wanted. What it does This project is a port of the popular DeFi application Uniswap to Godwoken Testnet v1 How I built it At the beginning, I deployed all the Uniswap contracts to Godwoken Testnet v1. It was fairly simple and straightforward. Then I started understanding the Uniswap interface code as I wanted to use the same interface used by Uniswap with just the addition of the Godwoken network. Once I understood the flow I began making Godwoken specific changes to the interface. Once I got the interface working with the Godwoken network I deployed mock token contracts. Challenges I ran into The most challenging part was getting the wrapping and unwrapping of the CKB token working. Debugging the nft manager contract multicall took a lot of time. Transaction confirmation time is high on testnet, you need to wait for metamask confirmation to know that transaction is mined. Accomplishments that I am proud of You can now use the Uniswap interface with all the previously supported networks and the new addition of Godwoken! Smart contract addresses on Godwoken Testnet v1 UniswapInterfaceMulticall deployed to: 0x041916125514fbD39A6B192A98aec5dc519dD4b0 UniswapV3Factory deployed to: 0x0B344563CEEa1AbeD9eCf07B0EF131ab43Bf2138 SwapRouter deployed to: 0x43aeb2B2bC97D32D3e5418b4441225a164eB3726 NFTDescriptor deployed to: 0x10E0c54f11FB09bC0fca66c63a69386644b29133 NonfungibleTokenPositionDescriptor deployed to: 0x3C37B508c53917C86bB477E0dCEEFd8aA2f6Abc1 NonfungiblePositionManager deployed to: 0xA89E21064F131312aBBF750eFF94b780bd7b8e30 Quoter deployed to: 0x5C96109D6535e8AD49189950aeE836b84A1Bc10B TickLens deployed to: 0xACED02E1A5AC1DB647C70cdB803B9DBD3ddc8Edf V3Migrator deployed to: 0x45415787f4C5612d60aD1ac982Ff1010f9c88Aa6 SwapRouter02 deployed to: 0x3672a53dbcD7777A38D14748EF24CE313e70f3a9 WCKB deployed to: 0xbb9a94A220f3e41CE7cBf198d7555E727038de80 ETH deployed to: 0x861a4540C7F23fDfAdAdBFe7D7a06542254BE803 USDC deployed to: 0x5Ba883ADF2A2D0C29C4d006F92D6060C4CE7079d DAI deployed to: 0xc25b5CfCb909885C48038F7b844E8084C7614236 LINK deployed to: 0x6c04EBDfF0A24fC96aC7275c9b4972FD5107BBc7 UNI deployed to: 0xF2Ab144Dc527EEaDDADc4df31712c6C73bf50C2d Faucet deployed to: 0x4271365E80756D10c395389d1b36c0DE50F7d8a9 <div