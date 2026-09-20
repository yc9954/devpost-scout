---
slug: "ast-walking-around-starport"
url: "https://devpost.com/software/ast-walking-around-starport"
title: "(AST)Walking around starport"
hackathon: "Cosmos HackAtom VI "
organization: "Cosmos"
winner: true
words: 604
team_size: 1
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "domain/developer_tools"
  - "domain/finance_payments"
  - "substrate/code_repository"
---

# (AST)Walking around starport

> Eliminate the need for placeholders throughout the code by manipulating Abstract Syntax Trees.

[Devpost](https://devpost.com/software/ast-walking-around-starport) · hackathon [[Cosmos HackAtom VI]]

## Facets

**domain** [[developer_tools]] [[finance_payments]]
**substrate** [[code_repository]]

**stack** abstract-syntax-trees, go, protobuf

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for (ast)walking around starport

## Body

Inspiration I wanted to further understand the cosmos ecosystem. Starting with starport, which is the first step in the process of creating a new blockchain, seemed like the perfect first step. What it does It builds ASTs for both the protobuf language files and the go files and manipulates them in order to insert the elements as required. One can either create completely new nodes and insert them in specific positions relative to other elements or mutate currently existing nodes as required. How we built it Protocol buffers For the protocol buffer language, support for parsing is available with emicklei/proto and is currently already used in starport (for the protopackages package). Since the protocol buffer language is small and simple, the project creates an abstraction package over it that allows creation of nodes via a higher-level API. In addition to that, functionality similar to astutil is implemented (in the form of a Cursor and Apply ) in order to allow precise manipulation of positioning and early exit from the tree traversal (things not offered by the proto packages Walk functionality). Currently protofmt is used in order to output the AST back into source file. Since this is relatively opinionated, though, a different formater is currently written and being tested that can be tailored to have as little opinions as possible. A new package, protoutil , has been created inside the pkg/protoanalysis folder. Golang For go, most of the tools are readily available. Go's built in ast / parser / astutil give you everything you need in order to manipulate go elements. This includes parsing, manipulation and outputting of ASTs back to source files via printer.Fprint . Due to some shortcomings (bad support for comment parsing) of the ast package, though, Decorated Syntax Trees are used which provide the same set of tools. Since the language is generally large and more complex than protocol buffers, creating new nodes on the fly is not available via a more explicit high level package. Instead, strings are directly supplied to the parser which is tasked with creating new nodes. Helper/utility functions have been added directly in the goanalysis package. Challenges we ran into The first challenge was understanding the project, how it operates, how to test it and how to augment it. The more I worked on it, the more clear things became. The second main challenge involved understanding the Cursor objects as provided for astutil/dstutil and how to translate that over to protocol buffers. After panicking many times with reflect , I believe I've got a solid understanding of how it operates. Accomplishments that we're proud of I personally liked how the wrapping of the ASTs in the proto package was done. It made it easy to create new nodes and mutate files. What we learned Mainly two things: The codebase of starport and how it works The structure of go/protobuf source files and the way in which to manipulate them. What's next for (AST)Walking around starport A couple of improvements/enhancements I can think off: Refactoring! There's a number of places where common code is used, these can be further consilidated in smaller utility functions that are shared. What to do when certain elements don't exist. For example, if a const () doesn't exist in certain files, the code doesn't currently try and create one. It could easily do this instead of failing. The creation of go nodes could be more structured (instead of creating them from strings). All in all, I believe this generally just requires another iteration of refactoring to get it to a much cleaner state. See the project's README.md for additional notes! <div