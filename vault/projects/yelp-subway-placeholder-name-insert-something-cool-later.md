---
slug: "yelp-subway-placeholder-name-insert-something-cool-later"
url: "https://devpost.com/software/yelp-subway-placeholder-name-insert-something-cool-later"
title: "CoinStop"
hackathon: "The Postman API Hack"
organization: "Postman"
winner: true
words: 908
team_size: 3
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "domain/education"
  - "substrate/document_pdf"
  - "substrate/geospatial"
  - "substrate/sensor_telemetry"
---

# CoinStop

> You’re on the subway after work and you want dessert. Do you have time to search for ice cream parlors at each stop? Our API minimizes your search by finding all nearest ones along your subway route.

[Devpost](https://devpost.com/software/yelp-subway-placeholder-name-insert-something-cool-later) · hackathon [[The Postman API Hack]]

## Facets

**domain** [[education]]
**substrate** [[document_pdf]] [[geospatial]] [[sensor_telemetry]]

**stack** discord, dropbox, github.io, google-maps, here, javascript, openapi, opencage, postman, yelp

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for coinstop

## Body

Jimbo bot posting a link to dropbox with the route and business information. Collections for CoinStop with mock responses. The file Jimbo POSTed to Dropbox during the "Upload Businesses to Dropbox" step. We created a Postman monitor that ran a collection and checked for special hours. Unfortunately it requires API keys in INITIAL value. They aren't mocking us anymore. We made 1000 calls, and we don't have money to upgrade. GoFundMe??? The visualize tab of the "Render Map Page" runs our JavaScript and shows interactive map. You can ignore the HTTP request, ok if it fails. Using Vonage you can text a "start;stop;businessType" and get back the results from CloudNewman. Inspiration This API was inspired by a personal experience. One summer afternoon on the subway back home from school, one of our members, Lydia, craved ice cream. She decided to find a good ice cream parlor at one of the stops along her route home. That day Lydia spent over 15 minutes doing nine different searches for ice cream at each of the 9 local stops. As a result of this, we decided to create an API that will automate this search process. What it does The CoinStop API is not limited to just ice cream. CoinStop minimizes your searching by finding you a subway route and any type or name of business at each intermediate stop. If you don’t mind taking a stop to pickup your clothes or food or medication, CoinStop can help you efficiently do your errands. CoinStop also uploads a summary of your route, stops, and found businesses on Dropbox and sends you a link via Discord. How we built it Identify key APIs when used together can solve our problem (In this case: Yelp, Here, OpenCage, Google Maps) Read their documentation and get API Keys/authentication from each Create the environment Start out with the basics, and then scale up Build the workflow, write appropriate pre-reqs/tests Visualize the results for usability and write monitors for metrics Write documentation Challenges we ran into Probably the biggest challenge is the fact that there are so many APIs and it's not obvious which API will work the best for your project. The majority of the APIs we looked at require you to sign up to get an API key. If you accidently put it in a mock response body, then Postman Security security.notifications@getpostman.com will send you email and you get to go and figure out how to delete your old key and create a new one. Investigating APIs takes some effort and the terminology isn't always the same across APIs for the same concept, like mapping, so once you learn one API you can't necessarily use another API. We honestly felt that the majority of the time was spent browsing at all the different APIs and felt totally overwhelming but it was cool at the same time to see diversity and definite pros and cons to using each one. Another challenge is being restricted to the free Postman version. We ran into couple issues where we ran out of mock server requests because we hit the max requests. As a result our project was limited by that. And square favicons why.............................. Accomplishments that we're proud of Identifying multiple issues, being able to pinpoint the biggest one, and creating a solution for it Being able to collaborate as a team and deliver on initial requirements we set Expand our skillset by learning new technologies (None of us were familiar with Postman before the hack) Finish a project that we set out to do What we learned Programming in JavaScript How to Create APIs How to use existing APIs by reading their documentation and following their procedures How to setup a Postman Environment How to create Collections How to use Pre-Req and Test scripts to pass responses from requests to another and verify for correct data How to define collection workflows How to mock responses How to use visualizers to display our data very elegantly How to use monitors That there is an API for generating meaty lorem ipsum text baconipsum.com . Yes it's every possible variation of pork and it's sow cool. I learned OpenAPI 3.0 and hand created a JSON document that represents the Yelp Fusion Business v3 endpoint . Using an "allOf" array you are able to combine a $ref with additional data; so you can define a location in schema, then later if something returns a location that also has a display address you can combine them (take a look at "display_address" in our workspace under APIs/Yelp APIs/Define tab . We created an API "{{visualizerAssetsMock}}/js/coords-on-map.js?v=1.0" with an example having a HTTP 200 OK status code and the body having our JS content, then we made a mock server from it, so whenever we use {{visualizerAssetsMock}}/js/coords-on-map.js?v=1.0 it returns the JavaScript (but we didn't have to push it to our own server -- until we used up our 1,000 mock request for the month, then we switched to hosting on github.io; which we had never used before.) What's next for CoinStop Rename the project from "CoinStop" to "CoinStops" (so if you can't find us at CoinStop anymore, be sure to check for CoinStops). If that doesn't work, reach out to us on email! Account for other modes of transportation besides subways (Cars, buses, etc). Adding Twitter integration; we have ideas on how we want it to work. More refactoring & adding tests. Scale up of course! <div