---
slug: "lostdog-mx"
url: "https://devpost.com/software/lostdog-mx"
title: "Lostdog.mx"
hackathon: "2018 Developer Circles Community Challenge"
organization: "Facebook"
winner: true
words: 1207
team_size: 2
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "domain/developer_tools"
  - "domain/immigration_refugee"
---

# Lostdog.mx

> we want to create a huge pet lover community

[Devpost](https://devpost.com/software/lostdog-mx) · hackathon [[2018 Developer Circles Community Challenge]]

## Facets

**domain** [[developer_tools]] [[immigration_refugee]]
  <sub>weak: finance_payments</sub>
  <sub>weak: geospatial</sub>

**stack** amazon-web-services, angular.js, facebook-ads, heroku, javascript, mongodb, node.js, sass

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for lostdog.mx

## Body

Facebook ads. An ad will display in the location given summary the first question when reporting a lost pet adding colors a pattern for dogs the payment form (it only shows when reporting a lost pet) the board with location filter open you can preview the add the change some info. the board displaying all lost pets ad automatically generated on our facebook page page of the dog part 2 (the lost map) page of the dog with actions (found it, seen it, subscribe) email template for seen it Inspiration Our pets are some of the most reliable, amazing companions we have, they are the inspiration, and motivation for many of us. We love them and treat them as members of our family and when they get lost, our hearts get broken. We want to help our community by providing resourceful, efficient, safe and amiable application to locate and rescue their lost pets so that there will be no more broken hearts . This is why we created LostDog . Pets provide to their owners physical and emotional benefits, with that in mind, LostDog’s aim is to form strong interrelated communities to relieve the pain of feeling helpless when losing a pet, knowing that there is a reliable, efficient tool that will enable them to find fast, even beyond state borders their beloved dog. We started creating Facebook ads manually for each pet in our site, which was time-consuming because we required at least 30 mins per person per ad, so we had to improve it. What it does LostDog is an MVP (Minimum Value Product) of a marketplace where lost & found dogs are published. We designed an engine that matches pets not only according to their characteristics but also according to their location, through a geolocation system . It also manages the reward for each pet in a secure way by using QR codes . It creates Facebook ads in the location where the pet was lost, with no human intervention only with the parameters that the user inputs ( this is the update we are competing for ). This way to bring people together by displaying automated ads on the location of the event (lost pet) so nearby people can interact with this event, with the owner that lost it, or other people that are interested in looking for it. When an ad is generated, this ad is bound to a page. This page has 3 actions, the first one "Lo encontre" (means I've found it) will notify the owner and all the people subscribed to it. (people that interested or is looking for the pet). The second one, "Lo he visto" (means I've seen it), will also notify the owner and all the people subscribed to it with the location that the user saw. This will motivate all subscribed users to go and search for the pet near the location. The last options will subscribe you to both of the events above. It also provides safeness by asking evidence of the pet. How we built it To build the integration with Facebook-marketing-API we first had to ask ourselves what did the user really needed. But that was a not a question for us to answer, so we asked some of our users. Most of the responses pointed out to the possibility of modifying the ad as well as a way to increase its reach if needed. After knowing the needs of the user, Chris started designing the functional, technical, and UI/UX of this new update. The functionality had to be simple so that end user wouldn’t have to re-adapt, thus reducing the learning curve. In the technical part, our API had to connect to our Facebook page, create campaigns, ad-sets, ad-creatives, and get estimations per daily budget. Plus to be able to save the ad-set Id in the DB and to trigger a notification every time an ad was created allowing Chris to review it and avoid rejections due to poor quality data. With the UI/UX designs, we had to make it simple and fun so that the end user enjoyed being in our web-app. After having all the main designs, Chris coded all the front-end with Angular and the back-end with Node.js, Express and the Fb-Marketing-SDK. Then we hosted our back-end in Heroku for a rapid deployment and the front-end in S3 and CloudFront. Now having everything coded and deployed we had to test it to be sure we had a high-quality product. Challenges we ran into I wanted to show the user the estimated reach that Facebook provides from a given daily budget . So if the user increased the budget he would get a higher estimated reach of people. But I just couldn't find a specific API for this particular purpose. So I made reverse engineering by inspecting the Facebook manager console to see how they were doing it. I found out that they pull a huge array of values from an API-endpoint. This array of values is the reach-vs-budget plot broken into chunks of linear sections. Now, what I had to do became clear. I had to call that service in the exact same way and then, to get the corresponding estimated reach for a given budget, I had to locate the value in a segment of the plot to make a linear interpolation and extract the specific reach estimation for the given budget. And this is how I came across one of my many problems during the project. Accomplishments that we're proud of We are proud of building a resilient, efficient and secure high-quality product from end to end. We are proud to announce that we have returned some pets to their owners and that we have, up to now, more than 100 pets registered . We are proud that we have created a community that supports us, with already 8k followers on the project via Facebook. What we learned We learned that sometimes you may have a good idea but it is not really good if people won't use it or in other words, if there is no market for it, so before even start creating the idea , the usability and market needs to be validated by interviewing your future users . We learned that not always the best products are the ones that prevail, but the ones that are constantly changing with the needs of their market . As for me (Chris) I learned how to make good UI/UX designs, I learned how to integrate a lot of services form AWS like SNS, SES, S3, EC2, Lambda, CloudFront, and I improved my JS skills in the front-end with Angular and in the back-end with node-express. What's next for Lostdog.mx We need to reduce the pricing so we can help more people and pets . To do this, we need to move our backend code into a Server-less technology. We need to implement adoptions , in a fun and interactive way, by matching the users with the pet that correspond to their needs and behaviors. We also need to add a bucket of donations so people can have free ads. Our main objective is to become the biggest pet lover community in Latin America . <div