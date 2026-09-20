---
slug: "instant-websites-for-confluence"
url: "https://devpost.com/software/instant-websites-for-confluence"
title: "Instant Websites for Confluence"
hackathon: "Atlassian Codegeist: Add-on Hackathon"
organization: "Atlassian"
winner: true
words: 366
team_size: 1
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "user/general_public"
  - "substrate/geospatial"
  - "substrate/web_dom"
---

# Instant Websites for Confluence

> Collaborate on Confluence then publish to super fast Amazon AWS for public access and pretty URLs

[Devpost](https://devpost.com/software/instant-websites-for-confluence) · hackathon [[Atlassian Codegeist- Add-on Hackathon]]

## Facets

**user** [[general_public]]
**substrate** [[geospatial]] [[web_dom]]

**stack** amazon-web-services, atlassian, javascript, metalsmith, node.js

## How they structured the write-up

- inspiration
- what it does
- how i built it
- challenges i ran into
- accomplishments that i'm proud of
- what's next for instant websites for confluence

## Body

Inspiration There is no better place to collaborate and create great content than Confluence. I wanted to use Confluence for internal company work and also for creating and updating the public company website and product documentation. Using Confluence for both means the team has one tool to learn, a great content editor, comments and collaboration, and all the other goodies Confluence provides. While I could point customers to a Confluence Cloud instance I wanted a super fast and responsive website so customers get what they are looking for as quickly as possible, making them happier. I also wanted pretty URLs ( https://arijea.com/ vs https://arijea.atlassian.net/ , for example). Bringing these things together led to the creation of Instant Websites for Confluence. What it does Instant Websites is an Atlassian Connect add-on that integrates with Confluence Cloud. It is installed by a System Administrator and enabled for a Confluence space by a Space Administrator. Instant Websites assists with publishing a Confluence space to a mobile responsive and static website on Amazon AWS S3. First it converts the Confluence storage format to a static HTML site using Metalsmith. That is then published to Amazon AWS S3. This content is, in turn, delivered via Amazon AWS CloudFront ensuring that the customer gets the content as quickly as possible, wherever they are in the world. Finally Amazon AWS Route 53 enables the customer to CNAME a vanity URL ( http://arijea.com/ ) to Amazon AWS, hiding the Amazon URL from the customer. Ultimately the customer gets the company website and documentation in a mobile responsive format as quick as possible. How I built it Node.js service that connects to Confluence via Atlassian Connect. That service tracks content changes in a Confluence Space and when it detects a change it converts the raw storage to static HTML using metalsmith ( http://www.metalsmith.io/ ). That content is then published to Amazon. Challenges I ran into Conversion and rewriting Confluence CSS and content to be suitable for a static website is the biggest challenge. Accomplishments that I'm proud of It works and we've got beta customers lining up! What's next for Instant Websites for Confluence More themes and an easier on-boarding experience for Space Administrators. <div