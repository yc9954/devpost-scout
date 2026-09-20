---
slug: "launchkit-7jb5l2"
url: "https://devpost.com/software/launchkit-7jb5l2"
title: "LaunchKit"
hackathon: "DevNetwork [API + Cloud + AI] Hackathon 2026"
organization: "DevNetwork"
winner: true
words: 838
team_size: 1
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/on_device_local"
  - "mechanism/realtime_stream"
  - "substrate/geospatial"
  - "substrate/web_dom"
---

# LaunchKit

> Your domain already replaces Bitly, Linktree & Google Workspace ($56/mo). LaunchKit makes it easy: AI naming, branded links, email, DNS, security & brand protection — no agency needed.

[Devpost](https://devpost.com/software/launchkit-7jb5l2) · hackathon [[DevNetwork -API - Cloud - AI- Hackathon 2026]]

## Facets

**mechanism** [[on_device_local]] [[realtime_stream]]
**substrate** [[geospatial]] [[web_dom]]

**stack** anthropic-claude, artificial-intelligence, brand-protection, css3, dns-management, domain-management, email-forwarding, git, html5, http-basic-auth, javascript, link-analytics, name.com-api, next.js

## How they structured the write-up

- inspiration
- how i built it
- challenges
- what i learned

## Body

AI generates 8 brand names instantly Branded links with click analytics Brand safety scan — 25 variants, 1 click Full DNS CRUD with type hints Order history with one-click refunds All domains, health & alerts at a glance Live webhooks, self-hosted receiver hello@domain.com → Gmail, free 4/4 score: lock, privacy, renew, DNSSEC AI Brand Kit + launch checklist Replace $56/mo tools with your domain Live shareable bio page on your domain Inspiration The idea hit me the same way it hits every founder: I registered a domain, and immediately opened three other tabs. Bitly for branded short links. Linktree for a bio page. Google Workspace for a professional email address. That's $\$35 + \$9 + \$12 = \$56$ per month — charged by three different companies — for capabilities my registrar's API already supported natively. The name.com API can create URL forwarding routes, email forwarding rules, manage DNS records, and handle the full domain lifecycle. The features were there. The product layer wasn't. I wanted to build the tool I wished existed on day one of domain ownership. How I Built It LaunchKit is a Next.js 15 App Router application with TypeScript, Tailwind CSS, and shadcn/ui. Every API credential stays server-side in route handlers — the browser never touches a key. The architecture has three layers: src/lib/namecom.ts — a typed client wrapping every name.com API endpoint with a single request<T>() helper using HTTP Basic Auth src/app/api/ — Next.js route handlers that proxy, normalize, and enrich responses before they reach the UI src/app/ — client components with real-time state The AI layer runs on local Ollama ( qwen2.5:14b ) during development and falls back to Anthropic Claude Haiku for cloud deployment — no model dependency required to run locally. I integrated 48 name.com API endpoints across 9 feature areas: Feature Endpoints AI name generation + registration 6 Link Hub (URL forwarding) 6 Email Hub 5 Security Center 9 Brand Protection scanner 1 (used creatively) DNS Record Manager 4 Transfer Manager 6 Domain Health + ZoneCheck 4 Notifications + Webhooks 4 Orders + Refunds 3 The Brand Protection scanner deserves its own mention. Given a registered domain mybrand.com , it generates ~25 variant domains algorithmically: TLD variants: mybrand.net , .org , .io , .co , .app , .ai Typo variants: doubled letters ($mybr\mathbf{aa}nd.com$), missing letters ($myband.com$), adjacent transpositions ($mybradn.com$) Prefix/suffix variants: getmybrand.com , mybrands.com , mybrandhq.com All 25 are checked in a single checkAvailability call. The result feeds a Brand Safety Score: $$\text{Safety Score} = \left(1 - \frac{\text{taken variants}}{\text{total variants}}\right) \times 100$$ A score below 70 triggers an amber alert. Green domains get a one-click Register button. Red domains are flagged as potential threats. Challenges The API spec vs. reality gap. The YAML spec said one thing; the sandbox returned another. Field names differed ( eventName vs event ), required fields weren't documented ( active: true on subscriptions, orderItemIds[] on refunds), and enum values had undocumented suffixes ( domain_expiration_change not domain_expiration ). Every integration required probing the actual error response to discover the real contract. Silent NaN serialization. Empty numeric form fields — Key Tag in DNSSEC, for example — produce Number('') = NaN . When serialized: JSON.stringify({ keyTag: NaN }) → { "keyTag": null } . The API returns 'key_tag' can't be null . No warning, no type error, just a silent null. Fixed with parseInt() and digit-only input handlers. Serverless AI. Ollama runs locally but not on Vercel. The fix was a priority chain: try Anthropic first if ANTHROPIC_API_KEY is set, fall back to Ollama. This made the app deployable to the cloud without changing a line of feature code. The sandbox stuck-domain problem. The sandbox processRefund marks order items as refunded but doesn't delete the domain from the registry. So after one test registration + refund cycle, the domain sits in limbo — not deletable, not re-registerable — for the rest of the session. The solution was detecting this state explicitly and showing a clear message rather than an opaque error. Shareable brand pages. The brand page at /b/[domain] is meant to be shared publicly. Initial implementation stored the profile in localStorage — invisible to anyone visiting from another device. Moved to a server-side in-memory store via /api/profile/[domain] , making the page genuinely shareable for the demo. What I Learned The name.com API is more capable than its dashboard suggests. URL forwarding, email routing, DNSSEC, webhooks — features most domain owners never discover because they're buried or unexplained. The real opportunity wasn't the API surface; it was the guidance layer on top of it. Building LaunchKit taught me that the best API integrations aren't wrappers — they're products. A security score is more useful than a list of toggles. A brand safety score is more useful than a raw availability check. The API gives you data; the product gives you decisions. The Brand Protection scanner is the clearest example: checkAvailability is a utility endpoint. But applied to algorithmically generated typo variants with a risk score and one-click remediation, it becomes a feature no competing tool offers. <div