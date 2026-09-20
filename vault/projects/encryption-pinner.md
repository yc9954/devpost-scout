---
slug: "encryption-pinner"
url: "https://devpost.com/software/encryption-pinner"
title: "Encryption Pinner"
hackathon: "Chainlink Spring 2022 Hackathon"
organization: "Chainlink Labs"
winner: true
words: 561
team_size: 1
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "domain/civic_government"
  - "domain/developer_tools"
  - "user/developer"
  - "user/general_public"
  - "substrate/geospatial"
  - "substrate/web_dom"
---

# Encryption Pinner

> Encryption Pinner is a simple development tool, which allows users to encrypt their files with an encryption method of their choice, and then pin them to their personal/business Pinata gateway.

[Devpost](https://devpost.com/software/encryption-pinner) · hackathon [[Chainlink Spring 2022 Hackathon]]

## Facets

**domain** [[civic_government]] [[developer_tools]]
**user** [[developer]] [[general_public]]
**substrate** [[geospatial]] [[web_dom]]

**stack** javascript, jquery

## How they structured the write-up

- inspiration
- what it does
- who is it for
- how we built it
- accomplishments that we're proud of

## Body

Inspiration I have been involved in Web 3 hackathons since last year now, and have used IPFS for pretty much every project I have built. Whilst IPFS itself is an amazing technology, certain use cases require additional functionality which is not "out of the box" so to speak. Services like NFT.storage and Pinata have built layers upon the existing IPFS network, in order to offer developers additional needed functionality. Due to the public nature of the network, making IPFS hosted files private has only be possible via encrypting files prior to upload. Currently there does not seem to be any fast tools for developers to achieve this. Encryption Pinner does just that, by allowing users to keep a file private, whilst hosting it on the public IPFS network. Developers can experience all of the benefits of IPFS hosted content, whilst retaining the privacy similar to a centralised file storage system. We currently use Pinata's API for pinning our project files (we have a custom gateway), but this could conceivably be done using other methods (e.g NTF.storage), or directly to IPFS. What it does Encryption Pinner utilises Nodes "crypto" module for fast file encryption via the web browser. Users can choose between dozens of encryption methods, with a passcode of their choice. Upon encrypting a file, it will be pinned to Pinata using a custom Pinata gateway. From there, users can retrieve their encrypted files in the same way they would retrieve any other IPFS hosted content. The files can then be decrypted using the passcode the user entered initially. Who is it for Encryption Pinner is a simple tool made for developers who would like to easily host private data on IPFS. Why might a developer want to host something private on a public network? The IPFS network boasts numerous benefits, and has become the go to file storage system for NFT meta data. NFT assets which are perhaps reserved for holders or specific members of a community, may be encrypted using our service quickly and easily and hosted in the same way any other file might. In addition to this, I have heard of individuals making use of IPFS to host articles, news etc. Which is restricted in certain countries in order to bypass government censorship. Whilst it wouldn't be proper for me to encourage this one way or another, it did occur to me that encrypting such files could add an additional layer of security for such use cases. Users would need to distribute an passcode and ID as a pose to a URL, which is more discrete. There are of course additional reasons a dev may want to encrypt their IPFS hosted content, and these are likely to be the same reasons a user might choose to have their data backed up to a secure centralised cloud service. How we built it The technical side of this tool is fairly straightforward. The frontend is simply Vanilla HTML and some jQuery, responsible for forwarding uploaded files via our routes in order to undergo encryption. We make use of the Node.js "crypto" library and its broad range of ciphers in order to perform this encryption. Upon successful encryption, we make an Axios POST request to Pinata where we pin the encrypted file. Accomplishments that we're proud of Creating a simple easy to use tool which can benefit Web3 developers. <div