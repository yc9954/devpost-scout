---
slug: "stakeshield"
url: "https://devpost.com/software/stakeshield"
title: "StakeShield"
hackathon: "Theta Network 2024 Hackathon"
organization: "Theta Labs"
winner: true
words: 269
team_size: 0
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "mechanism/revocation_withdrawal"
  - "substrate/financial_record"
---

# StakeShield

> StakeShield is your ultimate guardian against crypto wallet hacks and stake disruptions. Developed by FuelFoundry, StakeShield consists of three powerful tools...

[Devpost](https://devpost.com/software/stakeshield) · hackathon [[Theta Network 2024 Hackathon]]

## Facets

**mechanism** [[realtime_stream]] [[revocation_withdrawal]]
**substrate** [[financial_record]]

**stack** php, python, web3

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for stakeshield

## Body

StakeShield Service Descriptions MetaForge StakeShield Dashboard Inspiration After years of managing and eventually inheriting the ThetaTech Community Discord, where members frequently sought help with their unstaked crypto by bad actors, we created StakeGuard to assist them. Due to popular demand, we finally developed a frontend for all Theta stakers. Welcome to StakeShield, a comprehensive solution for monitoring (VaultMonitor), alerting (StakeWatch), and protection (StakeGuard). What it does StakeShield includes two brand new solutions debuting at this year's hackathon: StakeWatch and VaultMonitor, which tie back into the existing StakeGuard-as-a-Service offering from FuelFoundry. StakeWatch monitors your stakes in real-time, sending email alerts to you (and us if desired) while VaultMonitor provides one location to monitor all of your lovely Theta Network assets in one convenient location. VaultMonitor optionally, when enabled, keeps an eye on your current balances and provides you with withdrawal notifications via email should they occur. How we built it We used PHP, Python and a wee bit of JS. Challenges we ran into Adding full support for TNT20 tokens, which requires more time. We have the critical functionality covered thankfully. Accomplishments that we're proud of Achieving detection of withdrawals and unstakes within 5 minutes, compared to our original 4-hour target, saving to date over $2 million in USD of potentially hacked THETA, TFUEL and TNT20 tokens, and to-date operating at a 100% success rate. What we learned The Theta Protocol Ledger has many options that require reverse engineering to understand fully, but it’s worth the effort. What's next for StakeShield Adding full support for TNT20 token balances and TNT20 unstakes from subchain validators and simplified enrollment into StakeGuard. <div