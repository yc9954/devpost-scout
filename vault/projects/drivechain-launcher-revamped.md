---
slug: "drivechain-launcher-revamped"
url: "https://devpost.com/software/drivechain-launcher-revamped"
title: "Drivechain - Revamped Launcher and Thunder"
hackathon: "Bitcoin 2025 Official Hackathon"
organization: "Bitcoin++"
winner: true
words: 265
team_size: 1
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "domain/developer_tools"
  - "substrate/code_repository"
---

# Drivechain - Revamped Launcher and Thunder

> Drivechain Launcher and sidechain Thunder reimagined with a revamped UI and improvements

[Devpost](https://devpost.com/software/drivechain-launcher-revamped) · hackathon [[Bitcoin 2025 Official Hackathon]]

## Facets

  <sub>weak: revocation_withdrawal</sub>
**domain** [[developer_tools]]
**substrate** [[code_repository]]

**stack** electron, rust

## How they structured the write-up

- inspiration
- how i built it
- challenges we ran into

## Body

Wallet tab Fast Withdrawal tab Settings About dialog Chains tab Inspiration Drivechain is unique among Bitcoin scaling solutions because it enables completely new functionality through sidechains while maintaining Bitcoin's security model. I've always found that most blockchain tools prioritize function over design and UX. Both Drivechain Launcher and Thunder was no exception - powerful and useful, but lacking the polished UI experience that makes applications truly enjoyable to use. I'm a huge fan of simple yet modern design philosophy. When I tried the Drivechain Launcher, I immediately saw an opportunity to transform it into something that not only works well but looks and feels amazing. I wanted to create an experience where managing blockchain nodes feels as intuitive and elegant as using any professional desktop application. Similary, I wanted to do improvements on the sidechain Thunder. How I built it I approached this redesign methodically: First, I analyzed the codebase and created a plan for the redesign of both the Drivechain Launcher and Thunder. Apart from the revamped UI, I fixed the open issues reported in the Drivechain Launcher github repo. I also added some features and fixes to the Thunder sidechain as well. Challenges we ran into The challenge was to truly understand the current codebase and improve the design of the app incrementally making sure no existing functionalities broke while I improved the design. The Drivechain Launcher was built using Electron while Thunder was built using Rust. Fixing issues and adding new features on existing large codebases are always a challenge and I had to be very careful while I did that. <div