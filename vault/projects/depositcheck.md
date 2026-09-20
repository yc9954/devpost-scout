---
slug: "depositcheck"
url: "https://devpost.com/software/depositcheck"
title: "DepositCheck"
hackathon: "DevNetwork [API + Cloud + AI] Hackathon 2026"
organization: "DevNetwork"
winner: true
words: 949
team_size: 1
has_repo: true
has_live: true
has_video: false
tags:
  - "project"
  - "domain/finance_payments"
  - "domain/housing_homeless"
  - "domain/retail_commerce"
  - "domain/transportation"
  - "user/legal_professional"
  - "substrate/geospatial"
  - "substrate/video_visual"
---

# DepositCheck

> Before you wire a rental deposit, drop in the listing's photo. Google Lens through SerpApi finds everywhere that exact image already lives, and names the other address it really belongs to.

[Devpost](https://devpost.com/software/depositcheck) · hackathon [[DevNetwork -API - Cloud - AI- Hackathon 2026]]

## Facets

**domain** [[finance_payments]] [[housing_homeless]] [[retail_commerce]] [[transportation]]
**user** [[legal_professional]]
**substrate** [[geospatial]] [[video_visual]]

**stack** computer-vision, google-lens, nextjs, node.js, react, reverse-image-search, serpapi, typescript, vercel, vercel-blob, vitest

## How they structured the write-up

- inspiration
- what it does
- how i built it
- challenges i ran into
- accomplishments that i'm proud of
- what i learned
- what's next for depositcheck

## Body

Inspiration Rental scams work by theft, not invention. A scammer copies the photos and the description from a real listing, swaps the contact details and the address, and reposts it somewhere with weaker verification. Someone wires a deposit for a property the "landlord" has never owned. Generation Rent examined 300 Facebook Marketplace rental listings in late 2024 and found 56% used images lifted from Booking.com, Rightmove or Zoopla. The photos are the one thing the scammer cannot change. Swap them out and the listing stops looking like the flat that attracts victims in the first place. But a renter cannot check that. You would have to recognise one apartment interior among billions of published images, from memory, on a phone, while a "landlord" tells you three other people are viewing tonight. A vision model does exactly that in about two seconds. Nobody was putting it in front of the renter at the moment the money moves. What it does You upload one photo from the listing and type the address you were given. SerpApi's google_lens engine with type=exact_matches runs Google's visual matching model over the live web index and returns every page carrying that same image. The claimed address is matched against what those pages say. The photo is deleted as soon as the lookup returns. Three verdicts: CORROBORATED : the photos appear elsewhere alongside the same address, which is what a genuine syndicated listing looks like. CONTRADICTED : the photos belong to one specific other address, and the result names it. UNVERIFIED : not enough evidence either way. There is deliberately no green "this listing is safe" state. A listing built from AI-generated photos returns zero matches, the identical signal to an honest landlord who photographed the flat themselves and posted it nowhere else. Absence of corroboration is not evidence of honesty, and a UI that implied otherwise would be at its most confident exactly when it was most dangerous. How I built it The perception layer is Google's image-matching model, reached through SerpApi. Matching one photo against the indexed web is a machine vision problem, and SerpApi is what turns it into a JSON response an application can reason over. What I wrote on top is deliberately not generative. Address parsing, source counting and classification happen in ordinary code, ending in a single pure function. The model perceives; lib/verdict.ts decides what the perception is worth. When a tool can accuse a real person of fraud, I want to point at the line that made the call and at a test that pins it. An LLM in that seat would have been faster to write and impossible to defend to the landlord on the other end of it. Next.js 16 and React 19 on Vercel, TypeScript throughout, Vercel Blob as the temporary photo host. 177 tests run fully offline and spend zero SerpApi searches. Challenges I ran into The tool accused a real landlord. On the first genuine production request, a marketing photo submitted with its true address came back CONTRADICTED. The matching logic was not at fault. That request received a truncated response of 23 matches; twelve later calls for the same photo returned 84 to 88, three of which name 13505 Burnet Rd, and the same code then said CORROBORATED. The bug was epistemic. CONTRADICTED had drifted to mean "your address appears in none of the matches", and against a live index that can return an incomplete answer, absence-based reasoning is unsound. A truncated result set and a genuine mismatch produce the same signal, and no threshold separates them: that truncated response still carried 23 matches across 9 sources, which is not thin by any measure I could have set. So absence stopped counting as evidence at all. An accusation now requires a competing street address actually found in the results, named by at least two independent sites. Truncation can cost a verdict, but it can never manufacture one. The reasoning is written up as ADR-0001 in the repo. Accomplishments that I'm proud of Shipping a tool that states, in the product, what it cannot do. DepositCheck cannot judge an apartment complex's marketing photo: those staged shots are reused across every unit and every aggregator page, so the same image legitimately appears under many addresses. Measured across four complexes, such photos yielded 0, 10, 10 and 26 competing addresses, never exactly one. So the app says so and asks for a different photo, a window view or an awkward corner of the actual unit, because those identify a property where a show kitchen cannot. A renter told "we cannot judge this" is safe. A renter told "this looks fine" is not. What I learned Search results are evidence, and evidence has to be handled like evidence. A live API returning less than it did a minute ago is normal operation, not an outage. I also learned where to draw the line between the model and the code. Perception belongs to the model, because no rule I could write recognises an apartment across a billion pages. Judgment belongs in code I can test, because the model has no way to know what a wrong answer costs the person reading it. And I learned to distrust green states. The strongest design decision in this project was removing an option from the verdict enum. What's next for DepositCheck Multi-photo checks, so one truncated response cannot decide a verdict on its own. SerpApi Google Maps to verify the address is a residential property rather than a parking lot or a mailbox storefront. SerpApi Google Search on the landlord's phone number and email, which scam operations reuse across dozens of listings. Per-caller upload token binding and an edge rate limit. <div