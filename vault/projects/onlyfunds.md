---
slug: "onlyfunds"
url: "https://devpost.com/software/onlyfunds"
title: "OnlyFunds"
hackathon: "NEAR MetaBUILD III Hackathon"
organization: "NEAR Protocol"
winner: true
words: 874
team_size: 3
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "domain/civic_government"
  - "domain/legal_justice"
  - "user/government_staff"
  - "substrate/financial_record"
  - "substrate/structured_db"
  - "substrate/video_visual"
  - "substrate/web_dom"
---

# OnlyFunds

> Crowdfunding protocol for projects on NEAR that gives backers the ability to control the release of funds to the team through DAO voting, reducing the risk of total loss.

[Devpost](https://devpost.com/software/onlyfunds) · hackathon [[NEAR MetaBUILD III Hackathon]]

## Facets

**domain** [[civic_government]] [[legal_justice]]
**user** [[government_staff]]
**substrate** [[financial_record]] [[structured_db]] [[video_visual]] [[web_dom]]

**stack** css3, html5, javascript, python, react, solidity

## How they structured the write-up

- inspiration
- the problem
- solution
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what's next for onlyfunds

## Body

Pricing comparison with other platforms Explore different projects Present yourself Have a say in projects you contributed to Inspiration In the Web2 crowdfunding model, backers have no mechanism to influence the development of the project, such as when the founding team disappears or creates something very different from what was promised. Our goal is to improve the existing concept of crowdfunding with the help of Web3. We achieve this by storing the pledged money in a smart contract. The full amount is released over time, through a DAO voting system that checks if the project accomplishes its milestones. The problem Funders perspective In the last decade, crowdfunding has seen a massive rise in popularity. And with it, many projects saw the opportunity to raise money, with no proof of concept ready. Often, they simply present an idea with no plan on how to realize it. In the last few years, a well-rendered trailer was enough, and people lost millions in unfinished products that never saw the day of light. And once they run out of money, funders lose every cent they previously pledged. This can massively discourage new funding and potentially good ideas receive no funding. Projects Perspective While crowdfunding platforms offer a stage for projects to present themselves, they come with problems and complications too. In addition to a platform fee, nearly all platforms have an additional transaction fee. Once projects are funded, they pay up to 3 percent, just to receive their money. On top of that, long wait times until they receive the money can delay the project’s start time. Solution With the help of Web3 we tackle both issues at the same time. Projects create a new campaign, and a smart contract gets created once they enter all the information. Users can then invest in the project, by contributing money to the smart contract. If the funding goal is reached, a partial amount immediately gets released to the project. Our crowdfunding platform gives backers the power of DAO governance to control the release of the other funds raised. This holds the founding team accountable to be transparent about their work. A vote at each milestone either releases the remaining funds or returns them to the backers. On the other hand, we can provide a transparent and easy model for projects. We have a fee, only if they are successfully funded and that is it. Near allows us to charge no transaction cost, as the gas costs are negligible. Projects can calculate much better on their timeline, as soon as they are funded, they can start. What it does Our crowdfunding platform gives backers the power of DAO governance to control the release of funds raised and hold the founding team accountable. A vote at each milestone either releases the remaining funds or returns them to the backers. Our site gives new start-ups the opportunity to present their vision and raise money to bring their idea to life. They can link to their websites, share a title image and write about them. Once they are set, they hit create project and a smart contract on Near, via aurora, gets released. This contract can then be funded by backers. If the funding goal is reached, the project can finalize the funding phase and will receive an initial 25% of the amount raised. All backers can now watch the project and with a DAO voting system they decide, when (and how many) additional funds should be released. Should the project show bad signs or simply stop working on it, a "withdraw" vote can be initiated and the remaining money gets returned to the backers. How we built it We categorized our work into three main fields. Website, Smart contracts and presentation. The website was built using React and a Firestore for the Database. We decided to settle for the database, to ensure fast loading times on our site. The smart contracts are the backbone of our platform. We have two contracts, a factory(1) that produces the project contract(2). When people create their campaign on our website, our factory automatically deploys a project smart contract for them, through which they can get funded. Challenges we ran into 8 weeks can seem long, but to plan out and add the workflow into your daily routine requires a lot of discipline. Launching a new platform not only means building a great product, but also includes extensive research. To see where your competitors are, where is a suitable location to found your new business and many more. You have to prioritize, otherwise there is no end to this additional research. Accomplishments that we're proud of Even though we had to scale down our team, we still managed to not only produce a working product on main net, but also a Pitch-deck & Business-plan to get our amazing product out there. What's next for Onlyfunds 1. Company Set up a legal entity in suitable jurisdiction Continue talks with potential compliance officer Ramp up marketing efforts to launch a first campaign 2. Platform Implement automatic verification on Aurorascan Projects will be able to style their description with bb-codes More options for projects to present themselves We will officially launch in Q1 of 2023 Check out our Pitch Deck <div