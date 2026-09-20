---
slug: "hypertally"
url: "https://devpost.com/software/hypertally"
title: "hypertally"
hackathon: "Chainlink Fall 2022 Hackathon"
organization: "Chainlink Labs"
winner: true
words: 918
team_size: 4
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/sensor_fusion"
  - "mechanism/vision_ocr"
  - "domain/climate_energy"
  - "domain/developer_tools"
  - "domain/finance_payments"
  - "user/developer"
  - "user/researcher"
  - "substrate/geospatial"
  - "substrate/sensor_telemetry"
  - "substrate/video_visual"
---

# hypertally

> hypertally enables on-chain validation, monitoring, data analysis, and computer vision analysis of geo-referenced carbon projects.

[Devpost](https://devpost.com/software/hypertally) · hackathon [[Chainlink Fall 2022 Hackathon]]

## Facets

**mechanism** [[sensor_fusion]] [[vision_ocr]]
**domain** [[climate_energy]] [[developer_tools]] [[finance_payments]]
**user** [[developer]] [[researcher]]
**substrate** [[geospatial]] [[sensor_telemetry]] [[video_visual]]

**stack** agromonitoring, bacalhau, chainlink, docker, opencv, polygon, python, solidity, uma

## How they structured the write-up

- inspiration
- problem are solving
- what it does
- how we build it
- what we learned
- what's next for hypertally

## Body

Cover Problem Idea How does it work? Team Inspiration hypertally was created inspired by Pachama . Pachama is a company that trains Machine Learning models to analyze satellite data and assess the quality of nature-based carbon credits. We set out to create a solution that enables on-chain validation, monitoring, data analysis, and computer vision analysis of geo-referenced carbon projects using Chainlink oracles, IPFT NFT Storage, and Bacalhau as the main technologies. Problem are solving Estimating how much carbon is stored by nature-based carbon projects is expensive, time-consuming, and relies heavily on centralized certification standards and third-party validation entities. Additionally, due to the high costs and resources required, project validation happens on a per-project basis, and very few projects can assess the scale of their impact on a larger eco-region and how other externalities like weather, global economic trends, and commodity prices affect the future of carbon projects. Carbon tokens on-chain are a great innovation. Along with other solutions like the carbon pools and the open registries, create a new exciting design space for financial products and applications that could bring more transparency, traceability, and adoption to Carbon Markets. However, Carbon tokens are derived from traditional Carbon Credit certification and validation processes, therefore subject to its challenges. What it does hypertally lets any stakeholder in a nature-based carbon project report the ecological state of a geo-referenced site. hypertally harnesses Project Bacalhau to run computing analysis with satellite and sensor data, and estimate the ecological state and potential impact of forest projects. hypertally aims to help communities, individuals, and institutions fund, launch, and monitor high-quality forest projects. Additionally, hypertally supports existing CO2 tokens from Toucan Protocol, with our solution we could enrich the metadata of CO2 tokens with coordinates and continuous status updates. With hypertally , centralized certification entities could reduce the cost of project validation. Project Developers could assess the impact of their project and estimate how much carbon their projects will capture. Investors could study the health of a project and make informed investment decisions. Researchers can have access to an incentivized environment that aggregates different data streams related to carbon projects so they can add value to communities and project developers in need of deeper analysis and insights. Finally, Local stakeholders could participate in a network of land stewards supporting the monitoring of the ecological state of nearby projects. How we build it hypertally lets users create dynamic geo-referenced NFTs that represent nature-based carbon projects using coordinates. Users can also bring existing CO2 tokens from Toucan Protocol, and create a wrapper NFT to enrich it with coordinates. The NFT contract calls a Satellite Data API using a Chainlink oracle to get an image of the site that gets stored in the NFTs metadata in IPFS NFT Storage. hypertally then, lets anyone participate as a project advocate by reporting the ecological state of a site. hypertally does this by using an external adapter, a Data Provider Smart Contract on Chainlink, and the Chainlink network to let advocates submit data from Satellite Data APIs, CPI data, and other types of sensor data(LiDAR, Lab Tests, photos, etc). Data inputs are stored in the metadata of the NFT as well. Additionally, hypertally enables users to take the information from the NFT metadata to run data analysis and computer vision analysis using OpenCV in a Bacalhau instance, returning and updating the ecological state of the forest project. What we learned Building hypertally was a lot of fun. However, there are a few things we learned that we would like to change or improve in upcoming versions: We didn't prioritize the User Experience of this idea. In a future project, we would like to explore how individuals can submit geo-reference data from phones as well as how this tool can be used for Satellite Data providers as a revenue stream. We even finished the project dreaming about how to incentivize drone owners to report data. We wrote a smart contract for an optimistic oracle using UMA hoping to explore affordable and accurate data inputs. However, we deprioritized it in favor of having a working prototype in the time we had. We think this could be a great direction to explore in upcoming iterations. We were unable to try more interesting computer vision models with OpenCV due to the lack of time. However, we found several approaches to assessing the health of a forest project worth trying. In an upcoming iteration, we would like to explore the design of an open-source platform and incentives for researchers and scientists to support the creation of better computing models. In the future, we could harness Machine Learning to run even more interesting analyses using the data in hypertally . We look forward to learning how our solution would need to evolve to allow for that. We experimented with bringing real carbon tokens from Toucan Protocol into the project. We believe a tool like hypertally can enrich these tokens with coordinates and geo-referenced data, and augment their potential for impact and adoption. However, we didn't have enough time to build a proper solution to bridge the actual tokens. Our solution for this hackathon was limited to creating a copy of Toucan's tokens. What's next for hypertally We would love to design hypertally as a protocol. We are eager to explore how incentives, governance, and staking models can leverage the solution we prototyped to create a network of nature-based project advocates. There's lots of work to do and we are happy we got this far without any idea. <div