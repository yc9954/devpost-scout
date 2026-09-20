---
slug: "the-carbon-games-irl-in-real-life-bounty-hunt"
url: "https://devpost.com/software/the-carbon-games-irl-in-real-life-bounty-hunt"
title: "The Carbon Games - IRL (In Real Life) Bounty Hunt"
hackathon: "NEAR MetaBUILD III Hackathon"
organization: "NEAR Protocol"
winner: true
words: 1506
team_size: 2
has_repo: false
has_live: true
has_video: false
tags:
  - "project"
  - "mechanism/cross_origin_web"
  - "domain/civic_government"
  - "domain/developer_tools"
  - "domain/education"
  - "domain/finance_payments"
  - "user/developer"
  - "user/educator_student"
  - "user/general_public"
  - "substrate/document_pdf"
  - "substrate/financial_record"
  - "substrate/geospatial"
  - "substrate/web_dom"
---

# The Carbon Games - IRL (In Real Life) Bounty Hunt

> The world's first blockchain-enabled In-Real-Life (IRL) Bounty Hunt! An IRL bounty hunt is a live, interactive scavenger-style game in which players compete to reach a destination for rewards

[Devpost](https://devpost.com/software/the-carbon-games-irl-in-real-life-bounty-hunt) · hackathon [[NEAR MetaBUILD III Hackathon]]

## Facets

**mechanism** [[cross_origin_web]]
**domain** [[civic_government]] [[developer_tools]] [[education]] [[finance_payments]]
**user** [[developer]] [[educator_student]] [[general_public]]
**substrate** [[document_pdf]] [[financial_record]] [[geospatial]] [[web_dom]]

**stack** firebase, firestore, node.js, react, rust, typescript

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for the carbon games - irl (in real life) bounty hunt

## Body

Dashboard - Submit Event and Bounties Dashboard - Upgrade Plan Switch Account Role Sponsor Event Event Summary Claim Rewards Screen (Mobile App) Claim Rewards Screen (Mobile App) Inspiration We were inspired to build the IRL Bounty Hunt after COVID, to get people back into the real-world, making social interactions with other humans in the way it's been done for millennia - in-person, in-real-life (IRL)! Since the onset of the COVID-19 pandemic, many people have been spending much more time indoors than they usually would. Although there are signs that the pandemic is ending, people still spend a huge amount of time indoors leading to health issues. According to a study by the American Heart Association, adults who sit for more than 11 hours a day have a 40% higher risk of death from any cause compared to those who only sat for 4 hours a day. Fortunately, the rise of IRL bounty hunts has provided a fun and engaging way for people to get out of the house while still following safety measures. By organizing a game that requires players to explore different areas around their city or town, they can still get outside while also staying safe by avoiding large groups of people. This is a great way to stay active and get some much-needed fresh air! Our dashboard is the world's first blockchain-enabled IRL Bounty Hunt platform, allowing anyone, anywhere in the world to easily create a bounty-hunt for their city, campus, company, or event! What it does The IRL Bounty Hunt Platform has 2 parts to it: Part 1: Setting the bounty. Any user can log in to the IRL Bounty Hunt dashboard using his/her NEAR account. Once logged in, the user needs to upgrade his/her user account to the role of Event Manager. Once the user pays the fee in NEAR to upgrade the account, they are redirected back to the dashboard. The user can now submit an event through the dashboard. First, the user fills in information such as the name of the event, a short description, start and end dates, venue name, location, and more. Once the event is ready, the user clicks submit and approves the transaction on NEAR. Once the transaction is approved, the event is live and is visible on our carpooling app, which is currently available on the App Store and Play Store. The event manager can now add a bounty to the event! Here's how that works. First, the user finds the recently published event in the list of submitted events on the dashboard and clicks on it. The event manager can now set an initial bounty amount followed by a bounty type (for example, to be distributed among the top 100 players). Once published, any other user aligned with the event's success, such as a sponsor, can increase the bounty without the event manager's permission. Part 2: Claiming the bounty Players can only claim the bounty (i) through the mobile app and (ii) if they are physically present at the event. Each player checks-in through the app, and the rewards are automatically distributed at the end of the event, by the smart contract. How we built it For the dashboard: First we read the NEAR docs and looked at other projects out there to plan ahead with the frontend and backend tasks. Then we came up with the structure to integrate the dashboard to the whole project. Then we implemented the basic logic. Once we were happy with the logic we moved to UI optimization For the smart contracts: We reviewed the Near Documentation and cookbooks which were well written and helpful. For each feature, we first planned the structure of the smart contracts, and then using the documentations and cookbook alongside our experience with Rust, we implemented the planned structure flow. Challenges we ran into For the dashboard development: Keeping a seamless experience when moving the user between the dashboard and the NEAR transaction approval page. Shortage of test NEAR Not being able to approve multiple transaction at the same time. Securely signing in users For the smart contract development: Not very responsive developer community support. On the Near Discord dev-support group, there are a lot of fraudulent users. If a question is posted, no response comes from the main group. Some fraudulent users then send a DM pretending to be the admin and will ask for live account passphrases. The group needs to be better moderated and more active. Inability to deploy multiple contracts to a wallet account. We had to create new wallets or sub accounts. Setting up local development is more complicated when compared to some other blockchain protocols Smart contract panics on testnet when more than 6 methods are added to it. A few times the testnet was not fully-operational. Accomplishments that we're proud of For the dashboard: Created a secure way for users to sign in using only their NEAR wallets. Showing event details on the markers on the map even though there wasn’t a supported was to do it. For the smart contracts: We are proud of all the methods and features of the smart contract developed - from payment to event management. In general, scavenger hunts (or "bounty hunts" or "treasure hunts") are fun, but quite tedious to organize. We created an intuitive, user-friendly platform that uses the power of permissionless blockchains (NEAR) to both setup bounties and reward users with secure validation. Even non-crypto-native users can now easily follow our demo videos to setup their own local bounty hunts. What we learned We learnt a lot about securely moving around data on the browser. How to use the least amount of states to avoid unnecessary renders of the DOM Learnt how to document the code while working on it with typescript A deeper understanding of how smart contracts work on the NEAR protocol. Also a better understanding of the integration dynamics. What's next for The Carbon Games - IRL (In Real Life) Bounty Hunt We plan to use our IRL Bounty Hunt in the following use cases: Educational By incorporating educational elements into the game, such as trivia questions or historical facts, players can get a better understanding of the area they’re exploring while also having fun. This could be especially helpful for students who are looking to learn more about their local area or history in an engaging way. In addition to being educational, IRL bounty hunts also help players stay active and foster deeper connections with their friends and family. By working together to complete tasks, players can strengthen relationships while also learning more about the area they’re exploring. We plan to partner with a university to launch our first campus-wide bounty-hunt. Improve Citizen Engagement IRL bounty hunts can be used to improve citizen engagement by encouraging people to explore their city and learn more about their local area. Studies have shown that when citizens are more engaged in their community, they’re more likely to take part in social activities and help out with local projects such as clean ups or beautification projects. According to a study by the University of North Carolina, citizens who are more engaged in their community are also more likely to volunteer and participate in civic activities such as voting. The same study found that when citizens have higher levels of engagement, they’re 3 times more likely to vote than those with lower levels of engagement. By encouraging people to explore their city and learn more about their local area through IRL bounty hunts, it can help foster a greater sense of community and increase citizens’ engagement in their city or town. This can lead to a stronger sense of civic pride, as well as improved social, economic, and environmental conditions in the area. We plan to partner with the city of Lisbon to launch our first city-wide bounty-hunt. Improve Attendee Engagement at Events IRL bounty hunts can be a great way to improve attendee participation at events. By incorporating an element of fun and excitement into the event through IRL bounty hunts, it can encourage more people to take part in the festivities. Studies have found that when attendees are more engaged at events, they’re more likely to stay longer and more likely to remember the event in a positive light. One example of an event that successfully incorporated IRL bounty hunts is the University of Pennsylvania’s “Pennopoly” event. The “Pennopoly” event utilized IRL bounty hunts as part of their scavenger hunt game. Attendees were encouraged to explore the university’s campus and monuments in order to find clues, answer questions, and solve puzzles. This helped increase attendee engagement at the event as well as foster a sense of camaraderie among participants. In addition to improving attendee engagement, IRL bounty hunts can also provide great opportunities for networking and connecting with potential employers or business contacts. By encouraging attendees to explore the venue and network with one another, it can be a great way for them to find new connections that could help further their career goals. <div