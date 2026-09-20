---
slug: "goshare-me"
url: "https://devpost.com/software/goshare-me"
title: "linksof.fun"
hackathon: "The Postman API Hack"
organization: "Postman"
winner: true
words: 766
team_size: 1
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "domain/developer_tools"
  - "user/developer"
  - "user/researcher"
  - "substrate/document_pdf"
  - "substrate/web_dom"
---

# linksof.fun

> If you build something and no one knows about it, then does it really exist ;)

[Devpost](https://devpost.com/software/goshare-me) · hackathon [[The Postman API Hack]]

## Facets

**domain** [[developer_tools]]
**user** [[developer]] [[researcher]]
**substrate** [[document_pdf]] [[web_dom]]

**stack** firebase, google-analytics, postman

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for linksof.fun

## Body

Demo web app for the custom URL shortening service. Analytics dashboard to measure which pages are popular. Automagical API documentation and code snippets. Postman collection to organize all requests. Inspiration I have been thinking about brand identities a lot lately. How some brands will revolve their creative marketing material around a theme like outer space or fantasy realms. But too often creators don't think about the links their customers will share from within their apps. For example, apps will have a social media share button within their apps for their customers to share some content but it has a ridiculously long link that just makes their message look busy. Linksof.fun wants to change that!! It allows developers to quickly setup a custom short URL shortening service and then use Postman to generate code snippets to integrate into their apps. With linksof.fun, developers also have a choice of what web analytics service they want to use so the data analyst on the team doesn't have to jump around between different services. What it does Linksof.fun takes any URL and returns a short link that is both easier to remember and can fit more naturally on mediums like SMS or Twitter. Brands can now purchase a domain name that fits closer to their main URL that is used to help share their message. For example let's say brandname.com is the main domain owned by the brand, they can purchase something like brandna.me to use for their URL shortening service. So when they want to share a link such as brandname.com/folder-name-1/folder-name-2/?utm_source=newsletter&utm_medium=sms&utm_campaign=spring_sale , they can instead share brandna.me/3Or9OyJpghCwLpVoeR9J which can fit easier on mediums like SMS. Linksof.fun also allows for vanity URL endings. For example, brandna.me/github both redirects to a desired page and is fairly easy for customers to remember. But the power of linksof.fun really comes through when you use Postman to generate new short URLs. By using Postman, developers can easily generate code samples for various languages such as JavaScript and Swift. With linksof.fun, every business can have their own URL shortening service, use whatever web analytics service they would like, and have an amazing vanity URL to help conform to their brand. How we built it Firebase Functions, Hosting, and Firestore are the main components on the backend. Google Analytics is currently being used for analytics tracking but can easily be replaced with a different service. Postman Collections helped organize the various API requests. Postman Code Snippets was instrumental to building the front-end code and will likely be used in the future to build integrations into future apps. Postman Environments was used to help organize the various requests so that a single generic collection can be used for multiple URL shortening services. Postman Monitors is used to help determine the health of the linksof.fun URL shortening service. Postman Documents is used to help give notes for the overall collection as well as getting the code snippets to make the requests in the application. Challenges we ran into I considered using Next.js for my front end but decided to go with vanilla JavaScript. The main reason for that is because I wanted to make sure my short URLs were as fast as possible so I didn't want anything on those pages that didn't absolutely need to be there. This made building the home page a little tricky but I tried to keep that as simple as possible by just using bootstrap. My goal of the homepage is just to be a proof of concept since I imagine most developers that use this repo and collection will likely have all sorts of front-end applications they need to integrate into beyond just the web. Accomplishments that we're proud of My goal was to make it easier for any developer to quickly spin up a URL shortening service, generate code snippets they can then place into their apps, and use whatever analytics service they like. What we learned Firebase Functions can host front end applications. I had no idea that existed before this project and made my life easier!! But the biggest thing was how to design better APIs by watching the various Postman YouTube videos and using the knowledge to create better documentation. What's next for linksof.fun My next goal is to add more analytics service options to the repo. Then, add Firebase authentication so that only certain users can create new short URLs. Finally, figure out if I can create a "one-click" button to deploy the GCP service, Postman collection, and analytics or at the very least get as close as possible to a "one-click" experience as possible. <div