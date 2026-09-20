---
slug: "devsheds"
url: "https://devpost.com/software/devsheds"
title: "DEVsheds"
hackathon: "Codegeist 2020"
organization: "Atlassian"
winner: true
words: 710
team_size: 1
has_repo: false
has_live: false
has_video: true
tags:
  - "project"
  - "domain/developer_tools"
  - "domain/scientific_research"
  - "user/developer"
  - "user/researcher"
  - "substrate/code_repository"
---

# DEVsheds

> Removing friction between teams and working application & ML code, DEVsheds provides instant workspaces for software development and data science teams to build and run code.

[Devpost](https://devpost.com/software/devsheds) · hackathon [[Codegeist 2020]]

## Facets

**domain** [[developer_tools]] [[scientific_research]]
**user** [[developer]] [[researcher]]
**substrate** [[code_repository]]

**stack** atlassian-connect-express, bitbucket, kubernetes, node.js, python, react

## How they structured the write-up

- elevator pitch
- inspiration
- what it does
- how i built it
- challenges i ran into
- accomplishments that i'm proud of
- what i learned
- what's next for devsheds

## Body

DEVsheds Launchpad Software Engineer View Data Science View Service Modules Module Dependencies Key Benefits Elevator Pitch Removing friction between teams and working application & ML code, DEVsheds provides instant workspaces for software development and data science teams to build and run code backed by a Bitbucket repository. Major pain points in the development lifecycle include: On-boarding and empowering a new member of the team Efficiently communicating progress directly from the most tangible output - working code Fixing problems that begin with the words “it works on my machine” DEVsheds broadens support across the development lifecycle and addresses the pain points above while staying within the familiar Atlassian user experience; allowing teams to enjoy the benefits of a consistent experience, single user administration flow and integrated development workflow. Inspiration I’ve been the new person on a team and I’ve been accountable for bringing new people into teams. When joining a new team, you want to make a good impression and you’re excited about being able to contribute. Yet the first experience of many software developers, data scientists, and test analysts is often the frustrating, time consuming and demoralising one of trying to set up a local development environment to get started. I get excited about the creative aspects of projects and the buzz of a team firing on all cylinders. I want to create tools that help people focus on what they enjoy rather than get bogged down with the mechanical requirements. What it does For teams creating software and data products, working code is where “the rubber hits the road”. It’s what is showcased to stakeholders and presented to customers. DEVsheds removes the friction between teams and working code by making it easy to start working with the code, share work products with teammates, and iterate on functionality of value to customers. It does this through: Being an embedded part of the Atlassian toolset to ensure a smooth flow across the development workflow involving Jira user stories and tasks, development of source code in Bitbucket, submitting and reviewing pull requests, and releasing code to communicate progress. Supporting the research and experimentation phase of systems, especially ones involving analytics and machine learning, with Notebooks that allow immediate feedback loops of write, run, and visualise. Provisioning reproducible and automated environments that allow rapid feedback and smooth collaboration. How I built it The solution employs the Atlassian Connect Express (ACE) library to integrate with Bitbucket and uses React for the user interface. Development workspaces are created as Kubernetes containers. DEVsheds builds on the open source projects Eclipse Theia, JupyterLab, the Jupyter ecosystem, and Garden.io. Challenges I ran into The key technical challenge of the project has been in automating, securing, and ensuring scalability of the underlying infrastructure. From a design perspective, the key challenge has been turning a complex process into a simple and intuitive user experience. Accomplishments that I'm proud of Making the complex simple: enabling easy transition from source code to development environment and working application. Hiding the complexity of integration and orchestration across multiple computing clusters. What I learned Lessons learned along the way include: Embedded product design is about more than integrating the technology - the goal is to create a simple and productive user experience Codegeist has afforded a deep dive into the APIs and modules available to the Atlassian Developer The many challenges in securing distributed systems What's next for DEVsheds The goal is to enable a closer connection between research, development, and the user experience. For example, I want to enable product teams to be able to experiment with data and machine learning models, engineer a promising model as a software service, and then deploy this service to see the impact on the user experience – all within the same workflow and set of tools so the focus is on creativity. This would be a major leap forward compared to the disjoint set of processes and tools that exists for many teams today. Future areas of focus include: Deeper integration within Atlassian workflows including pull-requests, deep linking of Jira user stories and tasks, and integration with Bitbucket Pipelines. Improved collaboration including commenting and review of code, notebooks, and releases. Easy access to environments for background jobs and specialised workloads such as machine learning model training. <div