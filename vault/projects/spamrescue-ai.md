---
slug: "spamrescue-ai"
url: "https://devpost.com/software/spamrescue-ai"
title: "SpamRescue AI"
hackathon: "Kiroween"
organization: "Kiro"
winner: true
words: 1006
team_size: 1
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/deterministic_policy"
  - "mechanism/realtime_stream"
  - "domain/developer_tools"
  - "domain/retail_commerce"
  - "substrate/code_repository"
  - "substrate/sensor_telemetry"
  - "substrate/web_dom"
---

# SpamRescue AI

> Stitching together 40 years of email technology to rescue leads from spam

[Devpost](https://devpost.com/software/spamrescue-ai) · hackathon [[Kiroween]]

## Facets

**mechanism** [[deterministic_policy]] [[realtime_stream]]
  <sub>weak: benchmark_measured</sub>
**domain** [[developer_tools]] [[retail_commerce]]
**substrate** [[code_repository]] [[sensor_telemetry]] [[web_dom]]

**stack** cron, gemini, google, imap, javascript, node.js, nodemailer, typescript

## How they structured the write-up

- aka frankenmail ⚡
- 🎯 overview
- ✨ key features
- 🏗️ architecture
- 🚀 quick start
- 🧪 testing
- 📊 classification algorithm
- 🔒 security
- 📈 dashboard features
- 🛠️ development
- 🤝 contributing
- 🙏 acknowledgments

## Body

Hero section Lead detail Page SpamRescue AI 🧟‍♂️ aka FrankenMail ⚡ Stitching together 40 years of email technology to rescue business opportunities from spam 🎯 Overview Note: The UI has been continuously improved post-video submission. The demo video shows an earlier version, while the current codebase features enhanced design with Instrument Serif typography, shadcn-style buttons, and refined interactions. Core functionality remains identical. SpamRescue AI is an intelligent lead-recovery system that leverages hybrid AI classification to identify and rescue legitimate business inquiries from email spam folders. By combining legacy IMAP protocols with cutting-edge LLM technology, the system prevents revenue loss from missed customer communications. The Frankenstein Approach This project exemplifies the Frankenstein category by seamlessly integrating disparate technologies across four decades: IMAP Protocol (1986) - Legacy email retrieval with modern async wrappers Google Gemini AI (2024) - State-of-the-art large language model for intent classification Pattern-Based Classification - Traditional regex-based signal detection Real-time Webhooks - Modern asynchronous notification delivery Hybrid Scoring Algorithm - Weighted ensemble combining pattern matching (30%) and LLM analysis (70%) ✨ Key Features Core Capabilities Autonomous Monitoring - Scheduled IMAP scans with configurable intervals Hybrid AI Classification - Dual-mode analysis combining pattern recognition and LLM inference Multi-Channel Notifications - Webhook-based alerts via Slack, Telegram, Email, and SMS Real-time Dashboard - Express-based web interface with live statistics and lead management Encrypted Credential Storage - AES-256-GCM encryption for sensitive configuration data Property-Based Testing - Comprehensive test coverage using fast-check for correctness guarantees Classification Modes Pattern-Based - Fast, deterministic signal detection using regex patterns LLM-Only - Context-aware analysis via Google Gemini 2.5 Flash Hybrid (Recommended) - Weighted ensemble achieving 95%+ accuracy 🏗️ Architecture System Design Technology Stack Backend Runtime: Node.js 18+ with ES Modules Language: TypeScript 5.3 with strict mode Email: node-imap (IMAP client), mailparser (MIME parsing) AI: @google/generative-ai (Gemini SDK) Web: Express 4.x (REST API) Scheduling: node-cron (periodic execution) Security: Native crypto (AES-256-GCM) Frontend Framework: Vanilla JavaScript (zero dependencies) Styling: Tailwind CSS 3.x via CDN Icons: Lucide Icons Charts: Chart.js 4.x Testing Framework: Vitest (unit + integration) Property Testing: fast-check 3.x Coverage: 26 tests, 12 correctness properties 🚀 Quick Start Prerequisites Node.js 18 or higher IMAP-enabled email account (Gmail, Outlook, etc.) Google Gemini API key ( Get one here ) Installation # Clone the repository git clone https://github.com/yourusername/spam-rescue-ai.git cd spam-rescue-ai # Install dependencies npm install # Build the project npm run build Configuration Create environment file: cp .env.example .env Set your Gemini API key: # .env GOOGLE_GEMINI_API_KEY=your_api_key_here Configure email and notifications: cp config.example.json data/config.json Edit data/config.json : { "emailAccounts": [{ "id": "account1", "name": "Business Email", "imap": { "host": "imap.gmail.com", "port": 993, "user": "your-email@gmail.com", "password": "your-app-password", "tls": true, "spamFolderName": "[Gmail]/Spam" }, "enabled": true }], "notificationChannels": [{ "type": "slack", "config": { "webhookUrl": "https://hooks.slack.com/services/YOUR/WEBHOOK/URL" }, "enabled": true }], "confidenceThreshold": 70, "averageDealValue": 1000, "scanIntervalMinutes": 60, "classificationMode": "hybrid" } Running Development Mode: npm run dev Production Mode: npm start Access Dashboard: http://localhost:3000 🧪 Testing Run Test Suite npm test Test Coverage Unit Tests: Email parsing, classification logic, data persistence Integration Tests: End-to-end scan workflow Property Tests: 12 correctness properties with 100+ iterations each Property-Based Testing The system uses fast-check to verify invariants: // Example: Confidence scores must be bounded [0, 100] fc.assert( fc.property(arbitraryEmail, async (email) => { const result = await classifier.classify(email); return result.confidenceScore >= 0 && result.confidenceScore <= 100; }) ); 📊 Classification Algorithm Hybrid Scoring Formula The system employs a weighted ensemble approach: Confidence_hybrid = 0.3 × Confidence_pattern + 0.7 × Confidence_LLM Signal Detection Pattern-Based Signals: Inquiry language detection (e.g., "how much do you charge") Purchase intent keywords (e.g., "want to buy", "get a quote") Industry context markers Urgency indicators Contact request patterns LLM Analysis: Contextual understanding of email intent Sender credibility assessment Business legitimacy evaluation Nuanced language interpretation Performance Metrics Mode Accuracy Latency Cost Pattern 75% <100ms $0 LLM 92% ~2s ~$0.001/email Hybrid 95% ~2s ~$0.001/email 🔒 Security Credential Protection Encryption: AES-256-GCM for stored credentials Key Derivation: PBKDF2 with 100,000 iterations Environment Variables: Sensitive data via .env (gitignored) TLS: Enforced for IMAP connections Best Practices Use app-specific passwords (not account passwords) Rotate API keys regularly Restrict webhook URLs to trusted domains Enable 2FA on email accounts 📈 Dashboard Features Statistics View Total scans executed Leads detected and rescued Emails analyzed Average confidence scores Estimated revenue rescued Lead Management Detailed lead cards with sender information Confidence score visualization Signal breakdown charts AI reasoning display Email content preview Filtering by confidence range and date Detail Page Full email content Classification method indicator (Pattern/LLM/Hybrid) Signal analysis with weighted contributions Doughnut chart visualization Copy-to-clipboard functionality Lead status management 🛠️ Development Project Structure spam-rescue-ai/ ├── src/ │ ├── classification/ # AI classifiers (pattern, LLM, hybrid) │ ├── config/ # Configuration management │ ├── dashboard/ # Web UI and API │ ├── email/ # IMAP client and parser │ ├── notifications/ # Multi-channel dispatcher │ ├── persistence/ # JSON data store │ ├── scan/ # Orchestration logic │ ├── scheduler/ # Cron scheduling │ ├── security/ # Encryption utilities │ ├── types/ # TypeScript definitions │ └── index.ts # Application entry point ├── .kiro/ │ └── specs/ # Spec-driven development docs ├── data/ # Runtime data (gitignored) ├── dist/ # Compiled JavaScript └── tests/ # Test suites Scripts npm run dev # Development mode with hot reload npm run build # Compile TypeScript to JavaScript npm start # Production mode npm test # Run test suite npm run test:watch # Watch mode for tests npm run test:gemini # Test Gemini integration 🤝 Contributing Contributions are welcome! Please follow these guidelines: Fork the repository Create a feature branch ( git checkout -b feature/amazing-feature ) Commit your changes ( git commit -m 'Add amazing feature' ) Push to the branch ( git push origin feature/amazing-feature ) Open a Pull Request Development Guidelines Follow TypeScript strict mode Write property-based tests for new features Update documentation for API changes Maintain test coverage above 80% 🙏 Acknowledgments Kiro IDE - Spec-driven development workflow and AI assistance Google Gemini - LLM-powered intent classification Built with ⚡ by [Anuj Kumar] for Kiroween 2025 - Frankenstein Category Never miss a customer again. <div