---
slug: "compass-whiteboard"
url: "https://devpost.com/software/compass-whiteboard"
title: "Compass Whiteboard"
hackathon: "Codegeist 2024"
organization: "Atlassian"
winner: true
words: 632
team_size: 4
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/cross_origin_web"
  - "mechanism/realtime_stream"
  - "domain/developer_tools"
  - "user/developer"
---

# Compass Whiteboard

> Visualise component dependencies and create amazing C4 models of your architecture within Compass!

[Devpost](https://devpost.com/software/compass-whiteboard) · hackathon [[Codegeist 2024]]

## Facets

**mechanism** [[cross_origin_web]] [[realtime_stream]]
**domain** [[developer_tools]]
**user** [[developer]]

**stack** atlaskit, react, react-flow, redux, typescript

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what's next for compass whiteboard

## Body

Inspiration Compass is a developer portal that provides a unified real-time representation of components in one place. This is an amazing tool we use internally to keep track of our component health; however, it has some disadvantages we’re trying to solve. Compass provides an efficient way to manage components, but we can’t view component hierarchy or all dependencies between them. The default dependencies page shows relationships only for the component but does not show transitive dependencies. Moreover, only one type of relationship is allowed. Our app is inspired by the C4 Model : is a way of visualizing software architecture. The C4 model is about presenting the runtime units (such as containers) and how functionality is partitioned across them and our team uses it to visualize our architecture. What it does Compass Whiteboard has a main page for visualizing all component dependencies. This is a whiteboard where users can simply drop components from the left panel. You can create relationships between components, view component scorecards, display only certain types of components, or even launch an analysis to view potential issues. When you first open Compass Whiteboard, it automatically builds a diagram for you. You are able to see transitive dependencies and even possible problems in your architecture. If you get stuck in finding a component on the canvas board, type in the search pane. Changes are applied to the components only after the user saves the flow. If you mistakenly alter the flow, you can roll back using the reset button. On the left sidebar, you can see three tabs: Components : this tab contains components that don't have dependencies or haven’t been added to the flow yet. You drag the component and drop it into the flow. View : this section helps you filter certain components in the flow. For example, if you want to see the relations between application services only, you can select the Services checkbox. Analysis : this section allows you to analyze your flow and identify problems. You can find orphan nodes, spanning trees and even reflow your component board. How we built it This was my first experience using Atlassian Forge, and I found Forge Tunnel incredibly effective in speeding up the development process. Our app leverages Forge Storage to store component positions within the flow and relation metadata. I aimed to design a flow that closely resembles the Compass component dependencies page. We chose the React Flow library to visualize dependencies, which has proven to be a cutting-edge tool for this purpose. Challenges we ran into React Flow supports vite but it depends on React > 18.0 , but some atlaskit components (like color-picker) were built on top of React 16 . This is not a critical issue, we can install our dependencies using the --force option, but it should be definitely fixed. We encountered ambiguity when defining the direction of relationships. After some research, we decided to add a separate setting in the plugin configuration, allowing the user to select either a straight or reverse relationship direction. By default, if the left component depends on the right component, the plugin draws the relationship from left to right. Accomplishments that we're proud of Atlassian Design - a great documentation, easy-to-use components; React Flow - the best library for building node-based editors; dagrejs - helper library for customizing components layout; What's next for Compass Whiteboard We’re going to add some new features: Highlighting flow problems - UI for displaying components that have a “bad” health score and have a certain amount of outbound dependencies; Subflows - some components belong to different teams/units and it would be great if we could treat them as a unified resource; Publishing to the Atlassian Marketplace; Fill free to reach me through vasylchyzhcorp[at]gmail.com to gain the repo access installation link <div