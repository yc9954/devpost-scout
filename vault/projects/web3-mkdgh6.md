---
slug: "web3-mkdgh6"
url: "https://devpost.com/software/web3-mkdgh6"
title: "Proof of Personhood"
hackathon: "Supernova "
organization: "DFINITY Foundation"
winner: true
words: 1128
team_size: 4
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/on_device_local"
  - "mechanism/structural_withholding"
  - "mechanism/vision_ocr"
  - "domain/civic_government"
  - "domain/security_privacy"
  - "user/developer"
  - "user/general_public"
  - "substrate/video_visual"
---

# Proof of Personhood

> a Sybil-proof identity system powered by decentralized AI human detection.

[Devpost](https://devpost.com/software/web3-mkdgh6) · hackathon [[Supernova]]

## Facets

**mechanism** [[on_device_local]] [[structural_withholding]] [[vision_ocr]]
**domain** [[civic_government]] [[security_privacy]]
**user** [[developer]] [[general_public]]
**substrate** [[video_visual]]
  <sub>weak: web_dom</sub>

**stack** deepneuralnetwork(dnn), flutter, rust

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for proof of personhood

## Body

website scan_to_verify verifying_motion verifying_voice mint_nft Inspiration One of the most challenging Web3 issues is known as the Sybil attack. A Sybil attack is when a malicious user leverages multiple crypto wallets and/or web2 social media identity to gain multiple positions with an unfair advantage of systems. Examples of Sybil attacks are quite common in Web3, such as: Token airdrops are exploited by bot-controlled wallets to gain a large percentage of community tokens, diluting the value for those left holding their bags when the bad actor sells off all their rewarded tokens as their core objective is to game the system. Here is a recent example. NFT whitelisting suffers the same attack as well. Twitter, Discord and Telegram have been plagued with phishing links sent by bot accounts luring a user to interact with malicious smart contracts to steal their crypto assets. In addition, many Web3 efforts are trying to build social impact projects, as well as crypto as a public good, all requiring a decentralized Identity layer with Sybil-resistance as the building block of the projects: Universal Basic Income (UBI) aiming to support sustainable development. 1 human 1 vote for Web3 DAO governance avoiding plutocracy. Examples like Optimism’s the Citizens’ House . To prevent Sybil attacks, both centralized and decentralized identity solutions exist with different pros and cons. Centralized solutions like Blockpass require users to KYC (Know Your Customer) and provide their sensitive personal information such as government IDs, addresses, face photos, etc without users understanding how that information will be secured. Such private information is stored in centralized servers, which is prone to the next Equifax data breach . Decentralized solutions such as ProofofHumanity and BrightID don't require government IDs and both rely on other human users to distinguish humans from bots. They use different mechanism designs with various economic incentives/penalty, and also human coordination is required. BrightID users need to attend a Zoom group verification call at specific timeslots and ProofofHumanity requires users to reveal a selfie video with their ETH address online to make a public announcement and deposit some amount of ether. Obviously both solutions are not user friendly and they have been around for a couple of years with only modest success in adaption because of high onboarding friction. What it does Proof of Personhood is a Sybil-proof identity system powered by decentralized AI human detection. It allows: a user to verify he or she is not a bot by answering a combination of random challenges with sequential simple human actions like simultaneous face gestures and speaking numbers; dApps or Web2.0 apps can prevent Sybil attacks by requiring users to complete Proof of Personhood via QR Code Authentication; Privacy preserved. No sensitive information (user face image or voice) ever leaves the user's device. The on-device AI algorithm and the algorithm running on the IC canister together perform a Reverse Turing Test, in a decentralized way. How we built it Frontend The Proof of Personhood is integrated with AstroX ME mobile wallet app (soon to be released) as an advanced add-on feature (under the Experiment menu). The mobile app is built with Flutter using Agent_Dart to interact with the Internet Computer. AI: Human Liveness Detection The core components are face detection and face tracking based on Deep Neural Network (DNN) to detect real human interaction. A random sequence of face gestures is computed at the canister and sent to the app to challenge the user to perform. So photo, pre-recorded video or paper mask attacks can be prevented. In addition, a random number speech challenge is also required with simultaneous face tracking. During the challenges, none of the face image or voice data are leaving the mobile device. Only the results of the liveness detection are sent back to the canister to determine the final result. Below is the Human Liveness AI Detection Flow. Backend The Proof of Personhood canister is built using Rust. It performs two tasks: Compute interactive random challenges and send them to the app; Authenticate a web app that needs a user's Proof of Personhood. A user can scan a QR code generated on the web to perform the Proof of Personhood. Challenges we ran into Originally we wanted to run the entire AI on a canister with only a web "thin client" so that a user can use proof of personhood from a web browser. Deploying an AI framework into a caster would be so cool and many new use cases will be unlocked. However, we found out that DNN is too computation-intensive to run on today's IC canister. So we switch to a decentralized Reverse Turing Test by the on-device AI algorithm and the algorithm running on the IC canister. Accomplishments that we're proud of We have built an end-to-end fully functional proof-of-concept of Sybil-proof identity on the Internet Computer using AI liveness detection, as well as the demo web app in just less than 2 weeks! What we learned We are a team of experienced engineers and entrepreneurs who have built Internet-scale applications in the past 10 years and started to build on Internet Computer last year. During the project, we learned a lot about the problem space of Sybil-proof decentralized identity and previous attempts. Dfinity's People Parties project has provided us with a lot of insights as well and inspired us to try a different approach using a combination of various mature technologies for faster trial-and-error in the real world. We also learned a lot about the existing AI solutions. Although the solutions are mature in some use cases (especially face detection and voice), some assumptions do not apply to web3. So more innovations are needed to bridge the two technologies. What's next for Proof of Personhood We intend to make Proof of Personhood a public good for a Sybil-attack-free Web3 world. To make it a reality, there are a few milestones ahead: Drive user growth and adaption of Web3 apps using Proof of Personhood service: Reach out to NFT projects in IC community to use Proof of Personhood for Sybil-proof NFT fair mint; Integrate with Discord/Telegram so that general web3 projects in larger crypto ecosystems can use Proof of Personhood as well; Continue to explore how to run the entire AI module on canisters, so users can use Proof of Personhood from a browser only. Incorporate additional methods like mechanism design/incentive, or social graph analysis to combat newer and more sophisticated Sybil-attack vectors, while striking a good balance between ease of use for end-users and effectiveness of Sybil-resistance; Research how to apply zero-knowledge (ZK) cryptography to additional on-chain expressible claims for user cases like age checks while preserving privacy; Explore a good business model or tokenomics to support the long-term health of Proof of Personhood (to pay the R&D cost, canister cycle cost, etc). <div