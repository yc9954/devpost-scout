---
slug: "zoom-recordings-for-confluence"
url: "https://devpost.com/software/zoom-recordings-for-confluence"
title: "Zoom Recordings+ for Confluence"
hackathon: "Codegeist 2020"
organization: "Atlassian"
winner: true
words: 702
team_size: 1
has_repo: false
has_live: true
has_video: false
tags:
  - "project"
  - "mechanism/cross_origin_web"
  - "domain/developer_tools"
  - "domain/labor_employment"
  - "user/developer"
  - "substrate/structured_db"
  - "substrate/web_dom"
---

# Zoom Recordings+ for Confluence

> Add, display, search and watch Zoom cloud recordings directly within Confluence.

[Devpost](https://devpost.com/software/zoom-recordings-for-confluence) · hackathon [[Codegeist 2020]]

## Facets

**mechanism** [[cross_origin_web]]
**domain** [[developer_tools]] [[labor_employment]]
**user** [[developer]]
**substrate** [[structured_db]] [[web_dom]]

**stack** atlaskit, cloudflare, react, zoom

## How they structured the write-up

- inspiration
- what it does
- how i built it
- challenges i ran into
- accomplishments that i'm proud of
- what i learned
- what's next for zoom recordings+ for confluence

## Body

Try it now: https://marketplace.atlassian.com/apps/1223133/zoom-recordings-for-confluence Inspiration With so many people now working from home or remote, asynchronous Zoom recordings have become a key team communication tool for many businesses. But sharing recordings among team members is quite a mess: Cloud recordings are limited to Pro accounts. To save costs most companies will have only a few employees with paid Zoom accounts which results in siloed recordings. No central location to access relevant recordings. The current workaround is to bulk forward emails with recording links or manually copy URLs into a shared spreadsheet. Recordings are password protected by default. When this setting is left on it requires finding the recording owner who then needs to search their emails for the password. What it does It's a macro that allows teams to collaboratively add, edit, display, search, sort and watch any Zoom cloud recordings without leaving Confluence. Some features: Connect with Zoom Oauth to fetch and add recordings from your Zoom account. Manually add non-password protected Zoom recording links. Edit recording topics instead of the default eg "Nathan Waters' Zoom Meeting". Add a password for password-protected recordings (easy access via iframe popup). Display thumbnails in three layouts: table, grid and list. Search, pagination and sort by date, topic or length. Recordings open into a dialog popup with a video player. Pasting a Zoom recording link into Confluence editor auto-converts to video player. No data leaves the Confluence instance (it's all within content properties). How I built it React and Atlaskit with code splitting. Confluence content properties. Serverless Cloudflare Worker for backend API. Zoom API and Oauth (awaiting app approval). HTML5 video component. Static build deployed to Netlify. Challenges I ran into There are many hacks involved in making this work: Dealing with potentially sensitive recording material I didn't want to do any external storage. However the key-value Confluence content properties are limited to 32KB chunks. So I built and tested a helper function to split data into 32KB max chunks and run a loop to get/set content properties. Would be good if that chunking was handled by the getContentProperty() and setContentProperty() functions. There were also some useful features (eg auto-add, password bypass) I had to drop because I didn't want to store Zoom access/refresh tokens externally or in content properties. Secure storage of 3rd-party access tokens within Confluence would be a neat option. Please change CONFCLOUD-62377 from a suggestion to a bug. My workaround hack for that was to use URL query parameters and a timestamp in the saveMacro data. The Zoom API is severely limited. Zoom requires all interactions happen server-side, the /recordings response doesn't return any thumbnails, or any video embed code and doesn't say which recordings are password protected. Not even in the official Zoom account dashboard do you see thumbnails for recordings. Through trial and error I discovered the returned download_url works within a HTML5 video element. So the thumbnails you see in my app are video elements skipped to 1 second in and with all controls/interactions disabled. The manual-add link feature is using a Cloudflare Worker to fetch the HTML and extract hidden input elements with the topic, date and duration details. It does the same to check if a recording is password protected. Accomplishments that I'm proud of Solving the challenges above piece by piece and putting the work in to get this project over the finish line. I'm a solo dev and for this app it's taken 7 days per week, ~10-12 hours per day for the past ~3 weeks. #codelife What I learned I finally made the switch to React Hooks with this app so learned a lot there (I still prefer Svelte over React). More in love with Cloudflare Workers than I was before. I built a custom API using tiny-request router. Found a few bugs and limits in the Atlassian developer platform. I figure you're running this hackathon for two reasons: more apps and to improve the DX. So hopefully some of my feedback is useful :) What's next for Zoom Recordings+ for Confluence Awaiting app approval from Zoom. Until then the Oauth connect only works for my account. Submit the app for approval on the Atlassian marketplace. Iterate based on feedback from customers. <div