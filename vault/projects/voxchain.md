---
slug: "voxchain"
url: "https://devpost.com/software/voxchain"
title: "VoxChain"
hackathon: "[REDACTED] Hackathon"
organization: "NEAR Protocol"
winner: true
words: 665
team_size: 7
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/deterministic_policy"
  - "mechanism/realtime_stream"
  - "mechanism/voice_speech"
  - "domain/developer_tools"
  - "substrate/financial_record"
---

# VoxChain

> VoxChain: Speak to the blockchain. With AI-powered simplicity, just say your command, confirm, and let VoxChain handle the rest. No complex interfaces—just effortless control.

[Devpost](https://devpost.com/software/voxchain) · hackathon [[-REDACTED- Hackathon]]

## Facets

**mechanism** [[deterministic_policy]] [[realtime_stream]] [[voice_speech]]
**domain** [[developer_tools]]
**substrate** [[financial_record]]

**stack** alchemysdk, expo.io, expogo, exposdk, fevertokensapi, firebase, javascript, langchain, langsmith, mistral, navigation, openai, pydantic, python

## How they structured the write-up

- inspiration
- what we learned
- how we built voxchain
- challenges we faced
- the future of voxchain

## Body

Inspiration The blockchain world offers incredible possibilities but is often plagued by a steep learning curve and complex user interfaces. Many people are intrigued by the idea of digital assets and decentralized transactions but feel intimidated by the complex processes involved. We wanted to change that by creating a blockchain experience that feels intuitive and accessible to anyone. This inspired us to design VoxChain, a mobile app that transforms blockchain interaction into a simple, conversational experience, where users can manage their assets just by speaking. What We Learned Building VoxChain taught us a lot about the interplay between AI and blockchain technology. Here are some key takeaways: Voice Processing and AI Models: We learned how to integrate voice recognition with natural language processing, allowing users to speak commands that the app can understand and execute on the blockchain. Working with Large Language Models (LLMs) required a deep understanding of how to handle user intent in various contexts. Mobile expertise in Blockchain: Since typical blockchain interactions require multiple steps and confirmations, we leveraged our mobile expertise to simplify this. Through this, we were able to mask complexity behind an intuitive, user-friendly interface, enabling smooth, single-command transactions. How We Built VoxChain The project involved several key technologies and processes: Speech-to-Text and NLP Processing: Using AI-powered voice recognition, we capture and process user commands. Once a user speaks a command (e.g., "Send 0.5 ETH to Alice"), the app translates this command into blockchain-ready transactions using NLP. We are using prompt engineering combined with pydantic models corresponding to the different types of transactions alongside some hyperparameters tuning to force our model to be deterministic and minimize errors making the model respect the pydantic schemas then matching its output with the corresponding . Integration with Blockchain Protocols: We designed VoxChain to be compatible with popular blockchain protocols. Through API integrations, VoxChain can interact with wallets, search for known addresses, confirm balances, and execute transactions. This is also where we applied account abstraction to streamline these interactions. Smart Contract Development: To handle transactions efficiently, we developed smart contracts that VoxChain uses to execute transactions on behalf of the user, while also ensuring each transaction’s security. User Experience and Security: We focused heavily on simplifying the interface while maintaining robust security. For example, after a user confirms their intent, VoxChain takes care of all the details, from gas fees to wallet access, giving users an effortless experience without sacrificing safety. Challenges We Faced Building VoxChain presented several challenges: Accurate Intent Recognition: Interpreting user intent accurately was more challenging than we anticipated. Simple phrases like "send 10 USDT to Bob" could vary in wording, so we had to train our model to recognize a variety of command structures and identify users' intents reliably. Latency and Real-time Processing: Voice processing and transaction execution both require fast response times to maintain a smooth user experience. Balancing speed and accuracy in real-time processing was crucial and required optimization across our tech stack. Blockchain Security Risks: With an AI-driven transaction interface, security was a constant concern. We had to ensure that VoxChain couldn’t misinterpret commands and that every transaction was secure, incorporating confirmation steps and secure authentication throughout. Adapting to Different Blockchain Protocols: Each blockchain has its quirks, and making VoxChain adaptable to multiple blockchain ecosystems was no small feat. We created a flexible backend to support different blockchains and their specific protocols, allowing users to work with multiple assets and networks. The Future of VoxChain We’re excited about the future of VoxChain! Moving forward, we hope to integrate more blockchain networks, add support for a wider range of digital assets such as send NFTs, use account abstraction to simplify even more the onboarding and handling of transactions and continuously improve our AI model’s accuracy. Our ultimate goal is to make interacting with blockchain as simple as having a conversation, bringing the power of decentralized finance to everyone. PS: *You can try out the application here: link **To access all the repos of the project: link <div