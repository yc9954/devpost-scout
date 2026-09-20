---
slug: "tron-security-dashkit"
url: "https://devpost.com/software/tron-security-dashkit"
title: "Tron Security Dashcam"
hackathon: "TRON Grand Hackathon 2022"
organization: "TRON DAO"
winner: true
words: 498
team_size: 2
has_repo: true
has_live: false
has_video: false
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "domain/finance_payments"
  - "domain/security_privacy"
  - "domain/supply_logistics"
  - "user/developer"
  - "user/researcher"
  - "substrate/structured_db"
  - "substrate/video_visual"
  - "substrate/web_dom"
---

# Tron Security Dashcam

> The Tron Security Dashcam is a start-of-the-art collection of risk dashboards that monitors fishy activity that happens on-chain, & also notifies Tron Security experts about what's happening in Web3.

[Devpost](https://devpost.com/software/tron-security-dashkit) · hackathon [[TRON Grand Hackathon 2022]]

## Facets

**mechanism** [[realtime_stream]]
**domain** [[finance_payments]] [[security_privacy]] [[supply_logistics]]
**user** [[developer]] [[researcher]]
**substrate** [[structured_db]] [[video_visual]] [[web_dom]]

**stack** dune-analytics, jupyter, python, sql, storj

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for tron security dashcam

## Body

Inspiration I'm a Web3 Security engineer and data scientist. Please check out my Web3 security company Rektify AI , we are building the future of decentralized blockchain security and have a weekly radio show every Saturday discussing security best practices and weekly hack recaps. I’ve picked up a lot of experience analyzing DeFi hacks in my former position as a head database engineer at a DeFi insurance firm and doing smart contract audits for Code4rena. Throughout my research and development, I learned that the dream of mass adoption is dependent upon blockchain education and security. Most of the vulnerabilities that pillage cryptocurrencies are not scams or rug pulls, it’s technical errors made apparent through smart contracts, servers, and central points of failure. As far as the Tron blockchain, I wanted to create a monitor for the protocol since it is susceptible to DDos and Dos due to its nature as a PoS protocol. What it does Monitors fishing activity on the blockchain, Tron bridges, and keeps inventory on holders to ensure the security of the network. The Tron Security Dashcam(TSD) is a web application that can be of use to the Tron foundation to prevent attacks from being deployed on the network. How we built it For the front-end we used javascript, html, css, and WebFlow to bring the stack together. Users are able to toggle the data visualizations at the bottom of the dashboard. For analysis and data visualizations we used Python. We also launched a STORJ instance to decentralize our data used for the web application. Challenges we ran into The biggest challenge was finding open-source relevant attack data provided by TRONSCAN. The toughest part was finding more intricate data that would contribute to the presence of a vulnerability. I’m sure if we were afforded this data the data products we created would be more dynamic and insightful. We were disappointed that we were able to use Covalent API because the Tron chain is not compatible with their platform but we were about to defeat that hurdle by creating an API Key. Accomplishments that we're proud of Plugging the back-end and front-end together Launching the web app Deploying the Tron API Tracking the growth of Tron holders What we learned TRONSCAN is very different from Etherscan. Typically with blockchain scanner systems with a plethora of raw data is a blockchain data scientist's greatest wish. However, the TRONSCAN allows access to download .csv files instantly as well as real-time images of on-chain event data. We also learned that creating a security product requires security and our ideas will be addressed in future work. What's next for Tron Security Dashcam In the future, we plan to make the bridge more dynamic and interoperable. We worked with the data that was open-source and was relevant to the potential that the Tron blockchain had to display a vulnerability. Also, increasing the number of dashboards from 4 to 16 would be a next step in making TSD a reliant product. <div