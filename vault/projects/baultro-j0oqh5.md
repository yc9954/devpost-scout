---
slug: "baultro-j0oqh5"
url: "https://devpost.com/software/baultro-j0oqh5"
title: "Baultro"
hackathon: "Electroneum Hackathon 2025"
organization: "Electroneum"
winner: true
words: 911
team_size: 1
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "domain/climate_energy"
  - "domain/developer_tools"
  - "domain/security_privacy"
  - "substrate/code_repository"
  - "substrate/financial_record"
---

# Baultro

> Baultro is a multiplayer platform that is both an AI game and a prediction market, offering an innovative approach to competitive gaming with economic incentives on the Electroneum blockchain.

[Devpost](https://devpost.com/software/baultro-j0oqh5) · hackathon [[Electroneum Hackathon 2025]]

## Facets

**mechanism** [[realtime_stream]]
**domain** [[climate_energy]] [[developer_tools]] [[security_privacy]]
**substrate** [[code_repository]] [[financial_record]]

**stack** gemini, nextjs, solidity, typescript, zerepy

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for baultro

## Body

Home Raid Chat Fail riad Baultro - Devpost Submission Inspiration The inspiration for Baultro came from observing how AI, gaming, and blockchain technologies were evolving separately but rarely combined effectively. I wanted to create a game where: AI isn't just a backend tool but the central gameplay mechanic Blockchain provides real economic stakes rather than just tracking points Social engineering and conversation skills become a valued gaming ability Electroneum was the perfect blockchain for this concept because of its low transaction fees and fast block finality (5 seconds), which allows for near real-time game outcomes without breaking the player experience. What it does Baultro is an AI-powered gaming platform where players interact with AI \"vaults\" through conversation. Each vault is guarded by an AI personality that players must outsmart to win tokens staked in the vault. The platform offers four distinct game modes: Battle Mode : Players try to hack into an AI security system using social engineering Love Mode : Players attempt to make an emotionally-restricted AI express romantic feelings Mystery Mode : Players extract a secret phrase hidden within the AI's knowledge Raid Mode : Players create vaults with stakes that other players try to break into All game outcomes and stakes are managed on the Electroneum blockchain, with smart contracts handling the prediction markets, match creation, and token distribution. How we built it Frontend Next.js 15 with App Router for the application framework React 19 for UI components and state management Tailwind CSS for styling viem for type-safe Electroneum contract interactions AI Integration Google Gemini API for AI conversations Custom system prompts for each game mode and difficulty level Server-side API integration to protect API keys Smart Contracts Two primary Solidity contracts deployed on Electroneum testnet: BaultroFinal.sol : Handles the prediction market functionality BaultroGames.sol : Manages game modes like battles and raids ANKR Premium API for reliable RPC connections Development Workflow Bun for package management and builds Local testnet for initial contract testing Electroneum testnet for final deployment Challenges we ran into Smart Contract Complexity : Balancing gas efficiency with complex game logic was challenging. Early versions of the contracts had functions that consumed too much gas. I had to refactor to optimize storage and compute patterns. Verifying AI Outcomes : Since AI responses can be subjective, creating a reliable way to verify when a player has \"won\" against the AI required multiple approaches: Pattern matching in responses AI self-evaluation of its security breach Hybrid verification system for edge cases Cross-chain Migration : The project was initially built for another chain, and migrating to Electroneum required updating all contract interactions and wallet providers. Finding documentation on some Electroneum-specific features was occasionally challenging. AI Reliability : The AI models sometimes responded inconsistently to similar inputs, which made gameplay testing difficult. I needed to create a robust system of prompts and evaluation criteria to ensure consistent gaming experiences. Accomplishments that we're proud of Successfully deployed and verified smart contracts on Electroneum testnet Created a smooth integration between AI gameplay and blockchain verification Built an intuitive user interface for a complex technical concept Implemented a multi-mode gaming platform with a single codebase Optimized contract gas usage for affordable gameplay on Electroneum What we learned Smart Contract Development The development of the Baultro contracts taught me several important lessons: Storage Optimization : Electroneum, like other EVM chains, makes storage operations expensive. I learned to minimize on-chain data by: Using packed structs (e.g., using uint64 instead of uint256 where possible) Storing only critical verification data on-chain Using events for historical data not needed for contract execution // Example from BaultroFinal.sol struct Prediction { uint64 id; // Using uint64 instead of uint256 to save gas address creator; string title; string description; string[] options; uint256 stake; uint256 totalBets; int8 resolvedOption; // Using int8 with -1 as unresolved state uint64 createdAt; // Timestamps as uint64 saves gas uint64 resolvedAt; } Permission Patterns : Implementing proper access controls without excessive gas costs: // Example permission check from resolvePrediction function require( predictions[predictionId].creator == msg.sender || owner == msg.sender, \"Only the prediction creator or contract owner can resolve predictions\" ); Event Emissions : Using events efficiently for off-chain tracking: // Event definition for tracking prediction creation event PredictionCreated( uint64 indexed predictionId, address indexed creator, string title, uint256 stake ); Gas-efficient Loops : Handling array operations without excessive gas: // Example of gas-efficient pagination from getPredictions function getPredictions(uint64 fromIndex, uint64 limit) public view returns (Prediction[] memory) { uint64 resultSize = uint64(min(limit, predictionsCount - fromIndex)); Prediction[] memory results = new Prediction[](resultSize); for (uint64 i = 0; i < resultSize; i++) { results[i] = predictions[fromIndex + i + 1]; } return results; } Electroneum-Specific Knowledge Working with Electroneum's 5-second block finality required rethinking UI patterns for transaction confirmations Learned how to properly verify contracts on Electroneum's block explorer Discovered the importance of ANKR API for reliable RPC connections What's next for Baultro Complete Multiplayer Implementation : Finish and test player vs. player functionality Mainnet Deployment : Move from testnet to Electroneum mainnet once testing is complete Mobile Apps : Develop native mobile applications for broader accessibility AI Personality Editor : Allow players to create and share their own AI vault personalities Backend Development : Build a scalable backend in Elixir for improved performance and monitoring Community Building : Create tournaments and events to build a player community With Electroneum's fast transaction times and low fees, Baultro can become an accessible and engaging platform for combining AI gameplay with real economic stakes.` <div