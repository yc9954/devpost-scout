---
slug: "zed-vscode"
url: "https://devpost.com/software/zed-vscode"
title: "Zed"
hackathon: "DevRev Hackathon - Coding with AI"
organization: "DevRev"
winner: true
words: 298
team_size: 1
has_repo: false
has_live: false
has_video: false
tags:
  - "project"
  - "mechanism/structural_withholding"
  - "domain/developer_tools"
  - "domain/health_clinical"
  - "user/developer"
  - "substrate/financial_record"
---

# Zed

> The Extensible Developer Toolkit for Increased Productivity

[Devpost](https://devpost.com/software/zed-vscode) · hackathon [[DevRev Hackathon - Coding with AI]]

## Facets

**mechanism** [[structural_withholding]]
**domain** [[developer_tools]] [[health_clinical]]
**user** [[developer]]
**substrate** [[financial_record]]

**stack** developer, javascript, openai, productivity, vscode

## How they structured the write-up

- the extensible developer toolkit for increased productivity
- features:
- requirements

## Body

Zed The Extensible Developer Toolkit for Increased Productivity Zed is a combination of 6 features that solve the most common developer pain points: Code Generation, Debugging and Error Diagnoses. Features: 1. Search StackOverflow right within VSCode Discovered a bug/error you've never seen before? Quickly search for that on StackOverflow without ever leaving VSCode. 2. Read in-depth articles from popular developer blogs (e.g freeCodeCamp) Need to brush up on a particular skill/forgot what the charAt() method in Java does? Brush up your knowledge by browsing through high-quality articles on popular developer blogs such as freeCodeCamp.org. Due to how the freeCodeCamp RSS feed is structured, only the latest 10 articles can be fetched. This is a work in progress. 3. Generate high-quality documentation using OpenAI Let Zed take over the documentation-writing process for you. This step, powered by OpenAI, will generate relatively high-quality documentation for function in a variety of different languages ( Python/Javascript/Java/Go/C# currently). 100% accuracy cannot be guarenteed however. 4. Generate code from Natural Language/Text Let Zed generate code for you! Simply provide a short description of your intended function, highlight it, and execute the Zed command. As easy as 1, 2, 3. This uses OpenAI initially; however, if we determine that the returned code is not sufficiently valid, we fetch code from top StackOverflow posts matching the search query. 5. Super-charge console.log statements [JavaScript-specific] Automate the process of "print-debugging" by selecting the variables you want to track during program execution, and Zed will generate console.log statements for each selection with custom file and line information as well as the parent function/class. 6. Realtime Variable Tracking in the VSCode Debugger [JavaScript-specific] Track the output of all console.log statements during debugging in the VSCode Debugger. The output is inlined neatly with said console.log statement. Requirements OpenAI Auth Key <div