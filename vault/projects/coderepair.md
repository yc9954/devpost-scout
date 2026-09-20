---
slug: "coderepair"
url: "https://devpost.com/software/coderepair"
title: "CodeRepair"
hackathon: "TreeHacks 2024"
organization: "TreeHacks"
winner: true
words: 670
team_size: 4
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

# CodeRepair

> Tool to automatically identify and fix bugs in codebases using GPT-4 to use debugger tools and automatically erase bugs. Scales to codebase of any size.

[Devpost](https://devpost.com/software/coderepair) · hackathon [[TreeHacks 2024]]

## Facets

**domain** [[developer_tools]] [[security_privacy]]
**user** [[developer]]
**substrate** [[code_repository]]

**stack** python

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for coderepair

## Body

Inspiration Many aspects of the programming workflow have been automated by the introduction of LLMs—especially with regard to code synthesis with products such as Github Copilot, AlphaCode and more. Other companies such as CodeGen and Sweep AI have begun tackling more niche subtasks, such as automatically solving tickets, conducting unit testing, catching security vulnerabilities, and more. However the complexity of coding tasks that can be solved with language models such as GPT4 is still very limited. Specifically, LLMs are used to scan and analyze codebases at a surface level to suggest code changes, identify errors, and fill code gaps. On the other hand, when humans debug code, they leverage tools such as GDB to inspect the state of a program’s internal variables and logic to garner a more complete picture of the root cause of the bug. We put these same developer tools in the hands of GPT4 to augment its current capacity for debugging code in hopes that it will be more capable in addressing runtime errors, algorithmic errors, and more. What it does CodeRepair identifies and fixes errors that cause runtime failures. Anything from segmentation faults and logic errors, to unit test failures and integration test failures… We allow GPT4 to conduct a far deeper analysis of the code’s behavior by giving it control over the GDB debugging tool. You think that’s it? We were also able to provide monitored access to shell commands so GPT can dynamically explore the codebase, circumventing its normal context length limitations. As far as we know, this is the FIRST application of LLMs where developer tools like GDB were provided to further beef up the robust model. How we built it We envisioned an agentic workflow where GPT4 can determine its own decisions while requesting for additional knowledge in the form of shell command and GDB command outputs from our program. More specifically, CodeRepair is based on Python and the OpenAI API, using the GPT4 Turbo model. Challenges we ran into Designing the backend architecture of the GPT agent proved to be a much larger challenge than any of us expected. We spent a significant portion of our time testing a solution that eventually appeared unnecessarily complicated and highly undoable in the time constraints. One of the largest challenges we ran into was scalability. This problem was twofold: How do we deal with really large codebases that would exceed GPT context length? Come watch our live demo to see this unfold! How do we deal with really large agent traces? We didn’t want the length of the [(action, output), (action, output), …] chain produced by a single agent to grow too large due to performs concerns. This was a large consideration for us while developing and motivated our original approach which was to create multiple subagents, all of which were instantiated and orchestrated by a single main agent. This approach proved to overcomplicate the task, as getting the orchestrating agent to perform well was very difficult. Accomplishments that we're proud of Watching GPT effectively use gdb and intelligently step through the code base was super cool and something that we are proud of. We are not aware of any other software that gives a language model that capability so it was definitely great to watch our program doing this. What we learned We learned the importance of providing GPT with deliberate instructions. One of the most difficult things was getting GPT to produce the output in a correct structure so that it could be reliably used by later parts of our program. One of the things we found is that in order to do this we really had to spoon feed to GPT exactly what it was and wasn’t allowed do. What's next for CodeRepair There is a lot in store for CodeRepair that we are super excited about. One particular thing we are really eager to work on next is to generalize our program to work for all languages rather than being bottlenecked by the debuggers available to us. https://github.com/jasondu7297/coderepair.ai <div