---
slug: "birdbox-6r59dj"
url: "https://devpost.com/software/birdbox-6r59dj"
title: "Birdbox"
hackathon: "The European Commission's EUvsVirus Hackathon"
organization: "European Commission"
winner: true
words: 1273
team_size: 6
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/graph_reasoning"
  - "mechanism/simulation_digital_twin"
  - "domain/civic_government"
  - "domain/finance_payments"
  - "substrate/financial_record"
  - "substrate/regulation_legal_text"
  - "substrate/sensor_telemetry"
  - "substrate/structured_db"
---

# Birdbox

> This project applies SNA methodologies and Big Data tools, used to analyze social networks to study the relations established between companies in EU market for systemic financial risk supervision.

[Devpost](https://devpost.com/software/birdbox-6r59dj) · hackathon [[The European Commission-s EUvsVirus Hackathon]]

## Facets

**mechanism** [[graph_reasoning]] [[simulation_digital_twin]]
**domain** [[civic_government]] [[finance_payments]]
**substrate** [[financial_record]] [[regulation_legal_text]] [[sensor_telemetry]] [[structured_db]]

**stack** mongodb, mysql, node.js, sna

## How they structured the write-up

- inspiration
- what it does
- how i built it
- challenges i ran into
- accomplishments that i'm proud of
- what i learned
- what's next for birdbox
- built with
- additional questions
- the problem your project solves
- the solution you bring to the table (including technical details, architecture, tools used)
- what you have done during the weekend
- the solution’s impact to the crisis
- the necessities in order to continue the project
- the value of your solution(s) after the crisis

## Body

BirdBox GUI BirdBox architecture Inspiration Our inspiration comes from the financial challenges all EU countries are facing in this pandemic crisis and different strategies they use to minimize the negative impact on the economy. The pandemic crisis happened very quickly and left most of the countries unprepared in a difficult situation. The governments are forced to create quick, but effective and tenable plans to minimize the losses. We wanted to design a solution that would help them to find optimal strategies for financial relief packages by quickly detecting the most critical areas and finding the ones where the stimulus would have the best possible impact (generating revenue, saving jobs, preventing companies shutdown). This solution is applicable for, not only the immediate consequences of the Corona crisis, but also in case of a comeback that would again affect the economy. What it does Birdbox uses aggregated transactions data – for the purpose of the hackathon on company level, but it is possible to use other aggregations (e.g. sector, country level). Transactions data is graphically displayed as a network, where nodes represent companies, and their transactions are directed links between them. This gives a visual representation of the whole money exchange network with its strongly and weakly connected parts, taking into consideration the whole network structure and not only specific company data. Birdbox has two main functions: represent the market as a network and detect key market players The importance of each company in the network is calculated using graph theory and network analysis methods. We use different network analysis metrics to calculate the companies importance based on different criteria (e.g. incoming/outgoing cash flow, number of different customers/suppliers, the level of connectedness, etc.). create simulations of stress events in the market The users can simulate stress events that could potentially affect the whole network: e.g. what would happen in an event of significant income reduction for a specific company/industry, or if a company with a high importance score was given a crisis credit to help its business and, by extension, the entire company's neighborhood (its suppliers and customers). Birdbox is designed to help countries make smarter, data driven strategies to help key players in the market and to find scenarios that will have the most positive impact on the economy. How I built it The solution is built out of several components. We built a web application that displays the network data in informative graphs and allows the user to drill down and get specific information/calculations (company information, importance scores, simulations). The data analysis and calculation module in the background processes the input data (transactions between companies) and stores the results in a database. The user interface loads data from the database and display it in the most user friendly way. For the purpose of the hackathon we used generated data that would, in real life, be available from regulatory bodies or financial agencies on country or EU level. This aggregated transaction data can be enriched with additional datasets such as: Data from the Tax Administration Activity type score Industry classification score Credit score Number of employees in order to build even better models and simulations. Challenges I ran into One of the biggest challenges we ran into was the data. As we do not have access to real financial data, we generated a test dataset for the purpose of the hackathon. We tried to represent a network of companies that are connected through financial transactions, but we realize real-world data will be different and will require a process of gathering and preparation, and, potentially, privacy regulations. Moreover, other information could be considered in the solution, besides the transactions (e.g. company market share, industry-relevant data). Accomplishments that I'm proud of We are very proud that we built the solution in such short period of time, and made both frontend and backend functional, as well as the analytics module. More importantly, we are proud that our concept gives quick results and, with the right improvements, can give valuable inputs to financial crisis management. What I learned We learned that social network analysis can be a very good tool to analyze the relationships between entities in a financial system, as it considers the network structure, the transitivity of financial interactions and the way certain changes affect different parts of the network. By detecting the most important entities and creating simulations through the network, we can create strategies which would involve manipulating those entities (companies) to investigate the impact on the whole network. What's next for Birdbox We plan expanding the solution with a more advanced simulation module that would allow us to create more sophisticated predictions and estimations for specific use cases. Furthermore, we think that it would be beneficial to include finance and economy experts; domain knowledge would help us define other variables and aspects we might consider in the calculations and simulations to get even more informative and more accurate results. Built with The solution is built with NodeJS framework and Python scripts as background services. The database layer consists of MySQL and MongoDB databases, while the user interface is built with Angular framework. Additional questions The problem your project solves Our solution can help governments to find optimal strategies for financial relief packages by quickly detecting the most critical areas and finding the ones where the stimulus would have the best possible impact on generating revenue, saving jobs, preventing companies shutdown by performing different scenarios. The solution you bring to the table (including technical details, architecture, tools used) Birdbox is modern scalable, cloud-ready web application built out of several cutting-edge technology components. Following components and framework are used: MongoDB – Storage layer NodeJS – Backend Python – Calculations and algorithms Javascript - Frontend Please see attached presentation in Birdbox.zip For the purpose of the hackathon it uses generated data that can be available from regulatory bodies or financial agencies on country or EU level. In order to build even better models and simulations, this aggregated transaction data can be enriched with additional datasets. Our assuption is that aggregated trasaction data is owned by governments and regulatory bodies and that this data may be available for implementation of application scenarios. What you have done during the weekend During the weekend we have developed prototype of the solution using generated dataset. Tasks we have successfully completed: Preparation of synthetic dataset Design architecture of the solution Implementation of backend logic for data ingestion Implementation of algorithms for complex SNA calculations Implementation of GUI and data visulaisations Prepare text pitch Prepare video pitch The solution’s impact to the crisis Our platform will allow governments to test different scenarios and simulations of how crisis or financial assistance affects the economy. The solution's impact to the crisis would be: Saving jobs Minimizing effects of the recession Better decision making in government and financial sectors Better resource allocation for financial injections in crisis based on real data Better understanding of market forces performing different simulations The necessities in order to continue the project In the future, we plan to include finance and economy experts to get more domain knowledge to expand the solution with a more advanced simulation module that would allow us to create more sophisticated predictions and estimations for specific use cases. It is mandatory to have access to real data to continue the project. The value of your solution(s) after the crisis This solution is applicable for, not only the immediate consequences of the Corona crisis, but also in case of a comeback or any other chrisis that would again affect the economy. It is also applicable for market analysis and risk scoring for any market conditions. <div