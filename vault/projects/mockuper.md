---
slug: "mockuper"
url: "https://devpost.com/software/mockuper"
title: "Prototyper - Create Prototypes in your Jira Issue"
hackathon: "Codegeist 2020"
organization: "Atlassian"
winner: true
words: 600
team_size: 1
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "domain/retail_commerce"
  - "substrate/video_visual"
  - "substrate/web_dom"
---

# Prototyper - Create Prototypes in your Jira Issue

> Easily create interactive prototypes in your Jira Issue. No external tool needed.

[Devpost](https://devpost.com/software/mockuper) · hackathon [[Codegeist 2020]]

## Facets

**domain** [[retail_commerce]]
**substrate** [[video_visual]] [[web_dom]]

**stack** forge, javascript, react, svg

## How they structured the write-up

- inspiration
- what it does
- how i built it
- challenges i ran into
- accomplishments that i'm proud of
- what i learned
- what's next for prototyper

## Body

Sample home page Inspiration Prototypes and mockups are an essential part of the Software development process. However, it is not possible to create interactive prototypes directly in Jira. This means you need to integrate third-party solutions, and you end up wasting time from changing between different software. So, what if you could quickly and easily create interactive prototypes directly in your Jira Issue? Well, that's what Prototyper is for. What it does It allows you to create interactive and responsive prototypes in your Jira Issue using a simple, yet powerful markup language. The parser transforms raw text in beautiful, interactive and responsive prototypes (made from SVG and HTML). Seventeen widgets have been developed so far, but more is coming =) Card List List Items Input Button CheckBox Radio Option Select Label Title Header Image Search Link Separator Line Goto You can customize alignment, spacing, colors, and icons. We use the FontAwesome icons, which means you have access to hundreds of icons to use in your prototypes. Input fields and forms :title My Title align=center top=60 bottom=30 :input Name :input Email :input Password :select City :checkbox I accept the terms and conditions :button Sign up goto=home :link I have an account Renders this: Cards, Tabs and Headers :header Events right=search left=bars :card title=Pink Floyd subtitle=The best show of the year image=show goto=details :card title=U2 subtitle=The 360° Tour image=show :tab Featured icon=list color=primary :tab Promos icon=percent :tab Weekend icon=calendar goto=weekend :tab Favorites icon=star Renders this: List and List items :header Pink Floyd left=chevron-left :image type=show :title Pink Floyd :label This is the best show of the year :list :item Stall subtitle=$140 right=chevron-down :item Boxes subtitle=$200 right=chevron-down :item VIP subtitle=$599 right=chevron-down :button Checkout goto=checkout Renders this: Search inputs :header Filter left=chevron-left :goto Back goto=home :search Search events :list :item Pink Floyd goto=details :item Queen :item Guns N'Roses Menu :header Events right=search left=bars :goto Dismiss Menu goto=home :menu Menu :item Profile :item Settings :item Notifications :item Logout goto=login :card title=Pink Floyd subtitle=The best show of the year image=show :tab Favorite icon=list :tab Promos icon=percent :tab Weekend icon=calendar :tab Favorites icon=star Renders this: Changing colors :color primary=green :header Events right=search left=bars :card title=Pink Floyd subtitle=The best show of the year image=show goto=details :card title=U2 subtitle=The 360° Tour image=show :tab Featured icon=list color=primary :tab Promos icon=percent :tab Weekend icon=calendar goto=weekend :tab Favorites icon=star Renders this: Responsive pages How I built it Forge only allow us to use their components to build interfaces. This means that we cannot use HTML tags to create interfaces. The secret sauce to create the prototypes was to use SVG images with a foreignObject tag inside it. This allowed me to embed arbitrary HTML elements, including even styles. Challenges I ran into The biggest challenge was finding a way to create beautiful and interactive prototypes without being able to use HTML tags directly in Forge. After trying different approaches, the final solution of using SVG images with a foreignObject inside allowed me to fulfil my vision for the app. Accomplishments that I'm proud of I'm really proud of the flexibility and interactivity it is possible to achieve with my app. It can be easily extended to include more widgets, more customisations, and yet everything is very simple to use. What I learned It was a great experience to learn how to use Forge and other Atlassian products. The ecosystem is amazing and allows you to create amazing products by leveraging Atlassian solutions. What's next for Prototyper Add desktop specific widgets Add more widgets Add canvas widgets (to allow drawing anything) Allow cloning a page Add more themes Add more device sizes <div