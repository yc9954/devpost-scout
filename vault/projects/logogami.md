---
slug: "logogami"
url: "https://devpost.com/software/logogami"
title: "Logogami"
hackathon: "Atlas Madness"
organization: "Google"
winner: true
words: 413
team_size: 2
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/on_device_local"
  - "mechanism/realtime_stream"
  - "mechanism/runtime_tool_creation"
  - "substrate/video_visual"
  - "substrate/web_dom"
---

# Logogami

> An SVG spec to manage your brand logo in one elegant optimized dynamic asset, in the cloud.

[Devpost](https://devpost.com/software/logogami) · hackathon [[Atlas Madness]]

## Facets

**mechanism** [[on_device_local]] [[realtime_stream]] [[runtime_tool_creation]]
**substrate** [[video_visual]] [[web_dom]]

**stack** cloudrun, mongodb, realm, sveltekit

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for logogami
- google architecture diagram
- public git repo
- youtube demo
- logogami.com

## Body

Diagram Inspiration Pain Point Brand and logo asset management. Unless an organization had a dedicated marketing design team in complete control of all branded materials, it's difficult to keep the correct logo asset in everybody's hand. Solution Dynamic, efficient SVG in the cloud. SVG can now be rendered consistently and reliably across all uses. It's now more portable than EPS, and more practical than any raster format. We've come up with a dynamic and management SVG logo spec, taking full advantage of re-using Symbols with CSS variables, that allows storing multiple variations and themed versions of a logo in one optimized SVG file. By dynamically managing this SVG logo from MongoDB and centralizing in the Cloud , this one logo is delivered anywhere it is needed. Dynamic means the owner is in control in real time. Dark, Pride, and Holiday themed variations of the logo can be efficiently included and set as the primary facing logo as wanted. What it does The Logogami app allows a user to login using MongoDB App Services and manage their logos. Logo data is stored in MongoDB. It is processed using the Logogami SVG spec to a single SVG file, which is hosted on Cloud CDN or accessed directly on a Brand Guide webpage. How we built it MongoDB Atlas is the data backend, with App Services for user identity. The app frontend is coded in SvelteKit . The app is hosted on Google Cloud Run , with Docker and related CD tools. Cloud CDN is used to deliver final assets. Challenges we ran into There are two basic technical limitations holding back full use case potential: Problem: E-mails still have bad SVG support. Logogami is perfect for creating email signatures, but email clients don't like SVGs. Solution: Also has dynamically generated raster version of the logo for email signatures. Problem: Cross-domain blocking of svg use tags prevent using directly from CDN. Solution: Download the SVG locally. A code snippet to javascript fetch() the logogami SVG directly from the CDN and put it inline. Accomplishments that we're proud of The overall implementation is a perfect fit for MongoDB. The SVG design spec is very elegant. What we learned We learnt a lot about SVG optimization, CDN architecture. What's next for Logogami Continued development of the app. More derived assets. Print color management. CMS integration. Dynamic creation of marketing material, social media images, etc. Google Architecture Diagram https://googlecloudcheatsheet.withgoogle.com/architecture?link=c0601c40-1f46-11ee-9f8f-290d07fabc7d Public GIT Repo https://bitbucket.org/makeitTim/logogami-public/src/main/ YouTube Demo https://youtu.be/tAh767xy-YY Logogami.com https://logogami.com <div