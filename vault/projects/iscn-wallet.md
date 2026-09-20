---
slug: "iscn-wallet"
url: "https://devpost.com/software/iscn-wallet"
title: "ISCN wallet"
hackathon: "Cosmos HackAtom VI "
organization: "Cosmos"
winner: true
words: 192
team_size: 1
has_repo: true
has_live: true
has_video: false
tags:
  - "project"
  - "domain/developer_tools"
  - "user/developer"
  - "substrate/code_repository"
  - "substrate/financial_record"
---

# ISCN wallet

> Create, update and transfer your own ISCN.

[Devpost](https://devpost.com/software/iscn-wallet) · hackathon [[Cosmos HackAtom VI]]

## Facets

**domain** [[developer_tools]]
**user** [[developer]]
**substrate** [[code_repository]] [[financial_record]]

**stack** cosmjs, iscn-js, vue.js

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for iscn wallet

## Body

Create/Update ISCN Batch Create/Update List ISCN By Owner Find ISCN By ID Inspiration Currently, there's no online tool for users who want to update ISCN or batch create ISCN. What it does Users can (batch) create, update ISCN, transfer ISCN, list ISCN by owner address and find ISCN by ID with the tool. How we built it Vue.js + cosmjs + iscn-js Challenges we ran into During the development, we found out that including multiple "create ISCN" messages in one transaction will cause an error. After some investigation, we figured out the module will generate the same ISCN ID for every ISCN in the same transaction and cause the error (ID should not be duplicated for newly created ISCN), so users need to sign the transaction one by one currently. We also reported the bug to the chain development team. Accomplishments that we're proud of Report a module bug about the "create ISCN" message. What we learned Analyzation of the module source code is also an important part for front-end developers. What's next for ISCN wallet Improve the UI design, add more descriptions about what's ISCN and how to create ISCN. <div