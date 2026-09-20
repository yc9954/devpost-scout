---
slug: "tstron"
url: "https://devpost.com/software/tstron"
title: "tstron"
hackathon: "TRON Grand Hackathon - Season 3"
organization: "TRON DAO"
winner: true
words: 464
team_size: 1
has_repo: true
has_live: false
has_video: false
tags:
  - "project"
  - "domain/accessibility"
  - "domain/developer_tools"
  - "user/developer"
  - "substrate/financial_record"
  - "substrate/web_dom"
---

# tstron

> TypeScript is one of the most popular languages now for some reason and de facto primary web development language. Blockchain devs should not stay behind!

[Devpost](https://devpost.com/software/tstron) · hackathon [[TRON Grand Hackathon - Season 3]]

## Facets

**domain** [[accessibility]] [[developer_tools]]
**user** [[developer]]
**substrate** [[financial_record]] [[web_dom]]

**stack** github, node.js, npm, typescript

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for tstron

## Body

README NPM package More CI! Inspiration My initial idea was related to developing specific cross-browser wallet extension targeting developers (with both security/privacy and debugging focus). I wanted to improve my typescript at the same time, so decided to use Tron SDK . It was disappointing when I discovered that there is no one, so the submission changed its shape to what I'm currently presenting. What it does It does exactly what TronWeb library does. It makes working with Tron HTTP API easier by many wrapper functions and classes. Additionally, it contains all protobuf files converted to typescript. How we built it I started from form of TronWeb and began to add types gradually. During the transition a few serious bugs were discovered (I will report then upstream and patch when I have some time) and successfully resolved. So I can confidently say that current library stage is cleaner than in was - and this was one of my primary goals. Also, in my opinion modern CI&CD pipeline is important for every library and package, so all tests and builds are performed on github and visible to all users. Challenges we ran into I'd say that there was only one extremely difficult challenge: complete absence of HTTP API documentation. Protocol buffers, you say? Nope! I'm using them as templates for later manual editing, because some endpoints' responses do not match protobuf files. Official documentation? Oh yeah, it says literally "returns: transaction", go guess what it is supposed to mean (spoiler: no, not a Transaction from protobuf definition). Accomplishments that we're proud of The thing I'm most prod of is that I have achieved almost complete type correctness. Everything besides plugins (which are anyway almost impossible to handle in strongly typed contexts) and a couple of places (like sidechain attribute which is TronWeb | undefined and I haven't managed to overload constructor properly) shows proper types - including queries to external APIs (yes, HttpProvider.request(<some_url>) returns typed JSON response depending on URL and passed options!). This means that other developers can use their IDE or other tools to easily figure out what one or another endpoint does and which response to expect. What we learned Well, first what I learned after building relatively large typescript project is "do not build projects with typescript", long-lasting interaction with typescript was the worst dev experience in my life, IMO. Also I have mastered trial-and-error debugging method, checking all API endpoints responses like a blind. What's next for tstron There are two most crucial tracks for now: first, I have added a few tests to original suite, but the coverage is still extremely low. More attention should be paid to testing and infrastructure. Second, HTTP API is not the only one - this library has to support gRPC as well. <div