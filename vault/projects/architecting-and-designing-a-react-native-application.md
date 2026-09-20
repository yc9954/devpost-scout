---
slug: "architecting-and-designing-a-react-native-application"
url: "https://devpost.com/software/architecting-and-designing-a-react-native-application"
title: "Architecting and Designing a React Native Application"
hackathon: "2020 Facebook Developer Circles Community Challenge"
organization: "Facebook"
winner: true
words: 496
team_size: 1
has_repo: true
has_live: false
has_video: false
tags:
  - "project"
  - "domain/developer_tools"
  - "user/developer"
  - "substrate/geospatial"
---

# Architecting and Designing a React Native Application

> A guide on architecting and designing a React Native application (with React Native v0.63), with the aid of a starter template (React Native with Typescript App Starter Template).

[Devpost](https://devpost.com/software/architecting-and-designing-a-react-native-application) · hackathon [[2020 Facebook Developer Circles Community Challenge]]

## Facets

**domain** [[developer_tools]]
**user** [[developer]]
**substrate** [[geospatial]]

**stack** java, javascript, mobx, react-native, typescript

## How they structured the write-up

- inspiration
- what it does
- how i built it
- challenges i ran into
- accomplishments that i'm proud of
- what i learned
- what's next for architecting and designing a react native application

## Body

Template App Landing Page/View Template App Landing Page/View - Tab 4 Template App - App Development Scratchpad Page/View Template App - Drawer Menu Template App - Recipe Box Sub-application Inspiration Every time I needed to create a new React Native application, I was starting from scratch, with the architecting, designing and piecing everything together. I needed to create a reusable template with all that, and as well other things I might need. What it does It provides a template which one can use to quickly start building their React Native application. How I built it I bootstrapped a new React Native application, and put in all the pieces like global stores management with MobX, routing and navigation with React Navigation, and an encompassing architecture and design philosophy on the project, that can be followed as I build future React Native applications, off of this template. Challenges I ran into Before building this template, I had already built a similar one for web with React, React JS SPA App Starter Template Framework . In web, I was persisting my global state (stores) to "localStorage" for offline functionality. Also, I could set automatic persistence of all stores with "onload" of the web app. However, here in React Native for mobile devices I have had to find a way to perform persistence, only when requested; and this actually ended up teaching me how to achieve the same for the web (earlier, once upon an interview, when I presented my web framework, the interviewer asked if I could be able to find a way for only "on-demand" persistence of the stores, when such a use case arises, and so I have finally been able to achieve that). Accomplishments that I'm proud of The design I have implemented for managing global app state (stores) and their persistence to AsyncStorage . This facilitates offline capability, and also retention of test data, across development reloads, which can really better the developer experience, by the developer not having to fill out data forms across development reloads. I am using MobX for the global state management, but it can be replaced with any other library on top of this same architecture and design. Also my design and architecture for navigation in this template, being handled by React Navigation routing and navigation library, is also agnostic of the routing and navigation library, and one can use any of their desired React Native routing and navigation library, on top of my navigation design and logic. All of this, is the culmination of close to 4yrs of building applications with React Native. What I learned I learned a little more about React Hooks and also greatly improved my Typescript skills. What's next for Architecting and Designing a React Native Application I want to build a CLI and maybe even a desktop studio, which future users can use with "low-code" to build even quicker, their React Native applications, based off of the design and architecture from this template. <div