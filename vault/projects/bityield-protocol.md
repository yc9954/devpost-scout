---
slug: "bityield-protocol"
url: "https://devpost.com/software/bityield-protocol"
title: "BitYield Protocol"
hackathon: "Starknet Re{Solve} Hackathon"
organization: "Starknet Foundation"
winner: true
words: 412
team_size: 3
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "substrate/financial_record"
---

# BitYield Protocol

> A Bitcoin Native Yield Optimization protocol with automated optimization through AI Agents across multiple protocols on Starknet .

[Devpost](https://devpost.com/software/bityield-protocol) · hackathon [[Starknet Re-Solve- Hackathon]]

## Facets

**mechanism** [[realtime_stream]]
**substrate** [[financial_record]]

**stack** cairo, javascript, node.js, openzeppelin, starknet-foundry, typescript

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for bityield protocol

## Body

BitYield Protocol Inspiration Bitcoin holders control $2 trillion in assets, yet 95% of BTC remains idle. While Ethereum DeFi exploded with TVL exceeding $50B, Bitcoin users face a painful reality: accessing yield requires navigating complex bridges, multiple wrapped tokens, and fragmented protocols across chains. We envisioned a future where a grandmother in El Salvador could earn yield on her Bitcoin savings as easily as she checks her balance. BitYield Protocol makes this vision real on Starknet - combining Cairo's provable computation with Bitcoin's security and AI Agents (for simplier UI/UX) to create the first truly native Bitcoin yield aggregator. What it does BitYield Protocol is the first AI-powered Bitcoin yield aggregator on Starknet Seamless Bridge Integration : Users deposit BTC through Atomiq Protocol's Bitcoin bridge, receiving WBTC on Starknet through AI Agent Intelligent Yield Optimization : Our StrategyManager automatically allocates funds across Vesu lending markets (currently 70/30 split) using Cairo-verified rebalancing algorithms ERC4626-Compliant Vault : Users receive byWBTC share tokens representing their yield-bearing position with real-time price appreciation: Automated Rebalancing : Our Contracts auto triggers rebalancing when yield differentials exceed 5% threshold Fee Optimization : Performance fees (1%) + management fees (0.5% annually) auto-compound into user positions How we built it Architecture Stack Smart Contracts : Cairo, Starknet Scaffold 2 Frontend : Next.js, React, TypeScript, Tailwind CSS Agents : LangGraph, Node.js Challenges we ran into 1. Atomiq contracts not yet on Starknet testnet Solution : Created comprehensive MockAtomiqGateway simulating full bridge flow including relayer authorization, Bitcoin transaction verification, and WBTC minting/burning. 2. Creating flexible adapters that work with different yield sources Vesu's ERC4626 vs Troves' custom interface presented integration challenges. Solution : Built trait-based adapter system with standardized deposit() , withdraw() , get_total_assets() interface, allowing hot-swappable protocol integrations. Accomplishments that we're proud of First Bitcoin-native yield aggregator on Starknet Seamless UX - No manual bridging/wrapping for users Automated optimization via Cairo smart contracts Multi-protocol integration (Vesu, Troves, Atomiq) ERC4626 compliance for composability What we learned DeFi Yield Mechanics Studied Vesu's lending model and realized optimal rebalancing isn't just APY comparison—must factor in: Utilization curves : $$r(u) = r_0 + \frac{u}{1-u} \times r_{slope}$$ Gas costs vs yield delta Slippage on large rebalances Bridge Architecture Learned Bitcoin SPV proofs, relayer economics, and the importance of separation between bridge state (off-chain verification) and application logic (on-chain distribution). What's next for BitYield Protocol Integrate Troves/Endurfi strategies Add more Vesu pools Implement auto-compounding Advanced rebalancing algorithms (APY optimization) Governance token for protocol decisions Cross-chain yield opportunities <div