---
slug: "chain-sleuth-graph-saas"
url: "https://devpost.com/software/chain-sleuth-graph-saas"
title: "Chain Sleuth (Graph SaaS)"
hackathon: "[REDACTED] Hackathon"
organization: "NEAR Protocol"
winner: true
words: 887
team_size: 3
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/graph_reasoning"
  - "mechanism/realtime_stream"
  - "mechanism/retrieval_grounding"
  - "mechanism/vision_ocr"
  - "domain/developer_tools"
  - "user/developer"
  - "user/researcher"
  - "substrate/financial_record"
  - "substrate/geospatial"
  - "substrate/structured_db"
---

# Chain Sleuth (Graph SaaS)

> "ChainSleuth: Your AI blockchain detective. Instantly analyze any NEAR address to uncover patterns and risks across chain data, social media, and web presence. Each investigation becomes an NFT."

[Devpost](https://devpost.com/software/chain-sleuth-graph-saas) · hackathon [[-REDACTED- Hackathon]]

## Facets

**mechanism** [[graph_reasoning]] [[realtime_stream]] [[retrieval_grounding]] [[vision_ocr]]
**domain** [[developer_tools]]
**user** [[developer]] [[researcher]]
**substrate** [[financial_record]] [[geospatial]] [[structured_db]]

**stack** bitteai, elysia, langchain, nearblocks, neo4j, node.js, pikespeak

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for chain sleuth (graph saas)

## Body

Infrastructure and tech-stack Query Engine Node creation pipeline Interactive Graph CHAIN SLEUTH: AI-Powered Blockchain Intelligence on NEAR Inspiration The blockchain space has a significant knowledge gap - while data is publicly available, understanding it requires deep technical expertise. We saw how investigators, researchers, and regular users struggled to make sense of blockchain activities. Our inspiration came from combining three powerful technologies: NEAR Protocol's infrastructure, Neo4j's graph database capabilities, and advanced AI language models. We envisioned a platform where anyone could investigate blockchain activities simply by asking questions in natural language. What it does CHAIN SLEUTH transforms complex blockchain data into accessible intelligence through: Natural language queries for blockchain investigation Comprehensive analysis of NEAR Protocol transactions and smart contract interactions Integration of social media signals and web footprints Advanced pattern detection and relationship mapping NFT-based preservation of investigation results Real-time monitoring and alerts for suspicious activities Graph-based visualization of blockchain relationships When users engage with Chain-Sleuth, they can simply enter any NEAR Protocol address to initiate a comprehensive investigation. The platform immediately begins collecting and analyzing data across multiple dimensions, creating a holistic view of the address's activities and relationships. This process leverages our advanced graph database to connect seemingly disparate pieces of information into a coherent narrative. The investigation process starts with on-chain analysis, where Chain-Sleuth examines every transaction, smart contract interaction, and token transfer associated with the address. But it goes far beyond simple transaction tracking. Our AI systems analyze transaction patterns, identify recurring relationships, and flag unusual behaviors that might indicate particular usage patterns or potential risks. What sets Chain-Sleuth apart is its ability to correlate blockchain data with off-chain information (final version will store all data on-chain via NEAR smart contract). The platform scans and analyzes social media presence, web footprints, and DeFi protocol interactions, creating a comprehensive digital profile. This multi-dimensional analysis helps users understand not just what an address has done, but the context and patterns behind those actions. Users can interact with this wealth of information through natural language queries. Instead of navigating complex blockchain explorers or writing technical queries, they can simply ask questions like "What DeFi protocols has this address interacted with?" or "Show me unusual transaction patterns." The Bitte.ai agent integration processes these queries, leveraging our graph RAG engine to provide detailed, context-aware responses that draw from both historical data and real-time blockchain information. How we built it Our technical stack leverages cutting-edge technologies: Core Infrastructure NEAR Protocol for smart contracts and NFT minting Neo4j graph database for relationship mapping Redis for real-time state management Advanced RAG (Retrieval Augmented Generation) for AI responses Data Pipeline PikesPeak integration for NEAR blockchain data Custom scrapers for social media signals WebSocket system for real-time updates Graph-based data structuring for relationship analysis AI Layer Large Language Models for natural query processing Custom machine learning models for pattern detection Graph neural networks for relationship analysis Automated report generation and summarization Frontend Infrastructure React-based interactive dashboard Real-time investigation status tracking Graph visualization interface for relationship exploration Query engine UI for natural language interactions Node creation pipeline interface for custom investigations WebSocket integration for live updates Interactive data visualization components Bitte.ai Agent Integration Custom Bitte agent for blockchain querying Direct integration with PikesPeak API Natural language processing for user queries Connection to graph RAG engine for enhanced responses Real-time blockchain data retrieval and analysis Context-aware responses using historical data AI-powered investigation suggestions Automated pattern recognition and reporting Query and Graph Interaction System Natural language query processor Graph database query builder Real-time graph exploration tools Custom investigation workflow creator Interactive node relationship viewer Pattern detection visualization Investigation history tracking Challenges we ran into Technical Complexity Integrating multiple data sources into a coherent graph structure Optimizing query performance across large datasets Maintaining real-time synchronization with blockchain data Building reliable AI models for pattern detection User Experience Making complex blockchain data accessible to non-technical users Creating intuitive visualizations of network relationships Balancing depth of analysis with speed of delivery Ensuring accuracy of AI-generated insights Accomplishments that we're proud of Successfully integrated graph-based RAG with blockchain data Developed a conversational interface for complex blockchain queries Created an NFT-based system for investigation permanence Built scalable pipeline for processing multiple data sources Achieved real-time monitoring and alert capabilities Developed sophisticated pattern recognition algorithms Created an intuitive user interface for complex data visualization What we learned The power of combining graph databases with blockchain data Importance of user experience in blockchain tools Challenges of processing and analyzing on-chain data at scale Techniques for optimizing graph-based queries Methods for ensuring AI model accuracy with blockchain data Strategies for effective data visualization NEAR Protocol's capabilities for building complex applications What's next for Chain Sleuth (Graph SaaS) Technical Expansion Cross-chain analytics integration Enhanced AI prediction models Advanced graph analysis capabilities Automated investigation templates Feature Development Custom investigation workflows API marketplace for developers Enhanced visualization tools Community-driven investigation sharing Market Growth Enterprise solution deployment Integration with DeFi protocols Compliance tool development Educational resources and training Community Building Investigation template marketplace Collaborative investigation tools Expert network development Knowledge sharing platform CHAIN SLEUTH is more than a tool - it's a platform that democratizes blockchain intelligence, making sophisticated analysis accessible to everyone in the Web3 ecosystem. By combining the power of NEAR Protocol, graph databases, and AI, we're creating a new standard for blockchain investigation and analysis. <div