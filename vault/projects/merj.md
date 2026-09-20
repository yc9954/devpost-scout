---
slug: "merj"
url: "https://devpost.com/software/merj"
title: "merj"
hackathon: "Cal Hacks 12.0"
organization: "Cal Hacks"
winner: true
words: 667
team_size: 4
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/retrieval_grounding"
  - "domain/developer_tools"
  - "user/developer"
  - "substrate/code_repository"
---

# merj

> Merj is your AI-powered merge copilot. It reviews both branches, understands intent with CodeRabbit, and uses Claude to suggest secure conflict resolutions automatically. One command. Zero headaches.

[Devpost](https://devpost.com/software/merj) · hackathon [[Cal Hacks 12.0]]

## Facets

**mechanism** [[retrieval_grounding]]
**domain** [[developer_tools]]
**user** [[developer]]
**substrate** [[code_repository]]

**stack** bash, chromadb, claude, coderabbit, javascript, python, voyageai

## How they structured the write-up

- inspiration
- what it does## inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for merj

## Body

Project Workflow Inspiration What it does## Inspiration Every developer knows that sinking feeling when a git pull command results in a merge conflict. The resulting scramble to pursue multiple lines of code is tedious and severely detrimental to the development process. What it does What if you never had to worry about merge conflicts again? That is why we built merj, a robust command-line tool that harnesses the power of modern Artificial Intelligence to streamline this process for developers. When a developer runs a pull command from their terminal, our software automatically scans for potential merge conflicts. It uses codebase context to resolve them effectively while preserving the goals of both branches. How we built it merj is a tool we built on top of Git to minimize the learning curve for developers using our software. At a high level, merj has two states immediately after being called: a clean state and a conflict state. When the state is clean, our merj pull command behaves like git pull and updates the codebase; however, if our git pull results in a merge conflict, we immediately start our troubleshooting logic. The first thing we do is take a diff between the remote node and the last common ancestor node of the divergent nodes, and a diff between the local node and the same last common ancestor node. We then run a Retrieval Augmented Generation pipeline using the voyageai API to embed text, and ChromaDB to store vector embeddings, to retrieve code chunks from our codebase that are most relevant to the merge conflict, providing context for future LLM calls. After we get the code context, we use CodeRabbit’s powerful agent to summarize the changes between each divergent node and its common ancestor, providing semantic context alongside our code context. Finally, we combine all this context with the current merge conflict in Claude 3.5 Sonnet to perform our final resolution. Challenges we ran into System design Integration LLM Formatting One of the key challenges that we spent a lot of time working on was designing the entire end-to-end system. This was the first time any member of our team had created a command-line interface tool or built something related to version control, so we had to gain a deep understanding of the inner workings of merge conflicts to develop an effective plan. Another major problem we ran into was integrating all our components. Our program consists of many different elements, such as version control, Retrieval Augmented Generation, CodeRabbit’s API, and LLM calling, which made it very hard to integrate into a single end-to-end pipeline. Lastly, we spent time optimizing the format of our LLM prompt to get the desired output for our clients. Accomplishments that we're proud of The main accomplishment we are proud of is our ability to integrate many different software components, with which we have minimal experience, into a single, cohesive software application that solves a practical problem many developers have faced. We were also really excited to learn about CodeRabbit and integrate their powerful ability to semantically synthesize information in git histories to enhance the quality of our final product response. What we learned Throughout the hackathon, our team learned practical skills in version control, Retrieval Augmented Generation, and command-line interfaces. We were very excited to explore many new tools in the software space and to persevere through the learning curves to deliver a high-quality final product. What's next for merj The future of merj falls into two different buckets. The first bucket focuses on scaling merj to work for many people across many different repositories and large codebases while reducing command latency. The second bucket of merj is potentially integrating a live component into the git mechanism. This will work as follows: One person will push their code, and every other member of the project will receive an update that someone has pushed code, allowing them to automatically merge the new commit into their current working directory with just a click of the button. <div