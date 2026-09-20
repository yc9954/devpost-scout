---
slug: "aidverify"
url: "https://devpost.com/software/aidverify"
title: "AidVerify"
hackathon: "Frostbyte Hackathon"
organization: "FrostByte Club"
winner: true
words: 686
team_size: 4
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/provenance_signing"
  - "mechanism/realtime_stream"
  - "mechanism/vision_ocr"
  - "domain/civic_government"
  - "domain/finance_payments"
  - "domain/labor_employment"
  - "user/frontline_worker"
  - "user/government_staff"
  - "substrate/code_repository"
  - "substrate/document_pdf"
  - "substrate/financial_record"
  - "substrate/video_visual"
---

# AidVerify

> AidVerify is a blockchain-powered platform that ensures transparent, fraud-free aid distribution through AI-based face recognition, connecting donors, NGOs, and field workers in a trusted ecosystem.

[Devpost](https://devpost.com/software/aidverify) · hackathon [[Frostbyte Hackathon]]

## Facets

**mechanism** [[provenance_signing]] [[realtime_stream]] [[vision_ocr]]
**domain** [[civic_government]] [[finance_payments]] [[labor_employment]]
**user** [[frontline_worker]] [[government_staff]]
**substrate** [[code_repository]] [[document_pdf]] [[financial_record]] [[video_visual]]

**stack** beautifulsoup4, clerk, cloudinary, ethers.js, express.js, fastapi, fuzzy, httpx, insightface, lucide-react, mongodb, mongoose, node.js, onnx-runtime

## How they structured the write-up

- 🔹 project title & summary
- 🔹 problem statement
- 🔹 target audience / beneficiaries
- 🔹 proposed solution
- 🔹 technical approach & tech stack
- 🔹 impact & feasibility
- 🔹 challenges & learnings
- 🔹 references & credits
- 🔹 files & links

## Body

Logo Ai review AI review summery Face verification landing page List you campaign Ngo Panel 🧾 AidVerify – AI-Powered Transparent Aid Distribution Platform Building trust through technology — making every donation count. AI + Blockchain for transparent, fraud-free humanitarian aid. 🔹 Project Title & Summary Title: AidVerify – Blockchain & AI-Powered Transparent Aid Distribution Platform Summary: Fraud and mismanagement in humanitarian aid systems often prevent donations from reaching real beneficiaries. AidVerify is an AI + Blockchain-powered platform that brings transparency, trust, and traceability to aid distribution. The system uses AI-based face recognition to verify beneficiaries in real time, ensuring that no person receives duplicate or unauthorized aid. All NGO applications and donation records are securely stored on the blockchain , offering immutable transparency for donors and administrators. An integrated AI NGO Verification API authenticates NGOs through document OCR and online cross-verification , ensuring that only legitimate organizations are approved. Donors can monitor campaign progress, transaction hashes, and fund utilization reports — guaranteeing end-to-end visibility . With FastAPI-based AI microservices , Ethereum smart contracts , and a React + Node.js architecture , AidVerify showcases how emerging technologies can restore public trust in social welfare systems — truly making every donation count. 🔹 Problem Statement Billions of dollars in humanitarian aid are lost annually due to fraudulent claims , identity manipulation , and opaque fund distribution . Existing platforms lack reliable identity verification mechanisms, resulting in duplicate beneficiaries and unverified NGOs . This erodes public confidence, discourages donations, and leaves genuine victims unsupported. AidVerify addresses this global challenge by: Verifying beneficiaries through AI-powered face recognition Auditing NGOs via AI document validation Recording all aid transactions on the blockchain for permanent transparency 🔹 Target Audience / Beneficiaries 💰 Donors: Individuals, corporations, and institutions seeking transparent charity impact. 🏢 NGOs: Verified organizations managing legitimate aid campaigns. 👨‍👩‍👧‍👦 Beneficiaries: Genuine recipients of humanitarian support. 🏛️ Government/Regulators: Oversight bodies ensuring fairness and compliance in aid distribution. 🔹 Proposed Solution AidVerify guarantees that aid reaches the right people through a three-tier verification pipeline : 🧠 AI Face Verification: Real-time beneficiary identification with liveness detection and duplicate prevention . 📑 AI NGO Verification: Automatic document scanning, OCR-based authenticity checks, and cross-referencing with public records. ⛓️ Blockchain Transparency: Immutable logs of donations, fund utilization, and NGO approvals for complete auditability. Its modular AI microservices and Ethereum smart contracts form a unified, fraud-resistant, and scalable ecosystem. 🔹 Technical Approach & Tech Stack 🖥️ Frontend React 19.1.1 Vite, TailwindCSS, Radix UI Clerk Authentication ⚙️ Backend Node.js, Express.js MongoDB, Cloudinary JWT Authentication, Multer 🤖 AI/ML Services FastAPI, InsightFace, YOLOv8/v11 ONNX Runtime, OpenCV, OCR (Tesseract) ⛓️ Blockchain Solidity (v0.8.18), Ethereum Network Truffle, Web3.js, IPFS Approach Justification: FastAPI + ONNX Runtime ensures low-latency AI inference. Ethereum provides decentralized and verifiable transparency. Microservice architecture enables modular scalability and independent upgrades. Cloudinary + IPFS securely manage images, proofs, and documents. 🔹 Impact & Feasibility 🌍 Transparency: Every donation is publicly traceable on the blockchain. 🔒 Fraud Reduction: Prevents fake NGOs and duplicate aid claims through AI-based verification. ⚡ Scalability: Cloud-native microservices allow easy deployment across regions. ❤️ Social Value: Restores confidence in humanitarian systems and optimizes real-world impact. AidVerify is deployable on AWS or GCP , using MongoDB Atlas and Smart Contracts on Testnet/Mainnet , making it ready for NGO pilots and CSR initiatives . 🔹 Challenges & Learnings 🚧 Challenges Handling low-quality mobile face captures during real-world verification. Synchronizing AI inference latency with blockchain transactions. Managing large-scale document datasets during OCR-based NGO validation. 🎓 Learnings Integrating AI and Blockchain can create scalable, trust-driven ecosystems. Emphasized the importance of data preprocessing and model optimization . Gained deeper understanding of ethical AI design , prioritizing fairness and privacy. 🔹 References & Credits Face Recognition: InsightFace (MIT License) OCR Engine: Tesseract.js Blockchain Tools: Truffle , Web3.js Team Members: 🧠 Debjyoti Ghosh – AI/ML Development 🎨 Biswajit Chatterjee – Frontend & UI/UX 🧩 Biswa Ganguly – Backend Development ⛓️ Diprajit Chakraborty – Blockchain & Smart Contracts 🔹 Files & Links GitHub Repository: https://github.com/aidverify Demo Video: 🎥 YouTube Demo – AidVerify Empowering trust through technology — ensuring every donation reaches those who need it most. <div