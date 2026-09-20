---
slug: "croplink"
url: "https://devpost.com/software/croplink"
title: "CropLink"
hackathon: "Chainlink Spring 2023 Hackathon"
organization: "Chainlink Labs"
winner: true
words: 613
team_size: 5
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "domain/agriculture_food"
  - "user/frontline_worker"
  - "substrate/financial_record"
  - "substrate/structured_db"
---

# CropLink

> CropLink revolutionizes produce sales, empowering farmers with secure and efficient transactions. Join us to streamline your selling process and achieve success in the agricultural industry.

[Devpost](https://devpost.com/software/croplink) · hackathon [[Chainlink Spring 2023 Hackathon]]

## Facets

**mechanism** [[realtime_stream]]
**domain** [[agriculture_food]]
**user** [[frontline_worker]]
**substrate** [[financial_record]] [[structured_db]]

**stack** amazon-web-services, chainlink, express.js, next, node.js, react, solidity, typescript

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for croplink

## Body

Inspiration CropLink, is inspired by the goal of revolutionizing the way farmers sell their produce. It aims to provide a decentralized platform where farmers can connect with registered sellers to facilitate fair and transparent transactions. What it does CropLink is an AgriTech Dapp (Decentralized Application) that allows farmers to list and add their produce for sale. They can provide details such as the name, quantity, and price of their produce. The platform leverages smart contracts and Chainlink oracles to ensure transparent transactions and mitigate risks associated with unpredictable weather conditions. CropLink uses Chainlink oracles to monitor weather patterns, including heavy rainfall, which could potentially damage the farmers' produce. Smart contracts written in Solidity automatically activate in such cases, allowing farmers to sell their crops to registered sellers securely. How we built it The project utilizes the following technologies and services: Frontend : This is the user interface where farmers and sellers interact with the Dapp. It can be a web-based interface. Sign in with metamask : Users can connect their accounts using a MetaMask. Backend : This is the server-side of the Dapp built using Express.js. AWS Dynamo DB : Dynamo DB for storing all user data and providing a highly scalable and flexible database for future updates AWS Lambda : Lambda for seamlessly hosting our external adapter which connects to the USDA API to provide real-time demand data of crops. AWS API Gateway : API Gateway exposes our Lambda as a RESTful API so the Chainlink Bridge can connect it to the Chainlink Oracle. CropLink smart contract : The smart contracts are written in Solidity. It includes the core logic of the Dapp, including functions for farmers to sell their produce, sellers to buy produce and automated price adjustments based on the weather conditions. Chainlink : The Chainlink is responsible for fetching external data, such as weather information or supply and demand data from USDA API. Accuweather : Accuweather is used for fetching weather conditions. Challenges we ran into One of the challenges faced during the development of CropLink was integrating the weather function and making it useful for farmers to interact with. The team had to ensure that the weather data provided by Chainlink and Accuweather was accurate and reliable. They also had to design the user interface in a way that farmers could easily access and interpret the weather information to make informed decisions about their produce. Accomplishments that we're proud of One of the notable accomplishments of the team was successfully integrating Chainlink and Accuweather into the CropLink platform. This integration allowed farmers to have real-time access to weather information, which played a crucial role in their decision-making process. By leveraging the power of oracles and external data sources, CropLink provided farmers with valuable insights into weather conditions that could potentially impact their produce. What we learned During the development of CropLink, the team learned how to work with decentralized oracles like Chainlink. They gained knowledge and experience in integrating external data sources into smart contracts and leveraging that data to enhance the functionality of the Dapp. This experience likely provided the team with a deeper understanding of blockchain technology and its potential applications in the agriculture sector. What's next for CropLink The future plans for CropLink include expanding its presence beyond the Sepolia testnet and deploying it on other blockchain networks. The goal is to make CropLink a global solution that caters to farmers worldwide, facilitating the entire process of selling their produce. By offering a decentralized platform with weather integration and transparent transactions, CropLink aims to provide farmers with a reliable and efficient way to connect with buyers and sell their produce in a global marketplace. <div