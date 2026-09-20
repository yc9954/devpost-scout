---
slug: "code-scaffolding-in-starport-with-ast-analysis-and-mutation"
url: "https://devpost.com/software/code-scaffolding-in-starport-with-ast-analysis-and-mutation"
title: "Code Scaffolding in Starport with AST Analysis and Mutation"
hackathon: "Cosmos HackAtom VI "
organization: "Cosmos"
winner: true
words: 499
team_size: 1
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "domain/finance_payments"
  - "substrate/code_repository"
  - "substrate/geospatial"
---

# Code Scaffolding in Starport with AST Analysis and Mutation

> To remove placeholders from Starport, replace all instances of placeholders by parsing, query, and mutate the AST to add new definitions

[Devpost](https://devpost.com/software/code-scaffolding-in-starport-with-ast-analysis-and-mutation) · hackathon [[Cosmos HackAtom VI]]

## Facets

**domain** [[finance_payments]]
**substrate** [[code_repository]] [[geospatial]]

**stack** golang

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for code scaffolding in starport with ast analysis and mutation

## Body

Inspiration Knowing how hard it can be to edit code in place, I chose to use two AST libraries written in golang to integrate into starport that allows walking an AST (analysis) and insert new AST nodes into the tree (mutation) What it does Instead of relying on a regular expression matcher, or specially worded comments, we manually walk the AST of a file, looking for functions that we wish to edit, then insert nodes into the tree before writing them back out to disk How we built it Wrapping the golang DST and protobuf proto libraries, I was able to construct AST builders to make working with each language's AST almost painless. Challenges we ran into As a team of one, there was only so much I could get done in the time allotted. Additionally, a large amount of pre-existing code is only slightly different from other "typed" templates, and replacing them all would have been long and tedious at first until a final solution with ease of use was divised. Additionally it's been difficult to strike a balance between "expert level code" and "something anyone can pick up and use right away" There was also the issue of naming conventions and code generation changing in the base starport repository, even up until a few days before the competition ended. At some point I had to make a decision to stop rebasing on top of upstream. Lastly, there is not silver bullet parsing, querying, and modifying library for golang and protobuf. Accomplishments that we're proud of Building the AST nodes in a quick and concise manner with a nearly WYSIWYG approach to the code (when using the golang AST API is much more prone to errors, and there is no builtin way to do this in protobuf) was very great to have working, especially when it worked for the first time. The approach this project takes can be reused everywhere in starport, but could also be used for general project scaffolding and could possibly even lead to a replacement for an API like yeoman , a generic javascript based code scaffolding tool What we learned The current way of editing templates with placeholders is easier to see at a glance, however it breaks if someone removes comments from a generated file. With the AST approach, only the expected functions have to exist. What's next for Code Scaffolding in Starport with AST Analysis and Mutation In addition to helping replace the rest of the AST nodes in scaffold map, singleton, etc. I would like to break out the gocode and protocode packages into a library, as well as fork the two main packages I relied on, integrate them into said library, and also write a way to allow quickly walking and finding items in an AST by using CSS selector style syntax. (NOTE: While there are several libraries that work on the builtin golang compiler's AST library, none of them work on the DST library, which preserves comments) <div