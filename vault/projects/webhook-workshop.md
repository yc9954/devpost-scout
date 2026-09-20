---
slug: "webhook-workshop"
url: "https://devpost.com/software/webhook-workshop"
title: "Webhook Workshop"
hackathon: "GitLab Innovation Pitch Competition"
organization: "GitLab"
winner: true
words: 451
team_size: 2
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "domain/developer_tools"
  - "user/developer"
  - "user/general_public"
  - "substrate/code_repository"
  - "substrate/financial_record"
  - "substrate/web_dom"
---

# Webhook Workshop

> Build and deploy webhooks without the pain

[Devpost](https://devpost.com/software/webhook-workshop) · hackathon [[GitLab Innovation Pitch Competition]]

## Facets

**domain** [[developer_tools]]
**user** [[developer]] [[general_public]]
**substrate** [[code_repository]] [[financial_record]] [[web_dom]]

**stack** deno, deno-deploy, deno-kv, gitlab, gitpod, openai, typescript, webhooks

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for webhook workshop

## Body

Editing a webhook in Gitpod Inspiration At The Adaptavist Group , we have started to make use of a recently installed self-hosted GitLab, and many teams are looking to migrate from other git, CI/CD, and issue tracking systems into it. Talking to my colleagues, a major concern seemed to be being able to customize their workflow, and integrate other apps with GitLab via webhook events. It seems that a major barrier to this was the faff required to develop, test and deploy such webhooks. What it does The codebase is a simple webserver that provides webhook endpoints, but the focus of this project is to improve the developer experience, making the workflow around the code quick, easy, and painless. We bring together the latest best of breed technologies into an environment for getting started quickly on the webhook development and deployment lifecycle, without limiting future flexibility. Gitpod provides an environment to edit your webhook code and run a development server with a public URL (essential for webhook testing), giving a realtime development cycle experience, and avoid the faff of setting up a tunnel. Deno provides a modern Typescript runtime that avoids the large initial download of packages, and incorporates all the tooling (ie. formatting, linting, type checking, task running, testing) you need. Deno Deploy provides a cloud edge hosting solution with a very simple deployment mechanism, and support for a transactional distributed key-value store, queueing, and scheduling out of the box, without having to provision additional services. GitLab itself provides the git repo hosting for your webhook codebase, and CI/CD to test and deploy them to Deno Deploy. The intention is that you should fork this project, and use it as a template from which to create your own webhooks. It contains a number of example webhooks, including a hook to create an issue on a pipeline failure and use an OpenAI LLM to summarise the reason and suggest a remedy. How we built it The development was all done within the environment itself, using Gitpod, with VSCode in a browser, and hosting the code on our internal GitLab, before moving it over to the public gitlab.com. Challenges we ran into Surprisingly few thanks to the quality of the technologies used. The greatest challenge was the short time frame, we didn't start until about 2 weeks before the deadline. Accomplishments that we're proud of Turning around this idea so quickly. What we learned Start sooner :D What's next for Webhook Workshop More example webhooks Improve documentation Streamling the getting started process wherever possible More helper functions to make webhook coding much easier Alternative deployment options Declarative webhook registration - avoiding having to manually configure the webhooks in the GitLab UI. <div