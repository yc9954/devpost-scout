---
slug: "polymetis-pii-protection"
url: "https://devpost.com/software/polymetis-pii-protection"
title: "PII Protection"
hackathon: "Codegeist 2021"
organization: "Atlassian"
winner: true
words: 953
team_size: 4
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/structural_withholding"
  - "domain/developer_tools"
  - "domain/finance_payments"
  - "user/developer"
  - "substrate/document_pdf"
  - "substrate/structured_db"
---

# PII Protection

> Optimize Data Security and Privacy in Jira

[Devpost](https://devpost.com/software/polymetis-pii-protection) · hackathon [[Codegeist 2021]]

## Facets

**mechanism** [[structural_withholding]]
**domain** [[developer_tools]] [[finance_payments]]
**user** [[developer]]
**substrate** [[document_pdf]] [[structured_db]]

**stack** customui, forge, javascript, react

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for pii protection

## Body

PII can check all issues in your Jira instance for sensitive data. Of course, it also checks incoming Service Requests written by your customers PII findings are displayed for admins only in a concise overview, so that you take the appropriate actions More than a dozen checks are already included with many more to come soon! Inspiration As developers, we have all heard of Little Bobby Tables and hence we check every user input. But malicious code is not the only thing to worry about, especially from a privacy or security perspective. A lot of valid user input can still be sensitive and should not be stored in your Jira instance. Whether it’s the carelessly uploaded password to a production system in a bug report or a customer asking for support and sending along their credit card: Sensitive data can get into Jira a lot quicker than admins want it to or can prevent. As an admin (or SecOps or Privacy Advocate or Compliance Manager), you simply cannot read every comment, every incoming Service Request. But our app, PII Protection, can! Before we developed PII Protection, we had been looking for a long time for an app that manages the control of sensitive data in Jira. Finally we had to build it ourselves. Thanks to Forge, we could finally do so in a secure manner! What it does PII Protection checks every change to string fields (like summary and description) and comments in Jira for sensitive data and alerts admins to any findings. What it checks for is customizable and it currently supports more than a dozen checks, helping admins to find credit card numbers, password or banking information with many more checks coming soon. The app’s findings are only available to admins and can be seen in a table. Admins can remove findings or click a link to be taken directly to the issue in question. How we built it As stated before, we wanted to make sure that we touch sensitive data as little as possible, Forge made this possible. Whenever an issue or comment is created or updated, a Forge function is triggered. PII then checks whether the change introduces sensitive data into the instance. In case it find’s anything, our App notes the time, date, type of finding as well as the issue in question and add it to the findings list. Given the constraints inherent in Forge (ex. no more than 10s of runtime), our goal was to keep everything running fast without any calls to outside systems. Challenges we ran into Although we enjoyed building this app, there were a few challenges: Forge Storage We needed a way to store some settings data as well as all the findings of potentially sensitive data. Forge Storage was the natural choice and it does work great. However, it is quite limited when it comes to querying abilities, at least coming from a full-featured database. When you run your own database, you get to use all kinds of queries, with Forge Storage you are (currently) limited to a key-value store where the only way to search for documents is by how their key starts. It’s not that bad though, if you're aware of this constraint, have a use-case that fits well and plan your data model accordingly. Redacting Data Originally, we wanted to give admins the option to have the app automatically redact all of our findings. While this is easily done, we opted against it for now, as it would not increase the security of PII data. Any data we would redact would still be available in the issue history, as there currently is no way to suppress the issue history or mark an entry as private. Of course, we did file a Suggestion – FRGE-335 – for this. App Permissions Sometimes we did not receive notifications for events in certain projects. Given that our app has all the right permission scopes, this was puzzling at first – until we found out about FRGE-212 . Apparently, due to the way that Forge and permissions work, in some cases our app would simply not receive all required permissions for all projects and hence would not receive events. The workarounds list in FRGE-212 worked perfectly, but it was quite a journey to actually find the problem – simply not receiving some events hardly felt like a permissions issue at first and we did quite some chasing around until we found and solved the problem. Accomplishments that we're proud of Before we had Forge, an app like this simply wasn’t possible. Sure, you can subscribe to events with Connect and perform the same checks we do in an Atlassian Connect app. But that app would be external to a customer’s Jira instance, which basically means that, in order to find out whether some data is sensitive and should not even be in Jira, you would have to export it to a 3rd party first. Forge lets us avoid this problem by keeping everything running within Altassian systems. Also, PII Protection available on the Marketplace today! That’s pretty neat, too 😃 What we learned Working with Forge is quite different from Connect, with its own advantages and challenges. Since there’s no automatic live logging in production, we need to make extra sure that our app recovers well from errors Despite Forge’s current limitations, there’s already a lot possible if you think creatively. What's next for PII Protection We are very excited about our new app and have many ideas to develop it further: More checks Different ways to automatically handle PII data in your instance Direct notifications for admins Listen to customer feedback … we are available on the Marketplace after all <div