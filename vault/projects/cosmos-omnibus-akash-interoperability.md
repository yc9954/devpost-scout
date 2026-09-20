---
slug: "cosmos-omnibus-akash-interoperability"
url: "https://devpost.com/software/cosmos-omnibus-akash-interoperability"
title: "Cosmos Omnibus: Akash Interoperability"
hackathon: "Cosmos HackAtom VI "
organization: "Cosmos"
winner: true
words: 346
team_size: 1
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "domain/developer_tools"
  - "user/developer"
  - "substrate/code_repository"
---

# Cosmos Omnibus: Akash Interoperability

> Targets adding multiple Cosmos based chains to Cosmos Omnibus repo to make deployments easier on Akash Network. The challenge is a part of Interoperability track under Akash organization.

[Devpost](https://devpost.com/software/cosmos-omnibus-akash-interoperability) · hackathon [[Cosmos HackAtom VI]]

## Facets

**domain** [[developer_tools]]
**user** [[developer]]
**substrate** [[code_repository]]

**stack** akash, docker, docker-compose, shell

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for cosmos omnibus: akash interoperability

## Body

Inspiration I had been exploring Akash and Cosmos for a decent time, and am really into idea of decentralized cloud. Saw HackAtom and found the track something I could contribute, and was able to immediately connect with the idea. Cosmos node deployments on Akash would help a lot more people to move away from centralized cloud services and help increase Akash adoption in general What it does Cosmos Omnibus allows developers to run Cosmos Nodes on Akash. I am working on adding more chains on the project and improving the deployment and contribution process to Cosmos Omnibus in general. How we built it I found widely used chains in the Cosmos registry which did not have SDL and Docker compose files to make deployments on Akash easier and added support for them one at a time. Challenges we ran into Few chains that I added followed process which isn't standard as adopted by the Cosmos Omnibus project. For such projects, had to do different configuration management and make base Dockerfile generic enought to adapt to those usecases. Accomplishments that we're proud of I've been able to add support for following chains to Cosmos Omnibus: Bitsong ( https://github.com/ovrclk/cosmos-omnibus/pull/54 ) Bandchain ( https://github.com/ovrclk/cosmos-omnibus/pull/58 ) Crypto.org chain ( https://github.com/ovrclk/cosmos-omnibus/pull/56 ) Impact Hub chain ( https://github.com/ovrclk/cosmos-omnibus/pull/55 ) Kichain ( https://github.com/ovrclk/cosmos-omnibus/pull/60 ) Starname ( https://github.com/ovrclk/cosmos-omnibus/pull/65 ) Comdex ( https://github.com/ovrclk/cosmos-omnibus/pull/66 ) Irisnet ( https://github.com/ovrclk/cosmos-omnibus/pull/67 ) Shentu ( https://github.com/ovrclk/cosmos-omnibus/pull/68 ) Likecoin ( https://github.com/ovrclk/cosmos-omnibus/pull/69 ) Rizon ( https://github.com/ovrclk/cosmos-omnibus/pull/77 ) Cheqd ( https://github.com/ovrclk/cosmos-omnibus/pull/80 ) Alongside this, I'm actively working with repo maintainer to enable more chains and improve contribution and deployment process in general. What we learned Got a good idea about working of Cosmos chains and understanding of Tendermint framework. Had a good learning about Akash network as well. What's next for Cosmos Omnibus: Akash Interoperability I'm looking at following improvments. Automatic Snapshot generation in CI Bot based commits post snapshot generation for adding snapshot json to environment in the SDL. Support for a wide range of chains which require extra steps than the generic ones done in the current cosmos omnibus repository. <div