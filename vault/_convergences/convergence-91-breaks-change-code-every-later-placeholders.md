---
tags:
  - "convergence"
projects: 3
hackathons: 2
---

# 3 projects, 2 hackathons, one claim

**Shared vocabulary** breaks, change, code, every, later, placeholders

### [[sankofa-mcq8af]] — Sankofa
> a reviewer approves a change because the diff looks fine, and two days later something breaks that had callers nobody knew about, which is an information failure rather than a process one

*GitLab Transcend Hackathon* · problem: the artifact under review shows the change and not what depends on it

### [[ast-walking-around-starport]] — (AST)Walking around starport
> scaffolding tools generate code with placeholders that every later change has to find and update, so the template's convenience becomes the project's maintenance burden

*Cosmos HackAtom VI * · problem: blockchain scaffolding relies on placeholder strings throughout the generated code

### [[code-scaffolding-in-starport-with-ast-analysis-and-mutation]] — Code Scaffolding in Starport with AST Analysis and Mutation
> generated code is edited by text substitution into placeholders, so every later change is string manipulation on a structured artifact and breaks unpredictably

*Cosmos HackAtom VI * · problem: scaffolding relies on placeholder markers throughout the generated code
