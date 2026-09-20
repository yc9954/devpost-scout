---
slug: "agentzero"
url: "https://devpost.com/software/agentzero"
title: "AgentZero"
hackathon: "TreeHacks 2025"
organization: "TreeHacks"
winner: true
words: 1044
team_size: 3
has_repo: true
has_live: false
has_video: false
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "mechanism/structural_withholding"
  - "domain/supply_logistics"
  - "substrate/structured_db"
---

# AgentZero

> Our autonomous and verifiable AI agent removes human inconsistency in making trading decisions, enabling data-driven trades with real-time analysis, customization, and safety.

[Devpost](https://devpost.com/software/agentzero) · hackathon [[TreeHacks 2025]]

## Facets

**mechanism** [[realtime_stream]] [[structural_withholding]]
**domain** [[supply_logistics]]
**substrate** [[structured_db]]

**stack** eigenlayer, gnark, go, python

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for agentzero

## Body

Workflow of our agent Inspiration As a stock-market investor, I deeply understand emotions are one of the greatest obstacles to success in financial markets. Humans have all felt the fear of uncertainty and loss, the temptation of impulsive choices, and the long period to react and make decisions. But what if we could remove human fragility and the reaction time from the equation? By using a fully automated , verifiable AI agent, we utilize technology to make precise, unstoppable, and data-driven decisions. Our fully autonomous agent is more than just a tool—it is a revolution in investing. With real-time analysis, user-defined customization, and adaptive intelligence, it ensures that trades are executed efficiently, rationally, strategically, and safely. The future of finance is not dictated by emotions, but by innovation . It is time to embrace the next generation of investment intelligence. What it does Our system consists of two specialized machine learning models: Price Model: This model is trained on historical Ethereum (ETH) price data, identifying patterns, trends, and volatility to make accurate price predictions. News Model: This model processes real-time news from Eigenlayer and other sources, analyzing sentiment, keywords, and market-moving narratives to gauge the impact of external events on ETH prices using the finBERT large language model. We combine these models by allowing users to assign custom weightings to each—giving them control over how much influence price trends versus news sentiment have on the agent’s final decision-making. Once the weighted predictions are generated, our fully automated AI agent can execute trades and market reactions in real-time, ensuring optimal strategies based on user preferences and live data. This level of customization and automation ensures a strategic, data-driven approach that removes emotional bias and maximizes efficiency in ETH trading. How we built it We built our system by integrating EigenLayer for fetching real-time news data and Dune for pulling Ethereum price data. News Processing: The news data is retrieved via EigenLayer and analyzed using an LLM (finBERT), which assigns a sentiment score from -1 to 1 continuously to each news event, where score 1 indicates most positive, -1 indicates most negative, and 0 represents neutral. We then computed the average score for all of related the news. Price Prediction: The price model is trained using a Random Forest Regression model on historical price data from Dune, identifying market trends and fluctuations. User Interaction & Agent Customization: Users can set custom weightings for the influence of news sentiment versus price prediction on decision-making. Users also define the execution frequency, determining how often the automated agent executes actions based on the weighted results. By combining these elements, our AI-driven system provides a fully customizable and verifiable trading agent, allowing users to optimize their strategies with real-time, data-driven decisions while eliminating emotional bias. Challenges we ran into At the beginning, we had limited knowledge of blockchain technology, making it challenging to deploy our agent on-chain. However, by learning from online resources and extensive research through Google, we gradually gained the coding skills needed to integrate agent. Another major challenge was designing a verification process to ensure that the model was trained on the intended dataset. Verifying the authenticity of training data in a decentralized environment is inherently complex. We addressed this by reducing the model's size, making it more efficient while maintaining transparency in the training process. Through persistence and problem-solving, we overcame these obstacles to build a trustworthy, on-chain AI trading agent that is both verifiable and efficient . Accomplishments that we're proud of We started from scratch and converted our innovative and crazy idea into an applicable real-world project. Through effective collaboration, extensive problem-solving, and actively seeking help from sponsors, our team built an impactful and inspiring AI agent that can own and manage on-chain data (current price), integrate verifiable off-chain services and Web3 APIs (Dune and Infura testnet faucet), and enforce policies or rules that guarantee safety, trust, and transparency. What we learned New knowledge in web3 and blockchain: We learned new knowledge in web3 and blockchain, which is a hot and intriguing area but brand new to all 3 of our team members, including the fundamental concepts like zero-knowledge proof and zkTLS, and TestNet. The fact that the agent can automatically generate proofs that provide users with an easy and efficient way of verification is intriguing to us. We also learned about the impactful companies in this area like EigenLayer with its Verifiable Agents and Taisu Venture, which helped us verify the source of the data we retrieved from OpenAI. As we developed our verification of machine learning datasets, we also came up with an interesting algorithm for proofing the dataset used. Technical skills: We also developed our coding skills by building up machine learning and LLM models and atomizing the whole process, and tested experiments with APIs. Soft and interpersonal skills: Moreover, as John Hennessy mentioned in the workshop, we should be humble and authentic and always do something new. We kept these values in mind through the whole process of TreeHacks, and always asking questions, sharing our thoughts, and thinking outside of the box to be innovative. Our team worked together from not knowing each other to close teammates and friends. Our interpersonal skills like teamwork and communication improved, and we knew how to work with people from different backgrounds and skillsets. What's next for AgentZero Although we have successfully deployed AgentZero on-chain, there is still room for improvement to enhance its performance and accuracy. Improved News Analysis: We aim to refine the news analysis logistics to better interpret and categorize news events with greater contextual understanding. Enhancing sentiment detection and incorporating entity recognition could improve decision-making accuracy. Higher-Resolution Data: Currently, due to the lack of a pro version, we are limited to hourly data rather than minute-by-minute or second-level updates. Upgrading our data pipeline to process more granular real-time data would enable faster, more responsive trading actions. AgentZero is also applicable to other coins in the future. Exploring Advanced Deep Learning Models: While Random Forest Regression has served us well, we plan to experiment with more advanced deep learning architectures such as LSTMs, Transformers, or Reinforcement Learning to improve price prediction accuracy. By implementing these improvements, AgentZero will continue evolving into a smarter, faster, and more precise AI-powered trading agent. <div