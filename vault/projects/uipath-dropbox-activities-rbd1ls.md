---
slug: "uipath-dropbox-activities-rbd1ls"
url: "https://devpost.com/software/uipath-dropbox-activities-rbd1ls"
title: "UIPath.Dropbox app connector"
hackathon: "Power Up Automation"
organization: "UiPath"
winner: true
words: 618
team_size: 1
has_repo: false
has_live: false
has_video: true
tags:
  - "project"
  - "domain/developer_tools"
---

# UIPath.Dropbox app connector

> A custom Dropbox app connector for UIPath (already used in custom UIPath Dropbox activities)

[Devpost](https://devpost.com/software/uipath-dropbox-activities-rbd1ls) · hackathon [[Power Up Automation]]

## Facets

**domain** [[developer_tools]]

**stack** c#

## How they structured the write-up

- inspiration
- what it does
- how i built it
- challenges i ran into
- accomplishments that i'm proud of
- what i learned
- what's next for uipath.dropbox.activities

## Body

Inspiration The idea to create custom activities for Dropbox came to me when one of my friends asked me to help him out with the some integration issue he was having with the Dropbox JS SDK. What it does The project contains custom UIPath activities which facilitate automation of Dropbox tasks with UIPath Studio. The project contains: A Dropbox application connector (responsible for communicating with Dropbox by reusing the Dropbox .Net SDK) A set of custom activities (create file, copy, move, delete, upload, download, other) to be used by UIPath Studio to automate tasks for Dropbox How I built it I didn't have any experience with Workflow Foundation so I ended up reading some chapters from "pro wf 4.5" to get a general idea about the concepts and then "microsoft windows workflow foundation 4 cookbook" for extra details. Then I started coding. I started with a single solution with 2 projects, one with a dropbox connector and one with a console test app to use the connector and see if/how it works. Then I had to create the activities and found myself blocked because I wasn't sure how to create an async one. So I did some research and found UIPath community activities which had some examples. I investigated those, found examples of how to create async activities and after this, everything just worked without any major issue. Challenges I ran into Initial blocker was definitely the async activity and not understanding how exactly to create that Creating the package and installing it in UIPath was easy. It was not easy to understand why the activities were not visible in the IDE. Still have no clue why it worked in the end I had some issues with nulls being thrown in some activities and I was honestly expecting to get a better stack trace. I did not find anything useful in the ones I got so I had to go through the entire activity to take a guess where the problem might be Something weird happened while preparing for the demo. I was doing changes to some activities and even though I uninstalled the old version of the package and only then installed the new version some activities did not get an update with their new variable names Some of my custom activities appear in UIPath Studio under an "Activities" subfolder while other directly under "UIPath.Dropbox" group Accomplishments that I'm proud of Definitely being able to submit (even though the current state of the implementation has some small bugs) Being able to read a small book and get started up although I felt I did not know enough Feeling lost along the way but pushing forward until everything starts to work out What I learned It is definitely possible to create something for the communities as long as you invest the time It is very challenging to decide on the smallest documentation needed to get me started If you need inspiration there's a huge chance somebody did something similar on github lol Contribution is awesome! What's next for UIPath.Dropbox.Activities Definitely fix the issues mentioned in the README file which I found while preparing to record the video demo Add extra authentication support Exception handling (for example if you create a folder which already exists current activity does not fail gracefully) Improve the documentation in the README file and also in the code Maybe add tests? Not sure here since it's the first time I'm dealing with WF. Any suggestion will be appreciated Do an in-depth investigation of what is the complete set of actions that the Dropbox SDK supports and create a list of issues which will track the implementation of these. PR's will be appreciated ;). <div