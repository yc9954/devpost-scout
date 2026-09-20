---
slug: "esg-alygnement-for-asset-managers"
url: "https://devpost.com/software/esg-alygnement-for-asset-managers"
title: "The Responsible Investors"
hackathon: "Hack to the Future 2020"
organization: "Finastra"
winner: true
words: 698
team_size: 12
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/simulation_digital_twin"
  - "domain/climate_energy"
  - "domain/developer_tools"
  - "user/developer"
  - "substrate/web_dom"
---

# The Responsible Investors

> Scoring Finastra ESG Funds (Environmental Social Governance criteria) using Fintech AI and Natural Language Processing through FusionFabric.cloud

[Devpost](https://devpost.com/software/esg-alygnement-for-asset-managers) · hackathon [[Hack to the Future 2020]]

## Facets

**mechanism** [[simulation_digital_twin]]
**domain** [[climate_energy]] [[developer_tools]]
**user** [[developer]]
**substrate** [[web_dom]]

**stack** ai, alygne-(fintech), angular.js, django, finastra-fusion-invest, fusionfabric.cloud-platform, natural-language-processing, portfolio-optimization/reporting-api, postgresql

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for the responsible investors

## Body

The Responsible Investors Architecture App in FusionFabric.cloud Reporting API in FusionFabric.cloud The team in action Movie picture 1: Introduction and title Movie picture 2: Alex, the B2C Retail Investor Movie picture 3: Alygne, the AI Movie picture 4: Diogo, the B2E Asset Manager - Finastra client Alygne imported via API the 10 companies of a Fund Alygned assessed a company (Carrefour) regarding three ESG dimensions: employee benefit, climat change, LGBTQ ESG score breakdown by various sources: what the company claims vs market perception URls and extracts of relevant articles, posts and tweets: Climate change URls and extracts of relevant articles, posts and tweets: employees benefits URls and extracts of relevant articles, posts and tweets: LGBTQ Fusion Invest The Retail Investor Interface Inspiration The investors mindset is changing, they request the need to integrate social criteria in their investments. Financial investment funds aligned with ESG criteria have a direct and positive impact on the society and the environment. What it does It's a four-step story, referring to the steps (1-4) of the Architecture diagram (uploaded). The Fintech (Alygne) consumes an OpenAPI (GA) on FusionFabric.cloud to load the issuers (companies, assets) of a fund. The underlying Finastra product is Fusion Invest, and the persona an Asset Manager named Diogo, who wants his clients to invest in the ESG-funds of his portfolio. The Fintech AI is able to collect data from the www, related to ESG-criteria of a given issuer/company. Using Natural Language Processing, the AI gathers relevant press releases, social networks, tweets, and corporate announcements of the Internet. Note: the Fintech is able to split the company's self-assessments (their own communication) vs the market's perception (press, social networks). The Fintech algorithm computes quantitative ESG scores, for each issuers (we selected 12: Carrefour, Accor, LVMH, Hermes, etc.) and for several dimensions (we selected 3: Employee-benefit, LGBT-friendliness, and Climate change). Using a return SPI (new interface, simulated in toolkit for this hackathon), the Finastra user retrieves the ESG score of his issuers and aggregates them at the fund level. The story continues in his core product (Fusion Invest), where the asset manager can increase the allocation of good companies (regards to ESG-criteria and scoring), and reduce the exposure to those that underperform. He can also share this transparency towards his own customers. We retained for this the persona Alex, who's Diogo's client, a retail investor who, as an employee, wants to invest his employee savings and retirement according to his beliefs and convictions. How we built it We didn't only make a demo: we produced a movie. The background is a project driven by technical constrains, human skills, and hackathon judging criteria. We first drafted a Use Case based on persona who have an interest in ESG: a retail investor, an asset manager and an AI. Step by step, the user stories became a real scenario, and the demo transposed into a movie. For a very fast reactivity, we created micro-teams like the ones in charge of making a movie. The product owners and delivery managers became "the scenarists", the developers became "the CGI's", the persona became "the actors", the architects became "the post-production", and of course, heads of became "the producers". Challenges we ran into Different time zones (San Francisco, Paris, London, Singapore, HK) Delivery under short time constraints Moving from a technical solution to a professional video Balancing the "best effort" and the total focus, when required. Accomplishments that we're proud of Building a brand new partnership (Alygne and Invest never worked together before) The roles we've all played (not only the actors!) Everyone, each micro-teams delivered their own part. All are successful Beyond difference of cultures, countries, experience and skills, all converged to a single deliverable: our movie "The Responsible Investors". What we learned How to build the "Story Telling" on top of innovation: the demo video transposed to a real movie ESG awareness, especially social criteria applied to retail and institutional investors "Natural Language Processing" capabilities How easy it is to co-innovate between Finastra and a fintech through FFDC. What's next for The Responsible Investors Win the hackathon Enhance the hackathon scenario to a viable Use Case Get the support of the organization Release a new App <div