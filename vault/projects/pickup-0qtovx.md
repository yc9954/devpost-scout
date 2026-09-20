---
slug: "pickup-0qtovx"
url: "https://devpost.com/software/pickup-0qtovx"
title: "Pickup"
hackathon: "PennApps XII"
winner: true
words: 367
team_size: 4
has_repo: false
has_live: true
has_video: false
tags:
  - "project"
  - "mechanism/voice_speech"
  - "domain/education"
  - "domain/retail_commerce"
  - "domain/security_privacy"
  - "substrate/document_pdf"
---

# Pickup

> Forget cloud storage - with Pickup you can leave files on your hard drive ready to be picked up anytime, anywhere

[Devpost](https://devpost.com/software/pickup-0qtovx) · hackathon [[PennApps XII]]

## Facets

**mechanism** [[voice_speech]]
**domain** [[education]] [[retail_commerce]] [[security_privacy]]
**substrate** [[document_pdf]]

**stack** asp.net, azure, bash, c, c#, cocoa, ios, mac, node.js, objective-c, onedrive, python, ssh

## How they structured the write-up

- the inspiration
- the mission
- how it works
- the technology stack
- obstacles and difficulties

## Body

The Inspiration The inspiration for Pickup is two-fold. We've all forgotten important files on our home computer, be it homework assignments or shopping lists. Pickup allows users' files to never be more than a few taps away. We also wanted to change how people access their files. Cloud storage has several limitations - it requires you to upload your important files to third party cloud services, not all of whom can be trusted. Even the best intentioned, most purportedly secure sites are vulnerable . In addition, you can only store so much on the cloud for free. The Mission We wanted to give users an alternative to cloud storage. Instead of the need to upload every document to the cloud or use a bulky remote desktop to view files, users should have the freedom to interact with their computer files, anytime, anywhere. How It Works First we perform a one time installation to pair your phone with your laptop. After that, users can SSH into their laptops (even if they're sleeping) from anywhere, at anytime with only the computer and account password. Users then have access to the full file system for either searching, using the voice command, or through our browse function. Upon finding the right file, users have the option to either upload the file to OneDrive, preview it on their phone, or send an email to themselves or any other person with the file as an attachment. Pickup supports all file types for email and uploading! The Technology Stack We used node.js, ASP.NET, Microsoft Azure web services to create a backend for our application. We also built a client mobile app for iOS with Objective-C. In addition, we wrote a suite of bash scripts that run in remote ssh sessions to retrieve files from a user's computer. Obstacles and Difficulties Azure deployment - difficulties with having things ported to DOS - decided not to use a Linux box - some NPM package platform problems Magic Packets - didn’t wake up the computer over WAN originally Azure Storage - couldn’t upload files without corruption that weren’t plain text Well's Fargo Center uses NNNAT in a WDS system, which made it impossible to test ssh <div