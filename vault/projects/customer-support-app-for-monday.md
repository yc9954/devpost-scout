---
slug: "customer-support-app-for-monday"
url: "https://devpost.com/software/customer-support-app-for-monday"
title: "Customer Support App For Monday"
hackathon: "monday.com Apps Marketplace Challenge: solutions for teams "
organization: "Monday.com"
winner: true
words: 285
team_size: 1
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
---

# Customer Support App For Monday

> Provide customer support for your user without leaving monday with gmail or outlook

[Devpost](https://devpost.com/software/customer-support-app-for-monday) · hackathon [[monday.com Apps Marketplace Challenge- solutions for teams]]

## Facets


**stack** mysql, php, vue

## How they structured the write-up

- inspiration
- what it does
- how i built it
- challenges i ran into
- accomplishments that i'm proud of
- what i learned
- what's next for customer support app for monday
- testing instructions

## Body

Available Integrations Chat View Inspiration While providing customer support the customer send mails. Then the mails have to be added to the board item and reply using the other mail clients (gmail/outlook). What it does This app allow user to provide customer support for user with out leaving monday.com. Currently there are two integrations Gmail and Outlook. How I built it The backend was built using php and mysql. The frontend was built using vuejs. The gmail rest api and Microsoft graph api are used along with monday.com graphql api. Challenges I ran into I ran into many challenges and forget it everything. Accomplishments that I'm proud of I finished at time. What I learned I learned how to use monday.com how to make app for it. I learned gmail api, outlook api, monday.com api. What's next for Customer Support App For Monday Add support for many other chat providers (facebook, telegram, ...). The big current limitation is one board can contain only one chat provider account (eg. gmail or outlook). So update it to support many chat providers per board. Testing Instructions Add App to the account Add an integration 2a. Authorize monday.com (first time only) 2b. Select account (Gmail/Outlook). Outlook integration doesn't support add/remove label. 2c. Authorize the selected account (first time only) (Gmail shows unverified app page since the app is not verified by google. Ignore it and continue) Add the customer chat view in item view. Select chat id field and email id field from settings. Owner field is optional. Send mail to the linked email. It will be added as the item in the board. Reply using the customer chat view. It will work according to the integrations set.. <div