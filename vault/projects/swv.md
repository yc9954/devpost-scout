---
slug: "swv"
url: "https://devpost.com/software/swv"
title: "Slack with Voice"
hackathon: "Alexa Skills Challenge: Life Hacks"
organization: "Amazon"
winner: true
words: 683
team_size: 1
has_repo: false
has_live: false
has_video: true
tags:
  - "project"
  - "domain/developer_tools"
  - "user/developer"
  - "substrate/code_repository"
  - "substrate/web_dom"
---

# Slack with Voice

> The ultimate work-from-home experience for Amazon Echo users

[Devpost](https://devpost.com/software/swv) · hackathon [[Alexa Skills Challenge- Life Hacks]]

## Facets

**domain** [[developer_tools]]
**user** [[developer]]
**substrate** [[code_repository]] [[web_dom]]

**stack** alexa-sdk, moment.js, node.js, slack-api

## How they structured the write-up

- slack with voice
- inspiration
- what it does
- invocation
- all available commands
- features
- source code
- what's next for slack with voice

## Body

Slack with Voice The ultimate work-from-home experience for Amazon Echo users Slack with Voice is a hackable voice user interface for Slack. It connects your Slack workspace with Amazon Echo. Inspiration Slack a digital workspace for millions of user. Just the way Alexa can read out emails and send messages, she should be able to read out and send our Slack messages too. Because that's where most of the work-chat happens. This is an incredibly useful "work from home" skill because it lets you collaborate with your team from the convenience of your home. Even if you don't do so, when you are at home afterhours & need to connect with your team for some reason, it is the best handsfree solution for Slack. There is one similar skill in the market, but the audience didn't seem very pleased with the functionalities. So I decided to build one for myself and later published it in Alexa Skill Store. What it does It can send & read messages from Slack (public or private channels & direct messages). You can also star messages, add emoji reactions, add new reply to a message & listen to all replies. We create an unified VUI for the users where all available commands (regardless of the command or the list that will be read out) result in a reading mode that supports Starring, Reactions, Replying, Reading Replies, Move back and forth in the list, Asking for help or to repeat the last messages, Stop or cancel actions. Invocation Alexa, open Slack Chat Alexa, open Slack Chat and read messages from General Alexa, open Slack Chat and send message to General All Available Commands SEND COMMANDS: "Send message to [Channel]" : Send message to public or private channel • Example: "Send message to general" "Send direct message to [Person Name]" : Send direct message (DM) to a person • Example: "Send direct message to John" READ COMMANDS: "Read messages from [Channel]" : Read message from public or private channel • Example: "Read messages from general" "Read direct messages from [Person Name]": Read direct message (DM) from a person • Example: "Read direct messages from John" "Read starred messages" : Read your starred messages ACTIONS IN READING MODE: All three Read commands above fetches one message at a time. Say "next" to read next message. "React [Reaction]" : React to a message, currently supported Reaction: "like", "dislike", "love", "ha ha", "wow", "sad", "angry" • Example: "React ha ha" "Star" : Star a message "Send reply": Reply to a message • Tips: "Reply [You message]" is a shortcut for this command, Example: "Reply I'm on my way" "Read replies": Read all replies to a message • "Read replies" command fetches 3 replies at a time. Say "more replies" to fetch next three. MISC. "Help" "Repeat" "Stop"/"Cancel" Features See the demo video for details Unified VUI Progressive Response Smart Name Resolution Mention/Custom Label Resolution Markdown to SSML Complete summary in response Source Code Head over to the Github Repository of this skill ( https://github.com/mehamasum/slack-with-voice ) Use model.json in Alexa Skill Kit Developer Console (ASK) to build the model. Save it and build it. Create a Slack app here https://api.slack.com with scopes: [users:read,chat:write:user,im:write,im:history,channels:read,channels:history,groups:read,groups:history,reactions:write,stars:write,stars:read] Save the Slack app credentials (Client ID, Client Secret, Verification Token) In ASK's "Account Linking" page put following information: Authorization Grant Type: Auth Code Grant Authorization URI: https://slack.com/oauth/authorize Access Token URI: https://slack.com/api/oauth.access Client ID: YOUR_CLIENT_ID Client Secret: YOUR_CLIENT_SECRET Client Authentication Scheme: Credentials in request body Scope: scopes listed above Put the generated Redirect URLs in your Slack App's whitelisted Redirect URLs Backend: Create a Lambda function and put the ARN in the ASK's "Endpoint" page Create an Environment variable in your lambda: APP_ID=YOUR_SKILL_ID Clone Soruce code git clone https://github.com/mehamasum/slack-with-voice.git cd slack-with-voice npm install Zip everything (including node_modules) and upload it to your Lambda What's next for Slack with Voice Add Search features Add support for "Files" and other non-textual message subtypes Find a way to handle multi-way messaging Icon copyrights: Alexandru Nastase ( https://dribbble.com/anodpixels ) Slack With Voice is not created by, affiliated with, or supported by Slack Technologies, Inc. <div