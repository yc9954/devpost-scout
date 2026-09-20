---
slug: "buildblocks-x-xrpl"
url: "https://devpost.com/software/buildblocks-x-xrpl"
title: "BuildBlocks x XRPL"
hackathon: "Cal Hacks 11.0"
organization: "Cal Hacks"
winner: true
words: 380
team_size: 2
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/retrieval_grounding"
  - "domain/security_privacy"
---

# BuildBlocks x XRPL

> Create and deploy audited smart contracts on the XRPL EVM side chain using easy to understand smart contract blocks.

[Devpost](https://devpost.com/software/buildblocks-x-xrpl) · hackathon [[Cal Hacks 11.0]]

## Facets

**mechanism** [[retrieval_grounding]]
**domain** [[security_privacy]]

**stack** evm, nextjs, rainbowkit, ripple, sidechain, tailwind, typescript, wagmi

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for buildblocks x xrpl

## Body

The BuildBlocks smart contract block builder interface The BuildBlocks Compile and Deployment interface Inspiration There is a huge barrier of entry when it comes to entering the web3 space. A minor mistake in your code can cost you thousands of dollars! Firms and companies spend hundreds of thousands of dollars auditing their smart contracts to ensure that there are no exploits in their code, but with BuildBlocks, we have created drag and drop dynamic smart contract components and a platform that allows anyone to develop, compile, and deploy audited smart contracts on the XRPL EVM side chain! Along the way, we found ways to integrate classic EVM hooks and injectable wallets onto the chain. What it does Using a Retrieval pipeline on audited DeFi contracts from resources such as Uniswap, OpenZeppelin, etc., BuildBlocks allows for users to use easy-to-understand blocks to create extremely intensive smart contracts in the blink of an eye. How we built it We built BuildingBlocks using the standard NextJS, Tailwind stack, but on top of that, we used injectable wallets, the XRPL EVM side chain RPC provider for wallet injection, the SolC compiler for automated Solidity contract compilation, and SIDAI's RAG pipeline generation service which we created buckets of audited Solidity smart contracts. Challenges we ran into The XRPL chain is not fully EVM compatible, so our first challenge was deciding which chain of XRPL to build on. After deciding on using the EVM-compatible chain due to its potential for widespread adoption. Secondly, as the EVM side-chain is very new, there were no integrations with popular providers such as MetaMask or Wagmi. Because of this, we had to work around this by manually injecting the XRPL RPC and chain ID into both of these providers. Additionally, working with developing RAGs was a new learning experience for the entire team! Accomplishments that we're proud of Created high quality smart contracts with drag and drop composables! Full end-to-end suite of developing, compiling, and deploying a smart contract! What we learned The life cycle of a smart contract! Our team learned a lot about full stack and on-chain development. Working with a new chain is always cool, especially a Ripple side chain! What's next for BuildBlocks x XRPL Cross chain compatability and developing smart contracts for cross-chain compatability! <div