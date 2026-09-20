---
slug: "hackathon-project-cyzhlf"
url: "https://devpost.com/software/hackathon-project-cyzhlf"
title: "MaiD - Mail in your feeD."
hackathon: "The Postman API Hack"
organization: "Postman"
winner: true
words: 996
team_size: 2
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "domain/developer_tools"
  - "user/developer"
  - "substrate/video_visual"
  - "substrate/web_dom"
---

# MaiD - Mail in your feeD.

> MAID saves your time by gathering latest feed from your favourite websites and delivering them to your mail at a schedule of your convenience. Maid is highly customizable and also very easy to setup.

[Devpost](https://devpost.com/software/hackathon-project-cyzhlf) · hackathon [[The Postman API Hack]]

## Facets

**domain** [[developer_tools]]
**user** [[developer]]
**substrate** [[video_visual]] [[web_dom]]

**stack** amazon-web-services, cloudflare, collection, davinci-resolve, javascript, mailjet, monitor

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for maid - mail your personal feed.

## Body

Maid Cover GIF MAID sample feed GIF 404 page - MAID is lost in galaxy Backend Meme Inspiration As developers and tech folks, we learn from websites such as Medium, Reddit, Hacker news, and Dev.to. Over time, we realized that we are spending a significant amount of time on these websites and also getting distracted from articles that are irrelevant to us. When exploring Postman collections and its automated features it hit upon us that we could just add all of our favorite websites(APIs/RSS feeds) in a collection and set up a monitor to mail an aggregated feed. It was a simple idea but its something that would save quite some time for a lot of us in the tech community. What it does MAID sends you a feed of all your favorite websites. Just add your favorite website(APIs/RSS) feeds and use the Util functions provided to create your personalized feed. How we built it We built our app logic entirely using JS in postman. Collection: We added feed sources(HackerNews, Medium topics, dev.to tags, subreddits etc.,) as requests under one Collection. Collection Variables: The filters for feed sources are added as collection variables. For example, the variable MEDIUM_Topics is used for sending medium requests to get data for a particular medium topic. Pre-request Scripts: We provided util functions for parsing RSS feeds, standardizing feeds, and sending next requests. All of the util functions are documented in detail. By adding util functions in the pre-request script of collection, we were able to reuse them in all requests. Test Scripts: We added tests to verify if the requests are run as expected. We also call the util functions to process the response, customize it and then decide the direction of monitor/runner workflow. Response Visualizer: We also added visualizer for viewing the mail directly in postman. Users can visualize their mails without actually sending them. Mock Server and Examples: We added examples for all the requests and created a mock server so that one can try out and understand the requests without actually adding the required credentials/keys. Monitor: You can setup a monitor to run MaiD periodically. We recommend it running daily at the time you are most comfortable reading. Environments: We are using one environment to set temporary variables needed for requests. We persist a variable in the environment which allow us to prevent duplicate feeds when the monitor is run next on that environment. External Technologies/APIs: Amazon S3 for uploading feed. MailJet Apis to send mail. Davinci Resolve for video editing. Inkscape for creating graphic assets. Challenges we ran into Running requests in order: Initially we couldn't figure out how to run them in order. But thanks to Postman's extensive documentation, we figured we could use pm.setNextRequest() UI: Being two backend developers figuring out how to build a great UI with just HTML and CSS was challenging. But we are proud of the final UI we were able to build. Mail: Given that email clients are very restrictive in the rendering the CSS in email, we were not able to bring the complete UI in the mail. We worked around this problem by uploading the HTML to AWS S3 bucket and sharing the feed link in the mail. Writing maintainable and reusable code: Given how postman sandboxes request for obvious reasons, writing code with DRY principles was a challenge. but with a little bit of fiddling around community forums and documentation, we were able to hack our way through it. This meant for us personally, the time required to add a new feed is exponentially lower than the first feed. and for the users, adding a new feed would take around 5-10 mins if not less. Video Editing/Graphic Design: Given the amount of love we've poured into the product from the initiation of idea to building a working product, we didn't want to do any less in the presentation. So we spent countless hours in designing a final video that's worth pairing up with a software we love. Accomplishments that we're proud of All the complexities related to the parsing and delivering of feeds have been abstracted out which means we ended up with a product that is not only useful for developers but also other functional area folks such as product managers. We are very proud that we end building a product that helps not just us but a lot of others. We are very hopeful that anyone facing similar problems as us and stumbles on MaiD will love with it and most likely end up using it. Given that the current-gen tech is all about web APIs in one or the other form We believe the possibilities of customizing MaiD are limitless. What we learned We learned that in-order to build a fully functional backend you don't have to have a crazy big infra setup or pay to one of those expensive IaaS/PaaS services. We were able to build the entire backend logic on Postman. Think about it, without postman, to build an app like this, we would need to Write the logic in a backend, Deploy it on cloud Setup schedulers to send mails. Build frontend UI for users to customize their feeds Build rest services to connect front-end with the backend. With postman and it's public collections, we were able to build an entirely open backend and give users the ability to customize their feeds. We never thought that was possible before we did it. 🤯 What's next for Maid - Mail your personal feed. Discover and follow feeds based on topics. make it easy for non-tech people to use maid. For example adding APIs specifically to stocks or cryptos and other niche areas. Adding Summary of articles in feed. For now, we only have the titles in the feed. In the future, we plan to add a summary and images of the article directly in the feed. Adding social media feed we already added Reddit, we plan to add Instagram/Twitter later. <div