---
slug: "pro-active-environment-comparison-tool"
url: "https://devpost.com/software/pro-active-environment-comparison-tool"
title: "Pro-active Environment Comparison Tool"
hackathon: "The HCL-Pega Pathbreaker Hackathon"
organization: "HCL"
winner: true
words: 313
team_size: 5
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "domain/developer_tools"
  - "user/developer"
---

# Pro-active Environment Comparison Tool

> Compare any application deep into its rules data instances. Provides debugging tools for developers which reduces a lot of manual effort in comparing rules after deployment.

[Devpost](https://devpost.com/software/pro-active-environment-comparison-tool) · hackathon [[The HCL-Pega Pathbreaker Hackathon]]

## Facets

**domain** [[developer_tools]]
**user** [[developer]]

**stack** api, pega

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for pro-active environment comparison tool

## Body

Data Comparison results Rule comparison results ECT Admin Inspiration Pega developers often face challenges with the Rules and data mismatch across environments like DEV, QA, Staging and Production. We as a Pega developers faced these kind of issues may a times. It is a tedious task all the times to compare rules across different environments. We thought to have a Pega portal for environment(s) comparison including Rule counts, Data counts, Application wise artifacts counts, etc., So we have built one. What it does ECTPro tool will help a user to compare different environments in a single portal with very few clicks. It saves a lot of time for developers and QAs working on a project. It is built on Pega 8.6.2 . Users can enroll for Rule count stats notification and System cleanup notification emails which are assisted by a job scheduler. How we built it We have used Core Pega PRPC features Leveraged the integration features of Pega mainly Data API in Pega API collection Used Bi-Directional ping architecture Please refer technical documentation for more details Challenges we ran into Initially, faced challenges in figuring out the design and architecture Dynamic table creation for comparison became a challenge Accomplishments that we're proud of Rule count comparisons - Implemented Rule count comparisons for All rulesets, Just a ruleset, Rule set and version Data instance count comparisons - Implemented Data instance count for all concrete data classes, Just for a given data class What we learned Architecting the entire project gave different experience as lot of optimization is involved like reducing a bunch of connectors to one Leveraging Existing Pega API and using of existing OOTB rules for development improved the development experience What's next for Pro-active Environment Comparison Tool This tool can be developed with additional features included in the video and can be published to Pega market place for greater visibility <div