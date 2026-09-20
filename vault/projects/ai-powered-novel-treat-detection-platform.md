---
slug: "ai-powered-novel-treat-detection-platform"
url: "https://devpost.com/software/ai-powered-novel-treat-detection-platform"
title: "UnHarmd"
hackathon: "Google Cloud Gemini Hackathon"
organization: "Google"
winner: true
words: 613
team_size: 0
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "mechanism/simulation_digital_twin"
  - "domain/transportation"
  - "substrate/structured_db"
---

# UnHarmd

> An intelligent LLM-powered honeypot network simulating services, capturing, and analysing attacks in real time to enhance security insights and detect emerging threats over multiple common platforms.

[Devpost](https://devpost.com/software/ai-powered-novel-treat-detection-platform) · hackathon [[Google Cloud Gemini Hackathon]]

## Facets

**mechanism** [[realtime_stream]] [[simulation_digital_twin]]
**domain** [[transportation]]
**substrate** [[structured_db]]

**stack** app-engine, cloud-functions, golang, google, google-cloud, nginx, node.js, postgresql

## How they structured the write-up

- inspiration
- what it does + how it works
- challenges we ran into
- accomplishments that we're proud of
- what's next for unharmd

## Body

Homepage Attack Report Breakdown Launched Production Version of homepage design Github Repo for Edge Honeypot Nodes that report back to central server General branding Inspiration I run a few websites that re constantly getting hit with random probes, which made me think would it not be possible to use a LLM to simulate a target environment. And while pretending it would be able to learn what the attacker is trying to do. The project aims to answer the question "WHAT IF WE LET THEM IN", what can we learn? Once it has learned it should be able to create a report of the attack + how to mitigate it automatically. What it does + How it works Unharmd starts and stops a list dynamic network of honeypots that is continually refreshed to capture the latest threats. Leveraging existing LLMs, we analyze each connection, engaging with attackers through protocol-compliant responses to gather critical insights. If LLM identifies a confirmed attack, we generate a detailed report, accessible here. Instances are created in Google Cloud in random regions and run our custom node which listens on specific ports and protocols. When traffic is received it pipes is via LLM to ask how it should proceed and what to send to the client. Once we have learned everything we can, the connection is blocked. Nodes are stopped and restarted again every few days to keep the IPs fresh. The service supports various and ever growing list of services such as http server/postgres/redis etc etc The edge honeypot nodes are totally open source and hosted on Github at https://github.com/unharmd/node . The actual prompts and process are private but the edge + function that power the LLM queries are open source to help others improve it and allow businesses to consider running it inside their own infrastructure for more learnings. At launch the tool supports the following services and has honeypots running for each in random locations over the world using LLM: Generic HTTP Server WordPress Joomla Drupal Apache Struts Nginx Server Tomcat OpenCart Magento phpMyAdmin Elasticsearch Grafana Kibana Jenkins Docker Registry Nextcloud Roundcube Webmail Zimbra MicrosoftExchange Challenges we ran into The LLM response time is a bit slow, but still fast enough for most attackers as they sit and wait for at least a few seconds. In the future this can be made faster with a LLM local model. For now caching has also been used, so that as the database grows and more protocols are learned less and less calls will go out to the LLM itself. Making it easy to find new patterns too. Costs are also a big issue till this is a self funded project, added various smart caching items. By learning to respond it avoids having to call the LLM API all the time and will start calling only for actual novel requests which need inspection. Accomplishments that we're proud of Have been able to identify a few attacks already. And quite sure we would be able to detect new zero days with the given data so far. What's next for UnHarmd Next if this works as expected we can offer the service to businesses to report new attacks in realtime for them to check (that match their tech stack) and send out a monthly auto generated report for all subscribers. All generated with AI. Idea is that the report could be free and serve as a way to advertise security / automated mitigation services and then allow businesses to subscribe for realtime alerts + WAF updates + auto AI powered fixes to their code. Reducing the time from when a attack was found and then fixed to hours or even minutes! <div