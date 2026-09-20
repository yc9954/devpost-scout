---
slug: "evm-jty6dl"
url: "https://devpost.com/software/evm-jty6dl"
title: "EVm"
hackathon: "Hack the North 2022"
organization: "Techyon"
winner: true
words: 445
team_size: 2
has_repo: true
has_live: false
has_video: false
tags:
  - "project"
  - "mechanism/sensor_fusion"
  - "domain/developer_tools"
  - "domain/finance_payments"
  - "domain/housing_homeless"
  - "domain/transportation"
  - "substrate/financial_record"
  - "substrate/sensor_telemetry"
---

# EVm

> Accelerate the adoption of electric vehicles worldwide by contributing to a network of decentralized charging stations.

[Devpost](https://devpost.com/software/evm-jty6dl) · hackathon [[Hack the North 2022]]

## Facets

**mechanism** [[sensor_fusion]]
**domain** [[developer_tools]] [[finance_payments]] [[housing_homeless]] [[transportation]]
**substrate** [[financial_record]] [[sensor_telemetry]]

**stack** blockchain, ethereum, flask, hardhat, iot, javascript, python, raspberry-pi, react, solidity, tailwind, web3.0

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for evm

## Body

Inspiration As more and more people embrace the movement toward a greener future, there still remain many concerns surrounding the viability of electric vehicles. In order for complete adoption of these greener technologies, there must be incentives toward change and passionate communities. What it does EVm connects a network of electric vehicle owners and enables owners to rent their charging stations when they aren't needed. Facilitated by fast and trustless micropayments through the Ethereum blockchain, users can quickly identify nearby charging stations when batteries are running low. How we built it Using Solidity and the Hardhat framework, smart contracts were deployed to both a localhost environment and the Goerli testnet. A React front-end was created to interact with the smart contract in a simple and user-friendly way and enabled a connection to a metamask wallet. A Raspberry Pi interface was created to demonstrate a proof of concept for the interaction between the user, electric vehicle, and charging station. While the actual station would be commercially manufactured, this setup provides a clear understanding of the approach. The Raspberry Pi hosted a Flask server to wirelessly communicate data to the web-app. An LCD display conveys the useful metrics so the user can rest assured that their interaction is progressing smoothly. Challenges we ran into This was our first experience in the blockchain development space. Not only learning the syntax of Solidity, but gaining an understanding of the major underlying blockchain concepts made for a steep learning curve in little time. Configuration with Hardhat did not go smoothly and required a great deal of debugging. Integrating the hardware with the web-app and smart contracts through the Flask REST API required extensive testing and modification. Accomplishments that we're proud of Building our first dApp was a huge accomplishment in itself. Our ambition to connect two of the most rapidly emerging fields, IoT and Blockchain, sparked new creativity in areas that are still very complex and unknown. What we learned We not only learned how to write and deploy efficient smart contracts to the Ethereum network, but also saw how they can be integrated into user-friendly web-apps. Building EVm also provided us an opportunity to develop modular, low-level software by learning more about interrupt-driven design as well as various serial communication protocols. What's next for EVm We look forward to deploying the smart contracts on actual blockchain networks. To improve transaction times and minimize gas fees, layer 2 chains will be explored to host the project in the future. Extensive testing and refactoring will be done to augment the security and efficiency. Reaching out to industry leaders to make the product more viable will be essential for its adoption. <div