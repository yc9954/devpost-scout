---
slug: "ayuda-debo-dinero"
url: "https://devpost.com/software/ayuda-debo-dinero"
title: "Ayuda debo dinero"
hackathon: "HackMty 2025"
organization: "TEC ACM"
winner: true
words: 706
team_size: 3
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/voice_speech"
  - "domain/finance_payments"
  - "substrate/financial_record"
---

# Ayuda debo dinero

> An optimizer-first debt coach that turns your budget into exact per-card payments, cutting interest, lowering utilization, and guiding smarter financial decisions every month.

[Devpost](https://devpost.com/software/ayuda-debo-dinero) · hackathon [[HackMty 2025]]

## Facets

**mechanism** [[voice_speech]]
  <sub>weak: simulation_digital_twin</sub>
**domain** [[finance_payments]]
**substrate** [[financial_record]]
  <sub>weak: document_pdf, video_visual</sub>

**stack** anthropic, fastapi, gemini, nessieisreal, python, tailwind, typescript, vercel, vite

## Body

app cards team! Smart Wallet — Your Personal Finance Advisor Authors: Hildegard Zerrweck, Cyrce Danae Salinas & Israel Booz Rodríguez Abstract Smart Wallet is an optimizer-first system that calculates optimal payments across multiple credit cards using a compound interest model, and then uses large language models (LLMs) to generate personalized and easy-to-understand feedback. During development, the system can also ingest synthetic account and transaction data from the Capital One “Nessie” (nessieisreal) sandbox API. The main goal is to help users avoid interest, reduce credit utilization, and respect their monthly budget, using a mathematically grounded optimizer. The solution features a backend built in Python with FastAPI, a web interface developed with Vite, TypeScript, and Tailwind, and integrates Gemini API and Anthropic for AI-powered explanations. Project Description Smart Wallet addresses a real personal finance problem: helping users decide exactly how much to pay on each credit card to minimize interest and maintain a healthy utilization rate. Users log in, upload their credit card statements (PDF or image), and the system automatically extracts the relevant fields required for optimization — such as balances, limits, APRs, due dates, minimum payments, and installment amounts. Once the information is processed, the optimization engine determines an optimal payment plan for each card based on compound interest and budget constraints. The system ensures that users can cover minimum payments while allocating the remaining budget to minimize interest or balance utilization across all cards. The Gemini-based explanation module then translates the numerical results into clear, practical advice, explaining why each payment amount was chosen and how it improves the user’s financial situation. The web interface allows secure login, statement upload, data verification, plan visualization, and optional text-to-speech feedback powered by ElevenLabs. Inputs and Data For each credit card, the system uses the following data: total balance, credit limit, annual percentage rate (APR), remaining days in the cycle, minimum payment, installment balances, and the “pay no interest” threshold. At the user level, Smart Wallet takes a total monthly budget and reserves a portion (typically 30%) to maintain liquidity. The remaining amount is distributed optimally among all credit cards. When real data are unavailable, the system can use synthetic accounts and transactions from the Capital One “Nessie” API to simulate user cases during development. Optimization Model The optimization engine applies a compound interest function to evaluate how each payment reduces potential interest accumulation. If a payment does not reach the “pay no interest” threshold, the remaining balance will generate interest in the next cycle. Additionally, Smart Wallet considers credit utilization — encouraging payments that bring utilization closer to or below 30% — and ensures all minimum payments are met. By combining these objectives, Smart Wallet produces a balanced strategy that minimizes future interest, improves credit health, and respects the user’s monthly budget. System Architecture and Tech Stack Smart Wallet is built with a modular and transparent architecture: Backend: Python (pandas, cvxpy) and FastAPI for optimization and API endpoints. Frontend: Vite, TypeScript, and TailwindCSS for a responsive, modern UI. LLMs: Gemini (Google) and Anthropic (Claude) for generating human-like explanations. Data Sandbox: Capital One “Nessie” (nessieisreal) API for testing synthetic account and transaction data. Optional TTS: ElevenLabs API for text-to-speech feedback. Expected Outcomes When the user’s budget covers all “pay no interest” amounts, the total interest generated in that billing cycle becomes zero. If the budget is limited, Smart Wallet prioritizes payments where each dollar saves the most interest — typically on cards with higher APRs or longer remaining cycles. When the model includes a utilization weight, it also prioritizes reducing balances above 30% utilization to improve credit health. Privacy and Best Practices Smart Wallet maintains strict separation between public and private data. Public issuer data (such as reference interest rates) are stored separately, while user information is encrypted and never shared externally. API keys and environment variables are stored securely on the backend. Conclusion Smart Wallet provides a rigorous and transparent way to manage personal debt by combining mathematical optimization with AI-driven explanations. It helps users understand exactly what to pay, how much, and why, transforming complex financial planning into clear, actionable decisions. By preventing avoidable interest, reducing utilization, and empowering users with financial clarity, Smart Wallet becomes a reliable digital coach for smarter, stress-free debt management. <div