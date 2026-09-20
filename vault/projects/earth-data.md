---
slug: "earth-data"
url: "https://devpost.com/software/earth-data"
title: "net.zero"
hackathon: "Chainlink Fall Hackathon 2021"
organization: "Chainlink"
winner: true
words: 1025
team_size: 5
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "mechanism/sensor_fusion"
  - "domain/climate_energy"
  - "domain/finance_payments"
  - "user/educator_student"
  - "substrate/document_pdf"
  - "substrate/geospatial"
  - "substrate/sensor_telemetry"
---

# net.zero

> Todays' centralised sustainability disclosures are non mandatory, biased & manual . We aim to decentralise ESG disclosures that drive an autonomous corrective Climate action towards net.zero.

[Devpost](https://devpost.com/software/earth-data) · hackathon [[Chainlink Fall Hackathon 2021]]

## Facets

**mechanism** [[realtime_stream]] [[sensor_fusion]]
**domain** [[climate_energy]] [[finance_payments]]
**user** [[educator_student]]
**substrate** [[document_pdf]] [[geospatial]] [[sensor_telemetry]]

**stack** chainlink, javascript, python, solidity

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for net.zero

## Body

Climate Action Inspiration Sustainability disclosures are passive in nature. We believe there is an opportunity for us to decentralise, mitigate single points of failure, bias and dependency for climate disclosure data. We believe technology can provide systemic evidence to monitor, control and mitigate greenhouse gasses. The mission of the project is to build a path to net zero. The corrective action can help us save our only home; Earth. It is upon us to do the right thing for the planet. What is net zero? Put simply, net zero refers to the balance between the amount of greenhouse gas produced and the amount removed from the atmosphere. We reach net zero when the amount we add is no more than the amount taken away. Currently net zero mechanism has a central dependency on analytics firms facilitating collection and processing of Environmental, Social and Governance (ESG) data. In most scenarios data is consolidated using a questionnaires which may fail to capture mandatory disclosures. Current disclosure methods has an information asymmetry wherein a climate event may be excluded from disclosure, as it it at the discretion of the entity. This single point of dependency can lead to bias, inaccurate reporting and green washing. Institutions and Individuals may direct capital or invest in organisation's that may be unknowingly polluting or supporting unsustainable practices. It is of utmost importance that investors have access to transparent information to make an informed decision to support green economy**. It is imperative that investors have access to accurate information to engage in sustainable practices or corrective actions. We believe there is an opportunity for us to decentralise, mitigate single points of failure, bias and dependency on centralised players. Technology can provide systemic evidence to monitor, control and mitigate greenhouse gasses. The Vision : We rise to the challenge of building a moral, decentralised and data centric green economy. **A green economy is an economy that aims at reducing environmental risks and ecological scarcities, and that aims for sustainable development without degrading the environment. The mission: To build a path to net zero. A mechanism for corrective action that sets us on path to Green economy. What it does Provides unbiased disclosure to public/investors/ institutions. Provides an immutable trail of evidence on pollution triggers. Use the data to drive a net.zero mechanism that aligns with United Nations Sustainable Development Goal 13 i.e. take urgent action to combat climate change and its impacts* The challenged is to do this in the most cost efficient, decentralised and impactful way(UX). How we built it We segregated the build into two parts: earth.data and the net.zero mechanism. earth.data We built a Chainlink external adapter to bring in data from a satellite feed for pollution data. A first of the kind pollution data oracle capable of real time pollution levels for a given geographic location. The tutorial and document library helped us greatly to overcome some of the teething issues. Once we were confident that the pollution oracle was stable, we explored Chainlink Keepers as a solution to call the API on demand (one time) or at regular intervals (tracking). We wanted to make sure we had the right balance of API call frequency and gas costs. We integrated all the logic to the front end to create unbiased visuals that disclose climate trigger insight and trace of historical event, based on customer demand. net.zero Last but not the least we linked the backend to the logic where every pollutant that breached the pollution treshold was minted as a Green Tax token (ERC1155 open zepplin source) containing token URI unique to the event i.e. Unix Times stamp, Latitude and Longitude and pollution parameters breached. There by creating a complete auditable autonomous tax generation and accountability for industrial pollution in a geographic location. The tokens are directly minted into governing body's wallet without any intermediation from net.zero ERC1155 smart contact. We didn't have time to build delivery vs payment mechanism for Green Tax Tokens and Governance rules. Challenges we ran into Our approach to the build was highly agile, with daily stand ups and discussions to keep the pace moving at time challenging. Knowledge gap TOML Gas Optimisation Time to code Accomplishments that we're proud of Working as a team Ability to understand and work with each others strengths. Dedication to work through differences and focusing on the goal. Exponential learning, the ability to use tools, videos and docs to make something that works without a formal training. Going over and above to dedicate time and effort for a good cause. What we learned Ways of working We learnt that having a clear understanding of vision is important. It saves precious time and effort in building the right outcomes. We quickly realised the value of communication and collaboration, we spoke about ideas and discussed them until there was clear understanding of next steps. We learnt to time-boxed activities to keep thing nimble and agile as we were dealing with many unknowns. There was a lot of documentation of ideas and concepts. We learnt to be resilient and pivot when something wasn't working. Technology We got our basics right on tools offered by Chainlink ecosystem. External adapters, Hosting chainlink nodes, Deploying keepers and Chainlink NFT were our biggest take away. The sessions offered by chain link accelerated our learning and saved us time in research. Code along videos helped us excel. Some of us with very basic coding skills picked up Python, Javascript and Solidity in a very short span of time. We can proudly say we learnt more in these few weeks compared to a couple of years. What's next for net.zero Direct satellite feed from EUMETSAT Multi source validation for pollution data calls. a faster and a better external adapter. Gas optimisation by post processing of pollution data. In line with Gas optimisation strategy build net.zero API creation for chainlink initiators approach. Publish a paper on our project in Medium. Build on layer 2 infrastructure. Engage govt & urge public policy on decentralised climate disclosures. Build trading mechanism with govt issued carbon credits. Polished user journey and UX. Governance Mechanism for Green Tax tokens. Events report; blockchain telemetry. <div