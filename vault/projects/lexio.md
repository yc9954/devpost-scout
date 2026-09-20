---
slug: "lexio"
url: "https://devpost.com/software/lexio"
title: "Lexio"
hackathon: "Junction 2017"
winner: true
words: 441
team_size: 2
has_repo: true
has_live: false
has_video: false
tags:
  - "project"
  - "domain/legal_justice"
  - "user/legal_professional"
  - "substrate/financial_record"
---

# Lexio

> An easy and flexible price estimate service for legal assignments.

[Devpost](https://devpost.com/software/lexio) · hackathon [[Junction 2017]]

## Facets

**domain** [[legal_justice]]
**user** [[legal_professional]]
**substrate** [[financial_record]]

**stack** express.js, node.js, postgresql

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for lexio

## Body

Inspiration At the moment there are no automated price estimation services for law firms. Typically clients inquire about the cost of the assignment beforehand. Nowadays solicitors give estimates based on their previous experience with similar cases. Typically the costs are difficult and laborious to predict. What it does Lexio provides a price estimate of the probable cost of an assignment. The service uses data from CSI Lawyer to provide an insight on how much the client can expect to spend according to the total costs of similar cases. Lexio gives the lawyer a starting point for pricing the case and provides an easy to use interface to send an estimation to the client. How we built it We started by analysing a transaction data dump from CSI lawyer and modelled the typical structure of certain projects. Then we created an Express.js based web app with two interfaces, one for the client prospect and one for the law firm. Clients are able to fill in a simple case submission form. Once it's submitted, Lexio calculates an estimate for the assignment based on previous transaction data. This estimate is then presented to the lawyer, who can further adjust it according to the client's needs and her expertise on similar matters. Challenges we ran into In the beginning, the data was in a form that was a bit difficult to process. Furthermore our estimator would give more accurate results if there was more data to crunch. Also, given that we were only a team of two people and there was only two days to work on this project, we had to limit the scope and features of the project. Accomplishments that we're proud of We built a relatively nice looking and feeling interface for the estimator. What we learned Ville: I learned how to focus on the most crucial tasks to proceed on the critical path of the project. Also, I learned a little bit about data visualization. Olga: This hackathon gave me hands-on experience on the world of legal tech. I learned how a legal tech service such as ours can benefit both law firms and its clients. Especially cool was to step out of my comfort zone and put my theoretical legal knowledge into practice, look at legal services from both lawyers and clients perspective. What's next for Lexio We thought that the service could be extended so that the lawyer could use it without the need for a submission from a client first. Also the service could be extended to help lawyers and clients track the progress of an assignment and update the price estimate in the event of changes. <div