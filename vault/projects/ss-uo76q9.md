---
slug: "ss-uo76q9"
url: "https://devpost.com/software/ss-uo76q9"
title: "Harmoney"
hackathon: "Quick Base Virtual Hackathon"
organization: "Quickbase"
winner: true
words: 717
team_size: 1
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "domain/finance_payments"
  - "domain/transportation"
  - "user/frontline_worker"
---

# Harmoney

> Providing easy credit facilities to all

[Devpost](https://devpost.com/software/ss-uo76q9) · hackathon [[Quick Base Virtual Hackathon]]

## Facets

**domain** [[finance_payments]] [[transportation]]
**user** [[frontline_worker]]
  <sub>weak: financial_record</sub>

**stack** node.js, quickbase, react

## How they structured the write-up

- problem statement :
- what it does
- how i built it
- challenges i ran into
- what i learned
- what's next for harmoney

## Body

Landing page Loan Request form User profile Loan status Data model Problem Statement : In many low-income groups, people do not have access to credit opportunities as easily as the others. For example, a vegetable vendor, or a rickshaw driver, will require some amount of money as an initial investment each day to start their daily business activities. However, there is no bank or private institution which could cater to the needs of these people. Since, these kind of customers belong to a high-risk category, most institutions are reluctant to grant them loans. Hence, such people rely on a small scale money dealer, who charge a heavy rate of interest (eg: charging 1-2% each day, which is expensive in the long run), even if the person could be a decent borrower. Thus, these groups of people are exploited, by charging them heavy rate of interests, just because they are not able to prove their credit worthiness. What it does Harmoney aims to create value for these groups of people by: 1) Assisting these people build a credit history, so that the loan sanctioning process in made easier 2) Provide a platform for the lenders to interact with these customers 3) Help them in getting micro loans to get started with their businesses Through the Harmoney platform, lenders can provide loans to these customers through a regulated interest schedule. In case there is a default in paying back the loan, the lenders can negotiate an insurance with Harmoney, instead of head hunting individual borrowers. How I built it The data model of the Harmoney app consists of the following: Customers : Whenever a new customer logs in to the system, all the information like his name, email, phone, address, verification ID, etc would be recorded here. Loan Details : A new loan request would be recorded in this table, consisting of fields like purpose of loan, loan amount, rate of interest, EMI amount, principal and interest components of EMI, tenure of the loan, etc Applications : The customers and loan_details tables have a many-to-many relationship and the applications table is used as an intermediate table to achieve that. Tradelines : This table has the month-on-month record of the days past due (DPD) field, which is the key performance indicator for measuring how good/risky a customer is. If a customer defaults on a payment, then the DPD for that month increases. Thus, the month-on-month DPD history for a customer will give us an idea of how good or risky the customer is. Cashflow : The monthly due amount and the collected amount received from a customer is recorded here. The pipelines used to for automating the workflow of the Harmoney app consists of the following: Whenever a new loan is requested, a slack message is sent to the loan approver in the slack channel. For each approved loan, a default tradeline is inserted with DPD=30(meaning payment missed for current month), which gets updated once EMI for current month is paid. If someone makes a payment for the current month, the DPD = previous DPD - 30, to indicate a successful payment and no due. On the 1st of every month the pipeline is scheduled to insert a tradeline for each active loan with DPD = previous DPD + 30, which is updated by the other pipeline if payment is made. To build the web application, I used the following technologies: ReactJs: To build the front end of the app, where users can login and request for a new loan Quickbase REST APIs : They were used to fetch an app, insert/update data in Quickbase and to query data. Challenges I ran into Learning a new data management tool and its advanced features and implementing them from scratch was a great learning experience. What I learned I learnt how to use Quickbase and all its powerful features like relationships between tables, lookup and summary fields, Pipelines to automate the data inflow and data automations, integrating pipelines with external tools like Slack, Docusign, etc. and creating dashboards for the monitoring various key performance indicators of the organization. What's next for Harmoney The Harmoney app will also aim to enter other niche areas of personal finances, mutual funds, etc for the low-income groups, as these people are unaware of such facilities. <div