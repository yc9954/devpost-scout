---
slug: "finance-ai-uyi6g8"
url: "https://devpost.com/software/finance-ai-uyi6g8"
title: "Finance AI"
hackathon: "Databricks Generative AI World Cup"
organization: "Databricks"
winner: true
words: 422
team_size: 4
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/vision_ocr"
  - "substrate/structured_db"
---

# Finance AI

> Empowering Tomorrow's Investments with Today's Intelligence

[Devpost](https://devpost.com/software/finance-ai-uyi6g8) · hackathon [[Databricks Generative AI World Cup]]

## Facets

**mechanism** [[vision_ocr]]
  <sub>weak: retrieval_grounding</sub>
**substrate** [[structured_db]]

**stack** ai, chatbot, gdelt, generative, huggingface, langchain, llm, openai, python, rag, streamlit, text2sql, vectordb

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for finance ai

## Body

Finance AI: Solution Architecture Databricks Cluster for Compute Databricks Experiments Run Databricks Model Artifacts Databricks Registered Model Databricks Model Serving Inspiration The inspiration for this project stems from recognizing the need to simplify stock market analysis in the face of complex geopolitical events. It aims to empower decision-makers by providing accessible and timely insights, ultimately enhancing risk management and driving innovation in investment strategies. What it does The Finance AI project simplifies stock market analysis by distilling complex geopolitical data, empowering decision-makers to make informed choices amidst information overload. By democratizing access to sophisticated analysis, it enhances risk management, drives innovation, and enables proactive investment strategies in response to geopolitical events. How we built it To craft this solution, we harnessed the power of GDELT data for comprehensive analysis, employed open-source Hugging Face models to extract sentiment, and meticulously developed and deployed our solution within the Databricks platform. Challenges we ran into Below are the primary challenges encountered: Managing the extraction and querying of extensive GDELT datasets. Navigating the deployment process of the Streamlit application on the Databricks platform. Accomplishments that we're proud of We managed to find gdelt-doc-api that let us put filters while querying the data, in order to only get the subset of data required for our analysis. Usage of open source models to predict sentiment Creation of chatbot that can convert user queries in text to sql to get result from database Analysis of Volatility and sentiment relationship What we learned We've delved into the intricate relationship between market sentiment and its profound effects on both stock prices and volatility. Through our analysis, we've discerned how positive or negative perceptions among investors can significantly sway market dynamics, influencing the upward or downward movement of stock prices. Additionally, we've observed how shifts in sentiment can lead to fluctuations in market volatility, reflecting the level of uncertainty and risk aversion prevailing in the market. Understanding these dynamics has provided us with valuable insights into the psychological aspects driving financial markets and has equipped us to navigate and respond to changing market conditions more effectively. What's next for Finance AI Right now, we're using the Streamlit app to show off what our application can do. But down the road, we're thinking of trying out some other frameworks that can handle bigger loads. It's all about making sure our solution can grow with our users and keep up with whatever they throw at it. We're all about staying flexible and keeping things fresh to give our users the best experience possible. <div