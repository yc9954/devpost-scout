---
slug: "ixo-assistant-custom-action-test-environment"
url: "https://devpost.com/software/ixo-assistant-custom-action-test-environment"
title: "IXO Assistant Playground"
hackathon: "Cosmos HackAtom VI "
organization: "Cosmos"
winner: true
words: 563
team_size: 2
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "domain/civic_government"
  - "domain/climate_energy"
  - "domain/developer_tools"
  - "user/developer"
  - "user/educator_student"
  - "substrate/financial_record"
  - "substrate/geospatial"
  - "substrate/video_visual"
---

# IXO Assistant Playground

> A friendly docker environment to easily implement, configure and test custom actions that can be integrated into the IXO Assistant bot.

[Devpost](https://devpost.com/software/ixo-assistant-custom-action-test-environment) · hackathon [[Cosmos HackAtom VI]]

## Facets

**domain** [[civic_government]] [[climate_energy]] [[developer_tools]]
**user** [[developer]] [[educator_student]]
**substrate** [[financial_record]] [[geospatial]] [[video_visual]]
  <sub>weak: web_dom</sub>

**stack** docker, html, python, rasa

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for ixo assistant playground
- use cases

## Body

Inspiration Make it easy for developers to learn, experiment with and implement custom actions for the IXO assistant. IXO assistant provides a powerful toolsuite for evaluators to get external data from both the real world and the chain state which they can use to evaluate specific claims of earth state changes. What it does A docker-compose environment including a rasa-server, rasa action-server, chatbot UI and a jupyter notebook server. The chatbot has a number of custom actions configured: Get time for [place] - This gets the local time at a place. (Included as an example with great tutorial for writing custom actions) find address for DID [DID] - Converts DID to ixo cosmos address. Taken from IXO Assistant (had to tweak to get working) voting bond from user [user_did] to bond [bond_did] - Returns current bond state for a particular user DID. (Taken form IXO Assistant with tweaks) esri geocode [location] - Returns a esri map for specific location How we built it We first tried to integrate this into the IXO application but ran into a number of issues. So created a custom test evironment where developers could develop and validate custom actions before integrating them into the IXO assistant. Challenges we ran into Navigating the complexities of the IXO application UI. A number of bugs including the IXO assistant not being accessible in the current application. Getting the rasa server configured correctly in docker was also a challenge. Getting the Esri api to return an base64 image that could be rendered in the chat. Accomplishments that we're proud of Getting custom actions to be recognised and executed. The docker environment we have created. What we learned How to write custom actions for the IXO assistant How to use the Esri What's next for IXO Assistant Playground Add signing capability so user can generate transactions to sign from the ixo wallet. Further integration with Esri. This has a lot of powerful features for tracking real state changes in the world. E.g. heat, weather, deforestation, pollution. Use Cases Yoma is a youth agency marketplace developed in partnership with UNICEF, Foundation Botnar, Goodwall, DIDx and various other organisations to provide youth access to learning and earning opportunities. Verifiable proofs of opportunity completion build up a verifiable digital CV controlled by their digital self-sovereign identity wallet. A future extension of Yoma is what we refer to as Green Yoma , which will focus on exposing youth to sustainable development projects where they can participate as impact makers and build up a verifiable green CV. Digital verifiable CV's allow seamless access to earning opportunities in Yoma. The IXO Assistant and extension of this work will be leveraged in Green Yoma to provide impact evaluators with seamless access to various data sources to assist in evaluation decision making via the IXO assistant. Example IXO Assitant Use Cases for Green Yoma Access air pollution data to determine if youth interventions made an observable difference. Access earth observation data to verify impact claims such as reforestation, plastic cleanup etc. Allow youth to manage their wallets, credentials and interaction with the IXO ecosystem via the IXO assistant. The IXO assistant can be leveraged a wide range of use cases in Green Yoma to assist in impact claim submission, evaluation, rewards etc. For more information about the Green Yoma vision watch our Children and Youth Forum 2021 presentation here . <div