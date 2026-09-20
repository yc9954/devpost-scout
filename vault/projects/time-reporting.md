---
slug: "time-reporting"
url: "https://devpost.com/software/time-reporting"
title: "Time Reporting"
hackathon: "monday apps challenge"
organization: "Monday.com"
winner: true
words: 519
team_size: 3
has_repo: false
has_live: false
has_video: true
tags:
  - "project"
  - "domain/agriculture_food"
  - "domain/developer_tools"
  - "substrate/structured_db"
---

# Time Reporting

> Integrated and secure solution for managing time reports.Includes Board View and Workspace set up to track time per person for up to 3 levels of reference (e.g. Client -> Project -> Activity)

[Devpost](https://devpost.com/software/time-reporting) · hackathon [[monday apps challenge]]

## Facets

**domain** [[agriculture_food]] [[developer_tools]]
**substrate** [[structured_db]]

**stack** amazon-web-services, apollo, react, typescript

## How they structured the write-up

- inspiration
- what it does
- how to install
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for time reporting

## Body

Inspiration Knowledge based works and consultants usually have a timesheet approach to time reporting which wasn't really possible without integrating monday.com to external services such as Harvest and toggl. We wanted to make it easier to manage Timesheets in monday.com and provide the same value for a fraction of the cost! What it does It has never been easier for you to report time against clients, projects and tasks in one place. All inside of monday.com without needing any 3rd party services or integrations. The time reporting solution provides a board view that makes it easy to select relevant objects and quickly enter time reports in a weekly or monthly timesheet. Managers or time admins can view everyone's submissions and approve entries by changing a status which in turn can initiate any custom automated workflow thanks to monday.com's strong native automations. How to install Time Reporting app consists of a board view and a workspace template . Workspace template contains 4 boards and it's recommended you install it first (from any workspace: Add -> Choose from templates -> See More Templates -> select "Time Reporting"): Time Reporting - this board contains a view where you can enter times, as well as sample views with visualisations Clients / Projects / Activities - 3 boards with example items you can log time against. Time Reporting board contains links to these boards. Clients board defines allowed projects per client (using link to Projects board). Projects board defines allowed activities per project (using link to Activities board). How we built it We used React on top of monday.com SDK and Apollo as a GraphQL library. App is being hosted using several AWS services. We wanted to focus on complementing the monday.com native functionality in order to utilise existing automations, integrations and dashboards to view and consume the data. Challenges we ran into Achieving monday.com look and feel for the board view took time and attention to details. We specifically focused on performance and ease of use - spreadsheet-like keyboard navigation, optimistic responses for API calls etc. This app manipulates items in batch, but there’s no batch edit/delete API calls in monday.com, so we had to manage state of multiple API calls at once. Accomplishments that we're proud of Another highly wished for functionality added to monday.com. We realise there are time reporting solutions out there which are integrated with monday.com, but nothing beats native board view and keeping data in one place for security and ease of use. What we learned Learned a lot about using GraphQL in complex apps like this view. Several new CSS tricks were useful when implementing monday.com style table which hides behind the header when scrolled. What's next for Time Reporting Use "edit rows assigned to them" board permission to prevent non-managers from editing data Determine managers based on board owners Time planning/ budgeting view to allocate time for a week or a month at a time. Optimisation for large tables with 1000+ time entries Smaller quality of life enhancements (e.g. set status for all rows in a week/month with a single click) Mobile support Bug fixes <div