---
slug: "node-ops"
url: "https://devpost.com/software/node-ops"
title: "Node Ops"
hackathon: "Chainlink Spring 2022 Hackathon"
organization: "Chainlink Labs"
winner: true
words: 279
team_size: 3
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "domain/developer_tools"
  - "user/developer"
  - "user/educator_student"
---

# Node Ops

> Node Ops lets Chainlink developers run their Jobs on-demand. A developer can host their job on a blockchain of their choice with the click of a button.

[Devpost](https://devpost.com/software/node-ops) · hackathon [[Chainlink Spring 2022 Hackathon]]

## Facets

**domain** [[developer_tools]]
**user** [[developer]] [[educator_student]]

**stack** amazon-web-services, chainlink, cloudflare, digitalocean, laravel, php, typescript, vue

## How they structured the write-up

- inspiration
- what it does
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for node ops

## Body

Inspiration I created my first EA by following Patrick's tutorial. It left out an important part, how to deploy it as a job and connect it to our smart contract. The good people at LinkRiver helped out. They deployed on the Kovan testnet and it worked like a charm. But when we wanted it on Polygon's Mumbai testnet, LinkRiver deployed it there. Same went for the Fuji testnet. Whenever we need a change to the EA we had to go request LinkRiver to redeploy and they did it for free. That sparked the idea that if we're facing this problem then other people should be too. What it does Step 1: User deploys their EA and gives the details. Step 2: Chooses chains they are interested in Kovan / Mumbai / Fuji / All the above Step 3: We respond with Oracle ID and Job ID Challenges we ran into How the v2 toml job spec works and how we can automate the generation. Accomplishments that we're proud of We we believe we're bridging a real gap in the developer ecosystem. Developers won't have to depend on the goodness of the node operators' hearts. They can deploy, modify and pull down Chainlink jobs as they choose. What we learned The mysterious inner workings of running a chainlink node 🙂 What's next for Node Ops 1) Make it as easy as possible. 2) We want to create paid option. The first job deployment will be free for any user. The next ones will cost money. 3) A dashboard to monitor the flow of requests into the Chainlink node. 4) Able for node operators to register and manage their nodes. <div