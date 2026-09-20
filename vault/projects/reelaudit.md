---
slug: "reelaudit"
url: "https://devpost.com/software/reelaudit"
title: "ReelAudit"
hackathon: "Amazon Nova AI Hackathon"
organization: "Amazon"
winner: true
words: 560
team_size: 3
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "domain/agriculture_food"
  - "substrate/geospatial"
---

# ReelAudit

> ReelAudit uses Amazon Nova to detect policy violations in videos, localize risky frames, suggest minimal edits, and help create market-safe versions for India, UAE, Germany, and more.

[Devpost](https://devpost.com/software/reelaudit) · hackathon [[Amazon Nova AI Hackathon]]

## Facets

**domain** [[agriculture_food]]
  <sub>weak: developer_tools</sub>
**substrate** [[geospatial]]

**stack** amazon-bedrock, amazon-nova, amazon-web-services, for, framer-motion, javascript, next.js, react, sdk, tailwind-css, typescript

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for reelaudit

## Body

thumbnail home Inspiration Global video compliance is still slow, manual, and expensive. A single ad or product video can be acceptable in one market but risky in another because of local rules around alcohol, safety, youth targeting, religious sensitivity, or misleading claims. We wanted to build a system that helps content teams detect those risks early, localize the exact moment in the video, and move toward minimal edits instead of cutting entire scenes. What it does ReelAudit uses Amazon Nova to analyze uploaded videos for market-specific compliance risks. It identifies risky timestamps, maps them to selected regions such as India, UAE, Germany, and the USA, and shows violations in a timeline-based review dashboard. The project also moves beyond detection. For each flagged moment, ReelAudit generates a remediation plan with a suggested edit strategy such as blur, mask, crop, disclaimer, replacement, or manual review. We also built a first auto-fix workflow that creates a market-safe draft preview for flagged segments so teams can review a safer version immediately. How we built it We built ReelAudit as a Next.js application with a landing page and a live compliance dashboard. Videos are uploaded to Amazon S3, and the backend sends them to Amazon Bedrock using Amazon Nova for multimodal video understanding. We created a market-rule layer that guides analysis for different jurisdictions and normalizes the model output into a structured compliance report. On top of the analysis layer, we added: a violation inbox with timestamps and confidence scores remediation plans focused on preserving scenes whenever possible chunk-planning logic for future long-form and hour-long video processing a browser-based auto-fix draft generator for fast review Challenges we ran into One of the biggest challenges was handling real video input reliably across model and payload constraints. We also had to separate what Amazon Nova does well, such as understanding and reasoning over video, from what needed to be built in our own pipeline, such as draft generation, scene-preserving edits, and export logic. Another challenge was designing for the real-world future state, where teams may upload videos in GBs and durations measured in hours, not just short demo clips. That required us to think about chunking, auditability, and scalable remediation from the beginning. Accomplishments that we're proud of We are proud that ReelAudit is not just a moderation demo. It is already structured around a real production problem: detect market-specific violations localize the exact moment in the video suggest the smallest compliant edit move toward market-safe versions without removing full scenes We are also proud that we built a live S3 + Amazon Nova flow and extended it with remediation-aware outputs and an initial auto-fix draft experience. What we learned We learned that solving compliance for video is not only an AI detection problem. It is a full pipeline problem involving understanding, localization, edit strategy, revalidation, and market-specific delivery. We also learned how to use Amazon Nova as the reasoning layer inside a larger system instead of treating it like a one-step solution. What's next for ReelAudit Our next steps are to: support long-form and hour-long videos using chunk-based processing improve object-level localization for more accurate blur and masking add stronger auto-fix workflows such as object blur, region masking, and market-specific exports re-run compliance after edits to verify that the new version passes local guidelines generate separate approved versions for different regions from one master video <div