---
slug: "idp-scim-sync"
url: "https://devpost.com/software/idp-scim-sync"
title: "idp-scim-sync"
hackathon: "Go Hack"
organization: "Google"
winner: true
words: 302
team_size: 1
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "substrate/structured_db"
---

# idp-scim-sync

> Keep your AWS Single Sign-On (SSO) groups and users in sync with your Google Workspace directory

[Devpost](https://devpost.com/software/idp-scim-sync) · hackathon [[Go Hack]]

## Facets

**substrate** [[structured_db]]

**stack** amazon-web-services, cli, go, golang, google-workspace, lambda, scim, spf13-cobra, spf13-viper, sso

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for idp-scim-sync

## Body

Inspiration Have a way to keep our Google Workspace Groups and Users synced with AWS Single Sing-On service without paying expenses services like Okta, OneLogin, etc. AWS created a project awslabs/ssosync to demonstrate their new AWS SSO SCIM API and I made contributions to this project PR#36 , PR#44 and PR#47 . Unfortunately, AWS stop and abandon the project, so I decided to create a new one with a different approach to avoid some of the limitations of the AWS SSO SCIM API What it does This just keeps synced Google Workspace Groups and Users with AWS Single Sign-On Service using Google Workspace Directory API and AWS SSO SCIM API How we built it Easy peasy! in the root of the project idp-scim-sync you have a Makefile with different targets, the default build the Golang project for your architecture. make Executables will be in the build/ folder Challenges we ran into Data synchronization between two REST API Hashing technique using Golang binary serialization to identify changes Store the last state of the sync to avoid repetitive calls to APIs Accomplishments that we're proud of I think the most important one is that thanks to the state file I reduce dramatically the calls to the AWS SCIM API to have the databases synced and at the same time reduction of the execution time (minutes to seconds) when no changes to be synced exist!. This is because I used hashing technique to compare changes What we learned How easy, productive and efficient is implement things Golang How hard is data replication Resolve a real problem using my mind and way to program What's next for idp-scim-sync It has algorithms that could take advantage of generics Also somebody from the community is requesting a nice feature hard to resolve Increments the unit test coverage! <div