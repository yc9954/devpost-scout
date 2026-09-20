---
slug: "payment-for-supply-chain-transparency"
url: "https://devpost.com/software/payment-for-supply-chain-transparency"
title: "Digital Payments for Transparency and Fair Supply Chains"
hackathon: "Square Developer Hackathon 2023 "
organization: "Square"
winner: true
words: 1353
team_size: 3
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "domain/agriculture_food"
  - "domain/finance_payments"
  - "domain/labor_employment"
  - "domain/supply_logistics"
  - "user/frontline_worker"
  - "user/general_public"
  - "substrate/financial_record"
  - "substrate/structured_db"
---

# Digital Payments for Transparency and Fair Supply Chains

> We add Square as the payment layer to the open source supply chain traceability software INAtrace. With digital payments we can create transparency which benefits stakeholders around the globe.

[Devpost](https://devpost.com/software/payment-for-supply-chain-transparency) · hackathon [[Square Developer Hackathon 2023]]

## Facets

**domain** [[agriculture_food]] [[finance_payments]] [[labor_employment]] [[supply_logistics]]
**user** [[frontline_worker]] [[general_public]]
**substrate** [[financial_record]] [[structured_db]]

**stack** next, postgresql, prisma, react, square, vercel

## How they structured the write-up

- in three sentences
- motivation & inspiration
- context: inatrace
- problem
- idea
- what we’ve build for this hackathon and what it does
- benefits for all stakeholders in the supply chain
- how we build it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what comes next?

## Body

Title of our application: Digital Payments for Transparency and Fair Supply Chains The problem: Intransparency, especially due to cash transaction in the supply chain The solution idea: Enable the farmers like Martha to use Square to handle payments digitally, traceable. Solution part 1: Martha can create a QR code for the order of her beans, Pedro can scan this code and process the payment Solution part 2: Martha sees the data of the sell in her history, Pedro gets a confirmation Digital Payments for Transparency and Fair Supply Chains In three sentences We developed a prototype that enables coffee farmers to sell their harvest with a digital payment to the roastery. The digital payment increases transparency in the supply chain which is important for social sustainability. Square APIs helped us to build an easy-to-use application without barriers for the target group. Motivation & Inspiration We are from the German team atlat. Our vision is to build software that improves the conditions of workers who are part of supply chains in the global south. One major problem is lacking transparency in supply chains. Currently we are working on projects that involve agricultural goods such as mangoes and coffee, for example from Ecuador. The lacking transparency makes it challenging for companies here in Germany to ensure the ecological and social sustainability of their product. Context: INAtrace One possible solution is the open-source software INAtrace . INAtrace is a tool that helps to make an agriculture supply chain digitally traceable. It focuses on the tracking of quantities of raw materials to understand from the farm over the processing site, the retailer to the end consumer how goods are traded. This is e.g., important for organic certifications. Furthermore, INAtrace allows it for the retailers easily to share the information about the origin of a good with the end consumer. To clarify: We are currently working with INAtrace, but we did not develop it. What we present for this hackathon in regard to INAtrace are mock-ups of how we could integrate it as part of a project. INAtrace is mainly developed by the GIZ, which is a goverment funded agency for international collaboration in Germany. We are motivated to contribute to their open source project, since the software can reach a huge scale and positively impact the lifes of many. Problem The data about the transaction between the processing site (e.g. a coffee roastery) and a farmer is so far not reliable. The transactions are based on cash and later entered manually by the roastery into INAtrace without any proper proof. However, the integrity of the data is crucial. The price per kg of the raw material determines if the farmer gets paid a so called “living wage”. This means, that they not just barely survive, but can live in dignity for their hard work. Idea Let’s empower farmers to get paid by their harvest not in cash, but with a digital payment. Smartphones are on the rise also in developing countries like Ecuador and often the first digital device. Hence, we need to build a mobile first WebApp. The digital receipt can than be integrated in INAtrace as a proof of the transaction. What we’ve build for this hackathon and what it does We built a WebApp that allows it for the coffee farmers to easily set up a location via Square. They can enter their current goods, like coffee beans or mangoes, in their inventory. They can also set the price per kg for their goods in the inventory. When they meet the manager from the roastery to sell their beans, they can then use the payment section of the WebApp. They enter the amount in kg they want to sell. The WebApp generates a QR-Code. The manager of the processing site can scan this QR code and choose one of the available payment options like Apple or Google Pay and credit card. The farmer can see the transaction in the sales section of the WebApp. The manager from the roastery receives a digital receipt of the transaction. All the described above is implemented in our demo application: https://square-atlat.vercel.app Additionally, we thought about how to use this receipt in the context of INAtrace. It can then be attached in INAtrace as a proof to make the payment transparent to other stakeholders in the supply chain. This enables the retailer in Germany to check if the farmers get paid fairly. This information can also be shared with consumers, via a QR-code on the coffee pack. We designed mock-ups of how these steps could look like. Benefits for all stakeholders in the supply chain Our solution is beneficial for all stakeholders along the supply chain: The farmer can receive digital payments and has therefore no safety issue with large amounts of cash. Also, the power imbalance between farmer and manager of processing site is now neglected because the retailer can see the paid price and could intervene, if the manager of the processing site tries to take advantage of the farmers. Hence, a living wage for the farmers can be ensured. The manager of processing site can now digitally proof, that they do not take advantage of the farmers and thereby strengthen the relationship with the importers & retailers. The importers & retailers can now make sure, that the farmers in their supply chain are compensated fairly. This is important for the social sustainability of their products. The consumers can inform themselves about the compensation for the farmers and thereby be more sure than just with certifications, that there consume does not cause harm in the production countries. How we build it We built the WebApp with React and next. As a database in the backend, we used a postgreSQL database, for the ORM of it we used prisma.io. We deployed this via vercel, which works super well with react apps. Of course we used several Square APIs in our WebApp: Square Locations API to create the accounts for the farmers. Square Catalog API to create the inventory of goods that the farmers can sell and manage the prizes. Square Order API to create the orders of the goods and set the quantity that is bought. Square Payment API to process the payment from the manager of the processing site to the farmer. Challenges we ran into We are focusing on developing countries like Ecuador. It is crucial to make the process as simple as possible. We must keep additional hardware out of the scope, because it would not be affordable for the farmers. Hence, one challenge was the limit to a “smartphone only” solution. At the beginning it was challenging to find our path through the many APIs that Square has to offer, especially since we are new to payment. What really helped us was the API explorer. We were able to quickly see the differences between e.g. orders and payments and understand what we actually need for our idea. Although there is so much to choose from, the documentation in the API explorer helped us to overcome this challenge. Accomplishments that we're proud of We are proud that we developed a really easy-to-use application for our target group, the farmers. Simplicity is key when adopting processes like these for groups, that so far did not have the chance to participate digitally. We are also happy that via the connection to INAtrace we were able to built a solution, that is beneficiary for all stakeholders in the supply chain. What we learned How many ways their are to create and pay a bill :) What comes next? Currently, we as atlat are in an ongoing dialogue about the adaptation of INAtrace for certain agrifood supply chains. We will present our prototype as part of the dialogue to see if it resonates with a potential project partner. If it does, we will improve our application (e.g. do the translation for the countries) and also implement the sections in INAtrace, that we have designed as mock ups so far. We are looking forward to continuing working with the Square APIs on this to improve the situations of farmers. <div