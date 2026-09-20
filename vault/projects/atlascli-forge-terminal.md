---
slug: "atlascli-forge-terminal"
url: "https://devpost.com/software/atlascli-forge-terminal"
title: "AtlasCLI Forge Terminal"
hackathon: "Codegeist 2022"
organization: "Atlassian"
winner: true
words: 695
team_size: 1
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/simulation_digital_twin"
---

# AtlasCLI Forge Terminal

> With AtlasCLI, the power of the Jira API is at your command.

[Devpost](https://devpost.com/software/atlascli-forge-terminal) · hackathon [[Codegeist 2022]]

## Facets

**mechanism** [[simulation_digital_twin]]
  <sub>weak: structured_db</sub>

**stack** forge, javascrript, jira, typescript, webpack

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for atlascli forge terminal

## Body

You can display the result in JSON, YAML or CSV in addition to tabular format Most of the Jira entities are covered Each command has detailed help You can display the result in tabular format Inspiration Sometimes we want a faster way to use Jira, find out data like the ID of issues, accounts, etc. or move information out of Jira to other applications. A CLI tool makes all of them accessible to power users. What it does AtlasCLI Terminal allows you to access Jira from a terminal inside the Jira UI. There are more than 350 commands, and we will continue to add new commands in the future. Using this tool, perform create/update/delete/list/get operations for Jira entities, like an issue, user, group, dashboard, etc. How we built it We were working on a command line tool for a while, but it was a command line tool that could only be used from a real terminal like "Power Shell", "Terminal", "iTerm", etc. Within this project's scope, we have created a new application that works within Jira UI . We used xterm.js within a custom UI app and created a Forge function to run our commands. We used the Forge storage to store the command history for each user. Most of the commands were already exist before the Codegeist, but we have added quite a bit during the Codegeist too. But this project is not the commands we have developed. They are easy to develop compared to the technical difficulties of getting them working in Forge runtime and browser. Because all the libraries we used depend on the packages which exist in a Node JS runtime but do not exist in the Forge runtime, like streams, process, TTY, crypto, fs, path, etc. Challenges we ran into A command line tool inherently depends on the operating system process, TTY, input/oules, and file system, all of which are not available in Forge runtime. To get it working in Forge runtime, we needed to patch or rewrite more than 10 3rd party dependencies for a few weeks. We needed to handle strange errors like "forge Error: Isolate is already disposed", and lots of snapshot errors in 3rd party dependencies. We simulated process environment, input, and output and were able to redirect these to a terminal that works in custom UI. It was a long journey from the time we started porting 3rd party dependencies to Forge runtime to a simple "Hello World" command output displaying on the UI. For weeks we needed to fix various build errors and dependency issues and patch/re-implement functionalities that don't exist in the Forge runtime. Accomplishments that we're proud of We have a functional application, which is very useful for us and lots of other users who like to use command line tools. We were about the give up due to the very strange errors we faced despite the fact that we had been developing for Forge platform for nearly 2 years. It was really fun to see a table printed in the embedded terminal. What we learned Since we have already developed many Forge and Jira apps in general, we couldn't learn much about the Forge platform or Jira application development. But, we learned a lot about Typescript and Webpack configuration. We have more than ten apps in the marketplace, and this project has the most advanced project structure. We have two different repositories, and we are using Webpack output from one project as a dependency in another. Both of the projects are npm/yarn workspaces that are split into multiple sub-projects. What's next for AtlasCLI Forge Terminal Some commands that require user interactions or display progress for long-running operations do not work. Also, some commands require complex input, like issue creation. Currently, they also don't work well. We will handle these later. We will also continue to add more commands to cover more usage scenarios. We will implement some utilities that will allow us to redirect the output of one command to another for more advanced usage. Additionally, we will implement a simple file system on top of forge storage so that users can write and save wrong scripts using the tool. <div