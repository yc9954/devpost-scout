---
slug: "github-to-whatsapp-push-notifier"
url: "https://devpost.com/software/github-to-whatsapp-push-notifier"
title: "Github to Whatsapp Push Notifier"
hackathon: "Cloud Native Hackathon"
organization: "WeMakeDevs"
winner: true
words: 307
team_size: 1
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "domain/retail_commerce"
  - "substrate/code_repository"
---

# Github to Whatsapp Push Notifier

> The whatsapp bot built using Twilo APIs which sends a Whatsapp message when code is pushed to a repository.

[Devpost](https://devpost.com/software/github-to-whatsapp-push-notifier) · hackathon [[Cloud Native Hackathon]]

## Facets

**domain** [[retail_commerce]]
**substrate** [[code_repository]]

**stack** apis, github-actions, python, twilio

## How they structured the write-up

- inspiration
- what it does
- how we built it

## Body

Inspiration So I always wanted there should be a quick way to let the project lead know that code has been pushed to GitHub repo, now GitHub notifications and emails don't work for me personally, I wanted something more quick and simple notification that will tell me the code has been pushed. What it does The WhatsApp bot is built using Twilio APIs which sends a Whatsapp message when code is pushed to a repository. How we built it Create an account in Twilio here . From your Twilio dashboard fetch Account Sid and Auth Token. To encrypt them, create new secrets in your repository named account_sid, auth_token, to_whatsapp_no and give its value. Create a .github/workflows/whatsapp-push-notify-action.yml . Add the following properties to whatsapp-push-notify-action.yml file . ```name: When a push occurs in the master branch, a private message is sent on Whatsapp. on: [push] jobs: build: runs-on: ubuntu-latest steps: - uses: actions/checkout@master - name: whatsapp-notify id: whatsapp-notify env: account_sid: ${{ secrets.account_sid }} auth_token: ${{ secrets.auth_token }} to_whatsapp_no: ${{ secrets.to_whatsapp_no }} - name : Run run: | echo 'Start!' ## Challenges we ran into One of the major challenges was that I need to have something that provides me service of automated messaging, and that is where Twilo APIs came into the picture and helped me to send notifications on WhatsApp using GitHub actions through their Twilio APIs. ## Accomplishments that we're proud of Successfully automated the push notifications using github actions and Twilio APIs. ## What we learned I learned about automating stuff using GitHub actions. Also learnt about how to use Twilio APIs. ## What's next for Github to Whatsapp Push Notifier Currently, the details and stats of push made are not being sent to the WhatsApp, will work on that so the notification receiver will have a more clear idea about the particular push made. <div