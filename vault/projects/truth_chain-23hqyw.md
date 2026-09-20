---
slug: "truth_chain-23hqyw"
url: "https://devpost.com/software/truth_chain-23hqyw"
title: "Truth_Chain"
hackathon: "Maximally Vibe-a-thon"
organization: "Maximally (https://maximally.in)"
winner: true
words: 882
team_size: 1
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/provenance_signing"
  - "mechanism/realtime_stream"
  - "mechanism/structural_withholding"
  - "domain/disaster_emergency"
  - "domain/media_journalism"
  - "substrate/geospatial"
  - "substrate/video_visual"
---

# Truth_Chain

> Deepfakes spread faster than we can debunk them. AI can't reliably detect AI. So I built TruthChain—a protocol that cryptographically proves images are real at capture. Stop playing catch-up.

[Devpost](https://devpost.com/software/truth_chain-23hqyw) · hackathon [[Maximally Vibe-a-thon]]

## Facets

**mechanism** [[provenance_signing]] [[realtime_stream]] [[structural_withholding]]
**domain** [[disaster_emergency]] [[media_journalism]]
**substrate** [[geospatial]] [[video_visual]]

**stack** android, java, kotlin, mysql, pinata, react, springboot

## How they structured the write-up

- inspiration
- what it does
- how we built it
- what we learned
- what's next for truth_chain

## Body

Inspiration Deepfakes are spreading faster than we can debunk them. Every day, manipulated images flood social media, and fact checkers are overwhelmed trying to keep up. I realized we were fighting the wrong battle. Instead of playing detective after images go viral, we needed to prove authenticity at the moment of capture. That's when I discovered Adobe's C2PA initiative for content provenance. They were building something powerful, but I saw an opportunity to take it further by combining their content credentials framework with blockchain's immutability. The vision became clear: give every real photo a digital birth certificate that nobody can fake or erase. What it does TruthChain proves an image is real the moment it's captured. When you take a photo with our Android app, the phone's secure hardware chip instantly stamps it with GPS location, timestamp, and a cryptographic signature. This isn't just metadata anyone can edit. It's locked by the device's security processor. We then upload the signed image to IPFS, the decentralized web, where it becomes permanent and unchangeable. Anyone can verify any image through our web portal by simply dragging and dropping it. Real photos get a green checkmark showing exactly where and when they were taken. Fake or tampered images trigger an immediate red warning because the cryptographic math doesn't match. No guessing, just mathematical proof. How we built it The architecture has three main pieces. First, the Android app uses the device's Trusted Execution Environment to generate cryptographic signatures at capture time. We tap into the phone's secure hardware to create hashes that can't be forged. Second, our backend handles the upload pipeline and stores images on IPFS for permanent, decentralized storage. We built smart contracts to anchor these hashes on the blockchain, creating an immutable record. Third, the React web portal provides the verification interface where anyone can check authenticity by comparing uploaded images against our stored hashes. We implemented drag and drop functionality with real time cryptographic verification that instantly shows whether an image matches our records or has been altered. Challenges we ran into Getting camera hardware integration working was brutal. Every Android manufacturer implements their security chip differently, and documentation was sparse. We spent weeks figuring out how to reliably access the Trusted Execution Environment across different devices. Network latency created another headache because blockchain writes aren't instant. Users couldn't wait thirty seconds after every photo, so we built a hybrid system with local verification and periodic blockchain anchoring. The biggest challenge was balancing transparency with privacy. We needed to prove location and time without exposing sensitive metadata that could compromise user safety. We solved this with selective disclosure, where verification happens without revealing everything. Optimizing the hashing algorithm for mobile was also tricky since cryptographic operations drain batteries fast. Accomplishments that we're proud of We built a working end to end system that actually proves image authenticity. The Android app successfully captures and signs images using secure hardware. Our IPFS integration means these proofs are permanently stored and can't be deleted or manipulated. The web portal delivers instant verification results that anyone can understand. Green means real, red means fake. No PhD required. We're especially proud of achieving real time verification speed despite the complex cryptography happening under the hood. The user experience feels seamless even though we're doing hardware level security checks, decentralized storage, and blockchain anchoring. We also cracked the privacy problem with our selective disclosure approach, proving authenticity without exposing sensitive location data when users don't want to share it. What we learned Cryptography became my second language. I learned how hash functions create unique fingerprints for digital data and how even changing one pixel completely changes the hash. Merkle trees taught me efficient ways to verify data integrity without processing everything. Working with Trusted Execution Environments showed me how hardware security creates trust that software alone cannot. Blockchain development taught me about immutability and decentralized consensus. I discovered that user experience matters just as much as the underlying tech. Our first prototype had users manually copying hashes and pasting them into verification tools. It was technically sound but completely unusable. Simplifying to drag and drop made all the difference. I also learned that privacy and transparency aren't opposites. With zero knowledge proofs and selective disclosure, you can prove something is true without revealing everything about it. What's next for Truth_Chain We're launching two major upgrades. First is device attestation using Google's SafetyNet and Play Integrity APIs. Before we trust any signature, we'll verify the phone itself hasn't been compromised, rooted, or tampered with. This closes a critical security gap. Second is our Honest AI engine, and this is the game changer. Right now, AI chatbots hallucinate and spread misinformation because they train on the entire messy internet. We're building an AI that only learns from TruthChain verified images. When journalists ask it what happened at an event, it responds with answers backed by cryptographically signed evidence. It can cite exactly which verified photos informed its response. This creates an AI that cannot lie because it only reads proven truth. We're also exploring partnerships with news organizations and social media platforms to integrate TruthChain verification directly into their workflows. Imagine scrolling through your feed and seeing verification badges on real journalism while unverified content gets flagged automatically. <div