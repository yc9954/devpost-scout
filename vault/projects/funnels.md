---
slug: "funnels"
url: "https://devpost.com/software/funnels"
title: "Funnels"
hackathon: "monday.com Apps Marketplace Challenge: solutions for teams "
organization: "Monday.com"
winner: true
words: 445
team_size: 1
has_repo: false
has_live: false
has_video: true
tags:
  - "project"
  - "domain/developer_tools"
  - "substrate/geospatial"
  - "substrate/video_visual"
---

# Funnels

> Marketing and sales funnel visualisation. Tree / journey graphs for in-depth analysis of status transitions.

[Devpost](https://devpost.com/software/funnels) · hackathon [[monday.com Apps Marketplace Challenge- solutions for teams]]

## Facets

**domain** [[developer_tools]]
**substrate** [[geospatial]] [[video_visual]]

**stack** react

## How they structured the write-up

- inspiration
- what it does
- how i built it
- challenges i ran into
- accomplishments that i'm proud of
- what i learned
- what's next for funnels

## Body

Funnels for sales and marketing Tree view with View Settings Tree view tooltip Tree view / dark mode Funnel view, selected node, tooltip Funnel view with tooltip Inspiration Conversation with folks at Omnitas Consulting about how their customers use Monday.com. Development of this app was driven mostly by their feedback and the needs of clients using Monday.com as CRM system. Thomas and Fredrik from Omnitas Consulting kindly offered to provide their commentary on how this app can be used. You can view them in the presentation video. (BTW: I added English subtitles, so just turn them on in youtube settings should you need them) Also, I like pretty UIs and funnels was an opportunity to create something good looking and useful at the same time. What it does Funnels visualise sales or marketing funnels. It can also draw diagrams of transitions between states, which is useful when tracking efficiency of workflows and sales processes (e.g. check what route most of the leads take from initial contact to closing the deal). We call that chart "Tree" or "Journey". How I built it I used React on top of monday.com SDK. Charts are drawn with lovingly handcrafted SVG. Challenges I ran into calculation of formulas from monday.com boards. There's no API to get actual values for formula columns, so I had to employ third party parser and imitate behaviour seen in the boards. Apologies in advance if calculations behave differently than in Monday.com processed formulas, but it's difficult to handle special cases for different types of columns etc. drawing charts for weird data in such a way that it looks good and readable. Example of this is very large and very small values on the same chart. Tree / journey diagram can contain very large and small nodes which at first resulted in huge images with very fine, unreadable details. I had to scale values in a smart way to preserve relative sizes, but never draw too big or too small elements. sanitisation of values - handling of edge cases, zero weights, negative weights etc. Accomplishments that I'm proud of Looks like this is a product solving a very real need of large community of Monday.com users using it primarily as CRM system. It's been tested with real users who confirmed usability and usefulness. I also like how it looks. What I learned I learned some use cases of Monday.com by speaking to power users. Technically, the biggest learning is probably details of SVG as I had to create some elaborate algorithms to draw pretty curves in the charts. What's next for Funnels Documentation, more testing and squashing bugs, submission for review and listing on Marketplace. <div