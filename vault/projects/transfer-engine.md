---
slug: "transfer-engine"
url: "https://devpost.com/software/transfer-engine"
title: "Transfer Agent"
hackathon: "The Postman API Hack"
organization: "Postman"
winner: true
words: 187
team_size: 1
has_repo: false
has_live: false
has_video: false
tags:
  - "project"
  - "substrate/document_pdf"
---

# Transfer Agent

> Facilitate Data/File Transfer and Test services between local and Remote using various protocols (SFTP,...) thru POSTMAN ecosystem

[Devpost](https://devpost.com/software/transfer-engine) · hackathon [[The Postman API Hack]]

## Facets

  <sub>weak: multi_agent</sub>
**substrate** [[document_pdf]]

**stack** express.js, heroku, node.js, postman, sftp

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for transfer agent

## Body

transfer-agent-download-request transfer-agent-upload-request transfer-agent-environment transfer-agent-mock-server chai-like-unit-tests transfer-agent-monitor monitor-notification-mail transfer-agent-document documenter-transfer-agent collaboration-comments collaboration-comments-notification Inspiration integrates different API services (Postman, SFTP,...) to participate to the POSTMAN API challenge What it does facilitates automatic data/file transfer between local and remote using various protocols (SFTP,...) and managed thru POSTMAN tools (workspace, collection, mock, documentation,...) How we built it define and organize API requests within POSTMAN collections collaborate with comments exchange within POSTMAN collaboration module configure environment variables with POSTMAN Environment module test the API requests using POSTMAN desktop agent configure testing with POSTMAN mock-server module document API using POSTMAN document tool monitor with POSTMAN monitor tool, which sends mail notification on errors Challenges we ran into make POSTMAN monitor successfully the service due to systematic errors "NETERR: getaddrinfo ENOTFOUND" at the beginning. Finally the correct fix has been found and applied to avoid the errors Accomplishments that we're proud of implement the API with all POSTMAN integrated tools (workspace, collections, document, monitor, collaboration, mock-server, ...) What we learned POSTMAN integrated tools (workspace, collections, environment document, collaboration, monitoring, mock-server, ...) What's next for Transfer Agent Adapt the transfer agent service on Dropbox <div