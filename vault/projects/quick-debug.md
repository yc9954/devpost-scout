---
slug: "quick-debug"
url: "https://devpost.com/software/quick-debug"
title: "Quick Debug"
hackathon: "The Postman API Hack"
organization: "Postman"
winner: true
words: 680
team_size: 3
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/simulation_digital_twin"
  - "domain/developer_tools"
  - "domain/education"
  - "user/developer"
  - "user/educator_student"
---

# Quick Debug

> A workspace to automatically notify developers when API tests fail and suggest solutions based on the error response returned by the server.

[Devpost](https://devpost.com/software/quick-debug) · hackathon [[The Postman API Hack]]

## Facets

**mechanism** [[simulation_digital_twin]]
**domain** [[developer_tools]] [[education]]
**user** [[developer]] [[educator_student]]

**stack** javascript, postman, slack, stack-exchange

## How they structured the write-up

- inspiration
- what it does
- how we built it
- accomplishments that we're proud of
- what we learned
- postman workspace setup
- endpoint setup

## Body

Slack output Inspiration When a confusing error message is displayed in the console we usually turn to the internet to figure out what might be causing that error. We use tools such as Stack Overflow and Github Issues to help us understand the error message better. What if there was a way to automatically suggest relevant links based on the error message returned by an endpoint in Postman? That's where Quick Debug comes in. What it does Quick Debug is a Postman workspace that aims to help developers debug faster. With the help of Postman monitors, developers can run tests on their endpoints. If an endpoint fails it returns an error message from your server and passes down that error message to the Stack Exchange API to search for relevant questions on Stack Overflow. The collection then sends a Slack message to the developer with the error message, affected endpoint, and relevant links from Stack Overflow. This can also be used to test multiple endpoints in the same collection. Why search Stack Overflow? One of the most powerful attributes of Stack Overflow is the accumulation of developers’ knowledge over time. Community members have contributed more than 18 million questions and 27 million answers. Why use Slack for errors? If your company is using Slack as a communication tool, then it makes sense to integrate it with your error reporting tools. The diagram below shows the process for a failed and passed API test. I made use of Postman monitors , environment variables , test scripts , and pre-request scripts . I also made use of a Postman mock server to simulate API error response examples. Note: This workspace is intended to be used during the development process of building and testing endpoints. While you can use it to test production endpoints, it is discouraged to do so as it might leak information from the server. How we built it I started off by creating a Postman workspace and a collection that contains 3 requests. Next, I created a test script that checks If an API fails, the script saves the error message in an environment variable . Next, I created a request that uses the Stack Exchange API to find relevant questions on Stack Overflow, those questions are then saved in an environment variable using a test script . For the last request, I added a Slack Webhook to send the error message to the developer. I made use of Postman monitors to run the collection regularly and I used a mock server to create endpoints that simulate error responses. Accomplishments that we're proud of Building a workspace that we can use to speed up our debugging process when testing endpoints, hopefully, other developers find it useful too. 😃 What we learned This hackathon helped us learn more about Postman, We learned how to use Monitors , Mock servers , Environment variables , Test scrips , and pre-request scripts . Postman workspace setup Get a Slack webhook from api.slack.com/messaging/webhooks Set the following environment variables: slack_webhook : The webhook you got from Slack test_api : This is your API that you wish to test. Note: You can test more than one API too. Endpoint setup For this collection to work correctly the test endpoints need to return a response in the correct format to the Postman workspace. Below are a few steps required to be done on your server-side endpoints, this applies to Node.js and Express servers: Install serialize-error with npm install serialize-error Add a try-catch block in your endpoint and pass your error message in serializeError as shown below: // Your endpoint app.get("/example", (req, res, next) => { try { // This will cause an error let student; console.log(student.name); } catch (error) { // Serialize and send the error const serialized = serializeError(error); res.status(500).json(serialized); //dev //res.status(500).json("There was a problem"); // prod } }); serialize-error will allow the endpoint to return the correct response to the Postman workspace. That's all you need to do on your server! 🏁 Note: For production APIs it's advised to use custom error messages instead. <div