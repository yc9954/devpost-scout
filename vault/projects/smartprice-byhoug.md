---
slug: "smartprice-byhoug"
url: "https://devpost.com/software/smartprice-byhoug"
title: "SmartPrice"
hackathon: "Chainlink Spring 2023 Hackathon"
organization: "Chainlink Labs"
winner: true
words: 756
team_size: 1
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
---

# SmartPrice

> SmartPrice is an inflation adjusted pricing service that uses inflation data to update the price of a given product or service.

[Devpost](https://devpost.com/software/smartprice-byhoug) · hackathon [[Chainlink Spring 2023 Hackathon]]

## Facets

  <sub>weak: video_visual</sub>

**stack** chainlink, hardhat, javascript, solidity, truflation, yarn

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for smartprice

## Body

frontend screenshot unit test passing 95% of lines covered in unit test Inspiration Inflation is not just a macroeconomic concept, it is a reality that every individual faces in their daily lives. When we observed the continuous rise in the cost of everyday commodities, the idea for SmartPrice was born. The concept was simple - to create a system that keeps up with inflation, ensuring that prices remain fair and sustainable. The rising cost of living is a significant concern for many people, especially in uncertain economic times. This sentiment of financial uncertainty and the very tangible impact of inflation on our everyday lives inspired us to develop SmartPrice. What it does SmartPrice is more than a simple pricing tool. It's a dynamic system that intelligently adapts to changing economic conditions. By utilizing a smart contract, SmartPrice takes a base price for a product or service and then updates it in accordance with real-world inflation data. This ensures that the prices remain accurate and fair, irrespective of inflationary pressures. SmartPrice doesn't just display prices but maintains their real value by constantly aligning them with the latest inflation data, making it a truly smart pricing tool. How we built it The development of SmartPrice required a mix of blockchain development skills, understanding of economic principles, and UI/UX design capabilities. We used the Hardhat environment for the development and testing of our Solidity smart contracts. This provided a robust and easy-to-use framework for building on the Ethereum blockchain. Package management and task running were handled by Yarn, allowing for an efficient and streamlined development process. The SmartPrice contract itself is written in Solidity, which was the ideal choice for creating complex financial logic on the blockchain. The integration of Chainlink oracles into our contract allowed for the use of real-world inflation data to adjust prices accurately. Challenges we ran into Developing SmartPrice was an exciting journey marked with unique challenges. One of the principal hurdles was understanding how to correctly implement inflation adjustments in a smart contract, a task that required extensive research into various economic models and principles. Integrating Chainlink Price Feeds was another considerable challenge we faced. The use of these decentralized oracle networks was critical for us to allow end-users to input dollar amounts easily rather than complex, large numbers in wei (the smallest denomination of ether), typical of Solidity contracts. This integration was necessary to create an intuitive and user-friendly experience, but it presented a significant technical obstacle. Furthermore, creating a robust, user-friendly frontend using Next.js and ensuring its seamless interaction with the blockchain presented its own set of complexities. Balancing usability and the inherent technical nature of a blockchain application was a challenge that we had to constantly address during development. Accomplishments that we're proud of We are proud of successfully developing a working smart contract that adjusts prices according to real-world inflation data. Our achievement lies in our understanding and application of economic concepts into a smart contract. Additionally, integrating Chainlink's real-world data into our contract was another accomplishment that we are delighted about. We're also proud of the user interface we built, which makes it easy for anyone to interact with the SmartPrice contract. What we learned In the process of building SmartPrice, we deepened our understanding of a range of technical skills. We developed an intricate understanding of Solidity and the Ethereum blockchain, with hands-on experience in creating and deploying smart contracts. Crucially, we learned how to integrate Chainlink's Oracles and their Automation services into our solution. These tools allowed us to inject real-world data into our smart contract and automate the updates based on the inflation rates. From a design perspective, we gained insights into best practices for user interface design and user experience to create an intuitive and engaging platform. What's next for SmartPrice As we look towards the future of SmartPrice, our aim is to refine and expand our current offering. We plan to integrate more data sources to provide a more accurate reflection of the inflation rate, not just in the U.S., but in other economies as well. This would allow us to adjust prices based on different fiat currencies, offering a truly global solution. Additionally, we aim to develop a more comprehensive front end, where users can set and view prices for multiple items. One of our most ambitious plans is to explore the implementation of predictive algorithms. These would forecast future inflation rates and automatically adjust prices accordingly, ensuring that prices set by our users remain sustainable and fair over a longer horizon. <div