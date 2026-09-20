---
slug: "accessform"
url: "https://devpost.com/software/accessform"
title: "AccessForm"
hackathon: "DevNetwork [API + Cloud + AI] Hackathon 2026"
organization: "DevNetwork"
winner: true
words: 476
team_size: 2
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "domain/accessibility"
  - "domain/education"
  - "domain/finance_payments"
  - "domain/health_clinical"
  - "user/educator_student"
  - "user/social_worker"
  - "substrate/document_pdf"
---

# AccessForm

> Call. Talk. Your form is filled.

[Devpost](https://devpost.com/software/accessform) · hackathon [[DevNetwork -API - Cloud - AI- Hackathon 2026]]

## Facets

**domain** [[accessibility]] [[education]] [[finance_payments]] [[health_clinical]]
**user** [[educator_student]] [[social_worker]]
**substrate** [[document_pdf]]

**stack** nutrient, serpapi, xeno

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for accessform

## Body

AccessFrom Inspiration A friend, Rickan, put it simply: the people who most need help with official paperwork are the ones least able to do it online. A blind person with a hospital bill, a 70-year-old who can't walk to the bus, a student with ADHD facing a disability office form. They all have a phone. Most of them don't have a screen they can use, and some don't have internet at all. What it does You call a number and say what's going on in your own words. AccessForm works out which official program fits, finds the real application form from the official source, asks you its questions one at a time in plain language, fills the actual PDF, and texts you the result with a list of what's still missing. Everything happens in one phone call. It never submits, never signs, and never decides eligibility. If it can't verify an official form for the exact organization you named, it says so and stops. How we built it Vapi runs the voice agent on a Twilio number. Every tool call hits a Next.js backend that uses SerpApi to find and verify the official form, OpenAI to read the form's fields and turn them into spoken questions, pdf-lib to fill the real PDF, Nutrient for accessibility tagging when credits allow, and Xano as the system of record for cases, answers, and completeness. A conversation page rebuilds the call live from Xano's event stream, so a laptop can watch a phone call as it happens. Challenges we ran into The agent once served Cedars-Sinai's form to someone who asked for UCSF. That became the product's first rule: never substitute. Real forms vary wildly. Two of the four hospitals we tried publish flat PDFs with no fillable fields. One phone call kept turning into several cases whenever the caller changed topic. Vapi's 20-second tool timeout made the agent apologise for searches that had actually succeeded. Accomplishments that we're proud of A real call, from a real phone, ended with a real 146-field paratransit application filled and a text delivered. The Cedars-Sinai hospital path, the first one we built, still passes unchanged. And every status the app shows is literal: "preserved" means we kept the form's own tagging, "sent" appears only when the provider confirms. What we learned Honesty is a feature. The moments that built trust were the ones where the agent said "I couldn't verify that" instead of guessing. We also learned that the backend is only half the latency: a page polling too eagerly can slow down the phone call it's watching. What's next for AccessForm Filling flat PDFs by coordinate overlay. Approve-and-send by email once a program publishes an intake address. Spanish. And a catalog that grows from every verified call, so the second person who asks about a form gets it in a second. <div