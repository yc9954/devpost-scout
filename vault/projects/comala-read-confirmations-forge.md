---
slug: "comala-read-confirmations-forge"
url: "https://devpost.com/software/comala-read-confirmations-forge"
title: "Comala Read Confirmations - Forge"
hackathon: "Codegeist 2020"
organization: "Atlassian"
winner: true
words: 725
team_size: 2
has_repo: false
has_live: false
has_video: true
tags:
  - "project"
  - "domain/developer_tools"
  - "user/developer"
  - "substrate/document_pdf"
---

# Comala Read Confirmations - Forge

> Whether you are sharing key pages with team members, or using formal read acknowledgements for compliance purposes, Read Confirmations allows users to confirm they have read a page with just a click

[Devpost](https://devpost.com/software/comala-read-confirmations-forge) · hackathon [[Codegeist 2020]]

## Facets

**domain** [[developer_tools]]
**user** [[developer]]
**substrate** [[document_pdf]]

**stack** ace, confluence, forge, forgeui, node.js, runtimeapi

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for comala read confirmations - forge

## Body

Using a simple on-page macro, assign users to confirm that they have read content. When a team member is assigned, they can acknowledge reading pages by simply pressing the "OK" button. Confluence Cloud creates amazing documents. Make sure the right people see them with Comala Read Confirmations. Use Comala Read Confirmations to make sure the right people have read the right Confluence Cloud documents. You can configure the app to show the elements that your users need to see, like due date, readers, detailed view and confirmation status Inspiration Our users already enjoy Read Confirmations in our Comala Document Management Family of Apps. Comalatech itself has been using Read Confirmations internally as we have been implementing SOC 2 practices. The feature has proven so useful that we wanted to bring it to Confluence Cloud as a stand-alone app in Forge. We are really excited to bring this app for teams of any size in the near future when Forge is widely available for Atlassian products. What it does Assign team members to read Confluence pages, and keep track of who has read them, with Comala Read Confirmations. Users confirm reading with a simple click, and you can request new people to read the document at any time. If the content of the page changes, send out a new request for confirmation from the previous assignees. How we built it Read Confirmations exists as a feature within our existing apps, but there was plenty of work needed to bring it to the Cloud. When Codegeist 2020 was announced, our team kicked into high gear to deliver this app on both the Forge and Connect platforms. In the spirit of innovating and for the team's first challenge we started to play around with the Forge UI, leveraging ContentAction as an entry point for our app and enabling user interaction with the ModalDialogs component. We knew that we wanted to implement the UserPicker to select users from a Confluence instance to read a page, and leveraging the AvatarStack component made it a really easy to pull user account information when the app assigns users to read a page. To our surprise Forge provides developers easy access to UI elements. All though it is still in the early stages we see the potential to interact with all the elements that Confluence allows for Connect apps. Challenges we ran into The first challenge was getting our Cloud team up to speed on the Forge platform. Thankfully the platform is very developer friendly, so soon we were able to focus on the development challenges ahead of us. When we did run into some issues with Forge, Atlassian's team was incredibly responsive in helping us resolve the problems through the Slack groups they setup for the hackathon. They made it really easy to follow up on the issues through a Jira board. Accomplishments that we're proud of We're very pleased to be among the first Marketplace Vendors to release a Forge app. We're big believers in Atlassian's Cloud vision, and Forge is a huge milestone in moving the ecosystem in that direction. What we learned Building a FaaS is not an easy task and Atlassian is making an incredible effort to launch a developer friendly environment where teams/organizations can create solutions on top of Atlassian's top products. Was surprised to know that in order for us to develop on Forge we needed both Jira and Confluence active on an instance - mental note: read the docs :P Support is critical in the first 3 days when you start building on a brand new platform, here is where we really put the pressure on Atlassian and they manage to deliver an excellent level of attention to all the information we provided and did a great follow up - kudos to the Forge team! Being open to not having all the answers let's you and your team make quick decisions to move forward in building software. This is what hackathon's all about...so plenty of fun during the days prior to submitting this app What's next for Comala Read Confirmations - Forge We're not stopping here with Read Confirmations. We have plans to release additional features for the app, and we've also discussed integrating it with our Comala Document Control app. The future should be exciting for both Confluence Cloud and Comala Read Confirmations! <div