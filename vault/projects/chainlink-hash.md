---
slug: "chainlink-hash"
url: "https://devpost.com/software/chainlink-hash"
title: "Wiki IPFS"
hackathon: "Chainlink Fall 2022 Hackathon"
organization: "Chainlink Labs"
winner: true
words: 433
team_size: 2
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
---

# Wiki IPFS

> On-chain IPFS file search solution. With Wiki IPFS you can index IPFS files on Polygon Network, retrieve CID starting from pure file hash (avoiding duplicates) and connect DID with deployed CIDs.

[Devpost](https://devpost.com/software/chainlink-hash) · hackathon [[Chainlink Fall 2022 Hackathon]]

## Facets


**stack** amazon-web-services, bacalhau, chainlink, fargate, filecoin, lambda, polygon, quicknode, react, solidity, web3storage

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for wiki ipfs

## Body

Wiki IPFS Logo Inspiration While working on a large upload on IPFS (with 100s of files) a couple of weeks ago, when realized that another person did the same thing 2 days before. Our CIDs were different as the chunk-size to create them was different, but the file content was the same. We wanted to find a solution to allow a better indexing of IPFS content, and potentially to connect a DID to each file. What it does Wiki IPFS creates a bridge between an IPFS CID representing a file, it's sha-256 and a Decentralized Identity . In this way, a user can query the chain for an hash, to get one (or more) CIDs with the same content; or query for a CID and get which is the DID connected to (and so if the file comes from a trusted entity). How we built it We started by creating a Chainlink Oracle with External Adaptors , called by a smart contract (CIDMatcher.sol) used to store the connections between CIDs, hashes and DIDs. When a CID is published on CIDMatcher.sol, a request to a Chainlink job is triggered. Our backend (built using a Serverless AWS backend) triggers a Lambda function that downloads the file at the given CID, hashes the file and returns a pair of CID - hash. We built the UI using React, to simplify both the upload of files to IPFS (using web3.storage ) and the query of already indexed files. Finally we created a sample of how you can use this Wiki on a Bacalhau job , to check that the file processed by the job comes from a trusted source. Challenges we ran into Due to the latency of newly uploaded IPFS files, we had troubles running External Adaptors as sometimes we have to retry the get of the file due to IPFS 400 response. Bacalhau does not allow for internet calls inside their jobs, but they'll be soon enabled, according to their roadmap ( see https://github.com/filecoin-project/bacalhau/issues/856 ) Accomplishments that we're proud of Creating a fully Serverless Chainlink External adaptor Integrate our solution inside a Bacalhau solution Enable the possibility to integrate PolygonID (haven't done yet due to tme constrains) Better understanding of wagmi hooks to interact with wallet inside a React App What we learned How to efficiently use a Chainlink oracle with External Adaptors Deep understanding of IPFS object Links, and in general of how IPFS works What's next for Wiki IPFS Allow for the verification of IPFS directories with more than 1 file inside Integrate PolygonID or other DID services make the solution cross-chain <div