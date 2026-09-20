---
slug: "azure-service-bus-queue-listener"
url: "https://devpost.com/software/azure-service-bus-queue-listener"
title: "Azure Service Bus Queue Requests and Deadletter Monitor"
hackathon: "The Postman API Hack"
organization: "Postman"
winner: true
words: 692
team_size: 1
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/provenance_signing"
  - "domain/developer_tools"
  - "user/developer"
---

# Azure Service Bus Queue Requests and Deadletter Monitor

> This Postman project is used to create, delete, view, and monitor Azure Service Bus Queues. You can start interacting with your queues as well as monitor your dead letter queues.

[Devpost](https://devpost.com/software/azure-service-bus-queue-listener) · hackathon [[The Postman API Hack]]

## Facets

**mechanism** [[provenance_signing]]
**domain** [[developer_tools]]
**user** [[developer]]

**stack** azure, queue, servicebus

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for azure service bus queue requests and deadletter monitor

## Body

Inspiration In my main job I interact with Azure Service Bus queues very often. Usually when I need to build services to send and receive from a queue, I build the "sender" or "receiver" first and have difficulties testing. The Azure Portal has a decent UI called an explorer, but it is extremely simple and doesn't support everything I need. With this Postman collection you can now create, edit, delete queues and then send, receive, peek, and unlock messages. What it does These collections handles three main things: Azure authentication using a device code method and access tokens Almost all of the REST operations supported for service bus queues including: Create queue Update queue Get queue(s) details Delete queue Send queue message Send queue messages (bulk) Peek queue message Receive and delete message Unlock message Run a Postman Monitor for listening to a queue's complimentary deadletter queue Fail Postman Test and report error of deadletter reason How we built it Azure Authentication I have spent a good amount of time using Azure's REST API and their documentation is very well written and thorough. I used the device code authentication which allows the user to authenticate via a browser. Users are not required to type their username and password in Postman which this method and, instead, use and already authenticated account, avoiding the need for logging in or typing a password (as long as they are already authenticated inside the browser). I save all the access tokens and refresh tokens to a Postman Environment . REST Operations Most of the REST requests were fairly straight forward, but I ran into a very difficult problem when needing to interact with messages on the queue. Azure Service Bus Queues requires a shared access signature (SAS) token as an authentication header which is made with an HMAC. I used the Postman Pre-request Script to generate the SAS. The remaining REST operations used the access token from the previous authentication steps. I greatly used a Postman Environment to store 15 different environment variables for endpoint paths, request bodies, and headers. I used Postman Tests to parse specific variables out of request responses and store those into the environment. Deadletter Monitor One bad thing that can happen with a message queue is a message be "deadlettered". This is when a message, most the time, has been delivered to some receive more than the maximum amount of times and then never completed. A message being moved to a deadletter usually implies there is something wrong the message, the sender, or the receiver and it is important to notified of a deadletter as soon as possible. My Postman Monitor uses the deadletter request to check the deadletter queue and throws a test error if anything is detected. Challenges we ran into As described above, one issue, and the most complicated, was creating an HMAC for an SAS token. Azure provided a Nodejs script to create and HMAC, but it was not totally compatible with Postman due to some external packages. I spent a fair amount of time refactoring their NodeJs script to use packages and method calls that are supported by Postman. I was also not as experienced with Postman Tests so those took me a while to get up to speed. Accomplishments that we're proud of I am very proud to have created a tool for me and the community that will support many people, not only in their personal projects, but also in their professional careers. Azure provides a great a service and I believe with help others have an easier time interacting with it. What we learned I learned a lot more about NodeJs cryptography, Postman Tests , Postman Pre-request Scripts , and Postman Monitors . What's next for Azure Service Bus Queue Requests and Deadletter Monitor I would like to continue building on the monitors for this as I think there can be a lot of value for people who are not practiced in a language such as .NET or NodeJs. Postman can be used by many more people than just developers and these collections will help non-developers learn more about Azure Service Bus Queues. <div