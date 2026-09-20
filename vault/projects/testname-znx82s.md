---
slug: "testname-znx82s"
url: "https://devpost.com/software/testname-znx82s"
title: "WeiGold"
hackathon: "Chainlink Fall Hackathon 2021"
organization: "Chainlink"
winner: true
words: 431
team_size: 1
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "domain/climate_energy"
  - "domain/developer_tools"
  - "domain/health_clinical"
  - "domain/immigration_refugee"
  - "user/developer"
  - "user/patient_family"
  - "substrate/web_dom"
---

# WeiGold

> Servo motor vending machine using Chainlink gold/silver/oil pricefeeds.

[Devpost](https://devpost.com/software/testname-znx82s) · hackathon [[Chainlink Fall Hackathon 2021]]

## Facets

**mechanism** [[realtime_stream]]
**domain** [[climate_energy]] [[developer_tools]] [[health_clinical]] [[immigration_refugee]]
**user** [[developer]] [[patient_family]]
**substrate** [[web_dom]]

**stack** bootstrap, chainlink, html, javascript, jquery, motors, raspberry-pi-4, solidity

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for weigold

## Body

Inspiration I remember seeing Cash4Gold ads when I was younger. Then, I heard the backlash from customers about unfair gold prices. Discovering Chainlink’s commodities pricefeed aggregator inspired me to make sure fair gold prices were being offered to customers. I love robotics, so this seemed like the perfect idea to make into a hardware vending machine project that communicates with blockchain smart contracts. What it does WeiGold ensures fair, transparent vending for physical gold, silver and oil based on Chainlink's commodities pricefeed aggregators. Final prices are based on a fee that scales Chainlink pricefeeds. Admins can easily withdraw funds, change servo states after refilling sold items, and changes fees. Fees are updated live to the user as well. These live updates on the FrontEnd are done by emitting smart contract events, while having web3.js subscribe to event emissions to call jQuery to update page elements. How we built it Blockchain wise, WeiGold is built on the Rinkeby testnet, which is based on the Ethereum blockchain. The smart contract is written in Solidity. Hardware wise, a Raspberry Pi 4, three S90 servos and a cardboard box were used. FrontEnd wise, HTML and Bootstrap displayed the site format. jQuery is used for displaying variable element data. Site hosting is done via Fleek (IPFS+Filecoin) for more reliability. Challenges we ran into Going solo for this project made it tough to push through difficult problems at times. However, being patient and working through these problems inspired me to push myself to learn as much as possible. I was struggling with making the website scale to mobile and desktop sizes particularly for "div" objects, but overcame this by brute forcing “min-height: vh”. Modifying colors in jQuery took time to research, but ended up working. Getting a website responsive like that was extremely satisfying. Accomplishments that we're proud of Building a fully functioning FrontEnd where it scaled responsively based on viewport height [vh]. I had tried doing this in the past, but the "div" objects would collide when I zoomed in or made the window resolution smaller. I love the site's minimalist style, along with the color selection and animations with blockchain updates using jQuery. What we learned Coming up with a locking mechanism for servo motors took trial and error, making improvisation very important. I tried making custom servo arms, but they kept falling apart. I ended up cutting the custom servo arm idea, and just made a latch on the cardboard slot door. What's next for WeiGold WeiGold hopes to inspire blockchain developers to integrate hardware with the blockchain to ensure more fair commerce. <div