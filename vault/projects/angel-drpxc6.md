---
slug: "angel-drpxc6"
url: "https://devpost.com/software/angel-drpxc6"
title: "Angel"
hackathon: "Mind the Product presents World Product Day: Everyone Ships Now"
organization: "Mind the Product"
winner: true
words: 575
team_size: 2
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "domain/finance_payments"
  - "substrate/document_pdf"
  - "substrate/financial_record"
  - "substrate/geospatial"
---

# Angel

> When aid orgs failed Ukraine, strangers saved strangers. Angel scales that. Pick a person, a verified volunteer manages their case, and you get the receipts. Compassion without the red tape.

[Devpost](https://devpost.com/software/angel-drpxc6) · hackathon [[Mind the Product presents World Product Day- Everyone Ships Now]]

## Facets

**domain** [[finance_payments]]
**substrate** [[document_pdf]] [[financial_record]] [[geospatial]]

**stack** claude, codex, github, lovable, novus, react, stripe, supabase, tailwind

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for angel

## Body

Novus Dashboard Get verified page (volunteer form). Volunteer verification: every helper, manually reviewed Browse verified cases: real people, real needs For donors page. For donors: how direct giving works Get help: a direct line for people in crisis Inspiration I've seen human compassion outperform big aid organizations. Since the start of the war, the volunteer network inside Ukraine has done extraordinary things — the whole world has witnessed it. Angel exists to let people abroad join that movement and help Ukrainians directly, scaling what Ukrainian volunteers on the ground are already doing every day. What it does Angel connects donors abroad directly to individuals in Ukraine through a network of verified volunteers. Donors browse real, documented cases and contribute to a specific person. Each case is owned end-to-end by a volunteer who stays in contact with the recipient, coordinates the support, and documents proof of delivery. Volunteers never touch funds — money flows directly from donor to recipient — and donors who complete verification can request deeper case details. How we built it We built Angel as a two-person team in the hackathon window. The frontend runs on Lovable, payments on Stripe, and we built parts of the system using Codex. We connected Novus to track user behaviours. Challenges we ran into Two big ones. First, Stripe — I'd never integrated payments before, and getting the flows right took real iteration, but it works. Second, and harder: figuring out how to keep volunteer, donor, and recipient information private without making the platform opaque. Privacy in a war context isn't a checkbox; the wrong disclosure can put a real person in real danger. We made our best calls for the hackathon build, and we've left room to iterate further (more on that below). Accomplishments that we're proud of We shipped a working end-to-end product as a two-person team — donor onboarding, volunteer onboarding, case creation, verification, and a live payment flow. Beyond the build, in the seven days since we started, we've already recruited volunteers, documented real cases of people who need help, and verified those cases. They're ready to receive support today. The only thing standing between donors and recipients right now is the switch from Stripe Sandbox to Stripe Live. What we learned The bigger lesson was about trust. Most aid organizations treat trust as a marketing message, and it's not working — they're losing public trust at scale. We decided to build trust through product design instead. Every decision at every step of the user journey — what to show, what evidence to surface, what options to give the user, what proof they can receive — either builds or erodes trust. There is no neutral choice. That realization clarified our mission: build a product where trust and transparency are reinforced at every step, so that no one is ever discouraged from helping another human being — or an animal — simply because they don't trust the system. What's next for Angel Going live. Switching Stripe from Sandbox to production so the verified cases we already have can start receiving help. In parallel, we'll be working closely with Ukrainian authorities to make sure personal data is protected at the standard the situation requires and that no one — recipient, volunteer, or donor — is put at risk. From there: expanding the volunteer network through trusted referrals, adding case categories (medical, displacement, education), and partnering with diaspora organizations that have reach but lack infrastructure. <div