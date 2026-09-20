---
slug: "peekmail"
url: "https://devpost.com/software/peekmail"
title: "Peekmail"
hackathon: "Hack for Humanity | 2025"
organization: "Kuba Apps"
winner: true
words: 146
team_size: 1
has_repo: true
has_live: false
has_video: false
tags:
  - "project"
  - "domain/developer_tools"
  - "user/developer"
---

# Peekmail

> Turn off email notifications and allow the peekmail utility to summarize any important emails for you instead of reviewing all incoming email and breaking your workflow.

[Devpost](https://devpost.com/software/peekmail) · hackathon [[Hack for Humanity - 2025]]

## Facets

**domain** [[developer_tools]]
**user** [[developer]]

**stack** openai, poplib, python

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for peekmail

## Body

Inspiration I'm easily distracted, and as a software developer, distractions break my flow and decrease my productivity. What it does Peekmail gathers your new emails and then uses an LLM to filter the emails to the most important ones and then summarize those. How we built it Written in Python, peekmail relies on Poplib (Post Office Protocol) to gather emails and then the OpenAI API to filter and summarize using a concise prompt. Challenges we ran into Email parsing is non-trivial, but Poplib helps to simplify this. Accomplishments that we're proud of I've used this utility for the last couple of day and found it useful to maintain my productivity. What we learned The OpenAI API is trivial to use for simple use-cases (as in peekmail) or in more complex use-cases. What's next for Peekmail Tailor for important email sources (boss, etc.), add iMAP support. <div