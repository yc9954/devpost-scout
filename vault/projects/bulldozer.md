---
slug: "bulldozer"
url: "https://devpost.com/software/bulldozer"
title: "Bulldozer"
hackathon: "IGNITION | A Global Solana Hackathon"
organization: "Solana Capital"
winner: true
words: 529
team_size: 2
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "domain/developer_tools"
  - "user/developer"
  - "substrate/code_repository"
---

# Bulldozer

> Programming is hard, working with the latest tech is even harder. Builders need power tools to make their dreams come true. Bulldozer makes it easier to create and maintain Solana programs.

[Devpost](https://devpost.com/software/bulldozer) · hackathon [[IGNITION - A Global Solana Hackathon]]

## Facets

**mechanism** [[realtime_stream]]
**domain** [[developer_tools]]
**user** [[developer]]
**substrate** [[code_repository]]

**stack** anchor, angular.js, rust, solana, typescript

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for bulldozer

## Body

Our landing site A sneak peek of the tool Inspiration Building software is hard af. I mean it, it really is. That's why we, as builders too, are committed to creating the dopest power tools so other builders can focus on what matters, their projects. We want to bring waves of software developers to Web3. By building the tools they need to make a smooth transition, many will just “plug-n-play” into it. What it does Bulldozer is a low code platform that makes it easier to build Solana programs, it’s powered by Anchor Framework. It gives developers the ability to manage their program’s ecosystem through a GUI, hiding all the gory details so they can focus on the business logic. How we built it We decided to go for a monorepo because we're planning to keep adding more tools. We chose Nx for managing the monorepo, it's not fully integrated with Rust build system which is kinda PITA, and that's something we're looking forward to fixing. Since we're generating Anchor based programs, we went the same road with our code. As of now, there's a single program to do it all, but we're open to the idea of splitting it into multiple subprograms. The client is built using Angular. I know it's weird to see a Dapp without React, but who knew, it's doable. It uses the @solana/wallet-adapter library for connecting to wallets. The @project-serum/anchor TS library powers all the requests to Solana. Challenges we ran into Two months ago we didn't know Rust, Solana, Anchor... Let's say the first few weeks were really "slow", learning a lot, reading even more. We're not VC funded, we're just two devs working our ass-off whenever we catch a break from our regular boring job. It was really challenging, we were expecting to deliver more, but it's better to deliver something. Accomplishments that we're proud of We are really proud to have come this far. It feels like a real marathon. Working crazy hours and weekends, putting skin in the game. Now we can tell, we know a thing or two about Rust, and we also finally know what tf is a PDA. There were ups and downs but we made it. We already have some early adopters running Bulldozer in their local environments. The day we posted our first-ever demo video, CT went wild, we reached almost 300 followers in our first hours. What we learned We learned more about crypto, blockchain, decentralization, in the last month than ever before. We feel like all we want to do now is Solana-related stuff. But there's a lot more to learn and we're excited for the future. What's next for Bulldozer We're planning on working full-time in Bulldozer and see where it gets us. We already have a roadmap of what want to achieve: Manage workspace and allow grouping of applications. Improve Anchor integrations. Enable real-time updates through events. Enhance usability across the whole process. Improve template engine. Set up continuous integration for internal development. Git integration for versioning of workspaces. CLI to list, build and deploy workspaces and applications. Plugin-support for community utilities. Cross program invocation between applications in a workspace. <div