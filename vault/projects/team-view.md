---
slug: "team-view"
url: "https://devpost.com/software/team-view"
title: "Team View"
hackathon: "monday apps challenge"
organization: "Monday.com"
winner: true
words: 831
team_size: 1
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/on_device_local"
  - "domain/developer_tools"
  - "user/developer"
  - "substrate/geospatial"
  - "substrate/web_dom"
---

# Team View

> Best way to manage workload and resources in monday

[Devpost](https://devpost.com/software/team-view) · hackathon [[monday apps challenge]]

## Facets

**mechanism** [[on_device_local]]
**domain** [[developer_tools]]
**user** [[developer]]
**substrate** [[geospatial]] [[web_dom]]

**stack** ant-design, html5, javascript, moment.js, monday-apis, monday-sdk-js, monday-ui-react-core, quill-js, react, sass, underscorejs

## How they structured the write-up

- inspiration
- what it does
- how i built it
- challenges i ran into
- accomplishments that i'm proud of
- what's next for team view

## Body

Workload thresholds with tasks and time estimates Maximize resource utilization Advanced filters No board limits and sub-items support Advanced item view Inspiration Workload and resource management is a key aspect of any project. There should be an easy way to track and manage workloads among different team members and see who's overloaded and who can take on more tasks. At the moment monday.com lacks this kind of detailed analysis about workload and resources. That's where Team View can help you to see a summary of your team and delegate tasks among team members in the best possible way to maximize resource utilization. Team View will also help you to understand how your team is performing and identify any bottlenecks that impact your deadlines. What it does Team View is the perfect monday app for resource and workload management, making it easy to see what people are working on now as well as in the future. It comes with a dashboard widget and a board view where you can connect any number of boards which has at least one People column and one Status column. All monday teams can get the benefit of Team View regardless of the field they are working on. Furthermore Team View is 100% secure since it stores all the information inside monday and does not transfer data in and out from monday. With Team View you can, Track & manage workloads: You can see a summary of all team members with their done percentages and tasks assigned to them. This helps to keep track of the project progress and identify how tasks are delegated between people. Workload thresholds: You can define workload thresholds as tasks or time estimates. This allows you to see each team member's current workload and identify who is overloaded and who is free. Do more... Less hassle! Unlike other monday apps, Team View has no limits on the number of boards that can be connected. It also supports sub items and you can create awesome dashboards with no time. Team View is built from the ground up to support heavy data loads and it offers an advanced item view to do more in less time. Following are the key features of Team View, ✅ No Board Limits: Configure unlimited number of boards without any limits. ✅ Sub-items Support: View and manage workloads of sub items. ✅ Workload Map: Visualize current workload of your team members. ✅ Done Percentages: Identify done and not done tasks with their percentages. ✅ Tasks vs Time: Track your team by both tasks and time estimates. ✅ Workload Thresholds: Identify overloaded people in your team with thresholds. ✅ Status Breakdown: Summary of each team member's current task statuses. ✅ Due Dates: Filter and visualize tasks by their due dates. ✅ People Cards: Analyze each team member's tasks summary. ✅ Drag & Drop: Easily switch task assignees by drag and drop. ✅ Advanced Filters: Filter items with multiple AND & OR conditions. ✅ Custom Sorting: Multiple sorting options to identify overloaded people. ✅ Advanced Item View: Improved item view to update details and post updates. ✅ Status Timeline: Visualize timeline of a task's status and identify bottlenecks. How I built it Team View was built using React. Both monday React UI components and the Ant design library were used to create the user interface and some styles were overridden to match with monday design guidelines. With the support of inbuilt monday JS SDK and GraphQL APIs I was able to query data from front-end. Before integrating with monday APIs, all the UIs were created locally and tested statically to reduce development times. Being the sole developer, it took me around 6 weeks to complete and finish the entire application. Challenges I ran into The main challenge for most of the current monday apps is the board limitations of dashboards. To mitigate this issue, I had to build a custom board configuration dialog and allow users to connect any number of boards including sub items. Team View aggregates data by people and task statuses. Creating a fluid UI with drag and drop support for tasks with custom grouping was a challenge since lots of data manipulations were required. The workload chart was also created from scratch and adding thresholds was a challenge since it requires many calculations across multiple boards. Accomplishments that I'm proud of While starting the implementation, I had a picture in my mind about how the final app should look like and at the end, I was able making it a reality with some extra features. I developed a separate website to market the application and proud about the things I was able to achieve within this short period of time being a solo developer. What's next for Team View Dark mode support was not able to add due to the limited time frame and I'm hoping to add this in the future. Also, I'm open for user feedback and Team View will improve further with time. <div