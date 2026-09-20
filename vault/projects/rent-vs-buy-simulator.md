---
slug: "rent-vs-buy-simulator"
url: "https://devpost.com/software/rent-vs-buy-simulator"
title: "Rent vs. Buy Simulator"
hackathon: "Hackonomics 2026"
organization: "hackonomics"
winner: true
words: 476
team_size: 1
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/simulation_digital_twin"
  - "domain/accessibility"
  - "domain/education"
  - "domain/finance_payments"
  - "domain/housing_homeless"
  - "substrate/structured_db"
  - "substrate/web_dom"
---

# Rent vs. Buy Simulator

> A fully accessible financial simulation. This app helps users determine the true opportunity cost of renting versus buying a home by calculating compound interest etc... over a customizable timeline.

[Devpost](https://devpost.com/software/rent-vs-buy-simulator) · hackathon [[Hackonomics 2026]]

## Facets

**mechanism** [[simulation_digital_twin]]
**domain** [[accessibility]] [[education]] [[finance_payments]] [[housing_homeless]]
**substrate** [[structured_db]] [[web_dom]]

**stack** css3, html5, javascript

## How they structured the write-up

- elevator pitch
- inspiration
- what it does
- how i built it
- challenges i ran into
- accomplishments i’m proud of
- what i learned
- what’s next

## Body

Rent vs. Buy Simulator Elevator Pitch I built a fully accessible, multi‑theme financial simulator that reveals the true opportunity cost of renting versus buying. My goal was to make financial literacy intuitive, beautiful, and welcoming — not intimidating. Inspiration Most mortgage calculators and financial tools today suffer from two big problems: They overwhelm beginners with cluttered UI and jargon They ignore basic accessibility standards When young adults try to make one of the biggest financial decisions of their lives, they’re met with interfaces that feel more like spreadsheets than guidance. I wanted to create the opposite — something that feels like an editorial notebook: calm, clean, and educational. A tool that proves financial literacy can be rigorous and aesthetically pleasing. What It Does My simulator projects a user’s net worth over a timeline of up to 50 years by comparing two scenarios side‑by‑side: Buying a Home Mortgage amortization Property taxes Maintenance costs Home appreciation Renting + Investing Rent inflation Investing the difference Stock market returns The simulator then calculates the opportunity cost and visualizes which strategy leads to higher long‑term net worth. I also included an educational section that breaks down six core economic concepts: Opportunity Cost Sunk Costs Compound Interest Liquidity Inflation Hedges The Mobility Premium How I Built It I built the entire project using HTML5, CSS3, and Vanilla JavaScript to keep it lightweight and fast. Design & Themes I created a CSS‑variables theme system with four modes: Editorial Minimal (default, low‑saturation, calm) Dreamy Y2K Dark Mode Colorblind‑Safe Mode Interactions I used GSAP for smooth number‑counting animations. Accessibility Accessibility was a top priority. The app: Is fully keyboard‑navigable Uses semantic HTML Includes ARIA live regions that announce results without overwhelming screen readers To prevent screen readers from reading every intermediate animation number, I separated the visual animation from the accessible output and added a debounce so only the final result is announced. Challenges I Ran Into The hardest part was balancing animations with accessibility. GSAP updates caused screen readers to read every number during the animation, which was unusable. My solution: Hide animated numbers from screen readers Create a separate sr-only live region Debounce announcements so only the final value is spoken This kept the UI smooth without sacrificing accessibility. Accomplishments I’m Proud Of Achieving a polished, Awwwards‑style UI using only Vanilla CSS and JS Implementing strict WCAG accessibility standards Making a financial tool that is genuinely inclusive for users with visual or motor impairments What I Learned I deepened my understanding of: ARIA live regions and how to use them responsibly Focus management in custom modals and settings menus Translating complex financial formulas (compound interest, amortization) into efficient JavaScript loops What’s Next My next step is backend integration. I plan to use Momen.app for user authentication so people can: Save their financial parameters Track projections over time Export personalized financial literacy reports <div