---
slug: "autolock"
url: "https://devpost.com/software/autolock"
title: "AutoLock"
hackathon: "Cal Hacks 11.0"
organization: "Cal Hacks"
winner: true
words: 460
team_size: 1
has_repo: true
has_live: false
has_video: false
tags:
  - "project"
  - "domain/developer_tools"
  - "domain/security_privacy"
  - "user/developer"
  - "substrate/code_repository"
---

# AutoLock

> Have you ever written insecure code? Probably, but how do you know? How do you fix it? Finding and fixing insecure code can be hard, so AutoLock makes simple.

[Devpost](https://devpost.com/software/autolock) · hackathon [[Cal Hacks 11.0]]

## Facets

**domain** [[developer_tools]] [[security_privacy]]
**user** [[developer]]
**substrate** [[code_repository]]

**stack** gin, go, javascript, postgresql, svelte, typescript

## How they structured the write-up

- inspiration
- what it does
- how i built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for autolock

## Body

Our Sweet Landing Page! Logging in with GitHub User home page Installation Page Installation Waiting Page Install Pull Request (Auto Generated) Vulnerability Screen Vulnerability Screen After Requesting Fix Vulnerability Fix Pull Request (Auto Generated) Inspiration During my last internship, I worked on an aging product with numerous security vulnerabilities, but identifying and fixing these issues was a major challenge. One of my key projects was to implement CodeQL scanning to better locate vulnerabilities. While setting up CodeQL wasn't overly complex, it became repetitive as I had to manually configure it for every repository, identifying languages and creating YAML files. Fixing the issues proved even more difficult as many of the vulnerabilities were obscure, requiring extensive research and troubleshooting. With that experience in mind, I wanted to create a tool that could automate this process, making code security more accessible and ultimately improving internet safety What it does AutoLock automates the security of your GitHub repositories. First, you select a repository and hit install, which triggers a pull request with a GitHub Actions configuration to scan for vulnerabilities and perform AI-driven analysis. Next, you select which vulnerabilities to fix, and AutoLock opens another pull request with the necessary code modifications to address the issues. How I built it I built AutoLock using Svelte for the frontend and Go for the backend. The backend leverages the Gin framework and Gorm ORM for smooth API interactions, while the frontend is powered by Svelte and styled using Flowbite. Challenges we ran into One of the biggest challenges was navigating GitHub's app permissions. Understanding which permissions were needed and ensuring the app was correctly installed for both the user and their repositories took some time. Initially, I struggled to figure out why I couldn't access the repos even with the right permissions. Accomplishments that we're proud of I'm incredibly proud of the scope of this project, especially since I developed it solo. The user interface is one of the best I've ever created—responsive, modern, and dynamic—all of which were challenges for me in the past. I'm also proud of the growth I experienced working with Go, as I had very little experience with it when I started. What we learned While the unstable CalHacks WiFi made deployment tricky (basically impossible, terraform kept failing due to network issues 😅), I gained valuable knowledge about working with frontend component libraries, Go's Gin framework, and Gorm ORM. I also learned a lot about integrating with third-party services and navigating the complexities of their APIs. What's next for AutoLock I see huge potential for AutoLock as a startup. There's a growing need for automated code security tools, and I believe AutoLock's ability to simplify the process could make it highly successful and beneficial for developers across the web. <div