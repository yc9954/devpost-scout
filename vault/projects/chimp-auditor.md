---
slug: "chimp-auditor"
url: "https://devpost.com/software/chimp-auditor"
title: "Chimp Auditor"
hackathon: "DocuSign Good Code Hackathon"
organization: "Docusign"
winner: true
words: 482
team_size: 1
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/retrieval_grounding"
  - "domain/developer_tools"
  - "user/developer"
  - "substrate/document_pdf"
  - "substrate/geospatial"
  - "substrate/structured_db"
  - "substrate/transcript_audio"
  - "substrate/video_visual"
---

# Chimp Auditor

> Review and Approval of Eastern Chimpanzee Range maps involving embedding of ArcGIS maps in Docusign envelopes ,using the Docusign Developers API, and Decision makers Sign-off.

[Devpost](https://devpost.com/software/chimp-auditor) · hackathon [[DocuSign Good Code Hackathon]]

## Facets

**mechanism** [[retrieval_grounding]]
**domain** [[developer_tools]]
**user** [[developer]]
**substrate** [[document_pdf]] [[geospatial]] [[structured_db]] [[transcript_audio]] [[video_visual]]

**stack** docusign, esri, express.js, mysql, node.js, react

## How they structured the write-up

- inspiration
- what it does
- how i built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned

## Body

Stakeholders Audits and Review Cycles Map Review Final Approval Document Signed Envelope Data Embedded map in doment Dashboard Inspiration I was waiting for the Docusign Good Code Hackathon 2021. As I participated and won the Docusign Hackathon in 2020, I was wondering what new I could do this time with the Docusign APIs. I went through the resources of the JGI challenge and I fixed my mind I should produce a best solution for their requirements. It started this way.. What it does The application helps the JGI to review, update and publish the dynamic conservation maps of the Eastern Chimpanzee Range. The application involves a GIS user to enter with his/her Docusign Credentials. Users can be added to a user group of Stakeholders. The GIS user creates review cycles with a map file exported from ArcGIS online. The map is embedded with a document and sent to all the users in the group using the Docusign API. The user can view status of sent envelopes and view the data from the signed envelopes as well. The user can create multiple review cycles by updating the changes, and send a final approval document and when everyone signs it, a new version of map can be published. How I built it The application is built using Docusign SDK, Nodejs, React, MySQL The React app uses Docusign Implicit Grant Authentication to authenticate user. The react app communicates with the nodejs backend application which consists of APIs that handle every actions with the Docusign, Docusign APIs used (using Nodejs SDK): Envelopes (creating envelopes by using text tabs, draw tabs etc) Envelopes Status (get status of envelopes) Envelopes Page Image (to get the map image) Envelopes Comments Transcript (to get all the comments in an envelope) Envelopes Form Data (to get the User inputs from envelopes) Users User Groups. ArcGIS online is also involved in the application for updating and exporting the conservation maps. All audit, review and envelopeIDs are stored in the database. Challenges we ran into I initially decided to go with BulkSend API, I almost completed implementing the API but later found out that, I can send only same envelopes using the BulkSend, where dynamic updating of envelopes is not possible. This has consumed more time. Finally, I started creating envelope with specific tabs for each envelope and sending it one by one. Accomplishments that we're proud of I am proud that I tried to use most of the Docusign APIs that fits the use case of the application. What we learned Learnt a lot about Chimpanzees and the importance of conserving them. Got a deeper understanding of the Docusign APIs. Got Familiar with Docusign Documentation :) ## What's next for Chimp Auditor If my solution fits the requirements of the Jane Goodall Institute, I can work with improving the current solution by working on changes and improving the user experience ! <div