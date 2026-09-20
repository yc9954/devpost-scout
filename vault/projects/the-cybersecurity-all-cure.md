---
slug: "the-cybersecurity-all-cure"
url: "https://devpost.com/software/the-cybersecurity-all-cure"
title: "Panacea"
hackathon: "United Hacks V7"
organization: "Hack United"
winner: true
words: 646
team_size: 3
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/on_device_local"
  - "mechanism/provenance_signing"
  - "domain/scientific_research"
  - "domain/security_privacy"
  - "substrate/genomic_bio"
---

# Panacea

> the cybersecurity all-cure

[Devpost](https://devpost.com/software/the-cybersecurity-all-cure) · hackathon [[United Hacks V7]]

## Facets

**mechanism** [[on_device_local]] [[provenance_signing]]
**domain** [[scientific_research]] [[security_privacy]]
**substrate** [[genomic_bio]]

**stack** jsx, react, rust, solana, tauri, typescript

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for the cybersecurity all cure - panacea

## Body

Inspiration The inspiration was from learning about bacterial conjugation and specifically the Streptococcus mutans strain (cavities). In 2002, Jeffrey Hillman modified a specific strain and created BCS2-L1 this was supposed to be the cure for cavities. The modified strain had its ability to produce lactic acid, which disolves the dentin (soft tooth material), removed and replaced it with faculties to produce mutacin (amino acid chain) that kills the standard strain. The reason why this wasn't publicly released was because of fear of creating a super disease or the standard Streptococcus mutans strain conjugating the modified strain and just creating super cavities. The logic of adapting to overcome infections and conjugation is what drove the idea and was simply applied and translated to cybersecurity. What it does Panacea is designed as a autonomous decentralized antivirus implementation, modeled after biological immune systems. The idea hinges on moving away from a centralized slow vendor security patches, that hinder the user and can't match malware velocity. Panacea establishes a crowd-source global defense network with a centralized registry. This allows it to be lightweight locally, respond to zero-day threats, identify and isolate threat vectors, as well as have individual complex solutions for different types of malware without creating bloat. How we built it We created a decentralized antivirus. The goal was velocity of threat detection and lightweight defense. To achieve this we created a antivirus that relies on a dual system: threat detection, and threat defense. The detection is a lightweight executable to monitors and reports discovered potential threats to the blockchain. To make sure that not just anything is reported it functions on a identification hash as was as a PoS adjacent structure, simply if lots of local nodes report similar malware code signatures it gets logged. The threat defense functions in a similar way and is modeled after bacteria phages or immune systems. It attacks the logged threats and if uses a combinatorial permutation matrix to test out different defenses, because it is simply using permutations it doesn't need to be "smart" it learns simply from failure. When a specific combination is found it logs it as the solution to that specific malware code signature in the blockchain so future attacks can be defeated faster. Challenges we ran into We ran into several challenges including working with blockchain as it was our first time, creating a secure system to prevent tampering, and working around not being able to use tracers or kernel level hooks (as we are on MacOS). Although tracers and hooks are only necessary in real application, outside of demo, we still wanted to find a way to implement our application more faithfully. Accomplishments that we're proud of We were really proud of coming up with a unique idea as well as designing an implementation around blockchain technology. We also were really proud of being able to finish this project as it was our first time working on a hackathon online with more asynchronous work as well as a more ambitions idea. What we learned We learned a lot about the limitations as well as the benefits of blockchain and why it's implemented the way it is in the market. It is really good for consensus and security of immutability but isn't as useful for the lightweight implementation we initially dreamed. What's next for The Cybersecurity All Cure - Panacea I think what would make this application even better is a separation of different types of defense agents for different types of malware, that way the application could be even more lightweight as well as having a more exact "genome"/combination for each malware signature. Also we would more more data off the blockchain and store it in distributed local storage or in a application linked the chain, which would allow the blockchain to perform it's primary function of allowing secure global decentralized communication between local nodes. <div