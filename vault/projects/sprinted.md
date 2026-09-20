---
slug: "sprinted"
url: "https://devpost.com/software/sprinted"
title: "SprintEd"
hackathon: "Codegeist 2022"
organization: "Atlassian"
winner: true
words: 1172
team_size: 1
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "domain/civic_government"
  - "user/educator_student"
  - "substrate/document_pdf"
---

# SprintEd

> Automatically assign sprint names from fun themes like animals or places - show your sprints some love today! Includes functionality to view, organise and update sprint information in one place!

[Devpost](https://devpost.com/software/sprinted) · hackathon [[Codegeist 2022]]

## Facets

**domain** [[civic_government]]
**user** [[educator_student]]
**substrate** [[document_pdf]]

**stack** forge, react, sass

## How they structured the write-up

- inspiration
- what it does
- how did you build it?
- challenges encountered
- accomplishments that you're proud of
- what you learned

## Body

GIF Demonstration of the Auto-rename feature Using the main interface to see an overview of your sprints Naming sprints with sequential city names Naming sprints with random animal names Onboarding makes it easy to get started Inline Edit Functionality Make your sprints shine in the Jira Backlog! Inspiration The inspiration for building this app from a challenge my team faced: how to effectively manage and differentiate sprints . We use Jira as our agile planning solution, applying the scrum methodology within the team, with 2-week sprints, planning, review and retrospective meetings. In addition to having an active sprint, we also tentatively plan several sprints ahead, as well as storing information on historic sprints. Information on sprints is split between the Sprint Report, Backlog and Active Sprints tabs depending on whether you are looking at historic, active or future sprints and we wanted a way to see all of this information in one place. In order to better differentiate sprints, which we previously identified with sequential numbers (Sprint 1, 2, 3 etc.), we decided to also give each sprint a fun name following a common theme - in our case animals (Alpaca 🦙, Bobcat 😸, Chickadee 🐥 etc.) and doing this sequentially both helps identification and provides an additional reference point for the position of the sprint (as well as being a bit of fun 😀). We found voting on what to call the next sprint a fun and creative addition to our agile ceremonies. What it does The core functionality is based around solving the two core problems identified above: View all sprints for a particular board and easily update the name, goals and target dates Automatically generate custom names for future sprints based on a theme SprintEd (a shortening of Sprint Editor) is available from all Jira software projects for teams using scrum and can be accessed from the sidebar: It's a marathon, not a sprint To fulfil the first requirement, I needed to be able to show a list of all of the sprints contained in the project to let you see your sprints from a birds-eye view. After opening the app, you are presented with a list of sprints for the active board which provides the following functionality: Quickly view, sort, filter and update sprint information from the table Automatically assign names to sprints based on a theme using the Auto-Name feature Easily view and change issues contained in a sprint Export sprint data for use in other applications Adding some personality Teams all over the world assign internal names to things like releases, versions and initiatives (codenames) - for example, Breezy Badger is the codename for Ubuntu 5.10 - but sometimes it's difficult to get inspiration and that's where the auto-name feature comes into play, generating names for your active and future sprints using the options you provide - select from a list of themes, such as animals, city names, anime characters and whether you want to apply them sequentially or randomly If you want some more inspiration, you can randomize the names and find a set of names that you like! How did you build it? For this hackathon, I wanted to identify an opportunity in Jira or Confluence based on improvements and ideas from my teammates. First, I identified what these opportunities were and which areas to target with the initial proof of concept and for each opportunity, I documented the requirements and dependencies of that feature and how it could be integrated with the host application in an effective way. Next, I took this document and checked the requirements against the following criteria: Is it feasible within the allotted timeframe (2 weekends)? Did the idea have reach beyond just our needs? Do the required Forge modules exist? Does the Atlassian Cloud REST API have the required APIs? Once I had performed this validation, the sprint management idea was chosen, as it was the most feasible, had a well-defined scope and most of the APIs existed to make the app useful. The next step was to decide what tools to use to build the app and the best place to start was the Atlassian Forge documentation site , which guided me to the Forge CLI tool which made it easy to get started by selecting the most relevant template and provided me with a quick way to try out the UI Kit and Custom UI rendering options and figure out which one I needed to fulfil the requirements - as I had experience with React, I chose the Custom UI approach and cloned the forge-turbo library by toolsplus which provided me with a monorepo with which to start coding - I also decided to use the AtlasKit UI library to ensure that the UI matched what users were already familiar with in Jira. At several points during development, I collected feedback from potential users and tweaked the UI and functionality until all feedback had been taken into account and ended with a round of user acceptance testing. Challenges encountered I encountered a number of challenges during the development of the app: Deciding on the right idea to turn into an app Figuring out the best way to present the application to the user within the Jira interface Presenting the Auto-Name interface in an easy to use and intuitive way How to onboard new users to the app One of our initial ideas was the automated renaming of sprints according to project-level configuration, which would detect when new sprints are created and change their name using the Forge Triggers functionality, however, there isn't currently support for Jira software sprint events, which makes this more difficult - while I believe that there is a way to implement this feature with a Web Trigger and a manually configured Jira webhook this wasn't feasible in the timeframe allocated. Accomplishments that you're proud of Making the Auto-Name feature work in a simple and intuitive way was challenging and went through several revisions until it was easy to understand - the addition of the animated transitions when the value changes used visual means to make it clear that the name had changed. The inline edit feature on the main table was tricky to get working without the layout of the table changing when the editable field was opened and took some adjustment to get right, but it turned out well and allows for quick changes to be made without switching dialogs. The onboarding module was a last-minute addition to the application, as it was discovered that the inline editing capabilities of the table were not clear enough - as they visually look indistinct from paragraph text and it would be a good idea to have a tutorial that is shown on the first launch that demonstrated what you can do! What you learned I learnt it's possible to build complex apps with Forge in a relatively short period of time. The command line interface made getting started easier and there was a good selection of resources and reference material available online. <div