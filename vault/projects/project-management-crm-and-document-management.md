---
slug: "project-management-crm-and-document-management"
url: "https://devpost.com/software/project-management-crm-and-document-management"
title: "Project Management, CRM and Document Management"
hackathon: "Quick Base Virtual Hackathon"
organization: "Quickbase"
winner: true
words: 629
team_size: 2
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "substrate/document_pdf"
---

# Project Management, CRM and Document Management

> App tracks Opportunities which convert to Projects, tracks counterparties and key project details. Manages documents, uploads to Box and serves links to all counterparties.

[Devpost](https://devpost.com/software/project-management-crm-and-document-management) · hackathon [[Quick Base Virtual Hackathon]]

## Facets

**substrate** [[document_pdf]]
  <sub>weak: structured_db</sub>

**stack** api, box, pipelines, powerbi, quickbase, workato

## Body

SolarTracker Home Dashboard The API linked Box environment with fully templatized folder structure We endeavored to create a flexible and robust project management solution that could help internal users track all required deliverables with workflow automation and notifications and provide similar functionality to all of the external 3rd parties involved in a project and serve them all of the required documents and tasks to keep things on track and meet critical deadlines. ProjectTracker keeps your internal functional teams on task and updated on all critical project data. It also serves all required data and documents to outside counterparties dynamically with the simple click of a checkbox. This eliminates the need for numerous external datarooms and duplication of documents. As all Opportunities, Projects, Entities and Closings are created in Quickbase, a templatized folder structure is created in Box and linked to the triggering record. Document templates for each of these document owners are pre-configured in the Documents table and as Documents are uploaded, they are automatically placed in their correct folder location and named formulaically. Links to these documents are written back into Quickbase and served to all of the outside counterparties with a maintainable permission structure that will only serve a counterparty the exact documents they should see and only when you make that visibility active. We tried to leverage native Quickbase functionality wherever possible with extensive use of Automations, Pipelines and API integration managed by Workato for document management between Quickbase and Box. We then connected all required fields to a Power BI dataset and built out robust cross-table reporting which we embedded in the Home page and leveraged for reporting needs in addition to the Quickbase Notifications feature. Each table has Dynamic Form Rules to control visibility, and trigger workflows with Automations and Pipelines. While we had great success leveraging the Pipelines native functionality within Quickbase for our API integrations with Box, we did run into limits with the tool around Box Sharing actions. We had to build out the more complex functions in Workato to compliment what we achieved in Pipelines. We also leveraged Power BI for unified reporting as we have found the lack of executive reporting in Quickbase to be challenging for some organizations, however we are very excited for the new features that are coming to Quickbase soon! The deep permission model from Contacts > Companies > the locations those Companies are listed on Projects and Closings and then the relationship of those document parents down to their associated documents that dynamically controls document by document access with a simple click of a checkbox on the Closing record is our favorite and most complex part of the app. Serving Deliverables to counterparties in a timely manner and assuring that all parties are served the most up-to-date documents is a challenge for any organization and we feel we have solved the challenge in an elegant and maintainable solution. We learned a ton about the growing functionality of Pipelines and really appreciate the features being developed there. We found simple and scalable approaches for creating document templates with an extensive amount of pre-populated metadata and simple ways to populate those templates to their parents with the push of a button on the Projects table that triggers multiple API calls so everything happens seamlessly on the backend for a one-click user experience. We plan to bring a lot of what we learned and efficiencies we created back into the core Quickbase apps that our entire company utilizes to conduct all of our day-to-day business. This app was just created as a demo but we will certainly be able to leverage many of the features in our own tools. We are hoping to learn through the other submissions as well and grow through the entire experience! <div