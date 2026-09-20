---
slug: "aurascan_elite"
url: "https://devpost.com/software/aurascan_elite"
title: "MediVerify-Pro"
hackathon: "Frostbyte Hackathon"
organization: "FrostByte Club"
winner: true
words: 447
team_size: 1
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "domain/developer_tools"
  - "domain/health_clinical"
  - "domain/supply_logistics"
  - "user/general_public"
  - "user/patient_family"
  - "substrate/code_repository"
  - "substrate/financial_record"
  - "substrate/geospatial"
  - "substrate/structured_db"
---

# MediVerify-Pro

> MediVerify Pro: A secure MERN-stack platform to combat counterfeit medicine. Instant serial verification for consumers and smart inventory management for admins. Safety in every dose.

[Devpost](https://devpost.com/software/aurascan_elite) · hackathon [[Frostbyte Hackathon]]

## Facets

**mechanism** [[realtime_stream]]
**domain** [[developer_tools]] [[health_clinical]] [[supply_logistics]]
**user** [[general_public]] [[patient_family]]
**substrate** [[code_repository]] [[financial_record]] [[geospatial]] [[structured_db]]

**stack** bcrypt, css3, express.js, html5, javascript, jwt, mongodb, node.js, postman

## How they structured the write-up

- 💡 inspiration
- 🔍 what it does
- 🛠️ how we built it
- 🚧 challenges we ran into
- 🏆 accomplishments that we're proud of
- 📚 what we learned
- 🚀 what's next for mediverify-pro

## Body

💡 Inspiration The global rise in counterfeit pharmaceuticals is not just a logistical problem; it’s a life-threatening crisis. I was inspired to create MediVerify Pro to provide a transparent, foolproof shield for patients. My goal was to turn every smartphone into a professional verification tool, ensuring that "Medicine is for Healing, Not for Risk." 🔍 What it does MediVerify Pro serves two main roles: For Admins: A robust dashboard to manage pharmaceutical inventory, track stock, and generate secure, non-sequential serial numbers. For Consumers: A public portal where anyone can input a serial number to instantly check authenticity. The system doesn't just verify the ID; it calculates if the product is safe or expired based on real-time data. 🛠️ How we built it The project utilizes the MERN stack for high performance and scalability: Backend: Node.js and Express manage the API architecture. Database: MongoDB stores medicine records and admin credentials securely. Frontend: A modern SPA built with JavaScript and Tailwind CSS, featuring a sophisticated Glassmorphism UI. Security: Every admin session is protected by JWT and passwords are encrypted using Bcryptjs . To ensure the uniqueness of our serial numbers, we rely on high-entropy generation. The probability $P$ of a collision can be expressed as: $$P \approx 1 - e^{-\frac{n^2}{2 \times 62^L}}$$ (Where $n$ is the number of IDs and $L$ is the character length) . 🚧 Challenges we ran into One of the toughest hurdles was implementing the Dual-Validation Logic . We had to ensure that if a serial number exists but the product is past its expiry date, the user receives a "Warning" rather than a "Success" message. Synchronizing date objects between the server's MongoDB timezone and the user's local browser time required precise handling of ISO strings. 🏆 Accomplishments that we're proud of Successfully creating a fully responsive interface that maintains its premium "Glass" look across both Desktop and Mobile devices. Implementing a Live Search feature that filters hundreds of medicine records instantly without refreshing the page. Building a secure authentication middleware that effectively guards the pharmaceutical database from unauthorized access. 📚 What we learned Building MediVerify Pro taught me the importance of Clean Architecture . I learned how to separate concerns by using: models/ for data structure. routes/ for API endpoints. middleware/ for security layers. This modular approach made debugging much faster and allowed for a scalable codebase. 🚀 What's next for MediVerify-Pro The vision doesn't stop here. Future updates will include: QR Code Integration: Allowing users to scan a code instead of typing serial numbers. Blockchain Ledger: Moving the verification records to a decentralized ledger to make them 100% immutable. Email Alerts: Automatically notifying admins when a batch is approaching its expiration date. <div