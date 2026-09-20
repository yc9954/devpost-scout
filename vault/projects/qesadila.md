---
slug: "qesadila"
url: "https://devpost.com/software/qesadila"
title: "Qesadila"
hackathon: "The European Commission's EUvsVirus Hackathon"
organization: "European Commission"
winner: true
words: 1170
team_size: 2
has_repo: true
has_live: true
has_video: false
tags:
  - "project"
  - "mechanism/provenance_signing"
  - "mechanism/realtime_stream"
  - "mechanism/vision_ocr"
  - "domain/civic_government"
  - "domain/developer_tools"
  - "domain/finance_payments"
  - "domain/health_clinical"
  - "domain/labor_employment"
  - "domain/legal_justice"
  - "user/developer"
  - "user/general_public"
  - "user/legal_professional"
  - "substrate/code_repository"
  - "substrate/document_pdf"
  - "substrate/financial_record"
  - "substrate/video_visual"
  - "substrate/web_dom"
---

# Qesadila

> Voting system for governments, city councils, corporations or anyone using Qualified electronic signature, X509 cert or PGP..

[Devpost](https://devpost.com/software/qesadila) · hackathon [[The European Commission-s EUvsVirus Hackathon]]

## Facets

**mechanism** [[provenance_signing]] [[realtime_stream]] [[vision_ocr]]
**domain** [[civic_government]] [[developer_tools]] [[finance_payments]] [[health_clinical]] [[labor_employment]] [[legal_justice]]
**user** [[developer]] [[general_public]] [[legal_professional]]
**substrate** [[code_repository]] [[document_pdf]] [[financial_record]] [[video_visual]] [[web_dom]]

**stack** avalonia, azure, c#, devops-pipelines, docker, github, github-actions, kubernetes, nuxt, vue.js

## How they structured the write-up

- the problem
- the solution
- what we did
- solution impact to the crisis
- after the crisis
- necessities in order to continue
- business plan propositions
- pitchvideo url
- thanks

## Body

Logo We have significantly increased test coverage in QesadilaBackend at the EUvsVirus hackathon Submission Qesadila EUvsVirus The problem Pandemic is chalenge for democracy . Maintain institutions nowaday means to protect elected representatives rights to participate on taking decisions. The city council meetings in many countries are (base on the law) personall, public and risky because of infection. For many citizens the municipalities are representing the democracy as closest institution. Many citizens participate on the public meetings to control representatives. Without any change we can expect spread of the virus between elected representatives and citizens joining meetings of the municipalities. During the time there could be so many victims , that remaining persons will not fully represent the citizens (voters). People in the quarantine , staying at home caring for relatives, or in the hospital have limited possibilities to participate . Many countries are looking for the solution . Unfortunately some politicians already started to limit the competencies of the city councils, temporary switching off the national parliament , arguing by protecting the representatives. Another politicians without IT security knowledge allowed to use risky tools for making decisions. European parliament temporary use e-mail voting , cities in Slovakia started to use video calls , e-mails, signed papers as the voting evidences. If real time deep fake video are possible, e-mail can be changed, anyone can doubt such a decision so as institutions, or democracy. The solution Qesadila allows secure online voting . Voter autorises each voting ballot by signature using eID based on PKCS#11 worldwide standard (commonly issued by governments), or PGP certificate, which can anyone generate using the Qesadila for free. The solution consists of Qesadila web (to display voting results, manage Voter Lists and Voting Forms), Qesadila Auth desktop application (for authorisation of the user and his ballots. Windows, macOS, Linux supported) Backend with logic, API, data storage. We have ambition to use Qesadila as an example of using modern technologies for governments. What we did We started to work on the solution only this month and this is our 3rd hackathon. During this hackathon we implemented: creation of the PGP certificate (for persons not using eID) in desktop application authorisation on the web * site by signing in desktop application using PGP certificate or eID improved workflows tooned GUI the solution is finaly localized to three languages and ready to easily add another languages. Solution impact to the crisis Using secure e-voting solutions like Qesadila will protect representatives from disease, allow to participate the representatives from quarantine, hospital, home allow to participate citizens from quarantine, hospital, home keep municipality / institution more representative and operational stop loosing necessery local leaders more people to participate, with longer time interval frame for voting strengthen democracy The municipalities are active looking for the secure voting solution and we are receiving suggestion and requests to check the solution. We feel strong need of our solution. After the crisis To keep using secure e-voting solutions like Qesadila after the pandemic will keep us prepared for another crisis allows to * participate from anywhere - e.g. business trip and will take to more representative decissions promote modern technologies do municipalities more effective and flexible save time , money, environment (with less transport to/from meetings, using less paper) Necessities in order to continue During this short month April 2020 we found out, that to develop proof of concept under the NGO Srdcom doma o.z. will not be enough . There are too many small cities and villages they doesn’t have IT cappacities to use our open source code and to build and run own system. To help them, means to provide the solution as cloud service , which means costs for cloud infrastructure, development, support. This can be done with viable success project . We are in a touch with local representatives in Slovakia, lawyers, having communication channells to members of the national parliament, which is necessary because every big change in the society influes the legislative. The new Slovak government supports electronic solutions and plans national electronic voting. We take this as so strong advantage, that we decided to use Slovakia and Cezch republic as pilot country for development. We have been contacted by IT companies representatives. We feel we have the good idea, which is needed by market . If is it so in a little bit conservative Slovakia, the need in other countries can be stronger. Beginning in May 2020 we plan to organize the pilot in few Slovak cities to get findings from real potential clients. This will take to prioritization of the possible features of the solutions, estabish cooperation with asociation of the cities and vilages in Slovak republic and Czech republic. add support od the Czech and Estonian eID and do roadmap of another countries ask for donation for start from non-commercial source, as we’d like to make the solution as cheap as possible for clients, create business and finantial plan in a cooperation with business consultants we met during hackathon, participate in programs supporting startups and inovations. Business plan propositions Problem worth solving maintain decision making offsite fullfill the national law with sharing information from municipalities to citizens Our solution e-voting system autorized with government issued eID, or PGP certificate public ballots with data to verify the voting process What’s unique focus on authorisation, certificates can be our strong specialistation, is defenetly strong side and can be almost unique with growing experiences in the time. It can take us to management of signed documents. Target market cities as a main type of client --141 cities in Czech republic [Source: https://sk.wikipedia.org/wiki/Zoznam_miest_na_Slovensku --607 cities in Czech republic [Source: https://cs.wikipedia.org/wiki/Seznam_m%C4%9Bst_v_%C4%8Cesku_podle_po%C4%8Dtu_obyvatel#Mapa_m%C4%9Bst_nad_10_000_obyvatel ] --50 000 cities in EU [Source: https://ec.europa.eu/social/main.jsp?catId=1141 ] EU, starting in Slovakia and Ceech republic The competition base on the infromation from municipalities in Slovakia, there is no e-voting system based on PGP / eID authentification. Sales chanels Internet Consultants teaching municipalities representatives Association of the cities and villages in Slovakia (ZMOS) Union of the cities of Slovakia (UMS) Expences cloud services based on transactions or monthly fees developers and support Milestones pilot grant to move from volunteering proof of concept to professional service first contract first contract with the city over 25 000 citizens Team long term core team from the project Biatec.cz for payment gateway data transformation for accounting purposes. We know, we will look for another roles to join our team. Partners short list of long term partners will be define during May 2020. Currently in touch with: law firm, consultants for municipalities, business consultants IT partners intrested in our PGP /eID Know-how. ##Prototype URL Web application “Qesadila web”: https://www.qesadila.com Download page - desktop application “Qesadila Auth” for Win, Mac, Linux: https://www.qesadila.com/qesadila-auth/ Code: Open source under GNU GPLv3 licence: https://github.com/Qesadila/QES https://dev.azure.com/Qesadila/_git/QesadilaBackend https://dev.azure.com/Qesadila/_git/QesadilaAuth Pitchvideo URL https://vimeo.com/zubo/qesadila-en Thanks For the support during EUvsVirus hackathon (24.-26.4.2020) we are very grateful for inspiration and strong support to Martina Pipiskova, Zuzana Nehajova, Eva Polivkova, for consuptation to Pavlina Louzenska so as to NGO Srdcom doma o.z., Commodity exchange Bratislava, AAA Auto. <div