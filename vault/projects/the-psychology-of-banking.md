---
slug: "the-psychology-of-banking"
url: "https://devpost.com/software/the-psychology-of-banking"
title: "The Psychology of Banking"
hackathon: "Plotly Analytics Vibe-a-Thon"
organization: "Plotly"
winner: true
words: 782
team_size: 1
has_repo: false
has_live: true
has_video: false
tags:
  - "project"
  - "mechanism/measured_ablation"
  - "mechanism/realtime_stream"
  - "mechanism/simulation_digital_twin"
  - "domain/finance_payments"
  - "domain/transportation"
  - "user/frontline_worker"
  - "substrate/sensor_telemetry"
  - "substrate/structured_db"
---

# The Psychology of Banking

> Unlock the psychology of banking. This interactive story goes beyond demographics to decode the hidden drivers of customer financial decisions, revealing what truly motivates a 'yes' to a campaign.

[Devpost](https://devpost.com/software/the-psychology-of-banking) · hackathon [[Plotly Analytics Vibe-a-Thon]]

## Facets

**mechanism** [[measured_ablation]] [[realtime_stream]] [[simulation_digital_twin]]
**domain** [[finance_payments]] [[transportation]]
**user** [[frontline_worker]]
**substrate** [[sensor_telemetry]] [[structured_db]]
  <sub>weak: video_visual</sub>

**stack** llm, plotly, python

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for the psychology of banking

## Body

Dashboard Screenshot Inspiration My inspiration for this project, "The Psychology of Banking," came from a fascination with the human element in data science. Often, data analysis focuses on cold, hard numbers and demographics. I wanted to go deeper and understand the 'why' behind customer behavior. I was particularly interested in how psychological factors, like economic stress, seasonal trends, and emotional responses to marketing, influence financial decisions. The UCI Bank Marketing dataset provided the perfect opportunity to explore this by moving beyond simple demographics and diving into the behavioral psychology of banking customers. What it does This project is an interactive Plotly dashboard that acts as a comprehensive behavioral analysis of financial decision-making. It transforms the raw UCI Bank Marketing dataset into a compelling data story. Identifies Customer Personas: It reveals six distinct customer personas based on their behavioral patterns, helping to categorize customers beyond simple age or income brackets. Predicts Economic Stress: The dashboard includes indicators that can predict a customer's likelihood to invest, highlighting the impact of economic stress. Optimizes Contact Strategies: It provides insights into the optimal timing and frequency of contact that can double conversion rates. Reveals Seasonal Psychology: It uncovers seasonal patterns in financial risk-taking, showing how customer behavior shifts throughout the year. Analyzes Campaign Fatigue: The dashboard identifies thresholds for campaign fatigue, helping banks avoid annoying customers and reduce diminishing returns. How we built it I built the dashboard using Python and a suite of powerful libraries. Data Cleaning & Preprocessing: I started with the UCI Bank Marketing dataset, which required extensive cleaning and feature engineering to prepare it for analysis. Exploratory Data Analysis (EDA): I used libraries like Pandas and NumPy to explore the data, calculate key metrics, and identify potential relationships. Advanced Data Profiling: I went beyond basic statistics, creating custom metrics and features that represent psychological and behavioral factors. Plotly Dashboard Creation: I used the Plotly library to create the interactive visualizations. I focused on building a coherent data story, linking different plots and insights to guide the user through the behavioral analysis. Deployment: I uploaded the dashboard to the Plotly Cloud, making it accessible and shareable. LLM Integration: I leveraged a Large Language Model (LLM) for Plotly to generate parts of the code and provide explanatory text for the different sections of the dashboard. This significantly sped up the development process and helped with the initial data storytelling. Challenges we ran into Data Interpretation: The most significant challenge was translating raw data points into meaningful psychological insights. It required a deep dive into the context of the dataset (e.g., the 2008-2010 financial crisis) to accurately interpret the customer behavior. Storytelling with Data: I struggled initially with making the dashboard a narrative rather than just a collection of charts. I had to carefully structure the flow to build a compelling case for the psychological drivers behind the data. Overfitting: In building the predictive models, I had to be careful to avoid overfitting, ensuring that the insights were generalizable and not just specific to the quirks of the dataset. Accomplishments that we're proud of Creating the Personas: I'm most proud of successfully creating and visualizing the six distinct customer personas. This went beyond the initial project scope and provided a powerful, actionable framework for banks. Insightful Predictions: The ability to identify economic stress indicators and predict investment likelihood was a major accomplishment, demonstrating the power of behavioral data. Successful Deployment: Deploying a complex, interactive dashboard on the Plotly Cloud was a significant technical achievement. What we learned This project taught me the importance of a human-centered approach to data science. It reinforced that the most valuable insights often come from understanding the context and the motivations behind the data. I learned: Advanced Plotly Skills: I gained a much deeper understanding of Plotly's capabilities for creating sophisticated, interactive dashboards. Data Storytelling: I learned how to craft a compelling narrative with data, using visuals to guide an audience toward a specific conclusion. The Power of LLMs: Using an LLM for code generation and explanation was a game-changer, showing me how AI can significantly accelerate the development process. What's next for The Psychology of Banking Real-time Data Integration: The next step is to integrate a real-time data source to make the dashboard dynamic and constantly updated. Predictive Modeling: I want to build a more robust predictive model to forecast customer churn or identify at-risk customers with greater accuracy. A/B Testing Simulation: I'd like to add a feature that allows users to simulate A/B tests on different marketing strategies to see the projected impact on conversion rates. Sentiment Analysis: I plan to incorporate sentiment analysis from social media data to get an even richer psychological profile of customers. <div