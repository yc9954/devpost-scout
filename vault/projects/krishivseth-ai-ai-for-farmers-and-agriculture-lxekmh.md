---
slug: "krishivseth-ai-ai-for-farmers-and-agriculture-lxekmh"
url: "https://devpost.com/software/krishivseth-ai-ai-for-farmers-and-agriculture-lxekmh"
title: "KrishivSeth AI-(AI for farmers and Agriculture)"
hackathon: "Frostbyte Hackathon"
organization: "FrostByte Club"
winner: true
words: 791
team_size: 1
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/benchmark_measured"
  - "mechanism/realtime_stream"
  - "mechanism/voice_speech"
  - "domain/agriculture_food"
  - "domain/civic_government"
  - "user/frontline_worker"
  - "substrate/sensor_telemetry"
  - "substrate/structured_db"
  - "substrate/video_visual"
---

# KrishivSeth AI-(AI for farmers and Agriculture)

> KrishivSeth AI is an offline farming assistant that detects crop diseases,predicts risks,irrigation and fertilizer,analyzes market trends & uses quantum-optimization to choose the most profitable crop

[Devpost](https://devpost.com/software/krishivseth-ai-ai-for-farmers-and-agriculture-lxekmh) · hackathon [[Frostbyte Hackathon]]

## Facets

**mechanism** [[benchmark_measured]] [[realtime_stream]] [[voice_speech]]
  <sub>weak: simulation_digital_twin</sub>
**domain** [[agriculture_food]] [[civic_government]]
  <sub>weak: supply_logistics</sub>
**user** [[frontline_worker]]
**substrate** [[sensor_telemetry]] [[structured_db]] [[video_visual]]
  <sub>weak: web_dom</sub>

**stack** css, fastapi, html, javascript, python, script.js

## How they structured the write-up

- how we built it
- ⚔ challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for krishivseth ai

## Body

KrishivSeth AI INSPIRATION STORY: In many villages, farmers don’t fail because they lack effort — they fail because they lack predictive intelligence. They decide crops based on tradition, not data. They sell in mandis without knowing future price trends. They overuse water and fertilizers because advisory systems are generic, not hyper-local. After studying platforms like Crop in and nurture farm, we noticed something critical: They provide data, but not decision optimization. There is no system that answers: “What should this farmer grow, this season, on this land, to maximize net profit with minimal risk?” That gap inspired us to build an AI-driven agricultural profit engine — not just an advisory app, but a decision-making system that predicts ROI, optimizes inputs, and connects farmers directly to high-value buyers. We believe farming should move from guesswork to algorithmic precision. KrishivSeth AI – AI for Agriculture Inspiration India is one of the largest agricultural economies, yet farmers face: Late disease detection Unpredictable weather Poor market price awareness Excess fertilizer usage Lack of localized advisory Our mission is making AI accessible to every farmer using only a smartphone. What it does Crop Disease Detection Farmers upload an image → AI predicts disease → treatment suggestion provided. 💡 What It Does 🌿 1. Crop Disease Detection (CNN Based) We classify plant leaf images using Convolutional Neural Networks. Image transformation: $$ I' = W * I + b $$ Convolution operation: $$ S(i,j) = (I * K)(i,j) = \sum_m \sum_n I(m,n)K(i-m,j-n) $$ Activation function (ReLU): $$ ReLU(x) = \max(0,x) $$ Softmax classification: $$ P(y=i|x) = \frac{e^{z_i}}{\sum_{j} e^{z_j}} $$ Cross-entropy loss: $$ Loss = -\sum y \log(\hat{y}) $$ Python Model Code import tensorflow as tf from tensorflow.keras import layers, models model = models.Sequential([ layers.Conv2D(32, (3,3), activation='relu', input_shape=(128,128,3)), layers.MaxPooling2D((2,2)), layers.Conv2D(64, (3,3), activation='relu'), layers.MaxPooling2D((2,2)), layers.Flatten(), layers.Dense(128, activation='relu'), layers.Dense(10, activation='softmax') ]) model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'] Accuracy calculation: \( Accuracy = \frac{Correct\ Predictions}{Total\ Predictions} \) 🌦 Weather-Based Advisory Evapotranspiration model: ET0=Δ+γ(1+0.34u2)0.408Δ(Rn−G)+γT+273900u2(es−ea) Soil Moisture Index: SMI= Field Capacity Current Moisture If SMI<0.5⇒Irrigation=Required Uses forecast data to suggest irrigation timing. Example moisture estimation: $$ Soil\ Moisture\ Index = \frac{Rainfall + Irrigation}{Evaporation + Crop\ Usage} $$ ```const axios = require('axios'); async function getWeather(city) { const response = await axios.get( https://api.weatherapi.com/v1/current.json?key=API_KEY&q=${city} ); return response.data; }``` Market Price Intelligence Displays mandi prices to optimize selling decisions. Profit estimation formula: $$ Profit = Selling\ Price - Production\ Cost $$ Using Linear Regression \y=β0+β1x1+β2x2+ϵ\ $$ MSE=n1i=1∑n(yi−y^i)2 $$ $$ θ:=θ−α∇J(θ) $$ ```from sklearn.linear_model import LinearRegression model = LinearRegression() model.fit(X_train, y_train) predicted_price = model.predict(X_test)``` 🧪 Fertilizer Optimization Recommends fertilizer quantity based on soil nutrients. \( Recommended\ Fertilizer = Required\ Nutrient - Available\ Nutrient \) AI Decision Engine Using Logistic Regression $$ P(Disease)=1+e−z1 z=w1x1+w2x2+b P(A∣B)=P(B)P(B∣A)P(A) $$ System Architecture Farmer → Mobile App → API Gateway → AI Model → Decision Engine → Recommendation Time Complexity: $$ CNN Training :O(n⋅d⋅k2) , Inference : O(d⋅k2) $$ Multilingual Voice Support Speech-to-text and text-to-speech integration for accessibility. Quantum Farming Mathematical Layer Quantum State of Farm Conditions Represent farm condition as superposition: ∣ψ⟩=α∣Yield⟩+β∣Profit⟩+γ∣Water⟩+δ∣Risk⟩ Constraint: ∣α∣2+∣β∣2+∣γ∣2+∣δ∣2=1 This models uncertainty in: Weather Soil Market Quantum Decision Probability Probability of selecting decision P(Di)=∣⟨Di∣ψ⟩∣2 System chooses highest probability farming strategy. Quantum Optimization Objective Instead of single optimum: min H where Hamiltonian : H=w1Yield+w2Profit−w3Risk−w4Water Quantum Annealing Inspired Optimization Energy minimization: E=i,j∑Jijxixj+i∑hixiUsed to find: ✔ Best crop ✔ Best irrigation ✔ Best fertilizer combination Quantum-Inspired Code Layer : Quantum Decision Simulator ; import numpy as np def quantum_decision(yield_val, profit, risk, water): state = np.array([yield_val, profit, -risk, -water]) norm = np.linalg.norm(state) psi = state / norm probabilities = psi**2 return probabilities Quantum Optimization Score : def hamiltonian(yield_val, profit, risk, water): w = [0.4, 0.3, 0.2, 0.1] return w[0]*yield_val + w[1]*profit - w[2]*risk - w[3]*water Quantum-inspired Best Plan Selection : best_plan = min(plans, key=lambda x: hamiltonian(*x)) How we built it Frontend Flutter / React Native AI Model CNN-based classifier Built using TensorFlow / PyTorch Loss function: $$ Loss = -\sum y \log(\hat{y}) $$ Backend Node.js / Firebase REST APIs for weather and mandi data ⚔ Challenges we ran into Low-quality image inputs Limited dataset for regional crops Ensuring safe fertilizer recommendations Real-time API integration UI simplicity for rural users Regularization : Lreg=L+λ∣∣w∣∣2 Dropout: y=f(Wx)⋅mask Performance Metrics Precision: Precision=TP/TP+FP Recall=TP/TP+FN F1 Score: F1=2⋅Precision+RecallPrecision⋅Recall Future Work: LSTM for time-series price prediction:ht = σ(Whht−1+Wxxt) Reinforcement Learning for irrigation control:Q(s,a)=Q(s,a)+α[r+γmaxQ(s′,a′)−Q(s,a)] Accomplishments that we're proud of High validation accuracy Working end-to-end prototype Voice interaction support Scalable backend architecture What we learned Dataset quality directly impacts model performance Simplicity improves adoption Real-world deployment constraints differ from lab environments What's next for KrishivSeth AI Phase 1 – Pilot Deployment Field testing with farmers Phase 2 – Advanced AI Soil nutrient prediction Pest outbreak forecasting Outbreak prediction model: $$ P(Disease) = \frac{1}{1 + e^{-z}} $$ Phase 3 – Scale Government partnerships Nationwide deployment <div