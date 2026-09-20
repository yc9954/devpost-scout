---
slug: "flowpath-uslge3"
url: "https://devpost.com/software/flowpath-uslge3"
title: "FlowPath"
hackathon: "Power Up Automation"
organization: "UiPath"
winner: true
words: 666
team_size: 3
has_repo: false
has_live: true
has_video: false
tags:
  - "project"
  - "mechanism/vision_ocr"
  - "domain/finance_payments"
  - "substrate/financial_record"
  - "substrate/web_dom"
---

# FlowPath

> Establishing a powerful integration between the two most popular automation tools - UiPath and Microsoft flow.

[Devpost](https://devpost.com/software/flowpath-uslge3) · hackathon [[Power Up Automation]]

## Facets

**mechanism** [[vision_ocr]]
**domain** [[finance_payments]]
**substrate** [[financial_record]] [[web_dom]]

**stack** api, json, swagger, webhook

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for flowpath

## Body

Team - Santhosh Selvam , Dinesh Balasubramanian , Suresh Subbarayalu Inspiration UiPath is the most popular RPA software in the market. On the other hand, MS flow is the most popular cloud based automation tool with a tight integration with the Office applications and more than 250 external connectors like LUIS, Azure, Computer vision, Ethereum, Salesforce, ServiceNow, Bitbucket, JIRA etc. Deep integration between these two powerful platforms will open up numerous opportunities to automate the processes and eliminate some of the existing limitations. A custom connector is built for UiPath to integrate with MS Flow platform. Both are widely used in the enterprises to achieve automation goals. This integration will ensure a proper connection to bridge the gaps, push the limits and improvise the automations . What it does Orchestrator API and Webhooks are combined with the MS flow custom connector creation to define and develop triggers and actions in accordance with the Custom Connector framework. The New Uipath cloud and API authentication mechanism are used to build the connector. UiPath Triggers added to MS Flow When a Job completes successfully When a Job fails when a new item added to queue Actions added to MS Flow Start a Job Add a Queue item Get all Releases Get all Processes Get Job status Wiki Installation Creating connection Triggers Actions Technical possibilities Execute UiPath robots based on diverse amount of triggers available with MS flow (inbuilt, custom and third party). Examples - Triggers from SharePoint, Outlook, Facebook, Twitter, GitHub, JIRA, Salesforce, Workday, MS Kaizala, Azure, Slack.... Execute workflows on MS flow platform with triggers from UiPath . Example - Run a skype flow to notify the stakeholders on successful UiPath job completion. Orchestrator webhooks are configured in MS flow to build a custom connector for UiPath Train the models built in with AI builder and use the processed data in UiPath jobs Connect with AI services like LUIS, Face API, computer vision with the UiPath workflows thru MS flow Build PowerApps for Mobile and web to provide a easy user interface to the users to run/monitor the automations Build Microservices combining MS Flow with UiPath using HTTP request feature of MS Flow Use Cases Run Uipath job on a file is added or modified to sharepoint, Google drive, OneDrive.. Run Uipath job on arrival of particular emails (Invoices, Reports...) Process Invoices/Receipt thru trained models in AI builder and execute UiPath jobs with the extracted data Execute other onboarding processes when a new employee is added to workday On any uipath event (job completion, failure etc..) get notified thru skype, MS teams, Slack, SMS, mobile push notifications ... Create and process Surveys Setup Approval flows References https://orchestrator.uipath.com/v2019/reference#consuming-cloud-api https://forum.uipath.com/t/consuming-apis-with-the-new-cloud-orchestrator/123112 https://docs.microsoft.com/en-us/flow/#pivot=start https://www.pcworld.com/article/3401459/microsoft-adds-ai-capabilities-to-powerapps-and-flow-to-automate-business-tasks.html https://india.flow.microsoft.com/en-us/connectors/ How we built it FlowPath connector is built using the Custom Connector option for Microsoft flow to interact with UiPath. Orchestrator REST APIs and Webhooks are the base for building the connector. We built the connector swagger from scratch to test each option and define the necessary parameters Each trigger and action is a http call with the necessary request parameters and the response schema is defined as per the specifications provided UiPath. Challenges we ran into Several challenges were faced in building this connector like Authentication mechanism for the community edition is revamped recently and the new one was very hard to integrate with Flow Defining the UiPath outbound webhooks as Triggers in Flow was a big challenge because of the thin documentation by Flow in this area Accomplishments that we're proud of Introducing a huge set of triggers to execute UiPath jobs/actions Extending the connector ecosystem of MS flow to UiPath which benefits both the applications Finding an alternative approach to the revamped cloud api authentication which took too much to break What we learned Quantum of benefits by integrating UiPath MS flow Infinite opportunities in designing an ideal automation with this integration What's next for FlowPath More actions Once Cloud API authentication moves to OAUth 2.0 flow, it will be integrated into FlowPath <div