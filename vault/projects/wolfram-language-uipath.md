---
slug: "wolfram-language-uipath"
url: "https://devpost.com/software/wolfram-language-uipath"
title: "Wolfram Language + UiPath"
hackathon: "Power Up Automation"
organization: "UiPath"
winner: true
words: 696
team_size: 1
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "domain/developer_tools"
  - "domain/education"
  - "user/developer"
  - "substrate/geospatial"
  - "substrate/video_visual"
---

# Wolfram Language + UiPath

> Call the Wolfram Language from UIPath

[Devpost](https://devpost.com/software/wolfram-language-uipath) · hackathon [[Power Up Automation]]

## Facets

**domain** [[developer_tools]] [[education]]
**user** [[developer]]
**substrate** [[geospatial]] [[video_visual]]

**stack** uipath, wolfram-technologies

## How they structured the write-up

- inspiration
- what it does
- how i built it
- challenges i ran into
- accomplishments that i'm proud of
- what i learned
- what's next for wolfram language custom integration

## Body

Decay Graph Wokflow Wolfram Alpha Activities Inspiration The Wolfram Language has always been an amazing technology to me. From solving my high school calculus problems, to answering a simple question I have about the world with all of the answers I'd ever need and more visualizations than I have use for, the Wolfram Language system has been an amazing tool to use throughout my life. I have recently begun my RPA Development journey, and coincidentally the Wolfram company released a free license for the Wolfram Language kernel for developers. I wanted to bring all of the power of this tool to the UiPath ecosystem and enable users to perform advanced mathematical analysis, create rich visualizations, and open up the possibilities for deep integration between a symbolic language with immense capabilities and a sophisticated automation framework. What it does This custom activity pack allows a user to launch or connect to a Wolfram Language kernel and interact as if they were working directly in the shell. The user can evaluate Wolfram Language expressions as strings or the Expression class provided with the WL .NET Interface. The results of this expression map back to .NET Types for use in the workflow. Expressions can also be evaluated to images, sound, or even custom .NET Objects. There are also low level commands that allow interaction with the Wolfram Language on a packet level. The Wolfram Language / .NET interface utilizes Wolfram Symbolic Transfer Protocol to facilitate communication between the symbolic runtime of the WL kernel and the object-oriented .NET runtime. Direct manipulation of this protocol allows for complete and direct control of the Wolfram Language kernel. The user may open a Wolfram Language kernel as a parent scope with evaluations inside, and the activity pack will take care of the setup and tear-down of the WL runtime process, or the user may open a Kernel and store it as a variable in their workflow for use later, closing it manually when required. How I built it I utilized the Custom Activity template as a base, and modified the Application class to provide each of the methods required for starting a Kernel, sending expressions for evaluation, and working directly with the WSTP connection. Once I had a base of a functioning application, I started working on creating Windows Workflow Foundation activities to interface with the Application class. Challenges I ran into Debugging the inner-workings of my Application class which uses the .NET/Link library when it was executing from an activity was difficult. It would be nice if the UiPath debugger provided more insight into the Activity's state when an exception occurs. It also required additional effort to customize the activity's designer, but I was able to get that working and add custom icons to my activities. Additionally, documentation for the .NET/Link library is fairly sparce, which lead to some trial-and-error development in order to find what is required to get it communicating with the Wolfram Language kernel properly. Accomplishments that I'm proud of I was able to build a complete integration suite between a powerful computation system and a sophisticated automation framework. These activities can be utilized at my company in the future to provide powerful solutions as part of our UiPath RPA propjects. What I learned I learned a tremendous amount about development of custom activities for the Windows Workflow Foundation, which will be helpful in the future as my company begins creating them for RPA implementation projects. I learned more about UiPath development and debugging in a hands-on environment. I also learned much about the Wolfram Language system, its capabilities, and how to create amazing programs with it. What's next for Wolfram Language Custom Integration There are many processes you can utilize the Wolfram Language, but some basic workflows that many users would want are tedious to create in UiPath studio. I want to build a package of snippets / workflows to simplify standard processes such as changing the Wolfram Language's current directory, or exporting an evaluated object to the Wolfram Cloud. I would also like to connect the WL Kernel to a front-end so that the visualizations may be interacted with and used with standard UiPath activities. <div