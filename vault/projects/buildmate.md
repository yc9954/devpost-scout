---
slug: "buildmate"
url: "https://devpost.com/software/buildmate"
title: "Postman Helper"
hackathon: "The Postman API Hack"
organization: "Postman"
winner: true
words: 1100
team_size: 3
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/voice_speech"
  - "domain/developer_tools"
  - "user/developer"
---

# Postman Helper

> Run or get the status of your Postman monitors from anywhere using your favorite Alexa-enabled device.

[Devpost](https://devpost.com/software/buildmate) · hackathon [[The Postman API Hack]]

## Facets

**mechanism** [[voice_speech]]
**domain** [[developer_tools]]
**user** [[developer]]

**stack** amazon-alexa, amazon-web-services, github-jobs, node.js, postman, slack

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for postman helper

## Body

Inspiration We are a team of automation engineers based in Kathmandu, Nepal and who have played around a bit with Postman before. But sadly, our experience was just limited to sending very elementary GET requests. There would be times when we would feel that our experience with Postman needed some sharpening since quite few of our colleagues from other teams were already using Postman and they had very good things to share about it. So when Pujan , one of our office colleagues and a proud team member of Team Tilicho informed us of this hackathon, we jumped right in. When we started to look into so many cool things that could be build with and around Postman, we were completely blown away and a bit frustrated that we'd subdued our desire to learn Postman for so long. There were a few late-nights that the team pulled off, a plethora of different techniques and technologies that we used, and we ran onto some deadends where we had to compromise and implement a workaround. Our product is an amalgamation of our wish to learn and build a Postman service that could open up a door of opportunities to add value to the development community as well as learn some of the key skills and concepts in API testing using Postman. In the end, we are proud of what we have learned. It was quite a journey! What it does Since voice-enabled devices are getting traction every day, we decided that we could build a solution which could utilize the power that this technology can bestow upon us and leverage that to build neat services to run our collections, monitors using Postman CLI runner ( Newman ). User can enable the Alexa skill in any of their Alexa-enabled devices, and then give the following voice commands like : To run all the available monitors "Alexa, open Postman and run the monitors" To get the stats of the last run of all the available monitors "Alexa, open Postman and give me the status" To run a particular collection for which the collection and environment JSONs are present in the repo "Alexa, open Postman and run workflow" After the run for all the monitors or a workflow is completed, the build status is sent to the team's Slack channel and the output report of the collection run is produced as an artifact which the user can collect after the run is complete. How we built it To start off, we looked around the Postman API to explore the already available resources. To verify our scenario using the Postman APIs to get the monitors' information and relay the status messages to the Slack channel using the Slack API in an iterative manner was done using the Postman application. Also, a couple of Monitors were set up using the application which were set up to run at fixed schedules. Among the many options of a CI/CD solution, we chose to use GitHub Workflows since we had seen it being used by developers to demo their code in many conferences and also it seemed quite intuitive since we were using it as our VCS. We created some basic GitHub workflows which were used to run these collection through Newman . Finally, we added a layer of Amazon Alexa skill on top of this to enable these workflows to be triggered through GitHub API. The Alexa skill is coded in Node JS and is hosten as an AWS Lambda Challenges we ran into Having used Postman only sparingly in our previous encounters, we faced multiple challenges along the way. But the huge Postman community and the neatly maintained documentations always guided us along the way. The first challenge was since we were using API keys along the way to hit the APIs, we were not sure how to keep them secret. We overcame this by using environment variables which saved us much trouble. Another hurdle came up when we wanted to get the information of all the monitors and then post them as Slack messages iteratively for each gathered monitor uid. We dug up a lot of resources and finally found a solution to build a request workflow by chaining the subsequent requests. In doing so, we learnt plenty about using the Pre-request Script and Test sections to manage and pass on the variable values to and fro. We utilized the Postman Console to debug our tests and workflows. Also, there were multiple issues when debugging the Alexa skill. And once again, we had Postman to save us the trouble of verifying the GitHub APIs that we used directly from the skill code to trigger the workflow. Accomplishments that we're proud of To be really honest, none of us had ever gotten our hands dirty in the world of API Testing with Postman, forming complex request workflows in Postman, using Newman to run the collections and generate reports, understanding and implementing GitHub Workflow, developing Alexa skills and hosting the code as AWS lambda. To be fair to us, our job role doesn't demand the knowledge of these technologies. We are extremely proud that we worked together in mixing all these technologies, in which we had very limited expertise, to develop a solution which we think is really cool. What we learned To put it simply, a gigantic amount of knowledge. Postman, in which we had no skill whatsoever turned out to be so much fun to learn and to develop and test the APIs and workflows. We learned the core concepts of the API testing in making this app and also a lot about how we can use it in our daily work as well. This hackathon has really opened many avenues for each one of us. It has introduced us to concepts like workflows, Alexa skills and many more. We think that our journey has just started and we are really excited to move ahead and grow with this experience. What's next for Postman Helper There are a lot of areas where we can improve the existing version of the app. It could be viewed as a proof of concept for now. Below is the direction where we are looking at : We are thinking of improving the Alexa skill to make it more responsive and dynamic. Postman API can be further utilized to implement other key functionalities like creating a new monitor, configuring an existing one, adding a collection to run as a monitor, etc. After Newman finishes the run, the team can be notified with the report as an attachment in the Slack channel. <div