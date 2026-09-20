---
slug: "send-the-list-of-network-services-to-cisco-webex-teams"
url: "https://devpost.com/software/send-the-list-of-network-services-to-cisco-webex-teams"
title: "Send the list of Network Services to Cisco Webex Teams"
hackathon: "The Postman API Hack"
organization: "Postman"
winner: true
words: 384
team_size: 1
has_repo: false
has_live: false
has_video: true
tags:
  - "project"
---

# Send the list of Network Services to Cisco Webex Teams

> This project enables users to fetch the configured services on the NSO, store their count and extract services name as EnvVariable, and using this variable send the message in Cisco Webex Teams.

[Devpost](https://devpost.com/software/send-the-list-of-network-services-to-cisco-webex-teams) · hackathon [[The Postman API Hack]]

## Facets


**stack** cisco, nso, webex

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for send the list of network services to cisco webex teams

## Body

Inspiration I've been recently working on a project where we had to develop some services for customers on Cisco Network Services Orchestrator - NSO . We had also to develop the list of tests to test services are working when deployed and I started actively using Postman to compose the requests (ie. to create service, update the service, delete..). The NSO provides the RESTCONF API and all of the above is pretty easy to do once the service is developed. It is however a bit complicated to quickly fetch the list of the configured services and we needed that info to be compared in a few environments so I got the inspiration to do this task now :) What it does The collection basically has two requests - the first is get a request to NSO to fetch all of the configured services by calling to /restconf/data/tailf-ncs:services . The response is then parsed to json object, and from there we extract the service names. We do that by looking in the key names while in loop, as the keys are not known upfront (ie. service names we define as we develop them). Once the service names are known, we save them as the string, do a bit of manipulation on the string to "beautify" the output, and save this data in EnviromentalVariable. Then we have POST to Cisco Webex Teams (but could be easily changed to Slack) with the notification of how many services are currently available and the list of Service names (using a static variable for device id, also used for authentication, and the two dynamical ones - count and service name). An environment will need to store environmental variables. How we built it As explained above :) Challenges we ran into The biggest challenge was to find an efficient way to extract the keys from a nested json object by a person that never did js before! Yaaay!! Accomplishments that we're proud of Working collection :) What we learned A bit of javascript and use of env variables will be using more of this for sure in the future! What's next for Send the list of Network Services to Cisco Webex Teams Plan to expand the collection with more APIs to be used in automated testing of the services developed. <div