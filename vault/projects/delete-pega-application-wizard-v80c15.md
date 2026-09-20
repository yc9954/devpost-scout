---
slug: "delete-pega-application-wizard-v80c15"
url: "https://devpost.com/software/delete-pega-application-wizard-v80c15"
title: "Delete Pega Application Wizard"
hackathon: "Pega Community Hackathon 2022"
organization: "Pegasystems"
winner: true
words: 495
team_size: 6
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
---

# Delete Pega Application Wizard

> Delete Pega Application Wizard is used to automate any Pega application deletion.

[Devpost](https://devpost.com/software/delete-pega-application-wizard-v80c15) · hackathon [[Pega Community Hackathon 2022]]

## Facets

  <sub>weak: financial_record</sub>

**stack** appstudio, casemanagement, cosmos, pega, workflowautomation

## How they structured the write-up

- inspiration
- problem statement
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for delete pega application wizard

## Body

Inspiration Many a times, we have used OOTB Pega Wizards for importing products, renaming or refactoring classes, deleting rulesets etc. These wizards have helped us save a significant amount of time, thus improving productivity. We wanted to add one more feature to this wizard which would simplify the process of decommissioning Pega application. Problem Statement Today while designing any POC application in one of the existing servers, we do not have any automated process for cleaning up the Pega environment once the POC has been completed. Similarly, if we have any Pega application that needs to be deployed to production before a dedicated server is ready, we might have been using another available server to deploy the production ready application so that the end-users can start using the application without delay. Later, when the actual production server is available, we would be taking the backup of the application from previous environment and re-deploy to the new server. After this, we would be spending a lot of manual effort in analysis; cleanup process would be completely manual which might not be 100% accurate. What it does To address the above problems, we built a Wizard using Pega Workflow Automation which automates the entire application deletion process seamlessly reducing a lot of manual effort, saving time and improving the accuracy. How we built it The solution is built using Pega 8.7 version, Theme Cosmos: 04-01 utilizing the Pega Case Management, Workflow Automation and User Interface. The application is created using Pega App Studio. The following processes are performed automatically in the specified sequence: Drop DB Tables specific to the application Delete OOTB Table Records specific to the application being deleted from common tables like Assign-Worklist, Assign-Workbasket etc. Delete Rulesets present in the application stack Delete Non-Version Rules like Work Queue, DSS, Access Group, Class, etc. Finally the application rule is also deleted Challenges we ran into We had to spend a lot of time to analyze the identification of common tables like worklist, workbasket, attachments, events etc. where we just have to delete our application specific records alone while retaining the records pertaining to other applications in the shared environment. There were a lot of non-versioned rules. Streamlining a process to collate and delete all the non-versioned rules needed an extensive analysis and brainstorming. Accomplishments that we're proud of Providing an innovative add-on feature to the existing Pega Wizards that provides a quick and automated solution Ready to use Plug & Play Accelerator Providing a solution that can be leveraged at any SDLC stage and in any environment from Dev to PROD What we learned Build User Friendly Accelerators and Wizards using Pega Automation Effectiveness and importance in the current IT industry Team work and Time Management What's next for Delete Pega Application Wizard Currently, the product mandates the manual backup of the application being deleted. This process can be automated. Self Service user manual with step by step instruction on how to run the wizard <div