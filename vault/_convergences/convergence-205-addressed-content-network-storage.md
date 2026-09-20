---
tags:
  - "convergence"
projects: 3
hackathons: 2
---

# 3 projects, 2 hackathons, one claim

**Shared vocabulary** addressed, content, network, storage

### [[nftstorage-helper]] — NFTStorage Helper
> content-addressed storage only persists what someone keeps requesting, so an asset that is rarely viewed quietly disappears from the network that was supposed to preserve it

*Chainlink Spring 2022 Hackathon* · problem: infrequently requested IPFS content is dropped from nodes and slows or vanishes

### [[chainlink-hash]] — Wiki IPFS
> content-addressed storage produces a different identifier for the same file uploaded twice, so duplication is invisible and the network stores the same content repeatedly

*Chainlink Fall 2022 Hackathon* · problem: two people uploading the same files got different identifiers and did not know

### [[encryption-pinner]] — Encryption Pinner
> content-addressed storage is public by construction, so anything sensitive has to be encrypted before it is pinned and there is no standard step for doing that

*Chainlink Spring 2022 Hackathon* · problem: IPFS is used in nearly every project and encrypting before pinning is manual
