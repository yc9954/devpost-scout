---
slug: "consentkey"
url: "https://devpost.com/software/consentkey"
title: "ConsentKey"
hackathon: "DevStudio 2026 by Logitech"
organization: "Logitech"
winner: true
words: 1352
team_size: 5
has_repo: false
has_live: false
has_video: false
tags:
  - "project"
  - "mechanism/deterministic_policy"
  - "mechanism/human_in_the_loop"
  - "mechanism/provenance_signing"
  - "mechanism/realtime_stream"
  - "domain/developer_tools"
  - "user/developer"
  - "user/government_staff"
  - "user/legal_professional"
  - "substrate/structured_db"
---

# ConsentKey

> A Logitech Actions SDK plugin that turns your MX Console into a physical consent firewall — blocking AI agents from executing risky actions without a hardware-signed human approval.

[Devpost](https://devpost.com/software/consentkey) · hackathon [[DevStudio 2026 by Logitech]]

## Facets

**mechanism** [[deterministic_policy]] [[human_in_the_loop]] [[provenance_signing]] [[realtime_stream]]
**domain** [[developer_tools]]
**user** [[developer]] [[government_staff]] [[legal_professional]]
**substrate** [[structured_db]]

**stack** actions, api, github, jwt, logitech, node.js, python, rest, sdk, sha-256, typescript, websocket, yaml

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for consentkey

## Body

ConsentKey Architecture Inspiration AI agents are no longer experimental. Tools like Cursor, GitHub Copilot, and CI/CD bots can now autonomously rotate cloud keys, deploy to production, delete databases, and modify infrastructure — faster than any human can supervise. We watched a developer's Cursor session accidentally propose dropping a production table. Another team had a CI bot rotate secrets mid-deployment, breaking 14 dependent services. The compliance team asked: "Who approved this?" The answer was nobody. Software approval dialogs exist, but they're click-through noise — the digital equivalent of a terms-of-service checkbox. YubiKeys prove identity, not intent. There was no tool that required a human to physically, deliberately, and provably consent to what an AI agent was about to do. That gap is what inspired ConsentKey. We asked: what if the Logitech MX Console wasn't just a productivity surface — what if it became a trust anchor ? A physical object that stands between an AI agent and the real world, requiring a real human decision before anything dangerous executes. What it does ConsentKey is a Logitech Actions SDK plugin that transforms the MX Creative Console and MX Master 4 into a physical consent firewall for AI agents and automation workflows . When an AI agent or automation tool wants to execute a high-risk action — a Terraform apply, a kubectl delete, a secrets rotation, a production deploy — it must first request a hardware-signed approval token from the MX Console. Here's what happens: The Console displays a consent card showing exactly what will happen: action summary, a diff of changes, risk level (LOW / MEDIUM / HIGH / CRITICAL), and estimated blast radius. The device vibrates a risk-encoded haptic pattern — a single gentle tap for low-risk, an unmistakable danger pulse for high-risk. Your body feels the weight of the decision before your eyes process it. You perform a deliberate physical gesture to approve or deny. Low-risk actions require a single press. High-risk requires a hold + confirm. Critical actions require a two-step sequence and a typed reason note. There is no accidental approval. A signed approval token is issued — containing the action hash, timestamp, your user ID, device serial, and policy ID. The agent must present this token to execute. Without it, the action is blocked with a 403. A tamper-evident audit log entry is written using SHA-256 hash chaining — every decision is cryptographically linked to the one before it, exportable for SOC2 and ISO 27001 compliance audits. The key insight: ConsentKey approves intent, not identity. That's what makes it different from any existing security tool. How we built it ConsentKey is composed of three tightly integrated components: 1. Actions SDK Plugin (MX Console UI Layer) Built using the Logitech Actions SDK, the plugin renders dynamic consent cards on the MX Console display, encodes risk levels as distinct haptic vibration patterns, handles gesture recognition (tap / hold / double-hold / deny twist), and communicates with the local Consent Broker over WebSocket. 2. Local Consent Broker (Security Engine) A lightweight local service that receives agent action requests over HTTP, evaluates them against a YAML-configurable policy engine, computes an action hash (SHA-256 of action type + parameters + timestamp), issues short-lived signed JWT approval tokens (60–180 second expiry), and writes the tamper-evident audit log. 3. Agent Adapters (Plug-and-Play Integrations) consent-run <command> — a CLI wrapper that gates any shell command logitech/consentkey-action@v1 — a GitHub Actions step for CI/CD workflows Python/Node SDK for programmatic integration with agent frameworks like LangChain, AutoGen, and Cursor extensions Policy rules are human-readable YAML: rules: - match: "terraform apply" risk: HIGH require: hold_confirm - match: "kubectl delete" risk: CRITICAL require: two_step + reason_note - match: "secrets/*" risk: HIGH require: hold_confirm + dual_approval Challenges we ran into Making haptics feel meaningful, not random. The hardest design problem was creating haptic patterns that communicate risk intuitively — without any training. We went through dozens of pattern iterations. The breakthrough was thinking of it like a car's collision warning system: the urgency of the sensation has to match the urgency of the situation instinctively. Preventing accidental approvals without creating friction hell. If the consent flow is annoying, developers will find ways around it — defeating the entire purpose. We had to find the right balance: low-risk actions should feel effortless (single tap), while high-risk actions should feel deliberate (hold + confirm) without feeling punishing. The gesture design went through multiple rounds of user testing. Making "tamper-evident" actually credible. Saying "audit log" is easy. Making it tamper-evident in a way that a compliance auditor would accept required building real hash-chaining — each log entry includes the SHA-256 hash of the previous entry, making any retroactive modification detectable. Getting this right without overclaiming what MVP cryptography can guarantee took careful scope management. Scoping the integration surface. AI agents can plug into hundreds of tools. We had to resist the temptation to build adapters for everything and instead pick the one scenario that is universal and immediately legible to judges and users alike: preventing destructive infrastructure actions. One use case, told perfectly, beats five use cases told vaguely. Accomplishments that we're proud of Reframing the hardware's identity. The MX Console is marketed as a productivity tool. We turned it into a security primitive. That conceptual shift — from shortcut surface to trust anchor — is the accomplishment we're most proud of. The haptic risk language. Building a vocabulary of physical sensations that communicates risk level without any visual interface is genuinely novel. It works. Users in testing could distinguish LOW from HIGH from CRITICAL by feel alone within minutes. A real security architecture, not a demo. JWT-signed tokens, SHA-256 hash-chained audit logs, policy engine with YAML rules, device-serial-bound approvals — ConsentKey is built with the primitives that actual security engineers recognize and respect. One scenario that explains everything. The terraform apply demo — agent proposes dangerous action, console intercepts, haptic danger pulse, denied, safer alternative proposed and approved — tells the complete product story in under 60 seconds. That clarity is an accomplishment in itself. What we learned Physical objects change decision-making quality. There is a body of research on "friction by design" in security — adding intentional resistance to dangerous actions improves outcomes. What we didn't fully appreciate until building ConsentKey is how much more effective physical friction is than digital friction. A popup is dismissed without thought. A haptic pulse and a hold gesture cannot be. The "YubiKey vs. ConsentKey" distinction is everything. Early feedback often came back: "isn't this just a YubiKey?" Clarifying that YubiKeys authenticate who you are while ConsentKey authenticates what you're agreeing to — and shows you the specific action, diff, and blast radius before you agree — was the sharpest communication challenge and the most important lesson in how to position a genuinely new category. Compliance teams are the real buyer, not developers. We built ConsentKey thinking about developers. We learned quickly that the economic buyer is the compliance officer, the CISO, the person who has to answer "who approved this?" to an auditor. Designing the audit log and compliance export features with that person in mind changed the entire product roadmap. What's next for ConsentKey Short term (next 90 days): Full public release on the Logitech Marketplace Adapters for the top 5 agent frameworks: LangChain, AutoGen, Cursor, GitHub Copilot, Devin Team dashboard for shared policy management and real-time approval notifications Slack/email alerts when a CRITICAL action is blocked Medium term: Dual approval mode — CRITICAL actions require consent from two different registered MX devices, enabling a true two-person integrity control for the most sensitive operations Mobile companion app — approve low-risk actions remotely when away from the desk, while hardware remains required for HIGH and CRITICAL Compliance report generator — one-click SOC2 and ISO 27001 evidence packages from the audit log Long term: Expand ConsentKey beyond the MX Console to any Logitech device with haptic capability — making the entire Logitech hardware ecosystem a distributed trust infrastructure for the age of autonomous AI Partner with CI/CD platforms (GitHub, GitLab, Harness) and cloud providers (AWS, GCP) to make ConsentKey the industry-standard human-in-the-loop control for agentic workflows <div