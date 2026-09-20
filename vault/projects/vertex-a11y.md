---
slug: "vertex-a11y"
url: "https://devpost.com/software/vertex-a11y"
title: "Vertex A11y"
hackathon: "HackGT 12: Midnight at the Museum"
organization: "HexLabs"
winner: true
words: 886
team_size: 4
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/cross_origin_web"
  - "mechanism/realtime_stream"
  - "domain/accessibility"
  - "domain/developer_tools"
  - "domain/supply_logistics"
  - "user/developer"
  - "substrate/video_visual"
  - "substrate/web_dom"
---

# Vertex A11y

> Vertex A11y empowers developers to champion accessibility, offering real-time insights and practical solutions that transform websites into experiences everyone can use.

[Devpost](https://devpost.com/software/vertex-a11y) · hackathon [[HackGT 12- Midnight at the Museum]]

## Facets

**mechanism** [[cross_origin_web]] [[realtime_stream]]
**domain** [[accessibility]] [[developer_tools]] [[supply_logistics]]
**user** [[developer]]
**substrate** [[video_visual]] [[web_dom]]

**stack** chrome, css, html, javascript, json, motion, node.js, openai

## How they structured the write-up

- key features
- benefits
- technologies used

## Body

Vortex A11y Highlight Feature Vortex A11y AI Recommendation Feature Pre-Scan Vortex A11y Extension Pre-Scan Vortex A11y Extension Inspiration Over 216 million people suffer from a form of visual impairment around the world. While assistive technologies continue to advance each year, web development has comparatively been stagnant. A study done by WebAIM found that over 96% of the top million websites did not comply to disability guidelines such as those under the American Disability Act (ADA) and the Web Content Accessibility Guidelines (WCAG) that aimed to make websites more accessible for the visually and auditorily impaired. As developers, we understand that accessibility may be an afterthought in comparison the more important or daunting task of designing a website. Our Chrome extension, Vortex A11y , focuses on remedying this problem by making accessibility more accessible for developers. What it does Vertex A11y is a Chrome extension that helps developers build more accessible websites by providing real-time, actionable insights on accessibility issues. It scans web pages for compliance with ADA and WCAG 2.1 standards and highlights problematic elements directly in the browser. Key Features Automated accessibility checks for images, color contrast, keyboard navigation, forms, semantic HTML, media captions, and heading structure Visual highlighting of violations on the page Actionable code suggestions to fix issues immediately Compliance scoring with tiered ratings (A, AA, AAA) Developer-friendly workflow : instant feedback, filtering, sorting, and contextual learning for each violation Modern interface : smooth animations, responsive design, and dark theme optimized for developer use Benefits Accelerates accessibility adoption Reduces post-deployment fixes Empowers developers to create inclusive web experiences for all users How we built it Vertex A11y was developed using Vanilla JavaScript to create lightweight, fast content scripts without framework dependencies, and Motion.js to provide smooth animations and interactive feedback in the user interface. The extension performs accessibility checks across seven core categories: images, color contrast, keyboard navigation, forms, semantic HTML, media, viewport, and heading structure. For development and deployment, we used ESBuild to bundle scripts to bypass the restrictions due to Manifest v3. By combining real-time scanning, visual feedback, and educational guidance, Vertex A11y helps developers integrate accessibility into their workflow from the very start of the development process. Technologies Used Category Technologies / Tools Purpose / Description Frontend Vanilla JavaScript Lightweight content scripts without framework dependencies Motion.js Smooth animations and micro-interactions in the popup UI Build & Development ESBuild Fast bundling and build optimization Accessibility Testing ADA & WCAG 2.1 Guidelines Level A, AA, AAA rating evaluation Color contrast algorithms WCAG-compliant luminance calculations Semantic HTML validation Checks for proper landmark usage and heading structure Images Alt text presence and quality Color Contrast WCAG AA/AAA compliance (4.5:1 / 7:1 ratios) Keyboard Navigation Focusable interactive elements Forms Label associations and accessibility Media Video caption requirements Viewport Zoom and scaling configuration Heading Structure Logical heading hierarchy Challenges we ran into OpenAI API Integration : Requests were misrouted to the web app instead of the API, requiring debugging and restructuring of calls. Manifest V3 Limitations : Inline scripts were disallowed, so we reworked Motion.js animations to run entirely through content scripts and the popup. Backend–Frontend Integration : Merging the scanner, AI explanations, and UI demanded careful message passing and modular design to keep the extension fast and reliable. Accomplishments that we're proud of Successful OpenAI API Integration : We’re proud of getting the OpenAI API working seamlessly within the extension to provide contextual explanations and code-level fix recommendations. Smooth Frontend Animations : Using Motion.js, we built an intuitive and modern interface with responsive animations that make the developer experience more engaging. Real-Time Issue Highlighting : One of our favorite features is the ability to visually highlight accessibility issues directly on a live webpage, giving developers instant clarity on what needs attention. What we learned TailwindCSS : Early in the project we experimented with TailwindCSS while building the foundations and saw how powerful utility-first styling can be for quickly prototyping UI. Motion Framework : We gained hands-on experience with Motion.js, learning how to build smooth, responsive animations that enhance usability while working within Manifest V3 limitations. OpenAI API : We learned how to properly integrate the OpenAI API into a Chrome extension, managing requests, debugging errors, and using it to generate contextual, developer-friendly explanations. CSS Mastery : We deepened our understanding of modern CSS, from custom properties to gradients and responsive layouts, refining the UI’s polish and accessibility. Better GenAI Prompting : We improved at crafting prompts that yield useful, actionable outputs from generative AI, which helped both the extension’s guidance system and our own development workflow. What's next for Vertex A11y We see Vertex A11y as just the beginning of a more comprehensive accessibility toolkit. Some of the future directions we’re excited about include: Support for Auditory Accessibility : Expanding beyond visual impairments to include checks and recommendations for users with hearing disabilities. Fixed Website Preview : Offering a preview mode that shows what a page would look like once accessibility issues are resolved. Pre-Deployment Assistant : Building an AI-powered coding assistant that helps developers write accessible code before their websites go live. Performance Dashboard : Creating a dashboard where developers and organizations can track their progress and performance in building accessible websites over time. Beyond Websites : Extending our platform to evaluate accessibility in other applications and digital products, not just web pages. <div