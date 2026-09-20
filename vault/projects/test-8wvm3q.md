---
slug: "test-8wvm3q"
url: "https://devpost.com/software/test-8wvm3q"
title: "1View"
hackathon: "monday Apps Challenge: Dream it, build it"
organization: "Monday.com"
winner: true
words: 1011
team_size: 1
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "domain/developer_tools"
  - "user/developer"
  - "substrate/code_repository"
  - "substrate/web_dom"
---

# 1View

> Make your Dream View in monday to manage, update and track everything at one single place.

[Devpost](https://devpost.com/software/test-8wvm3q) · hackathon [[monday Apps Challenge- Dream it- build it]]

## Facets

**domain** [[developer_tools]]
**user** [[developer]]
**substrate** [[code_repository]] [[web_dom]]

**stack** ant-design, chart.js, html5, javascript, moment.js, monday-apis, monday-sdk-js, quill-js, react, sass, underscorejs

## How they structured the write-up

- inspiration
- what it does
- how i built it
- challenges i ran into
- accomplishments that i'm proud of
- what's next

## Body

Make your Dream View in monday.com Over 170+ filtering conditions with AND, OR chaining to create complex filters Create dynamic and customizable auto sorting views for each user requirement Pick and group items from multiple boards to a single collection Jot personal notes on items that are only visible for you Add status updates to multiple board items without switching pages Set high level timelines to track sprints and milestones Group and visualize filter data based on Status, People and Groups Inspiration The idea for 1View came from the existing user feedback and issues they have on the monday community and #mydreamapp inspiration board. Some of the most common issues users are having is to See & update all tasks from one place Create advanced filters to see what they only need Able to auto sort pulses Build dynamic and custom Kanban boards Add sprint timelines and personal notes 1View was implemented to solve all these issues and more by keeping simplicity as its core. Users can create tailor-made data rich views for their own requirements. 1View will help them to do more in less time by building their dream view. What it does As the name suggests, 1View is a monday app that allows users to see and update everything at one single place. 1View is available as a monday dashboard widget and a board view. Every monday user and business can get the benefit of 1View regardless of the field they are working on. Anyone can easily add 1View to their dashboards and board views within just few seconds. Furthermore 1View is 100% secure since it stores all the information inside monday and does not transfer data in and out from monday. With 1View you can, See and update all tasks from one place When your projects get bigger and bigger we know that you need a single place to see and update multiple tasks from different boards without switching pages. 1View will help you to achieve this. Create custom views Did you ever want to create personal views that are tailor-made just for you. 1View can help you. Track sprints with timelines Keep everybody on track by setting time duration for filters and showing them in a high level timeline. Following are the key features of 1View. ✅ Advanced Filters: Over 170+ filter conditions to chain with unlimited AND or OR. ✅ Create Collections: Collect different items from different boards into a single list. ✅ Auto Sort: Filters will sort automatically when their related board data changes. ✅ Quick Status Updates: Update multiple items from multiple boards within one page. ✅ Personal Notes: Jot personal notes to items and they are only visible for you. ✅ Sprint Timelines: Set high level timelines for sprints to track them easily. ✅ Graph Views: Group & visualize filter data with Status, People and Groups. ✅ Customization: Personalize filters and collections for your look and feel. ✅ Import/Export Views: Create duplicates of 1View widgets by importing/exporting. ✅ User Access Management: Control who can make changes to filters and collections within a widget. Others will only have read access. Apart from these key features, there are many more tweaks and settings are available in 1View to provide a good user experience. How I built it 1View was built using React. The Ant Design library was used to create all the custom UI components in 1View and all the styles were overridden to match with monday design guidelines. With the support of inbuilt monday JS SDK, GraphQL APIs, storage services and events I was able to process and store all the data relevant for 1View. All the cell renders, filters and sortings were written from scratch using the occasional support of Underscore JS. At the initial stage of the implementation, I developed 1View as a local React app to increase productivity and to reduce build times. In this process, monday API playground gave me a great support to generate hard coded data for local app development. Once I finished the critical part, I deployed the app using ngrok to monday and was able to integrate actual APIs and services. This way of development saved me a lot of time when debugging and coding the application. Being the sole developer, it took me around 5 weeks to complete and finish the entire application. Challenges I ran into Lack of documentation for some monday JS SDK events was a challenge at the initial stage. Then I used to look at the SDK source code and identify certain parameters and behaviors which was not in the documentation at that time. Initial request to extend the trial period was not succeeded through forms. I resolved this by attending the 2 day online workshop and directly asking a monday developer. He gave me a great support on extending the trial period. Building monday like data cells, filters and sorting was a great challenge and had to do extensive testing to see if they are working as expected in all states. Lack of support for more events in boards is still a issue and only a handful events are currently supported by monday. When it comes to column types like formula and progress, still monday does not provide required cell data through APIs. Accomplishments that I'm proud of At the start of the implementation I had a picture in my mind about how the final app should look like. I was able to add more features than the original idea and really proud about the final output and the app functionality. Also, I created a separate website to market the application and proud about the things I was able to achieve within this short period of time being a solo developer. What's next There is a roadmap ahead for 1View and hope to add continuous updates and features in future. Features like dark mode support, group summaries were not able to add due to the limited time and I'm hoping to add these in the future. Also, I'm open for user feedback and 1View will improve continuously with time. <div