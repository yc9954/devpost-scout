---
slug: "rydr-xnd1t9"
url: "https://devpost.com/software/rydr-xnd1t9"
title: "Rydr"
hackathon: "Build Resilient Apps with Polkadot Cloud"
organization: "POLKADOT"
winner: true
words: 729
team_size: 2
has_repo: true
has_live: true
has_video: false
tags:
  - "project"
  - "domain/developer_tools"
  - "domain/finance_payments"
  - "domain/labor_employment"
  - "domain/supply_logistics"
  - "domain/transportation"
  - "user/frontline_worker"
  - "substrate/document_pdf"
  - "substrate/financial_record"
  - "substrate/geospatial"
  - "substrate/structured_db"
---

# Rydr

> Ride Together,Earn Together

[Devpost](https://devpost.com/software/rydr-xnd1t9) · hackathon [[Build Resilient Apps with Polkadot Cloud]]

## Facets

**domain** [[developer_tools]] [[finance_payments]] [[labor_employment]] [[supply_logistics]] [[transportation]]
**user** [[frontline_worker]]
**substrate** [[document_pdf]] [[financial_record]] [[geospatial]] [[structured_db]]

**stack** appwrite, moonbase, moonbeam, polkadot, react, solidity, tailwind, vercel

## How they structured the write-up

- inspiration
- what it does
- how we built it
- accomplishments we're proud of
- what we learned
- what's next for rydr
- dream big

## Body

My Rides Offer a ride My account Home Page Trip information Featur Find a Ride RYDR - Decentralized Ride-Sharing on Polkadot Inspiration Living in Uganda, I've watched friends and family struggle with expensive ride-sharing apps that take 25-30% commission from drivers. Meanwhile, passengers worry about payment disputes and hidden fees. I thought: what if blockchain could solve this? Not just as a tech experiment, but as a real solution that puts money back in drivers' pockets and gives passengers transparent, trustless transactions. The math is simple but powerful: $$\text{Driver Earnings}_{\text{Traditional}} = \text{Price} \times (1 - 0.25) = 75\% \text{ of fare}$$ $$\text{Driver Earnings}_{\text{RYDR}} = \text{Price} - \text{Gas Fee} \approx 95-98\% \text{ of fare}$$ That's a 20-25% increase in earnings for the same work. For a driver making 10 rides/day at $15/ride, that's an extra $825/month - enough to change lives. What it does RYDR is a peer-to-peer ride-sharing platform where: Drivers post rides with their route, timing, and price Passengers book rides and pay upfront - funds are held in escrow Smart contracts automatically release payment when the ride completes Both parties connect using familiar wallets (MetaMask or Polkadot wallets like SubWallet) The magic happens through Moonbase Alpha - drivers keep 95%+ of fares instead of 75%, passengers get transparent pricing, and nobody needs to trust a middleman. How we built it Frontend Stack: React + Vite for a snappy user experience Tailwind CSS for responsive design Mapbox for interactive route visualization Blockchain Layer: Solidity smart contract deployed on Moonbase Alpha (Polkadot's EVM-compatible parachain) Dual wallet support: MetaMask and Polkadot wallets (SubWallet, Talisman) @polkadot/extension-dapp for native Polkadot integration Backend: Appwrite for storing ride metadata (coordinates, driver info) Hybrid approach: blockchain for money, database for speed The smart contract handles escrow: function bookRide(uint256 rideId) external payable { require(msg.value == rides[rideId].price, "Incorrect payment"); rides[rideId].passenger = payable(msg.sender); rides[rideId].status = RideStatus.Booked; // Funds held in contract until release } ## Challenges We Ran Into ### 1. The Network Confusion At **3 AM**, I deployed to the **Base network by mistake**, then spent hours debugging why my **Moonbase** contract wasn't responding. **Lesson learned:** always double-check your **Chain ID**! ### 2. Two Wallet Types, One App Supporting both **MetaMask (Ethereum)** and **SubWallet (Polkadot)** was tricky. SubWallet has its own **EVM account** that's different from the **Substrate address** conversion. I had to detect which wallet was active and route transactions accordingly: ```javascript if (isSubWallet) { // use EVM account from SubWallet } else { // MetaMask flow } 3. Coordinate Chaos Mapbox uses [lng, lat] arrays, Appwrite stores {lat, lng} objects. I kept placing markers in the ocean 🌊. The fix was simple but took too long: const correctedCoords = [location.lng, location.lat]; 4. The BigNumberish String Error When canceling rides, I mistakenly passed Appwrite document ID (hex string) instead of the blockchain ride ID (number) . Smart contracts do NOT like that. Added a proper field: { "blockchainRideId": 42 } Accomplishments We're Proud Of ✨ It actually works! You can create a ride, book it with DEV tokens , and the escrow releases correctly. ✨ Dual wallet support — full integration for both Ethereum (MetaMask) and Polkadot (SubWallet). ✨ Real-world potential — could genuinely help drivers in my community earn more. ✨ Learned so much — Substrate ↔️ EVM compatibility, wallet systems, hybrid storage patterns. What We Learned Technical Moonbeam's unified accounts are genius — one address for Substrate + EVM. Gas estimation often tells you why a transaction will fail . Hybrid storage (blockchain + database) is ideal for dApps. Design Users don't care about decentralization — they care about saving money and avoiding disputes . Wallet UX matters — every extra step reduces conversions. Better errors → "Ride already booked" instead of "BAD_DATA". Philosophy Not everything belongs on-chain. Use blockchain for trust , databases for speed . Familiar UX is key for Web3 adoption. What's Next for RYDR Short-term Add on-chain reputation system . Ride scheduling (book later). React Native mobile app. Medium-term Deploy to Moonbeam Mainnet → Astar → Acala. DAO governance for fee decisions. Add an insurance pool . Long-term Cross-chain payments via XCM (DOT → GLMR). AI route optimization . Expand to logistics — packages and delivery. Dream Big What if every gig worker kept 95% of their earnings instead of 70% ? Blockchain makes that possible. RYDR is just the beginning. Built with ❤️ for the Polkadot Hackathon . <div