---
slug: "upi_fraud_detection"
url: "https://devpost.com/software/upi_fraud_detection"
title: "UPI_Fraud_Detection"
hackathon: "DSH Hacks V1"
organization: "DreamWeave"
winner: true
words: 567
team_size: 1
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "domain/finance_payments"
  - "domain/retail_commerce"
  - "domain/supply_logistics"
  - "user/small_business"
  - "substrate/financial_record"
  - "substrate/sensor_telemetry"
  - "substrate/structured_db"
  - "substrate/web_dom"
---

# UPI_Fraud_Detection

> AI-powered UPI fraud detection system that analyzes transaction patterns in real time to identify suspicious activities and help prevent digital payment fraud.

[Devpost](https://devpost.com/software/upi_fraud_detection) · hackathon [[DSH Hacks V1]]

## Facets

**mechanism** [[realtime_stream]]
**domain** [[finance_payments]] [[retail_commerce]] [[supply_logistics]]
**user** [[small_business]]
**substrate** [[financial_record]] [[sensor_telemetry]] [[structured_db]] [[web_dom]]

**stack** css3, flask, github, html5, javascript, lightgbm, numpy, pandas, python, render, scikit-learn, smote, xgboost

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- what we learned
- future improvements

## Body

Inspiration With the rapid growth of digital payments in India, UPI has become one of the most widely used payment systems . However, this convenience also brings an increase in digital fraud and suspicious transactions . Many fraud detection systems rely on simple rule-based methods that fail to detect new fraud patterns. This project was inspired by the idea of using machine learning to automatically detect suspicious transactions by analyzing patterns in transaction data such as amount, device type, bank details, and network information. The goal was to build a real-time fraud detection system that can help identify risky transactions before financial damage occurs. What it does The UPI Fraud Detection System predicts whether a transaction is fraudulent or legitimate based on various transaction features. Users can enter transaction details through a web interface, and the system instantly analyzes the data using a trained machine learning model. The model evaluates patterns in: Transaction amount Merchant category Transaction type Sender and receiver banks Device type Network type Time of transaction Based on these features, the system predicts if the transaction is safe or potentially fraudulent . How we built it The project combines machine learning with a full-stack web application . Data Processing The dataset contains 25,000+ UPI transactions with multiple transaction features. Data preprocessing steps included: Removing irrelevant columns such as transaction ID and timestamp Handling categorical variables using One-Hot Encoding Scaling numerical features using StandardScaler Handling class imbalance using SMOTE , since fraud transactions were extremely rare. Mathematically, SMOTE generates synthetic samples between minority class observations: x_new = x_i + λ (x_nn − x_i) Where: x_i = a minority class sample x_nn = one of its nearest neighbors λ = a random value between 0 and 1 Machine Learning Models Multiple models were tested to compare performance: Logistic Regression Random Forest XGBoost LightGBM Each model was evaluated using confusion matrix and classification metrics . The best performing model was then saved and integrated into the application. System Architecture The system is built with the following components: Frontend HTML CSS JavaScript Backend Flask (Python) Machine Learning Scikit-learn XGBoost LightGBM Imbalanced-learn (SMOTE) Deployment GitHub Render Cloud Platform Users submit transaction details → Flask backend processes the request → the ML model predicts fraud risk → result is displayed instantly. Challenges we ran into One of the biggest challenges was extreme class imbalance in the dataset. Out of 25,000+ transactions, only around 480 were fraud cases . This caused models to initially predict all transactions as normal , achieving high accuracy but failing to detect fraud. To solve this, SMOTE oversampling was applied to balance the training dataset. Another challenge was deploying a machine learning pipeline that contained preprocessing steps and categorical encoders. Ensuring compatibility between training and deployment environments required restructuring the pipeline and properly saving the model. What we learned Through this project we learned: How to handle imbalanced datasets in fraud detection Building machine learning pipelines for real-world deployment Integrating ML models with Flask APIs Deploying a full-stack AI application on cloud platforms Most importantly, we learned that accuracy alone is not enough in fraud detection . Metrics such as recall and precision for the fraud class are critical to evaluate real-world effectiveness. Future Improvements This project can be further enhanced by: Using deep learning models for sequential transaction analysis Integrating real-time streaming transaction data Implementing risk scoring systems Adding user authentication and monitoring dashboards <div