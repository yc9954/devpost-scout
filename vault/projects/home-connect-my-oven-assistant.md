---
slug: "home-connect-my-oven-assistant"
url: "https://devpost.com/software/home-connect-my-oven-assistant"
title: "Home Connect My Oven Assistant"
hackathon: "Alexa Skills Challenge: Beyond Voice"
organization: "Amazon"
winner: true
words: 568
team_size: 7
has_repo: false
has_live: true
has_video: false
tags:
  - "project"
  - "mechanism/sensor_fusion"
  - "domain/developer_tools"
  - "user/developer"
---

# Home Connect My Oven Assistant

> We provide an everyday baking support by giving the best oven settings for a requested dish. For ovens with Home Connect we can directly start the recommended program, but also provide alternatives.

[Devpost](https://devpost.com/software/home-connect-my-oven-assistant) · hackathon [[Alexa Skills Challenge- Beyond Voice]]

## Facets

**mechanism** [[sensor_fusion]]
**domain** [[developer_tools]]
**user** [[developer]]

**stack** amazon-alexa, amazon-dynamodb, amazon-web-services, cloud-foundry, kotlin, node.js, spring-boot, typescript

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what's next for home connect my oven assistant

## Body

Start screen Pizza recommendation with further alternatives Cake recommendation with standard settings as alternative (German) Details for cake request (German) Help screen with list of supported dishes (Echo Show 5) Help screen with list of supported dishes (Echo Show 8) Inspiration Free cooking without recipe is fun. But sometimes you're not sure about the oven's best settings without reading the manual. This is where we want to support, by providing the best settings based on a dish. More than this, modern ovens have hundreds of automatic oven programs and additional options like sensors, steam assist, microwave support etc. We also want to cover all of these options and help users to get the best out of their ovens. What it does The skill provides recommended oven settings for several dishes. For connected ovens with Home Connect it checks all available heating mode and automatic program and provides an individual recommendation. For certain dishes it guides you with maximum 3 questions to the correct result. The oven is automatically set to the recommended program and you can even start it right away. Next to the recommendation the skill provides also alternative programs and settings if applicable. How we built it For the realization of My Oven Assistant we have implemented an Alexa Custom Skill. The skill accesses a serverless AWS lambda, which was developed using Node.js and TypeScript. In the process, the Alexa Presentation Language (APL) has enabled us to develop our skills for the visual use in the kitchen. For the support of persistence in the skill a DynamoDB hosted by Amazon was chosen. The Lambda function also accesses a service developed specifically for our Alexa skills via an API, which links internal data from our ovens to the various dishes. Therefore a Spring Boot application with Kotlin was developed, which is hosted via Cloud Foundry. In order to control the ovens from within the skill, we use the Home Connect API . Challenges we ran into During the development of the skill, technical and organizational challenges occurred for us: A technical challenge for us was to customize and deliver the APL templates to support different aspect ratios and device displays. In addition, it was difficult to optimize the development environment and tools in an agile team with multiple developers. Through manually created deploy scripts using the ASK CLI, we were able to overcome this challenge. Due to the variety of oven programs and their special purposes, we can't always give a recommendation by just a dish. In such cases we had to find relevant decision criteria and request this from the user in a simple way. The biggest challenge that we're currently working at is the variety of dishes in the regional cuisines and the different expectations of the baking results. First we focused on the German kitchen (therefore the best experience is currently for German language) and continue now with UK and other European countries, supported by locals. Accomplishments that we're proud of Within a few months and with a small, but highly team we were able to develop an Alexa skill optimized for use in the kitchen by using the Alexa Presentation Language. The skill has great potential for our company and shows new opportunities for interaction with kitchen appliances in the future. What's next for Home Connect My Oven Assistant We continue extending the supported dishes, especially for English and further European languages. <div