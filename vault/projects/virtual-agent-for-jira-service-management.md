---
slug: "virtual-agent-for-jira-service-management"
url: "https://devpost.com/software/virtual-agent-for-jira-service-management"
title: "Virtual Agent for Jira Service Management"
hackathon: "Codegeist 2022"
organization: "Atlassian"
winner: true
words: 373
team_size: 5
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
---

# Virtual Agent for Jira Service Management

> Empower operations and support teams to deliver exceptional support at scale, fast, with our new AI-powered virtual agent technology. This project came out of Atlassian's Cloud Roadmap (Q4 23)

[Devpost](https://devpost.com/software/virtual-agent-for-jira-service-management) · hackathon [[Codegeist 2022]]

## Facets


**stack** digitalocean, django, javascript, machine-learning, postgresql, python, react, redis, uikit

## How they structured the write-up

- inspiration
- what it does
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for virtual agent for jira service management

## Body

ask a question to the virtual agent accept/reject the virtual agent's recommendation select which group you want to be added decide if the recommended knowledge management link works for you create ticket if the virtual agent cannot auto-resolve your request Gaspardesk goes to Codegeist 2022 In the process of striving to achieve the unachievable, we decided to get involved and create something new, something innovative. We combined our AI Conversational Platform with Atlassian to create a unique, end-to-end chatting experience, that helps users improve their daily IT experience ! Inspiration This feature aligns with Gaspardesk’s mission to auto-resolve repetitive employee support requests and allow Atlassian’s Admins to focus on things that matter most for their organization. What it does We have a virtual support agent (also known as IVA – Intelligent Virtual Agent) that is a conversational bot that uses artificial intelligence and NLP models to understand user intentions and prevent employees from creating support tickets. It can auto-resolve repetitive internal support requests within a few seconds and without human involvement. Examples of those requests include things such as reset your passwords, add and remove users from groups. Furthermore, it can deflect employee requests with ML based knowledge management recommendations. ## How we built it We used components from the UI kit and a subset of React’s features on Atlassian Forge to create an end-to-end chatting experience, that integrates seamlessly with our machine learning platform. Challenges we ran into The biggest hurdle was establishing a safe and authenticated way communicating between the Forge App and our platform. Also, the selection of the ready-made components were very limited and the abilities to customize were extremely poor. This means that without employing the Custom UI feature, the UI layout would not be very satisfying and user friendly. Accomplishments that we're proud of In a very short time frame, we managed to achieve to plug our Platform into Jira Service Management using the Forge framework. What we learned It was a rewarding experience to use React. What's next for Virtual Agent for Jira Service Management Deploy the Virtual Agent in Jira Service Management Customer Portal, in where employees can go and auto-resolve their own issues without having to talk to a Jira Service Management agent. <div