---
slug: "coolfi"
url: "https://devpost.com/software/coolfi"
title: "CoolFi"
hackathon: "One Trillion Agents Hackathon"
organization: "NEAR Protocol"
winner: true
words: 735
team_size: 2
has_repo: true
has_live: true
has_video: false
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "mechanism/revocation_withdrawal"
  - "domain/developer_tools"
  - "substrate/code_repository"
  - "substrate/financial_record"
---

# CoolFi

> CoolFi simplifies crypto transactions with seamless swapping (intents), wallet insights, Twitter integration. Track trends, interact with CoolFi Chat Assistant, and even send Bitcoin via NEAR intents!

[Devpost](https://devpost.com/software/coolfi) · hackathon [[One Trillion Agents Hackathon]]

## Facets

**mechanism** [[realtime_stream]] [[revocation_withdrawal]]
  <sub>weak: provenance_signing</sub>
**domain** [[developer_tools]]
**substrate** [[code_repository]] [[financial_record]]

**stack** bitte, intent, javascript, near, nextjs, typescript

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for coolfi

## Body

CoolFi: What's cooler than being Cool. Working Swap on CoolFi Working Swap on CoolFi Working Swap with Bitcoin on CoolFi Example signature prompt on Bitte Playground Working Swap on X Inspiration The concept emerged from the rising trend of AI-driven agents and decentralized finance automation. We noticed that while many projects prioritize streamlining DeFi transactions, they often fall short in providing interactive and personalized user experiences. So to make it feel less overwhelming, we also added Twitter integration. That way, users get a sense of familiarity, making crypto feel a little less like the Wild West. And hence the bitcoin integration with near wallet. What it does CoolFi is your all-in-one platform for managing cryptocurrency transactions with ease. Here’s what you can do: Swap Crypto – Exchange tokens seamlessly, including cross-chain swaps using NEAR Intents. Bitcoin Transactions with NEAR Wallets – Easily send BTC using your NEAR wallet and swap using NEAR Intents. Twitter Integration – Follow and interact with crypto swaps (including BTC transactions) directly from X. CoolFi Chat Bot – Ask questions, get portfolio insights, check prices, and even initiate all transactions and swaps via chat. CoolFi simplifies crypto, making it more accessible, engaging, and user-friendly ! How we built it We combined cutting-edge web technologies with blockchain integrations to make CoolFi. Here's how we brought it to life: Integrating Near Intents: We started by building a functional implementation of NEAR Intents , enabling: Transfers Swaps Deposits Withdrawals Next, we integrated Bitte to create a working prototype of the app. We then expanded functionality by adding APIs to Bitte AI , including Bitcoin APIs and real-time market data retrieval. Once the core functionality was in place, we focused on designing and developing the UI for a seamless user experience. Finally, we tackled Twitter integration , which came with its own set of challenges—especially handling link encoding and decoding while ensuring everything worked smoothly. By combining all these, we made CoolFi a simple yet powerful crypto transaction platform that brings blockchain and social engagement together. Challenges we ran into Ensuring proper encoding and decoding of links while preserving data integrity was a major hurdle. Similar challenges arose when handling Bitcoin transactions , where we had to recreate transactions accurately to avoid errors. The * NEAR * ecosystem was highly fragmented, making it time-consuming to locate the necessary components. Even the documentation was spread out, requiring extra effort to piece everything together. Initially, understanding how Bitte AI worked was challenging—many processes seemed to happen magically , making debugging difficult. Training a model to predict future market trends was a completely new territory for us. With no prior experience in this field, we had to quickly learn data processing, feature engineering, and model tuning to get meaningful results. At first doing everything at the api and making the user sign by returning the payload seemed tough. But later we found out that making the perfect link for the user to sign was even bigger a hurdle. Accomplishments that we're proud of One accomplishment we are proud of would be integrating cross chain swap of near-intents while using Bitte AI The best thing we did was maybe integrating twitter in our app. It was really hard to make links for everything when every api modifies the link in some way. Integrating Bitcoin with near-intent also took a lot of effort as we again had to send the transaction payload back to the user for him to sign which we later relayed to the chain in another api by recreating the transaction. What we learned This hackathon pushed us to explore a lot of new areas. We dived deep into the codebase to truly understand how things worked. Debugging took countless late nights, sometimes over something as small as an extra encoding step. Most importantly, we learned to keep pushing forward —solutions often came when we were on the verge of giving up. What's next for CoolFi Smarter AI for Market Predictions Improving our crypto prediction model with more features, better tuning, and real-time adaptability . Exploring on-chain analytics to enhance trading insights. Enhancing Twitter & Social Trading Making CoolFi’s Twitter integration even smarter , allowing users to execute transactions directly through tweets. Adding community-driven insights —real-time trending discussions on crypto movements. Just a thing we missed out on above, it would be better to use Meteor Wallet than MyNearWallet for all intended functionalities to work well <div