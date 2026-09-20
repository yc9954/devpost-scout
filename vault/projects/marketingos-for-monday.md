---
slug: "marketingos-for-monday"
url: "https://devpost.com/software/marketingos-for-monday"
title: "MarketingOS for Monday"
hackathon: "monday apps challenge"
organization: "Monday.com"
winner: true
words: 692
team_size: 1
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/revocation_withdrawal"
  - "substrate/document_pdf"
  - "substrate/web_dom"
---

# MarketingOS for Monday

> We built a "Marketing OS" for Monday.com's Work OS.Create & manage full multi-channel campaigns from Monday.Supports SMS, Email, WhatsApp, ad-targeting (Google/Facebook, etc) and even postcards.

[Devpost](https://devpost.com/software/marketingos-for-monday) · hackathon [[monday apps challenge]]

## Facets

**mechanism** [[revocation_withdrawal]]
**substrate** [[document_pdf]] [[web_dom]]

**stack** angular.js, facebook-ads, google-adwords, google-cloud-functions, lob, mongodb, node.js, pupeteer, stanpp, twilio, whatsapp

## How they structured the write-up

- project site
- docs
- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for marketingos for monday

## Body

Use our integration recipies to put all your sends on autopilot Link-merge gives every contact their own unique short-URL so you can see who clicked Use any column as a field-merge Built-in testing with any record, for any channel Monitor and analyse your campaigns with our dashboard widgets Target ads to selected records across Facebook, Messenger, Instagram WhatsApp, Google, YouTube, etc. Send on 4 channels + target ads on 2 channels Project Site https://monday.instant.marketing Docs We've added a full docs site: https://monday.instant.marketing/docs/latest Inspiration I was actually inspired by the "Work OS" slogan of Monday. What if we added a "Marketing OS" as well? That sounds powerful..! As a consultant I've worked on marketing technology for big companies. But operating&integrating a marketing tool is hard . What if we took all the functionality & features of expensive stand-alone marketing software, and built the entire thing from scratch around Monday.com? What it does Create & run entire multi-channel marketing campaigns from inside Monday.com -- without any external software. It's a full Marketing system built around Monday.com. You add the marketing view, select your records (filters are supported) - and a wizard lets you create & send a campaign. We support SMS, Email, Postcards, ad-targeting (Google/Facebook, etc.) and WhatsApp messages. After sending - monitor it with the 2 dashboard widgets, and automate it with our set of integration recipies. How we built it We use Angular because we're more familiar. This meant re-implementing a lot of your React components from-scratch in Angular. The backend is NodeJS. Challenges we ran into The sheer scope. The number of channels, integrations and features. Delivering so much (a feature complete marketing-system with 6 channels, field-merges, A:B testing, reporting & automations) without feeling complex. This took a lot of design iteration. Every PDF-rendering API we tried was too low resolution for the postcards (they looked blurry when they arrived from the printer). So we had to build our own PDF-rendering service which supports super-high resolution. Getting an elegant field-merge! I wanted this to function like a token (delete as one, cursor skips over it as one, seamlessly upgrade any text-field). This field-merge UI alone was maybe 100hours. Fitting everything into a 2 minute video with so many channels, features. (We could easily do 2 mins just on postcards -- for example.) So we did a dedicated website , and a docs site too With so many integrations, we had to elegantly handle so many possible error paths (expired token, missing configuration, etc.) Accomplishments that we're proud of The field-merge system was very technically complex! Designing an entire marketing system to fit into a wizard/overlay. There's a LOT of design work to remove the need for a stand-alone marketing tool. Automatic URL-shortening means we can run A:B tests. It's a small detail - but when you select a channel, there's an animation I really like in the left plane. I was able to get it just so. What we learned If I was doing this again I would definitely do a smaller project. The scope of this ended up maybe 5 times+ larger than any other Monday app I'm aware of. Print-ready PDF rendering. We tried commercial PDF APIs and they couldn't handle the resolution needed for commercial postcard printers (our first samples were blurry). So we eventually had to build our own PDF rendering service to do super high resolution. This was a whole bunch of new skills. Building an icon font: because we use Angular not React - we had to build the Monday icons into an icon-font ourselves. I learned a bit about how SVGs and icon-fonts work. Implementing the design system I think helped me improve as a designer. What's next for MarketingOS for Monday I love Monday's integration recipies - so adding a bunch more of those makes sense. (We are testing triggering automations when somebody clicks/opens/replies: e.g. "when a record clicks {message} - do {something}" I think fully integrating 2-way marketing with the Monday integration recipies has a lot of potential. E.g. SMS to tell everyone about their shift update, and automation when somebody responds "OK" -- or doesn't respond in a given time. <div