---
slug: "find-your-open-source-opportunity"
url: "https://devpost.com/software/find-your-open-source-opportunity"
title: "Find Your Open Source Opportunity"
hackathon: "GitLab Innovation Pitch Competition"
organization: "GitLab"
winner: true
words: 307
team_size: 1
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "domain/developer_tools"
  - "user/developer"
  - "substrate/code_repository"
  - "substrate/structured_db"
  - "substrate/web_dom"
---

# Find Your Open Source Opportunity

> FYOSC analyzes your recent Gitlab activity, projects, and dependencies and suggests open source projects that you should contribute to, no matter what skillset you have, making open-source sustainable

[Devpost](https://devpost.com/software/find-your-open-source-opportunity) · hackathon [[GitLab Innovation Pitch Competition]]

## Facets

**domain** [[developer_tools]]
**user** [[developer]]
**substrate** [[code_repository]] [[structured_db]] [[web_dom]]

**stack** gitlab, nextjs, supabase

## How they structured the write-up

- inspiration
- features
- how we built it
- what's next for find your open source opportunity

## Body

Landing Page Recent Projects Open Source Issues Your Profile Inspiration URL: https://gitlab-innovation-pitch.vercel.app/ Goal: Enable a diverse set of people to contribute to open source projects that they use and love. Category: #socialimpact #dx Open source projects are the backbone of the software industry. However, many open-source projects face challenges in attracting contributors, maintaining codebases, and ensuring the sustainability of their work. On the other hand, developers often struggle to find meaningful open-source projects to contribute to, especially when they are new to the open-source community or not a in a traditional developer role. This project aims to address these challenges by providing a platform that connects developers with open-source projects that align with their skills, interests, and preferences, fostering a more inclusive and diverse open-source ecosystem. Comic by XKCD: https://xkcd.com/2347/ Features User Authentication : Users can sign in using their GitLab account, allowing the platform to access their repositories and projects. Profile Creation : Depending on the recent activity of the user, the platform will categorize your skills and interests into different categories. Builders, Managers, and Testers. Dependency Analysis : The platform will analyze the dependencies of the user's projects Project Recommendations : Based on the user's skills and dependencies, the platform will recommend open-source projects that align with their preferences. How we built it The project is built using Next.js for the frontend, Supabase for database & authentication, and the GitLab API for retrieving user/project data and authentication. The implementation currently supports Node.js projects and NPM packages hosted on GitLab, with the potential for expansion to other programming languages by adding parsers for specific dependency management tools. Gitlab Project What's next for Find Your Open Source Opportunity Moving forward, the project aims to expand its support for additional programming languages and dependency management tools, making it accessible to a broader range of users and projects. <div