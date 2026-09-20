---
slug: "go-hep-goldb-contributions"
url: "https://devpost.com/software/go-hep-goldb-contributions"
title: "go-hep + goldb contributions"
hackathon: "Go Hack"
organization: "Google"
winner: true
words: 242
team_size: 1
has_repo: true
has_live: false
has_video: false
tags:
  - "project"
  - "domain/developer_tools"
  - "user/developer"
  - "substrate/code_repository"
---

# go-hep + goldb contributions

> Improve maitainability of go-hep and goldb projects.

[Devpost](https://devpost.com/software/go-hep-goldb-contributions) · hackathon [[Go Hack]]

## Facets

**domain** [[developer_tools]]
**user** [[developer]]
**substrate** [[code_repository]]

**stack** github-actions, go, golangci-lint

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for go-hep + goldb contributions

## Body

Inspiration I wanted to contribute to science. What it does Improve code quality to ease access to CERN projects for other external contributors. How we built it go build ./... Challenges we ran into The testsuite of the goldb project was not working. One contributor had submitted a fix but it had not been reviewed before I called the maintainers. I have implemented CI based on GitHub Actions, but the goldb testsuite doesn't pass on Windows. The code in the goldb project is not idiomatic. Cleanup was (and is still) necessary before contributing significant features. I started implementing CI on GitHub Actions for go-hep, but so far the CI fails and I haven't finished the work. There was too much low hanging fruits (minor contributions) to submit before doing advanced Go contributions such as Go using generics. I had to wait for review and merge of such contributions before. The contributor process of the go-hep project (pull request required on the hep-license project) was unusual and unexpected: it wasn't mentioned on the Go Hack rules site. Accomplishments that we're proud of go-hep: 6 pull requests merged. More to come. goldb: 2 contributions appied/merged. 2 pending. What we learned CI GitHub Actions. Running golangci-lint on GitHub Actions. Discovering the HEP context was interesting. Scientific code is a good change from daily business code! What's next for go-hep + goldb contributions More contributions to come on GitHub Actions and goldb test suite fixes. <div