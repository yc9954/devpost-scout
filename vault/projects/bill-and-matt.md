---
slug: "bill-and-matt"
url: "https://devpost.com/software/bill-and-matt"
title: "Bill and Matt"
hackathon: "monday.com Apps Marketplace Challenge: solutions for teams "
organization: "Monday.com"
winner: true
words: 792
team_size: 1
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "user/general_public"
---

# Bill and Matt

> Invite our in-house experts on your monday boards to effectively automate, communicate and streamline repetitive tasks of executing a construction projects. Comes with companion exporters and web app.

[Devpost](https://devpost.com/software/bill-and-matt) · hackathon [[monday.com Apps Marketplace Challenge- solutions for teams]]

## Facets

  <sub>weak: cross_origin_web</sub>
  <sub>weak: labor_employment</sub>
**user** [[general_public]]

**stack** c#, dotnet, javascript, node.js, revit, xaml

## How they structured the write-up

- inspiration
- what it does
- how i built it
- features included
- challenges i ran into
- accomplishments that i'm proud of
- useful links
- what i learned
- what's next for bill and matt

## Body

On site workers can send updates directly to your monday board App view for vendors to view requirements and details Companion app which runs on any device makes sharing easier Notify vendors automatically on changes to your requirements Share updates and files to everyone from one place keeping communication simple and effective Invite and compare quotes for your requirements from different vendors An inline 3D interactive viewer helps you contextualize information Use QR codes to track your materials across the physical realm Material information copied to monday board with a single click Channel all conversations to your monday board and keep it together One click revit exporter to transfer your information to monday boards Select schedules you want to sync with your monday board. Main Page Inspiration Executing a construction project was the most tedious task when I worked as an architect. The same situation is faced by almost everyone in the architecture, engineering and construction(AEC) industry. It's not the task itself but gathering and communicating disparate information between all stakeholders of a project that becomes cumbersome. A lot of the tasks are also pretty repetitive. eg: extract information from design files, send it to vendors for getting their quotes, informing vendors of changes to material quantities, comparing quotes from different vendors etc. Monday.com seemed like a perfect fit to automate and improve the workflows in this process. What it does It takes your material and qunatity data from Autodesk Revit - the most popular Building Information Platform used in the AEC industry - and sends it over to a monday.com board connected to your account. From here you can take control of different aspects of ensuring timely delivery of these materials. An inline 3D view in your monday.com board shows you the information about your materials and quantities in an interactive view. Something even Revit does not allow you to do. Use monday.com integrations to invite bids for your quantities. It makes the task really simple as the platform can smartly connect information across different places and allows meaningful automation of mundane tasks. Connects your information in the monday environment with a custom built progressive web app which can run on any device. It becomes easy to share information with external contractors and vendors with the convenience of simply updating monday boards. Helps you track items that are needed virtually and with physical markers to make sure there is no material wastage and timelines are running on track. Simplifies all of the above process when project specifics and quantities change midway. How I built it Revit exporter is made with Windows Presentation Forms and works with the RevitAPI to extract material information and geometry. Everything else is Javascript running either in the browser or on a server. Vue along with Vuetify acts as the front end framework and the public app makes it run like a native app on any design using Progressive Web App specs. Features included Revit exporter Plugin to export schedule information from Revit to monday.com boards. Web App https://bill-and-mat.herokuapp.com Companion web app which links with user's monday.com boards to share information with external teams. Model View - monday.com Board View An interactive 3D explorer for your AEC projects. View models within your board to locate schedule items and share with your team for effective communication. Model View - monday.com Vendors View View information on vendors assigned to contact for quotes on items and their delivery schedule. Submitted quotes can be easily compared and purchase orders dispatched from this view. Notify Schedule Changes - monday.com Integration Notifies your vendors about changes to schedule items. Sync from your Revit projects after design changes to trigger this integration and automatically notify your vendors. QR Code - monday.com Item View Item view to display QR code for item. Use it like a bar code for your item to track it throughout the life-cycle of the line-item for the duration of the project. Challenges I ran into Getting the 3D viewer to work in a friendly way turned out to be a daunting task. Accomplishments that I'm proud of The UX portion turned out really great where I personify the features as two characters who help the user out. Useful Links Install revit plugin Export from Revit How use monday 3d model viewer How to setup vendor communication automations How to use vendor boardview to compare quotes How to use issue purchase orders from monday board How to use item tracking and monday board communication What I learned Lots of takeaways here. Working across 2 different languages and programming environments was an interesting challenge. What's next for Bill and Matt I would like to build more integrations and add features for automated change detection. Set it up on a custom domain. <div