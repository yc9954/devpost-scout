---
slug: "protocol-aura"
url: "https://devpost.com/software/protocol-aura"
title: "Protocol: Aura"
hackathon: "Maximally Vibe-a-thon"
organization: "Maximally (https://maximally.in)"
winner: true
words: 795
team_size: 3
has_repo: true
has_live: false
has_video: false
tags:
  - "project"
  - "mechanism/human_in_the_loop"
  - "domain/supply_logistics"
  - "substrate/financial_record"
  - "substrate/geospatial"
  - "substrate/transcript_audio"
  - "substrate/video_visual"
---

# Protocol: Aura

> AI commerce is transactional; Aura makes it aesthetic. Standardizing how agents "vibe-check" inventory and negotiate style autonomously using 8-dimensional latent space manifolds.

[Devpost](https://devpost.com/software/protocol-aura) · hackathon [[Maximally Vibe-a-thon]]

## Facets

**mechanism** [[human_in_the_loop]]
**domain** [[supply_logistics]]
**substrate** [[financial_record]] [[geospatial]] [[transcript_audio]] [[video_visual]]

**stack** fastapi, gemini-2.0-flash, github, langchain-google-genai, numpy, plotly, pydantic, python, scikit-learn, streamlit, uv

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for protocol: aura
- additional notes

## Body

Protocol: Aura dashboard showing a successful aesthetic negotiation and live agent-to-agent transcript. Structured Vibe Receipt providing cryptographic proof and verifiable transcript hash for the autonomous trade. 8-dimensional radar chart showing the latent "vibe" analysis used by agents to align on aesthetic meaning Difference between Traditional and AURA Inspiration Current Agentic Commerce (like Google's "Buy for Me") is fundamentally transactional. Agents are exceptional at finding the cheapest price for a specific model number, but they are historically terrible at understanding Aesthetics . Humans don't shop for a "100% Cotton Black Shirt"; they shop for a "Succession-style quiet luxury look" or a "cyber-noir techwear vibe." We realized that for AI agents to truly represent human interests, they need a way to negotiate Meaning , not just Metadata . We built Protocol: Aura to bridge this gap—standardizing the latent space of "vibes" so agents can negotiate aesthetics autonomously. What it does Protocol: Aura is a Layer 2 extension for the Agentic Commerce Protocol (ACP). It replaces keyword-based search with 8-dimensional vibe vectors . Quantifiable Aesthetics : It maps emotional prompts (e.g., "CEO who codes at night") into a high-dimensional latent space across axes like rebellion , minimalism , and elegance . Agent-to-Agent Negotiation : A Shopper Agent sends a vibe-target and a budget mandate to multiple Boutique Agents. Aesthetic Swap Logic : Boutique Agents performing Manifold Analysis to find "Vibe-Close" products and propose transformations (e.g., swapping fabric types to drop price while preserving the silhouette). Autonomous Handshake : Agents evaluate trade-offs (Match vs. Distance) and execute a purchase if the shopper's mandate is satisfied. Vibe Receipt : Every successful trade generates a cryptographic receipt that proves the aesthetic alignment and budget satisfaction of the deal. How we built it We built the core engine in Python , using a modular architecture that separates the protocol logic from the agent personas. LLM Engine : We utilized Gemini 2.0 Flash to bridge the gap between human natural language and our 8-axis vibe model. Mathematics : We implemented a rigorous L2 Euclidean Distance formula to calculate the Aesthetic Match Score ($S$): $$S(V_s, V_p) = \frac{1}{1 + \sqrt{\sum_{i=1}^{n} (V_{s,i} - V_{p,i})^2}}$$ Protocol Schema : We used Pydantic to define a strict, machine-readable protocol (QUERY, OFFER, ACCEPT, REJECT) that ensures agents can talk to any store implementing the AURA standard. UI : A Streamlit dashboard provides a "God-view" of the agents' private conversations, including radar charts for vibe visualization and a live negotiation transcript. Challenges we ran into The biggest challenge was Mathematical Consistency . In a world of "vibes," it’s easy for things to feel subjective. We spent significant time calibrating our agent logic to ensure that an 85% match at Store A meant the same thing as an 85% match at Store B. Another hurdle was managing Trade-off Reasoning . Training an agent to decide when to prioritize "Budget-fit" over "Vibe-fit" required building a weighted decision engine that respects the shopper's drift tolerance—if the vibe is 10% off but the price is 40% lower, the agent has to decide if that’s a "winning" deal. Accomplishments that we're proud of We are incredibly proud of the Aesthetic Swap logic. Seeing a Boutique Agent intelligently suggest removing color accents to make a bundle "monochrome serious" just to stay under a user's budget—and having the Shopper Agent acknowledge that transformation—feels like the future of commerce. We successfully moved the needle from "Search" to "Negotiation." What we learned We learned that Latent Space is the UI of the future . As agents take over the clicking and the searching, the "User Interface" becomes the protocol itself. We also realized how powerful it is to standardizing "subjective" data; once you turn a "vibe" into a vector, it becomes a negotiable contract. What's next for Protocol: Aura Multi-Round "Counter" Turns : Moving beyond the 2-turn handshake into deeper bargaining. Cross-Store Bundling : Allowing a Shopper Agent to negotiate a single outfit across three different AURA-enabled boutiques. Vibe-Synthesis : Integrating with image generation models to show the user a high-fidelity visualization of the "negotiated aesthetic" before they confirm. ACP Integration : Fully aligning with the emerging Agentic Commerce Protocol standards to become the "Aesthetic Layer" of the agentic web. Additional Notes The Experiment AURA was born out of a playful experiment: Could two AI agents agree on what 'Elegant Chaos' looks like without a human in the loop? We realized that while LLMs are good at descriptions, they need a standardized mathematical framework to reach a consensus for commerce. The Aesthetic Extension We view AURA as a Layer 2 extension to the Agentic Commerce Protocol (ACP). While ACP handles the mechanics of the trade, AURA handles the aesthetic handshake , making it possible for agents to operate in subjective industries like fashion, interior design, and luxury goods. <div