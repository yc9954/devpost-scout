---
slug: "cryptowise-intelligent-trading-and-insights-platform"
url: "https://devpost.com/software/cryptowise-intelligent-trading-and-insights-platform"
title: "CryptoWise: Intelligent Trading and Insights Platform"
hackathon: "Cal Hacks 11.0"
organization: "Cal Hacks"
winner: true
words: 768
team_size: 4
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "mechanism/simulation_digital_twin"
  - "user/researcher"
  - "substrate/structured_db"
  - "substrate/web_dom"
---

# CryptoWise: Intelligent Trading and Insights Platform

> Revolutionize your cryptocurrency trading experience with our platform that combines real-time data visualization, intelligent query handling, and automated trading strategies.

[Devpost](https://devpost.com/software/cryptowise-intelligent-trading-and-insights-platform) · hackathon [[Cal Hacks 11.0]]

## Facets

**mechanism** [[realtime_stream]] [[simulation_digital_twin]]
**user** [[researcher]]
**substrate** [[structured_db]] [[web_dom]]

**stack** express.js, fast, fetch, groq, javascript, kraken, machine-learning, metamask, node.js, python, react, single-store, smart-contract, websockets

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for cryptowise: intelligent trading and insights platform
- overview
- automated trading
- query handling
- data acquisition
- machine learning
- analytics

## Body

UI SingleStore DB Schema Data Number of Records Chatbot Response Automated Trading Logs ML API ping logs CryptoWise: Intelligent Trading and Insights Platform Inspiration The inspiration for CryptoWise stemmed from the dynamic and often unpredictable nature of the cryptocurrency market. We recognized the need for a comprehensive platform that not only provides real-time data but also offers intelligent insights and automated trading capabilities. Our goal was to empower traders, researchers, and enthusiasts with tools that enhance decision-making and streamline trading processes. What it does CryptoWise is an all-in-one platform designed to revolutionize the cryptocurrency trading experience. It offers: Real-Time Data Visualization: Users can view up-to-the-minute cryptocurrency values and trends through interactive charts. Intelligent Query Handling: A chatbot integrated with advanced LLM technology answers queries related to real-time, historical, and generic cryptocurrency data. Automated Trading: The platform includes a predictive model that suggests Buy, Sell, or Hold actions based on real-time data analysis, with the capability to execute trades automatically when conditions are met. How we built it We built CryptoWise using a combination of cutting-edge technologies: Data Acquisition: Integrated WebSocket APIs to fetch real-time cryptocurrency data, which is stored in SingleStore Database for fast retrieval and analytics. Visualization: Used SingleStore's analytics API to create dynamic charts that display changing market trends. Chatbot Integration: Leveraged the GROQ API and OpenAI 3.5 Turbo model to develop a chatbot capable of handling complex queries about cryptocurrency. Predictive Modeling: Developed a model trained on real-time and historical data from Kraken's WebSocket and OHLC APIs to make trading decisions. Automated Trading with Smart Contracts: Utilized smart contracts for executing trades securely. MetaMask authentication ensures secure access to users' wallets using private keys. Initially planned integration with Fetch.ai's agent-based tools faced challenges due to technical integration complexity and resource allocation constraints. Challenges we ran into Throughout the development of CryptoWise, we faced several challenges: Data Integration: Ensuring seamless integration of real-time data from multiple sources was complex and required robust solutions. Model Training: Continuously training the predictive model on diverse datasets to maintain accuracy was demanding. User Interface Design: Creating an intuitive and user-friendly interface that effectively displays complex data was challenging but crucial for user engagement. Agent-Based Trading Integration: The complexity of integrating Fetch.ai's agents with our existing infrastructure proved challenging, along with resource limitations. Accomplishments that we're proud of We are proud of several key accomplishments: Seamless Data Flow: Successfully integrated various data sources into a cohesive platform that delivers real-time insights. Advanced AI Integration: Implemented a sophisticated chatbot that enhances user interaction with accurate and relevant responses. Automated Trading Feature: Developed an automated trading system using smart contracts that executes trades based on predictive analytics, offering users a competitive edge. What we learned The development of CryptoWise taught us invaluable lessons: Importance of Data Accuracy: Real-time accuracy is critical in financial applications, necessitating rigorous testing and validation. AI Capabilities: Leveraging AI for query handling and decision-making can significantly enhance user experience and platform functionality. User-Centric Design: Designing with the user in mind is essential for creating an engaging and effective interface. What's next for CryptoWise: Intelligent Trading and Insights Platform Looking ahead, we plan to expand CryptoWise's capabilities by: Enhanced Predictive Analytics: Further refining our models to improve prediction accuracy and broaden the range of supported cryptocurrencies. User Personalization: Introducing features that allow users to customize their experience based on individual preferences and trading strategies. Community Engagement: Building a community around CryptoWise where users can share insights, strategies, and feedback to continuously improve the platform. CryptoWise aims to set a new standard in cryptocurrency trading by combining powerful analytics with intuitive design, making it an indispensable tool for anyone involved in the crypto market. API Documentation Overview This section provides details about the various API endpoints used in the CryptoWise platform, categorized according to their role in the architecture. Automated Trading Automated Purchase Endpoint URL: http://146.190.123.50:4000/api/simulate-purchase Purpose: Simulates the purchase of cryptocurrency based on model predictions. Query Handling Query to LLM URL: http://146.190.123.50:4000/query Purpose: Sends user queries to the LLM for categorization and response generation. Data Acquisition Kraken WebSocket API URL: wss://ws.kraken.com/ Purpose: Provides real-time cryptocurrency data for live updates. Historical Data URL: https://api.kraken.com/0/public/OHLC Purpose: Fetches historical price data for cryptocurrencies. Machine Learning ML Prediction API URL: http://146.190.123.50:5000/prediction Purpose: Provides predictions on Buy, Sell, or Hold actions based on real-time data analysis. Analytics Bollinger Bands URL: http://146.190.123.50:4000/api/analytics/bollinger-bands?coin=XBT&period=20&stdDev=2 Purpose: Calculates Bollinger Bands for specified cryptocurrency and period. Historical Volatility URL: http://146.190.123.50:4000/api/analytics/historical_volatility?coin=XBT Purpose: Computes historical volatility for the specified cryptocurrency. Stats URL: http://146.190.123.50:4000/api/analytics/stats Purpose: Provides statistical analysis of cryptocurrency data. Candle Data URL: http://146.190.123.50:4000/api/analytics/get_candle_data?coin=XBT Purpose: Retrieves candlestick data for detailed market analysis. <div