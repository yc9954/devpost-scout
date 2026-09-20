---
slug: "aws-monitor"
url: "https://devpost.com/software/aws-monitor"
title: "AWS Monitor"
hackathon: "The Postman API Hack"
organization: "Postman"
winner: true
words: 758
team_size: 1
has_repo: false
has_live: true
has_video: false
tags:
  - "project"
  - "domain/developer_tools"
  - "user/educator_student"
  - "substrate/code_repository"
---

# AWS Monitor

> A set of easily customizable requests for monitoring your AWS infrastructure. You don't have to be an AWS expert anymore to have a solid overview of what's going with your stack!

[Devpost](https://devpost.com/software/aws-monitor) · hackathon [[The Postman API Hack]]

## Facets

**domain** [[developer_tools]]
**user** [[educator_student]]
**substrate** [[code_repository]]

**stack** amazon-web-services, javascript, postman

## How they structured the write-up

- background
- solution
- documentation
- configuration
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for aws monitor
- collaboration

## Body

Receive easily customisable Slack notifications. Be gently notified when your bill grows out of control! Be gently notified when your bill grows out of control! Why even bother checking your AWS Bill? I'm sure you are just running few Lambda functions and a small enough DynamoDB instance, right? However, take a look at this article: 2700$ AWS bill?! 💸💸💸 Whether you want it or not, this can happen to you as well. That's why, to allow you to sleep at night, this workspace was created. 😴 Background For you and me, guys that just want to create some cool applications, having to worry about AWS is an unpleasant chore. Especially if you have to think about the things that you wouldn't like to worry at all. From time to time you adjust some Lambda code and think: "Ehh, I will just check the current AWS bill amount. Just to be sure... Wait... Where was this tab?!". This way you just lost another 5 minutes that you could have spent on something productive. Also, the bill is 0,47$ so you actually didn't have to do it. But who knows? Solution This small workspace consists of few useful requests that could be run using Postman's awesome Monitors feature. Also, because of the code that is currently written in the "Pre-request Script" and "Tests" sections, you can create your own additional requests that will allow you to monitor exactly the services that you are interested in. Currently, the workspace reports: AWS Bill amount. Number of Lambda invocations for the current month. Amount of new logs in bytes stored on your CloudWatch. Read and write data about this month's DynamoDB usage. Total size in bytes of a given S3 bucket. Statuses of EC2 instances in a given region. Running, desired and pending count of the ECS service. Documentation The workspace is documented using Postman Documentation features. Please look here to get more in-depth details. Configuration REMEMBER TO DO NOT USE YOUR AWS ADMIN CREDENTIALS! IF THEY LEAK, YOUR ACCOUNT CAN BE COMPROMISED! To be able to run the requests you need to fill out the following variables inside the AWS Monitor Environment accessKeyID (used to fetch your AWS bills) secretAccessKey (the same as above ☝️) spendingLimit (by default it's 20$) slackWebhookUrl (This one is optional. It's just more convenient to receive a short report each day, directly to your Slack inbox.) Don't know how to create a Slack Webhook? It's easy 👉 click here After you configured the variables, you can choose the requests that you are interested in by dragging them from Monitoring Requests section into the AWS Monitor Requests collection. Remember to put the requests between Preflight and Cleanup requests. This way everything will work as expected. The last step is to configure a Postman Monitor for AWS Monitor Requests that will run the checks on a regular basis. To do this, please follow this tutorial . How we built it Built with ♥️ and Postman. The workspace is meant to be used with AWS. Challenges we ran into The most difficult part, for now, was decrypting AWS documentation regarding some of the checks that were implemented. Not every service is documented well enough, so we hope this workspace can also serve as a working example of how the API can be used. Accomplishments that we're proud of The specific use of "Tests" scripts allows us to treat requests as separate units. After each request, the script produces an output that is gathered together and then sent as one message to the specified Slack webhook producing a nice message. What we learned Explored almost the whole suite of solutions that Postman offers. The workspace uses a public workspace containing 3 collections, environment and is meant to be run using Monitor. What's next for AWS Monitor Thanks to the possibility of forking workspaces and submitting pull requests, we hope that the tool could be expanded with new requests. Collaborators will be able to create their own requests that will be merged into the main workspace. The collection of requests will allow each user to combine them to satisfy their particular needs. The workspace could be also expanded to include other cloud providers (like Azure, Google) but then we would have to think about a new name 😁 Other improvements will include integrating other notifications options like for example different chats etc. Collaboration Everyone is invited to collaborate on creating new requests for public use. To do that, fork Monitoring Requests collection, create a new request and make a pull request. <div