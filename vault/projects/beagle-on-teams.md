---
slug: "beagle-on-teams"
url: "https://devpost.com/software/beagle-on-teams"
title: "Beagle For Teams"
hackathon: "Microsoft Teams App Development Challenge 2021"
organization: "Microsoft"
winner: true
words: 938
team_size: 5
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "domain/labor_employment"
  - "user/researcher"
  - "substrate/sensor_telemetry"
  - "substrate/structured_db"
---

# Beagle For Teams

> Beagle is a truly agile conversational platform aimed at bringing data and analysis to all the people in an organization through their messaging/collaboration platforms like MS Teams

[Devpost](https://devpost.com/software/beagle-on-teams) · hackathon [[Microsoft Teams App Development Challenge 2021]]

## Facets

**domain** [[labor_employment]]
**user** [[researcher]]
**substrate** [[sensor_telemetry]] [[structured_db]]

**stack** azure, azure-graph-api, azure-sql-server, celerey, django-rest-framework, powerbi, python, react, teams

## How they structured the write-up

- beagle journey

## Body

Your personal virtual assistant Beagle usage scenarios Users can "select an analysis" configured for them within the Virtual Analyst Users will be prompted with a "set of cards" related to the selected analysis Users can use "filters" to deep dive on the fly within MS Teams Advance Beagle Features User can interact with beagle in "Natural Language" While chatting with a teammate, Users can "search for a card" and send it to them in chat window itself User can collaborate on insights with his team, by adding the card to his team's "Narrative Board" User can set a "Notification" ,for card to be delivered at set frequency User can "Download" the card in PPT or Excel format User can provide "Feedback" on cards Users who are always on the fly, can access Beagle on their phones or tablets Beagle Journey What inspired us to create Beagle? At Decision Point, a Microsoft Gold Partner for Data Analytics, we do extensive work with clients in creating value from their enormous data assets. Although, dashboards are one of the primary ways in which the analytics outputs are shared with its end users, organizations struggle with driving adoption and usage - but why? We realized in our client conversations that dashboards are just not agile enough to keep pace with changing business priorities, requires significant cost and time effort to maintain and in many cases the users struggle to get to their insights buried under a mountain of charts and filters! As the pandemic hit and organizations across the world started adopting MS Teams as the de-facto operating system of the remote workforce, we started wondering how simple and powerful it would be to converse with your data within MS Teams itself and collaborate seamlessly with your colleagues to discover insights and create value? And that’s how Beagle was born! How does Beagle do that? Beagle lowers the barriers of adoption and eliminates the need for training (of individuals) by taking data to people through a collaboration app such as Microsoft teams. Beagle shows relevant data to a user in form of Insight Cards and allows them to deep dive on it using filters within MS teams itself, and helps in faster decision making Beagle Studio brings in very high agility in creating the no-code analysis reports itself and any new analysis/ modifications can be created within hours and made available to the stakeholders Beagle has a set of advanced features like : Natural language inputs to get insights Search and share a Insight Card while chatting with a teammate ( in chat interface itself) Collaborate on insights with a teammate using Beagles Narrative board within MS Teams Ability to set custom notifications Download the Insight Card in form of a PPT and Excel Provide feedback on the Insight Card Beagle also brings in advanced analytics to users in ready to consume form : Truly “no code” environment to create Insight cards Availability of advance Virtual Analyst (VA) templates which can be used by just plugging the intended set of data into it. Example : Sales forecasting VA, Out of stock Analysis VA, Share Analysis VA, Sales Growth Decomposition VA Beagle integrates with all forms of data sources, be it from Excel files, Power BI dashboards or an Azure Data Lake Definitions: Insight Cards - A visual output that is generated (from multiple data sources) by Beagle to a query from the MS Teams user Virtual Analyst : A virtual analyst is an “BOT” entity with whom the end user interacts with on MS teams. Narrative Board - A narrative board is an Insight cards collective where multiple people can share their opinion on the set of information showed What are the modules of Beagle? There are two modules of Beagle : Beagle Studio and Beagle Viewer. Beagle Viewer : It is the user facing component that connects to any collaboration platform like MS Teams It facilitates the consumption of analysis through a guided, conversational experience It enables users to access Insight Cards directly through collaboration platforms like MS Teams or Slack. We really wanted users to be able to ask questions regarding the data they were consuming and the ability to find the necessary answers by deep diving into the Insight Cards. Hence we built filtering and sorting abilities into Beagle Viewer. Narrative Boards to build context around Insight Cards and notifications are other features that make interaction with Beagle Viewer a more enriching experience. Beagle Studio : It allows you to configure your data sources, create your analysis and do access control Beagle Studio can connect to multiple sources like Excel/ csv, RDBMS, Big Data or to your BI Tools like Tableau or Power BI. Beagle enables you to do cross functional analysis of data, User can analyse metrics from different sources at one place. Users can create Virtual Assistants, which are Microsoft Azure Bots, and configure them specifically for their analysis needs. Any information reports (called "Insight Cards") can be created in minutes using available card templates Challenges while developing Beagle : Metric builder was extremely challenging to build, more so because we wanted to harness our domain intelligence as well while building it. Also the fact that we are directing our efforts in creating a product with a shallow learning curve, didn't allow us to raise the complexity of the product in any way whatsoever. We are of course proud of the results that we have achieved with respect to metric builder.. We are also proud of Beagle Viewer and the opportunities that it provides for greater collaboration between teams and make the team meetings more productive. <div