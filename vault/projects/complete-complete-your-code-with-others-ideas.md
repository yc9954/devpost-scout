---
slug: "complete-complete-your-code-with-others-ideas"
url: "https://devpost.com/software/complete-complete-your-code-with-others-ideas"
title: "Complete"
hackathon: "Hack the North 2019"
winner: true
words: 499
team_size: 4
has_repo: true
has_live: false
has_video: false
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "mechanism/retrieval_grounding"
  - "substrate/document_pdf"
  - "substrate/web_dom"
---

# Complete

> Complete: your code with other's ideas

[Devpost](https://devpost.com/software/complete-complete-your-code-with-others-ideas) · hackathon [[Hack the North 2019]]

## Facets

**mechanism** [[realtime_stream]] [[retrieval_grounding]]
**substrate** [[document_pdf]] [[web_dom]]

**stack** css3, flask, html, javascript, python, selenium, typescript

## How they structured the write-up

- inspiration
- improving today's coding experience
- revolutionising tomorrow's coding methodology
- how we built it
- challenges we ran into
- what's next for complete: your code with other's ideas

## Body

Automatically generate functions via a description! Copy code from all over the internet without Alt-Tabbing!!! Inspiration Before I solve my complicated calculus assignment, I go through examples. I don't even go through my notes, but I go through the solved examples. I do the same while coding something complicated. I go through the examples in the documentation and on StackOverflow. But why should I do the searching and reading when I can have my computer do it for me? Complete does exactly that. It parses the internet and produces code snippets in real-time to complete your code with other's ideas. Reading through pages of documentation and bad StackOverflow answers is a thing of the past! Improving today's coding experience Complete is a VSCode extension that parses GoogleCode, Github, Bitbucket, Codeplex, FedoraProject, Sourceforge and Minix3 using the Search code API. All the user has to do is highlight (or search for) code in his/her IDE and Complete renders code snippets from open source repos that use the highlighted bit of code. How is it different from just a google search? Our searching algorithm. You could get the same examples Complete gathers through parsing the internet but not in under 3 seconds and in the comfort of your favourite IDE, VSCode! Revolutionising tomorrow's coding methodology We have come one step closer to a 5th generation programming language with Complete. We have incorporated GitHub's Semantic Code search for a subset of Python. All the user has to do is type out a comment with what he/she wants the code to do and we interpret the meaning and insert a code snippet that should connect into the flow of the code with minor changes. How we built it We used typescript, HTML, CSS and JavaScript to create an appealing front end that is intuitive and convenient to use for long periods of time. Our searching algorithm - We use TF-IDF (term frequency-inverse document frequency) to weight keywords in highlighted snippets and process only the important keywords while searching. We use the Search code API to parse the web and get actual code snippets. We then run the results from through Difflib, a difference comparator, to get the most similar and relevant snippets. Semantic Search- We process users comments (that start with '@s') and run it on GitHub's Semantic search and use selenium to scrape the data. Challenges we ran into Processing large chunks of code into a few meaningful keywords was by far the hardest challenge. Not all words have equal importance and weighting them maningfully was rather complicated. We used TF-IDF and Difflib to get through this. Learning typescript from scratch to make our vscode was a mammoth task that took a lot of time and effort. What's next for Complete: your code with other's ideas Improving the searching algorithm! Our algorithm can be further fine-tuned and results further refined. Semantic search is the cutting edge of research. Keeping up with developments and research is vital in keeping our tool relevant. <div