---
slug: "esg-ai"
url: "https://devpost.com/software/esg-ai"
title: "ESG AI"
hackathon: "Hack to the Future 2020"
organization: "Finastra"
winner: true
words: 692
team_size: 4
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/on_device_local"
  - "mechanism/realtime_stream"
  - "domain/climate_energy"
  - "domain/education"
  - "domain/finance_payments"
  - "domain/labor_employment"
  - "user/researcher"
  - "substrate/code_repository"
  - "substrate/financial_record"
---

# ESG AI

> Smarter Sustainable Investing Through Data and Deep Learning

[Devpost](https://devpost.com/software/esg-ai) · hackathon [[Hack to the Future 2020]]

## Facets

**mechanism** [[on_device_local]] [[realtime_stream]]
**domain** [[climate_energy]] [[education]] [[finance_payments]] [[labor_employment]]
**user** [[researcher]]
**substrate** [[code_repository]] [[financial_record]]

**stack** azure, data, databricks, deep-learning, esg, machine-learning, networkx, numpy, pandas, particle, pyspark, python, pytorch, streamlit

## How they structured the write-up

- background

## Body

ESG AI ESG AI Research Portal ESG AI Research Portal ESG AI Research Portal ESG AI Research Portal ESG AI Hacking for Good Using the Power of Streamlit. Background Environmental, Social, & Governance ( ESG ) investing has rapidly gained popularity in the world of finance. The idea is to invest in companies that are sustainable, particularly in in the 3 ESG categories: E nvironmental - Issues such as climate change and pollution S ocial - Issues around workplace practices and human capital G overnance - Issues such as executive pay, accounting, and ethics There has been a tremendous amount of research around ESG investing. Harvard Law School Forum on Corporate Governance published a paper titled "ESG Matters" in which they studied companies with particularly high ESG scores compared to those with low scores with the following conclusions: Higher ESG is associated with higher profitability and lower volatility High ESG scoring companies tend to be good allocators of capital Good ESG companies generally have higher valuations, EVA growth, size, and returns ESG Reporting Currently 90% of S&P 500 companies publish annual sustainability reports, which can range from as little as 30 pages to over 200 pages. There is not one clear reporting format, but there are some general reporting guidelines. For example, Nasdaq publishes their own guide to help companies report meaningful information to stakeholders. Analysts leverage these reports to understand company trends and themes. Developing an investment thesis is a painstaking, manual process that can take weeks for a single company. Greenwashing Greenwashing is the practice of making statements or policies that make an investment appear more serious about ESG than it actually is. As such, analysts need to be mindful of self-reporting and make sure to leverage other credible sources in order to minimize the effect of greenwashing on our sustainability analysis. Current Approach ESG scoring is tricky. Research analysts leverage many sources to manually come up with scores around the ESG categories. These scores must be updated every so often, but by the nature of the current process scores cannot be reported in real time. As there are thousands of companies, the current approach is hardly scalable. Our Approach We aim to make ESG scoring an automatic, data-driven process. We leverage the GDelt news source to ingest historical and real-time news articles, tweets, and other digital publications that we classify into the three ESG categories. We then perform scoring based on sentiment, which can be adjusted based on given windows of time. Additionally, we leverage the deep learning algorithm, Node2Vec to embed the connections on a graph from news article mentions. This allows us to find better suggested competitors to compare ESG results against. Examples of ESG found in News E: Nike (NKE): “Its Flyknit and Flyleather products were developed with environmental sustainability in mind. Nike signed onto a coalition of companies called RE100, vowing to source 100% renewable energy across its operations by 2025. There's more, but any interested investors should read Nike's latest sustainability report, which uses the GRI framework, the Sustainability Accounting Standards Board (SASB), and the United Nations' Sustainable Development Goals (SDG).” S: Accenture (ACN): “Accenture pays close attention to its diversity and inclusion in its workforce. The company plans to improve its workplace gender ratios, with a goal to have 50% female and 50% male employees by the end of 2025. Accenture plans to better its corporate makeup as well, pledging to have at least 25% female managing directors by 2020.” G: Intuit (INTU): “It has achieved a 40% diverse board, one of the highest levels in corporate America today. Intuit shows accountability by tying its executives' incentive compensation to revenue and non-GAAP (Generally Accepted Accounting Principles) operating income, as well as to the company's overall performance on annual goals related to employees, customers, partners, and stockholders.” [ source ] Behind the Scenes Our Application has been created with the following technologies: Streamlit Python Pyspark DataBricks NetworkX Pytorch Thanks to Streamlit Sharing, there's an easy way to access our app HERE ! (This link works in your browser and your phone) You can also clone the github repository to run the app locally. <div