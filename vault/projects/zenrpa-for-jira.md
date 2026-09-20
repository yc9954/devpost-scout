---
slug: "zenrpa-for-jira"
url: "https://devpost.com/software/zenrpa-for-jira"
title: "ZenRPA Triager for JIRA"
hackathon: "Codegeist 2020"
organization: "Atlassian"
winner: true
words: 751
team_size: 2
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "domain/finance_payments"
  - "domain/health_clinical"
---

# ZenRPA Triager for JIRA

> TurboTax for issue triage. Build your own simple triage flow without code.

[Devpost](https://devpost.com/software/zenrpa-for-jira) · hackathon [[Codegeist 2020]]

## Facets

**domain** [[finance_payments]] [[health_clinical]]

**stack** express.js, mongodb, nextjs, postgresql, react

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for zenrpa for jira

## Body

Inspiration As product builders, we have collectively spent the past 7 years leading product teams and using JIRA at 3 major unicorn companies representing over $1B worth of annual recurring revenue. We've found that large Enterprise B2B companies have unique challenges when it comes to customer issue triage: We tended to have large enterprise contracts that customer success managers had a huge incentive to protect We tended to have large enterprise prospects that account executives had a trememdous incentive to win We tended to have major partnerships that business development folks had a large incentive to grow and unblock The Pareto principle applied: 80% of revenue came from less than 20% of our logos, a highly uneven distribution Unsurprisingly, each stakeholder thinks the issue THEY filed in JIRA is the most important. Typically, whoever has the loudest voice wins this tug-of-war. Finally, we all know that one person who only ever chooses "P1" severity when filing their issue. Yes, you know who I'm talking about. Everything is a P1 to that person. FTW! We believe product teams everywhere are underserved for this conundrum. We believe they are missing a powerful, informative, and opinionated triaging tool within their own issue tracking systems. What it does Our product is an embedded issue triager tool for JIRA. It is a meticulously crafted and opinionated re-design of the way a Product team triages incoming issues in the Enterprise B2B context. Our product lets Product teams take a TurboTax-like approach to triage issues within JIRA Software. For every issue that gets filed, a PM is guided through a series of simple questions and verifications. At each step, the PM is presented with just the data they need to triage, pulled from a CRM, analytics tool, or internal Admin, conveniently into the JIRA issue. Each step has a simple one-click answer. When we showed our designs to Product teams, they were excited, but we learned that their triage processes differ so much that they needed a way to actually build their own process in. So: Our product is not only the issue triage tool itself, but also a no-code app builder that lets Product teams make a triage tool of their own. How we built it We used the Atlassian Connect framework to build a triage interface for Product Managers directly into issues in JIRA. A webpack bundle carrying a React app is deployed into the JIRA environment. Since Product teams have different requirements for their triage process, and require different data inputs, we built an intuitive no-code app builder that actually re-compiles the triage app for a Product team's specific process. Some features include: Connect your CRMs, analytics tools, and internal Admins to source data from Pull your customer profiles (ex: Salesforce Account record) and analytics context right into a JIRA issue Build the connected path of TurboTax-like questions a PM can quickly answer for every issue they triage Challenges we ran into We got super constructive feedback on our tool from various Product teams. As a result, we had to re-architect some of our earlier product designs when we learned that they had such uniquely different triage processes that they needed flexibility to re-build the triage tool for their process. Accomplishments that we're proud of We landed a proof-of-concept launch with a major unicorn company that will put our TurboTax-like triage approach to the test, so we can prove that our approach really works even at scale. We believe the next generation of 1M users of JIRA will need simple but powerful triage capabilities, and we're very proud to deliver that for them. What we learned From interviewing customers and showing them our app designs, we learned why they would pay for our solution: Issue triage happens faster , when PMs don't need to pull up the process on a Google Doc and gather data such as customer ACV from Salesforce, usage stats from Mixpanel, etc. Issue triage becomes fair and consistent , which avoids the "loudest voice in the room" situation Issue triage becomes measurable for the first time, because you can capture the entire timeline of actions and what specific actions the PMs take in the course of triaging, you can see your team impact from triaging right When we learned this, we published our findings to our quick landing page for this product! What's next for ZenRPA for JIRA We're gearing up to run the POC with a potential enterprise customer and are focused on making that a success by August. <div