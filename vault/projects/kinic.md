---
slug: "kinic"
url: "https://devpost.com/software/kinic"
title: "Kinic"
hackathon: "Supernova "
organization: "DFINITY Foundation"
winner: true
words: 1377
team_size: 1
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/measured_ablation"
  - "mechanism/revocation_withdrawal"
  - "mechanism/voice_speech"
  - "domain/security_privacy"
  - "user/general_public"
  - "substrate/code_repository"
  - "substrate/financial_record"
  - "substrate/video_visual"
---

# Kinic

> A search engine for web3.

[Devpost](https://devpost.com/software/kinic) · hackathon [[Supernova]]

## Facets

**mechanism** [[measured_ablation]] [[revocation_withdrawal]] [[voice_speech]]
**domain** [[security_privacy]]
**user** [[general_public]]
**substrate** [[code_repository]] [[financial_record]] [[video_visual]]

**stack** love, motoko, vue

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for kinic?

## Body

Kinic Logo Claiming a site for an SEO boost Auctions Sample Ad Space Samples Ad Space with Gif Inspiration Did you know web2 Search makes around $12 per user / per year? These massive profits mostly come from Ads. Reworded: this revenue comes from your data being packaged and utilized for secondary sale to advertisers. Most of the time we are completely unaware of this exchange in value. These products seem to be 'free' to use. But of course there is no such thing as a free lunch. Do any of these profits go to the content providers that you find? Sometimes.. Do you get a kickback if your search data results in more sales or insights for an advertiser? Almost never. Does it go into a pool to help promote apps and content that you enjoy? No. 'Search' can be done better with web3! It can be used for discovery and insights, spotlighting new applications, and aligning economic incentives that match the values of individual users. A quick look into what web3 is all about will have the reader amazed at the potential. But in summary, web1 was all about browsing and reading content. Web2 is about writing and sharing. Web3 is all of web1 and web2, plus ownership. The very content and data that you share or produce can be protected and monetized like never before. Indeed, web3 has many advantages for end-users and companies: better privacy, security and direct-to-user business models to name a few. What is web3? Web3 is ownership. Unfortunately web3 is still young! And like many other new technologies there exist a few barriers to entry that prevent a full and immediate transition. One major barrier being discoverability. Which leaves many saying: "I made my cool thing on web3. Now what?". Kinic is my answer to the problem of discoverability for web3 apps and content. I was inspired to build it because I was seeing content being made but having little chance of being discovered. Not because of quality, or variety of the content, but by the systems' of centralized gatekeepers. These systems are in the interest of the status-quo. The gatekeepers do not mind to care. "Nothing is more expensive than a closed mind, and a missed opportunity". - H. Jackson Brown, Jr Rather than trying to play the web2 'SEO game' with transcribers at boundary nodes or landing sites, we should create and support web3 specific SEO. 'Search' that can only be done with an advanced blockchain powering it. 'Search' that can help incentivize and power the very things people are searching for. In stark contrast to maintaining the "status-quo", we are inspired to build by the forward, positive progress, which we can now all discover in the new decentralized internet. Kinic has a high level of technicality and runs on the revolutionary Internet Computer blockchain. We deep dived into how this blockchain works to make content search possible, powerful, and concise. Moreover, we have Motoko code that allows for bidding and site claiming directly on-chain. In short, this submission represents lots of hacking and loads of fun /s 💻❤️ . We decided on May 13th to build Kinic in public. We did this to help inspire others and bring some spice to SUPERNOVA. (I strongly encourage others to do the same in future!) That's right! We had just an idea with a way to get it done, a badly designed MVP page, 0 followers and no traction at the start of SUPERNOVA. I wanted a full blown product-to-market match making experiment and I definitely got one with this 30 day sprint - Slept like 20 hours week-one out of excitement 🧟‍♂️ Kinic now has 1000+ followers, revenue #s and other strong KPIs, much better design and branding, and a more polished MVP. What it does Allows for content search on frontend canisters. A user can input text, categories or canister IDs to discover relevant content hosted on the IC. How we built it Search: We used traits of the IC discovered in the Rust source code to gather all canister IDs on subnets. By using other 'smart-code' we identify keywords for each app and app type. We then prioritize 'claimed sites' over WIP or staging sites, creating a new basis for web3 SEO. Frontend: The app is built using Vue.js. We A/B tested a few variants to find a simple and sleek design. Take a look at our images on Twitter to see the evolution. The name Kinic comes from the word kin from kinship, and IC from the Internet Computer. It is also an onomatopoeia for a click noise. Our design and logo have been derived from this using AI term matching and other methods. Ad Bids and Site Claiming: We use Motoko 👻 ❤️ We used the Ledger canister to allow for bidding on Ad categories. The highest bidder cannot revoke their bid. Other bidders can reclaim their bid, and bid again if they desire. After the auction closes (time based), the highest bid is decided as the winner and gets a two-week ad spot. The ads appear on category pages on the right side. They can be images, videos, or gifs and have links. Claiming sites is done by comparing the canister owner principal ID by what is given to us in a DFX command. Motoko does not have an 'info' method call yet, so we are forced to do this comparison with DFX for now. ( https://forum.dfinity.org/t/getting-a-canisters-controller-on-chain/7531 ) Challenges we ran into Oh boy. A lot of technical challenges like how do we iterate through canisters? What to do with all of these Wallet canisters? How to differentiate between phishing and other bad content vs legitimate apps? Accomplishments that we're proud of The community likes Kinic! We hope they love it as we build it out further :) https://twitter.com/kinic_app Many established teams Tweeted the first week of launch showing support. ✌️ Unsolicited demo video made for Kinic: https://www.youtube.com/watch?v=-qytoxhHyyA&feature=youtu.be ICOS uses Kinic as default search: https://twitter.com/icpcsnft/status/1529629378300239874 We tried a CrowdFund NFT and were the fastest sell out of all time. Our NFT is focused on providing visibility to new projects on the IC; if they use the perk of the NFT they get an SEO boost in their chosen category for one day. We are very proud to have made a useful product that is being enjoyed daily. What we learned I am a serial entrepreneur and technical founder. The first stage of product building, for me, is all about validating an idea. Kinic exceeded all of my expectations in this. We have learned the exact content deployed on the IC and have visualized the boundary line of the IC-verse. Now we are very keen to build Kinic and help web3 expand: with more features to incentives good content and apps on the IC! Kinic is like an ever increasing repulsive pressure, behaving as an opposite of gravity. A bit like nuclear fission in a ________ 💥 😉 What's next for Kinic? We have plans to index the inner contents of backend canisters. We are in a discussion with Nuance first.. but will create an automated way to get this done. We are building ways to incentives content on the IC! Why build, write, or upload, on web2 when you can profit more on web3? Help Dfinity Foundation beat the baddies, with an API to track malicious content or phishing sites on the IC; Comms channel already opened with relevant team. We have a blue sky of options but will focus our efforts on demonstrating web3's competitive advantages. (#1 Technically this could also be possible for NFTs or other backend canisters; Rather than asking "submit your app and code" we can index the public functions and assume the NFT standard used. NFT canister owners can then verify their code and get a "Verified" tag. This is in contrast to existing methods that require someone to pre-approve an NFT before listing.) Our WIP mantra: No more competitive advantages for web2. Or "Got web3 content?" ** Product video is unsolicited from the community. It does not contain code for auction or claiming sites. We are doing a thorough review of that code before pushing it to production. It can be viewed in our Github repository. ** <div