---
slug: "lucidchart-onprem-for-confluence-server"
url: "https://devpost.com/software/lucidchart-onprem-for-confluence-server"
title: "Lucidchart OnPrem for Confluence Server"
hackathon: "Atlassian Codegeist: Add-on Hackathon"
organization: "Atlassian"
winner: true
words: 619
team_size: 4
has_repo: false
has_live: true
has_video: false
tags:
  - "project"
  - "mechanism/cross_origin_web"
  - "mechanism/realtime_stream"
  - "mechanism/retrieval_grounding"
  - "substrate/document_pdf"
  - "substrate/video_visual"
---

# Lucidchart OnPrem for Confluence Server

> Others are going cloud—we're taking our top web-based add-on to OnPrem with cutting edge functionality in Confluence

[Devpost](https://devpost.com/software/lucidchart-onprem-for-confluence-server) · hackathon [[Atlassian Codegeist- Add-on Hackathon]]

## Facets

**mechanism** [[cross_origin_web]] [[realtime_stream]] [[retrieval_grounding]]
**substrate** [[document_pdf]] [[video_visual]]

**stack** atlassian, aui, confluence, google-closure-compiler, java, javascript, less

## How they structured the write-up

- the story
- inspiration
- why it's special
- how we built it
- challenges we ran into
- what's next for lucidchart onprem for confluence server
- summary

## Body

The story One of the top Confluence & JIRA add-ons, Lucidchart is the leading online provider of diagramming, charting, wireframing, mockup, and now presentation software (all in one application). With over 5 million users worldwide, almost everyone had access to Lucidchart.... except customers that required onpremises storage of their documents. Enter Lucidchart OnPrem for Confluence Cloud . We built Lucidchart OnPrem to provide our cutting edge technology to customers sitting behind firewalls, and also to offer a Paid-by-Atlassian add-on within the marketplace. Inspiration Over 300+ customers have requested an onpremises add-on from Lucidchart. We built this for them, and for all the others who wanted Lucidchart, but were unable to adopt our cloud-based solution. Why it's special While we were not able to replicate all of web-based Lucidchart's functionality (e.g., mobile apps, @mentioning, free integrations, etc.), we still wanted to deliver the premier self-hosted solution for Confluence. Below are a few features that only we are able to offer to customers behind firewalls. Real-time collaboration - multiple editors can diagram together in real-time without overriding each other's edits, enhancing collaboration. Lucidchart OnPrem is the first self-hosted add-on with real-time collaboration In-editor collaboration - comment on shapes, leave feedback, and record next steps within the diagram Presentation-mode - easily create presentations from diagrams for meetings, or embed as slides in pages Visio import / export - high-fidelity Visio import and export Auto-generate diagrams - automatically generate ERDs and other diagrams from source files, like .schema All of these features come in addition to the standard functionality of creating, editing, and embedding diagrams, charts, and visuals to improve communication in Confluence. Lucidchart also includes extensive templates and shape libraries for network diagrams, flowcharts, UML diagrams, UI mockups, Venn diagrams, org charts and more. How we built it We reimplemented some of the back end code of our cloud app within the Confluence environment and tweaked the front end to work with it. In the process we had to make significant changes to core system concepts like users, collaboration, comments, diagrams, and attachments so that they make sense on this new platform. Since this add-on has to work on instances without any internet access, we had to bundle all the necessary resources (js, css, images, fonts, templates, etc.) inside the add-on instead of loading them on-demand from a CDN. Implementing some of our unique features like real-time collaboration was particularly challenging as this is not a feature implemented for Server-based add-ons, and the approach was new to the add-on ecosystem. Challenges we ran into We ran into several major challenges in taking the functionality of our add-on from the cloud to fully onpremises. Among these were challenges enabling real-time collaboration, using an embedded rich viewer within Confluence to create slide shows, and taking our 100% cloud-based functionality into a format that can be used entirely behind a firewall. What's next for Lucidchart OnPrem for Confluence Server We are currently taking the lessons we learned from building Lucidchart OnPrem and applying them to our web-based Lucidchart add-on. These changes will make both products faster, more reliable, and more valuable to our end users. Aside from the business push, we also plan to continue iterating and improving upon the add-on based on customer feedback. For instance, we will be releasing a new version with improved revision history controls shortly. Summary Just like taking a Server-based add-on to the Cloud, taking Lucidchart to the Server was challenging and required many large and small changes to our existing product to deliver an excellent solution for our customers. We hope you'll enjoy testing Lucidchart OnPrem. Feel free to give us your thoughts as we are always working to make our products better, faster, and smarter. Thanks! <div