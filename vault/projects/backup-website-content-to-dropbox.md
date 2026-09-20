---
slug: "backup-website-content-to-dropbox"
url: "https://devpost.com/software/backup-website-content-to-dropbox"
title: "Backup Website Content to Dropbox"
hackathon: "The Postman API Hack"
organization: "Postman"
winner: true
words: 684
team_size: 1
has_repo: false
has_live: true
has_video: false
tags:
  - "project"
  - "domain/developer_tools"
  - "user/developer"
  - "substrate/code_repository"
  - "substrate/web_dom"
---

# Backup Website Content to Dropbox

> No more headache over migrating to a new web hosting platform. Use this collection to back up your website content to a Dropbox folder. When you move, simply plop this folder into your new project.

[Devpost](https://devpost.com/software/backup-website-content-to-dropbox) · hackathon [[The Postman API Hack]]

## Facets

**domain** [[developer_tools]]
**user** [[developer]]
**substrate** [[code_repository]] [[web_dom]]

**stack** api, dropbox, github, javascript, postman

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for backup website content to dropbox

## Body

Inspiration Like many developers, I build my own website using a static site generator, namely Gatsby.js. That means both my code base and site content live in the same repository. I'm happy will all the cool things I've learned from building a static site, but somehow I can't help feel like there is something wrong with putting both source codes and blog content in the same place. There are several problems with this approach, but the most vexing thing is how to move the blog content to a new platform painlessly? As a curious developer, I often feel the itch to try out a new site builder, like Next.js, Nuxt, Eleventy etc. Currently, my blog content lives in an unmemorable folder inside a folder that stores all the codes for my website. That folder looks just like any other innocuous folder in my laptop, but it is a cumulation of thousands of unpaid, thankless hours spent on researching, writing, retouching, and editing. I can imagine that when I want to move to Next.js, I will waste a bit of time scratching my head while finding where my blog content is located. What it does Retrieve files and directories inside a target directory in a Github repository. If this directory contains child directories that in turn contains more files, make extra requests to retrieve those files. Loop through each file in a child directory, grab the download url for each file and upload it to Dropbox. Repeat for the remaining child directories. How we built it I spent a bit of time trawling through the documentations for Github API and Dropbox API. At first, I had no idea where to start. I didn't know how to grab download links for each file in the target directory. Then I discovered that there is a Github API endpoint that allows users to get all the files from a directory. The response for that API contains a download url for each file. Once I have the download url for all the files in the target directory, I'm at a loss as to how to upload them to Dropbox. Do users have to run a request to download Github files to their local machine, then run another request to post those files to their Dropbox folder? That would surely slow down the process. It turns out that there is a Dropbox API that takes a download URL, a file path and saves the content of that URL to the given path in the user's Dropbox folder. This means I can automate the whole process to my heart's content. Challenges we ran into The most important part of the building this collection is to create a cache to avoid duplication. I don't know how big my users' Github directories are, so I have to write an algorithm to take stock of files that have already been backed up and avoid re-uploading files that haven't changed since the last backup. The next challenge is figuring out a way to run a request dynamically several times. For example, if a directory has 16 files, that means 16 requests to upload to Dropbox. Each request only differs in the file path and its download url. How do I program it so that users only need to click the run button once, then Postman will run the remaining 15 requests automatically?It takes a long time of testing and debugging to write a script that makes this idea possible. Accomplishments that we're proud of Use hash table to cache the already backed-up content and avoid duplication. This is so important as your directory gets larger. Run a request dynamically with collection runner and Postman's function setNextRequest() . What we learned There are too many things I've learned to count, but the most memorable thing is data structure. I've been neglecting that topic for a long time, and now I incidentally fell into it thanks to Postman. What's next for Backup Website Content to Dropbox Integrate this collection with a Postman monitor to schedule the backup so that users only have to run it once!. <div