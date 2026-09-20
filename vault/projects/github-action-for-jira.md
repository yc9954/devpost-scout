---
slug: "github-action-for-jira"
url: "https://devpost.com/software/github-action-for-jira"
title: "GitHub Action for Jira"
hackathon: "Codegeist 2021"
organization: "Atlassian"
winner: true
words: 649
team_size: 0
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/cross_origin_web"
  - "domain/developer_tools"
---

# GitHub Action for Jira

> Send GitHub Action Workflow Information to Jira.

[Devpost](https://devpost.com/software/github-action-for-jira) · hackathon [[Codegeist 2021]]

## Facets

**mechanism** [[cross_origin_web]]
**domain** [[developer_tools]]

**stack** forge, javascript

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- storytelling

## Body

Inspiration I was inspired by Atlassian Open DevOps, to use Jira as a single pane of glass and single source of information. By sending over GitHub Action (GitHub's CI solution) workflow information to Jira, teams are able to use that as another data point to make decisions accurately and quickly. What it does GitHub Action for Jira takes GitHub Action workflow results and send the information to Jira. Once the GitHub Action workflow YAML has been configured, Jira users will be able to view the status of the latest workflow in the issue or even have a trail of all the workflows that have been run in the issue comments. How we built it Obviously this was built using the Atlassian Forge platform. To receive information from GitHub Actions, we use Web Trigger that takes the information sent from a workflow and use the Storage API to store the latest workflow result and link. We also use the comments Jira API to create comments if that configuration is enabled. To save configuration values and also perform configuration checking, we rely on Storage API as well to store and retrieve the configuration values. For the user interface, we rely on Forge UI Kit and use several components including Admin Page and Form. We used the Issue Panel component to display the latest workflow information in the Jira issue. Challenges we ran into Initially I wanted to use the Jira Software Builds API , as the API does a lot of heavy lifting, including preparing a user interface to access builds. However the API endpoint is not ready and currently not available in Forge. This lead me to be creative and I started experimenting with having workflow information in comments. However this could easily clutter an issue's comment when there are multiple workflow runs, so I wanted a way to highlight the latest build. First I tried using Custom Field. However, I faced an issue where in the Custom Field, I had a link but that link was not navigable and would not open up to the GitHub Action workflow page. After consulting the Office Hours, I was suggested to try using Issue Panel. It served the use case I had, so I stuck with that for the final implementation. One feature that I wanted to add was to provide a button in the Admin Page to easily copy the configuration needed for GitHub Action YAML file to the user's clipboard. I tried multiple ways, including using Custom UI. However, as the Admin Page is an iframe and the iframe does not have the necessary permission to access the user's clipboard, I decided to not implement this feature. Accomplishments that we're proud of There are 2 things that I am proud of this project: Able to get the necessary information from GitHub Actions The initial part of trying to get the necessary information from GitHub Actions workflow was challenging. After several trials and errors, I finally able to have a concise configuration to only get the information needed. Having a decent user experience even without the Build API available Initially I was quite bumped out that the Build API was not available in Forge. However I took that as an opportunity to try out as many things as I could in Forge, which lead me to experiment with Custom Fields, then Custom UI and finally settling with Issue Panel. What we learned It is the first time I developed an Atlassian app using the Forge platform. It was a great experience trying out what was available in Forge and also figuring out what were the limitations. Storytelling I had a chat with a fellow participant in Codegeist, Afif about his experience in Codegeist and using Forge. Check the video below (Volume Warning: The video can be loud so please lower down your volume before watching. We are sorry about this.): <div