---
slug: "verified-4vamju"
url: "https://devpost.com/software/verified-4vamju"
title: "VERIFIED"
hackathon: "Chainlink Spring 2022 Hackathon"
organization: "Chainlink Labs"
winner: true
words: 1140
team_size: 2
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/on_device_local"
  - "substrate/financial_record"
  - "substrate/web_dom"
---

# VERIFIED

> Your social media presence VERIFIED on-chain. Ensure trustworthy interactions in Web3 by choosing to link your wallet to your Web2 social media profiles.

[Devpost](https://devpost.com/software/verified-4vamju) · hackathon [[Chainlink Spring 2022 Hackathon]]

## Facets

**mechanism** [[on_device_local]]
**substrate** [[financial_record]] [[web_dom]]

**stack** browserless, chainlink, docker, dokku, ethers, node.js, remix, vrf, vuejs

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for verified

## Body

URL verification page Verifications report page Logo Inspiration VERIFIED comes from multiple observations: The certification process on social media is not accessible enough: Only a few persons can have their identity certified online, it is often only for the most famous personalities. The application processes are time-intensive and often require several applications. The anonymity of the blockchain can be a drawback: When it comes to certain financial transactions, having a certified identity of recipients allows for trusted financial transactions, which is rarely the case in wallet-to-wallet transfers. Financial scams are common: Scammers use social media use as a tool to usurp identity, create fake charities and use social engineering to steal money. For example, Elon Musk impersonators on Twitter scammed people out of nearly $2 million. In 2021, crypto related scams accounted for 64% of investment scams on social media (according to FTC reports: Social media a gold mine for scammers in 2021 | Federal Trade Commission, ftc.gov). The number of those scams increased to become 12 times higher than in 2020 and the amount of losses increased by nearly 1 000% to reach $14 billion (Chainalysis). What it does Considering this growing social issue, we developed a decentralised verification process that links Web3 wallets to Web2 social media profiles. It enables checking the social media accounts linked to a wallet before confidently sending funds. The verification process of the social accounts consists in: The user sends 0.2 LINK from his wallet for the verification process. He then chooses the social media account he wants to verify among the ones compatible with VERIFIED (to date: Twitter, Twitch, TikTok) and copy his social account personal page URL. A verification request is then created, including the following elements : the URL to verify, a CSS selector of an element in the HTML page that is only editable by the owner of the page (e.g. a description field) and a unique random string of numbers, the challenge. This uses the Verifiable Random Function service provided by Chainlink. The user inputs this verification code in the element mentioned above, on its social media account and saves the modification. He then launches the verification process . The contract initiates a request to an oracle connected to a Chainlink External Adapter with web-scraping functionality. This adapter will load the URL previously defined, an check the HTML page (and the mentioned element) for the challenge that was previously generated and stored in the contract. Upon validation, the web 3 wallet and the web 2 social media account are considered linked at this exact time. The process takes less than 3 minutes: 30s to add LINK (step1) 60s for the challenge to be generated (step 2) 20s to copy the challenge in the social media account page (step 3) 30s for the verification (step4) With VERIFIED, we empower people with a trustworthy technology to reduce crypto-related scams on social media. Other use cases that can be addressed with VERIFIED: Trusted charity fundraising creation by letting users create a wallet linked to the social media account for the cause of their choice. The wallet can then only be claimed by the social media account owner. It ensures that the money really goes to the intended beneficiary. Social media accounts aggregator. Seller identification on marketplaces. Additional or alternative verification solution to the existing ones made by social media (lengthy, troublesome, human made…). Metaverse land claiming How we built it We started with the external adapter, as we could not find any that would allow us to process javascript-enabled websites. We then set-up our own node so we can run the external adapter on it. We tackled a first version of the contract, starting by adding the VRF feature, then communication with our oracle node. At this point we could deploy the contract and verify a URL once per contract. The next step was to make this contract a "master contract" that anybody can call without having to deploy one themselves. It required contract storage, wallet management. The last contract feature we added was the possibility to get a report of verifications per address. Finally we built the web front-end, and added events on the contract-side to make the UI smoother. Challenges we ran into Having no previous blockchain experience, the hardest part was the novelty of the concepts, technologies and tools we had to start using. We also thought that there was an actual external adapter we could use on github but it turned out there was no javascript enabled, and we decided to code our own. Because we use a scraper to get data from websites, there were some times when the scraped content was not consistent (cookies validation page, random login walls) and it forced us to choose very carefully the websites that can be verified. Another drawback of the scraper running on a single node is to get flagged as a bot, and we took extra care making sure that our scraper will go undetected. One a more technical note, the node job spec written in TOML was very cryptic, and we took more time than expected on writing them for our node. Accomplishments that we're proud of First MVP in 3 weeks, from 0 web3 experience Building our own javascript enabled external adapter Expansion from 1 social account verification (Y Combinator, that was HTML only) to 3 of the main social platforms (Twitter, TikTok, Twitch). What we learned Web3 is not that hard & it's fun There is truly awesome technology out there (chainlink, ethers.js, metamask) Writing a simple smart contract is easy but making it production-ready is extremely hard What's next for VERIFIED About the technology: The charity fundraising use case we want to address quickly requires more development. In particular, for the creation of what we call “unclaimed wallets”. Those wallets could only be obtained by the owner of specific social media accounts and would be ideal to empower people to create fundraising for others in a safe and trusted way for donors. We will set-up one DAO to act as an authority on which verifications are valid at a given time, because the HTML code of social media websites changes and evolves which can compromise the verification. Consolidate code/contract audit Continue testing on a larger scale (more accounts, more oracles). Check what is the proportion of oracles that give the good response. Select a ratio of “positive responses given”/”total responses given” to ensure a success probability above a threshold to be defined. Resources that are required to launch the external adapter per node are very high when Browserless is run locally and need to be reduced. Social media accounts API implementation About the business: Seek grants at the regional and national level to continue development and kickstart business operations. Possible token creation for an ICO. BSC Address for prize transfer : 0x479Ff3699d7bD5D7434A311252c1D2de12305D1F <div