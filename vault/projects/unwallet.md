---
slug: "unwallet"
url: "https://devpost.com/software/unwallet"
title: "Unwallet.me"
hackathon: "Constellation: A Chainlink Hackathon"
organization: "Chainlink"
winner: true
words: 1267
team_size: 4
has_repo: true
has_live: true
has_video: false
tags:
  - "project"
  - "mechanism/measured_ablation"
  - "mechanism/provenance_signing"
  - "domain/developer_tools"
  - "user/general_public"
  - "substrate/financial_record"
  - "substrate/geospatial"
  - "substrate/sensor_telemetry"
---

# Unwallet.me

> Next-Gen Web3 Onboarding by combining seedless Passkey-powered AA wallets with domain auto-registrations & multi-chain management.

[Devpost](https://devpost.com/software/unwallet) · hackathon [[Constellation- A Chainlink Hackathon]]

## Facets

**mechanism** [[measured_ablation]] [[provenance_signing]]
**domain** [[developer_tools]]
**user** [[general_public]]
**substrate** [[financial_record]] [[geospatial]] [[sensor_telemetry]]

**stack** avalanche, ccip, chainlink, ens, foundry, next.js, openai, passkey, permissionless.js, pimlico, react, solidity, tailwind, thegraph

## How they structured the write-up

- inspiration 💡
- what it does ⚙️
- how we built it 🛠️
- challenges we ran into 🧗‍♂️
- accomplishments that we're proud of 💪
- what we learned 🎓
- what's next for unwallet 🔮

## Body

Multichain CCIP/ENS Architecture Pitch - Solution Pitch - Problem Try it out yourself: https://unwallet.me Twitter Announcement: https://twitter.com/unwallet_me/status/1737874854953783299 Inspiration 💡 The user experience of web3 is still broken. Billions of funds are lost due to the complexity of seed phrases, private keys, and alphanumeric wallet addresses. The masses are not yet onboarded and this will not change with drop-off rates >90% for wallet setups. With account abstraction, wallets can be smart contracts with flexible signer setups that eliminate the private key and increase security at the same time. Smart wallets are getting more and more popular in the growing Ethereum L2 and broader EVM ecosystem, but at the same time they also introduce new challenges. Contrary to EOA wallets, smart wallets have to be separately deployed on different chains which can lead to different multinetwork wallet addresses or complex state drifts. Now, users not only have to deal with the complexity of one alphanumerical wallet address, but ones on multiple chains which might not even be in sync. How can we solve this? What it does ⚙️ Unwallet revolutionizes web3 onboarding & account UX by providing a seedless & gasless multi-chain smart wallet with a native on-chain domain. This domain is registered in a multi-chain ENS protocol that follows a hub & spoke architecture using CCIP for communications with the hub being deployed on Avalanche Fuji . 🗻 Select Domain – The user selects an on-chain domain name or gets inspired by AI. Create Smart Wallets – Multi-chain smart wallets with counterfactual addresses on all supported chains are created with Passkey-powered signatures. Automatic Domain Setup – Multiple batched transactions to register & configure the users new multi-chain domain are passed within one single user operation. Login & Unified Dashboard – After the onboarding flow and a later via biometric login, the user is forwarded to a unified multi-chain dashboard with aggregated balances which are converted with the help of price feeds by Chainlink. In the future, this is the place where the user will be able to manage their new domain from any associated wallet on any associated chain. With Unwallet, we achieve: Web3’s easiest onboarding process Seedless & gasless onboarding by leveraging account abstraction and Passkey technology Registering & configuring a complex multi-chain domain setup in one single user operation Overcoming the entire account complexity by abstracting private AND public keys. First cross-chain domain system where the domain can be managed from all connected chains (incl. Avalanche, Polygon, Optimism and Base) How we built it 🛠️ Despite the hacky nature of such an event, we really tried to go the extra mile on all technical levels by using the latest & greatest tech stack and available SDKs. But at the same time we maintained very high, almost production-grade, coding standards & project setups (have a look yourself). Contract Tools : For writing & deploying Solidity, we used the Foundry toolkit (i.e. forge) and Remix. Protocol : We forked ENS and extended its multi-chain capabilities with a hub & spoke architecture via CCIP. For each of the following 4 contracts, there exists a {Contract}CCIP (hub) and xc{Contract} (spoke) implementation with in total more than 20 function selectors that are executable cross-chain now. This is showcased in the Register.s.sol script. Chains : We deployed on the following testnet chains: Avalanche Fuji (hub), Polygon Mumbai (spoke), Optimism Goerli (spoke), and Base Goerli (spoke) with a customized deploy.sh & verify.sh shell script that calls the Deploy.s.sol foundry/forge deploy script internally. Frontend : We built a modern React-based frontend application with Next.js 14, app-dir routing, modified shadcn/ui components, and Next.js API routes for Turnkey & OpenAI interactions. Web3 Interactions : For efficient and type-safe chain queries & tx’s, we use wagmi, viem, and AbiType. With the wagmi code generation CLI, we directly gather metadata from. Domain Registration & Setup : The user operation includes: domain registration; setup of resolving address; setup of reverse resolution; setup of multi-chain resolving addresses for all configured smart wallets via ENSIP-11. Account Abstraction : For initializing AA smart wallets in our frontend, we use the Pimlico SDK incl. their Bundler, Paymaster, and permissionless.js. Passkeys : For biometric-based accounts & signatures we manually (!) integrated Turnkey, which is also used by ZeroDev or Web3Auth. AI : We use prompts via the OpenAI API to generate creative ideas for domain names which we then stream to the frontend. Indexing : To show recently registered domains on our landing page and gather KPIs, we deployed a Subgraph via The Graph which is indexing our registry and reverse registrar contracts. Chainlink Data Feeds : To aggregate & convert a user-friendly multi-chain balance, we fetch verifiable price rates directly from the on-chain Chainlink Data Feeds on Ethereum Mainnet. Challenges we ran into 🧗‍♂️ Smart Contract challenges: Understanding ENS contracts co-dependencies; especially the PublicResolver part. CCIP's EIP165 supportsInterface was set to "pure" visibility and wasn't marked virtual. So we had to clone it and mark it as view and virtual. Some functions of CCIP & ENS libraries were incompatible with each other. We had to make conscious changes to both to solve this. Following on the ENS pragma statement (>= 0.8.4) our team faced inconsistent behavior. It was caused because we were using different compiler versions. Solidity version of 0.8.20 had breaking changes in both bytecode and the openzeppelin contracts. After our discovery, we bumped the versions to ^0.8.20. Frontend challenges: The custom integration of Passkey (Turnkey) functionality with ERC-4337 SDK (Pimlico) Clean Passkey UX (minimize signing requests; ui overlay; domain usernames) Smart Wallet initialization with domain registration, auto-setup of all multi-network addresses (via ENSIP-11), and auto-setup of reverse resolution. – Everything in one user operation with ERC-4337's executeBatch. Seamless multi-chain-first experience (e.g. fetching/aggregating/converting all balances from all chains; or determining counterfactual addresses on all networks) Accomplishments that we're proud of 💪 With unwallet.me, we developed a new onboarding primitive for web3 that abstracts away seed phrase, private key, public wallet address, gas fees and manually creating wallets on different chains. We created the first cross-chain domain system that is not only resolving on multiple chains but the domains can be managed from any supported chain. We were able to overcome all challenges we faced during development. What we learned 🎓 How to develop and utilize the advantages of CCIP and use Chainlink Data Feeds. How to create a multi-chain domain system based on ENS with CCIP that allows us to manage a domain from all supported chains. How to use account abstraction for smart wallet creation and transaction signing. How to manually build a secure Passkey-based authentication & signing process while maximizing for UX. What's next for Unwallet 🔮 Add more L2s and EVM-based Alt L1s with the goal to support the entire EVM ecosystem with the ultimate goal to go even beyond this ecosystem and expand non-EVM chains. Explore ENS subname wrapper and how we might be able to build our namespace on top as an extension to ENS to leverage its economic and technical security. We would like to challenge our ideas with the ENS DAO and ENS Labs. Use CCIP Read to bring domain state to Ethereum Mainnet in a gas-optimized way as well as powering single-step cross-L2 read calls. Integrate multi-chain bridging and swapping functionality aggregators such as via li.fi or socket.tech. As soon as something like EIP-7212 is implemented, we would like to bring Passkey signature evaluation directly for a maximum of decentralization while staying gas efficient. Build mobile app to utilize a mobile-first onboarding and wallet experience Add more on-chain specific functionality like a native marketplace for trading, and demand-based domain renewal system. gm 👋 <div