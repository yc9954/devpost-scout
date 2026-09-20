---
slug: "roku-dev-tools"
url: "https://devpost.com/software/roku-dev-tools"
title: "Roku Dev Tools"
hackathon: "The Postman API Hack"
organization: "Postman"
winner: true
words: 572
team_size: 1
has_repo: false
has_live: true
has_video: false
tags:
  - "project"
  - "domain/developer_tools"
  - "user/developer"
  - "user/general_public"
  - "substrate/web_dom"
---

# Roku Dev Tools

> A collection of useful commands and examples to aid in Roku TV development. Control your Roku device from Postman! Debug and test your Roku projects within Postman.

[Devpost](https://devpost.com/software/roku-dev-tools) · hackathon [[The Postman API Hack]]

## Facets

**domain** [[developer_tools]]
**user** [[developer]] [[general_public]]
**substrate** [[web_dom]]

**stack** javascript, postman, roku, slack

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for roku dev tools

## Body

Launching Netflix on Roku using Postman Inspiration As an independent developer who has created channels for Roku, I found that there is a steep learning curve due to the platform supporting the proprietary BrightScript and SceneGraph SDKs. I saw an opportunity to use Postman to help in the debug process, and even to connect Roku devices directly with other platforms such as Slack. There is a powerful, yet little known API called External Control Protocol that allows developers to send commands to directly manipulate a Roku device or TV on a local area network. This Workspace for Postman contains references and examples of the power of ECP. What it does Note: you must have a Roku device on your network to test the API. There are certain commands that will only work on integrated Roku TVs, but most commands will work on all Roku devices (even standalone devices). Roku Dev Tools provides examples of using the External Control Protocol, which can be used to do anything from simulating a Roku Remote, installing new channels, or even deep linking to content within existing channels. There are four featured demos in this workspace: (Monitor demo) Send Currently Tuned TV Channel to Slack Using a monitor, we can schedule the Roku ECP API to periodically send the currently tuned TV Channel info to Slack. It will return a response that will include info such as the TV channel number, name, signal strength and program description. Launch Netflix This example shows how to automatically load the Netflix channel on your Roku device. After opening Netflix, it will post to Slack. Turn off TV after 30 seconds This script will wait 30 seconds before turning off your Roku TV. You can adjust the time by changing the Pre-request script. It also sends a notification to Slack. Send available TV channels list to Slack This demo is compatible with Roku TVs and will send the available list of TV channels to Slack. How we built it This was built in Postman using the Workspace, Collections, Monitor, and Environment components, along with folders containing commands and examples. One of the examples uses a Monitor to periodically send the currently tuned TV channel info to slack. It basically will post a notification in Slack that lets you know what is currently on the TV, including the name of the program and description and channel number. The Slack webhook URL, along with a few other variables, can be configured using the Environment called "Roku TV". Challenges we ran into Learning how to effectively use Postman and understand some of the platform's concepts were a welcome challenge at first, but then I watched some of the YouTube videos that helped explain key concepts. The Developer 101 video was very helpful. Accomplishments that we're proud of I was able to identify and categorize key components of the ECP API and group them into folders within the collection, and come up with a few demo examples of how these tools can be used that I hope will inspire potential developers. What we learned The public Postman examples helped to inspire some of the examples. For example, one demo features the ability to send available TV channel information to Slack. What's next for Roku Dev Tools I hope to expand this collection by offering more demos and examples of interfacing with Roku devices. I'm currently working on a demo that integrates with Microsoft Teams. <div