---
slug: "semiconductor-manufacturing-rpa-for-iiot-analysis-report"
url: "https://devpost.com/software/semiconductor-manufacturing-rpa-for-iiot-analysis-report"
title: "Semiconductor Manufacturing - RPA for IIoT Analysis report"
hackathon: "Automation Anywhere Bot Games"
organization: "Automation Anywhere"
winner: true
words: 323
team_size: 2
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/sensor_fusion"
  - "user/developer"
  - "substrate/structured_db"
  - "substrate/video_visual"
---

# Semiconductor Manufacturing - RPA for IIoT Analysis report

> RPA to generate report of control charts based on IIoT Data. The report helps to keep the equipments up and running to maintain high-quality standards of products.

[Devpost](https://devpost.com/software/semiconductor-manufacturing-rpa-for-iiot-analysis-report) · hackathon [[Automation Anywhere Bot Games]]

## Facets

**mechanism** [[sensor_fusion]]
**user** [[developer]]
**substrate** [[structured_db]] [[video_visual]]

**stack** oracle, python

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned

## Body

Inspiration Semiconductor manufacturing consists of sophisticated, state of the art, 1000s of equipment. A multitude of IIoT sensors provides information about the equipment performance, which are analyzed using control charts. Daily review of these charts is essential to maintain high-quality standards of products. There are 200+ charts to be captured every day, doing this manually needs 5000+ annual hours. Due to time constraints very few critical charts were captured. What it does FDC system (Fault Detection and Classification) gets data from IIoT sensors of equipment and plots Charts. FDC Database has the list of Chart IDs that have spiked or exceeded above-set limits RPA gets the list of Chart IDs that are out of control from FDC Database RPA logs in to FDC UI, enters Chart ID and Date range RPA takes snapshot of the chart that appears in the UI and saves the image to specified folder Saved Images are then appended to PowerPoint File for review of Engineering Team. This File helps the team provide quick corrective actions to avoid equipment downtime and any degradation in product quality How we built it We gathered the pain points of Equipment Engineers in creating the report of OOC (Out Of Control) charts Detailed Requirement Analysis was done. Hybrid solution of RPA and python was suggested. RPA to take the OOC charts’ screenshots and python to collate the image files into PowerPoint. Bot account access was obtained for FDC Database and Front End Bot used Database Commands to extract list of Chart IDs Bot used Object Cloning commands for front end operations of FDC Challenges we ran into Automation Anywhere product limitation in creating PowerPoint File from the Chart Image Files. To solve this python script was written. Accomplishments that we're proud of We are proud of improving our manufacturing quality by helping in analysis of equipment performance What we learned We learnt how to utilize RPA to solve our manufacturing operations problem <div