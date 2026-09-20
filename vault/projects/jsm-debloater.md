---
slug: "jsm-debloater"
url: "https://devpost.com/software/jsm-debloater"
title: "GDPR Filter Panel for Jira"
hackathon: "Codegeist 2022"
organization: "Atlassian"
winner: true
words: 576
team_size: 6
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "domain/finance_payments"
  - "substrate/video_visual"
  - "substrate/web_dom"
---

# GDPR Filter Panel for Jira

> Allows JSM agents to effortlessly detect and delete GDPR-sensitive PII data in Jira issues using AI/ML- and regex-based classification in a continuous evaluation and learning on the Jira data fields.

[Devpost](https://devpost.com/software/jsm-debloater) · hackathon [[Codegeist 2022]]

## Facets

**domain** [[finance_payments]]
**substrate** [[video_visual]] [[web_dom]]

**stack** atlaskit, forge, javascript, lerna, react, rust, tensorflow.js, typescript, wasm, yarn

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for gdpr compliance for jira/jsm

## Body

Inspiration We were inspired to continue the way our most successful app, Kantega SSO Enterprise was built, through solving a pain we felt ourselves. We started off with our issues in JSM, and our first idea was a "JSM-debloater", which identifies and wraps signatures and other html email artifacts that take up unnecessary space. The idea evolved and we instead went for another avenue - GDPR and sensitive data. As JSM users we have issues with complying with GDPR, which requires us to delete Personal Identifiable Information (PII) after a certain time since our processing rights expire. Our goal for this app is to enable JSM agents to continuously keep their Jira GDPR-compliant by purging outdated and unnecessary PII which they no longer have legitimate interest to process. What it does Offers a panel to filter out PII in textual- and image data in Jira Issues using regex- and Machine Learning-based classification. Feedback loop where false positives may be rejected and added to a knowledge pool, while real PII can be removed from the issue. Offers row specific and global bulk edit of PII data. Detects data like phone numbers, credit card numbers, email, name, both in text-based and image-based classification. How we built it We do text based PII(Personal Identifiable information) through a Web assembly module compiled from Rust code. This will give us better performance, but we also mase this as a POC to test if it is viable to use Wasm in a Atlassian Forge context. Next we tried adding a image classification pipeline, based on tensorflow.js, for detecting PII in image attachments. We added a form for uploading and training a neural network model through "transfer learning", a process that builds a new model based on an existing model for similar problems. We also show that running a image classification is viable in a jira issue panel module. Challenges we ran into New and emerging technologies leads to a lot of changes, that often leads to documentation being outdated. Tensorflow and AI/ML in general is theoretically heavy subjects, and we need to further read up on the ML basics, as well as the tensorflow specifics. Accomplishments that we're proud of Web Assembly (WASM) in Forge! Tensorflow classifications in the browser, inside Forge. What we learned How to run Wasm within forge context Limitations and possibilities within Forge Transfer learning allows us to provide users with a powerful and modifiable classification model, client side. How to develop efficiently in Forge. Tunneling, handling appIds and using our preferred frameworks within this context. What's next for GDPR Compliance for Jira/JSM We envision a powerful app that allows organizations to effortlessly maintain a GDPR-compliant Jira instance. While it today filters PII for existing data, we envision a solution with live preemptive client-side detection of GDPR-sensitive data which can be stopped live, before it is submitted. Some of our ideas require changes and more flexibility to the Forge platform, other might be possible to acheieve with more engineering efforts. Possibly running training and/or classifications in Forge backend Customization of regex filter rules for PII detection Utilize usage data to improve detection models over time(continous learning) Finalizing the app and releasing to marketplace. Group-based scramble hiding of data based on user memberships. Here we are currently limited by Forge APIs. Hopefully forge will allow us to be able to preemptively filter data client-side in the future, as this is not possible with the current state of Forge. <div