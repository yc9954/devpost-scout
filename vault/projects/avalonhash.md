---
slug: "avalonhash"
url: "https://devpost.com/software/avalonhash"
title: "AvalonHash"
hackathon: "Constellation: A Chainlink Hackathon"
organization: "Chainlink"
winner: true
words: 447
team_size: 1
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "domain/supply_logistics"
  - "substrate/financial_record"
---

# AvalonHash

> Empowering Blockchain: Next-Gen Efficiency and Security with AvalonHash- Revolutionizing Avalanche's EVM Landscape

[Devpost](https://devpost.com/software/avalonhash) · hackathon [[Constellation- A Chainlink Hackathon]]

## Facets

**domain** [[supply_logistics]]
**substrate** [[financial_record]]

**stack** avalanhego, bash, go, subnet-evm

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for avalonhash

## Body

Subnet Configuration Metamask Connection Airdrop and Precompiles Health API result Precompiled Contract implementation Inspiration The inspiration for AvalonHash stemmed from the pressing need to enhance blockchain technology's scalability, efficiency, and security. The limitations of existing blockchain platforms, particularly in handling complex computations and ensuring robust security protocols, drove our ambition to innovate. Our goal was to leverage the unique features of the Avalanche blockchain and integrate advanced cryptographic functions, like the Poseidon hash function, to set a new standard in blockchain technology. What it does AvalonHash revolutionizes the Avalanche blockchain by introducing a custom Ethereum Virtual Machine (EVM) implementation that significantly boosts computational efficiency and transaction speed. The cornerstone of AvalonHash is the integration of the Poseidon hash function into precompiled contracts, enhancing the blockchain's security and enabling more complex cryptographic operations. This not only fortifies the blockchain against security threats but also expands its applicability across various industries. How we built it The project was built through a combining expertise in blockchain technology, cryptography, and software development. We started by deeply analyzing the Avalanche blockchain's architecture and identifying opportunities for customization. The development process involved reengineering the EVM to support our customizations and integrating the Poseidon hash function into precompiled contracts, ensuring seamless execution and compatibility. The subnet configuration: --------------------------------+ | PARAMETER | VALUE | +-------------------+----------------------------------------------------+ | Subnet Name | cryptographicSubnet | +-------------------+----------------------------------------------------+ | ChainID | 76543 | +-------------------+----------------------------------------------------+ | Mainnet ChainID | 0 | +-------------------+----------------------------------------------------+ | Token Name | CRY | +-------------------+----------------------------------------------------+ | VM Version | v0.5.10 | +-------------------+----------------------------------------------------+ | VM ID | koFB4hKzyWmm6e22WAkPgwPruXvuL7qCZ6DTkXiTnz1grAeGx | +-------------------+----------------------------------------------------+ | Fuji SubnetID | r2CYJEkekfgWbKA1yjPyKg4FFiaeajpvrBbzhsnkZs46A2CoG | +-------------------+----------------------------------------------------+ | Fuji BlockchainID | 26bsE9jLMoRAwLs8MdmTtHNvpSiWc31WSgYdLqdjsqQEhvUjHc | +-------------------+----------------------------------------------------+ How to connect to this subnet: You can use metamask to connect. Name: AvolonHash Subnet RPC: http://158.220.101.185:9650/ext/bc/26bsE9jLMoRAwLs8MdmTtHNvpSiWc31WSgYdLqdjsqQEhvUjHc/rpc Chain Id: 76543 Currency Symbol: CRY Challenges we ran into Ensuring that our custom EVM implementation remained compatible with the broader Avalanche ecosystem presented both technical and logistical hurdles. Balancing innovation with system integrity and user accessibility was a continuous learning process throughout the development phase. Waiting syncronization of Fuji Testnet on validator. Accomplishments that we're proud of We are immensely proud of successfully integrating the Poseidon hash function into the Avalanche blockchain, a feat that marks a significant step forward in blockchain cryptography. Also, this was my first time to build subnet and deploy it in Fuji network. What we learned Throughout this project, we gained valuable insights into advanced cryptographic functions, blockchain architecture, and the intricacies of the EVM. I learned how to build deploy and validate Avalanche Subnet. What's next for AvalonHash Moving forward, AvalonHash aims to expand its capabilities and explore broader applications in various sectors like finance, healthcare, and supply chain management. <div