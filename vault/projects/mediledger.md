---
slug: "mediledger"
url: "https://devpost.com/software/mediledger"
title: "MediLedger"
hackathon: "TreeHacks 2025"
organization: "TreeHacks"
winner: true
words: 927
team_size: 4
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/structural_withholding"
  - "domain/developer_tools"
  - "domain/education"
  - "domain/health_clinical"
  - "domain/supply_logistics"
  - "user/educator_student"
  - "user/patient_family"
  - "substrate/code_repository"
  - "substrate/financial_record"
---

# MediLedger

> A privacy-preserving drug availability search powered by EigenDA and ZK-PTLS

[Devpost](https://devpost.com/software/mediledger) · hackathon [[TreeHacks 2025]]

## Facets

**mechanism** [[structural_withholding]]
**domain** [[developer_tools]] [[education]] [[health_clinical]] [[supply_logistics]]
**user** [[educator_student]] [[patient_family]]
**substrate** [[code_repository]] [[financial_record]]

**stack** data, eigenda, express.js, flutterflow, merkle-proofs, merkle-trees, node.js, sha256, typescript, web3

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for mediledger

## Body

Initial Proof of Concept (working interface for hospitals to request drug availability on) Inspiration Hospital stockouts—the unavailability of essential medications and medical supplies—present a major crisis in healthcare. Patients suffer delays in critical treatments, emergency rooms lack life-saving drugs, and hospitals are forced to ration care. Despite medical advancements, hospitals still rely on outdated, fragmented inventory systems, leading to supply shortages that compromise patient outcomes. The biggest challenge? Hospitals don’t want to share their entire inventory with competitors. Right now, checking stock requires manual calls between hospitals, which is slow, inefficient, and unscalable. The result? Wasted time that directly exacerbates preventable patient harm. Our project is uniquely ambitious in the way we are applying Web3 to a deeply centralized system like healthcare, but we want to reinvent how cybersecurity works in this important industry. We care about using blockchain for social good, so a detailed problem statement highlighting the inspiration for our product is linked below. What it does MediLedger is all about collaboration: providing a decentralized platform on which hospitals can more securely and confidently transmit sensitive data. Our system enables hospitals to securely check drug availability at other hospitals without exposing full inventory details on both ends. Instead of storing a simple list of drugs, each hospital stores its own inventory in a Merkle tree, where each leaf node contains a cryptographic hash of a drug name and quantity. The Merkle root (a compact summary of the entire inventory) is then submitted to EigenDA, a decentralized data availability layer. EigenDA allows hospitals to store inventory commitments on-chain without revealing individual stock details and ensures data integrity—any change in inventory changes the Merkle root, which prevents tampering. When a hospital needs a drug, the AI agent first checks the local hospital’s inventory. If the drug is out of stock or the supply is trending low, the AI agent fetches Merkle roots of nearby hospitals from EigenDA using Zero-Knowledge Proofs (zkProof) and the provided Merkle trees. The hospitals that have the requested drug generate a Merkle proof, which extracts the leaf node (hashed drug and quantity) from the Merkle tree, includes all necessary sibling hashes to allow recomputation of the Merkle root, and ensures the proof matches the stored Merkle root on EigenDA. The system then outputs a list of hospitals whose Merkle proofs have been validated, thus proving they have the drug in stock. How we built it The backend server was built with Express.js, Node.js, and TypeScript. For the hashing algorithm, we used SHA256. While configuring the adapter for EigenDA, we used EigenLayer’s extensible agent framework for verifiable AI capabilities and data availability logging. The frontend was built with FlutterFlow, with an initial POC frontend built using Next.js. Challenges we ran into The biggest challenge was integration—the backend deployment was not Much of what we worked on also involved repositories and tools with limited documentation, where we underwent educated debugging in a field we had little prior experience in. We initially had two ideas (this one and another more fintech focused on price manipulation) that we pivoted twice between on Friday, so defining the initial feature set for both with a blockchain focus took some time, especially with the crunch time of 36 hours. The biggest challenge was integration as well with FlutterFlow. Accomplishments that we're proud of For most of the team, TreeHacks 2025 is our first hackathon ever. We could have played it safe using familiar Web2 tech stacks from classes, we decided to challenge ourselves by diving headfirst into Web3 and cryptography. In a span of 36 hours, we overcame the steep learning curve of understanding and implementing Merkle proofs and trees, which are notoriously complex but incredibly powerful for verification. Despite occasional roadblocks, we were determined to not give up on our ambitious ideas (where else has blockchain been integrated with healthcare?). Our team wore multiple hats—from testing backend deployment to graphic design and marketing. In the end, we are proud of how we built a fully decentralized inventory system for hospitals to use. What we learned One of our largest takeaways from this weekend is how accessible hacking can be—even to students with limited technical exposure. With the right background and a willingness to learn new tools, we became a determined team that collaborated well on an interesting idea. Blockchain can be used for security and social good, and we hope we proved that through intersecting these technologies with healthcare. For a more technical side, we learned how hash-based data structures allow for selective proof generation. Storing data off-chain in EigenDA was a major shift from Web2 thinking, and now we understand that different decentralization techniques come with trade-offs in performance. What's next for MediLedger If we had more time, we would love to implement more features related to Web3: Right now, our proof verification happens off-chain in our backend. A great addition would be to store Merkle roots & zkProofs on Ethereum or a Layer 2 (e.g., Polygon, Arbitrum). This would allow on-chain smart contracts to verify zkProofs without a centralized backend. Currently, hospitals only react when a drug is out of stock or if supply has a diminishing trend. We would love to use our AI agent to predict drug shortages before they happen: analyzing historical hospital inventory data to forecast demand surges and sending alerts to hospitals before a stockout occurs. Currently, hospitals authenticate via API keys. Instead, we could use Web3 wallets (e.g., MetaMask) for hospital authentication, where hospitals could digitally sign zkProofs before submitting them. This would prevent unauthorized hospitals from accessing inventory data. <div