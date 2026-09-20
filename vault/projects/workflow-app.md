---
slug: "workflow-app"
url: "https://devpost.com/software/workflow-app"
title: "Workflow App"
hackathon: "monday apps challenge"
organization: "Monday.com"
winner: true
words: 804
team_size: 1
has_repo: false
has_live: false
has_video: true
tags:
  - "project"
  - "domain/civic_government"
  - "domain/developer_tools"
  - "user/educator_student"
  - "substrate/code_repository"
---

# Workflow App

> Workflow app allows creating visual step-by-step workflow process with required columns and custom permissions in each step

[Devpost](https://devpost.com/software/workflow-app) · hackathon [[monday apps challenge]]

## Facets

**domain** [[civic_government]] [[developer_tools]]
**user** [[educator_student]]
**substrate** [[code_repository]]

**stack** html5, javascript, material-ui, moment.js, monday-apis, monday-sdk-js, monday-style, mongodb, node.js, react

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for workflow app

## Body

Workflow item view display Required columns and permissions configuration settings Inspiration Inspiration for Workflow App came from insights gained implementing software solutions in leading pharmaceutical companies such as Novartis, Pfizer where the ability to create a structured and controlled workflow that requires management approval and fulfillment of mandatory fields is crucial. Some of the commonly required features are: Structured based workflow , a structured process with a specific pre-set order or execution. Required columns per step , in order to move forward in the process every user is required to fill mandatory fields in different steps. Permission settings , single user can not perform the record from start to end (i.e can not approve his own request) See here a short video What it does As the name suggests, Workflow App allows users to easily create visual step-by-step process with required columns and customs permissions for each step. Following are the key features of Workflow App: Structured process , enforcing a linear step-by-step workflow that simplifies the user journey. Users only need to click “next” and the workflow app will take them through the journey. i.e. lead → qualification → closure (no way to skip qualification) Required columns per step , allows setting required columns in each step (and not only for the creation of an item via a monday.com form) and focuses the users on required data in order to move forward with your process. i.e. you cannot finish the qualification stage without filling the timeline column Permission settings , it allows to set permission on a status column per step and by that allowing only permitted personnel to perform a specific step. i.e. only the manager can change the status from Pending Approval to Approved. Workflow App can be used for a variety of use cases such as: R&D, Product Development, Sales Processes, Marketing, Creative, HR, Vacation Approvals, Design, and almost any process you can think of. A tutorial of Recruiting Management process designed with the Workflow App, can be found here How we built it Workflow App was built using React as the frontend technology and Node.js as the backend technology. We used the monday.com and Material-UI libraries to create most of the components and styles that were adjusted to match with monday.com design guidelines. We used a backend to save all the workflow configuration data - steps, required columns, and custom permissions. All the authentication and authorization of the requests between monday.com to the backend were handled using middleware between the app client id and the current user's token. We integrated with monday.com APIs and SDK to query, retrieve and mutate the data. Challenges we ran into At the initial stage, it was tough to understand and cover all the monday.com SDK and APIs and develop it dynamically using React and Node.js. I used to handle this challenge by reading the source code in GitHub, the documentation, and the sources via the monday.com community. In addition, as our application contains a backend service, we worked hard to highly secure the communication using HTTPS certificates, authorized and private requests, and encrypted storage. During the development, we got the best support and attention from monday.com support, either private messages or via the monday.com community. Accomplishments that we're proud of Role-based permission : monday.com has built-in personal permission for columns. In complex processes , there is a need to provide permission by role rather than by person (for e.g., only the VP of Sales can approve a discount). In Workflow App we succeeded in implementing role-based permission for the status column, based on the people column. For example, only a person who is selected as VP of Sales in the people column can approve a discount. This adds a new level of functionality within the limits of the existing permissions settings of monday.com Required Columns : today the only option to set required columns for the users is via forms and only on initial entry . Finding a creative way to add required columns functionality in different steps of the flow is something we are proud of What we learned Workflow App introduces technical functionality that was not available in the existing monday.com status column permission settings. We delved deeply into monday.com product, business and use-cases learning the entire SDK and API documentation in order to create the functionality required by our App. This was successful due to the existing monday.com technical framework. What's next for Workflow App Currently, the Workflow supports a single path. In the next version, we will add 2 main functionalities Complex decision tree - allowing advancement through multiple paths to completion. Parallel approval for steps - functionality that will allow multiple role-based approval to advance a single step (e.g. the need for VP Sales, VP Operations, and VP Finance to approve an investment in a new CRM) <div