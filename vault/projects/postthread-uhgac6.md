---
slug: "postthread-uhgac6"
url: "https://devpost.com/software/postthread-uhgac6"
title: "PostThread"
hackathon: "Polkadot Hackathon: North America Edition"
organization: "AngelHack"
winner: true
words: 1261
team_size: 2
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/on_device_local"
  - "domain/civic_government"
  - "domain/climate_energy"
  - "domain/developer_tools"
  - "domain/retail_commerce"
  - "user/developer"
  - "user/general_public"
  - "substrate/structured_db"
---

# PostThread

> PostThread is a web3 social media app that rewards it users instead of extracting from them. To do this we use blockchain economics that encourage users to post quality content and curate the platform

[Devpost](https://devpost.com/software/postthread-uhgac6) · hackathon [[Polkadot Hackathon- North America Edition]]

## Facets

**mechanism** [[on_device_local]]
**domain** [[civic_government]] [[climate_energy]] [[developer_tools]] [[retail_commerce]]
**user** [[developer]] [[general_public]]
**substrate** [[structured_db]]

**stack** amazon-web-services, crust, fastapi, netlify, next, polkadot, python, react, rust, substrate, swagger, tailwind

## How they structured the write-up

- live site
- inspiration
- what it does
- project liberty's social media parachain protocol (mrc)
- how we built it
- airdrop
- accomplishments that we're proud of
- what we learned
- what's next for postthread

## Body

frontpage userpage logo Live Site You can check out the site for yourself right now at PostThread.app . Feel free to create a username and make posts and comments. However, this is just a demo so all passwords are set to password no matter what you put in. If you would like to dive deeper into the backend you can also checkout the swagger docs for the REST api used by the frontend here Inspiration Social media is not in our best interest. We are the product and the service. Users create most of the content on these sites and are not rewarded appropriately. We also do not know how these algorithms work. Their loyalties lie with advertisers not with users and these misalign incentives led to the polarizing climate we live in. They want to keep you on the site as long as possible at any cost and have learned that playing with your emotions is the best way to do that. Blockchain technology has made it so we no longer have to live in this social media dystopia. The blockchain can be thought of as an open decentralized database, where users can have control and ownership of their data. We believe this will not only allow content creators to be paid more effectively and efficiently, but will open up a world of possibilities where you can actually chose the type of social media experience you want. You will have a say in what they do with your data and have control over how the media is presented to you. I consider the current state of social media to be a national emergency. The population is growing more polarized, angry and divisive everyday and it think it directly attributable to social media. We live in a new world of big data, which we haven't quite figured out how to navigate yet. Therefore, it opens up an opportunity for these large corporations to take advantage of us. Decentralization allows the people to take control back from the corporations and I think we have created the beginning of an application that can do just that. What it does PostThread is a social media app first and a crypto app second. We hide all the crypto aspects from the user as most people aren't interested in it, but we believe it is important they have the ability to control their data should they choose to. At any time a user can take control of their assets and tokens. Also, all data is stored publicly on the blockchain or hosted on IPFS, so it can not be abused by a centralized entity. We believe we can give the user more control in the future by encrypting the data and allowing the user to provide a key to those they wish to share the data with. Each day users are paid tokens depending on their user and social score. The user score is determined by their contributions to the site such as posting good content, curating the site by voting or linking to their web2 social media accounts. Their social score come strictly from who is following them. Using graph theory we can determine how important a user is in the overall social graph. Centralities are calculated and compared against all other users. Combining these two scores, I believe, results in a fair distribution of tokens each day and encourages users to contribute, curate and interact with the community. Project Liberty's Social Media Parachain Protocol (MRC) The developers at Project Liberty released the first version of their protocol just as the hackathon was starting, which gave us a great opportunity to be one of the first to work on it. Their goal is to create a protocol layer that is free from corporate control and gives power back to the user. We found their approach to be easy to use and powerful. It was very easy to start minting data to the blockchain and query the data afterwards. We think having a protocol layer is key to a prospering decentralized social media because any value PostThread creates can be captured by any other social media that comes after and vice versa. This adds competition and collaboration, which are always most beneficial to the consumer and user. We think this will promote open-source projects with users themselves contributing to the site. The best way to beat the billion dollar social media empire is to lean into the open, free and sharing economy of our users. How we built it The frontend was built using NextJS and Tailwinds for styling. The frontend calls a REST API, which was developed using the fastapi library and uses Swagger documentation for easy communication between my partner and I. The backend uses the substrate library to communicate with the MRC parachain built by the team at Project Liberty. This chain has not reached the testnet yet so it was deployed locally on a machine I own. Initially it was deployed to AWS, but the costs were too high. Using the Reddit API, the top 100 posts are pulled every hour and minted to the blockchain. The posts metadata is uploaded to IPFS with the hash being stored on chain. We also setup an SQLite database to access the data more easily from the API. This script also listens for new blocks and will add new data to the database, such as when a user mints a post through the UI. Airdrop We set it up where a user can input their Reddit username to check how many tokens have been airdropped to them based off of their Reddit karma. They can claim these tokens by posting about the airdrop on Reddit. We think this type of marketing can be an easy way to piggyback off of web2. Content creators have proven their value in web2 and now with our web3 app we can directly pay them to advertise for us and to come over to our app. Accomplishments that we're proud of We are proud of having a functioning site that any user can instantly use no matter if they come from a crypto background or not. We are also proud we were able to implement some of the economic ideas we had for the app like the daily rewards and airdrop. I think these are the key to attracting quality users which will lead to the exponential adoption of the platform we believe can happen. We have many more ideas for attracting quality users in the future as well. What we learned The first couple weeks of the hackathon were spent learning about Polkadot, Substrate and Rust as we were brand new to this space coming from developing Solidity apps. I now feel as though have a strong understanding of the Polkadot system and Substrate library. We transitioned halfway to doing everything through a python REST API using the python substrate library instead of handling everything through the frontend. I found this to be a massive advantage as python is much quicker to develop in. I think continuing with the REST API will lead to a very secure, fast and dependable application. What's next for PostThread We are looking to team up with the developers at Project Liberty, who built the parachain we used. We want to help deploy the parachain to the testnet and work with them to integrate with PostThread. We also will be applying to grants to with hopes to continue working on our social media site full time and potentially find others to work with. <div