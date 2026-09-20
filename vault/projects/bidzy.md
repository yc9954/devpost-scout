---
slug: "bidzy"
url: "https://devpost.com/software/bidzy"
title: "Bidzy"
hackathon: "MEGA Hackathon 2025"
organization: "MegaHackathonLeague"
winner: true
words: 403
team_size: 5
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/cross_origin_web"
  - "mechanism/realtime_stream"
  - "domain/developer_tools"
  - "domain/finance_payments"
  - "domain/supply_logistics"
  - "domain/transportation"
  - "user/developer"
  - "substrate/geospatial"
  - "substrate/structured_db"
---

# Bidzy

> Revolutionize logistics with real-time bidding! Shippers post jobs, carriers bid live—saving costs, ensuring reliability, and tracking shipments. AI + blockchain for trust & efficiency.

[Devpost](https://devpost.com/software/bidzy) · hackathon [[MEGA Hackathon 2025]]

## Facets

**mechanism** [[cross_origin_web]] [[realtime_stream]]
**domain** [[developer_tools]] [[finance_payments]] [[supply_logistics]] [[transportation]]
**user** [[developer]]
**substrate** [[geospatial]] [[structured_db]]

**stack** escrow, eth, express.js, javascript, mongodb, nextauth, nextjs, node.js, prisma, railway, react, shadcn, socket.io, sol

## How they structured the write-up

- inspiration
- what we learned
- how we built it
- architecture diagram
- challenges

## Body

Landing Page AI Chatbot User can create bids here Live Bidding Page User History Smart Contracts AI Price Calculator About Bidzy - Global Shipping Marketplace Inspiration The logistics market is broken — opaque pricing, poor fleet utilization, and missed opportunities are bleeding value from both sides. Inspired by the dynamics of financial markets and the efficiency of real-time trading platforms , Bidzy introduces a high-frequency bidding system that flips the script. Clients lock in the best shipping rates through a live, competitive auction. Logistics providers increase fleet efficiency and maximize profit margins by securing more jobs at optimal rates. Market-driven transparency ensures fair pricing and better decision-making for both parties. Bidzy isn’t just another shipping platform — it’s a dynamic marketplace that turns logistical chaos into a structured, profit-maximizing opportunity. What we Learned Building Bidzy taught me invaluable lessons about: Real-time technologies : Implementing Socket.IO for live bidding required a deep understanding of WebSocket connections, event handling, and state synchronization. UX for competitive environments : Designing interfaces that remain calm and usable during fast-paced bidding scenarios. Payment processing : Integrating secure payment flows while maintaining a smooth user experience. Logistics domain knowledge : Understanding the complexities of shipping requirements across different transport methods. How we Built It Bidzy was constructed using a modern tech stack: Frontend : Next.js with TypeScript for type safety and better developer experience. Styling : TailwindCSS for responsive, utility-first styling. Real-time communication : Socket.IO for bidding events and notifications. Authentication : NextAuth.js for secure user management. Database : Prisma ORM with PostgreSQL for data persistence. Deployment : Vercel for the main application and Railway for dedicated socket server. The architecture follows a hybrid approach with server-side rendering for improved SEO and client-side interactivity for the dynamic bidding interfaces. Architecture Diagram Frontend : link Backend : link API : link Challenges The journey wasn't without obstacles: CORS configuration : Setting up proper cross-origin resource sharing between the main app and socket server proved particularly challenging when deploying to production. Race conditions : Managing concurrent bids required careful state management to prevent conflicts. Real-time data sync : Ensuring all users see the same bid information simultaneously across devices. Performance optimization : Reducing unnecessary re-renders during high-frequency bid updates. Despite these challenges, the platform has evolved into a robust solution that simplifies shipping logistics for businesses of all sizes while creating new opportunities for carriers to optimize their routes and capacity. <div