---
slug: "product-vision-k0fgao"
url: "https://devpost.com/software/product-vision-k0fgao"
title: "Product Vision"
hackathon: "monday apps challenge"
organization: "Monday.com"
winner: true
words: 973
team_size: 2
has_repo: false
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "domain/labor_employment"
  - "domain/retail_commerce"
  - "substrate/geospatial"
  - "substrate/video_visual"
  - "substrate/web_dom"
---

# Product Vision

> Need to see how things fit together? Nothing beats a vision board!

[Devpost](https://devpost.com/software/product-vision-k0fgao) · hackathon [[monday apps challenge]]

## Facets

**mechanism** [[realtime_stream]]
**domain** [[labor_employment]] [[retail_commerce]]
**substrate** [[geospatial]] [[video_visual]] [[web_dom]]

**stack** cloudflare, cloudflare-durable-objects, cloudflare-kv, cloudflare-workers, fabric.js, javascript, react, typescript

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for product vision

## Body

Product Vision - Making your ideas come to life Vision Board - board view Product Glance - item view Product Details - integration Vision Board - board view (dark theme) Product Glance - item view (dark theme) Inspiration We've all experienced putting together a project then realising the individual pieces weren't as cohesive as we hoped. In e-commerce this mistake can lead to one of two situations: either purchasing more than what is necessary and taking a loss, or having a disappointed customer. When you go into a store it's easy to hold products next to each other and get a feel for the final result. With more and more purchases happening online these days we miss out on this crucial step in the buying experience. What it does Product Vision makes it easy to collaborate on projects that require purchasing products online. Product Details (integration) The Product Details integration allows users to simply add a product url in a monday.com item column and have the rest of the columns populated however suits them best. We provide a number of product details to choose from including name, price, rating, availability, and more. Product Glance (item view) The Product Glance item view gives a quick overview of products that have been added to monday.com item columns. Details include the name, rating, description, availability, price, preview image, and a link to the product page. Product Glance updates in real time whenever another user updates the item. Vision Board (board view) The Vision Board board view is the titular view of Product Vision. It is a real-time canvas that teams can collaborate on and make as tidy or as messy as their creative process desires. Features include: Auto-population from items on the monday.com board Real time changes from other team members on the board Visibility of other team members cursors inside the board A link directly to the monday.com item Built-in monday.com filters allow users to focus on what is important by making other items grayscale Free hand drawing Customisable text annotation Saving the vision board to a png How we built it Initially we looked for third party solutions to provide us product details, but quickly realised that if we wanted to make Product Vision free, feature-full, and reliable, we had to do it ourselves. To collect product details we use Cloudflare Workers alongside a mix of open-standards and custom web scraping. This gives us low operating costs and amazing performance due to our code being distributed globally. To get real-time collaboration on the Vision Board board view we are using Cloudflare Durable Objects. This is a bleeding edge technology that we hope to take full advantage of as it progresses through its Beta phase. The vision board uses fabric.js as a mechanism to efficiently render to the browsers canvas API. We have build React components around fabric.js to make development and maintenance even easier. In order to allow users to update their monday.com items exactly as they want, we required both a custom trigger and a custom action. Using a custom trigger allowed us to include an item mapping in the recipe sentence that inserted product details into item columns. The custom action was required as it was the only way to update existing items with the item mapping. We used a mixture of shortlived tokens and webhooks to allow an end-to-end experience without the need for any authentication beyond installing the app. Challenges we ran into As is with the internet, no two website are alike even when using the same standards. This meant that our custom product details web crawler had to constantly evolve throughout its development to ensure we could support as many websites as possible. As Cloudflare Durable Objects are currently in beta we have had to be flexible with their usage. An outage during our final opportunity to work on the Product Vision submission almost caused us to lose out on submitting Product Vision at a standard we're proud of. Accomplishments that we're proud of Through a lot of trial and error we ended up with a wide range of sites we support crawling product details from. We're proud of managing this without the use of any third party services. At a few points during development we thought we would have no choice but to implement an oauth flow to provide the level of functionality we wanted. Through a lot of research and out of the box thinking we managed to overcome these hurdles without sacrificing user experience. With how customisable monday.com is we wanted to ensure that even if you didn't have a need for every one of our features, you still had a need for Product Vision. We feel like we have accomplished this, while still building a cohesive and fun experience. What we learned Without prior video or icon creation experience, we needed to learn new tools. We ended up learning how to use Davinci Resolve for video editing and Affinity Designer for icon creation. We also learned that using bleeding-edge technology requires a lot of patience and forward-planning. What's next for Product Vision A lot of our decisions were made around performance, however we were not able to get the most out of the technology we chose, as is expected during a hackathon. This leaves us room to improve. Although we are happy with how fast we managed to get it, things can always be made faster. We want to use more machine-learning for our web-crawling implementation. It's got solid legs as is, but it is in no way perfect. Allowing assets from monday.com items to be included as images on the Vision Board, as well as a wider range of customisation on its tools. We plan on submitting Product Vision to the monday.com apps marketplace as soon as Cloudflare Durable Objects becomes GA. <div