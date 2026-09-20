---
slug: "marketview-vr"
url: "https://devpost.com/software/marketview-vr"
title: "MarketView VR"
hackathon: "Meta Horizon Start Developer Competition"
organization: "Meta"
winner: true
words: 536
team_size: 1
has_repo: false
has_live: false
has_video: true
tags:
  - "project"
  - "domain/developer_tools"
  - "user/developer"
---

# MarketView VR

> Track and analyze your stock portfolio across VR’s infinite screens—an immersive workspace for personal investors.

[Devpost](https://devpost.com/software/marketview-vr) · hackathon [[Meta Horizon Start Developer Competition]]

## Facets

**domain** [[developer_tools]]
**user** [[developer]]

**stack** android, android-studio, compose, kotlin, mcp

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for marketview vr

## Body

Inspiration Stock analysis has always been a multi‑screen activity: serious investors juggle charts, news, and multiple tickers at once, but are constrained by flat monitors and limited screen space. MarketView VR explores how virtual reality can turn that workload into an immersive, spatial environment, giving portfolio management the same “mission control” feel that professionals get from multi‑monitor desks—without the hardware overhead. What it does MarketView VR is a VR‑native stock analysis workspace for Meta Horizon OS. The current P0 build focuses on three panels: a Portfolio Overview Panel showing daily price and percentage changes across tracked stocks, a Stock Detail Chart Panel for exploring intraday and historical trends, and a News Panel surfacing relevant headlines in context. There is no trading or execution; the app is intentionally research‑only, designed for calm, focused market monitoring in VR. How we built it Started with Figma Make for initial mockups, refined in Figma for detail. Connected to Meta Horizon MCP server to incorporate all VR design recommendations. Built as an Android app targeting SDK 36 (compatible with Android 24–36), using Jetpack Compose for UI. Divided into three layers: UI, business logic, and data—fetching real stock data via Alpha Vantage (historical prices) and Finhub (stock info/news). Multiple panels implemented via Android activities with default/recommended sizes, plus responsive resizing that auto-adjusts layout. Tested on Meta Quest 3S using Meta Quest Developer Hub. Future versions will migrate data logic to our own backend. Challenges we ran into The challenge we ran into was designing specifically for VR, which we found very important and thus spent a lot of time on. Balancing information density with VR comfort was tough—traditional finance tools compress too much text and data, which doesn't translate well to a headset. It took several iterations to perfect panel sizing, text scale, and contrast for readability without overwhelming users, while also resisting feature creep to stay disciplined for a true P0 release. Accomplishments that we're proud of The result is a minimal yet capable P0 app that feels “native” to VR rather than a flat app ported into 3D. The three‑panel layout already supports a meaningful daily workflow for monitoring a stock portfolio, and the design leaves clear room for future expansion. The app respects VR ergonomics and interaction patterns while still feeling like a professional‑grade finance tool. What we learned Designing for VR forced a rethinking of common finance UI patterns: typography, spacing, and hierarchy all need to be more generous, and interactions must work equally well with hands and controllers. It also highlighted how powerful spatial memory can be—users quickly associate specific information with specific positions in their virtual workspace, which is a strong advantage over traditional setups. What's next for MarketView VR The next planned release will add portfolio filters (such as top movers and worst performers) and additional chart types, including candlestick, bar, and comparison views. Future iterations will introduce historical performance tracking based on purchase price and quantity, plus a voice‑driven AI assistant so users can ask questions like “What caused this drop in June?” while looking at a chart. Over time, the goal is for MarketView VR to grow from a focused research tool into a full spatial “Bloomberg of VR” for individual investors. <div