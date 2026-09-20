---
slug: "vscode-datree"
url: "https://devpost.com/software/vscode-datree"
title: "VSCode Datree"
hackathon: "Cloud Native Hackathon"
organization: "WeMakeDevs"
winner: true
words: 650
team_size: 1
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "domain/developer_tools"
  - "domain/education"
  - "user/developer"
  - "substrate/geospatial"
---

# VSCode Datree

> An extension that can run Datree tests and show errors and suggestions directly in editor to assist developers writing error-free, up to the mark Kubernetes configurations to achieve optimum results

[Devpost](https://devpost.com/software/vscode-datree) · hackathon [[Cloud Native Hackathon]]

## Facets

**domain** [[developer_tools]] [[education]]
**user** [[developer]]
**substrate** [[geospatial]]

**stack** datree, node.js, react, typescript, vscode

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for vscode datree

## Body

GIF Helm Support GIF Demo Inspiration Datree is a CLI tool which allows rectification of K8s configuration files with ease and zero dependency. While researching the possible use case for the hackathon I came across an idea about a VSCode extension that can show errors directly in the editor and to my surprise there was no existing solution to this!! , I always wanted to make a VSCode extension and now it was the perfect opportunity. What it does A VSCode extension that can run Datree tests and show errors and suggestions directly in the editor to assist developers writing error-free and up to the mark Kubernetes configurations to achieve optimum results How we built it First, I started with parsing the CLI’s output with it’s JSON output format, faced some issues with the structure and contacted datree support for assistance, I came to know that there was already a issue which addressed this and Eyar Zilberman provided me with some ideas and a video that link that suggests such VSCode extension. I was very much pumped at this point and worked with full force to make it into a reality. VSCode has a very extensive API when it comes to developing extensions. I got the opportunity to learn and understand the logic that goes behind building such extensions. I worked with webviews, child processes, providers and typescript while building this extension and React.js for building the webviews. I periodically updated datree team with my progress and they were kind enough to solve my doubts and suggest improvements and features. Shimon Tolts suggested adding Helm support and Dima Brusilovsky suggested having an interface where the user can provide custom configuration for the tests, thanks to them I was able to complete the first stable release of the extension. While working on this project I interacted with many hackers, solved their doubts, got some of mine cleared, thanks to Community Classroom for making this happen. Challenges we ran into Parsing data from Datree was challenging at first as Datree is a command line based tool, parsing the output requires creating a child process which runs the commands, we then listen for events and collect the Buffer data through the std streams, Datree allows passing the output flag which makes it easy to interpret the data as JSON. The challenge that came up was to render the errors, at the moment Datree’s JSON output doesn’t have a defined structure that made me add sanity checks over the JSON objects. As of now Datree’s output lacks error context which makes it hard to show errors on specific line numbers, I built an algorithm that takes in Datree’s output and YAML file content and tries to map the errors with the use of regex and label values. With upcoming versions of Datree it would surely be easy to implement this. VSCode has a comprehensive guide for building extensions but was daunting at first and required some trial and error to arrive at functioning results. Accomplishments that we're proud of This open-source extension extends Datree’s functionality by allowing users to use custom policies made with Datree and use them directly through VSCode. What we learned While understanding the Datree policy system I learned various misconfigurations that people can unknowingly write in their K8s config files. I learned how to parse data from the command line and incorporate it in our own applications. Before adding Helm support to the extension I read about the working of Helm Charts, how it functions and makes writing K8s configuration easy. This allowed me to write detection functions that can detect the Helm workspace and act accordingly. I learned about VSCode developer API and how we can contribute to open-sources by creating extensions that make developer lives easier. What's next for VSCode Datree Work with Datree team and keep the extension up-to-date with the CLI for best developer experience. <div