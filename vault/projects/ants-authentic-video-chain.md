---
slug: "ants-authentic-video-chain"
url: "https://devpost.com/software/ants-authentic-video-chain"
title: "ANTS"
hackathon: "Build Resilient Apps with Polkadot Cloud"
organization: "POLKADOT"
winner: true
words: 898
team_size: 1
has_repo: false
has_live: false
has_video: false
tags:
  - "project"
  - "mechanism/provenance_signing"
  - "mechanism/retrieval_grounding"
  - "mechanism/vision_ocr"
  - "domain/developer_tools"
  - "domain/legal_justice"
  - "user/general_public"
  - "substrate/financial_record"
  - "substrate/video_visual"
---

# ANTS

> When AI can manufacture any video, how do we preserve reality? ANTS is blockchain infrastructure for cryptographic video authentication, enabling verifiable evidence for activists and citizens.

[Devpost](https://devpost.com/software/ants-authentic-video-chain) · hackathon [[Build Resilient Apps with Polkadot Cloud]]

## Facets

**mechanism** [[provenance_signing]] [[retrieval_grounding]] [[vision_ocr]]
**domain** [[developer_tools]] [[legal_justice]]
**user** [[general_public]]
**substrate** [[financial_record]] [[video_visual]]

**stack** css, javascript, polkadotapi, react, rust, substrate, typescript

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for ants-authentic video chain

## Body

Inspiration During the Polkadot workshop at 42Berlin, a questionnaire system using blockchain tech made me think about what information is important to store on-chain and sparked the question: What information truly matters enough to be stored on-chain, how can we redistribute power back to the people through verifiable evidence and media? Throughout history the custodianship of truth has evolved through distinct eras. Writers and scholars documented events in books, carefully preserving knowledge for future generations.Radio and television emerged as powerful mediums, broadcasting news primarily local events to the masses. Today social media has democratised information flow, enabling the instantaneous transmission of global events to billions. Yet this democratisation comes at a cost. We now live in an age where AI-generated videos can be fabricated in mere moments, although that allows for creativity it weakens certain types of media that existed for people as a record of history and evidence.Watermarks currently our only and if present indicator of AI generated content can be stripped or manipulated. People grow increasingly desensitised to what they witness questioning the authenticity of what they are seeing. This erosion of trust in visual media represents an existential threat to historical truth itself in a larger scale and evidence that each person holds in a smaller scale. How will future generations distinguish what actually happened from what was fabricated? How can minorities and marginalised communities leverage media as credible evidence when authenticity is perpetually in doubt? Respecting the core principles of why Web3 came about, I created ANTS and Authenticated Video Chain a blockchain-based solution that provides immutable, cryptographic proof of a video's origin, creator and timestamp. This isn't just a technical solution; the potential scalability of reclaiming truth from centralised authorities is its ultimate goal. Future historians will need verifiable evidence to understand our era. In the near future activists and witnesses to injustice will need authenticated media that courts and institutions cannot dismiss. By anchoring video authenticity to an immutable blockchain ledger we're building a foundation for trust in the digital age, ensuring truth once capture remains unalterable and verifiable for generations to come. What it does This technology is a blockchain platform where people can record videos directly through their camera, file uploads are not allowed to ensure authenticity. Frontend part of the technology calculates SHA256 hash, the transaction is then submitted to blockchain with the content hash. Blockchain generates cryptographic proof that is embedded directly into the MP4 file structure. After authentication the user can download the authenticated video with embedded immutable proof or share the QR code containing the proof. Verification process extracts the embedded metadata and verifies that the video has been created through this technology. How we built it Concerning the blockchain tech, a custom substrate blockchain was built for control over transaction costs and storage structure allowing for low transaction fees for people using this technology and for the ability to scale as a Polkadot parachain. Built a custom pallet called video registry with three core functionalities to (i)store hash, creator address and block timestamp (ii) retrieve cryptographic proof for verification and (iii) proof generation. Runtime was configured to combine the custom pallet with Substrate's core pallets. GRANDPA and Aura was used for fast blocks and finality. Concerning the frontend react, typescript and vite was used. Camera recording component was implemented using MediaRecorder API with codec detection. Hashing was achieved using WebCrypto API for content veification. Metadata was imbedded directly into MP4 files by creating custom uuid atoms with markers.Cryptographic signing was implemented with the Polkadot.js extension and Polkadot.js API was used for blockchain communication. Finally using qrcode library allowed for fast generation of proof for easy mobile verification. Challenges we ran into Learning Substrate and blockchain development from scratch was intense. The framework uses advanced Rust concepts, traits and has its own patterns that are still being grasped. Working with existing templates helped initially but integrating custom pallets introduced new complex themes understanding how pallets communicate, configuring runtime correctly and properly structuring extrinsics required persistence and experimentation. Imbedding the proof in the MP4 file was also pretty complex. Given that MP4 uses a nested atom/box structure injecting custom metadata required writing binary parsing logic, creating custom uuid atoms ensuring playback compatibility and appropriate extraction of custom metadata to prevent hash mismatches. Lastly, version conflicts between Substrate dependencies consumed significant debugging time. Accomplishments that we're proud of Besides all the technical aspects of building my own blockchain embedding cryptographic proof into MP4 files while maintaining playback functionality and achieving a start to end flow i mostly loved the idea of the project and how it can be used to solve real-world problems. The core idea drives everything: giving people the power to preserve their truth without intermediaries or censors. In an era where AI can fabricate reality in seconds, building a system that provides cryptographic, immutable proof of authenticity feels genuinely important. What we learned Building ANTS taught me that blockchain development is about designing systems that serve real human needs apart from the technical implementation. Building a blockchain requires considering economics, spam prevention and scalability from day one which is something that still needs to be considered in this project. What's next for ANTS-authentic video chain Immediate improvements would be creating the mobile app version for this technology since now its solely accessible through the browser, setting economic incentives and limited usage for each user. <div