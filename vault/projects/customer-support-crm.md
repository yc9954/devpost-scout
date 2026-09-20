---
slug: "customer-support-crm"
url: "https://devpost.com/software/customer-support-crm"
title: "Customer Support (CRM)"
hackathon: "Cloud Native Hackathon"
organization: "WeMakeDevs"
winner: true
words: 435
team_size: 2
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "substrate/code_repository"
  - "substrate/structured_db"
  - "substrate/web_dom"
---

# Customer Support (CRM)

> This a CRM for providing support to the customer and helping them with thier issues. Customer can directly call or create a support ticket either through voice or text.

[Devpost](https://devpost.com/software/customer-support-crm) · hackathon [[Cloud Native Hackathon]]

## Facets

**substrate** [[code_repository]] [[structured_db]] [[web_dom]]

**stack** alan, django, fastapi, javascript, postgresql, python, redis, symbl, symblai, twilio

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- what we learned

## Body

Inspiration Well my driving force was the ease of automation. Automation can make everyone life easy. So why not automate customer contact services too? using next level services such as twilio, symbl.ai and alan.ai What it does It automates web navigation and functionalities for web apps (in this case our DireNet website ) using AlanAi. User can create voice ticket (thanks to twilio) as well as text ticket. If you are lazy even to write, again AlanAi saves the day :) Agents can then claim these tickets and thanks to symbl.ai the text and voice analytics (along with recording) are shown to agent . So they can better analyse the issue user is facing. And if its a end of the world situation for user, he can call directly and if any agent is availabe (logged in system) and is not on any other call, call gets forwarded to the agent. This queue like system was possible with help of twilio and redis. How we built it We have a django app which handles all the logic related to website and database. Fast api handles all the logic related to integration of 3rd party services(twilio/symbl). Redis instance saves all the frequenty used data and free agents queue (which uses a blocking pop call to get a free agent). Alan script handles all the visual and speech of website and was created by Lakshay Tyagi (My teammate). Challenges we ran into Well there is always problem in integrating 3rd party apis. And above them integrating them with each other and create a workflow and a pipline can wreak havoc. Most of documention of the sponsers were easy to follow but things always breaks in starting. One of the main challenge was to make an agent queue to forward user calls which required some knowledege of redis and queue data structure. Also following best practices of github like making branches for every feature then merging, making sure never to commit sensitive info to repo is not an easy task for a begineer :( What we learned Well I was studying fastapi for a week and this project polished my fastapi skills. and to be honest this was first time i created a project with 3rd party app integration with 3 services (lol). but everything started falling in places after scavinging documentations (after initially breaking stuff offcourse). So, yeah i learned a wide variety of things from best practices of git/github to integrating differnet 3rdparty services with each other and create a workflow Also, this was my first time using redis too (and damn its so useful). <div