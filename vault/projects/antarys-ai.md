---
slug: "antarys-ai"
url: "https://devpost.com/software/antarys-ai"
title: "Antarys AI"
hackathon: "Frostbyte Hackathon"
organization: "FrostByte Club"
winner: true
words: 341
team_size: 1
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/retrieval_grounding"
  - "domain/retail_commerce"
  - "substrate/structured_db"
---

# Antarys AI

> A hackable vector db built on top of uSearch+rocksdb, for you to break it down, dissect and scale on demand

[Devpost](https://devpost.com/software/antarys-ai) · hackathon [[Frostbyte Hackathon]]

## Facets

**mechanism** [[retrieval_grounding]]
**domain** [[retail_commerce]]
**substrate** [[structured_db]]

**stack** c++, golang, rocksdb, zig

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned

## Body

Inspiration When I am building applications, it can be a rag application or a backend service and I need to embed a vector db directly in my project, I can use indexing libraries like faiss or hnswlib but what about scaling? what about generating embeddings and automatically expecting that a certain framework will handle memory optmization and load work, Antarys is a vector database as a framework which takes care of all of these. What it does It's a vector database to store, query and manage embedding indexes for semantic search but it lives in memory (+ disk persistence) for complete control. It uses a different async and RAM first architecture and can be directly invoked by projects. How we built it It's built using go and zig, the current version is written in go and there's a portable version written in zig, the go version has it's own HNSW engine built from the ground up and the zig uses Usearch for indexing. Challenges we ran into The startup, thankfully I ran into pebbledb from cockroach labs which solved this problem with the help of MVCC, the current variation which is more like a prototype uses JSON which will get replaced later down the line and the zig variation uses rocksdb! Accomplishments that we're proud of I managed to work with teams who implemented and used antarys's open source vector database like Dubotech which is an underwater drone company which used antarys to store their spatial data embeddings, UVTR used antarys for e-commerce products ( https://docs.antarys.ai/docs/impact/uvtr ) and open dimensions ( https://docs.antarys.ai/docs/impact/opendim ) used antarys for chat retrieval systems, had the luck to talk with Dane (CTO, cloudflare) for a possible partnership but it needs more work like IVF integration, more backup clauses etc etc. What we learned Building a vector database from the ground up is not easy, specially trying to chunk out every performance while sacrificing some quality, trying to maintain this golden ration of performance/quality is quite painful but can be improved as I get more experience! <div