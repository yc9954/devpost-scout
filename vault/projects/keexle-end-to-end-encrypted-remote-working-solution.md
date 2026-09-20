---
slug: "keexle-end-to-end-encrypted-remote-working-solution"
url: "https://devpost.com/software/keexle-end-to-end-encrypted-remote-working-solution"
title: "Keexle Open Source Project"
hackathon: "The European Commission's EUvsVirus Hackathon"
organization: "European Commission"
winner: true
words: 940
team_size: 9
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/privacy_tech"
  - "mechanism/structural_withholding"
  - "domain/civic_government"
  - "domain/developer_tools"
  - "domain/legal_justice"
  - "domain/transportation"
  - "user/developer"
  - "user/educator_student"
  - "user/general_public"
  - "user/legal_professional"
  - "substrate/code_repository"
  - "substrate/web_dom"
---

# Keexle Open Source Project

> End-to-end encrypted, Open Source remote working solution

[Devpost](https://devpost.com/software/keexle-end-to-end-encrypted-remote-working-solution) · hackathon [[The European Commission-s EUvsVirus Hackathon]]

## Facets

**mechanism** [[privacy_tech]] [[structural_withholding]]
**domain** [[civic_government]] [[developer_tools]] [[legal_justice]] [[transportation]]
**user** [[developer]] [[educator_student]] [[general_public]] [[legal_professional]]
**substrate** [[code_repository]] [[web_dom]]

**stack** erlang, leveldb, node.js, socket.io, vuejs

## How they structured the write-up

- the problem your project solves
- the solution you bring to the table
- what you have done during the weekend
- the solution’s impact to the crisis
- the necessities in order to continue the project
- the value of your solution(s) after the crisis

## Body

The problem your project solves During this unprecedented crisis, we have all had to adapt to remote working. Collaboration platforms have unsurprisingly soared in popularity. Tools such as Zoom & Slack may be appropriate for the communication of non sensitive information. However for businesses, institutions & organisations who handle confidential and sensitive data the privacy protections offered by these mainstream tools are entirely insufficient. Zoom has received the bulk of the criticism in the media in the last few weeks, however almost every collaboration platform has the same fundamental problem. User data is somewhat protected by TLS encryptions in transit, however the technology behind all these platforms necessitates content being decrypted when it reaches the cloud provider's server. This means the provider of the service has complete and unrestricted access to its user's data. On top of this, from a European perspective, all the major tools are US based companies, we feel its important for Europe to have its on tools, built and hosted in the EU, without the need for European data to be sent to overseas servers for analysis and exploitation. There also lacks a platform for developers to be able easy integrate end-to-end encryption to the tools they build. The solution you bring to the table To help facilitate private and confidential remote woking during this crisis, during the Hackathon, we decided to open source the end-to-end encryption technology we have previously worked in order to provide an SDK / API to the world. This is the first step in The Keexle Open Source Project This project allows developers from across Europe and beyond to come together to build tools that permit remote working, without sacrificing privacy for convenience. The purpose of this is to give developers the chance to develop industry specific tools without having to worry about the cryptographic aspects. We can offer the community a strong layer of end-to-end encryption which can be applied to any kind of productivity application. The goal of Keexle Open Source Project is to create a marketplace for developers to publish their tools. All the applications in the marketplace will be protected by our Keexle end-to-end encryption technology. This gives anyone who is looking for remote working tools that do not sacrifice privacy over convenience an ecosystem of solutions to browse, that they can be confident offer the highest levels of privacy and confidentiality. What you have done during the weekend The challenge of this week-end was to specify how we can turn the core parts of Keexle into an SDK. To do so, we have worked on basic examples of applications where end-to-end encryption was not available (a basic chat message, a todo list application). This is mainly a refactoring of codes and the analysis of what can be abstracted to developers. We manage to write tutorials and we provide a zip file (with the source code) that allow any developers to integrate end-to-end encryption and replication mechanisms to any existing apps. We setup a website that explains the theoretical protocol behind our technology: https://www.keexle.com/opensource/docs/ The solution’s impact to the crisis Clearly during this period of unprecedented remote working, businesses, institutions and individuals need to efficiently collaborate and communicate together remotely. However it is crucial that we do not sacrifice convenience privacy or security. Our solution, thanks to our unique technology being made public, opens the door to truly private and confidential remote working that is easy to use and open source. Developers can benefit from complex features coming from our SDK like file versioning, synchronization, end-to-end encryption, without having any deep knowledge on this topic. They can focus on the applicative layer of their application : the network layer, the synchronization between devices, the cryptographic layers including the exchange of keys between contacts are all provided by our solution. The management of contacts, workgroups and devices are also made easy. That means, current widely adopted platforms such as Microsoft Teams, Slack, Zoom etc. which are standards to provide efficient collaboration services can be challenged on the privacy aspect, in particular because, services using Keexle's SDK are fully encrypted end-to-end so therefore cannot access user data. The necessities in order to continue the project What we have produced over the course of this weekend Hackathon is just the first step in the Keexle Open Source Project. The ambition is to create an open source and European “App Store” for developers to create their own remote working tools that thanks to Keexle’s unique end-to-end encryption technology will ensure they're completely private and totally secure. Professionals have a legitimate need for privacy. For example, Lawyers, Intellectual Property consultants, Healthcare professionals they can't choose solutions hosted in the public cloud. They have no alternative. The value of your solution(s) after the crisis Online collaboration that keeps data private, safe and confidential is clearly not only valuable during this crisis. The issue of sacrificing privacy for convenience is crucial for businesses, institutions and indeed individuals. The goal of our project for our Keexle ecosystem of apps to become the gold standard for protecting business and individual’s rights to privacy. Our innovative solution can show the world that there is an alternative to the current system, an alternative reality where one does not need to sacrifice one’s right to privacy working remotely. We focus our work on efficient remote working. But our SDK and the marketplace we can provide would be the first one with services that are totally private and secure. We strongly believe that the Keexle Open Source Project can ensure that our privacy does not have to be erroded as we manage our way through this period, and beyond. <div