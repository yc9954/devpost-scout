---
slug: "folio-n7mugb"
url: "https://devpost.com/software/folio-n7mugb"
title: "Folio"
hackathon: "RevenueCat Shipyard: Creator Contest "
organization: "RevenueCat"
winner: true
words: 612
team_size: 1
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/simulation_digital_twin"
  - "domain/developer_tools"
  - "user/government_staff"
  - "substrate/geospatial"
  - "substrate/video_visual"
---

# Folio

> A portfolio tracker for stocks, crypto, commodities, and forex in one app.

[Devpost](https://devpost.com/software/folio-n7mugb) · hackathon [[RevenueCat Shipyard- Creator Contest]]

## Facets

**mechanism** [[simulation_digital_twin]]
**domain** [[developer_tools]]
**user** [[government_staff]]
**substrate** [[geospatial]] [[video_visual]]

**stack** alphavantage, clerk, expo-router, expo.io, ios, nativewind, react, react-native, revenuecat, supabase, swift, swiftui, typescript, widgetkit

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for folio

## Body

Inspiration Every DIY investor has the same problem. Your money is spread across five different apps. Stocks in one, crypto in another, maybe some property or gold you inherited. You're diversified, which is great, but you have zero visibility into the full picture. You don't know if you're overexposed to tech or if one bad month tanks everything. I wanted one place to see it all, understand it, and actually act on it. What it does Folio is a unified portfolio tracker for iOS. You add your stocks, ETFs, crypto, real estate, commodities, savings, everything, and see your total net worth in one dashboard. Live prices, performance charts, day movers, asset breakdowns. iOS widgets show your portfolio value right from the home screen. An AI assistant that actually knows your holdings can review your portfolio, flag risks, and even make changes for you. Add a position, remove one, rebalance, straight from the chat. There's a full market browser with 1000+ assets, price alerts, and a news feed filtered to what you actually own. Monetization runs through RevenueCat. Free tier covers full tracking and widgets, Folio Pro unlocks the AI assistant, advanced analytics, and unlimited alerts. How we built it React Native with Expo SDK 55, TypeScript throughout. Zustand for state management, Clerk for auth, Supabase for the backend and cloud sync. RevenueCat handles subscriptions and the paywall. The AI assistant runs on Claude and has direct access to portfolio data so it can give real, specific advice and execute actions. iOS widgets are built with expo-widgets using SwiftUI components, with data pushed from the app via snapshots (no network calls in the widget itself). Screenshot import uses vision AI to read brokerage screenshots and auto-populate holdings. NativeWind for styling, expo-router for navigation. Challenges we ran into Expo SDK 55 is bleeding edge. We're on a preview release, and the widgets API is still alpha. Debugging SwiftUI components through an Expo bridge with almost no documentation was a lot of trial and error. Getting price data to flow correctly across auto-priced assets (always USD from the API) and manual assets (user-defined currency) while supporting display currency conversion took more plumbing than expected. The AI assistant needed to both understand the portfolio context and have the ability to actually mutate state, which meant building an action system that maps natural language intents to real store operations safely. Accomplishments that we're proud of The screenshot import genuinely works. Drop in a screenshot of your Robinhood or Coinbase and your holdings just appear. The AI assistant isn't a chatbot bolted on, it's deeply integrated. It reads your actual positions, does the math, and can execute changes with one tap. The widgets look clean and update reliably. And the whole thing feels like a real app, not a hackathon prototype. Onboarding, paywall, sync, the works. What we learned How much of the Expo ecosystem is moving right now. SDK 55 with the new architecture, widgets in alpha, router v7. We were building on shifting ground and had to adapt constantly. Also learned a lot about building AI features that go beyond "chat with a bot." Letting an LLM take real actions in your app requires careful guardrails and a solid action handling layer. RevenueCat made the monetization side surprisingly painless compared to dealing with StoreKit directly. What's next for Folio Android support is the obvious one. Deeper analytics like correlation between holdings, risk scoring, and historical what-if scenarios. Brokerage API integrations so you don't even need screenshots. Shared portfolios so couples or families can track together. And expanding the AI assistant to handle more complex actions like setting recurring investments or building model portfolios from scratch. <div