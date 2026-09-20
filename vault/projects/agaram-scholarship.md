---
slug: "agaram-scholarship"
url: "https://devpost.com/software/agaram-scholarship"
title: "Agaram Scholarship"
hackathon: "DocuSign Good Code Hackathon"
organization: "Docusign"
winner: true
words: 444
team_size: 1
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "domain/developer_tools"
  - "domain/education"
  - "user/educator_student"
  - "substrate/structured_db"
---

# Agaram Scholarship

> Web application that connects people from all backgrounds to get scholarship support from the nonprofit Agaram Foundation, using DocuSign's eSignature API.

[Devpost](https://devpost.com/software/agaram-scholarship) · hackathon [[DocuSign Good Code Hackathon]]

## Facets

  <sub>weak: provenance_signing</sub>
**domain** [[developer_tools]] [[education]]
  <sub>weak: civic_government</sub>
**user** [[educator_student]]
**substrate** [[structured_db]]
  <sub>weak: document_pdf</sub>

**stack** angular.js, docusign-click-api, docusign-esignature, docusign-templates, mongodb, node.js

## How they structured the write-up

- how i built it
- challenges i ran into
- whats next

## Body

Inspiration In India, the education system has lot of issues in it. Majority of the children wants to pursue higher education and due to family and financial conditions lot of students are dropping out from schools even from intermediate classes. To deal with this drop-out situation, the government and various other non profit organizations like Agaram Foundation, have come up with suitable aids to meet their financial needs. Currently the scholarship process is by filling the forms and sending it to the organization by post manually. I noticed that this process is a huge burden to both the sides and especially during this Covid-19 many people were not able to complete the entire process. So I thought of creating a web application to create scholarship agreements that would benefit both the sides. It would also benefit the environment, as no postage is required and documents don't need to be wasted. What it does The application provides a way for both creating and applying the scholarship. Admins can create the desired scholarship for their needs based on the eligibility and criteria and it will automatically generate a template for the scholarship. They can also use this scholarship template to send the application to students manually from docusign dashboard. The students can then apply for the scholarship from the dashboard which in turn gets the consent from them using click api and redirects them to the form which needs to be filled by them to avail the scholarship using e-signature api . How I built it This app was built using the following technologies Frontend - Angular Backend - NodeJS Database - MongoDB I have used the docusign sdks to integrate with the docusign API Challenges I ran into The main challenge I have faced during this entire hackathon is building this entire client server architecture from the scratch which I haven't done before. Getting this application integration with the docusign API and also placing the custom docusign variables in appropriate positions to create a custom template. ## Accomplishments that I'm proud of I am proud that I was able to build and publish this entire project during this course of this hackathon and also I have learnt using many features of docusign API's which I could use in my future projects as well. I have also built this entire application generic so as any of them can clone and start using this application and customize it according to their needs. Whats next Need to build a more secure way of authentication for admin instead of just password. Make a chatbot to answer all the commonly asked queries Increase the responsiveness of the web application <div