---
slug: "swim-protocol"
url: "https://devpost.com/software/swim-protocol"
title: "Swim Protocol"
hackathon: "IGNITION | A Global Solana Hackathon"
organization: "Solana Capital"
winner: true
words: 1174
team_size: 1
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "domain/developer_tools"
  - "user/developer"
  - "substrate/financial_record"
---

# Swim Protocol

> Have you ever wanted to move your assets freely around the multi-chain DeFi ecosystem? Swim provides an avenue where you can move capital to and from different chains all in native assets

[Devpost](https://devpost.com/software/swim-protocol) · hackathon [[IGNITION - A Global Solana Hackathon]]

## Facets

**domain** [[developer_tools]]
**user** [[developer]]
**substrate** [[financial_record]]

**stack** alchemyapi, digitalocean, eui, react, rust, serum/borsh, solana, solana-program, spl-token, typescript, vercel, wormhole

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for swim protocol

## Body

Inspiration The Defi ecosystem has grown to be multi-chain in the last six months. Capital mobility, especially within stablecoins has grown in importance amongst the defi user community. With that in mind, we want to build a product that breaks down the barriers between all of the siloed ecosystems while enabling Solana, the fastest and cheapest chain, at the center. What it does At its core, Swim Protocol is a multi-chain AMM that allows users to connect to any of the blockchains that it currently supports (Ethereum/Binance Smart Chain/Solana), and swap native assets across these chains. Furthermore, when adding liquidity to the pool, the user has the ability to receive an LP token on any chain that Swim supports. How we built it After deciding on the project, we first looked at other AMMs. After spending a lot of time comparing the different decisions they made and testing their math, two of our developers started writing a new AMM contract from scratch. From the very start, we made the number of tokens in the pool easily configurable, thus saving a lot of headache later on. At the same time, our other two developers started work on a UI. We wanted to spend little time on the visuals, so we chose Elastic UI as a component library and started writing the forms and Solana program interaction. Eventually the smart contract was feature complete, so we deployed it to each developer’s local Solana cluster and started testing the UI against it. Soon after we set up a Wormhole environment on a Digital Ocean droplet which developers could SSH/port-forward to. The rest of the time the contract team spent fixing bugs, optimizing the compute budget, and writing tests. The UI team added support for non-Solana tokens to all forms and finally we were able to deposit six tokens across three different chains with one click of a button. Challenges we ran into Wormhole Environment Setting up all the pieces of a local Solana cluster, Ethereum and BSC chains, and a Wormhole Guardian setup to connect them all is not trivial The Wormhole team was very supportive though and we managed to get a working, stable environment running Wallets are not Ready for Multi-Chain We initially added and had plans for more Ethereum and BSC wallets but realized most of them are not built with cross-chain in mind Most BSC wallets inject themselves into window.ethereum Binance Chain wallets doesn’t do this but instead doesn’t support custom networks Metamask supports switching networks (which we ended up using) but that creates problems with reading user balances on Ethereum and BSC at the same time Cross-Chain Interfaces are Complex The most complex transaction our product can currently do is: Withdraw six amounts to three different protocols using LP tokens from either Ethereum or BSC. Hiding the intricacies involved in that kind of transaction while providing transparency and power to the user is a very challenging problem and one we had a lot of fun tackling Many edge cases can occur: What if the user has LP tokens on Solana, Ethereum, and BSC and they want to withdraw 90% to a single token? We probably want to use the LP tokens on Solana first, then wormhole the rest over from Ethereum? BSC? Both? We also have to calculate the estimated number of LP tokens needed, then add the user’s selected max slippage setting and therefore wormhole more than the user likely needs. The user ends up with a residue of LP tokens on Solana - what happens to those? Balances are constantly updated, thus triggering new estimated input/output amounts. We only want to recalculate those on user action, otherwise the numbers might automatically change right before the user submits (rendering their max slippage setting useless). Solana Compute Budget Limitations Solving the stableswap invariant requires running numeric methods (in our case Newton's method) Intermediate results for realistic values can require a precision of more than 128 bits Worse intermediate results can get very large (>>2^64) or very small (<< 1), hence requiring some kind of floating/decimal datatype Solana’s intrinsic support for datatypes larger than u64 has not been fully developed The built-in u128 has worse compute budget characteristics than the uint crate for add/sub/mul (14 vs 8 compute units for add/sub, 49 vs 8 for mul!, only division is faster!) The SPL precise_number module could be improved (1800 compute units for a single U256 division - that's almost 1% of the entire available compute budget!) In comparison, on Ethereum, the built-in u256 operations are cheap: ADD/SUB are 3 gas each and MUL/DIV are 5 gas each Solana is a bit opaque when trying to optimize for compute budget Lack of explanation for how to read the ELF dump (and what operations are even supported, much less their compute budget costs) You mostly have to guess what changes might be beneficial and then rely on profiling Rust Rust was at times trickier to write in than C++ (which we have a background in) No default arguments No function overloading No generics/template specialization Very limited (and only recently made stable) support for const generics Hence far too much reliance on macros and encoding of typenames in function names (when it should be a generic parameter) Accomplishments that we're proud of Decent UI While there are plenty of AMM interfaces, ones with cross-chain functionality are rare. We are proud of how we have hidden most of the complexities of cross-chain transactions from the user while giving them power where necessary. Of course, much is yet to be desired and we have big plans for form validation, error handling, and many edge cases. Liquidity Pool Contract from Scratch Writing a decent implementation for a stableswap liquidity pool basically from scratch, despite having no prior experience with Solana and being a freshly baked team Self-Consistent Fee Calculation Turns out that some of the major players in the AMM domain (Curve, Balancer, etc.) have inconsistent fee math. Operations that should yield the same result end up charging different fees We developed a model that's self-consistent This turned out to be harder than it sounds due to the non-linearity of the stableswap invariant What we learned Keeping track of decimals is important when handling token amounts, especially when the number of decimals differ between protocols Compute budget optimizations are tricky but very important A cross-chain UI demands a ton of edge case handling Having to test Ethereum interactions on mainnet hurts What's next for Swim Protocol Product Launch (audit scheduled for Nov 1st) Terra Support BTC & ETH pools Expanding the bridgeable network - possibly working with Wormhole to aggressively expand the network to other EVM compatible chains to connect Solana to more ecosystems Integrating our LP token and price API into the various protocols connected by Swim’s ecosystem Expanding to AMM variants (not sticking to just stableswap AMM’s) e.g. , SOL <> ETH cross chain, x*y=k style AMM Expanding Swim’s cross-chain user experience to other DeFi primitives / collaborating with existing Solana DeFi primitives to enable cross-chain compatibility <div