---
slug: "covidhack-oracle-provable"
url: "https://devpost.com/software/covidhack-oracle-provable"
title: "An Oracle to allow Pandemic-aware Policies"
hackathon: "COVIDathon - Decentralized AI Hackathon"
organization: "SingularityNet"
winner: true
words: 442
team_size: 2
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "domain/civic_government"
  - "domain/finance_payments"
  - "domain/legal_justice"
---

# An Oracle to allow Pandemic-aware Policies

> Aggregates Covid-19 data sources and publishes into Ocean. This can be used in legal smart contracts to have legal agreements that adapt to events such as pandemics in a responsible and predictive way

[Devpost](https://devpost.com/software/covidhack-oracle-provable) · hackathon [[COVIDathon - Decentralized AI Hackathon]]

## Facets

**domain** [[civic_government]] [[finance_payments]] [[legal_justice]]
  <sub>weak: climate_energy, disaster_emergency</sub>
  <sub>weak: small_business</sub>
  <sub>weak: code_repository, financial_record, web_dom</sub>

**stack** accordproject, amazon-web-services, docker, ergo, go, ipfs, node.js, oceanprotocol, python, serverlessframework

## Body

Oracle An Oracle to allow Pandemic-aware Policies Purpose: The covid-19 pandemic has caused widespread uncertainly for people and small businesses who feel the financial impact of the pandemic due to government restrictions, reduced customers numbers and spending power. Legal agreements are in many cases not well equipped to dynamically respond to restrictions and legislation. Tenancy agreements and Insurance contract, in particular, Business Interruption insurance is sometimes not clear and comprehensive in the handling of the current situation. The adoption of potential local and regional restrictions, that adapt based on local infection rates and risk factors mean that contracts need to be based on an trusted source of data, a agreed set of data schemas and a legal lexicon that can add clarity to legal agreements. The combination of these elements can lead to a fair and transparent set of legal agreements that can add clarity to an uncertain future. This project attempts to unite a number of these concepts in to a cohesive set of elements that can form a trusted set of data sources that are collected, aggregated and verified then made available on distributed platforms such as IPFS and published into a data trust such as Ocean. We aim to source from multiple trusted sources to get the most accurate data for the contracts to use. A platform such as Ocean is useful for sourcing data and algorithms to process the data, such as NLP models to extract data into a standard schema for use by contracts. Our current implementation uses the Provable platform as a trusted Oracle, but we wish to explore other options such as Chainlink, and algorithms that run inside Ocean or Singularity to act as a trusted source. The contracts can run on a range of permissioned and permission-less DLT systems, we have an implementation for Hyperledger Fabric in our repo below, with more to follow using Ethereum. The legal smart contracts have been developed as part of the Open Source Accord Project http://accordproject.org and we have published our sample pandemic policy contract that can use data returned from our Oracle at https://github.com/niallroche/covidhack-legalsmartcontract What have we built? A repository to manage (a set of) Oracle(s) to support smart (legal) contracts that can respond to global events such as: Pandemics (such as COVID-19) Civil Unrest Significant Climate events Natural Disasters Potential Oracles: Provable (formerly Oraclize) Chainlink Ocean Singularity Potential Data Sources: http://schema.org Special Announcement https://www.wikidata.org/wiki/Q81068910 Government websites legislation.gov.uk https://www.who.int WHO website Global and local Health information providers We have built upon our initial submission to the recent Global Legal Hackathon and have extended using IPFS and Ocean protocol. More information on hack is available at: https://challenge.globallegalhackathon.com/gallery/5ec84aef202da60044c03d6b <div