---
slug: "semiconductor-manufacturing-status-review-report"
url: "https://devpost.com/software/semiconductor-manufacturing-status-review-report"
title: "Semiconductor Manufacturing Status Review Report"
hackathon: "Automation Anywhere Bot Games"
organization: "Automation Anywhere"
winner: true
words: 409
team_size: 1
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/retrieval_grounding"
  - "user/developer"
  - "substrate/video_visual"
---

# Semiconductor Manufacturing Status Review Report

> A better way to capture and collate key parameters of Semiconductor Manufacturing Performnace is here! Helps in review and build growth strategy for delivering the targeted throughput of chips/wafers.

[Devpost](https://devpost.com/software/semiconductor-manufacturing-status-review-report) · hackathon [[Automation Anywhere Bot Games]]

## Facets

**mechanism** [[retrieval_grounding]]
**user** [[developer]]
**substrate** [[video_visual]]
  <sub>weak: structured_db, web_dom</sub>

**stack** a360, database, dll, html, python, vbscript, xml

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for semiconductor manufacturing status review report

## Body

Our Story.......... Inspiration Our Semiconductor Manufacturing Units have Daily Operations Review to ensure our Tools and Processes are inclined in meeting throughput of chips/wafers. Prerequisite for this Review Meeting is to have Status Report prepared. This Report has data from various manufacturing systems with details like -a. Past 24 hours Production, -b. Rate of Production -c. Key indicators of Performance issues Engineers spend significant amount of time to create this Status report. Close to 5hours for 10 departments. This is not the right utilization of Operations Engineers as their time is required for smooth operations and quality improvement. It is necessary for the Daily Operations Status Report to be available on time with 100% accuracy else it impacts the throughput of wafers. The current throughput we have is 150,000 wafers per year What it does RPA connects to various manufacturing systems (between 10 to 20 systems) of each department Filter for required data (department name, Dates, Device Types) Take snapshots and collect few data points Add snapshots and data points into Email and Excel Report How we built it Collaborated with Manufacturing Operations Team to gather their pain points Suggested RPA solution for the report preparation Detailed Requirements were gathered Access to the systems for Bot account was obtained Built a prototype first for one of the departments and scheduled to run for few days. Operations Team was very happy with the outcome as it was on time and accurate every day. Made the prototype production ready Extended the solution for other departments Challenges we ran into A360 product limitation of embedding the snapshot images into Email Body. We used VB script to solve this A360 product limitation of adding snapshot images into Excel workbook. We used python script to solve this. A360 product limitation of performing some excel manupulations. We used the metabot DLLs from V11 to solve this. Accomplishments that we're proud of We are proud of relieving our Operations Engineers’ from mundane tasks and making our Manufacturing Operations run efficiently What we learned We learned how to make a solution flexible. We built for one department and extended the solution to other departments. What's next for Semiconductor Manufacturing Status Review Report We are trying to collaborate with other operation teams, where they use a PPT file for the presentation instead of Email / Excel. Having the framework of the bot in common we are waiting to explore new systems and excited to face new challenges. <div