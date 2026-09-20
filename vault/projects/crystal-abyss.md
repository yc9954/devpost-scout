---
slug: "crystal-abyss"
url: "https://devpost.com/software/crystal-abyss"
title: "Crystal Abyss"
hackathon: "RevenueCat Shipaton 2025"
organization: "RevenueCat"
winner: true
words: 1055
team_size: 2
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "domain/developer_tools"
  - "domain/labor_employment"
  - "user/developer"
  - "user/educator_student"
  - "substrate/code_repository"
---

# Crystal Abyss

> Monument Valley meets Columns: drop mystical crystals through Dante's circles. Meditative puzzle game with elegant animations. Live on iPhone App Store.

[Devpost](https://devpost.com/software/crystal-abyss) · hackathon [[RevenueCat Shipaton 2025]]

## Facets

**domain** [[developer_tools]] [[labor_employment]]
**user** [[developer]] [[educator_student]]
**substrate** [[code_repository]]

**stack** sprite-kit, swift

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for crystal abyss

## Body

Main menu Level 1: Limbo Level 4: Greed Level 5: Wrath Level 6: Heresy Level 9: Treachery Inspiration I spent countless hours playing Columns on the Sega Genesis/MegaDrive. There was something magical about the simplicity of matching colored jewels combined with the escalating challenge as the game sped up. Years later, I wanted to recreate that nostalgic experience but with a modern, minimalist aesthetic inspired by games like Monument Valley , this is not yet achieved but we're working on it. I also wanted to add narrative depth to elevate the experience beyond a simple arcade port. Crystal Abyss draws inspiration from Dante's Divine Comedy , with players descending through the Nine Circles of Hell. Each level represents a different circle, with increasing difficulty and unique visual themes that capture the atmosphere of Dante's underworld – from the eerie calm of Limbo to the intense chaos of Treachery. What it does Crystal Abyss is an iOS puzzle game where players: Drop stacks of 3 colored jewels into a 6x13 grid Match 3 or more same-colored jewels horizontally, vertically, or diagonally Clear matches to score points and prevent the grid from filling up Progress through 9 levels inspired by Dante's circles, each with increasing difficulty Experience sequential match clearing with satisfying cascade animations and particle effects Enjoy Monument Valley-inspired visual polish with elegant animations and minimalist design Learn the game through an interactive tutorial system Pro users can choose the starting level The game combines meditative puzzle mechanics with atmospheric level progression, creating a serene yet challenging experience. How we built it This project became possible thanks to AI-powered development . I've wanted to build an app for years, but compaginating it with my employment and family always felt overwhelming. With Claude and Codex , I could finally make it happen without dedicating months of full-time work. The entire project was "vibecoded" – I would describe what I wanted, and the AI would generate the code. We iterated rapidly, building: Core Technology: SpriteKit for game rendering, physics, and animations SwiftUI for UI, menus, and cross-platform layouts Custom Manager architecture (GridManager, JewelManager, SoundManager, LayoutManager) for clean separation of concerns RevenueCat for monetization and premium level unlocking Key Features Built: Sequential match clearing with cascade detection Particle effects system for visual feedback Tutorial system with step-by-step guidance Dynamic difficulty scaling across 9 themed levels The Human Touch: Not everything was AI-generated: Music composition : Hand-crafted ambient soundtracks for each circle Some visual assets : Custom-designed elements requiring artistic vision Narrative design : Dante-inspired theming and progression Design collaboration : José joined to provide professional UX expertise (still implementing his improvements) Challenges we ran into The biggest challenge was debugging visual inconsistencies . SpriteKit's coordinate system (center-origin with Y-axis pointing up) continuously confused the AI: Major Technical Challenges: Jewels landing in incorrect positions due to coordinate transformation bugs between scene space and grid space Inconsistent jewel sizing – the same jewel type appearing in different sizes within the same game, requiring tracking down 8+ conflicting setScale() calls Clipping masks breaking collision detection because of parent-child coordinate system conflicts – we eventually had to abandon this approach entirely Animation scaling conflicts causing jewels to grow or shrink unexpectedly during cascades AI getting confused and going in circles, fixing one bug while introducing another Each fix would sometimes introduce new regressions as the AI struggled to maintain consistent mental models of coordinate transformations. Some bugs took days to solve through iterative debugging. The Solution: Extensive logging systems to track every scale and position change Clear documentation in CLAUDE.md to maintain context across AI sessions Breaking down problems into isolated, testable pieces Critical discoveries documented to prevent repeating mistakes Architectural rules like "AVOID DUPLICATION AT ALL COSTS" enforced in the codebase Accomplishments that we're proud of Visual elegance – Achieved the Monument Valley aesthetic we were aiming for, with smooth animations, particle effects, and satisfying match clearing Clean architecture – Evolved from a monolithic 760-line GameScene to a well-organized manager-based system entirely through AI collaboration Performance optimization – Removed debug logging, optimized rendering, and achieved smooth 60fps gameplay Narrative depth – Successfully integrated Dante's Divine Comedy theme into a classic arcade game format RevenueCat integration – Implemented freemium model seamlessly across all platforms in under an hour AI-powered velocity – Built in weeks what would have traditionally taken months, proving solo developers can create ambitious projects with AI assistance What we learned AI is an incredible accelerator – but requires "senior developer" oversight with clear requirements and debugging strategies Documentation is critical – CLAUDE.md with project context, architectural decisions, and known issues prevented the AI from repeating mistakes or losing context across sessions Iterative debugging works – even when AI creates circular bugs, persistent iteration with detailed logging eventually solves complex problems Clear constraints help AI – explicit rules about code duplication, dead code removal, and architectural patterns dramatically improved code quality AI struggles with spatial reasoning – coordinate transformations, visual positioning, and animation scaling required the most human intervention The "vibe" matters – having a clear aesthetic vision (Monument Valley minimalism + Dante's darkness) guided thousands of micro-decisions throughout development Proper tooling enables iteration – LogManager that disables debug logs in production, centralized design systems, and clean architecture made rapid changes safe What's next for Crystal Abyss We're continuing to refine the visual polish and expand the experience: Visual Enhancements: Monument Valley-inspired scrolling backgrounds that move as you descend through the circles Enhanced particle effects for level transitions and special moments Implementing José's design improvements around layout, typography, and visual hierarchy Gameplay Features: Enhanced match sound system with layered audio for cascades and multi-color matches Sequential piece drop animations for more telegraphed gameplay and better reaction time Additional special effects for combo chains and high-score moments Polish & Expansion: Bug fixes for remaining edge cases (rotation near landing, pause/resume collision detection) Additional levels beyond the nine circles Leaderboards and achievements for competitive play Potential multiplayer modes exploring competitive or cooperative puzzle mechanics The AI-powered development workflow has been so effective that features that would have taken weeks now take hours. We can experiment freely, iterate rapidly, and focus on the creative vision rather than implementation details. Crystal Abyss proves that with the right tools, vision, and AI collaboration, solo developers can create polished, cross-platform experiences that once required entire teams. <div