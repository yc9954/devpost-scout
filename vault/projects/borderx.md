---
slug: "borderx"
url: "https://devpost.com/software/borderx"
title: "BorderX.eu"
hackathon: "The European Commission's EUvsVirus Hackathon"
organization: "European Commission"
winner: true
words: 725
team_size: 4
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "domain/agriculture_food"
  - "domain/civic_government"
  - "domain/finance_payments"
  - "domain/immigration_refugee"
  - "domain/supply_logistics"
  - "domain/transportation"
  - "user/developer"
  - "user/general_public"
  - "substrate/code_repository"
  - "substrate/financial_record"
  - "substrate/web_dom"
---

# BorderX.eu

> A smart electronic declaration of priority transport service tailored to border crossing that enables shippers and border agencies to operate together seamlessly in times of COVID-19 crisis

[Devpost](https://devpost.com/software/borderx) · hackathon [[The European Commission-s EUvsVirus Hackathon]]

## Facets

**domain** [[agriculture_food]] [[civic_government]] [[finance_payments]] [[immigration_refugee]] [[supply_logistics]] [[transportation]]
**user** [[developer]] [[general_public]]
**substrate** [[code_repository]] [[financial_record]] [[web_dom]]

**stack** antd, axios, css, gitlab, heroku, hibernate, html, java, javascript, liquibase-(instead-of-flyway), maven, node.js, npm, postgresql

## How they structured the write-up

- the problem your project solves
- the solution you bring to the table (including technical details, architecture, tools used)
- what you have done during the weekend
- the solution’s impact to the crisis
- the necessities in order to continue the project
- the value of your solution(s) after the crisis
- the url to the prototype

## Body

The BorderX front end design The problem your project solves Closed inner-European borders during the COVID-19 pandemic are an unexpected disruption to existing supply chains that rely heavily on road transport. Currently, there is no system in place to prioritize shipments that are urgently needed. Therefore all transports need to be held at the border. We aim to change that. The solution you bring to the table (including technical details, architecture, tools used) We propose a system where carriers can declare the transport of priority goods and the borders they will cross. Governments can specify which goods should be prioritized, from medical supplies to livestock that cannot be in transit for long periods of time to shortages in their markets. They will then create priority lanes for transports that carry these goods. When a truck arrives at the border, the border agents will use the number plates to request information on the priority status. This includes the presence of a declaration as well as further possible signals to prove authenticity. The border agents can reduce their efforts to spot checks based on the server reply (pass, low risk, high risk), while important goods can reach their destination without further delays. In the background we have deployed a distributed ledger that takes care of sharing only the information that is required for the task with each party. The border agents will only get a reply for shipments that have declared to pass their country and only see the main signals. Government agencies will be able to provide pre-authentication to suppliers and carriers that prove to have sufficient auditing capabilities to prevent fraud. They will also be able to sanction carriers that commit fraud by adjusting signals. Auditing nodes will ensure the ability to follow up on shipments to reduce the risk of fraud further. We have set up our prototype with a Corda backend, because it’s enterprise blockchain architecture provides all features required for our product, both in the prototype as well as our future roadmap. The frontend is currently deployed as a web-app, which we intend to connect to an API that can automatically read number plates for border agents to use. Our solution is flexible and easy to deploy, due to the decentralized setup. Governments that want to take part can join without a long onboarding and preparation period, create guidelines for prioritized goods, provide tokens for their border agents, become auditors for shipments that concern their country and pre-authorize carriers. What you have done during the weekend We are a new team developed from the EUvsVirus hackathon, 5 engineers with avg. 13 years experience. We completed all deliverables within the 3 days. We developed the concept and product roadmap, a basic prototype network and nodes, a basic front-end and related material, e.g., website and video. The solution’s impact to the crisis Closed borders are a threat to both the principles of the EU and health and safety of citizens. Our solution helps reduce the negative consequences of such a heavy intervention by making sure that the most critical goods can pass the border in time to save lives. It can be deployed with very short notice and would be ready for potential closures from further waves of infections or other crises. The necessities in order to continue the project We would need support of the European Commision to support our product as a solution to improve the border situation and help us coordinate with member countries. We need the countries to join the network The value of your solution(s) after the crisis The solution can be applied directly to any situation where borders are closed, including any future crises and can be easily extended to include border to non-EU countries. It can also be adapted for crossings and corridors with limited capacity. It can both ensure that critical goods can cross easily, while other goods can trade their spot based on the economic value and urgency of the transport, thereby creating transparency and fairness in the process. Our network is suited to securely transport and access information in the process of transportation of goods and give governments the possibility to enforce rules on top of it in an automated way. This allows for new applications to be built on top of the network in the future. The URL to the prototype https://borderx.eu <div