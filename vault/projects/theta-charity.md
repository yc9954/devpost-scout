---
slug: "theta-charity"
url: "https://devpost.com/software/theta-charity"
title: "Theta Charity"
hackathon: "Theta Network 2023 Hackathon"
organization: "Theta Labs"
winner: true
words: 1028
team_size: 3
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "domain/legal_justice"
  - "domain/transportation"
  - "substrate/document_pdf"
  - "substrate/financial_record"
  - "substrate/geospatial"
  - "substrate/web_dom"
---

# Theta Charity

> Theta-Charity is a Theta Network-based decentralized streaming platform where creators can create charity-based streams for social, environmental and economic causes.

[Devpost](https://devpost.com/software/theta-charity) · hackathon [[Theta Network 2023 Hackathon]]

## Facets

**mechanism** [[realtime_stream]]
**domain** [[legal_justice]] [[transportation]]
**substrate** [[document_pdf]] [[financial_record]] [[geospatial]] [[web_dom]]

**stack** theta

## How they structured the write-up

- test the product:
- requirements
- introduction and problem
- tech we use:
- theta network:
- theta video:
- theta scan:
- xmtp:
- cloud micro services:
- what comes next

## Body

Landing Page Stream example Streamer's platform NFT platform Main architecture Test the product: URL: https://theta-charity.com/ Requirements Use Theta Network Mainnet on Metamask Wallet! Get it on Metamask: https://metamask.io/ Setup Theta Network Mainnet on Metamask: https://docs.thetatoken.org/docs/web3-stack-metamask Introduction and problem NFTs have exploded into the world scene with huge valuations but most of it have been focusing on digital art-work. It is true that we have huge companies like the NBA with Top shots and now even Disney, Tiktok and Instagram ready for the taking of this growing market. Nevertheless there are few instances where there have been real disruptors in this space. Streaming and Esports have become huge and growing. According to Business Insider, it is expected to grow at a 9% CAGR up from 454 million in 2019 to 646 million in 2023. The esports audience will grow on pace to nearly double over a six-year period, as the 2017 audience stood at 335 million. Streaming is another monster, in Twitch only Traffic continued to grow, with 1.5 million broadcasters and 100 million monthly viewers in 2015, rising to 2.2 million broadcasters and 15 million daily viewers in 2018. Twitch broadcasters, perhaps most famously Ninja, have featured on the cover of ESPN. Esports tournaments have drawn hundreds of thousands of concurrent viewers, with millions of dollars in prize money funded partly through the huge audience on Twitch. They have made an estimated $2.3 billion revenue in 2020, primarily from subscriptions and IAP with its more than 9 million users and its 18.6 billion hours of content that was consumed on the platform in 2020. One of the aspects that has made it transcend is the ability for its audience to interact with games, like “clipping” videos, predictions in which the audience can vote and so forth. We think this is an element that is limiting the mass adoption of Theta.tv. This is a huge market that has been overlooked by NFT marketplaces...until now. Enter Theta Clips, an NFT marketplace and addon where streamers, creators, gamers and its audience can easily and quickly upload short videos of their best moments and turn them into NFTs. Solution Diagram: Tech we Use: Theta Network: All contracts in the project are actively used in the Theta Mainnet network. Pre-deploy wTheta Token Contract: 0xAf537FB7E4c77C97403De94Ce141b7EdB9F7fCf0 Charity Contract: 0xF120b928Af227ce3941333c7D0945731958257A6 NFT Contract: 0x1c212b56BE6a9C96F1744d9f3CdD44De588de16B Theta Video: We use the dashboard APIs to make requests for livestreams and videos on demand already on the theta video platform. https://docs.thetatoken.org/docs/theta-video-api-overview Theta Scan: We use these APIs to access the NFT balances of each account easily, since the RPC calls do not provide a function to obtain the balances. https://www.thetascan.io/document/ XMTP: Sign in for authentication to the private conversation. Send direct messages through a private chat. Get message history with the same account. AWS: EC2: EC2 virtual machine that runs all the microservices through Docker containers. ELB: Load balancer that provides system scalability and in turn allows us to use our domain and the ssl certificate on the web page. Route53: Hosting service that allows us to use our domain with AWS services. How it's built: Theta Network: All transactions they make on Theta Network Mainnet. In total the platform has 2 main interactions with the Theta Network. Donations from the native token to the main contract of the charity. NFT-based DRM content and NFT mint. NFT from collection: 0x1c212b56BE6a9C96F1744d9f3CdD44De588de16B NFT-based DRM content: Theta Video: All the streaming services and NFT-based DRM content were done through Theta Video. To manage Streamers, the profiles of each of the Streamers were created within the Theta Video dashboard, with which we were able to provide each Streamer with their keys to perform their Streams. Through Theta Video APIs it was possible for us to obtain if the Streamers were doing a Live, thanks to this the viewers could always be aware when a live stream is made. Theta Scan: Theta Scan APIs were used to easily obtain the NFT balances of the account that you connect from Metamask to the platform. XMTP: Because our app requires a reliable service to carry out a private chat, it was decided to include the XMTP Client to carry out private messages between donors. Cloud Micro Services: All the microservices that we use in the cloud are deployed through docker, in containers, to be able to easily deploy the platform in a virtual machine, in the case of AWS an EC2 machine, however the containers are agnostic to the platform, so you can run the project on any virtual machine in any cloud. Static Website Web and Chat WebSocket Server. For the deployment of the application, the Docker Compose container orchestrator was used since we had to reliably run the static web page container and the websocket for the application chat simultaneously. Route 53: This service provides us with the hosting of the web page, in order to be able to use it so that the domain https://theta-charity.com/ connects directly to our services deployed in EC2. Elastic Load Balancer: Finally, with all these services created, we use a Load Balancer to be able to use our website from Route53 together with its SSL certificate. What comes next Basically all the basic functions of the platform are live and on mainnet, but of course, the most important aspect is the social one. However, we can see in our roadmap several next steps. First would be to establish Partnerships by: Collaborating with charitable organizations and NGOs to establish partnerships and onboard them onto the platform. Also, create agreements and processes for verifying and approving charities to ensure they meet the platform's criteria. Secondly we would have to Develop Community and Marketing Strategies by creating a marketing plan to raise awareness about Theta-Charity and its unique value proposition and engaging with potential creators and viewers through social media, content marketing, influencer partnerships, and community events. Lastly as every social laform depends on their content creatos we would have to explore partnerships with influencers, content creators, and other platforms to expand the user base. Of course all this complying with legal and regulatory requirements specific to each jurisdiction, especially regarding charitable donations, financial transactions, and data privacy. References https://www.twitch.tv/creatorcamp/en/connect-and-engage/charity-streaming/ https://www.donordrive.com/charity-streaming/ https://www.youtube.com/watch?v=Hh4T4RuK1H8 <div