---
slug: "chancery"
url: "https://devpost.com/software/chancery"
title: "Chancery"
hackathon: "DevNetwork [API + Cloud + AI] Hackathon 2026"
organization: "DevNetwork"
winner: true
words: 1684
team_size: 1
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/benchmark_measured"
  - "mechanism/provenance_signing"
  - "mechanism/realtime_stream"
  - "mechanism/revocation_withdrawal"
  - "domain/civic_government"
  - "domain/developer_tools"
  - "domain/finance_payments"
  - "domain/legal_justice"
  - "domain/supply_logistics"
  - "user/developer"
  - "user/general_public"
  - "user/legal_professional"
  - "substrate/code_repository"
  - "substrate/document_pdf"
  - "substrate/financial_record"
  - "substrate/structured_db"
---

# Chancery

> Power of attorney for AI agents. A human signs what the agent may commit to; every irreversible act is checked against that signed document and refused, out loud, with the clause it broke.

[Devpost](https://devpost.com/software/chancery) · hackathon [[DevNetwork -API - Cloud - AI- Hackathon 2026]]

## Facets

**mechanism** [[benchmark_measured]] [[provenance_signing]] [[realtime_stream]] [[revocation_withdrawal]]
**domain** [[civic_government]] [[developer_tools]] [[finance_payments]] [[legal_justice]] [[supply_logistics]]
**user** [[developer]] [[general_public]] [[legal_professional]]
**substrate** [[code_repository]] [[document_pdf]] [[financial_record]] [[structured_db]]

**stack** dns-over-https, dnssec, doctavian, foxit-esign, foxit-pdf-services, model-context-protocol, name.com, next.js, nutrient-dws, pades, pdf-a, react, rfc-8785, serpapi

## How they structured the write-up

- the problem
- what it does
- where the boundary is, and why
- a finding that went against us
- proof you can run
- proof you can check without cloning anything
- honest limits
- how i built it
- build story — xano
- one line per sponsor

## Body

The problem Agents are getting hands — they register domains, send contracts for signature, move money. Each of those is irreversible; there is no undo on a purchase and none on a signature. The usual answer is a guardrail: a config file, a policy YAML, an allowlist in the prompt. All of them share one flaw. The person who bears the consequences never read them. They approved a summary in a chat window, and what actually gets enforced is a separate artefact sitting in a database row that anyone with write access can widen. Chancery closes that gap: the thing the human reads and signs IS the thing that gets enforced, and every field of it traces back to the page it was read from. What it does A human signs a writ — a document stating exactly which irreversible acts an agent may commit to on their behalf, with spend caps, allowlists, name patterns, expiry, jurisdiction and escalation thresholds. The signed PDF is read back into machine-readable terms with a citation for every field; a term that did not ground in the page it came from is treated as absent, not as permissive. The document's hash, the agent's key and an expiry go into DNS as a WRIT1 TXT record, in the same place SPF, DKIM and CAA already live. From then on every irreversible act the agent attempts re-resolves DNS, re-checks the document hash, re-runs due diligence against live web data, and returns ALLOW or DENY citing the clause and the page. Revocation publishes a tombstone rather than deleting the record, because a deleted record is invisible to a resolver still serving the old answer from cache. Where the boundary is, and why Foxit left signing out of their MCP catalogue on purpose and invited entrants to argue about where the line belongs. This is the argument. Their line is drawn by tool category, which works but does not generalise: the moment an agent can also spend money, delete a record or publish something, each one needs its own bespoke exclusion, and none of them says what the human actually authorised. Worse, pushing the agent outside the protocol pushes it outside the place where the decision could have been recorded. Our line is drawn at irreversibility, and it is drawn once. Everything reversible is a tool an agent calls freely. Everything irreversible goes through a single gate, so an agent may ask for anything and the answer is a verdict citing a clause rather than a missing capability. A finding that went against us We claimed the boundary held because a PDF Services key is not eSign-entitled. We tested it and that is false: on a standard Foxit developer account the same credentials authenticate to eSign, which answers a well-formed call with a validation complaint rather than a refusal. Worse, our own probe had a classifier bug that read any error body as a refusal, so it would have reported success either way. Both are fixed, the withdrawn claim is recorded as DISPROVED in CLAIMS.md, and three tests pin the live-observed response shapes. It makes the argument stronger rather than weaker: a boundary cannot be delegated to a vendor's key scope, so it has to be about who holds a credential at all — which is why ours is structural. The agent process is constructed without any Foxit credential, and a credential field on its surface does not compile. Proof you can run pnpm bench — 35 scenarios with the expected verdict AND reason code declared as a literal before the engine runs, so a denial for the wrong reason scores as a failure. Six permitted, sixteen refused, thirteen traps. 35/35, zero false allows, zero false denies. No credentials, no network. pnpm demo — the whole walkthrough with real verdicts. pnpm verify chancery.live — resolves the live writ from public DNS. pnpm verify --bundle evidence/D-10.json — re-derives a published verdict offline; edit the recorded outcome and it refuses and exits non-zero. pnpm boundary — makes Foxit refuse us live and prints what it said. pnpm smoke — ten live calls to the real services, none skipped. 817 tests, tsc clean. Proof you can check without cloning anything Run dig +short TXT _writ.chancery.live and hash https://chancery.live/w/1.pdf — both give DJFCbC3nwknF6XUaOH9xIRBRWCSd6-UL4GiXzdiQjAs. That document was rendered from the same Writ object the engine enforces, converted to PDF/A and cryptographically signed, and its hash written into DNS through the registrar's API. The public ledger at https://x8ki-letl-twmt.n7.xano.io/api:chancery-verify/ledger/spine returns the hash chain: eleven links, genesis all zeros, unbroken. Those hashes are computed by an RFC 8785 canonicaliser running inside a Xano lambda and reproduced byte for byte by the TypeScript one, and the client refuses any entry it cannot recompute. Honest limits The published zone is not DNSSEC-signed — name.com's default nameservers do not support it — so a strict verifier reports the authority as unverified and denies; the opt-out is explicit and recorded in every decision made under it. Extraction is cached per document rather than re-run per act, which is safe because the hash is re-checked every time, but it is the one cached input in the path. Doctavian generates the writ live and all sixteen output checks pass, but the writ currently published at chancery.live was rendered through the Nutrient fallback: it was produced while Doctavian's engine was returning 500s, and the hash in DNS is bound to those exact bytes rather than to the newer document. Clause 2.1 prints its expiry as a raw ISO instant, because Doctavian has no date-formatting function that returns anything - the date is right and the presentation is not. A free-tier signature chains to a test certificate, not a publicly trusted root. Full accounting in CLAIMS.md and MOCKS.md, including an explicit NOT-CLAIMED list of things we are not asserting. How I built it The decision engine is a pure function of its inputs — no clock, no network, no database read — which is why a 35-case benchmark can exist at all and why any published verdict can be re-derived offline from its evidence bundle. Around it sit seven ports, one per external service, so it stays obvious which vendor is load-bearing for which step. Everything reversible is an MCP tool; everything irreversible goes through one gate. Three defects were found by running the thing rather than reading it: a record that could not be hashed made every unsigned writ throw instead of deny, an extraction schema whose hoisted rows meant a cap nobody could read became a clause with no cap, and the Foxit finding above. All three are in the commit history with the reasoning. Build story — Xano I replaced the approval portal: the procurement category where a human rubber-stamps a queue of requests with no context. Chancery replaces the queue with one signed instrument the machine enforces for every subsequent request, citing the clause. Built with Claude Code in one session. What would have taken far longer without Xano is standing the backend up headlessly — the whole schema, endpoints, functions and API groups went up in a single POST to /workspace/{id}/multidoc instead of an afternoon of clicking. What cost real time was XanoScript: almost none of my first pass was right, and the authoritative grammar turns out to ship inside npm pack @xano/developer-mcp as markdown rather than on the docs site. Twenty-nine findings that contradict or are missing from the public docs are written up in xano/README.md — the costliest being that a ? after the type means nullable while a ? after the name means optional, and that unknown filters parse fine and fail only at runtime, so |default: pushes green and then breaks. One line per sponsor Each challenge asks for this separately. Foxit Foxit does the reversible document work through its MCP server, and its eSign API is the one thing the agent provably cannot reach: the agent process holds no Foxit credential, so the refusal in the demo is a real 400 from Foxit rather than a message we wrote, and pnpm boundary reproduces it live. Doctavian Doctavian generates the writ, and it is the only part of the stack that could: the terms loop over each granted act and nest a second loop inside it, branch on jurisdiction and on which limits are set, and compute the aggregate ceiling, the expiry and the escalation threshold from their parts - sum() over four string-typed fields yields 2650.00 rather than a concatenation, and 25% of it yields 662.50. Sixteen assertions read those values back out of the rendered PDF and all sixteen pass. We also built the Doctavian MCP server that does not exist yet, and the undocumented behaviours we hit are written up in the repo - the costliest being that mdoc:text is a container element, so the self-closing value= form the docs imply is accepted, renders nothing, and reports no error, which silently deletes a whole clause from a document that still looks complete. Nutrient Nutrient does the load-bearing work twice: it renders and cryptographically signs the writ, and it reads the signed PDF back into enforceable terms with a citation for every field. The grounding gate keys on the match kind rather than the confidence number, exactly as Nutrient's own guidance says to, and never renders that number as a percentage. name.com The name.com API is both the second irreversible act we gate — registration spends real money and cannot be undone — and the publication and revocation channel for authority itself: search, registration, DNS record CRUD and DNSSEC, with revocation published as a tombstone rather than a deletion. SerpApi Live search is the second axis of the decision. Scope answers "was this permitted"; eleven SerpApi engines answer "is it still a sane thing to do", and a denial on a trademark collision nobody anticipated is the sharpest moment in the demo. A check that cannot complete returns unknown, and unknown denies. Xano Xano is the backend of record: registry, append-only ledger, act history, auth, expiry sweep, durable retry queue and an HMAC-verified webhook inbox, deployed as 45 XanoScript definitions in a single Metadata API request. <div