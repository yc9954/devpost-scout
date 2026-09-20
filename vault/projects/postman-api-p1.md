---
slug: "postman-api-p1"
url: "https://devpost.com/software/postman-api-p1"
title: "Postman OneDrive API Integration"
hackathon: "The Postman API Hack"
organization: "Postman"
winner: true
words: 351
team_size: 1
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "domain/developer_tools"
  - "user/developer"
---

# Postman OneDrive API Integration

> API collection to perform OneDrive Operations

[Devpost](https://devpost.com/software/postman-api-p1) · hackathon [[The Postman API Hack]]

## Facets

**domain** [[developer_tools]]
**user** [[developer]]

**stack** .net, api, azure, c#, postman, wpf

## How they structured the write-up

- inspiration
- what it does
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for postman api

## Body

Inspiration As a developer, sometimes it becomes easy if we can sync our folders/files to OneDrive with exclusion of some of the subfolders. Graph API helps in this case to create single API calls to upload file (large or small). Current OneDrive clients doesn't support exclusion of subfolders if folder is being synchronized. Idea here is to create individual API calls for files you need back up for. What it does WPF application (auto generated from Azure Portal & edited with some code changes to update postman collection variable with access token) requests Azure token for the Azure app and updates Postman collection variable with that value. Inside Postman desktop app, through MyOneDriveAPICollection, you can view OneDrive files, create folder, upload file(large and small) and delete files. ## How we built it Created an Azure app with necessary permission setup to access user's files. Used auto-generated WPF app to request authentication and authorization. Modified this app to update postman collection variable using Postman API. Added API calls to collection to perform various operations on OneDrive. Challenges we ran into There is no way to update postman collection variable's current value from outside. Meaning, through collection update, you cannot update variable's current value and while making API calls, postman app expects current value to be something else, it won't provided Initial value. This was a big challenge for me in order to automate this whole process. Accomplishments that we're proud of I was able to complete this project despite having very limited resources on how to access graph API (from start to end). Despite having challenge above, I found a workaround that allows me to set current value of a variable through pre-request script and later all requests can leverage the collection variable's current value. What we learned Postman API, Graph API. What's next for Postman Api Idea is to take this collection to next level by modifying app to accept folder path with folders/files to exclude and generate this collection for the given set of files/folders. For example, any nodejs project can be synched to OneDrive without including node_modules folder. <div