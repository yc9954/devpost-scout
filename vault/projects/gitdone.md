---
slug: "gitdone"
url: "https://devpost.com/software/gitdone"
title: "GitDone"
hackathon: "Code with Kiro Hackathon"
organization: "Kiro"
winner: true
words: 726
team_size: 1
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "mechanism/vision_ocr"
  - "domain/developer_tools"
  - "domain/education"
  - "domain/supply_logistics"
  - "user/developer"
  - "user/educator_student"
  - "substrate/code_repository"
  - "substrate/structured_db"
  - "substrate/web_dom"
---

# GitDone

> A GitHub-integrated deadline tracker that can be embedded into Notion to increase developer productivity.

[Devpost](https://devpost.com/software/gitdone) · hackathon [[Code with Kiro Hackathon]]

## Facets

**mechanism** [[realtime_stream]] [[vision_ocr]]
**domain** [[developer_tools]] [[education]] [[supply_logistics]]
**user** [[developer]] [[educator_student]]
**substrate** [[code_repository]] [[structured_db]] [[web_dom]]

**stack** aws-acm, aws-cloudfront, aws-codepipeline, aws-elastic-beanstalk, aws-rds, css3, flask, github, github-api, html5, javascript, notion, oauth2, postgresql

## How they structured the write-up

- inspiration
- what it does
- how i built it
- challenges i ran into
- accomplishments that i'm proud of
- what i learned
- what's next for gitdone

## Body

GitDone_LandingPage_DarkMode GitDone_LandingPage_LightMode GitDone_DeadlineCreationPage_DarkMode GitDone_DeadlineCreationPage_LightMode GitDone_DeadlineCountdownCard GitDone_DeadlineCountdownCard_Completed GitDone_DeadlineCountdownCard_TimeUp GitDone_DeadlineCountdownCard_Notion Inspiration As a student developer, I am surrounded by deadlines throughout the year, be it assignments, projects, or exams. At times, it becomes hard to keep track and identify which deadline to focus on when you are juggling multiple of them. To ease this process and reduce my procrastination on certain tasks, I developed GitDone. What it does GitDone is an open-source productivity tool that integrates with a user's GitHub account via OAuth2. It allows developers to create and manage deadline-driven goals for their repositories, such as project shipments, bug fixes, or version updates. The application generates a real-time countdown for each goal, which is automatically marked as "completed" when a commit with a specific, user-defined message is pushed to the repository. Each countdown is also available as a unique embeddable widget, enabling seamless integration into third-party productivity tools like Notion. How I built it I began by using Amazon Kiro to help brainstorm the project requirements, outline the initial architecture, and break down the development into manageable tasks. The application is architected as a 3-tier, production-ready web service on AWS. The frontend, initially drafted with HTML and CSS, was significantly enhanced using claude sonnet-4 . It helped refactor the stylesheet for a fully responsive design, implemented the JavaScript for a light/dark mode toggle, and created the client-side logic to display the unique embed link. The backend is a Python application built with the Flask framework, which serves a REST API and dynamically renders the frontend. The data layer was migrated from a non-persistent SQLite file to a managed AWS RDS PostgreSQL instance to ensure data integrity and persistence. The compute layer is hosted on AWS Elastic Beanstalk, which manages the underlying EC2 server infrastructure and application deployments. The edge layer is handled by AWS CloudFront, which acts as a CDN to cache static assets and provides security by terminating SSL/TLS for a custom domain. The entire deployment process is automated through a CI/CD pipeline built with AWS CodePipeline, which triggers on every git push to the main branch on GitHub. Challenges I ran into The primary challenge was architecting a truly cloud-native application. Initially, using a file-based SQLite database resulted in a critical flaw where 100% of the application data was lost on every redeployment due to the ephemeral nature of Elastic Beanstalk's EC2 instances. Migrating the data layer to a persistent AWS RDS instance required a significant architectural refactor and a deep dive into cloud networking. Configuring the multi-service networking and security was also a major hurdle. It required systematically debugging the entire request path from DNS and CloudFront, through the application's firewall, to the database's firewall to ensure all components could communicate securely. This involved creating precise AWS Security Group rules to link the services while adhering to the principle of least privilege. Accomplishments that I'm proud of I am proud of successfully designing, building, and deploying a full-stack, 3-tier application from scratch on AWS. Overcoming the initial architectural flaws by migrating the database to RDS was a major accomplishment that transformed the project from a fragile prototype into a robust, reliable service. Furthermore, engineering a fully automated CI/CD pipeline with AWS CodePipeline was a significant success. This pipeline now handles the entire software delivery lifecycle, allowing for seamless and error-free deployments directly from GitHub commits, which is a cornerstone of modern DevOps practices. What I learned This project was a profound learning experience in cloud architecture and full-stack development. I learned the critical difference between ephemeral and persistent storage in a cloud environment and gained hands-on experience implementing a managed database solution with RDS. I also developed a deep understanding of cloud networking and security by configuring security groups and troubleshooting connectivity across a multi-service stack. Finally, I learned how to methodically debug a complex, distributed system by isolating issues at each layer, from the end-user's browser all the way down to the database. What's next for GitDone The next steps for GitDone are focused on expanding its feature set and utility. I plan to integrate a notification system, expand support to other Git providers like GitLab, and develop a more advanced user dashboard with analytics. As the project is open-sourced, the ultimate goal is for the community to contribute and help shape its future, adding the features and integrations they desire most. <div