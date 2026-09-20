---
slug: "ai-file-agent"
url: "https://devpost.com/software/ai-file-agent"
title: "AI File Agent"
hackathon: "Dropbox Sign AI-Powered Agreements Hackathon"
organization: "Dropbox"
winner: true
words: 210
team_size: 1
has_repo: true
has_live: true
has_video: false
tags:
  - "project"
  - "mechanism/provenance_signing"
  - "substrate/document_pdf"
---

# AI File Agent

> Create Dropbox Sign requests as natural as possible.

[Devpost](https://devpost.com/software/ai-file-agent) · hackathon [[Dropbox Sign AI-Powered Agreements Hackathon]]

## Facets

**mechanism** [[provenance_signing]]
  <sub>weak: vision_ocr</sub>
**substrate** [[document_pdf]]

**stack** dropbox-sign-api, nanonets-ocr, nextjs, openai

## How they structured the write-up

- fileagent.ai
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for ai file agent

## Body

Simply fill a Dropbox Sign signature request template to create it and send it Get custom options for a given file type Night mode available What's the most natural way to understand a PDF file and generate a Dropbox Signature request from it? fileagent.ai What it does Upload any file type, use a PDF file in this case, understand its content and then generate a Dropbox Signature request as easy as possible. How we built it We designed and built a responsive web conversational UI to chat with your files: ✅ Extract content from any PDF file ✅ Authorize Dropbox Sign API to create e-signatures on your behalf ✅ Create embedded Dropbox Sig requests and send them to the signers Challenges we ran into Using only a textarea input, how can you seamlessly navigate a workflow to create a Dropbox Sign request? Accomplishments that we're proud of Try it out! It takes less than 30 seconds to create and embedded Dropbox Sign request. What we learned It is possible to integrate the whole Dropbox Sign API by using this custom chat interface. What's next for AI File Agent List all signature requests applying search filters Send reminders to the signers of a given signature request Add and edit signers <div