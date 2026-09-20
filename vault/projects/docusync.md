---
slug: "docusync"
url: "https://devpost.com/software/docusync"
title: "DocuSync"
hackathon: "The Postman API Hack"
organization: "Postman"
winner: true
words: 518
team_size: 1
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "domain/developer_tools"
  - "user/developer"
  - "substrate/code_repository"
  - "substrate/document_pdf"
---

# DocuSync

> Sync Github's Markdown file with Postman Documentation leveraging the power of Postman Monitors.

[Devpost](https://devpost.com/software/docusync) · hackathon [[The Postman API Hack]]

## Facets

**mechanism** [[realtime_stream]]
**domain** [[developer_tools]]
**user** [[developer]]
**substrate** [[code_repository]] [[document_pdf]]

**stack** api, github, postman

## How they structured the write-up

- inspiration
- what it does
- how i built it
- challenges i ran into
- accomplishments that i am proud of
- what i learned
- what's next for docusync

## Body

Inspiration We developers have heard from time to time that documentation is more important than the code itself. So is the documentation for APIs. Postman provides a markdown editor to document a Workspace, Collection, or even a Request and I have been contemplating for a while on how to integrate version controlling with Postman's Documentation editor. Why version controlling for API documentation, you ask?? Well to understand that lets imagine a situation. You have updated your old API documentation but turns out after a couple days you need the old document because your team or even yourself has came to conclusion after quite deliberation to keep the old API format. What would you do?? One solution is to save all the versions of different API documentation on your local machine before you change the documentation in Postman. But why the hassel?? That got me started on this project of integrating Github and Postman's Documentor and syncing real-time. Yes I am aware that I have shared my API Keys. They will be rendered inactive by the time I upload this project. Thank you. What it does It lets you create a project or a repository in github and listens, through postman monitor, if there is any changes in the markdown file specified. If there is any changes then it parses the text inside of the file and automatically syncs that with the documentation in postman that you have connected the markdown file with. How I built it Well first of all, It uses both Postman's and Github's API to send and take actions between them. And for that reason it requires the User's API Key. Docusync uses Postman Monitor for constantly checking for new updates in Github file and syncing with Postman. Once if it finds any updates in the Github repository it will parse the MarkDown file using the custom parse function that I have written. The parsed text is then stored as a environment variable and then used to set the documentation in postman. Challenges I ran into I have ran into couple problems when syncing the documentation for requests. Where as Workspaces and Collection documentations were "relatively" easy to set up with DocuSync. I wish I had more time to polish DocuSync. Time Management is a Big thing. Accomplishments that I am proud of I am proud that as a single person I could hack a bunch of stuffs together and create a fully working product that would boost developers productivity in the long run. What I learned I learned a lot about postman. I was amazed by the sheer strength of postman and what it could do. I never knew pre-request scripts, tests, mock server and especially monitors could be this powerful. I learned to manage the short time that I had. I learned how not to be a perfectionist. What's next for DocuSync There are couple things I would like to add to DocuSync. I hope that making DocuSync a postman's public workspaces would accelerate the development time. Two way sync between postman and github. The capability to resolve the concurrency issues automatically. <div