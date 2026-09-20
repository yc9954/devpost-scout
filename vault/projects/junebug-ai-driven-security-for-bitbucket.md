---
slug: "junebug-ai-driven-security-for-bitbucket"
url: "https://devpost.com/software/junebug-ai-driven-security-for-bitbucket"
title: "Junebug - AI driven Security for Bitbucket"
hackathon: "Codegeist Unleashed"
organization: "Atlassian"
winner: true
words: 353
team_size: 0
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "domain/developer_tools"
  - "domain/security_privacy"
  - "user/developer"
  - "substrate/code_repository"
  - "substrate/video_visual"
---

# Junebug - AI driven Security for Bitbucket

> Using ChatGPT to identify security issues directly in Bitbucket repos and raise JIRAs for non-obvious bugs that are hard to detect. Ensures maximum visibility for exploits and mitigates shipping risks

[Devpost](https://devpost.com/software/junebug-ai-driven-security-for-bitbucket) · hackathon [[Codegeist Unleashed]]

## Facets

**domain** [[developer_tools]] [[security_privacy]]
**user** [[developer]]
**substrate** [[code_repository]] [[video_visual]]

**stack** forge, node.js, python, tensorflow

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for junebug - ai driven security for bitbucket

## Body

Code Overview Card to Display Security Issues flagged by Chat GPT Custom Bulk action to display All JIRAs created due to security vulnerabilities in code Modal that arrives on selecting the bulk action, allows navigation to any of the JIRAs for any security issue Automatically obfuscated text in image using the app, the image had PII and was present in the code repo. Sample JIRA created by the App from a security vulnerability tagged Inspiration Security meets AI in this Bitbucket extension for high functioning developer teams. Very simply put, Junebug automatically flags security issues in code, and also creates JIRA issues for prompt action and also for visibility. Automates developer and tester workflow in a single app. What it does Uses GPT and Tensorflow to flag security and privacy issues in code and images in any given Bitbucket repository, creates an external link to a JIRA issue, and adds the JIRA issue to the latest commit of the file. Please note this is also not a production ready app, but intended more as a Proof of Concept How we built it We used the Forge platform, tensorflow, google cloud functions for serverless processing, a bunch of UI Kit code. It was pretty entertaining and a white knuckled introduction to JSX for us. The code is open sourced at the Github below, come marvel at our misadventures! Challenges we ran into JIRA and bitbucket are not that closely linked, despite being Atlassian products. We had to do some headscratching because the product that we had envisioned right from the start imagined JIRA to be very tightly coupled to Bitbucket. But we got there in the end! Accomplishments that we're proud of Learning to use React, Forge and JSX in a week or so is pretty high up on our list of accomplishments. overall it was great fun to work on this hackathon, and the Forge platform is immensely powerful. What we learned Javascript is a very interesting language, Forge is an excellent platform. Overall 5 stars, would code again. What's next for Junebug - AI driven Security for Bitbucket Hopefully some recognition! <div