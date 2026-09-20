---
slug: "hyper-updates"
url: "https://devpost.com/software/hyper-updates"
title: "Hyper Updates"
hackathon: "Constellation: A Chainlink Hackathon"
organization: "Chainlink"
winner: true
words: 618
team_size: 2
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/provenance_signing"
  - "mechanism/sensor_fusion"
  - "domain/developer_tools"
  - "substrate/financial_record"
  - "substrate/web_dom"
---

# Hyper Updates

> Secure your updates today with blockchain based immutable and Decentralised software updates!

[Devpost](https://devpost.com/software/hyper-updates) · hackathon [[Constellation- A Chainlink Hackathon]]

## Facets

**mechanism** [[provenance_signing]] [[sensor_fusion]]
**domain** [[developer_tools]]
**substrate** [[financial_record]] [[web_dom]]

**stack** go, hypersdk, nextjs, typescript

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for hyper updates

## Body

Postman Req Inspiration In response to the imperative need for secure and tamper-proof software updates, the inspiration behind this project lies in harnessing blockchain technology, specifically utilizing Avalanche HyperSDK to establish a private blockchain network. This system seeks to redefine software update management by ensuring transparency and decentralization. Tailored for IoT devices like ESP32 and Arduino, a custom library empowers devices to autonomously fetch updates from the blockchain while rigorously verifying integrity through recorded hashes. Integrated with IPFS, the project provides decentralized and immutable storage for software files. The vision extends to efficient update distribution, eliminating central points of failure through the Updates CLI as a secure vendor service. Beyond technical intricacies, the initiative embraces community-driven development, positioning itself at the forefront of innovation, trust, and transparency in software delivery. What it does We have created a firmware/software store and update system by creating a private blockchain Hyper Updates VM we created using Avalanche HyperSDK, and implemented a custom OTA(over the air) firmware updates library for ESP32 and Arduino devices. We implemented a vendor service(Updates CLI) which pushes updates to the Hyper Updates VM and simultaneously it creates MQTT call with transaction id to the IOT device then the IOT device can pull the updates from Hyper Updates VM. This works by uploading tlhe firmware binary to IPFS and creating a transaction which stores the data of the update name, version, firmware binary hash and IPFS URL of the binary. This info is then pulled by the IOT device through the transaction ID thus updating to the latest version of the firmware. How we built it We used Avalanche Hyper SDK to implement the Hyper Updates Hyper Updates VM which stores the data of the updates and the projects. Used Elegant OTA and MQTT libraries to implement the HyperOTA library which can query the chain using rpc or http calls. Used Next js to create the Vendor service UI which create updates by querying the rpc endpoints of the VM Challenges we ran into Integrating the ESP32 with the Hyper Updates Vm for Successfull OTA Updates was challenging, Additionally implementing the VM such that it supports chain calls without a wallet. This was done by creating an option of custodial wallets in the Hyper updates VM's CLI which exposes http endpoints and it will handle all the transaction signing. Accomplishments that we're proud of Implementing library for Hyper Vm IOT devices which calls the Updates-cli to verify updates and revert back to previous updated when validation failed was a challenging part since 1 bit flip can change the whole hash so we had to make sure the pulling of update is error free. What we learned We learned the integral parts of HyperSDK, how the actions are called and how the state is logged to the ledger storage. It made it more clear that how blockchains and the VM's work at the Node level. We also learned how we can leverage HyperSDK to easily create hyper fast and scalable VM's What's next for Hyper Updates Our recent prototype is just the tip of the iceberg, promising groundbreaking advancements in the firmware distribution sector. The focus is on enhancing system security significantly, and this is only the beginning. What's in Store: 1️⃣ Subnet Integration: We're introducing a robust subnet system where organizations can run their subnets independently. All these subnets will seamlessly connect through Avalanche, creating a network that facilitates easy communication and updates. 2️⃣ Effortless Updates: Forget the hassle of navigating various websites for updates! With our solution, once connected to a subnet, you can effortlessly pull updates using unique transactions. This streamlined process simplifies firmware distribution, eliminating the need to visit third-party sites for software updates. <div