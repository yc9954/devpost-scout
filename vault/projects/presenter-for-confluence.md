---
slug: "presenter-for-confluence"
url: "https://devpost.com/software/presenter-for-confluence"
title: "Presenter for Confluence"
hackathon: "Atlassian Codegeist: Add-on Hackathon"
organization: "Atlassian"
winner: true
words: 295
team_size: 1
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/cross_origin_web"
  - "domain/developer_tools"
  - "substrate/web_dom"
---

# Presenter for Confluence

> Present any Confluence page effortlessly and directly in your Browser

[Devpost](https://devpost.com/software/presenter-for-confluence) · hackathon [[Atlassian Codegeist- Add-on Hackathon]]

## Facets

**mechanism** [[cross_origin_web]]
**domain** [[developer_tools]]
**substrate** [[web_dom]]

**stack** atlassian-connect, atlassian-plugin-sdk, java, javascript, jquery, php, reveal.js, symfony

## How they structured the write-up

- what it does
- how i built it
- challenges i ran into
- what's next for presenter for confluence

## Body

What it does Presenter for Confluence turns any Confluence page into a beautiful, clean and hassle-free slideshow – directly in your browser. Literally all you need to do is hit the 'present' button and you are good to go. Spend more time focussing on content rather than struggling with inconvenient presentation software and separate files that need to be separately updated. The slides created by Presenter for Confluence are responsive and will look good on any screen. Discuss pages with your team or show them to clients without any distracting UI elements, taking advantage of the entire real estate of your screen. You can easily navigate through every single chapter using either keyboard or mouse. Simplify your workflow. Start using Presenter for Confluence. Try a live Demonstration in Confluence Cloud How I built it I started out building it as a traditional Plugin SDK add-on, because as a result of data protection laws we have to host all of our Atlassian software on private servers at my company. When the product was more or less finished, we decided that it would be great to also support cloud instances and therefore developed an Atlassian Connect version with a Symfony backend. I used Hakim El Hattab's great reveal.js for displaying the presentation and jQuery to parse the Confluence page's DOM into a great looking presentation. Challenges I ran into The most difficult thing was trying parse every possible Confluence page in such a way that it still looks good as a presentation. Also learning two very different plugin architectures from the ground up was quite an interesting challenge. What's next for Presenter for Confluence The add-on is now available on the Atlassian Marketplace and we look forward to hearing from our customers for feedback and suggestions. <div