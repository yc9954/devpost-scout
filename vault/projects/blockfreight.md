---
slug: "blockfreight"
url: "https://devpost.com/software/blockfreight"
title: "Blockfreight"
hackathon: "Chainlink Fall 2022 Hackathon"
organization: "Chainlink Labs"
winner: true
words: 515
team_size: 1
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "domain/supply_logistics"
  - "domain/transportation"
  - "substrate/document_pdf"
  - "substrate/financial_record"
  - "substrate/structured_db"
  - "substrate/video_visual"
---

# Blockfreight

> Blockfreight is an open blockchain product tracking platform for any parcel.

[Devpost](https://devpost.com/software/blockfreight) · hackathon [[Chainlink Fall 2022 Hackathon]]

## Facets

**domain** [[supply_logistics]] [[transportation]]
**substrate** [[document_pdf]] [[financial_record]] [[structured_db]] [[video_visual]]

**stack** chainlink, ethers, ipfs, metamask, polygon, react

## How they structured the write-up

- blockfreight

## Body

Blockfreight Home page Connecting wallet Creating a new parcel tracking contract Confirming deployment on Polygon Uploaded IPFS images IPFS-stored metadata Completed parcel record creation QR code that can be printed / pasted to any physical object, or linked directly View parcel history from the app Deployed FreightContract per item Printing QR code Emitted event from a recipient update event Updating a parcel location Live Chainlink API call from FreightContract Blockfreight Blockfreight is a blockchain product tracking platform for any parcel. Generates a unique blockchain-backed QR code that can either be presented or placed on the cargo of interest. Built for the Chainlink Fall 2022 hackathon. Demo video: https://youtu.be/1f7YgP_u_Qw Testnet link: Blockfreight Must be on Polygon testnet (Mumbai) for demo. Motivation Often excel spreadsheets that track the history of inventory and deliveries are shared via email, or stored in individual documents which can be harder to sync and maintain. For other vendors using software platforms (such as Flexport), much of the data is held centrally within those platforms, subject to custom terms and conditions, and modifiable by their internal teams. Also often need to have a formal app B2B subscription plan. Other common challenges that occur outside of platforms can include limitations from the non-universal nature of email (emails are private between sender and recipient), delays might not be accurately or consistently reported, and products might be lost. Using Polygon smart contracts, Blockfreight can: Enable an immutable, append-only, history of interactions with given parcels. Create a permission framework (optional) that enforces only certain wallets or user accounts can log events against a given item. Store the data in a transparent way for all parties, where no single party has to be the custodian of the data log. Perform low cost, high volume, and fast transactions. Once delivered/completed, the owner of the parcel can call the markCompleted contract method - the contract will no longer be able to be updated, but the record will be preserved on the Polygon blockchain and IPFS. Technologies used Polygon : Serves as the primary smart contract network for the Blockfreight application. Polygon enables fast and low cost smart contract transactions that make it easy to use Blockfreight in the field without heavy additional costs or time delays. Chainlink : Grab information from port and pull into the application. Uses an on-chain API call for reverse geolocation (via https://www.geoapify.com/reverse-geocoding-api ) to store the provided lat/lng as a formatted location. For example, a known location of a shipping warehouse can automatically be pulled and saved on the smart contract without having the user type anything. IPFS : Record keeping and storage. IPFS is used as the backend for the QR code scanning data lookup and enables uploading new images of the cargo at different checkpoints or if the status of the item has changed visibly during transit (ex: item experienced damage). Notes uploaded are also saved to the contract. Every completed freight update via the QR code emits a FreightEvent that gets indexed and appended to the parcel's contract. emit FreightEvent(_requestId, lastSender, lat, lng, notes, _location); Github here for full information: https://github.com/cbonoz/chainfa22 <div