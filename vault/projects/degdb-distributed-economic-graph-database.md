---
slug: "degdb-distributed-economic-graph-database"
url: "https://devpost.com/software/degdb-distributed-economic-graph-database"
title: "degDB (Distributed Economic Graph Database)"
hackathon: "PennApps XII"
winner: true
words: 350
team_size: 3
has_repo: false
has_live: true
has_video: false
tags:
  - "project"
  - "mechanism/graph_reasoning"
  - "mechanism/provenance_signing"
  - "substrate/financial_record"
  - "substrate/structured_db"
---

# degDB (Distributed Economic Graph Database)

> An actual web scale distributed database that encourages people to contribute through compensation.

[Devpost](https://devpost.com/software/degdb-distributed-economic-graph-database) · hackathon [[PennApps XII]]

## Facets

**mechanism** [[graph_reasoning]] [[provenance_signing]]
**substrate** [[financial_record]] [[structured_db]]

**stack** freebase, go, gossip, linode, node.js

## How they structured the write-up

- why? problems with existing graph databases
- how to solve
- implementation
- what's next?

## Body

degdb - Distributed Economic Graph Database An actual web scale distributed database that rewards people financially for making high quality data submissions to the graph and hosting servers. Design Doc/Ramble Why? Problems With Existing Graph Databases Owned by private companies with no incentive to share. Public databases are used by few people with no incentive to contribute. Large databases can’t fit on one machine and are expensive to traverse. Existing distributed graph databases require all nodes to be trusted. How To Solve Tying bitcoin directly to the knowledge graph instead of running the billing as a separate service like existing knowledge graphs actively encourages the community to contribute. If people have spare disk space or server capacity they can earn money with their space cycles, and content creators are actively rewarded for contributing high quality useful data. The graph database cryptographically signs every "triple" allowing for some percentage of the transaction fee to be transferred to the original creator. This encourages existing groups such as Wiki Media, or Music Brainz to integrate their data to the graph as they have a large quantity of structured data. One of the hardest problems with traditional graph databases is doing "reconciliation" or combining multiple data sources. By having contributors to the graph being directly paid by how useful their contributions are ensures that the data will be well integrated and easy to use. Implementation DegDB uses a modified version of the Gossip protocol to easily be able to detect new nodes and communicate between them. This easy to join system allow for our server management tool that can easily launch Linode instances. The core service is written with Go and prefilled with data borrowed from Freebase.com for demonstration purposes. What's next? Before DegDB becomes a production service there's a lot of polish that needs to be applied. This involves quite a bit of work hardening the protocol and adding anti-abuse algorithms to stop malicious users. Expanding the number of query languages will also help drive users as supporting the top 2-3 languages will make it very easy for existing databases to integrate. <div