---
slug: "anti-mafia-analytics-platform"
url: "https://devpost.com/software/anti-mafia-analytics-platform"
title: "Anti-Mafia Analytics Platform"
hackathon: "Graph For All Million Dollar Challenge"
organization: "TigerGraph"
winner: true
words: 447
team_size: 5
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/graph_reasoning"
  - "domain/finance_payments"
  - "user/government_staff"
  - "substrate/financial_record"
  - "substrate/structured_db"
---

# Anti-Mafia Analytics Platform

> Tackling organised crime, one node at a time.

[Devpost](https://devpost.com/software/anti-mafia-analytics-platform) · hackathon [[Graph For All Million Dollar Challenge]]

## Facets

**mechanism** [[graph_reasoning]]
**domain** [[finance_payments]]
**user** [[government_staff]]
**substrate** [[financial_record]] [[structured_db]]

**stack** pandas, python

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for anti-mafia analytics platform

## Body

Inspiration Organised crime negatively impacts society from issues such as drug trafficking to corruption to murder. Tackling these issues relies on understanding the complex interconnected web of crime incidents, criminals, and financial activity. Our project seeks to provide an analytics platform that can detect "moles" within the police force and spot fraud transactions. It is clear to see that the identification and subsequent disruption of these criminal organisations would greatly improve society both socially and financially. What it does Our analytics platform can see connections between Police Officers involved in an unusually high number of unsuccessful raids and wire tapped phone calls to members of the Mafia. This offers key insights into identifying "moles" within the police force. Furthermore, anomalous payment transaction values within the police force can be used to detect bribery. Wire tap connections can detect who the crucial members of the Mafia are and who to target for maximum impact. Our graph database can drastically reduce the time taken for the structure of a crime organisation to be uncovered, and hence lead to faster and more plentiful abolition of such organisations. How we built it We created the schema in Lucid Chart and designated primary keys, foreign keys, and attributes. Since there were no publicly available datasets on the Italian Mafia, we generated representative synthetic data. We performed research into Mafia family hierarchy, main crime activities and geography to make sure our data generated accurately. Using the Python language and associated Pandas library, we created CSV's for Mafia Members, Police Members, Public Individuals, Financial Transactions, Crime Incidents, Raids and others. The CSVs were loaded into TigerGraph. The schema was created and the CSV files were mapped to nodes and edges. GSQL queries were run to reveal insights of our synthetic data. Challenges we ran into Due to randomising much of our synthetic data it was occasionally challenging to find any sort of pattern when running queries. The GSQL queries also had some internal bugs that was no fault of our own. Accomplishments that we're proud of Our graph database was densely connected and revealed crucial links between police members, mafia members and raid tip-offs. It serves as a proof of concept for future crime analytics tools. What we learned If we were using our graph database as a proof of concept, it would help us greatly if we engineered the synthetic data to show the insights we wanted. We learnt the power of visualising connections to spot missing links in criminal investigations. What's next for Anti-Mafia Analytics Platform The next step is getting access to REAL organised crime data that will help solve cases and lead to a clamp down of organised crime. <div