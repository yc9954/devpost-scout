---
slug: "near-notification-service"
url: "https://devpost.com/software/near-notification-service"
title: "Near Notification Protocol"
hackathon: "NEAR MetaBUILD III Hackathon"
organization: "NEAR Protocol"
winner: true
words: 1256
team_size: 2
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "domain/developer_tools"
  - "user/general_public"
  - "substrate/financial_record"
---

# Near Notification Protocol

> We provide notification infrastructure for dapps which powers personalised interactions and on-chain notifications between dapps and their users.

[Devpost](https://devpost.com/software/near-notification-service) · hackathon [[NEAR MetaBUILD III Hackathon]]

## Facets

**mechanism** [[realtime_stream]]
**domain** [[developer_tools]]
  <sub>weak: transportation</sub>
**user** [[general_public]]
**substrate** [[financial_record]]

**stack** amazon-web-services, near-lake-framework, node.js, postgresql, prisma, rabbitmq, railway, react

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for near notification protocol
- note

## Body

How we help? Create custom notification templates for every event. Add multiple channels for sending notifications Send product updates directly through dashboard Users get in-dapp notifications Users can opt for multiple notification channels like telegram. Inspiration Near ecosystem has great tech working on the backend and is improving day in and day out in terms of user experience. But as we compare it to other ecosystems, Near still lags in terms of communication and user interactions. Dapps today don’t communicate with their users personally and users feel less engaged. Today web2 apps can’t imagine surviving without engaging in communication with users, so why don’t we bring the same user experience to what we think is the #future? But setting up the notification infrastructure even in the web2 world is a pretty complex task and requires tech resources and time. For dapps added to this complexity of making a scalable infrastructure is the complexity of handling & parsing events that comes from fetching node data and being in sync with the nodes. If all dapps go ahead to do all this on their own, they will have to go through rigorous tech work and spend a lot of resources & time, instead of doing what they do best. So we have decided to solve this problem for dapps by providing them with a scalable infrastructure for communicating with their users and enhancing the user experience for all users on Near Protocol. We aim to make users’ on-chain interactions more delightful and serve as a bridge of communication between dapps and their users. What it does Near Notification Protocol is an end-to-end notification architecture for dapps on Near Protocol and the only architecture that the dapps will ever need. For dapps to get onboarded to our infrastructure there is a dashboard exclusive for dapps, which is currently invite-only to serve the real customers with full responsibility. Currently, we allow dapps to send notifications to users through for in-app, telegram and email channels. We are working on bringing support for push notifications and web-hooks soon. We also provide support for protocols to integrate our notification SDK in their dapps to seamlessly onboard their users. The dashboard allows dapps to create multiple events either on-chain or off-chain. On-Chain Events: Since the transaction msgs for near are a bit complicated for users to understand, we are on a mission to build an open-sourced parser service to make on-chain messages human-readable. So we have two categories of on-chain alerts right now, generic notifications (default) and enhanced notifications (human-readable). - Enhanced Notifications: We currently support enhanced notifications for Ref Finance , Mintbase , Stader Labs , MetaPool , Linear Protocol and many more coming soon. Although we are focussing on supporting more protocols asap, we also allow protocols to raise PRs in our open-sourced parser service to support their dapps with enhanced notifications. - Generic Notifications: The protocols which we don’t support for enhanced notifications yet, can register on our dashboard to send their users generic notifications across multiple channels, which basically means users will be fed with the raw data that they see on explorers currently. Off-Chain Events: As of now, protocols engage with their users only through mass media platforms like Twitter or discord. Although they are a great medium to build communities, when we talk in terms of user experience, mass media does not engage a user more than personalised communication. What we saw in web2 over the past decade, was the high adoption of different notification channels to engage and onboard user. We want to bring the same UX on Near Protocol by allowing dapps to send users notifications about any product update , s* ecurity updates , **offers , **upcoming releases * etc via personalised mediums. Dapps can trigger these custom notifications through the dashboard or the public APIs. How we built it There are multiple components working together to provide a seemless notification infrastructure: Notification Backend: The backend is built in nodejs (typescript) with postgresql DB. It is responsible for providing highly scalable infrastructure for low-latency notifications. It manages the entire logic for sending notifications across multiple channels. It also manages user related services to provide better analytics for dapps to understand their user behaviour. Its also interacts with the parser service to get on-chain events and process them. Dashboard for protocols: We built the dashboard frontend in React.js(typescript). It allows dapps to easily get onboarded to our infrastructure without writing any code. It also provides them an interface to manage multiple events as well to send off-chain notifications. Notification UI Hooks for Dapps: We have built easy to integrate react-hooks(typescript) for dapps to easily integrate in-dapp notification services to their users. Parser Service: We used near-lake-framework to ingest the real-time block data from blockchain. We firstly came up with generic parser to support the generic notifications for all protocols. Then we went on researching into multiple protocols to provide enriched human readable notifications. All the parsed data is published to RabbitMQ queues for further processing. Challenges we ran into One of the major challenge was to setup enriched notification parser for multiple dapps, since we didn’t have prior exposure to some of the dapps we support now, it was difficult to analyse their data to setup rich message parsing for them. Although now with time, we have streamlined our process and now trying to automate the entire process as well. Another challenge was integrating with multiple notifications channels we had to support. We had to go through completely different setups of various providers. We would also like to acknowledge and appreciate of the Pagoda team for building an amazing “near-lake-framework”, without which it would have been really difficult to focus on building the enriched parser instead of setting up our nodes ourselves. Accomplishments that we're proud of We started working on this project from the last week of October, so we were always worried that we won’t be able to complete till the deadline, but we worked day in and day out to ship the end to end working POC that itself is quite performant. While working on this project for last 4 weeks, we now have developed a clear vision of what we want to build this project into and make this product a living standard for Near Ecosystem. What we learned We learnt a lot more about the internal data infrastructure of near blockchain while building the parsing service. Setting up scalable infrastructure. What's next for Near Notification Protocol The very first aim is to complete our infra setup and to start testing the product and demo its working to some major dapps in the ecosystem. The priority right now is to go live with some dapps asap and get their feedbacks. We are also working hard to make the entire onboarding procedure more seemless for dapps as well as to support push notifications and webhooks for mutiple more use-cases. We are also planning to integrate with major wallets in the ecosystem to make user’s experiences more delightful. Since we are building at the raw data infrastructure level, we also plan to provide enhanced data APIs for dapps. We have encountered this as a major problem across ecosystems for dapps to get started. With proper funding the team could continue to build, grow and bring more exciting developments to the Near Protocol. Note Since the dashboard is currently invite-only, any dapp who is interested to try our POC can book a slot at link . We would be really happy to assist you. <div