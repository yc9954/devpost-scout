---
slug: "autoflow-a4dhkw"
url: "https://devpost.com/software/autoflow-a4dhkw"
title: "Autoflow"
hackathon: "DevRev Hackathon - Coding with AI"
organization: "DevRev"
winner: true
words: 848
team_size: 4
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/retrieval_grounding"
  - "domain/developer_tools"
  - "domain/security_privacy"
  - "user/developer"
  - "user/researcher"
  - "substrate/code_repository"
  - "substrate/financial_record"
  - "substrate/geospatial"
  - "substrate/structured_db"
---

# Autoflow

> VS Code extension that uses OpenAI Codex and other open source models to automate developer workflow. It generates, autocompletes, and searches for source code, documentation, and git commit messages

[Devpost](https://devpost.com/software/autoflow-a4dhkw) · hackathon [[DevRev Hackathon - Coding with AI]]

## Facets

**mechanism** [[retrieval_grounding]]
**domain** [[developer_tools]] [[security_privacy]]
**user** [[developer]] [[researcher]]
**substrate** [[code_repository]] [[financial_record]] [[geospatial]] [[structured_db]]

**stack** fastapi, huggingface, openai-codex, python, pytorch, typescript

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for autoflow

## Body

GIF explanation GIF autocompletion Inspiration Nowadays, with the rising popularity of using machine learning to automate development workflow, several organizations are releasing coding assistants that help developers in their day-to-day tasks. One such example is OpenAI Codex. This is a version of GPT-3 that has been finetuned on source code from GitHub. It can perform tasks like generating source code and documentation. Users can request to use this model for free. However, there is a steep learning curve for new users. The code it generates is usually not aligned with the user’s intention. This is because users need to read OpenAI’s documentation on Codex best practices for prompts. Moreover, every type of tasks requires a specific set of parameter values for Codex. These can only be optimized through trial and error. To solve this, we developed Autoflow so that users get exactly what they want. We read up on all the best practices and experimented with Codex’s parameters. We then developed a series of templates for different kinds of tasks. These templates are used to instruct Codex to perform a specific task accurately. Furthemore, there are a set of tasks on which Codex performs poorly such as code refactoring and vulnerability detection. It also does not provide source code embeddings for free. Therefore, to extend the scope of our extension, we used open source models from HuggingFace to support tasks like code refinement, defect detection, semantic code search, and git commit message generation. What it does Autoflow provides plenty of features which are listed below User Intent Analysis Code Generation Code Explanation Documentation Generation Generating SQL Queries from Natural Language Commands Explaining SQL Queries Automatic API Calls Error Explanation Bug Fixing Create Function One Liners Unit Tests Generation Code Autocompletion Refactoring Code Detecting Vulnerabilities Github Commit Message Generation Code Semantic Search How we built it Bridging the gap between User and Codex Users do not always know the best practices to use Codex. Codex can not understand the context of poorly formatted queries This creates a gap between user's need and code generation. We have bridged this gap by creating custom templates. Users explain their need through easy commands and form inputs. We analyzse these inputs and generate custom templates with certain keywords that are part of Codex best practices to generate accurate results. Given below is a sample template we used to convert functions into one-liners: ''' <comment start> Convert this function in <language> to a one line function<comment end> <function header> <code> <comment start><language> one line version<comment end>: <function header> <return statement>''' Intent Analysis First and foremost problem is to understand the requirement of the developer. New users don’t have to memorize the commands needed to use our extension. They simply need to add a comment prefixed with #: for python files and //: for other files. They are then suggested the command for their intent in CodeLens. We also provide a more option which opens the command palette for the user. We have used Sentence Transformer (SBERT) model MiniLM-L6-v2 to understand the intent of the user. Development We developed a FastAPI server that acts as the backend. We developed the frontend for our extension in TypeScript. The extension takes user input from the frontend and sends a request to the server. The server first identifies the user’s intent. After doing so, it maps the user’s prompt into a set of templates. These template prompts are sent to Codex. We return the output to the frontend. We only performed a few other tasks using other open source models like CodeT5 , CodeBert , MiniLM-L6-v2 and CommitBert . Challenges we ran into Codex only provides accurate results on scripting languages like Python and JavaScript. It struggles on languages like Java and C++ We prefered accuracy over efficiency, so the features for which we used Codex are not returned instantly We had to recreate the source code embedding tensors for user’s source code everytime instead of efficiently editing only the parts that changed. This is mainly due to time constraints Accomplishments that we're proud of Learned to engineer prompts that accurately instruct Codex on what it should do Incorporated features beyond Codex’s capabilities by adding the latest large language models Ensured the UX is easy for beginners and accurate for experts What we learned This was the first time we developed a VS Code Extension. It has inspired us to develop extensions for the marketplace We learnt to use HuggingFace and SBERT for common NLP tasks What's next for Autoflow Add extended support for Java and C/C++ Currently code search only works for a single user. Our server overwrites a single code embeddings file everytime we get a request to update the user’s codebase embeddings. We will create a database that creates separate code embeddings for every user Customize our extension for common developer profiles like data scientists and developers. We would create custom templates for commonly occuring tasks in these domains and only show each user the commands based on their profile Deploy our server on the cloud and publish our extension on VS Code marketplace <div