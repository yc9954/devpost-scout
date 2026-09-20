---
slug: "eurocovidbusters"
url: "https://devpost.com/software/eurocovidbusters"
title: "IFFA (Integrated Fast Financial Aid)"
hackathon: "The European Commission's EUvsVirus Hackathon"
organization: "European Commission"
winner: true
words: 748
team_size: 6
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "domain/civic_government"
  - "domain/finance_payments"
  - "user/general_public"
  - "substrate/web_dom"
---

# IFFA (Integrated Fast Financial Aid)

> IFFA, the Integrated Fast Financial Aid, is a flexible & innovative platform that governments can use to accelerate COVID-related financial aid application and distribution among people and businesses

[Devpost](https://devpost.com/software/eurocovidbusters) · hackathon [[The European Commission-s EUvsVirus Hackathon]]

## Facets

  <sub>weak: deterministic_policy</sub>
**domain** [[civic_government]] [[finance_payments]]
  <sub>weak: immigration_refugee, labor_employment</sub>
**user** [[general_public]]
**substrate** [[web_dom]]
  <sub>weak: video_visual</sub>

**stack** amazon-web-services, bootstrap, cloud, css, flask, html, html5, javascript, jupyter, python, python-package-index, typeform

## Body

IFFA: financials IFFA: High level Architecture IFFA: Roadmap 1) The problem your project solves During the Corona crisis, some governments are overwhelmed by the influx of applications for financial aid. Assessing the eligibility of the applicants currently involves a considerable amount of manual effort, which also impedes proper fraud detection. Automating the process helps providing faster access to financial support where it is desperately needed. Many people and businesses depend on fast financial support from the government. Due to the sheer volume of requests, some government don't have the ability to swiftly provide financial needs to their citizens. Many people don't know where to apply (e.g. cross-border workers), applicants are not necessarily aware of mutually exclusive support programmes, or may have difficulties filling-in complex forms, maybe due to language barrier) 2) The solution you bring to the table Our project aims to support the governments by providing IFFA, an innovative, comprehensible and secure web interface, paving the way to a fast, automated and easy processing of financial support claims when it is urgently needed, now and possibly in future scenarios. IFFA is a website run by national or supra-national authority that allows applicants to manage their Covid-19 financial support. For the applicant: • In a first time, Applicant describes its situation in IFFA through multiple-choice questionnaire and IFFA sorts the aids to which he or she is eligible; • In a second time, Applicant fills-in its identification credentials from relevant tax authority delivering the aid and can fill-in its aid request directly through IFFA. For government officials: • Automation and standardisation of processing forms increase request processing efficiency increasing overall process smoothness, and in limiting workload • Consistency checks and controls reduce the number of ‘good faith errors’ and highlight potential fraud risks. 3) What you have done during the weekend We, the EuroCovidBusters started from scratch. Everything, from the first ideas, to an analysis of the current problems, designed decision trees of available financial support instruments, researched similar existing solutions and the development of the prototype took place this weekend. The combined length of our video calls amounts to 47 hours. 4) The solution’s impact to the crisis IFFA ensures that people receive adequate financial support during the crisis. This prevents businesses from bankruptcy, ensures everybody can pay their liabilities and relieves families from financial stress. IFFA does its small part at keeping the European economy alive. 5) The necessities in order to continue the project Funding for the first milestone of the project "creating release 1" with the following features: eligibility checks, Fraud/Consistency checks and a payment processing via existing application program interfaces (APIs). While developing the minimum viable product a second work stream identifies the first two suiting governments where the impact of implementing IFFA will maximised. The costs for achieving that milestone in 4 months are calculated to amount to 1.2 MEUR which includes employing 15 full time equivalent (FTEs) for development tasks and additional 3 FTEs for customer acquisition and project management. The preferred financing model is governmental funds that allow a project that will deliver a final open source product that potentially can be used and adapted by any government around the world. (see IFFA: Financials) 6) The value of your solution(s) after the crisis IFFA can be easily adapted to provide numerous services post-crisis: Any time a National government implements a new financial aid, these measures could be added to IFFA platform to ensure all citizens can check their eligibility and receive support in a speedy and user-friendly manner; Political decision makers can draw on solid, reliable and harmonized data to understand the effectiveness of past policies and for future decision-making; IFFA also holds the potential to be extended to all EU member states and beyond, during and post-crisis periods, to ultimately aid in processes harmonization and policy making. The URL to the prototype: http://63.33.197.236:5000/ The prototype showcases the process where users can enter there VAT-ID which are cross-checked for authentication. For the prototype we assume that all relevant data can be deducted from available governmental resources. Upon triggering the eligibility check, the data is submitted to the rules engine which automatically informs the user of his or her eligibility. Within the prototype for each request a random user is generated and evaluated accordingly. If he is eligible for financial support, the money will directly be transferred to his bank account (not implemented in the prototype). The lightweight implementation was prototyped using a flask server with a python back-end. https://github.com/Magelan88/IFFA.git <div