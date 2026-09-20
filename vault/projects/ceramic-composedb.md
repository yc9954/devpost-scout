---
slug: "ceramic-composedb"
url: "https://devpost.com/software/ceramic-composedb"
title: "Open Trust Claims"
hackathon: "EthCC Hack 2022"
organization: "EthCC"
winner: true
words: 421
team_size: 2
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/graph_reasoning"
  - "domain/developer_tools"
  - "domain/education"
  - "domain/media_journalism"
  - "user/developer"
  - "user/educator_student"
  - "substrate/structured_db"
---

# Open Trust Claims

> A visualisation tool for better journalism.

[Devpost](https://devpost.com/software/ceramic-composedb) · hackathon [[EthCC Hack 2022]]

## Facets

**mechanism** [[graph_reasoning]]
**domain** [[developer_tools]] [[education]] [[media_journalism]]
**user** [[developer]] [[educator_student]]
**substrate** [[structured_db]]

**stack** apollo-client, ceramic, graphql, js-composedb, material-ui, next.js

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for ceramic composedb

## Body

Page Where people will visualise and make further Claims Showing its draggable and easy to use Form to create claim Authenticating to composeDB Inspiration This product is specially for journalists, like a group of journalism students are investigating some news and finding out all connected stuff, and they want to show all these connection to whole world, so that people can find and investigate further on it. example: there is a murder case in a city xyz, some person will create a claim with subject: which will be heading of a topic, object: heading of the topic to which it is connected, relation: it'll define relation of his claim to main claim, proof: he'll add link of article or some data that can be used as proof for a claim. What it does People can visualise graph of all the connected claims for a particular topic to 2 or 3 depth, they can make other connected claims by clicking any existing claim on graph. User have to be authenticated to create claims. How we built it Next.js as frontend library, Material UI for UI components. We've used Cytoscape library to represent graph representation of claims on web browser. JS-composedb ceramic as graph database. Challenges we ran into At first it seems hard to understand, but when i tried to make a project using it, things starts getting clear, we just have to Run ceramic node --> Make a graphQL schema --> Create composite using cli command --> Deploy composite to ceramic Node --> Edit Ceramic daemon config file and add model id in indexing field there --> compile composite to use it in client side --> make a common apollo client util --> pass it apollo provider in parent component --> now we can query or mutate data in our application We've raised a Issue on Github for the challenges we've faced : https://github.com/ceramicstudio/js-composedb/issues/4 Accomplishments that we're proud of By suggesting changes and contributing in a Open source library that will help developers in various aspects, we hope it'll be most used library. What we learned We learned the vast opportunity available to make graph related applications with JS-ComposeDB, it'll surely saves a lot of time to implement application like many inbuilt function already there for authentication, signing, schema, storing data, etc What's next for Ceramic ComposeDB Our Prototype with mock data is ready but currently there are some issues while using graphql of compose db, so our next target is to integrate graphQL query to get and fetch claims. <div