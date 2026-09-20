---
slug: "diagnocenter"
url: "https://devpost.com/software/diagnocenter"
title: "Diagnocentre"
hackathon: "Atlas Madness"
organization: "Google"
winner: true
words: 621
team_size: 3
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "domain/health_clinical"
  - "substrate/structured_db"
  - "substrate/video_visual"
  - "substrate/web_dom"
---

# Diagnocentre

> DiagnoCentre is a valuable platform that provides quick and accurate diagnoses for medical reports and images. Our website is responsive and accessible, and currently supports four major diagnoses.

[Devpost](https://devpost.com/software/diagnocenter) · hackathon [[Atlas Madness]]

## Facets

  <sub>weak: cross_origin_web</sub>
**domain** [[health_clinical]]
**substrate** [[structured_db]] [[video_visual]] [[web_dom]]

**stack** css3, docker, github, html5, javascript, kubernetes, mongodb, mongoose, node.js, python, tailwind

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for diagnocentre

## Body

Home Screen Sign Up Page Log In Page After Logging Home Page Our Services#1 Our Services#2 Manual Diagnosis Form Anemia Diagnosis Form Anemia Detection Result Image Diagnosis Form Form After uploading an Image Fracture Detection Result User Collections Inspiration The inspiration for Diagnocentre came from the need for a quick and accurate diagnosis for medical reports and images. We realized that there was a gap in the market for a platform that could perform diagnoses on reports and images quickly and accurately at any given point. It is not an app but a Website that is more easily accessible to users all around the world. What it does Diagnocentre is a website that provides quick and accurate diagnoses for medical reports and images. The platform can take X-ray images and determine if they are fractured or not, or take tumor scans and identify the type of tumor. Additionally, it can analyze CBC report values or ECG report values and provide a one-line diagnosis. The images after the result of fracture and tumor diagnosis save the photo with the result on your profile page where you can see or delete as per the user's choice. How we built it Diagnocentre was built using a combination of medical image processing and web development technologies. Advanced machine learning was used for medical image processing and HTML, CSS, and JavaScript with Tailwind CSS were used for front-end web development. For the backend, Node.js with Express and various other Node packages were used. The website also uses a database called MongoDB Atlas, which is used to store user data and provide a personalized collection page for the user. For storing images, Google Cloud Bucket was used. The website uses machine learning models to process radiographic images and report values. Two of the models use CNN, which are Fracture Detection and Tumor Analysis. Fracture detection uses VGG19 with batch normalization, and Tumor Analysis uses a custom architecture. The other two models, which are Anemia Detection and Heart Health Detection, use regression models. The website is deployed on Google Cloud's GKE cluster, making it accessible to all users. Challenges we ran into One of the main challenges the team faced was ensuring the accuracy of the diagnoses. Medical image processing is a complex field, and it was important to ensure that the algorithms used were accurate and reliable. We used multiple types of models in a trial-and-error way to get to the most optimal solution so that they could achieve at least 90 percent accuracy in all their models for better results. Additionally, connecting the Node.js website with ML models was tricky as they had never done that before. After creating the models, they also had to train the models for which they used Google Colab with TensorFlow Enterprise. Accomplishments that we're proud of We are proud of the accuracy and accessibility of the diagnoses provided by Diagnocentre. Additionally, they are proud of the responsive and accessible design of the website, which ensures that all users can access the platform regardless of the device they are using. What we learned We learned a lot about medical image processing and web development during the development of Diagnocentre. They also learned about the importance of accuracy and reliability in medical diagnoses and the challenges of ensuring that a website is responsive and accessible to all users. What's next for Diagnocentre In the future, Diagnocentre plans to expand its services to include more types of medical reports and images. Additionally, we plan to continue improving the accuracy and reliability of the diagnoses provided by the platform. We also plan to explore new technologies and techniques in medical image processing to ensure that Diagnocentre remains at the forefront of the field. <div