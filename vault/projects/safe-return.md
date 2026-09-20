---
slug: "safe-return"
url: "https://devpost.com/software/safe-return"
title: "Safe Return"
hackathon: "The HCL-Pega Pathbreaker Hackathon"
organization: "HCL"
winner: true
words: 649
team_size: 2
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/sensor_fusion"
  - "mechanism/vision_ocr"
  - "domain/civic_government"
  - "domain/health_clinical"
  - "domain/labor_employment"
  - "domain/security_privacy"
  - "domain/supply_logistics"
  - "substrate/document_pdf"
  - "substrate/video_visual"
  - "substrate/web_dom"
---

# Safe Return

> An end-to-end solution for Return to Work strategies ensuring employees' safety, workplace, and transport arrangements in this pandemic.

[Devpost](https://devpost.com/software/safe-return) · hackathon [[The HCL-Pega Pathbreaker Hackathon]]

## Facets

**mechanism** [[sensor_fusion]] [[vision_ocr]]
**domain** [[civic_government]] [[health_clinical]] [[labor_employment]] [[security_privacy]] [[supply_logistics]]
**substrate** [[document_pdf]] [[video_visual]] [[web_dom]]

**stack** css, html5, javascript, pega

## How they structured the write-up

- inspiration
- what it does
- how we built it
- key points of this solution
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- future enhancements for safe return

## Body

Self service login screen Manage Request screen New request screen Health check screen Interest Survey Location based office access Get more information screen Manage request screen Dashboard for managers Get additional info from user Access Code Graphs for data You can access this project PPT here: https://docs.google.com/presentation/d/1QlnXdaIjZYobO-S9V7GuLrSXsvaFiv5-/ Inspiration As you all are aware COVID pandemic is upon us. As most of the employees are vaccinated, several Organizations are planning to move a part of their workforce back to Office. For all organizations, the Importance of Employee's health is paramount. They must ensure that the employees are fit enough to return to the workplace and ensure that enough safety arrangements are made to welcome them. Arranging workplace based on employee data. Employees should be given the flexibility to join the nearest office as well. Organizations should also follow regional government protocols mandated while these processes such as mandatory vaccination, Temperature monitoring, PPE Kits Provision, etc., Handling all these activities is a big task for a huge organization. What it does The above problem is solved by using a Pega solution called “Safe Return” build in Pega 8.6. The solution consists of Mashups interacting with employees from the employee portal runs on the company intranet and processing the cases. From this solution, we can able to do following Get daily health updates from employees Get up to date vaccination information from the employees Track the Return to office requests for the available offices Handle Transport requests if needed by employees Track the employee health after visiting the office Manage the office sanitization schedules Find and predict the interested employees who are ready to return back to the office How we built it We built using Pega 8.6 Community Edition and For Self Service - HTML, CSS, and JS. For the entire architecture please view: https://docs.google.com/presentation/d/1QlnXdaIjZYobO-S9V7GuLrSXsvaFiv5-/ Key points of this solution Ability to capture Employee Vaccination Status at any time. Ability to capture Employee Health Status at any time. Ability to reject requests when Health is not good before visiting the workplace. Ability to track employees who are sick after visiting Workplace. Ability to capture return interest to workplace interest and prepare a plan based on it. Ability to prepare return plan using Vaccination Status and Health Status data Challenges we ran into We faced challenges while implementing the following: Authentication of mashups, Communication between mashup and Pega case processing, Separate built- On app for the self-service portal to use theme-clarity UI system. Accomplishments that we're proud of The Pega Mashup integration with a self-service portal and made it feel like a native application. :) What we learned We learned many new capabilities of Pega, especially on mashups, Integrations, and Case processing. Future Enhancements for Safe Return Autovalidate vaccination certificate using OCR Validate the uploaded Vaccination certificate PDF using OCR without user intervention IOT Temperature monitor on workplace visit Capture the Temperature of the employees when they visit the premise and track those in the case. Scheduled Sanitization We can have a case type to manage the building and floor sanitization and trigger it based on some schedule and notify the concerned team Inventory management for PPE We can create a case to manage PPE kits like masks, sanitizers available at the office inventory Incident Tracking Incident Tracking Create a new case when any of the employees who visited the office are affected with corona symptoms in the last 15 days so it can be tracked. Capture Social distance violations using CCTV We can have some OpenCV image processing technology to initiate a case that breaches social distance violations inside the office Employee readiness survey We can have a new case type and send it out to all employees to capture interest for employees to return back. Scanning for Office Passes We can generate a unique QR code for each Return to the office to verify it at the office gates. <div