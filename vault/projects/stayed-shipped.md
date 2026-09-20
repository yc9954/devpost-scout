---
slug: "stayed-shipped"
url: "https://devpost.com/software/stayed-shipped"
title: "Stayed Shipped"
hackathon: "GitLab Transcend Hackathon"
organization: "GitLab"
winner: true
words: 790
team_size: 1
has_repo: false
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/graph_reasoning"
  - "domain/finance_payments"
  - "substrate/financial_record"
  - "substrate/sensor_telemetry"
---

# Stayed Shipped

> The survival ledger for AI-authored code. Everyone measures whether a change is risky before it merges; Stayed Shipped measures whether it survived after.

[Devpost](https://devpost.com/software/stayed-shipped) · hackathon [[GitLab Transcend Hackathon]]

## Facets

**mechanism** [[graph_reasoning]]
**domain** [[finance_payments]]
**substrate** [[financial_record]] [[sensor_telemetry]]
  <sub>weak: code_repository, structured_db</sub>

**stack** orbit

## Body

Inspiration Engineering orgs can measure AI spend to the cent and cannot measure what it produced. "Merged" is the metric everyone reaches for, and it is the wrong one: a change reverted four days later counted as productivity twice, once when the agent shipped it and once when a human cleaned it up. The moment code generation became nearly free, throughput and token invoices stopped being value signals. The question that actually decides how much autonomy you give an agent is simpler, and almost nobody has the number written down: did the change ship, and did it stay shipped? Browse this hackathon's own AI Catalog and the pattern is clear: the field is full of excellent pre-merge tools (blast-radius analyzers, risk scorers, impact predictors). Stayed Shipped is the other half of the loop. What it does For every merged MR, Stayed Shipped runs a survival window through the GitLab Orbit knowledge graph and produces a per-change verdict: A verification ladder declared honestly per repo: deploy-verified (Orbit's precomputed first_deployed_to_production_at ) or, as an explicit fallback, merge-verified. It never dresses a merge-verified result up as a deployed one. Tiered failure evidence, precision over recall: Class A revert detection via parsed reference and SHA lineage (counted), Class B bug or incident path-overlap (counted only after confirmation, always flagged incomplete coverage), Class C same-file churn (advisory, never counted). Cohort accounting no other entry does: every metric split across ai-authored, ai-assisted, and human, so verified share and review tax are reported per cohort. This is the autonomy question made measurable. Actions, not a dashboard: verdict labels as windows close, evidence-chain work items, a recurring digest issue, an author contestation loop ( cpvo::contested ), and a cleanup-contributions surface that credits the repairer rather than only flagging the original author. It ships as a GitLab Duo custom agent plus a flow published to the AI Catalog, and a stdlib-only Python reference engine. How we built it The engine is pure Python standard library, no third-party runtime dependencies, reading Orbit through query_graph and get_graph_schema . The Duo flow runs the same methodology against its own project's knowledge graph and performs the actions (labels, evidence issues, digest). Spend is an adapter input by design, so outcome verification works before a single token rate is configured. It implements CPVO (cost per verified outcome), a framework published before this hackathon with its own reference engine; the audit round-trips through that engine and the round-trip is covered by tests. Why Orbit is load-bearing Survival accounting needs merge requests, deployments, environments, work items, users, and pipelines joined in one place. Orbit's precomputed MR analytics columns and its AUTHORED / DEPLOYED_TO / CLOSES edges replace what would otherwise be five separate API integrations and a database. The outcome side of the ledger is computable in one query surface, which is what makes per-change survival verification feasible at all. Live results (honestly bounded) On a live Orbit-indexed repository, over 128 merged MRs, the cohort split came out at 26 ai-assisted MRs at 92.3 percent verified versus 102 human MRs at 99.0 percent, merge-verified. Small ai-assisted sample, one repo, merge-verified rather than deploy-verified: this demonstrates the differential is measurable, not a claim about AI code quality in general. That distinction is the product. Honest by design Stayed Shipped is a one-sided alarm. Failure detection is precision-over-recall, so a high verified share is only an upper bound, never a health grade, and the report says so. A low share is an adjudicable finding with a clickable evidence chain behind it. When an author disputes a verdict, they label the MR and the next audit demotes that evidence to advisory and logs it for human review. The tool measures changes, it does not grade people. Challenges we ran into The deployed flow is a prompt re-implementation, not the CLI, and a live run surfaced real divergences we fixed: it first collapsed a population audit to a single MR, hallucinated the run date, and could not reach Orbit for a cross-namespace project. The fixes: mentions always run a population audit, the run date must be supplied not inferred, and the flow audits its own Orbit-indexed project so reads and writes stay contained. Accomplishments we're proud of A mention-triggered flow that queries Orbit, returns correct survival verdicts with Class A evidence chains, applies cpvo::verified and cpvo::failed::reverted labels, and files a digest issue, all on a real indexed project, with every claim auditable. What we learned "Merged" hides reverts. Outcome verification needs a graph that joins MRs, deployments, work items, and users in one place, which is exactly what Orbit is. What's next Deploy-verified runs on a deployment-rich namespace, a larger ai-authored sample, and the spend adapter wired to real token rates to close the loop from outcome to cost. <div