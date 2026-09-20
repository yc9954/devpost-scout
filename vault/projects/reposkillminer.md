---
slug: "reposkillminer"
url: "https://devpost.com/software/reposkillminer"
title: "RepoSkillMiner"
hackathon: "Azure AI Hackathon"
organization: "Microsoft"
winner: true
words: 728
team_size: 1
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "domain/developer_tools"
  - "domain/labor_employment"
  - "user/developer"
  - "substrate/code_repository"
  - "substrate/financial_record"
  - "substrate/structured_db"
---

# RepoSkillMiner

> This app identifies low-level expertise on particular software frameworks and technologies , relying solely on GitHub data, using the Microsoft Language Understanding Intelligent Service (LUIS).

[Devpost](https://devpost.com/software/reposkillminer) · hackathon [[Azure AI Hackathon]]

## Facets

**domain** [[developer_tools]] [[labor_employment]]
**user** [[developer]]
**substrate** [[code_repository]] [[financial_record]] [[structured_db]]

**stack** blazor, c#, luis

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for reposkillminer

## Body

Inspiration A GitHub profile is becoming an essential part of a developer’s resume enabling HR departments to extract someone’s expertise, through automated analysis of his/her contribution to open-source projects. At the same time, having clear insights on the technologies used in a project can be very beneficial for resource allocation and project maintainability planning. In the literature, one can identify various approaches for identifying expertise on programming languages, based on the projects that developer contributed to. What it does In this app, we move one step further and introduce an approach to identify low-level expertise on particular software frameworks and technologies apart, relying solely on GitHub data, using the GitHub API and Natural Language Processing (NLP)—using the Microsoft Language Understanding Intelligent Service (LUIS). How we built it We developed an NLP model in LUIS for named-entity recognition for three (3) .NET technologies and two (2) front-end frameworks. Our analysis is based upon specific commit contents, in terms of the exact code chunks, which the committer added or changed. Step 1. Data Collection. We used GitHub’s REST API ver. 3 [21] to retrieve up-to-date data from GitHub repositories. Given a GitHub organization or repository we retrieve all commits as well as the authors of each commit. For every commit we retrieve the files included and the actual code chunks for these files. We preferred API ver. 3, over its successor ver. 4, because although the latest uses GraphQL, up to now there is no way to retrieve file contents using this version of the API. Step 2. Identification of commits’ programming language. For each retrieved commit we check the files included in the commit and in particular the file extensions to identify the employed pro-gramming languages. To do so, we use a slightly modified (re-moved duplicates and added a few more file extensions) version of the classification provided by GitHub Linguist [22], which is the library that GitHub uses for providing the language distribution information for the repositories. Both original and the modified classification file are available online. Step 3. Identification of commit technologies with LUIS. We built a model in LUIS to identify three (3) technologies in the .NET framework domain, namely: (a) Language-Integrated Queries (LINQ) which are first-class language constructs that allow writing of queries against strongly typed collections of objects; (b) Asyn-chronous Programming that allows code in the form of sequential statements which however executes based on external resource allocation and according to the order of tasks; and (c) Entity Framework which is an object-database mapper. Moreover, LUIS is trained to identify two (2) front-end frameworks, namely: (d) Angu-lar and (e) React. LUIS needs input utterances (i.e., inputs from the user that the model needs to interpret) to be provided for each tar-get intent (technology/framework) in the training step. We note that an intent corresponds to a purpose or goal expressed in a user's utterance. To train LUIS to extract intents and entities it is important to capture a variety of example utterances. Active learn-ing, or the process of continuing to train on new utterances, is essential to machine-learned intelligence that LUIS provides. We have created 98 example utterances for the 5 intents using existing or slightly altered (mainly altered variable names) existing samples from the official Microsoft, Angular and React documentation. Challenges we ran into Since the tool is still in a prototype phase, the application has some limitations including browser support (Firefox is the only fully supported one) and API limitations (GitHub API sets a limit to 5000 requests per hour). Accomplishments that we're proud of We evaluate the precision, recall and f-measure for the derived technologies/frameworks, by conducting a batch test in LUIS and report the results. The results were very promising. What we learned We learned using LUIS and Blazor What's next for RepoSkillMiner We plan to include more detailed visualizations and in-depth in-sights from the collected data including the evolution of project technologies within an organization over time, the designation of technologies which are “at risk” because of lack of resources, the cross-tabulation of technologies and people’s skills, etc. Developers’ experience in terms of commits or years can also be derived by analyzing a projects’ history. Once the tool is enhanced with the ability to detect more low-level technologies, we plan to evaluate its accuracy against the actual skills held by developers in a selected company, using a questionnaire-based study. <div