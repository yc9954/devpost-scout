---
slug: "linked-items-for-monday"
url: "https://devpost.com/software/linked-items-for-monday"
title: "Linked Items for monday"
hackathon: "monday.com Apps Marketplace Challenge: solutions for teams "
organization: "Monday.com"
winner: true
words: 982
team_size: 10
has_repo: false
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/cross_origin_web"
  - "domain/developer_tools"
  - "domain/retail_commerce"
  - "user/developer"
  - "substrate/code_repository"
  - "substrate/document_pdf"
---

# Linked Items for monday

> Connect tasks and get an overview of all their relations

[Devpost](https://devpost.com/software/linked-items-for-monday) · hackathon [[monday.com Apps Marketplace Challenge- solutions for teams]]

## Facets

**mechanism** [[cross_origin_web]]
**domain** [[developer_tools]] [[retail_commerce]]
**user** [[developer]]
**substrate** [[code_repository]] [[document_pdf]]

**stack** figma, graphql-api, monday-design-system, mondayapi, mondaysdk, react, react-diagrams-library, redux, typescript

## How they structured the write-up

- inspiration
- what it does
- use cases
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for linked items for monday

## Body

Inspiration We realized that managing large projects calls for a clear overview of what’s going on. Some task block others while some require an action from another team. Skipping between different boards sometimes becomes too demanding to keep it all in check. This is why we came up with an idea of linking items and showing their relations in an easy-to-read form. What it does The app lets you link items in many ways – you can decide whether they are simply connected, one task blocks another, one task causes a series of other tasks, or they remain in any other relation. The results can be displayed in two forms: Table: A customizable table view showing different groups of links, where you can preview the most important details and interact with linked items directly from the side drawer. Graph: A highly visual form of displaying all interconnections of a given item. The app comes with handy built-in templates that show how to start and how to benefit from every feature. There’s a possibility to add tasks on the go, right form the side drawer, so that they get automatically linked in the chosen way. The graph lets you get an overview of all the tasks in just a blink of an eye as well as giving you more control over the project lifecycle. It’s a flexible solution for all business types, no matter their scale. Use cases Here’s how Linked Items for Monday may help different businesses: #1 International sales department A large organization with clients all over the world may want to keep a close eye on all business processes on just one board. Upcoming deals require many people and groups to work in sync, so that agreements, presentations and documents are all created on time. Not to mention meetings, calls, emails and sudden plan improvements. Linked Items gets all that work connected, so no one will ever miss a task. #2 Software house The success of a software house depends heavily on a swift cooperation between the development and many different teams. Developers, support engineers, technical writers as well as sales and marketing people can work closely together, dynamically developing the product to meet all their clients’ needs. Linked Items provides everyone with a clear overview of what the others are up to, so that everyone is up to speed. #3 Family-run home renovation business Even the smallest business has to plan the work ahead in an organized way. Building and renovating things proves to be especially complex in terms of preparations, deliveries and deadlines. Linked Items comes in handy whenever tight coordination is needed. Missing some essential materials? No problem! Simply add them to your partner’s shopping list that they can read on the go. How we built it We started by modelling the data we wanted to present and ended up with two display modes: a table and a graph. Then we divided the team into two groups, each of which worked on one of the views. The graph view required us to do some research to find a suitable library that would allow us to achieve our goals. While working on the table view, a large part of the application was created: components, communication with the Monday API, which we could then use again in the graph view. The last step was to put everything together, which brought us a lot of joy. The application was mainly written in Typescript with the use of the React framework and the Redux library. The React-diagrams library has helped us a lot, as it is very flexible and easily adaptable to different purposes. Monday’s SDK proved to be very user-friendly for developers. We enjoyed working with the API written in GraphQL that, combined with the ability to test queries on the Monday platform and the pre-defined scheme of Monday’s API capabilities, made our work smooth and efficient. Challenges we ran into A big challenge was to design a way to present item dependencies to the user. On the one hand, we tried to give the users as much information as possible, while on the other, we wanted to be able to visually associate the correlations in the blink of an eye. For this reason, we decided on two views: a table and a graph, which we humbly believe worked out really great! Since the application is embedded in an iframe, another challenge was to design it in a way that would fit well into the Monday platform, which we again believe was successful. Accomplishments that we're proud of We are most proud of the fact that we were able to get together and work efficiently and in a good atmosphere on a common goal, despite the fact we do not work together on a daily basis. We are deeply confident our app solves real everyday problems while also making the work easier and more pleasant for the user. What we learned Working on this project has given us all a fresh perspective on our daily tasks. We were able to confront our previous knowledge of developing applications for different platforms with what Monday has to offer. This has shown us new perspectives for our future projects. We realized that new challenges not only bring fresh ideas, but also teach us how to use our existing knowledge and skills for the benefit of our partners. What's next for Linked Items for monday By the end of the project we had our heads full of ideas for further app development. We feel entirely committed to this product! Here’s what we’d love to work on next: displaying more details of the linked items in the drawer adding a preview of information from other columns, like status and priority adding a global page with an overview of all item links and relations generating a tree structure showing even deeper levels of item connections <div