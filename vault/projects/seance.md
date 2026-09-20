---
slug: "seance"
url: "https://devpost.com/software/seance"
title: "Seance"
hackathon: "Kiroween"
organization: "Kiro"
winner: true
words: 1268
team_size: 0
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/on_device_local"
  - "domain/accessibility"
  - "domain/developer_tools"
  - "domain/finance_payments"
  - "domain/retail_commerce"
  - "user/developer"
  - "user/small_business"
  - "substrate/code_repository"
  - "substrate/document_pdf"
  - "substrate/financial_record"
  - "substrate/geospatial"
  - "substrate/structured_db"
---

# Seance

> Explore the world's darkest legends

[Devpost](https://devpost.com/software/seance) · hackathon [[Kiroween]]

## Facets

**mechanism** [[on_device_local]]
**domain** [[accessibility]] [[developer_tools]] [[finance_payments]] [[retail_commerce]]
**user** [[developer]] [[small_business]]
**substrate** [[code_repository]] [[document_pdf]] [[financial_record]] [[geospatial]] [[structured_db]]

**stack** typescript

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for seance

## Body

kiro ide seance landing page choose a path book ui one wrong answer and the spirits yeet you back to the start book cover Building Seance: A Kiroween Hackathon Journey Inspiration When I discovered the Kiroween hackathon, I saw it as the perfect opportunity to test drive the Kiro IDE in a real-world project. I had been using other AI-powered IDEs, but Kiro's approach to specs and hooks intrigued me. The generous credit allocation for the hackathon certainly helped make the decision easier. I wanted to build something fun and seasonal that would let me explore Kiro's capabilities while creating an engaging educational experience around global folklore and dark history. What It Does Seance is an immersive web application that transforms learning about global folklore and history into an atmospheric, interactive experience. Users explore an interactive world map, selecting from 19 countries to uncover their dark tales through three thematic paths: People's Tales (folklore and myths), Crown's Secrets (political history), and Merchant's Ledger (economic history). The application features a realistic page-flipping book interface where users answer multiple-choice questions to progress through each country's stories. Wrong answers send you back to the beginning with a dramatic animation, while correct answers unlock new pages. The experience is enhanced with 3D smoke effects powered by Three.js, ambient sound design including owl hoots, wolf howls, and heartbeats, and a complete audio system with page-flip sound effects. How We Built It Technology Stack The project is built on Next.js 16 with React 19 and TypeScript, using Three.js and react-three/fiber for 3D graphics. The page-flipping mechanics use react-pageflip, while the world map is rendered with react-simple-maps. Styling is handled by Tailwind CSS 4, with Biome for linting and formatting. Development Process with Kiro The development process was significantly streamlined by Kiro's spec-driven workflow. I started by creating detailed requirements documents using the EARS pattern and INCOSE quality rules, which forced me to think through exactly what I wanted to build before writing any code. The specs acted like a clean, organized to-do list that kept development focused and prevented scope creep. Kiro's task system broke down the implementation into manageable chunks, with each task building incrementally on the previous one. This made it easy to track progress and ensure nothing was left hanging or unintegrated. The ability to mark certain tasks as optional (like comprehensive unit tests) allowed me to focus on core functionality first while maintaining the option to add polish later. Kiro Hooks One of the most valuable features was the hook system. I created a "Kiroween README Beautifier" hook that automatically enhanced the README whenever I modified it. This meant I could focus on building features while the documentation improved organically throughout the project. The hook added Halloween-themed badges, ASCII art, mermaid diagrams, and proper formatting without requiring manual effort. By the end of development, the README was polished and professional without taking time away from coding. Steering Rules Early in development, I noticed Kiro's agent was sometimes too eager to make changes without explicit permission. To address this, I created a code-policy steering rule that required explicit commands before any code modifications. This gave me complete control over when changes happened, transforming Kiro from an overly helpful assistant into a precise tool that only acted when directed. Challenges We Ran Into Audio Autoplay Restrictions Browser autoplay policies presented an interesting challenge. Audio wouldn't play until user interaction occurred, but by the time users navigated from the map to the book, that interaction was lost. The solution was to leverage the existing mute/unmute button as the audio unlock mechanism. When users unmute on the home page, it unlocks audio globally for the entire session, allowing page-flip sounds to work immediately when they reach the book interface. Page Progression Logic Implementing the quiz progression system required careful state management. Questions are distributed across book spreads with left and right pages, and users must answer correctly to unlock subsequent pages. The system needed to handle wrong answers by dramatically flipping back to the beginning while preserving the educational flow. This required coordinating the FlipBook component's imperative API with React's declarative state management. 3D Performance Balancing visual atmosphere with performance was crucial. The smoke effects needed to be dramatic without overwhelming slower devices. This required implementing WebGL detection with graceful CSS fallbacks, optimizing particle counts, and ensuring the effects enhanced rather than distracted from the core experience. Accomplishments That We're Proud Of Spec-Driven Development The spec workflow proved invaluable. Having clear requirements, detailed design documents, and organized task lists made development feel structured and professional rather than chaotic. Each phase built naturally on the previous one, and the final implementation closely matched the original vision. Immersive User Experience The combination of realistic page-flipping animations, atmospheric 3D smoke effects, ambient sound design, and educational content creates a genuinely engaging experience. The wrong-answer punishment of flipping back to the beginning adds stakes without being frustrating, and the progressive unlocking system maintains educational integrity. Clean Architecture The codebase follows clear separation of concerns with distinct data, presentation, and business logic layers. The question data is organized thematically across three files, components are reusable and well-encapsulated, and the global audio manager handles sound across the entire application elegantly. What We Learned Kiro IDE Capabilities Kiro represents what an AI-powered IDE should be. The spec system forces thoughtful planning before implementation, the task breakdown keeps development organized, and the hook system automates repetitive work. The steering rules provide fine-grained control over agent behavior, allowing developers to customize the experience to their workflow. Importance of Constraints The code-policy steering rule taught me that sometimes the best AI assistance is constrained AI assistance. By requiring explicit permission for changes, Kiro became more useful as a precise tool rather than an autonomous agent. This balance between automation and control is crucial for productive development. Educational Game Design Creating an educational experience that feels like entertainment requires careful balance. The quiz mechanics needed to be engaging without overshadowing the learning content. The atmospheric effects and sound design enhance immersion without becoming distracting. The progressive unlocking system maintains educational flow while adding game-like progression. What's Next for Seance Content Expansion The current implementation covers 19 countries with three thematic paths each. Future versions could expand to more countries, add additional paths, and include more questions per path. Community contributions could help build a comprehensive global folklore database. Enhanced Interactivity Additional features could include achievement systems for completing all paths in a country, leaderboards for high scores, and social sharing of completed paths. The book interface could support more complex question types beyond multiple choice, such as ordering events chronologically or matching terms to definitions. Accessibility Improvements While the current implementation includes basic keyboard navigation and screen reader support, future versions could enhance accessibility with high-contrast modes, adjustable text sizes, and more comprehensive keyboard shortcuts. The audio system could include visual indicators for users who prefer or require silent operation. Performance Optimization Further optimization could include lazy loading question data per country, implementing virtual scrolling for long question sets, and more aggressive code splitting. The 3D effects could adapt dynamically based on device capabilities, providing richer experiences on powerful hardware while maintaining smooth performance on modest devices. Seance demonstrates that educational content can be both informative and atmospheric, that AI-powered development tools can enhance rather than replace developer control, and that Halloween-themed hackathons are an excellent excuse to build something fun while learning new tools. The Kiro IDE proved to be exactly what I was looking for in an AI-powered development environment, and the Kiroween hackathon provided the perfect motivation to explore its capabilities. <div