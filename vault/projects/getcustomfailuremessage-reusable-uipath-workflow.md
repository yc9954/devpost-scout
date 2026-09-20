---
slug: "getcustomfailuremessage-reusable-uipath-workflow"
url: "https://devpost.com/software/getcustomfailuremessage-reusable-uipath-workflow"
title: "GetCustomFailureMessage"
hackathon: "Power Up Automation"
organization: "UiPath"
winner: true
words: 374
team_size: 1
has_repo: true
has_live: false
has_video: false
tags:
  - "project"
  - "substrate/geospatial"
  - "substrate/sensor_telemetry"
---

# GetCustomFailureMessage

> UserDefined failure messages for Exceptions

[Devpost](https://devpost.com/software/getcustomfailuremessage-reusable-uipath-workflow) · hackathon [[Power Up Automation]]

## Facets

**substrate** [[geospatial]] [[sensor_telemetry]]

**stack** uipath

## How they structured the write-up

- inspiration
- what it does
- how i built it
- challenges i ran into
- accomplishments that i'm proud of
- what i learned

## Body

Reusable workflow Inspiration There were various scenarios where we need to specify exception messages which can be easily understandable by the business user as with normal exception handling we cannot achieve this and needs to create the custom exception class every time. To avoid this I created a reusable component which gives the custom failure message based on the exception occurs in the script. What it does This Reusable workflow will take System.exception as in argument and provides the custom failure message defined by the user in Mapping excel sheet which contains various exception types and messages as out argument. The excel mapping sheet can be customized by the user at any point in time. Example : If Uipath is unable to recognize any elements on screen it will give exception message as cannot find UI element corresponding to this selector, user can write customize message for this as UiElement is Not Present on the screen in our mapping sheet so whenever uipath encounters this exception type the failure reason will be the one mentioned above. How I built it I developed this using Uipath Studio and with the excel mapping sheet Challenges I ran into So the challenge is when I want to define my own custom exception message regardless of the exception type then how to accomplish this?. So I used uipath.core.BusinessRuleException to define own custom exception messages and it will be handled in the reusable workflow. Example: If there was a scenario if I encountered a popup I need to raise an exception saying System ABC is not responding .If I use any specific exception type then the user-defined message in mapping sheet will override this message. So to overcome this I have implemented uipath.core.BusinessRuleException where the reusable workflow first check for exception type in mapping sheet if not found then it will check whether it is the business exception then write that corresponding message Accomplishments that I'm proud of This reusable component is very helpful while implementing exception handling in the project as it helped in updating the user-defined failure messages in summary reports, log files and kibana reports. What I learned I have learned about various exception types and about uipath business rule exception which is very helpful.' <div