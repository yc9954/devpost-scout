---
slug: "rustle"
url: "https://devpost.com/software/rustle"
title: "Rustle"
hackathon: "NEAR MetaBUILD III Hackathon"
organization: "NEAR Protocol"
winner: true
words: 521
team_size: 1
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "domain/developer_tools"
  - "domain/security_privacy"
  - "user/developer"
  - "user/researcher"
---

# Rustle

> Rustle is the first automatic auditor for NEAR community. It is free, open-source, and can help to locate tens of different vulnerabilities in NEAR smart contracts.

[Devpost](https://devpost.com/software/rustle) · hackathon [[NEAR MetaBUILD III Hackathon]]

## Facets

**domain** [[developer_tools]] [[security_privacy]]
**user** [[developer]] [[researcher]]

**stack** c++, python

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for rustle

## Body

Rustle Workflow of Rustle All the issues Rustle can detect Inspiration Crypto hacks caused severe losses and most of the hacks are due to smart contract vulnerabilities. Security code audit takes a semi-automatic way to find issues before the contract is deployed. In this case, we would like to design and open-source an automatic analyzer that any NEAR developers can use. We can design and implement different plugins for the analyzer and integrate the framework into the normal developing process. This can help to mitigate many potential issues and enhance the code quality of the contracts. What it does This project aims to check the security issues of smart contracts on NEAR. The project receives the contract code as the input and utilizes the program analysis technique to explore the potential defects in the contracts. Finally, a thorough report will be generated. How we built it We compile the NEAR contract code into LLVM IR. Based on the LLVM IR, we utilize the program analysis technique and write different LLVM passes. Each LLVM pass serves as a detector and can detect different defects in the contract. Challenges we ran into First, we need to understand and figure out all the possible attack surfaces in NEAR smart contracts. After that, we need to formalize the different defects in the contract and implement different plugins. Furthermore, the static analysis technique may come across false positives. How to reduce false positives is also a challenging task. Finally, there are vulnerabilities related to semantics, how to understand the semantics of the contract code is rather difficult. Accomplishments that we're proud of We are BlockSec . BlockSec is dedicated to building blockchain security infrastructure. The team is founded by top-notch security researchers and experienced experts from both academia and industry. We have published multiple blockchain security papers in prestigious conferences, reported several zero-day attacks of DeFi applications, and successfully protected digital assets that are worth more than 5 million dollars by blocking multiple attacks. We also audited many famous DeFi projects like Ref Finance, Burrow, Cornerstone, MetaPool, Linear, etc. in NEAR ecosystem. We now successfully designed and implemented the whole framework. The tool can now check many different kinds of security issues, which are listed in the repo. What we learned Automatically locating the vulnerabilities of smart contracts is not easy. We need to have deep understanding of NEAR protocol and Defi Security. Meanwhile, crypto hacks really harm the whole community. This motivates us to build this tool with huge effort. Currently, Rustle can be used in the development process to scan the NEAR smart contracts iteratively. This can save a lot of manual effort and mitigate part of potential issues. However, vulnerabilities in complex logic or related to semantics are still the limitation of Rustle. Locating complicated semantic issues requires experts to conduct exhaustive and thorough reviews. What's next for Rustle Add unit tests to make Rustle more robust Add online usage support so that Rustle can be used without local deployment Add support on different NEP specifications (e.g., NEP141, NEP171) and extend the capabilities with new detectors (e.g., float usage check, storage check.) <div