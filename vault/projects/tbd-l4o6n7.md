---
slug: "tbd-l4o6n7"
url: "https://devpost.com/software/tbd-l4o6n7"
title: "Intelligent Image Classifier"
hackathon: "Codegeist 2021"
organization: "Atlassian"
winner: true
words: 750
team_size: 5
has_repo: false
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/cross_origin_web"
  - "mechanism/vision_ocr"
  - "domain/civic_government"
  - "substrate/geospatial"
  - "substrate/video_visual"
---

# Intelligent Image Classifier

> Allows teams to automatically classify issues using multiple artificial intelligence algorithms. Filter or search for issues based on detected text or content within an image attached to a Jira issue.

[Devpost](https://devpost.com/software/tbd-l4o6n7) · hackathon [[Codegeist 2021]]

## Facets

**mechanism** [[cross_origin_web]] [[vision_ocr]]
**domain** [[civic_government]]
**substrate** [[geospatial]] [[video_visual]]

**stack** amazon-web-services, express.js, forge, node.js, rekognition, uikit

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for intelligent image classifier

## Body

Project Settings Inspiration We were inspired by a project we were working on with a local municipality where they wanted to be able to identify certain types of “work items” within their town and to classify them based on content that was attached to tickets that were submitted through their Jira Service Management portal. What it does The initial version of the Intelligent Image Classifier allows attachments to be scanned in the background once they are attached to a Jira issue. The images are scanned using various APIs and engines such as AWS AI Rekognition engine used to detect known content within images (computer vision), detect text that is found within an attached image, detect the file types (mime types) of attached images, look for explicit content and more. Once the images have been scanned, custom fields for the values that have been identified will be populated with the resulting values. This will allow users to use JQL to search for issues, create filters, etc. that include attachments that match various criteria. This enables use cases such as creating Jira Service Management Queues that are based upon things that are detected within attachments, using Jira Automation to automatically assign issues, tag with labels, etc.based on certain content identified in attachments, etc. How we built it The app is built using Forge, UI Kit, and Node.js / Express with a Web Trigger to detect when new attachments have been added to a Jira issue, jira-custom-field components for the custom fields, jiraAdminPage and jiraProject page UI Kit components for the Project Settings Page and Global Admin page. Challenges we ran into The biggest challenge was related to executing some of the APIs from within the Forge sandbox; initial attempts to do this by calling the AWS API directly from Forge failed because of limitations around crypto polyfill not working within forge. This required us to stream image bytes (not ideal for ultimate solution). Accomplishments that we're proud of We are proud that we’ve got something that we believe is innovative and that has a multitude of real-world use cases. We dealt with and solved some pretty difficult problems and learned a lot about Forge in the process! What we learned We learned a lot about the differences between Forge and Connect and the limitations and advantages of Forge. Some things are super easy in Forge but some of the limitations make other things more difficult. The fact that everything is sandboxed means that security is “built in” and much less to think about there. There’s also no server / backend required when using Forge vs Connect and performance can be better since it’s tied to the instance it’s installed into. What's next for Intelligent Image Classifier There’s a lot that we can do with this app. Here are a few use cases / features that we have thought of: Automatic actions can be added (without the need for users to set them up using automation or queuing) such as automatically assigning based on detections, automatically adding labels, populating selected custom fields, transitioning issues, etc. Blocking explicit content - If an image is attached that does not conform to company policy it can be automatically removed with a comment, activity entry, etc. added to the issue indicating that the attachment was blocked. There are many additional AWS / AI APIs that can be applied here. For example, we can use “custom labelling” to allow end users to apply domain knowledge and machine learning to attachments so that future attachments can be labeled with “custom” labels that each individual customer can use to train the app. For example, if there are screenshots of a certain application that are attached to JSM tickets, the users can manually tag these with labels (name of the application for example) and then after this is done a few times, the model will learn and automatically tag future images with these custom labels. Allowing the end user to specify their settings for the image recognition such as confidence levels, which features / engines should be enabled (globally and/or at the project level). Ability to search for other characteristics of files such as information found in EXIF data, date photo taken, GPS coordinates (location APIs, city, state, country, etc.), particularly useful for the municipality use case. Ability to scan and tag existing issue attachments based on a filter (this was something we had originally intended to include but Forge’s execution limit based on lambda made longer running tasks difficult). <div