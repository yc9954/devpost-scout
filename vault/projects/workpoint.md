---
slug: "workpoint"
url: "https://devpost.com/software/workpoint"
title: "Workpoint"
hackathon: "Codegeist 2021"
organization: "Atlassian"
winner: true
words: 877
team_size: 2
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
---

# Workpoint

> The best way to manage and redistribute workload in Jira

[Devpost](https://devpost.com/software/workpoint) · hackathon [[Codegeist 2021]]

## Facets


**stack** forge, react

## How they structured the write-up

- inspiration
- what it does
- what problems does it solve
- how we built it
- challenges we ran into
- accomplishments that we’re proud of
- what we learned
- what's next for workpoint

## Body

Inspiration Jira is an extremely comprehensive yet intuitive platform for managing issues within large teams. However, it currently does not provide an easy way to manage workload and evenly distribute issues among teams through a visual interface - something that we believe is vital for their productivity. Workpoint’s mission is to ensure that every team member’s time and effort is utilized optimally, and in the process helps the user identify and reassign issues belonging to overloaded members. Workpoint’s detailed analytics dashboard also helps you find bottlenecks and gauge your team’s performance. What it does Workpoint is the perfect Jira app for workload management that allows teams to gauge team performance through a drag-and-drop graphical interface, allowing teams to better manage their team’s issues, as well as have our algorithm automatically distribute issues evenly among team members. Managing Workload Our visual interface makes managing your team’s workload much easier. There is one card assigned per team member containing their number of complete and incomplete tasks, along with a pie chart showing their completion progress in the form of a percentage. Each card shows all of the issues assigned to that particular member, sorted by the issue statuses in the form of dropdowns. Lastly, for issues that don’t yet have an assignee, there is an “unassigned” card containing unassigned issue data. Workload Graph This informative line graph aptly visualizes the balance of workload within your team, providing insights into which team members have more tasks in total or left to complete. Workpoint has functionality for applying thresholds on these line graphs as well to further gauge the progress of each team member and see which team members are more overloaded relative to their colleagues. Drag and drop Workpoint has drag and drop functionality for easily reassigning tasks to various team members. Our graphs and dashboard updates these tasks dynamically to show the newly balanced workload information. Advanced filters Use our comprehensive set of filters to obtain the issues that you need. These include: Project Issue type Issue priority Assignee Created date Updated date Auto balance feature Workpoint’s auto balance engine allows teams to automatically balance issues within a set of unbalanced team members. This can be applied on all issues and team members, or also only a subset of issues and members through use of the filters. Once applied, workpoint provides a preview of the newly reassigned issues for each member based on our algorithm, and users can further customize how the issues are balanced through a manual drag and drop interface, before confirmation. What problems does it solve (1) Workpoint makes your team more productive by helping you balance tasks optimally through an easy-to-use drag and drop interface. (2) It helps you get an overview of team performance, and helps identify bottlenecks and weak links, which could impact project deadlines. (3) Detailed filters, line graphs, and thresholds enable customization. Workpoint is designed to suit a wide array of use cases and teams - it is truly yours! How we built it Workpoint is built on the Atlassian Forge platform for Jira. It uses a combination of custom Reactjs components, Atlaskit components, and react-dnd for the drag-and-drop functionality. Forge bridge facilitated our integration with the Jira API. Challenges we ran into (1) Figuring out how to use third-party React libraries with Forge, in order to integrate Atlaskit components. (2) Integrating with the storage API through invoke, to store the app configurations and settings. (3) Getting all the dropdown components to work seamlessly, with search boxes and icons. (4) Integrating drag and drop twice, with both reassigning issues from the cards, as well as for manually reassigning issues on the preview cards in the auto balance feature Accomplishments that we’re proud of I'm proud to have built a clean user interface that fits in very well with the Jira platform. The final product turned out even better than our original vision, the main difference being the addition of the auto-balance features. What I like most about Workpoint is that it strikes the perfect balance between comprehensive features and intuitive user experience. I'm super excited to launch Workpoint in the Atlassian marketplace! What we learned (1) Building Atlassian apps with the Forge platform (2) Using Atlaskit to build user interfaces (3) Using the Jira REST API with Forge (4) Implementing drag and drop functionality in Reactjs (5) Integrating an auto-issue distribution algorithm with our forge app What's next for Workpoint After the completion of Codegeist, I plan to launch Workpoint as an app in the Atlassian marketplace. I also have plans for feature expansion, in the form of customisable themes and layouts, more complex filter combinations and logic, and much more! Furthermore, I aim to further build upon our automatic issue distribution technology by taking into account more complex factors such as a member’s daily productivity (measured in number of tasks being completed a day) and relative skill level when redistributing tasks to maximize team efficiency. One of the judging criterias for Codegeist is ‘Potential Impact - Includes the extent to which the solution can address a need among Atlassian users.’ I believe that this is where Workpoint stands out. It is made by and for Jira users, and provides solutions to problems that teams face at the grassroot level. <div