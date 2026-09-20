---
slug: "boxoffice-ai"
url: "https://devpost.com/software/boxoffice-ai"
title: "Cineplex : Data-Driven Concession Optimization"
hackathon: "Frostbyte Hackathon"
organization: "FrostByte Club"
winner: true
words: 352
team_size: 2
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "substrate/sensor_telemetry"
---

# Cineplex : Data-Driven Concession Optimization

> We turn one-time viewers into loyal customers. Our XGBoost engine predicts customer retention so Cineplex can target high-value groups and boost concession margins.

[Devpost](https://devpost.com/software/boxoffice-ai) · hackathon [[Frostbyte Hackathon]]

## Facets

**substrate** [[sensor_telemetry]]
  <sub>weak: structured_db</sub>

**stack** jupyter-notebook, kaggle, matplotlib, numpy, pandas, python, scikit-learn, seaborn, shap, xgboost

## Body

💡 What Inspired Me I realized that movie theaters like Cineplex don't actually make their biggest profits from selling movie tickets—they make it at the concession stand selling popcorn and drinks. I was inspired by the idea that getting a customer to visit once is great, but getting them to return repeatedly is the true secret to growing a cinema's revenue. I wanted to use data to stop guessing and start mathematically proving exactly who comes back and why. 🛠️ How I Built It I built an end-to-end Machine Learning pipeline entirely within an interactive Jupyter Notebook. Data Prep: I started with a Kaggle dataset of cinema ticket sales. I cleaned the data and engineered a new metric called Estimated_Group_Spend (Ticket Price × Group Size) to track actual financial value. Customer Segments: Before predicting anything, I used an Unsupervised AI algorithm called K-Means Clustering to automatically group customers into 3 distinct behavioral buckets based on their age and spending habits. The Brains: I fed those segments into a highly advanced predictive engine called XGBoost. After hyper-tuning it to maximize accuracy, the model could predict if a customer would return. Transparency: Finally, I used SHAP (Explainable AI) to prove how the model made its decisions, ensuring business leaders could trust the output. 🧗 Challenges I Faced The biggest challenge was dealing with "Black Box AI." It's easy to build a model that spits out an accuracy number, but business stakeholders hate models they don't understand. I struggled with how to turn raw predictions into actionable business advice. Learning how to implement SHAP values was difficult, but it completely solved the problem by showing the exact directional impact of every single metric (like proving that large group sizes actively push customers toward returning!). 📚 What I Learned I learned that raw code isn't enough; you have to think like a business owner. I learned how to move beyond basic models like Random Forest into advanced Gradient Boosting (XGBoost). Most importantly, I learned how to use Unsupervised Learning (K-Means) to discover things about my customers that I didn't even know I was looking for. <div