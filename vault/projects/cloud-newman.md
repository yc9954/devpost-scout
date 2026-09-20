---
slug: "cloud-newman"
url: "https://devpost.com/software/cloud-newman"
title: "Cloud Newman Me"
hackathon: "The Postman API Hack"
organization: "Postman"
winner: true
words: 512
team_size: 1
has_repo: false
has_live: true
has_video: false
tags:
  - "project"
  - "domain/developer_tools"
  - "user/developer"
  - "substrate/document_pdf"
---

# Cloud Newman Me

> Turn your Postman collection into an API! Supports private data. Simple to use-just output your response in Tests using console.log. Counts toward 2-3 Postman API usage calls; 1000/month for free.

[Devpost](https://devpost.com/software/cloud-newman) · hackathon [[The Postman API Hack]]

## Facets

**domain** [[developer_tools]]
**user** [[developer]]
**substrate** [[document_pdf]]

**stack** azure, express.js, newman, request.js

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for cloud newman

## Body

Call flow diagram shows how a client can run a Postman collection using cloudnewman.me Invoke www.cloudnewman.me with collection_uid, environment_uid, X-API-Key and any Dynamic parameters you want inject into the environment. Built with security in mind - you to create an environment variable named "allow.<name>" before it is an allowed Dynamic query parameter! We invoked www.cloudnewman.me with this collection, which console.log a JSON object to be returned as the API result from CloudNewman. Built for debugging -In your overlay environment pointed to by {{environment_overlay_uid}} you can specify to return_logs instead of JSON. When "return_logs" is defined, instead of JSON response we get logs about what is running and any assertion failures! If "return_logs" is "secure" then you get all console.log messages, be careful these may have API keys, PII or other sensitive data. Inspiration Once you use Postman and see the power, you wish that you could expose what you have done as an API for others to consume. I wanted this feature so our other Postman API Hack CoinStop could get invoked by a WebHook. What it does You invoke Cloud Newman passing it your collection uid, environment uid, and private environment overlay uid. It creates an environment based on merging the environment and the private environment (so you can set private keys in your non-shared "My Workspace".) It uses Newman to run the collection using the environment. For any requests in your collection, if your scripts (Pre-request script & Tests tab) do a console.log(message); then the message is returned from the API. NOTE: The last message logged is the one returned, so you can do debug logging along the way without messing up the results. You can pass a "contenttype" parameter and the response will use that value as Content-Type header that it returns. If you are stuck trying to debug failures then you can add "return_logs" with an INITIAL and CURRENT value of true in your environment & instead of returning the response you will get all of the logs and any failed assertions. How we built it It is built on top of Express.js and the Newman library . It also pulls in an open source libraries Request.js to simplify communicating with the Postman API. Challenges we ran into I'm not very good at async calls in JavaScript. The code could be improved so the Postman API calls aren't all queued synchronously, but instead queued all requests and waited for the promises to complete. Accomplishments that we're proud of The Cloud Newman API is probably what I'm most proud of. Also using Postman to document the API, it was my second time creating an OpenAPI 3.0 document & I got it working in Postman and Swagger. What we learned I had never used Express.JS, Request.JS, or Newman before. For the other hack (CoinStop) I learned most of the Postman features. What's next for Cloud Newman Developer feedback is probably the next step. I'm in the process of moving soon, so feedback might not get addressed until mid-Feb. I'd also like to harden the code for security and reliability. <div