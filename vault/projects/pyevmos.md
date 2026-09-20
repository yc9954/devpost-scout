---
slug: "pyevmos"
url: "https://devpost.com/software/pyevmos"
title: "PyEvmos"
hackathon: "Evmos Momentum Hackathon led by Web3Scholarships (Deployment required for prize)"
organization: "Huobi"
winner: true
words: 527
team_size: 1
has_repo: true
has_live: true
has_video: false
tags:
  - "project"
  - "mechanism/on_device_local"
  - "domain/developer_tools"
  - "user/developer"
  - "substrate/financial_record"
---

# PyEvmos

> Python port of evmos.js - moving away from JS domination!

[Devpost](https://devpost.com/software/pyevmos) · hackathon [[Evmos Momentum Hackathon led by Web3Scholarships -Deployment required for prize-]]

## Facets

**mechanism** [[on_device_local]]
**domain** [[developer_tools]]
**user** [[developer]]
**substrate** [[financial_record]]

**stack** github, python, python-package-index, read-the-docs

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for pyevmos
- evmospy vs pyevmos

## Body

Pyevmos on PyPI Docs CI Inspiration It was a great surprise for me when I discovered that SDK which relies on protobuf - tool especially designed to be highly portable and implemented in many languages - exists only for TypeScript. I think I should fight JavaScript domination, so this project serves only one purpose: make evmos development available for broader developers category. What it does It allows to create messages and transactions, sign them locally with the private key and broadcast the result via REST API - same as original evmos.js library. How we built it After translating all original files and tests, I added a couple on-chain tests similar to examples present in evmosjs to ensure that our messages are understandable for real chain API. From the first day project was powered by Github Actions and multiple linters to ensure code quality and allow package users to see that everything works as intended. Challenges we ran into The main challenge was debugging external dependencies: after translating protobuf-related files and tests, I discovered major binary incompatibility of python ( betterproto ) implementation and reference standard. This was reported upstream and patched quickly, although release is still not live - so my project temporary depends on PyPI-deployed fork. Also serious bug was discovered in EIP712 library - it was reported upstream as well, but finally I replaced the library with the more mature one. Accomplishments that we're proud of I'm mostly proud of building "nice-looking" final result: the package is completely deployed, available for all users via usual package manager, passes all code quality checks and tests. The library is fully covered with types. The library has an extensive documentation built from source with Sphinx, so it is easy for newcomers to understand package usage. This is not just "install & go" solution, but highly customized pipeline involving custom sphinx plugin (created as part of this submission). Also I'm proud of "pythonic" result: no jumping case anymore, almost every function and attribute in-python use PEP8-recommended snake_case , and are converted to camelCase only on demand before serialization. What we learned I have never seriously dealt with protobuf before and wanted to learn it, so this project was an excellent chance to play with this system. What's next for PyEvmos Currently it is stable, most expected changes are related to upcoming upstream changes in Evmos ecosystem. We should support multiple broadcasting options (not only REST API, but other providers as well). Also it could be nice to provide UI for some features (like broadcasting the transaction from UI, given message parameters). Evmospy vs Pyevmos It was very demoralizing to find out official package created after my project was started, but finally it doesn't look like drop-in replacement. Pyevmos implementation sticks with original functional style, so it is easier to understand for those who used JS version before Pyevmos provides extensive API documentation (including separate protobuf docs) Pyevmos uses its own fork of awesome betterproto project instead of python-protobuf, which solves many usability problems (see betterproto docs ). Pyevmos heavily utilizes CI pipeline, including a couple of on-chain tests to verify that implementation is binary compatible with remote counterpart. <div