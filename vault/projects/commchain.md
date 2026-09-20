---
slug: "commchain"
url: "https://devpost.com/software/commchain"
title: "commchain"
hackathon: "One Trillion Agents Hackathon"
organization: "NEAR Protocol"
winner: true
words: 552
team_size: 1
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "mechanism/vision_ocr"
  - "domain/disaster_emergency"
  - "domain/finance_payments"
  - "domain/scientific_research"
  - "substrate/video_visual"
  - "substrate/web_dom"
---

# commchain

> Use blockchain and AI to enhance field operations - from military to search and rescue, large scale repairs, construction, humanitarian aid, disaster recovery and more.

[Devpost](https://devpost.com/software/commchain) · hackathon [[One Trillion Agents Hackathon]]

## Facets

**mechanism** [[realtime_stream]] [[vision_ocr]]
**domain** [[disaster_emergency]] [[finance_payments]] [[scientific_research]]
**substrate** [[video_visual]] [[web_dom]]

**stack** near, nearai, nextjs, python, typescript

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what's next for commchain

## Body

Main dashboard. Tasks on the left and completion events in the chat interface Log in screen Use case gallery Inspiration A recent study, Blockchain Applications in the Military Domain: A Systematic Review (2025), reviews 43 peer-reviewed papers that explore blockchain’s potential benefits for military operations. When combined with secure AI, these benefits include: Enhanced security and data integrity Automatic token-based operations and rewards Better overview and faster decision making Resilient decentralised infrastructure On the Ukrainian front lines today, while numerous operations are carried out, verifying their results remains challenging. For example, troops have sometimes been tasked with building fortifications that later turn out to be insufficient ( https://www.ft.com/content/18dd370b-e2cd-48c5-a182-4c21c5ae8870 ). This issue is compounded by various monetary incentives for task completion ( https://english.nv.ua/business/new-benefits-for-ukrainian-serviceman-in-2024-50432568.html ), which can increase the risk of collusion and corruption. Commchain uses blockchain to record commands (tasks) and allow soldiers to mark them as completed. Soldiers or operators would provide photo and video evidence, which is then verified by both AI and/or human reviewers. This system would give commanders a real-time overview of tokenized field operations and enable the prompt release of rewards and bounties for verified tasks. Goal is to use blockchain and secure AI execution to enhance high stakes, low trust operations that require precise accounting and rewards. For example wartime operations in conflict areas. For example a use-case where drone operators submit videos of successful strikes and recieve verification from AI to get bounty payouts in stablecoins—this concept was validated with a member of the Ukrainian army during the hackathon. The platform can be used to cater to many other use cases besides military that require complex task processing and automated accounting: Disaster recovery operations Humanitarian aid distribution Large scale public events Search and rescue missions Crowdsourced data collection Infrastructure and utility repairs What it does Commchain - communication system for the command chain Done in the MVP: Dashboard with list of tasks Users can open task and submit photo evidence Evidence is encrypted and uploaded to Storacha decentralized storage The encrypted completion is stored into custom smart-contract on Near blockchain Near-AI runs triggered by on-chain event decrypts the evidence (photo) conducts image recognition marks the task result as verified or rejected, or counts items on the photo (ai verification task is customizable) to decide if reward should be released stores result on blockchain How we built it Challenges we ran into I am using win environment so had to juggle wsl and python virtual environments which meant it was bit difficult to test and debug agent development. In the end I made 104 agent deployments to figure everything out (how to run async tools, write replys, messages, run completions etc etc) Used RSA encryption in the beginning but then realized we cant add python libraries to agents so I had to switch to nacl Accomplishments that we're proud of Everything works end to end! Although the test-case is narrow, it works. I like the flexible datamodel which allows separate template and AI verification prompt for each task type. Happy that when searching for teammates found great contacts with whom to hopefully continue the project and test in real life. What's next for commchain Seek funding and pilot projects. Blockchain is a natural fit for high stakes, low trust environments that require precise accounting and rewards! <div