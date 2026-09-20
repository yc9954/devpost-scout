---
slug: "eden-protocol-of-developer-dao"
url: "https://devpost.com/software/eden-protocol-of-developer-dao"
title: "Eden Protocol of Developer DAO"
hackathon: "Polygon BUIDL IT : Summer 2022"
organization: "Polygon"
winner: true
words: 1253
team_size: 5
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "domain/agriculture_food"
  - "domain/developer_tools"
  - "domain/supply_logistics"
  - "user/developer"
  - "user/small_business"
---

# Eden Protocol of Developer DAO

> Eden will be the world's opportunity protocol, providing a place where everyone can grow through work they love, thanks to our two-way person-project matching system.

[Devpost](https://devpost.com/software/eden-protocol-of-developer-dao) · hackathon [[Polygon BUIDL IT - Summer 2022]]

## Facets

**domain** [[agriculture_food]] [[developer_tools]] [[supply_logistics]]
**user** [[developer]] [[small_business]]

**stack** graphql, javascript, mongodb, neo4j, next.js, redux, solidity, tailwind

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for eden protocol of developer dao

## Body

Contributor Dashboard All projects Magic Application Champion Recruiting Dashboard Inspiration We’ve got one life. Let’s not waste it doing things we don’t love with people we don’t like. With 85% of people emotionally disengaged at work - seems like most of us are doing just that. Let’s create a better option. Let’s make work, work for us all. Imagine purpose & community being the key reasons people come together to learn, earn, connect & collaborate. What would an opportunity protocol that enables such a purpose & community-driven economy, look like? A simple idea with massive potential impact. We believe that DAOs hold the key to such a future of work. Nowadays, however, DAOs are held back overwhelming Discord channels, outdated Notion tables, and overflowing DMs that bury many great web3 opportunities. Pseudo-decentralized, mostly affinity-based coordination through calls between only the most dedicated people don't help to bring in new talent, and the harder it is for DAO members to connect, the harder it is for the DAO to attract, engage & retain talent. With growing participation equating to growing inaccessibility, the mission of each DAO risks failure… so we built a solution. Read more on why we're building this through our manifesto here What it does Eden (fka “Soil” in D_D) is our project/person matching tool/bot, which streamlines opportunity-finding on a DAO-wide scale. Its user experience aims to be effortless, yet delivering hyper-relevant, even life-changing, results. Eden’s combination of AI & community generated, on-chain reputation markers (such as endorsements, SBTs of community recognised achievements,...) ensures that the human element builds and drives the bot. The resulting matches are decentralized, autonomous & bottom-up, with results that web2 platforms such as Upwork, Fiverr, or LinkedIn could only dream of. By enabling frictionless person-project matching, engaging & retaining talent becomes organic. When people like their projects and work with people they admire they can do more. With this kind of ecosystem, any DAO can fulfill its mission, and any contributor can grow to their potential :)!! The growing freelance market would be the first to agree - “Life’s too short to work a job you hate with people you don’t like.. “ All of us at Eden believe that prioritizing values of purpose & community is the essence of building great things. That’s how we’re building a protocol that makes work, work for us all. How we built it For this hackathon specifically, we focussed on three things: 1) Allowing projects to be ownable on polygon. 2) Allowing users to mint Soul Bound Tokens for achievements they've accomplished throughout the community. 3) we made early explorations with a token. 1) We wrote a factory contract that mints an instance for each new project. In that project you have the champion, who is the owner + all the members own an NFT linked to that contract with specification of what their role was/is in the project. This functions as an on-chain CV with key information for our project/person matching algortihm. By allowing champions & members to own their project on-chain, they can port it to any other service that might want to use this information. 2) We wrote a factory contract that mints an instance for each Soul Bound Token contract. A third contract was written as a registry to keep track of all the instances. The idea is that when you get 50 endorsements for Front-End through Eden in Developer_DAO, you can then mint a SBT that says: "50 people endorsed me in D_D for Front-End. And this is something you can then take with you, on chain. This is also key information for project person matching as the minting won't be free & shows what you really care about yourself, as well. The logic for that is built outside of the contract as the contract simply checks if the requesting wallet is whitelisted. 3) we started exploring the complexities & tradeoffs of launching a token on polygon. Challenges we ran into What to prioritise first. We had many different ideas as to what we wanted to use polygon first and we found out about the hackathon quite late. We had to tradeoff impact & feasibility. The cases we ended up choosing were foundational for some of our even cooler ideas, such as self-owned projects being able to autonomously recruit by allocating an AI managed budget, allowing people to stake a certain amount of MATIC/... on eachothers' skills, making it possible for senior devs to lend credibility to junior devs they believe in in return for a percentage of the jobs juniors end up getting thanks to that credibility. Say for example I'm a junior ML engineer & you're a senior ML engineer. You can now stake X tokens on my ability to do great work as an ML engineer and in return you will get a percentage of the money I make on each ML job I get in the future. This gives the senior an incentive to spot talent early & this gives the talent an opportunity to get jobs they otherwise wouldn't be able to. When it came to the coding, we are lucky to be part of D_D where for each coding question we had, we had a couple of knowledgeable people to reach out to. Accomplishments that we're proud of 1) Everybody that's worked on this with us has comitted to keep on building, no matter what. 2) We had multiple DAO tooling startups reach out to us becasue they heard about what we were doing, purely through word of mouth. 3) The other day, we needed an extra frontender and we've become such a known project in D_D in such a short amount of time that we had 17 applications in one day to join the Eden team as a frontender. 4) The fact that we were able to combine releasing the alpha we built in D_D with what we built for this hackathon. What we learned 1) we learned about the relative complexities and tradeoffs of what it takes to deploy on chain 2) we also learned that there's actually more things that shouldn't be on chain & how to manage that 3) we learned that building the right thing is in the beginning more important than building it totally right 4) we learned that we freaking love polygon ;) - but seriously, polygon is one of the best chains to build on right now 5) we got a tad bit better at solidity :)) What's next for Eden Protocol of Developer DAO The team is growing & we will continue building Eden as the opportunity protocol we can see it become. There is no doubt about it for us that the way that will be achieved will be a combination of human & algorythm driven mechanics. We're looking into how we can achieve the human driven part through tokenomics & those on chain reputation markers. The algorithm part we've got a lot of really smart people for on our team. We believe that everything that's a platform today, will become a protocol tomorrow. Our aim is to build the protocol that offers an upgrade to the the upworks, fiverss, etc. of this world. Blockchains have enabled completely new paradigms to emerge. With the many challenges that our world faces, we need these new paradigms more than ever. For us, that starts with helping people find work they love at all times. Driven by the vision of a world where work works for all, we'll keep on BUIDLing. <div