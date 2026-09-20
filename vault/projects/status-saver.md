---
slug: "status-saver"
url: "https://devpost.com/software/status-saver"
title: "Status Saver"
hackathon: "Codegeist 2022"
organization: "Atlassian"
winner: true
words: 528
team_size: 5
has_repo: false
has_live: false
has_video: true
tags:
  - "project"
  - "domain/developer_tools"
  - "user/developer"
  - "substrate/document_pdf"
---

# Status Saver

> Improving Confluence's Content Status experience. Easily edit and save statuses in view mode, identify current page statuses from the page tree, and view page states report to determine action items.

[Devpost](https://devpost.com/software/status-saver) · hackathon [[Codegeist 2022]]

## Facets

**domain** [[developer_tools]]
**user** [[developer]]
**substrate** [[document_pdf]]

**stack** forge, javascript, react, typescript

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what's next for status saver

## Body

Byline and dialog where the activity is displayed and the user can insert a comment to change the status General view of a space using Status Saver, the status of the page is displayed and identified from the page tree Left side bar space report of all pages using a status Space report page macro, can be included in any page, for example the home page Inspiration This past June, Atlassian released Page Status, a new feature for Confluence Cloud that allows users to assign statuses to their content. The inspiration comes from mixing our document management expertise and the Content Status. We identified some key functionalities that improve the user experience and will cover more use-cases. What it does Status Saver improves Confluence's Content Status experience, allows users to easily view page statuses, edit and save statuses adding a comment while in view mode, record and access most recent status updates, and identify current page statuses from the page tree. For example, Status Saver enables you to build a basic QMS system that shows document stages from Draft to Published, letting stakeholders know if it’s ready for review, has been published or rejected, or if you’ve just started working on it. This information can be used for quality standard requirements, while increased visibility keeps teams connected, informed, and productive. How we built it First, our most experienced Forge developer let us know what we can do and what we can not using the Forge framework. Based on his knowledge, we adapted the app scope. Then, we assembled a seasoned and cross-functional team to be dedicated to the project: 1 frontender, 1 backender, 1 QA, 1 product marketing manager and 1 product manager. Status Saver is technically a full Forge app. Even the whole UI has been built using only the Forge UI Kit and the data associated with the status activity is stored using the Forge Storage api. Challenges we ran into There are two ways to change the Content Status with Status Saver: using the byline or the Confluence button in edit mode. However, we wanted to record any status change activity. We needed to create a listener for any confluence update page event and properly save the information associated with the status change. We discovered that Confluence Cloud allows you to save a page content property to store an emoji, so to show the current status from the page tree, we were able to add an emoji at the beginning of the page title without modifying the title. Finally, we tried but we weren't able to refresh the page after changing the status so the user needs to manually refresh it to view the status changes. Accomplishments that we're proud of We are really proud of implementing a really cool app that can cover multiple use-cases built entirely in Forge. We have all learned more about Confluence Cloud functionalities. What's next for Status Saver We believe there are endless ways Status Saver can be used and there are several great ideas that we could implement. We are confident it will bring clarity to Confluence users across the board! Thanks for checking out our app! <div