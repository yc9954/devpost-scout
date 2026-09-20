---
slug: "typomaster"
url: "https://devpost.com/software/typomaster"
title: "TypoMaster"
hackathon: "Code with Kiro Hackathon"
organization: "Kiro"
winner: true
words: 722
team_size: 1
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/cross_origin_web"
  - "mechanism/realtime_stream"
  - "domain/accessibility"
  - "domain/developer_tools"
  - "domain/labor_employment"
  - "domain/supply_logistics"
  - "user/developer"
  - "substrate/code_repository"
  - "substrate/sensor_telemetry"
  - "substrate/web_dom"
---

# TypoMaster

> Why practice with 'The quick brown fox' when you can practice with content you actually want to read?

[Devpost](https://devpost.com/software/typomaster) · hackathon [[Code with Kiro Hackathon]]

## Facets

**mechanism** [[cross_origin_web]] [[realtime_stream]]
**domain** [[accessibility]] [[developer_tools]] [[labor_employment]] [[supply_logistics]]
**user** [[developer]]
**substrate** [[code_repository]] [[sensor_telemetry]] [[web_dom]]

**stack** css3, html5, javascript, kiro

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for typomaster

## Body

TestingApp Inspiration I was frustrated with traditional typing practice tools that used boring, repetitive text like "The quick brown fox jumps over the lazy dog." Meanwhile, I spent hours reading interesting content online - news articles, technical blogs, Wikipedia pages - but none of that time was helping me improve my typing skills. I wanted to build a browser extension that could transform any webpage into typing practice, but I had limited experience with browser extension development. The complexity of Manifest V3, content script injection, and cross-browser compatibility seemed daunting for a solo developer. What it does TypoMaster transforms any webpage into an interactive typing practice session while preserving the original formatting and layout. Users can select any text on a webpage and start typing over it with real-time feedback. The extension provides comprehensive metrics including WPM and accuracy tracking, a floating hints panel with keyboard shortcuts, and settings persistence across browser sessions. It maintains full accessibility compliance with keyboard navigation and screen reader support, working seamlessly across Chrome, Firefox, and Edge browsers. How we built it Kiro helped me structure my vague idea into concrete specifications through a spec-driven development approach. Instead of jumping straight into coding, we started by analyzing requirements and breaking down user stories with clear acceptance criteria. Kiro guided me through creating detailed documentation in the .kiro/specs/ folder, defining clear interfaces between components, and planning the development workflow systematically. Once specifications were solid, Kiro's agents generated the core extension architecture. The AI handled the complex Manifest V3 configuration with proper permissions and service worker setup, created the content script system for webpage injection and DOM manipulation, and built the typing interface components with a non-destructive text overlay system. Throughout three development phases, Kiro helped build the fundamental text selection system, implement comprehensive metrics calculation, and ensure full accessibility compliance with over 90 test cases. Challenges we ran into Working with Kiro, we solved several complex technical challenges. The non-destructive DOM manipulation required creating an overlay system that wouldn't break existing webpage layouts. Format preservation meant maintaining bold, italic, and link styling during the typing process. Cross-browser compatibility demanded consistent behavior across different browser engines. Performance optimization ensured minimal impact on webpage loading times while maintaining smooth real-time updates. Accessibility compliance required full keyboard and screen reader support throughout the entire user experience without feeling like an afterthought. Accomplishments that we're proud of The entire development cycle took just two weeks from concept to production-ready extension using Kiro's spec-driven approach. We achieved complete feature implementation with all requirements met and comprehensive testing coverage. The extension reached production-ready quality with robust error handling and cross-browser support. Full accessibility compliance means the extension works seamlessly for users with disabilities through keyboard navigation and screen reader support. The maintainable codebase features clean architecture with clear separation of concerns and comprehensive documentation. What we learned Working with Kiro taught me the value of spec-driven development and starting with clear requirements before writing any code. I gained deep understanding of browser extension architecture, particularly Manifest V3 and content scripts. The project reinforced accessibility best practices and showed me how to build truly inclusive web applications. I learned comprehensive testing strategies for complex user interactions and discovered how AI-assisted development can significantly accelerate both learning and delivery while maintaining high standards for code quality. Kiro excelled at explaining complex browser APIs in understandable terms, generating clean and maintainable code architecture, creating comprehensive test suites automatically, and ensuring accessibility compliance from the project's inception. However, creative problem-solving for unique UX challenges required human insight, fine-tuning user experience needed human aesthetic judgment, and debugging edge cases in different browser environments often required human intuition and experience. What's next for TypoMaster The extension architecture supports future enhancements including advanced metrics with detailed typing analytics and progress tracking over time. We plan to add customization options with user-defined difficulty levels and practice modes tailored to individual needs. Social features like leaderboards and typing challenges could create a community around skill improvement. Content filtering capabilities would enable smart text selection based on difficulty level or topic interest, making practice sessions even more targeted and effective. This project demonstrates how AI-assisted development can create a partnership between human creativity and AI efficiency, producing results that neither could achieve alone in the same timeframe while maintaining accessibility and quality standards. <div