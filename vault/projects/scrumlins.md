---
slug: "scrumlins"
url: "https://devpost.com/software/scrumlins"
title: "Scrumlins"
hackathon: "Meta Horizon Creator Competition: Mobile Genre Showdown - Reloaded"
organization: "Meta"
winner: true
words: 369
team_size: 1
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "domain/developer_tools"
  - "domain/supply_logistics"
  - "user/developer"
---

# Scrumlins

> Hatch your Scrumlin. Earn Glowstones. Furnish your island home… and prepare to face the Lava Golem!

[Devpost](https://devpost.com/software/scrumlins) · hackathon [[Meta Horizon Creator Competition- Mobile Genre Showdown - Reloaded]]

## Facets

**domain** [[developer_tools]] [[supply_logistics]]
**user** [[developer]]

**stack** copilot, genai, github, metahorizonsdesktopeditor, typescript, vscode

## How they structured the write-up

- inspiration
- what it does
- how i built it
- challenges & next steps

## Body

Scrumlins Welcome Lava Golem Titan (Coming next update) Inspiration Scrumlins was born from the idea of combining the charm of pet simulators with the creativity of fantasy creatures, all inside a fully interactive Horizon World. After being accepted into the Meta Horizon Creator Program on September 23, 2025 , through the expedited process, I set out as a brand-new developer to create something ambitious in just one month. My goal: build a world that feels alive, social, and rewarding. What it does Players can: Adopt eggs from the Adoption Center and hatch their own Scrumlins. Feed and bond with them to earn Glowstones and Bonding Days . Use Glowstones to furnish and decorate their very own Tiki Hut , unlocking new furniture as they progress. Explore and socialize in Co-Care Zones for community bonuses. Prepare for the upcoming Battle Arena , where they’ll face the mighty Lava Golem and his molten minions once the feature launches. The growth and evolution phase is still in development, designed to expand the adopt → feed → grow loop in future updates. To model player progression, the Glowstone growth curve follows the formula \( G(t) = \alpha t^2 + \beta t + \gamma \), where ( G(t) ) represents Glowstones earned over time, showing how consistency and care accelerate player progress. How I built it Engine: Meta Horizon Worlds Language: TypeScript via the Horizon Core API ( horizon/core , horizon/ui ) AI Tools: GitHub Copilot (GPT-5), ChatGPT, and GenAI for asset creation Core Systems: GameState.ts , InventoryManager.ts , ShopGlowstoneManager.ts , HutManager.ts , HutFurnishingManager.ts , FurnitureTag.ts , UIRouter.ts , HUD.ts , ShopIconToggle.ts , CoralShopUI.ts , CoralInventoryUI.ts , HutClaimTrigger.ts , HutIntroManager.ts , GlowstoneServer.ts , GlowstoneCurrencyBridge.ts , DailyWheelManager.ts , FeedUI.ts , and AdoptionController.ts . Built solo , leveraging AI for debugging, scripting speed, and creative asset generation. Challenges & Next Steps Balancing mobile performance, maintaining multiplayer GameState isolation, and synchronizing complex UI systems were major hurdles. Gameplay is best on mobile, but will be available for a better web and VR experience in the next update. Next, I’ll finalize creature evolution, expand furnishing options, and launch the Lava Golem Battle Arena. Scrumlins proves that one creator, powered by AI and persistence, can build something extraordinary. <div