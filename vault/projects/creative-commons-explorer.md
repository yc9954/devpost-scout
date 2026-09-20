---
slug: "creative-commons-explorer"
url: "https://devpost.com/software/creative-commons-explorer"
title: "Creative Commons Image Explorer"
hackathon: "The Postman API Hack"
organization: "Postman"
winner: true
words: 435
team_size: 1
has_repo: false
has_live: true
has_video: false
tags:
  - "project"
  - "mechanism/sensor_fusion"
  - "domain/developer_tools"
  - "domain/education"
  - "user/developer"
  - "user/educator_student"
  - "user/general_public"
  - "user/researcher"
  - "substrate/video_visual"
---

# Creative Commons Image Explorer

> This is a public collection to help developers explore, visualize, and iterate on digital media in the creative commons — such as open access images from museums under the CC0 license.

[Devpost](https://devpost.com/software/creative-commons-explorer) · hackathon [[The Postman API Hack]]

## Facets

**mechanism** [[sensor_fusion]]
**domain** [[developer_tools]] [[education]]
**user** [[developer]] [[educator_student]] [[general_public]] [[researcher]]
**substrate** [[video_visual]]

**stack** handlebars.js, postman

## How they structured the write-up

- inspiration
- what it does
- potential uses for this api workspace
- challenges i ran into
- accomplishments that i'm proud of
- what i learned
- what's next for creative commons explorer

## Body

Image Grid visualizer in Postman Lightbox visualizer in Postman Inspiration I wanted to create a collection that allows developers with limited financial resources to start iterating and creating projects with digital media immediately. Utilizing open access APIs from museums and other organizations, this workspace aims to empower developers with the tools to access images What it does This Postman public workspace collects api calls for museums that offer open access images under the Creative Commons Zero license. These images are free to use for ANY purpose, commercial or otherwise. Many of these images are of great cultural and historic importance, not to mention super fun to browse through! The public workspace is the main component of my submission, but I also spun up a simple react app demonstrating a possible use for the collection here . Potential uses for this API Workspace Develop an app for students to digitally explore works of art that are normally only available if you have the privilege of visiting a museum in a metropolitan area Create an IoT picture frame that selects a new piece of artwork to display on your wall every day Create an academic research tool that allows students and scholars access to metadata about certain topic or subjects of historical artwork Create a print on demand service that allows users to order art prints and clothing made from public domain and creative commons artwork Challenges I ran into Some of the documentation for these open access APIs are a little spotty, but I did my best to port over specific details in the parameter descriptions. Accomplishments that I'm proud of I am very happy with how the visualizations for the Cleveland Museum of Art's API collection I created came out. One of the most important components of the data from these APIs is the actual images — it is such a nice feature in Postman to be able to switch over from the JSON and view the response as images as well in the visualizations tab. You can explore a beautiful grid of historic artwork right from the comfort of your Postman app, complete with lightbox navigation and QR code support! What I learned The Postman visualizer is so versatile! You can do so much more than charts or graphs. you can allow What's next for Creative Commons Explorer I would like to flesh out the api calls for the museums and chain them together in a way that allows developers to get off the ground quicker. There are several other museums that have APIs which can be added to the workspace as well. <div