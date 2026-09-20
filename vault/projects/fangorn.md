---
slug: "fangorn"
url: "https://devpost.com/software/fangorn"
title: "Fangorn"
hackathon: "Build Resilient Apps with Polkadot Cloud"
organization: "POLKADOT"
winner: true
words: 1369
team_size: 2
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/multi_agent"
  - "mechanism/provenance_signing"
  - "mechanism/realtime_stream"
  - "domain/labor_employment"
  - "user/general_public"
  - "user/researcher"
  - "substrate/financial_record"
---

# Fangorn

> Fangorn is a permissionless threshold encryption network that enables programmable access control for web3.

[Devpost](https://devpost.com/software/fangorn) · hackathon [[Build Resilient Apps with Polkadot Cloud]]

## Facets

**mechanism** [[multi_agent]] [[provenance_signing]] [[realtime_stream]]
**domain** [[labor_employment]]
**user** [[general_public]] [[researcher]]
**substrate** [[financial_record]]

**stack** arkworks, ink, ratatui, react, rust, substrate, subxt

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for fangorn

## Body

Inspiration Web3 promised digital ownership, but there is a gap: access control. While decentralized applications can rely on decentralized storage like IPFS, it offers no access control. Anyone knowing a CID can read the data. This makes it unusable for private content, token-gated files, or anything requiring conditional access. Current solutions either: rely on centralized APIs, reintroducing platforms that web3 was supposed to supercede rely on decentralized KMS like LIT, which are costly, chain-bound, and limited in scale So we asked: What does it take to share a secret onchain? What if owning an NFT not only let you 'own' a pointer to external data, but instead cryptographically guaranteed access? What if proving membership of a DAO granted access to unique datasets? How can this actually scale to millions of users? What it does Fangorn lets you encrypt data under onchain conditions. It accomplishes cryptographic access control through a paradigm that we call 'intent bound data'. It lets you encrypt data under public statements , like " Prove you own 1 of my NFTs". When someone prove they meet that condition (owning the NFT), a decentralized network verifies it and produces partial decryptions. The user just aggregates them and decrypts the data. Use Cases Token-Gated Content : easily gate content behind tokens (e.g. PSP22). This could provide new tools for digital creators to license, distributed, and earn from their work. On-chain secret sharing : share secrets on-chain without needing an expensive DKG protocol (like LIT) DAOs : member-gated resources become easy and automatable; access by proof not permission Data Marketplaces : Fangorn could give rise to new kinds of data marketplaces where creators define access control that's enforced by the network. This could be anything, from 'buy my NFT' to 'prove that you voted in referendum X and that you are a member of DAO Y and that it rained on Jakarta on Wednesday'. The Fangorn network supports various 'gadgets' that are registered in a 'gadget registry'. This is an extensible framework that can be used to easily introduce new gadgets with unique logic. For the scope of the hackathon, we build three: password-gadget - a minimalistic gadget implementation that allows data to be encrypted under a (one-time-use) password psp22-gadget - allows data to be encrypted such that knowledge of the public key of anyone owning at least a minimum balance of the token defined in the psp22 contract can decrypt the data sr25519-gadget - verify a schnorr signature Gadgets can be composed to build more complex statements. For example, by composing the psp2-gadget and sr25519 gadget, we achieve token-gated content . e.g. Psp22(contract_address, min_balance) && Sr25519() . How we built it Note: There is far more info in the project readme The core of the system is an interaction between three major components: Core Architecture : Iris Contract (ink!) - an onchain 'intent registry' Fangorn Network - p2p threshold encryption network Quickbeam & Entmoot - CLI/TUI tools for encryption/decryption, building witnesses, etc. Key Innovation Our scheme relies on breakthroughs in threshold encryption that eliminate the need for a distributed key generation mechanism, called silent threshold encryption . We worked directly with the authors of the paper, who produced an academic prototype , to enhance the library with better error handling and performance , though this was not part of the hackathon. Networking The networking is enabled using iroh , where we rely on gossipsub for communications between nodes. We also leverages Iroh's blobstore and docstore for storing public keys and public parameters needed to sync with the network and produce partial decryptions. Substrate Integration Each node has a configurable backend that must be able to communicate with smart contracts for calling and querying data. To do this, we used subxt and subxt_signer, as well as various other substrate dependencies and libs. We also implemented a contract-based intent store interface, which worker nodes and the entmoot client leverage in order to read/write intents to the registry. In addition, our keystore implementation leverages sp-keystore, sp-core, and various other low-level substrate libraries needed to implement an sr25519 keystore. Along with the dynamic intents store, we also developed an extensible gadgets framework that can be used to build new 'intents'. Each gadget is responsible for parsing raw user input into a 'statement' that the gadget can understand. It also encapsulates witness verification logic. Our docs include a guide on this. The psp22 and sr25519 gadgets both rely on subxt. We implemented two different ink! smart contracts. The 'iris' contract is basic intent registry contract, which is open and permissionless, allowing anyone to public their intent-bound data. Along with this, we use a psp22 contract using community-built tooling . Challenges we ran into This is the first usage of the silent-threshold-encryption library that we are aware of. There was no existing p2p infrastructure for this, meaning we had to design and implement this from scratch using Iroh. SCALE encoding and decoding of intents as generic Vec within the contract and then visualizing it on the UI was unclear at first. While substrate can pass metadata, our system does not (yet), so we had to hardcode the decoding logic in the UI unfortunately. Accomplishments that we're proud of We built the first practical implementation of silent-threshold-encryption used within an actual p2p network. I am highly confident there is nothing similar using the same crypto and architecture. Our extensible gadgets framework allows for new intents to be easily defined, composed, and configured with Fangorn nodes; and it's functional! The network is fully, yet minimally, functional, with a very high level of modularity. While the code still holds many unwraps and other nightmares, we are proud of the framework we developed. What we learned The team has had high-exposure to many substrate tools in the past. However, we learned many new technologies during development: We learned how to implemented networking using iroh We learned about ink! standards (PSP22) and how to use/build them. We learned how to build TUIs with Ratatui We learned how to build RPCs with tonic We learned best practiced for async environments (starting from scrach), about the various Mutex types, when to use Arc, and so on. What's next for Fangorn We see Fangorn as having high-potential. We see the protocol as having the potential to enable new kinds of decentralized applications that couldn't be done before. While solutions like LIT exist, our solution is intended to be far more scalable. That is, the underlying cryptography allows the Fangorn network to potentially reach the scale of millions of users (no DKG is really a big deal). As a result, we envision Fangorn as enabling things like decentralized secret sharing (e.g. dropbox-like applications), or streaming-service-like applications based on token gated content. It could provide the cryptographic underpinnings for getting the convenience of web2 but the ownership models of web3. We also have more technical items in mind for immediate development. You can find more information about these in the project README: Funding : To reach production readiness, we may pursue funding through the web3 foundation, the treasury, or other ecosystem funds if there is abundant interest in the capabilities of the solution. Advanced implementation : We have outlined a concept for a more advanced and extendable version of intent-bound-data that would make the network more robust. This includes both a new way of bundling intent with data as well as as more robust sync protocol. Shared storage implementations : We only implemented local shared storage structs for now(meaning Fangorn can only run if all nodes are on the same machine). It should be straightforward to implement shared storage against a centralized db or an IPFS swarm. zk-gadgets : currently, each gadget requires a public, plaintext witness that reveals it to the Fangorn workers. This is fine for now, but is not privacy preserving. Instead, we would investigate the implementation of zk-gadgets for verification of witnesses, resulting in a privacy-preserving way to use Fangorn. Economic integration : This version of Fangorn has no economic incentives for workers to operate, especially to operate honestly. In the future, we would investigate an economic integration layer, perhaps as a smart contract or parachain, where we can leverage staking mechanisms to both authorize and incentivize Fangorn workers. <div