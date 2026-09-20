---
slug: "gptstore"
url: "https://devpost.com/software/gptstore"
title: "GPTStore"
hackathon: "Constellation: A Chainlink Hackathon"
organization: "Chainlink"
winner: true
words: 632
team_size: 2
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "domain/developer_tools"
  - "domain/housing_homeless"
  - "user/developer"
  - "user/general_public"
  - "substrate/code_repository"
  - "substrate/web_dom"
---

# GPTStore

> Create and train GPTs from any information source and earn tokens by renting your created GPTs as NFT Rentals EIP-4907 to others on a time-based access

[Devpost](https://devpost.com/software/gptstore) · hackathon [[Constellation- A Chainlink Hackathon]]

## Facets

**mechanism** [[realtime_stream]]
**domain** [[developer_tools]] [[housing_homeless]]
**user** [[developer]] [[general_public]]
**substrate** [[code_repository]] [[web_dom]]

**stack** chainlink, eip-4907, express.js, nextjs, openai, openai-assistants, solidity

## How they structured the write-up

- overview
- inspiration
- functionality
- monetization strategy
- why rental method?
- technology stack
- implementation details
- accomplishments
- future roadmap
- docs

## Body

Banner logo GPTStore - Powered by OpenAI Assistant Overview GPTStore is an innovative initiative that harnesses the power of OpenAI Assistant and NFT Rental(EIP-4907) to create a dynamic ecosystem for developers. The platform allows users to easily build and train AI Dev Advocates using the OpenAI Assistant, enabling them to share domain-specific knowledge seamlessly. Users can monetize their efforts by renting out their AI Dev Advocates as Rental NFTs, providing others with time-based access to these intelligent assistants. Inspiration The inspiration behind the AI Dev Advocate Platform lies in our collective aspiration to empower developers with effortless access to accurate and real-time information. Our vision is to establish a platform where developers can engage in meaningful conversations with AI Dev Advocates, facilitating a unique and effective way to explore and comprehend complex concepts. Traditional language models often fall short in rapidly evolving domains due to knowledge cutoffs. The AI Dev Advocate Platform aims to overcome these limitations by leveraging the OpenAI Assistant and Rental NFT EIP-4907, which excels in adapting to the dynamic nature of today's information landscape by Training. Functionality The GPTStore Platform streamlines the process of creating AI Dev Advocates. Users can input a knowledge URL, specify the number of pages for crawling and indexing, and customize details such as name, description, pricing, and logo. The generated AI Dev Advocates are then made available on the platform for others to rent as NFT Rentals. Renters gain access based on their rented time, and automated systems ensure access revocation when the rental period concludes. Monetization Strategy To sustain the AI Dev Advocate Platform and support the usage of the OpenAI Assistant, we have implemented a unique monetization strategy. Users generate revenue (AVX) by renting out their AI Dev Advocates as NFT Rentals. The funds generated through rentals are allocated to cover the costs of OpenAI keys, ensuring continuous access to the powerful OpenAI Assistant thereby serving as Tech For Good to both the public and the Users. Why Rental Method? The decision to adopt a rental method over traditional monthly subscriptions is driven by several factors: Fair Usage: The rental method ensures fair compensation for users based on the actual utilization of AI Dev Advocates. Users pay for the time they actively use the service, promoting fairness in pricing. Cost-Efficiency: Renting allows users with occasional or project-specific needs to access AI Dev Advocates without committing to a fixed monthly subscription. This flexibility caters to diverse user requirements, making the platform more accessible. Resource Optimization: By adopting a rental model, users can optimize resource allocation and costs based on their specific needs. This approach aligns with our commitment to providing a cost-effective and efficient solution for users. Technology Stack Next.js Express Solidity OpenAI Assistant Chainlink Automation Chainlink Price Feeds Rental NFT (EIP-4907) Implementation Details Chainlink Automation: it runs through the list of NFTs and check for the ones that has expired.It uses the EIP-4907 extension, which adds an expiration date to NFT ownership. This makes it possible for the user to pay for a certain amount of time, and it will expire automatically using the Chainlink Automation. Chainlink Price Feeds: Dynamic calculation of rent fees in AVAX/LINK to USD on-chain using Chainlink Price Feeds for accurate and real-time conversion rates. Accomplishments The GPTStore has successfully implemented core functionalities, including AI Dev Advocate creation, renting of NFTs (Rental NFTs), Chainlink automation, price feed integration for dynamic pricing. Future Roadmap As the AI Dev Advocate Platform evolves, our vision extends beyond the current capabilities. We plan to diversify by incorporating additional web3 protocols and other Knowledge Domains, creating a vibrant ecosystem where users can craft specialized AI Dev Advocates tailored to distinct knowledge domains. The roadmap envisions a dynamic platform, fostering a community-driven marketplace for knowledge-sharing through rented AI Dev Advocates. Docs Documentation <div