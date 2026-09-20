---
slug: "bottlenecks"
url: "https://devpost.com/software/bottlenecks"
title: "Bottlenecks"
hackathon: "monday.com Apps Marketplace Challenge: solutions for teams "
organization: "Monday.com"
winner: true
words: 652
team_size: 1
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/on_device_local"
  - "mechanism/realtime_stream"
  - "domain/developer_tools"
  - "user/developer"
  - "substrate/web_dom"
---

# Bottlenecks

> Easily identify bottlenecks in your projects with monday

[Devpost](https://devpost.com/software/bottlenecks) · hackathon [[monday.com Apps Marketplace Challenge- solutions for teams]]

## Facets

**mechanism** [[on_device_local]] [[realtime_stream]]
**domain** [[developer_tools]]
**user** [[developer]]
**substrate** [[web_dom]]

**stack** ant-design, express.js, monday-apis, monday-sdk-js, react, sass

## How they structured the write-up

- inspiration
- what it does
- how i built it
- challenges i ran into
- accomplishments that i'm proud of
- what's next

## Body

Identify bottlenecks in your projects with monday Track and identify blockers in your projects Custom thresholds to identify dragging items Identify best performers from average task completion times Bottlenecks features Inspiration While working with monday boards, there's no any easy way to see how long each item state took to complete. As a result, we cannot easily identify the bottlenecks of an item and track in which state it was stuck the most. This raised the idea to develop a solution which can be integrated into a monday board with 0 configurations and analyze the life span of an item. By analyzing the timeline of an item, we can also see who are the best performers of a team and this helps us to build a more productive work environment. What it does Bottlenecks is a monday.com app that can track your project performance by identifying blockers. It comes with a board view that can be integrated with any monday board which has a status column. All monday teams can get the benefit of Bottlenecks regardless of the field they are working on. Furthermore Bottlenecks is 100% secure since it stores all the information inside monday and does not transfer data in and out from monday. With Bottlenecks you can, Track & identify blockers in projects With Bottlenecks, you can easily see the lifespan of a task and how long each teammate is taking to complete a given stage. Data can be aggregated per each task state. Bottleneck Thresholds Define custom thresholds to suit your needs and identify which items are dragging over time and take necessary actions. Best Performers Bottlenecks calculates the average time each team member is taking to finish a task and based on these calculations a Performance Leader board is displayed. Following are the key features of Bottlenecks, ✅ Custom Thresholds: Set custom thresholds and identify bottlenecks visually. ✅ Data Aggregation: View how long it takes to finish a given state across the board. ✅ Best Performers: Rank teammates based on the average time of task completion. ✅ Sort by Duration: Sort all your tasks based on the time it takes to complete. ✅ Time vs %: Support for both time durations and percentages. ✅ Data Filters: Search and filter for specific tasks via inbuilt monday search & filters. ✅ "0" Configuration: Everything works out of the box with 0 configuration. ✅ Real Time: Data will update in real time to show actual tasks states. How I built it Bottlenecks was built using React. The Ant Design library was used to create most of the custom UI components and styles were overridden to match with monday design guidelines. With the support of inbuilt monday JS SDK and GraphQL APIs I was able to query data from front-end. Before integrating with monday APIs, all the UIs were created locally and tested statically to reduce development times. Being the sole developer, it took me around 2 weeks to complete and finish the entire application. Challenges I ran into The main challenge was to read history logs of a board and convert them to a format that anyone can easily understand visually. I was able to develop a timeline view from scratch to show bottlenecks of an item and my goal was to create a pixel perfect UI. Accomplishments that I'm proud of While starting the implementation, I had a picture in my mind about how the final app should look like and at the end I was able to make it a reality. I developed a separate website to market the application and proud about the things I was able to achieve within this short period of time being a solo developer. What's next Dark mode support was not able to add due to the limited time and I'm hoping to add this in the future. Also, I'm open for user feedback and Bottlenecks will improve further with time. <div