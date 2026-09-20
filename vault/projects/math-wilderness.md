---
slug: "math-wilderness"
url: "https://devpost.com/software/math-wilderness"
title: "Math Wilderness"
hackathon: "DeveloperWeek 2026 Hackathon"
organization: "DevNetwork"
winner: true
words: 736
team_size: 1
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/graph_reasoning"
  - "mechanism/realtime_stream"
  - "domain/developer_tools"
  - "domain/education"
  - "user/developer"
  - "user/educator_student"
  - "substrate/document_pdf"
  - "substrate/geospatial"
---

# Math Wilderness

> Math Wilderness is an adaptive math learning platform where structured content relationships power personalized difficulty, unlocking concepts dynamically as learners progress.

[Devpost](https://devpost.com/software/math-wilderness) · hackathon [[DeveloperWeek 2026 Hackathon]]

## Facets

**mechanism** [[graph_reasoning]] [[realtime_stream]]
**domain** [[developer_tools]] [[education]]
**user** [[developer]] [[educator_student]]
**substrate** [[document_pdf]] [[geospatial]]
  <sub>weak: web_dom</sub>

**stack** css, html, javascript, sanity, typescript

## How they structured the write-up

- math wilderness
- the idea
- the core concept
- the content architecture
- the adaptive loop
- development approach
- why this matters
- what makes it strong
- the vision

## Body

Math Wilderness Adaptive learning powered by structured content relationships The Idea Most adaptive learning platforms talk about personalization, but what they really do is sort problems into easy, medium, or hard buckets and adjust linearly. That is not true adaptation. Real personalization requires understanding relationships: Which concepts depend on other concepts Which problems test which skills Which misconceptions connect to which errors How a learner performs across specific skill areas Math Wilderness is built around that idea. Instead of hard coding logic, we treat relationships as structured content. The intelligence of the platform comes from how the content connects. The Core Concept Math Wilderness turns math learning into a structured knowledge map. Concepts are locations on a learning trail. Problems are challenges tied to specific skills. Learners progress by mastering connected ideas rather than moving through a flat list. Every piece of content knows how it relates to other content. That structure allows the system to adapt dynamically without changing application code. The Content Architecture We built five core document types in Sanity, all connected through references. Concepts Concepts are the foundation. Each concept stores a list of prerequisite references. When a learner masters a concept, the system checks whether all prerequisites for the next concept are satisfied. If they are, that concept becomes available. No manual unlock logic. No redeployment. If you change prerequisites in Sanity Studio, the learning path updates instantly. This turns the curriculum into a live knowledge graph. Problems Problems do not have a fixed difficulty label. Instead, each problem stores a concept breakdown. This is an array of concept references with weights. Each weight represents how much that concept contributes to the problem’s difficulty. For example: Algebra weight 0.7 Geometry weight 0.3 The problem’s effective difficulty is calculated relative to the learner’s rating in both areas. This allows for composite difficulty matching instead of static tags. Attempts Every time a learner submits an answer, an attempt document is created. It stores: Correctness Response time ELO rating adjustments Concept performance impact This attempt history drives the adaptive loop. Campers Campers are the learner profiles. Each camper stores: • Global ELO rating • Concept specific ELO ratings • Mastered concepts • Attempt history references The ELO rating system uses a decreasing K factor as attempts accumulate, which stabilizes ratings over time and reduces volatility. Mascots Mascots are structured content too. Their dialogue and encouragement messages are editable in Sanity Studio. This shows how even narrative elements benefit from structured content. Non developers can adjust tone and messaging without touching code. The Adaptive Loop When a learner requests a problem: The system fetches their current concept and rating A GROQ query finds problems within a target rating range Previously mastered problems are excluded The closest difficulty match is selected The learner receives an optimally challenging problem After submission: Expected score is calculated ELO updates are applied to both camper and problem Concept mastery thresholds are evaluated Newly unlocked concepts become available automatically All of this is driven by content relationships and queries. Not hard coded curriculum logic. Development Approach Math Wilderness was built on Sanity using the MCP server for AI assisted development. We used AI to: Generate complex schemas with correct reference validation Populate sample data with structured concept breakdowns Write and refine multi level GROQ queries Iterate on ELO logic through rapid experimentation AI accelerated development. Structured content made the system powerful. The frontend is deployed on Vercel with real time updates from Sanity, creating a production ready adaptive learning experience. Why This Matters This project shows that intelligence does not only come from machine learning models. It can come from structure. By designing content with intentional relationships, we created a system where: Changing prerequisites updates learning paths instantly Difficulty adapts per concept, not globally Misconceptions can be targeted precisely Non developers can modify curriculum safely This is scalable, maintainable, and extensible. Add a new subject. Add new concepts. The system adapts automatically. What Makes It Strong Real world use case in adaptive education Clean, normalized schema design Structured references powering runtime intelligence AI assisted development through MCP Production deployment with live updates Extensible foundation for AI generated problems, spaced repetition, and social learning The Vision Math Wilderness is not just a math app. It is a demonstration that structured content can power adaptive systems. When content understands its relationships, the platform becomes intelligent by design. That is the real innovation. <div