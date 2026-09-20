---
slug: "update-with-excel-csv"
url: "https://devpost.com/software/update-with-excel-csv"
title: "Update with Excel / CSV"
hackathon: "monday.com Apps Marketplace Challenge: solutions for teams "
organization: "Monday.com"
winner: true
words: 262
team_size: 1
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "substrate/structured_db"
---

# Update with Excel / CSV

> Update board by loading changes from Excel or CSV file.

[Devpost](https://devpost.com/software/update-with-excel-csv) · hackathon [[monday.com Apps Marketplace Challenge- solutions for teams]]

## Facets

**substrate** [[structured_db]]

**stack** react

## How they structured the write-up

- inspiration
- what it does
- how i built it
- challenges i ran into
- accomplishments that i'm proud of
- what i learned
- what's next for update with excel / csv

## Body

Inspiration App idea was mentioned in #mydreamapp inspiration board and "Update with Excel / CSV" was created. What it does It allows to update or create new items on board from Excel and CSV files. User can review changes before updating board (table with changes is displayed). There are three steps to use the app (see video with full demo): Export board to Excel or start with new file Make changes in Excel file Upload changes to board Example use cases: Use Excel calculations/simulations results to update the board. Export data from external systems to Excel or CSV, and then update the board. How I built it I started with create-react-app and build simple prototype. App was then extended to include review stage, where user can see changes that will be applied to the board. It is hosted on AWS CDN to get fast loading speeds. It took few iterations with feedback to get it to current state. Challenges I ran into Error reporting to the user was challenging because monday.api() call is returning generic error without specific error code. There was an update in community that specific error reporting will be available soon. Accomplishments that I'm proud of Creating functioning app with video presentation and demo. What I learned Updating items API and more options in video editing tool. What's next for Update with Excel / CSV Adding support for more column types and reporting errors from API when it becomes available. If you would like any addition to the app to cover your use case, please let me know. <div