---
slug: "red-env"
url: "https://devpost.com/software/red-env"
title: "greenscreen"
hackathon: "Constellation: A Chainlink Hackathon"
organization: "Chainlink"
winner: true
words: 406
team_size: 2
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "mechanism/sensor_fusion"
  - "domain/climate_energy"
  - "domain/finance_payments"
  - "domain/transportation"
  - "substrate/sensor_telemetry"
---

# greenscreen

> Revolutionizing carbon emission tracking with IoT and blockchain. We measure vehicle emissions in real-time, and balance emissions on-chain with RED tokens. Join our journey towards a greener planet

[Devpost](https://devpost.com/software/red-env) · hackathon [[Constellation- A Chainlink Hackathon]]

## Facets

**mechanism** [[realtime_stream]] [[sensor_fusion]]
**domain** [[climate_energy]] [[finance_payments]] [[transportation]]
**substrate** [[sensor_telemetry]]

**stack** c++, daisyui, express.js, hardhat, javascript, next.js, ngrok, platformio, react.js, remix, solidity

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for greenscreen

## Body

Inspiration Our journey with greenscreen began from a crucial observation: the environmental sector's lack of tangible data and real accountability in carbon emissions tracking. Witnessing the inefficiencies in carbon credit platforms, where emissions couldn't be accurately quantified, we were driven to create a solution. This gap highlighted the need for a system that not only tracks emissions in real-time but also holds emitters accountable. What it does greenscreen represents a significant leap in environmental monitoring. By harnessing IoT technology, specifically advanced sensors like MQ135 and SHT10, it provides accurate, real-time data on vehicle emissions. This data is then securely logged onto the Ethereum blockchain, ensuring both transparency and security. Our system innovates with RED tokens, which embody 'environmental debt', making emissions tangible and tradeable, while complementing existing GREEN tokens in carbon credit markets. How we built it The construction of greenscreen was a meticulous process of integrating IoT with blockchain technology. We utilized the MQ135 sensor alongside a dedicated temperature and moisture module (SHT10) for enhanced accuracy. The ESP32 microcontroller was key in processing sensor data. Our integration with Chainlink's CCIP allowed secure data fetching onto the blockchain and facilitated cross-chain minting. The use of C++, JavaScript, Solidity, and NextJs+ReactJS were instrumental in building a robust and user-friendly system. Challenges we ran into Throughout the development, we faced challenges in ensuring precise data collection from the IoT sensors and integrating this data with the blockchain in a cost-effective way. Overcoming these obstacles required innovative engineering and persistent testing. Accomplishments that we're proud of We're particularly proud of creating a system that blends IoT with blockchain in a novel way. The RED token, representing 'environmental debt', is a unique concept, fostering accountability. We could make one very simple to operate and use hardware and software interface with the help of Chainlink Functions, which not only allowed us to fetch off-chain IoT data but also allowed to compute over it that too in a familiar manner using JavaScript What we learned This project deepened our understanding of IoT sensor technology, blockchain interoperability, and the intricacies of environmental data management. It also provided valuable insights into token economics and the practical challenges of applying technology for environmental impact. What's next for greenscreen Looking forward, we aim to scale greenscreen for broader impact. Our goals include improving public conscience towards tracking accuracy and expanding the token ecosystem to facilitate a more comprehensive approach to carbon emission management and offsetting. <div