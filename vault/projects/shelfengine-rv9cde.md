---
slug: "shelfengine-rv9cde"
url: "https://devpost.com/software/shelfengine-rv9cde"
title: "ShelfEngine"
hackathon: "Frostbyte Hackathon"
organization: "FrostByte Club"
winner: true
words: 130
team_size: 1
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/cross_origin_web"
  - "mechanism/retrieval_grounding"
  - "domain/labor_employment"
---

# ShelfEngine

> Local-first semantic search for your bookmarks: import once, find anything by natural language.

[Devpost](https://devpost.com/software/shelfengine-rv9cde) · hackathon [[Frostbyte Hackathon]]

## Facets

**mechanism** [[cross_origin_web]] [[retrieval_grounding]]
**domain** [[labor_employment]]

**stack** git, indexed-db, mini-search, react, typescript

## How they structured the write-up

- inspiration
- what it does
- why it’s different
- features
- built with

## Body

Inspiration My bookmarks turned into “I know I saved it somewhere” chaos. The problem wasn’t saving links. It was recall. What it does ShelfEngine is a local-first bookmark search engine that helps you find saved links even when you only vaguely remember them. Why it’s different Hybrid search: lexical + semantic ranking for messy, half-remembered queries Explainable results: shows why each link matched Fully local: no accounts, no backend, no data leaves your browser Features Plain language search or power operators ( site: , folder: , quotes, excludes, OR logic) IndexedDB storage with fast in-browser retrieval Optional Chrome extension bridge for bookmark sync Built with React, TypeScript, Vite, IndexedDB (Dexie), transformers.js in a Web Worker for non-blocking embeddings. Import once. Type what you remember. Get the right link. Fast. <div