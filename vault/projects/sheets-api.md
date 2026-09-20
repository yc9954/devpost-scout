---
slug: "sheets-api"
url: "https://devpost.com/software/sheets-api"
title: "Sheets API"
hackathon: "The Postman API Hack"
organization: "Postman"
winner: true
words: 274
team_size: 1
has_repo: true
has_live: false
has_video: false
tags:
  - "project"
  - "domain/developer_tools"
  - "user/developer"
  - "substrate/structured_db"
---

# Sheets API

> Launch an express API easily using a google sheet as DB for quick MVPs or prototypes

[Devpost](https://devpost.com/software/sheets-api) · hackathon [[The Postman API Hack]]

## Facets

**domain** [[developer_tools]]
**user** [[developer]]
**substrate** [[structured_db]]

**stack** api, express.js, google-client-authentication, node.js

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for sheets api

## Body

Inspiration Spreadsheets are still a thing 😵, we find it always and they will always get in queue again. When browsing for JavaScript libraries that works with spreadsheets I founded some that worked with Google Sheets and also provided interesting API solutions to use them. This made me think that would be interesting to have an express-ready solution to work with a Google Spreadsheet either to mock a datastore or to even provide a solution when spreadsheets are heavily used, how about pushing reports to Google Spreadsheet from your express API and schedule it with CRON 🙀 What it does Express Sheets provides basic CRUD actions towards Google Spreadsheets to create REST APIs or communicate with Google Spreadsheets How we built it We built it using google npm libraries, google-spreadsheet & express Challenges we ran into Querying spreadsheets as if it were a Database & complicated setup process from Google developers Accomplishments that we're proud of Managed to connect any tabs and data and have CRUD actions in one-liner, with: router.use('/users', connectTab('Users')) We get: http://localhost:3030/api/users GET http://localhost:3030/api/users/:id GET http://localhost:3030/api/users POST http://localhost:3030/api/users/:id PUT http://localhost:3030/api/users/:id DELETE What we learned Google APIs and authentication methods What's next for Sheets API Would like to have a library around this so it can be used for different problem spaces, also: [ ] Add support for custom ID options [ ] Add support for (tab) table relations [ ] Support refresh token update [ ] Enhance setup documentation & process [ ] Add TypeScript support [ ] Add linter [ ] Add semantic-release config [ ] Create npm library [ ] Add tests [ ] Add a UI dashboard <div