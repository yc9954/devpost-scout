---
slug: "jira-runbook"
url: "https://devpost.com/software/jira-runbook"
title: "Runbook for Jira"
hackathon: "Codegeist 2021"
organization: "Atlassian"
winner: true
words: 556
team_size: 1
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/cross_origin_web"
  - "domain/developer_tools"
  - "user/developer"
---

# Runbook for Jira

> Runbook for Jira lets you create rich and customizable runbooks on your Jira issues. Runbooks ensure that important activities are not missed, properly documented and clearly communicated.

[Devpost](https://devpost.com/software/jira-runbook) · hackathon [[Codegeist 2021]]

## Facets

**mechanism** [[cross_origin_web]]
**domain** [[developer_tools]]
**user** [[developer]]

**stack** forge, javascript, react

## How they structured the write-up

- inspiration
- what it does
- how we built it
- our development experience
- what's next

## Body

Runbook on a Jira Issue Creating a new runbook Adding an activity to your runbook Reordering activities Saving your runbook as a reusable preset Inspiration Runbooks are common practices to manage large scale tech activities and ensure that every detail is considered and addressed. Some examples are Release Runbooks and QA Checklists. Runbooks ensure that important activities are not missed, properly documented and clearly communicated across relevant parties. In the team I work with, we practice continuous delivery where we deploy features behind feature flags to production until stakeholders decide on an official release date where these features are made public. During these official releases we would prepare runbooks as excel files and attach them to a Jira issue. This is no doubt a clunky way of organizing and has been the core inspiration on developing a proper solution for Jira. What it does Runbook for Jira lets you create customizable runbooks on your Jira issues. Add customizable activities to your runbook and assign them to other users, and even save runbooks as presets so you can easily reuse them across any other issues. Features Create runbooks and attach them to any issue Add detailed activities including assigning Owners and Status Save runbook as presets so you can quickly clone the same runbook across any issues Reorder any activities in a runbook Assign activities to anyone Manage presets, rename runbooks Activity columns intelligently hides to optimize screen space when no information to display. How we built it The project is built with Forge and implements the storage API. I used the Forge UI Kit (Beta) extensively in building the user interface for Runbook where I made use of 19 components ( https://developer.atlassian.com/platform/forge/ui-kit-components/ ). The current version applies the issue panel module, with plans to expand to the admin module in coming updates. Our development experience Jira is used on a day to day basis and is a huge component of the toolset in the team I work with. There were a couple of things I had in mind in order to improve our working experience. Being new to development on Forge, I first had to study the SDK to determine whether it was possible to build the application we wanted. I spent a good amount of time in this area, going through many of the API and development blocks to find out what was possible with Forge. I also had to decide whether the UI Kit would support the application design I had in mind, without having to implement a custom UI. Our goal was to create a user experience which resembles as closely as possible to the experience Jira provides. And hence I was trying not to resort to developing on custom UI. There were some hurdles like the lack of a drag and drop feature, but was able to work around them. Overall I was delighted with the capabilities and the extendability of Forges. And most of all being able to developed a complete application using the SDK. The excellent documentation for the UI Kit, API as well as sample projects has been great help. What's next The immediate plan is to launch the application on Jira marketplace. Subsequently, we want to allow more robust customization through the admin page and to collect feedback from customers on what they'd like most in Runbook. <div