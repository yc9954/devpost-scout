---
slug: "geovox"
url: "https://devpost.com/software/geovox"
title: "Geovox"
hackathon: "NEAR MetaBUILD III Hackathon"
organization: "NEAR Protocol"
winner: true
words: 747
team_size: 2
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "domain/developer_tools"
  - "user/developer"
  - "substrate/geospatial"
  - "substrate/structured_db"
  - "substrate/video_visual"
---

# Geovox

> Find and collect items while you travel. It's a real-world location app that lets you hunt for NFT items while you're out and about.

[Devpost](https://devpost.com/software/geovox) · hackathon [[NEAR MetaBUILD III Hackathon]]

## Facets

**domain** [[developer_tools]]
**user** [[developer]]
**substrate** [[geospatial]] [[structured_db]] [[video_visual]]

**stack** google-maps-sdk, ipfs, near-api-js, node.js, react-native, rust

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for geovox

## Body

Landing Page of application See which NFTs are available in the areas around. Popup collect NFT in the location User profile page, display your current level and list of your NFT NFT detail screen, see the metadata detail here Inspiration Travel restrictions have been an enormous problem during the pandemic covid, and people are desperate to escape the quarantines. However, these travel restrictions are being reduced as the pandemic continues to decline. As a result, people can now travel more easily than before. We can use this problem to gain more users by offering a way for people who love to travel to hunt and collect items while they are out and about. What it does Geovox is a new platform that allows users to hunt for wild NFTs while on the go. By making use of satellite and map location data, we can show you exactly where to go and what kind of NFTs you'll find there! When a user travels, they'll be able to see which NFTs are available in the areas around them. This approach will increase the utility of our NFTs by giving them more features and rewards in multiple locations across the globe. In addition, we believe this will make web2 users feel more comfortable using our platform because it will allow them to experience the web3 features without worrying about the web3 technicalities or feeling overwhelmed by them. This project aims to increase the utility and gamification of NFTs for web2 users and onboard new users by allowing them to hunt for NFTs while they travel. We also utilize gamification features by implementing user leveling within the application. How we built it After we came up with the idea, we tried implementing the minimal version of the app and how things should work on the technical side (API, database, framework, library, etc.). Along with that, the designer was making the User Interface (UI) of our application. The Mobile Application We built the application using expo (react native) since it will generate two apps for both platforms (iOS and Android). Also, it uses javascript, which offers easier integration with NEAR ecosystem and more versatility for web developers. For the map, we use the OG react native maps (android google maps and iOS maps). since it offers fast integration with minimum setup. Backend This is where all the logic in the app happens, from creating the NFT and mapping them to a certain location and features for users to mint the NFT in that location. Our backend will show the n nearest NFT based on the current user location. If the users are 10 meters away from the NFT, then they can mint the NFT. For the tech stack, we used node.js , mongodb , turf , and most importantly near-api-js Smart Contracts We custom-made the NFT contracts that already satisfy the current NFT standard (NEP-177) to match our needs. It was built using rust and deployed in nft.geovox.tesnet Challenges we ran into We don't find any NEAR wallet that the mobile app can integrate natively. All the NEAR wallets are currently web-based. We were circumstancing this by login and authorizing the users via our backend In the long run, preventing users from cheating is crucial, especially those with fake locations. Fortunately, there is a library that we can use to detect this behavior. We use IPFS to store our NFT image, and in some cases, the images load very slowly. We are planning to use the CDN to speed up the image load Accomplishments that we're proud of People love this idea, we tested it with some people, and they really liked this idea and gave constructive feedback to us After several weeks of research and proof of concept the idea. We started the development of the application only 15 days before the Metabuild deadline and finished on the 13th day. Currently, the app is being reviewed by apple to beta test for our users What we learned NEAR implementation was easy due to the familiarity of our developers in javascript alongside with near-api-js library. That's why our development time was really fast. We learn new interesting libraries on our tech stack to visualize and map the location data in our application. What's next for Geovox Onboard more non-web3 users to web3 ecosystem by using our application Collaboration with Launchpad or NFT projects to help them release NFT in a particular location. Mainnet release on the app store and google play <div