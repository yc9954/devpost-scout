---
slug: "ai-coding-boost-developer-productivity"
url: "https://devpost.com/software/ai-coding-boost-developer-productivity"
title: "AI Coding - Boosting developer productivity"
hackathon: "DevRev Hackathon - Coding with AI"
organization: "DevRev"
winner: true
words: 865
team_size: 1
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "domain/developer_tools"
  - "user/developer"
---

# AI Coding - Boosting developer productivity

> Collaborative and fun Human-AI loop to generate code, fix and explain errors, generate unit tests and documentation. The future of development in a VSCode extension powered by OpenAI Codex.

[Devpost](https://devpost.com/software/ai-coding-boost-developer-productivity) · hackathon [[DevRev Hackathon - Coding with AI]]

## Facets

**domain** [[developer_tools]]
**user** [[developer]]

**stack** codex, node.js, openai, vscode

## How they structured the write-up

- inspiration
- what it does
- how we built it
- project structure & documentation
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for ai coding - boost developer productivity

## Body

Step 1 - Current code context Step 2- User instruction Step 3 - Sending to models Step 4 - Review code and accept AI Coding tasks Inspiration The developer workflow hasn't changed for years. We repeat ourselves over and over again and we need to write similar code to solve problems we have already solved, just in a different context. More important than the code developers create is actually their know-how of solving problems. So the question is: Isn't there a better way to develop code? How could we empower developers and boost their productivity by focusing on what needs to be done, and less on how it is done? The answer is AI Coding: a human-AI collaborative loop to boost developer productivity. What it does The future of programming is here: with AI Coding, developers focus on their knowledge of knowing what to do. AI Coding is an AI powered VSCode extension that boost developer productivity in four main areas ( install the extension ): AI auto code generation Through a collaborative Human-AI coding loop, developers can express their ideas in natural language and AI Coding will generate/change/edit the code for you. Focus on getting more done by saying what needs to be done, and let the machine do the repetive work of creating code for you. AI auto debugging Easily find the sources of bugs/errors and find fixes for them. Just copy the error message and AI Coding will automatically identify the source of error and even fix the bug for you. AI auto unit-testing Developing code is not enough. Your code needs to be tested in order to make it production-ready. AI Coding generate unit tests in a single click. Just right click and select Generate unit-tests and AI Coding will do the hard work for you. AI auto documentation Documenting code is also an important part of the developer flow, as others will review/edit your work in the future. For this, AI Coding helps you by automatically documenting your code with a single click. How we built it AI Coding is powered by OpenAI Codex model. It is an interactive collaborative human-AI loop made of 4 steps: Current context - We need to pass the content of the file we want to generate code/edit to the Codex model. For this, the code for the current active text editor is extracted (if it is a new file, it will be empty, but Codex work with well with empty contexts as well). Instructions - The next step is to take the user instruction on what needs to be done. This is extracted from a text area in the left bottom corner, in the AI Coding panel. Some instructions are pre-made (such as the instructions for installing packages, generating tests, improving documentation). For theses cases, there is a set of specific prompts used for each use case. Generation - Next, both the instruction and context are sent to the OpenAI codex endpoint. The code is generated until no more code is generated. Finally, the resulting code is shown side by side in a diff view, the same view used for comparing Git changes. This allows the developer to review the changes and accept them in a single click. When accepting the changes, the file content is them updated with the generated code. These are the 4 steps of the future of development: context, instruction, generate, and review. This loop can be repeated as many times as you want to develop any kind of application in any language. It is a fun, collaborative, and faster way to develop code. You won't want to go back to the old way! Project structure & documentation extension.ts - This is where the extension actions are registered. The correct AI action is called depending on which action is selected by the user. codegen.ts - The main app code which is responsible for delegating the action to different subtasks. It is responsible for: updating/reading state reading/setting user api key reading/updating current file instantiating editor view showing error messages calling code generator methods managing accept/cancel flow generator.ts - Responsible for calling the different OpenAI Codex engines. I am using both Codex Completion and the recently release Codex Edit api . prompts.ts - Builds the correct prompt to send to OpenAI Codex based on the different user tasks. state.ts - Manages the application state views.ts - Builds the webview to render the editing view. Challenges we ran into Using OpenAI Codex is very different. You need to develop the right "prompts" in order to guide the model into the right direction. Most of challenge was trying to figure out the best prompts to yield the best results in terms of code generation. Accomplishments that we're proud of I'm proud of having created a new and unique user experience with a human-AI-loop that not only boost developers productivity but also it is fun and engaging to work with. What we learned Development of VSCode extensions How to work with OpenAI Codex models and how to prime them What's next for AI Coding - Boost developer productivity Add more tools and capabilities to automate more daily tasks of the developer workflow Improve UX <div