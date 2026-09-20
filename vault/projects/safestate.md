---
slug: "safestate"
url: "https://devpost.com/software/safestate"
title: "SafeState"
hackathon: "H0: Hack the Zero Stack with Vercel v0 and AWS Databases"
organization: "Amazon"
winner: true
words: 1387
team_size: 2
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "domain/civic_government"
  - "domain/finance_payments"
  - "domain/housing_homeless"
  - "domain/retail_commerce"
  - "domain/transportation"
  - "user/general_public"
  - "substrate/code_repository"
  - "substrate/document_pdf"
  - "substrate/financial_record"
  - "substrate/geospatial"
  - "substrate/structured_db"
  - "substrate/video_visual"
  - "substrate/web_dom"
---

# SafeState

> A recall is just a PDF until something acts on it. SafeState blocks recalled products from being resold in real time, and warns the people who already own one. Built on Aurora DSQL and DynamoDB.

[Devpost](https://devpost.com/software/safestate) · hackathon [[H0- Hack the Zero Stack with Vercel v0 and AWS Databases]]

## Facets

**mechanism** [[realtime_stream]]
**domain** [[civic_government]] [[finance_payments]] [[housing_homeless]] [[retail_commerce]] [[transportation]]
**user** [[general_public]]
**substrate** [[code_repository]] [[document_pdf]] [[financial_record]] [[geospatial]] [[structured_db]] [[video_visual]] [[web_dom]]

**stack** amazon-aurora-dsql, amazon-dynamodb, amazon-web-services, anthropic-claude, aws-iam, cpsc-recall-api, fda-api, geist, next.js, nhtsa-api, node-postgres, postgresql, react, resend

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for safestate

## Body

Inspiration Somewhere right now, a crib that was recalled for a strangulation risk is sitting in an online listing. Photographed nicely. Priced to sell. The recall for it exists. It is public. A government agency issued it, a manufacturer paid for it, the news covered it. And none of that will stop the sale, because a recall today is just information. It lives on a web page and waits to be found. That is the part that got under my skin. We are not short on warnings. We are short on warnings that do anything. The first owner of that crib might have gotten an email. The second owner, the one buying it used for a new baby, is on nobody's list. The recall and the sale never meet. I wanted to build the thing that makes them meet. What it does SafeState turns a recall from a notice into a rule that a sale has to pass. The moment a used product is listed or bought, the marketplace asks SafeState one question: is this exact unit safe to sell. A recalled crib comes back blocked, with the hazard and the remedy attached. A safe one, the same model with a different serial number, goes straight through. The block is precise down to the individual serial, so a recall that only covers a range of units never punishes the rest. Around that one decision I built the rest of the experience: A marketplace gate that authorizes or blocks a sale in real time, at checkout. A manufacturer console to issue a recall by model, lot, serial range, or a single unit. The instant it is published, SafeState emails the current owners of affected units, not just the original buyers. A public "is it recalled?" check anyone can use, on any product, food, or vehicle, searching the live CPSC, FDA, and NHTSA databases at once. Safe Handoff for a private sale: check a used item, then share a link, a QR code, and a durable receipt, so the warning travels with the item. A bulk catalog scan that shows a marketplace its entire recall exposure in one call. A safety passport that follows a product to whoever owns it now, and an AI assistant that maps messy second-hand listings to the right recall. A consistency lab where you can run the multi-region read, a real concurrency race, and a 100-way load test yourself, against the live cluster. How we built it The front end is Next.js on Vercel. The transactional core is Amazon Aurora DSQL, and it is not there for decoration. The whole product rests on one promise: the instant a recall is committed anywhere, no marketplace in any region can ever read that product as safe again. That is a strong consistency problem, and it is exactly what DSQL is built for. I ran it as a real multi-region cluster, active in us-east-1 and us-east-2 with a witness in us-west-2. Write a recall through one region and the other region sees it immediately. No replication lag, no stale window. The trick that holds the guarantee together is small and a little satisfying. A recall and a sale of the same product are made to write the same row, a single per-model safety guard. DSQL uses optimistic concurrency, so when those two transactions race, one commits and the other is rejected with a real conflict, SQLSTATE 40001. My code catches it, retries the whole transaction, reads the freshly recalled state, and blocks the sale. That race can happen a thousand times and the recalled product never slips through once. I used a second database on purpose. Aurora DSQL owns the transactional decisions, where strong consistency is the product. Amazon DynamoDB owns the opposite workload: the high-volume, append-only stream of every check, verify, and scan, plus the durable Safety Receipts. That stream does not need a distributed transaction, so it sits on the database that fits it. The rest is glue I am quietly proud of. IAM token auth to the database, so there is no password living anywhere. A Vercel Cron job that pulls real recalls from the CPSC API every day. Claude, reading a listing a human actually wrote, like "used baby sleeper, works great," and figuring out which recall it belongs to. And email, sent through Resend, that reaches the people who already own a recalled product. Challenges we ran into Making the conflict fire on purpose was the first real fight. DSQL runs snapshot isolation, which will happily let two transactions that touch different rows both succeed, even when together they break a rule. So I had to design the collision, routing both the recall and the sale through that one guard row. DSQL has its own house rules too. No auto-increment sequences, so IDs are generated in code. One schema change per transaction. No foreign keys, so relationships live in the application. None of it is hard once you stop fighting it, but it does rewire how you think about a schema. Deploying taught me a lesson I will not forget. Vercel runs on Lambda, and Lambda reserves the AWS credential variables for itself, so the obvious way to give my functions database access simply does not work. I had to pass the credentials under different names and hand them to the signer directly. The load test taught me something too. My first version put a row lock on the guard during every check, which made two unrelated blocked checks conflict with each other for no reason. The conflict I actually care about is between a recall and an authorized sale, and both of those already write the guard row, so I dropped the lock from the read. The blocked path stopped fighting itself, and a hundred concurrent attempts now run clean. And the real world was messy, the way it always is. The public recall data has records where the title belongs to one product and the details to another, so I learned to trust the fields that are actually reliable and let the AI sort out the rest. Accomplishments that we're proud of That the hard promise is real, and real in production, not on a slide. You can open the live site right now, issue a recall in one region, and watch the other region block the sale a heartbeat later. You can fire two conflicting transactions and see the actual database conflict resolve itself in front of you. It holds under load. A stress test fires a hundred concurrent attempts to buy a recalled unit at the live cluster, and every single one is blocked. Zero recalled units sell. And the owner notifications are real: issue a recall, and a real email goes out naming each current owner and the exact unit they have. Mostly, I am proud that it does not feel like a demo. It feels like the beginning of something that should already exist. What we learned The biggest lesson is about when to reach for a database like DSQL. It earns its place when being correct under concurrency is the product itself, not a footnote. A recall registry sounds boring until you notice that its entire value is that two people can never disagree about whether a product is safe. That is a consistency problem wearing a child-safety costume. I also came away with a real feel for snapshot isolation and optimistic concurrency, the habit of forcing conflicts through a shared row, and a sense of where a second database earns its place: not for everything, but for the one workload that genuinely does not need a transaction. What's next for SafeState The next move is to live inside a real checkout, as an API a marketplace drops into its listing and payment flow, with tenant accounts and keys. The engine already reaches past cribs, into food and vehicles, and the next categories are batteries and appliances. The part I care about most is reaching even more of the current owners, the second or third owner nobody can contact today, through physical QR tags on resold items and a simple owner registry. A recall should find the person holding the product, not the person who bought it first. Recalls should stop being paper and start being decisions. This is the first version of that. <div