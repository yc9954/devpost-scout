---
slug: "social-pro"
url: "https://devpost.com/software/social-pro"
title: "Social Pro"
hackathon: "The Postman API Hack"
organization: "Postman"
winner: true
words: 315
team_size: 2
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/simulation_digital_twin"
  - "domain/developer_tools"
  - "user/developer"
  - "user/general_public"
---

# Social Pro

> A collection for social media managers and individuals to post to multiple social media channels simultaneously. Saves time, keeps the message consistent, meet time sensitivity needs

[Devpost](https://devpost.com/software/social-pro) · hackathon [[The Postman API Hack]]

## Facets

**mechanism** [[simulation_digital_twin]]
**domain** [[developer_tools]]
**user** [[developer]] [[general_public]]

**stack** imgur, postman, twitter, youtube

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for social pro

## Body

One API collection to interact with all Social platforms Inspiration We are inspired by platforms such as Hubspot and Hootsuite which have rich feature set and can interact with multiple social media platforms. Beneath the rich UIs and feature sets, these platforms are a collection of API Requests that interact with others. So we wanted to put our Postman skills to mimic the capabilities of Hubspot and Hootsuite. What it does Our API collections AKA Social Pro gather media content in different formats. It selects a target platform like Youtube, Twitter or Imgur. It uploads the content to the target platform. How we built it We have used the public APIs provided by Twitter, Imgur and Youtube to build a collection of requests in Postman, Our API collection authenticates with these platforms and then uploads the content. Challenges we ran into This is more of diversity problem which is expected. Each platform had it's own protocol or version for authentication. So we had to build the collection to work with different authentication mechanisms. These platforms may or may not accept all media types. So based on the platform we need to select the media format. E.g. Youtube is for videos only. Accomplishments that we're proud of We started off really late on this journey. However, we were able to quickly scale and include three platfoms. Postman is a relatively new tool for us and we manged to create an MVP. What we learned With a decent level of knowledge and by investing on a one time development cycle, one can simulate licnsed tools and use them with relative ease. Postman's rich capabilities for collaboration, documentation and simulation help achieve complex requirements in a short amount of time. What's next for Social Pro Integrate more social platforms Integrate Dropbox API to gather the media files Publish this as an manageable, reusable collection for developer community <div