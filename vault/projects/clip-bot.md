---
slug: "clip-bot"
url: "https://devpost.com/software/clip-bot"
title: "Clip Bot v2.0"
hackathon: "Power Up Automation"
organization: "UiPath"
winner: true
words: 414
team_size: 1
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "domain/developer_tools"
  - "user/developer"
  - "substrate/video_visual"
---

# Clip Bot v2.0

> Clip Bot is a reusable clipboard manager automation for integration with any agent-assisted UIPath project

[Devpost](https://devpost.com/software/clip-bot) · hackathon [[Power Up Automation]]

## Facets

**domain** [[developer_tools]]
**user** [[developer]]
**substrate** [[video_visual]]

**stack** clipboard, rpa, uipath, visual-basic

## How they structured the write-up

- v2.0 update
- inspiration
- what it does
- how i built it
- challenges i ran into

## Body

v2.0 UPDATE I have just published Clip Bot v2.0 on GitHub but have not yet written updated documentation or shot a new video. I will try to update these soon! v2.0 significantly adds and improves on the functionality/versatility of v1.0. Inspiration I was inspired to create an agent-assisted automation because I feel like this category of automation often gets left by the wayside in developers' rush to create "fully automated" robotics programs. I think agent-assisted automation can be very useful/powerful, and wanted to show that here. I settled on the concept of Clip Bot (A) because I find the concept of a clipboard manager to be very useful in my own day-to-day computer usage and (B) because I was intrigued by the "Monitor" activity and wanted to learn more about how to use it. What it does The Clip Bot is an agent-assisted automation component allowing users to copy items (text, images, files) to and from a multi-item "clipboard" while assigning a unique shortcut to each item for quick and dynamic pasting of multiple items (much like a clipboard manager). Alternatively, the user may choose/pre-load a set of items to the robot's "clipboard" at the start of the process, allowing the user to quickly paste any desired items from that set using pre-defined shortcuts. See included "Instructions" file for full details on how to use the robot. How I built it The Clip Bot is composed entirely of default UIPath activities and workflows. A couple "Invoke Method" activities were necessary to set non-text items (images and files) to the clipboard, but the rest of the workflow consists of common activities that most UIPath users should quickly be able to recognize and modify as needed for their own processes. Challenges I ran into Possibly the biggest challenge I ran into was figuring out how to prevent the robot from sending the same command multiple times. The robot runs on a tight loop that contains a "Monitor" activity on any user keyboard input. An example of the issue I would run into was that the loop would go by so quickly that the robot would paste an item from the "clipboard" two or three times rather than just once in a single press of the assigned shortcut keys. My solution to this was a couple of "Do While" loops the user will notice in my workflow that do nothing but wait for the most-recently pressed key to be released before allowing the workflow to continue. <div