---
slug: "web3qr"
url: "https://devpost.com/software/web3qr"
title: "Web3QR"
hackathon: "Chainlink Spring 2022 Hackathon"
organization: "Chainlink Labs"
winner: true
words: 357
team_size: 0
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "substrate/web_dom"
---

# Web3QR

> Deploy static websites to IPFS and generate decentralized QR codes.

[Devpost](https://devpost.com/software/web3qr) · hackathon [[Chainlink Spring 2022 Hackathon]]

## Facets

**substrate** [[web_dom]]

**stack** ipfs, javascript, react, web3.storage

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for web3qr

## Body

Scanning web3QR app Inspiration QR Code is the easiest way to access information from your device. The idea was to build a decentralized tool that can deploy static websites to IPFS with just a single click and generate decentralized QR Codes , so that without any third-party paid centralized cloud services users can deploy their websites by using Web3QR. What it does Web3QR allows you to deploy static websites to IPFS in a single click by using web3.storage . After publishing the website, you'll get a decentralized QR code, IPFS CID, and hosted gateway link. ✅ Decentralized QR code ✅ Permanent storage ✅ Unlimited uploads ✅ Free to use ✅ User friendly How we built it After deploying the website to IPFS, web3.storage returns a CID Qmeq3NxNX624KHNjiWWbWTJHE64BQrXpMDqW4hVNs1WHrk , which is a hash for an array of files stored on IPFS, and that later is combined with the IPFS gateway link https://dweb.link/ipfs/ to access the website. Further, a QR Code is generated with the help of IPFS gateway link which later you can scan it. Tech stack Languages: JavaScript, HTML5, CSS3 Libraries: React.js, QR Code Tools: web3.storage Platforms: Netlify Challenges we ran into Uploading a directory with full tree of files (complete path) I'm using react.js for this project so using getFilesFromPath is not possible, because the browser does not allow us to read from our file system , getFilesFromPath is used in node.js. By using webkitdirectory in HTML and querySelector in JS, it does not upload the website directory with a full tree of files. Example:- It uploads files without their full path making the other directories inaccessible. Directory structure: /website (root directory) ./index.html ./css/style.css How it uploads /website (root directory) ./index.html ./style.css Solution to this problem is webkitRelativePath which can be implemented with vanilla javascript. Accomplishments that we're proud of I've managed to create what I planned for this hackathon ( i.e., learning, designing, coding, and launching the Web3QR). What we learned I learned a lot about IPFS and web.storage. What's next for Web3QR My goal is to build similar useful web3 infrastructure tools for the new decentralized internet on top of the IPFS protocol. <div