---
slug: "eslint-plugin-baseline-js"
url: "https://devpost.com/software/eslint-plugin-baseline-js"
title: "eslint-plugin-baseline-js"
hackathon: "Baseline Tooling Hackathon"
organization: "Google"
winner: true
words: 531
team_size: 0
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "domain/developer_tools"
  - "domain/finance_payments"
  - "user/developer"
  - "substrate/code_repository"
  - "substrate/web_dom"
---

# eslint-plugin-baseline-js

> Make Baseline executable: one ESLint rule, powered by latest web‑features, that enforces availability by year and type‑aware API usage—single‑line setup, IDE/CI ready.

[Devpost](https://devpost.com/software/eslint-plugin-baseline-js) · hackathon [[Baseline Tooling Hackathon]]

## Facets

**domain** [[developer_tools]] [[finance_payments]]
**user** [[developer]]
**substrate** [[code_repository]] [[web_dom]]

**stack** eslint, javascript, node.js, typescript

## How they structured the write-up

- inspiration
- what it does
- accomplishments i'm proud of
- challenges i ran into
- what i learned
- what's next for eslint-plugin-baseline-js

## Body

GIF With VSCode Extensions GIF From CLI Inspiration During user interviews, I kept hearing the same frustration: existing static analysis tools can't reliably enforce JavaScript's Baseline browser support. This gap became impossible to ignore. While Baseline gives us a clear standard for browser compatibility, we lack the tools to enforce it where it matters most—in JavaScript, where most business logic lives. I realized that if we could bring the same consistency to JavaScript that developers enjoy with other web technologies, we'd not only improve DX but also prevent the silent user exclusion that happens when features break in older browsers. My goal was simple: make those invisible compatibility risks visible, and give teams the power to prevent user loss before code ships. Because at the end of the day, every unsupported JavaScript feature is a potential customer we're turning away. What It Does An ESLint plugin that instantly shows whether your code will work in the target environment, right in your editor and CI pipeline. One policy knob: Baseline as widely , newly , or a year (YYYY) . Regardless of detection method, the rule reports a single, unified Baseline message. When TypeScript is available, a type aware mode increases precision. Accomplishments I'm Proud Of High Developer Experience with a Single Rule Approach A single rule ( baseline-js/use-baseline ) enforces Baseline. Messages always follow one format (feature name + identifier + year/limited), minimizing learning cost. Both ignoreFeatures and ignoreNodeTypes accept strings or regular expressions, enabling teams to shape a pragmatic "house Baseline" without clutter. Orchestrated Detection The plugin reuses proven rules from eslint-plugin-es-x and ESLint core, filling gaps with focused internal rules. Typed, Data Driven Detection Type aware mode checks instance members (Element/Response/etc.) with the TypeScript TypeChecker to confirm property existence. When types aren't available, the plugin automatically disables instanceMember to avoid false positives. With Abstract Syntax Tree alone, foo.animate() could be either Element#animate() or a user defined method. Type aware mode (using @typescript-eslint/parser + project config) consumes parserServices and asks the TypeScript Checker for the receiver's interface before reporting. Support for web-features v3 Challenges I Ran Into Drawing the Right Line for Coverage HTML/CSS/environment driven semantics were scoped out to focus on JavaScript language/builtins/Web Application Programming Interfaces. The coverage generator explains exclusions with short memos, keeping the table trustworthy and reviews unambiguous. What I Learned Defining clear scope "what belongs in this tool and what stays out" turns coverage into a strategic signal. This approach prevents confusion and over investment. Including HTML/CSS could have created a single umbrella "Baseline" tool, but respecting community tooling and shipping a great JavaScript experience first proved more valuable. A narrowly scoped, high precision tool delivers more value to developers—and ultimately to end users—than a broad, fuzzy one. What's Next for eslint-plugin-baseline-js More Human and AI Friendly Errors Exploring low risk alternatives, adding source links, and surfacing a small "potential user impact" estimate in messages to speed up reviews. Feedback Driven Precision Partnering with early adopters to reduce false positives and false negatives, enhance descriptor coverage, and measure performance on large codebases. A Cohesive Baseline Experience Collaborating with HTML/CSS Baseline linting to deliver an end to end, consistent Baseline first accessibility/config and reliability story. <div