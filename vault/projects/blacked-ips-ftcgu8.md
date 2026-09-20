---
slug: "blacked-ips-ftcgu8"
url: "https://devpost.com/software/blacked-ips-ftcgu8"
title: "Blacked IPs – Your Melody for a Secure Network"
hackathon: "Chainlink Spring 2023 Hackathon"
organization: "Chainlink Labs"
winner: true
words: 792
team_size: 1
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "domain/developer_tools"
  - "domain/transportation"
  - "user/developer"
  - "substrate/code_repository"
  - "substrate/structured_db"
---

# Blacked IPs – Your Melody for a Secure Network

> Blacked IPs: Like a melody for your network's security. Harnessing AI to identify and block bot traffic, our system offers harmony amidst cyber threats. Tune into safer online spaces.

[Devpost](https://devpost.com/software/blacked-ips-ftcgu8) · hackathon [[Chainlink Spring 2023 Hackathon]]

## Facets

**domain** [[developer_tools]] [[transportation]]
**user** [[developer]]
**substrate** [[code_repository]] [[structured_db]]

**stack** amazon-web-services, bigtable, bunnyshell, chainlink, kubernetes, material-tailwind, mongodb, opensearch, pangea, sagemaker, tailwind-material

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for blacked ips

## Body

dashboard visits Inspiration As the Black Eyed Peas revolutionized the music scene with a unique and approachable sound, we aimed to bring the same innovative spirit to cybersecurity. Recognizing that web traffic is increasingly swamped by bots, and that traditional IP-based countermeasures have been rendered inadequate due to VPNs and proxy servers, we developed a superior solution: Blacked IPs. The demo can be seen at https://client-blackedips.bunnyenv.com/ What it does Blacked IPs goes beyond IP-level identification, incorporating fingerprinting technology for an added layer of defense, making it more challenging for bots to emulate real user behavior. With the integration of AWS SageMaker's probability regression, Blacked IPs can accurately predict a bot's likelihood based on the frequency of IP changes, page visits, and intervals between visits. By mitigating bot traffic, Blacked IPs allows project managers to focus on legitimate users, enabling data-driven decisions without interference. Pangea 1) Checking Embargo, IP Reputation, Proxy and VPN to determine whether to black list he IP based on their potential bot abuse 2) We use Vault Encrypt to make sure we encrypt the Crypto Wallet Private Keys, so private Keys are never stored within the database 3) We used AuthN to do user sign up as well as password login How we built it Our application is built on a MERN stack ( MongoDB , Express.js, React.js, and Node.js), running on a Kubernetes cluster set up and managed using Bunnyshell . We leveraged Tensorflow to identify potential bots based on their IP addresses and proxy usage. We logged these activities using Google Bigtable and integrated this data with a Chainlink External Adapter. This offers users a transparent view of both the bot funnel and the real user funnel within the Web3 environment. Our solution is deployed via Bunnyshell on Kubernetes using TailWind-Material Pro for the front end, which can be accessed at: https://client-blackedips.bunnyenv.com/ during development. For initial security, we employ the open-source library 'isbot' to check if the user-agent is a bot. We then verify via SageMaker whether the fingerprint has been associated with multiple IPs in the last 24 hours. If it passes this test, we cross-check with Pangea for IP reputation and Embargo, checking VPN/Proxy and secure our own login. Only when these tests are passed do we return a safe verdict, allowing users to continue. We log each blocked attempt as well as successful attempt for audit purposes. As the project is open-sourced, we can also access information via Web3 Chainlink, which can be particularly useful in countries where our services may be specifically banned. We store private keys through Pangea's vault encrypt, so that private keys are never exposed in our database even if the database is breached. I hope this revision better suits your needs, let me know if there's anything else you'd like to add or change. Challenges we ran into We encountered technical challenges akin to those in music production. Developing a system capable of accurately differentiating between bot and real traffic was daunting. The hurdles of IP-switching bots and proxies added to the complexity. However, these challenges only encouraged us to devise a more robust solution. Accomplishments that we're proud of We take immense pride in how Blacked IPs not only efficiently blocks bots but also equips project managers with precise data. By eliminating the bot traffic noise, we've created a tool allowing managers to concentrate on what truly matters - their users. We've also secured the domain blackedips.com. What we learned This journey taught us that innovation often entails a fresh perspective on old issues. Moving away from conventional IP-based strategies and incorporating fingerprinting technology, we could engineer a more sophisticated bot-deterrent solution. What's next for Blacked IPS Our immediate next step for Blacked IPs is to open-source the project. We believe that cybersecurity is a collective effort and open-sourcing Blacked IPs allows us to tap into the collective wisdom of developers across the globe. We are keen to see how the community will contribute to the existing project, and excited to support its growth. Beyond simply open-sourcing, we aim to foster a community committed to cybersecurity. Through shared experiences, resources, and knowledge, we can improve upon Blacked IPs and extend its functionalities. Just as the Black Eyed Peas continue to evolve their music, we plan to consistently refine and augment Blacked IPs to meet the evolving cybersecurity landscape, together with the community we build. As the project is open-sourced, we will also work on enabling access to information via Web3 Chainlink, fostering interoperability, and decentralizing the access to the data. We see this as a vital step, particularly for regions where our services may face specific restrictions. In essence, our future steps will focus on community engagement, open collaboration, and continued innovation in the field of cybersecurity. <div