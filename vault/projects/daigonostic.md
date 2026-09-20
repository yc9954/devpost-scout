---
slug: "daigonostic"
url: "https://devpost.com/software/daigonostic"
title: "dAIgnostic"
hackathon: "hack:now"
winner: true
words: 744
team_size: 2
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/structural_withholding"
  - "domain/health_clinical"
  - "user/clinician"
  - "user/patient_family"
  - "user/researcher"
  - "substrate/code_repository"
  - "substrate/geospatial"
  - "substrate/structured_db"
  - "substrate/video_visual"
  - "substrate/web_dom"
---

# dAIgnostic

> Data labeling for COVID-19 lung scans and RT-PCR data

[Devpost](https://devpost.com/software/daigonostic) · hackathon [[hack-now]]

## Facets

**mechanism** [[structural_withholding]]
**domain** [[health_clinical]]
**user** [[clinician]] [[patient_family]] [[researcher]]
**substrate** [[code_repository]] [[geospatial]] [[structured_db]] [[video_visual]] [[web_dom]]

**stack** css, express.js, html, javascript, microsoft-api, mongodb, node.js, react, recharts

## How they structured the write-up

- inspiration
- what it does
- how i built it
- challenges i ran into
- accomplishments that i'm proud of
- what i learned
- what's next for daigonostic

## Body

PCR Bounding boxes Inspiration COVID-19 diagnostics are one of the most important components in flattening the curve. Currently, testing relies on manual diagnosis of lung scans (CT/MRI), ELISA data, or PCR data, which is very time consuming. For images, rather than having cardiologists spend time to view lung image data, convolutional neural nets (CNNs) have been viewed as a way to diagnose patient image data, especially since COVID-19 patients have distinct markings in their lungs. Despite the image datasets that currently exist, CNNs are very data hungry and need annotated images to reach their full potential. We realized that currently, there are doctors who are not front-line physicians that can annotate these MRIs or CT-scans for training while they are at home. They can also draw bounding boxes to teach machine learning (ML) algorithms how to label specific features that distinguish COVID-19 patients. For lab data, RT-PCR and antibody tests are the industry standard. They involve a variety of reagents and biochemical steps. Ultimately, the final results of these tests are often amplification graphs or florescence data that can be modeled with CSV or Excel files. However, labeling this data requires scientists to manually look at each graph and annotate it. If an existing repository of labeled graphs could be used to train an ML algorithm, scientists could focus more of their time on the work that actually requires humans, such as the lab protocol steps. This would be critical in saving time for the noble researchers that are leading diagnostic efforts. What it does dAIgnostic is a platform for medical professionals and researchers to post data that are either pre-labeled or need labeling. Users sign up and can create tasks that involve images and graph data(RT-PCR). They can assign these tasks to specific other users or they can make these tasks public for everyone to label. After their tasks are labeled, they can receive annotations in JSON format. In addition to creating tasks, users can also label tasks. For images, they can draw bounding boxes and save these coordinates for the person who assigned the task. For PCR data, they can visualize the CSV data and view the coordinates of each point. Users can filter through tasks that they've already completed, haven't completed, have assigned, and public tasks available to all in our navigation menu. Ultimately, this creates a dynamic ecosystem where physicians and researchers on the front-lines create tasks for those who are currently working at home. How I built it Our stack was React, MongoDB, Express, and Node.JS. All of our front end interactions involved React components where the user would interact with the page to send requests and data back to our MongoDB database. Images were stored as Base64 strings and CSV data was stored as JSON. When we graphed the RT-PCR data, we converted it from JSON to graphical format using the Recharts library. The bounding box implementation was done with Canvas tags in React. We also added an API for users to import existing email contacts from Outlook if they want to assign tasks specifically to someone in their own community with the Microsoft API. Our website is also HIPAA compliant because all data is de-identified. Challenges I ran into It was difficult to find the appropriate implementation for the bounding boxes. Initially, we tried to store the boxes as tags but found that to be too challenging so instead, we manipulated the Canvas tag to consistently update the image whenever events were detected by the user clicking and dragging on the screen. Accomplishments that I'm proud of We are proud that we built a full stack application that allows users to modify data and store it on a database for task assigners to actually use in training their ML algorithms. Manipulating the different types of data that we had was challenging but rewarding once we could implement both CSV and image data. We believe that the temporal and monetary expense of labeling is a massive bottle-neck to using ML in the fight against COVID-19 so a platform that standardizes this labeling for everyone would be influential in this effort. What I learned Improved full-stack web dev skills. What's next for dAIgonostic Implement mass file uploading with GridFS. Make our UI able to cycle through different tasks without having to return to home screen. Handle anti-body testing data and create a forum for researchers and medical professionals to specify more about their tasks and datasets they have. <div