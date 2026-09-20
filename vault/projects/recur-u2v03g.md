---
slug: "recur-u2v03g"
url: "https://devpost.com/software/recur-u2v03g"
title: "RECUR"
hackathon: "NEAR MetaBUILD III Hackathon"
organization: "NEAR Protocol"
winner: true
words: 795
team_size: 2
has_repo: true
has_live: true
has_video: false
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "domain/developer_tools"
  - "domain/finance_payments"
  - "domain/housing_homeless"
  - "user/small_business"
  - "substrate/financial_record"
  - "substrate/video_visual"
  - "substrate/web_dom"
---

# RECUR

> RECUR is a recurring payments management tool that is built to enable subscriptions in Web3. It applies lazy evaluation to optimise the gas cost.

[Devpost](https://devpost.com/software/recur-u2v03g) · hackathon [[NEAR MetaBUILD III Hackathon]]

## Facets

**mechanism** [[realtime_stream]]
**domain** [[developer_tools]] [[finance_payments]] [[housing_homeless]]
**user** [[small_business]]
**substrate** [[financial_record]] [[video_visual]] [[web_dom]]

**stack** near, react, rust, vite

## How they structured the write-up

- introduction
- inspiration
- features & functionality
- how we built it
- what's next for recur
- track of the project

## Body

Introduction RECUR is a recurring payment management tool that is built with a focus on enabling subscription service in Web 3. We built an easy-to-use tool to help implement recurring payment flow on chain between a service provider and a subscriber. The service provider can be a traditional business type with a subscription revenue model (SAAS, video streaming, gym membership etc). It can also be an individual content creator, community, or DAO project that incurring revenue through recurring membership payment. We applied Lazy Evaluation to calculate the total amount of the stream of payments. Fees dost not need to be transferred on chain repeatedly at each billing cycle. Instead, it will only be accurately calculated when payment collection is called. This approach minimises the number of transactions happened on-chain and optimises the gas cost. This innovation enables our users to create highly frequent payment plans (e.g. in second, minute) inexpensively, which is almost impossible in traditional world due to its high operation cost. We have also built a simple Web 3 community website and integrated it with our tool to enable subscription services on chain. Our project is NEAR-native and build in a decentralised way. We also have ambitious plans to apply our payment flow management solution to create more innovative use cases to promote the subscription economy in Web 3. Inspiration We believe that the subscription service market will profoundly benefit Web 3.0 adoption. Subscription economy has already seen significant success in the traditional Web 2 world. It not only improves user experience but also empowers people to create small business and get paid directly. Meanwhile, mainstream subscription product will simply not be possible without a recurring payment management system, such as gym membership, video/music subscription, AWS services etc. To bring subscription services into the Web3 world, an essential step is to build a recurring payment flow management function on chain. RECUR is built to fulfil this mission. We focus on building a highly efficient and easy to use recurring payment flow management tool to enable users to integrate subscription service into their Web 3 scenarios. Features & Functionality RECUR implements recurring payment flow on chain between a service provider and a subscriber. Subscriptions are recorded on chain and its status can be verified to serve as an access proof to a provider’s service. Service providers can create one or more plans with customisable details such as payment intervals, payment rate. Subscribers can sign themselves to one or more plans and can manage their payment deposit using our service. Incurred fees will be calculated and locked in real time and can be collected any time by the providers. Subscription status will be managed and updated automatically based on payment result. Our initial release supports the following features: Subscriptions state can be verified on chain. This enables a subscription to be used as proof for service entry, which opens unique Web 3 use cases. Customisable plan for fields such as billing period (minutes, hours, weeks, months), prices. It employs lazy evaluation to optimise the gas cost and enables micro subscription payments. This enables users to create plans with highly frequent billing pierid inexpensively (e.g. in minutes). Automatically manages recurring payments for all subscriptions without user’s manual intervention at the end of each payment cycle. A subscriber has full access to her withdraw-able deposit and can top-up her deposit to fund ongoing subscriptions. Subscriptions can be cancelled safely by the subscriber. Subscriptions can also be stopped by the provider if payment is not settled. We have also integrated our recurring payment management tool to a simple Web 3 community website to demonstrate the simplicity of adding subscriptions services in Web3 using our tool. Currently, our service enables NEAR token payment. How we built it RECUR consists of smart contracts implemented in RUST and a web app built with React. The service is currently deployed and workable on NEAR Testnet. What's next for RECUR We have designed more highly useful features and integration for our services which we plan to continue building beyond the hackathon. Part of the future features include: Support stable FT tokens for payment. Represent subscriptions as NFTs to enable more Web3 use cases, such as access control Open SDKs for projects to efficiently leverage our payment flow management functions. Integrate with existing projects to enable subscription services, such as gaming, SocialFi, DAO. The team also has plans to integrate RECUR into the award winning RentVerse Project to further help develop utility NFT rental market. Track of the project Our project is brand new and is built completely during the submission period. The idea, code base and demo app are all built within this time range. We believe our project has offered enough creativity and originality to be considered for the Native track. <div