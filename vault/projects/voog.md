---
slug: "voog"
url: "https://devpost.com/software/voog"
title: "Voog"
hackathon: "NEAR MetaBUILD Hackathon"
organization: "NEAR Protocol"
winner: true
words: 800
team_size: 1
has_repo: true
has_live: true
has_video: false
tags:
  - "project"
  - "domain/finance_payments"
  - "domain/supply_logistics"
  - "domain/transportation"
  - "substrate/video_visual"
  - "substrate/web_dom"
---

# Voog

> Voog is the blockchain app-builder. Super-simple, UI-based smart contract builder with one-click deployment to the blockchain and an auto-generated UI to use the contracts.

[Devpost](https://devpost.com/software/voog) · hackathon [[NEAR MetaBUILD Hackathon]]

## Facets

**domain** [[finance_payments]] [[supply_logistics]] [[transportation]]
**substrate** [[video_visual]] [[web_dom]]

**stack** .net, assemblyscript, azure, blazor, bootstrap, c#, css, heroku, html, javascript, nearjs, spa, table-storage, typescript

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for voog

## Body

Voog.App Create workflows Gallery of examples Voog is an ancient Estonian word meaning 'flow' (of time or water). Inspiration General public is not really using blockchain - research shows it as well and its evident from Gartners latest analysis. It will be a long time (years) when blockchain is really used to solve day-to-day problems (and not just buying tokens). been thinking of a simple workflow/state-machine as a service for long time for my daily use in other projects Decided to combine these two ideas for this project: a super simple workflow engine with a visual builder to speed up blockchain adoption. What it does The idea is that it takes in a spec - a simple text representation of a workflow, and deploys it to blockchain. Spec has simple rules: one object with properties, states and state transitions. Example: Object: Ship Properties: Length/Height/Speed States: Standstill/Cruising Transitions: Sail (Standstill -> Cruising) and Stop (Cruising -> Standstilll) Main flow: There is a UI (SPA) which allows to easily edit the spec. In theory the spec of the workflow can also be created in Notepad and pasted into Voog.app. The the user can hit one button to compile it and also deploy to blockchain. Then the user can run methods on the workflow using an auto-generated UI as the client. You can ofcourse use any standard Near API. Examples can be found in www.voog.app/browse Other features: Transitions can have security restrictions: specific addresses or pre-approved addresses. Ability to add pre-approved addresses Transitions can also have payments to addresses Transitions can change object properties (variables) Copy AssemblyScript code - givest the raw assemblyscript which will be compiled. Copy/Paste Voog spec (text representation of workflow) Set color theme for every workflow - adds some individuality to each How we built it Javascript compiler uses NodeJs+Typescript and is hosted in Heroku. Front end app uses C#+.Net 6+Typescript+Blazor and Azure Tables to store the examples. Some other components used: Bootstrap, state-machine-cat (for diagrams) IDE used: Visual Studio 2022. Art was done by me as well (using Xara Designer Pro +) - I used to be a web designer long time ago. The skill sometimes comes in handy. Challenges we ran into I learned there are multiple variants, versions, modules, type systems etc in javascript/typescript: most challenging technically was to make Near AssemblyScript compiler work as a NodeJs service with all the Near compiler transforms - there were no examples and people in the Discord chat were saying its not possible or it is a "herculean effort". I was so happy when I finally got it working. I was struggling with near keys and giving automatic rights to users of the workflows so they could deposit funds with method calls. In the end I ran out of time - so that part is manual, but its not a blocker, just an inconvenience. Accomplishments that we're proud of Near API AssemblyScript compiler running as a service in NodeJs Everything works end to end. Although the main editor UI at first glance can be intimidating - it was still a lot of effort. The visual workflow image also helps. What we learned At some point during the project I realized when re-thinking existing businesses with a blockchain based workflow it fundamentally changes the game - opens up new opportunities and a more tight coupling with payments. More dialogue between counterparties (not just import/export data), but real integration of objects and actions. Its very easy to clone existing workflow to make your own. In the end I'd imagine instead of having 1 workflow (for example a supply chain) we end up with 1000 supply chain workflows with changes from industry, jurisdiction, culture etc. Instead of having one mammoth website (traditional SaaS), each company would have their own workflow/smart-contract - and in my view its an interesting re-thinking of the web and more in-tune with reality. What's next for Voog With proper funding the project could continue. Todo: Validate all assumptions. Go to different companies and see how the solution would work - what is missing and what is confusing. I already approached a large insurance provider to get feedback during the hackathon and the person (product lead) was very impressed. Increase the team Design a business model (have some options already) Automatic unit-test generation Flow integrations - being able to start sub-flows from parent flows. For example one flow could be to issue a parking ticket and impound the car- another flow to get the car out of impound (flow for impound operators)- which would again after finishing call the ticket flow to finalize the payment. This would make a flow essentially a lego building block. Different payment scenarios - multiple payment, parent item payments etc. Automatic formulas (like "parameter + 1" or "payment * ownerShare") Etc etc etc. <div