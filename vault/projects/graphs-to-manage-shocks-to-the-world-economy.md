---
slug: "graphs-to-manage-shocks-to-the-world-economy"
url: "https://devpost.com/software/graphs-to-manage-shocks-to-the-world-economy"
title: "ShockNet"
hackathon: "Graph For All Million Dollar Challenge"
organization: "TigerGraph"
winner: true
words: 1289
team_size: 1
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "domain/labor_employment"
  - "user/general_public"
  - "substrate/financial_record"
  - "substrate/geospatial"
  - "substrate/sensor_telemetry"
  - "substrate/structured_db"
  - "substrate/video_visual"
---

# ShockNet

> Prevent crises by predicting the transfer of shocks through the world economy. Users can adjust assumptions, investigate the predicted chains of shocks, and identify ways to avoid a crisis.

[Devpost](https://devpost.com/software/graphs-to-manage-shocks-to-the-world-economy) · hackathon [[Graph For All Million Dollar Challenge]]

## Facets

**domain** [[labor_employment]]
**user** [[general_public]]
**substrate** [[financial_record]] [[geospatial]] [[sensor_telemetry]] [[structured_db]] [[video_visual]]

**stack** d3.js, gtapagg, javascript, pandas, python, pytigergraph, tigergraphcloud

## How they structured the write-up

- inspiration
- what it does
- how i built it
- challenges i ran into
- accomplishments that i'm proud of
- what i learned
- what's next for shocknet
- references

## Body

The range of model assumptions a user can update Effects mode: countries plotted with colours coded for impact Horizons scanning: showing the places that reducing a dependency that might help avoid a crisis Explaining a shock chain in natural language to help users understand the prediction Inspiration I started from the Graph for Better Finance problem statement, focussing on preventing crises by allowing policymakers to investigate how difficulties or decisions in one country can spread to another country. I came up with a model that can show how shocks spread, and an app to allow policymakers to visualise and adjust the model to help them understand how best to avoid a future crisis or cushion the blow from a current one. What it does ShockNet has distilled data of economic cross-linkages (e.g. Mexico exports $10B of oil to Nicaragua; the production of Petroleum products in Nicaragua uses $2B of oil imports). These have been derived from the Global Trade Analysis Project GTAP database. The software uses these cross-linkages to predict how supply shocks will spread through the world economy. Adjustable assumptions A user investigating how shocks spread, can vary the assumptions used by the model. For example, what strength of cross-linkage will transfer a shock or not - e.g. if Financial Services in Nicaragua uses some imported oil, but it's only 0.5% of the total inputs to that activity, then assume Financial Services in Nicaragua does not experience a shock if imported oil experiences a shock. The other assumptions that can be adjusted relate to whether a country is likely to notice / care about the shock, based on what the app calls "critical industries." So, for example, Business Services in Nicaragua might experience a shock, but if business services only makes up 0.1% of national output, and 0.01% of unskilled labour costs, then the model will not consider Nicaragua to experience the shock. The first screenshot highlights the adjustable model assumptions. Analysis and visualisation Once the modelling assumptions are set, the app works in one of three modes: Effects mode The user can enter a selection of country-specific sectors (e.g. Oil in Mexico) or countries that are passing a supply shock to the global economy. From this starting point, the model predicts where the shock will spread to under the current assumptions. This mode can be used in an ongoing crisis or for "what if" simulations, to see whether a given country will experience the shock. The policy-maker can also dig into how the shock spreads in detail (which cross-linkages are active in the model) so they can evaluate how likely they think the prediction of a crisis spreading to their country. If they know a crisis is coming, they might be able to put policies in place to protect the affected industries / give extra support to affected citizens. From the point of view of a supra-national policy maker or economist, a colour-coding is used to highlight which countries face the biggest shocks, and hence where to focus attention on defending against a crisis. The second screenshot shows this colour-coded plot. Horizon-scanning mode The user can enter a selection of country-specific sectors (e.g. Oil in Mexico) or countries that they wish to protect from a supply shock. The model will predict all chains of shocks that could spread to these country-specific sectors. The model also provides an analysis that helps the policymaker focus their attention on the input-output relationships that are the lowest in scale and/or are responsible for opening up the widest possible numbers of chains of shocks. The third screenshot shows an example of this analysis (explained in more detail in the video and the user guide). Country grouping analysis The user can also use the app to detect which countries will be likeliest to spread shocks to each other, under the current assumptions. This allows a supra-national policy maker or economist to quickly get a sense of which countries are heavily interconnected and thus understand which countries should most avoid harmful policies against each other to prevent crises. How I built it Data extraction: I used the GTPAgg software to derive data files containing cross-linkages across 54 sectors and 134 countries, these are embedded resources of ShockNet I used a combination of Python, Pandas and PyTigerGraph to extract the linkages I wanted into my TigerGraph cloud instance - I chose this, as I wanted a library that could interact with the graphDB directly and PyTigerGraph seemed the best supported option Whilst developing the model, I made heavy use of TigerGraph GraphStudio to explore the graph and prototype queries For the running app (with the data loaded already), I run a Python webserver which interacts with the TigerGraph cloud, and sends it queries written in GSQL which For the front-end, I wanted something that a user can explore fairly interactively, so given my experience I chose Javascript and leaned quite heavily on d3.js which I knew to be good for network visualisations and also datamaps which builds on d3 to enable visualising a world map. More detail about how ShockNet works can be found in my brief (4 mins) explainer video Challenges I ran into In a multi-faceted project like this, there were a lot! Initially just finding, dissecting and understanding the economic data and models that were available was quite hard. I quickly realised that I wouldn't be able to come up with a quantitative solution to the problem, given my limited economics knowledge. Another huge challenge was visualising and interacting with the model in a meaningful way. Will users understand what the assumptions and results mean? I leant heavily toward natural language descriptions in the app, I felt explainability is important if the users want to have any kind of confidence in the app (see fourth screenshot). I also tried to provide a fairly detailed user guide . What will the users need to see? Can I lay it out for them in a manner that's presentable and allows them to see the most critical information easily? This is something that took some experimentation, given my lack of front-end development experience. Accomplishments that I'm proud of I'm really pleased that I managed to put together something usable, and makes use of the best in class available for the various bits of the challenge, even despite my lack of experience in all of them: existing economic models, TigerGraph, Python, Javascript, d3! What I learned A ton of technologies, some basics of economic models, and what's involved in hackathons. What's next for ShockNet I would absolutely love to add some basic notions of demand shocks and elasticities, e.g. the user could toggle an assumption that the Petroleum sector in Nicaragua will cut production if it experiences a supply shock (hence passing a demand shock to the producers of its inputs as well as a supply shock to those who rely on it). I ran out of time to do this before the end of the submission period. If I could get my hands on some up-to-date GTAP data or similar then I would update the data on cross-linkages that sits at the heart of the model to give an even more accurate view It would be great to continue exploring which graph analyses and metrics are the most useful to the policymakers who might be able to prevent / avoid / reduce the impact of a crisis References GTAP 8 Data Base Narayanan, G., Badri, Angel Aguiar and Robert McDougall, Eds. 2012. Global Trade, Assistance, and Production: The GTAP 8 Data Base, Center for Global Trade Analysis, Purdue University Software development projects that inspired me and I leaned on heavily PyTigerGraph TigerGraph In-Database Graph Data Science Algorithm Library pandas d3.js and their examples DataMaps <div