---
slug: "emr-interop-attacking-the-chaos"
url: "https://devpost.com/software/emr-interop-attacking-the-chaos"
title: "EMR Interop – Attacking the Chaos"
hackathon: "The Postman API Hack"
organization: "Postman"
winner: true
words: 660
team_size: 3
has_repo: false
has_live: true
has_video: false
tags:
  - "project"
  - "domain/finance_payments"
  - "domain/health_clinical"
  - "user/clinician"
  - "user/general_public"
  - "user/patient_family"
  - "substrate/geospatial"
  - "substrate/medical_record"
---

# EMR Interop – Attacking the Chaos

> EMR integration fuels digital health...but the APIs are a mess. Let us help you build and test integrations covering 85%+ of the market.

[Devpost](https://devpost.com/software/emr-interop-attacking-the-chaos) · hackathon [[The Postman API Hack]]

## Facets

**domain** [[finance_payments]] [[health_clinical]]
**user** [[clinician]] [[general_public]] [[patient_family]]
**substrate** [[geospatial]] [[medical_record]]

**stack** javascript, postman, python

## How they structured the write-up

- our purpose
- the tech
- creatitivity
- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for emr interop – attacking the chaos

## Body

Our Purpose To facilitate the critical acceleration of consumer facing digital health projects (including our own) by simplifying the daunting task of multiple EMR integration. The Tech We used Collections, Environments, tried (and failed) to use OpenAPI (both as an import and a link), and did our first monitor test today. Creatitivity We didn't come to slay a mouse. We're trying to use POSTMAN to wrestle a handful of mission critical, gigantic, sporadically documented, poorly tech supported third party APIs to the mat. How hard could that be? Inspiration Fueled by C19, insurance incentives and changing patient behavior 2020 saw accelerating growth in healthcare startups and funding More than 90% of new digital health startups in 2020 have an incredible tech hurdle to create a great experience…integration into doctor office systems, or Electronic Medical Records (EMRs) However, no two EMRs have either similar API calls or responses... What it does We built a POSTMAN workspace to facilitate development and testing We cover about 85% of the market and enable dev and testing of both ADMIN and CLINICAL capabilities For each call, we help build the request and show an example of the expected response We also have some environmental variables setup for common parameters and for the demo we’ve populated a token and some EMR values When we make the call, we also generate some some variable outputs that capture the EMR called, the FUNCTION called, and the RESULT For our service, we need to NORMALIZE the results, so, for example, whether an EMR API result calls a diagnosis a PROBLEM, or a CONDITION or a DIAGNOSIS… we need to map it to a common vocab so we feed it to an API on our service and based on the last collection call, ensure the mapping is working [TESTING!} How we built it Lots o' manual data entry to capture the specific GET/POST/DELETE/PATCH schemas of the major EMR vendors. A lot more data entry across the major EMR development environments to populate them with enough physician and patient data so that we could oAuth setup always takes longer than we plan – the desktop version of POSTMAN was helpful for a couple of the integrations. We fought back the tedium with loud music. Using RUN COLLECTION capabilities, error checking 108 different API calls was probablyamong the fastest/easiest parts of the project! Challenges we ran into It took us a while to figure out how setting variables in the test worked -- we ran the scripts, then went to ENVIRONMENTS thinking it would update there. It didn't. We abandoned the NORMALIZATION part of our project for awhile until we stumbled across where the variables were displayed, then it worked like a MONSTER. We tried importing an OPEN API schema a couple of times. The tool recognized the format, but generated an error on three different types of attempts. Accomplishments that we're proud of We've already used the tool for a little CODEGEN for some functions we hadn't quite locked down yet. We also found seven meaningful errors in our integrations. Doh. What we learned That we were using about 5% of what POSTMAN could do, and that the RUN COLLECTION feature is going to save us a TON of HEADACHES What's next for EMR Interop – Attacking the Chaos A little more documentation -- if you have any EMR integration experience, you'll know how to use this, but we have started to build a quick walkthru We couldn't get the oAuth to work on the web version of POSTMAN (we could on the desktop) -- it's next on our list to make this a good testing tool We're looking into how we might convert this into an "availability check" tool for both ourselves and the EMRs (serendipitously [?] one of the EMR test environments went down while we were building, prompting one of the team members to ask "what's our fallback plan now when the EMR is not available?". Doh.) <div