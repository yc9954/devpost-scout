---
slug: "porting-big-data-platform-on-graviton2"
url: "https://devpost.com/software/porting-big-data-platform-on-graviton2"
title: "Porting Big Data Platform on Graviton2"
hackathon: "AWS Graviton Hackathon"
organization: "Amazon"
winner: true
words: 460
team_size: 1
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "domain/climate_energy"
  - "domain/developer_tools"
  - "substrate/code_repository"
  - "substrate/video_visual"
---

# Porting Big Data Platform on Graviton2

> Big data project is famous for burning CPU. We should use it responsibly. Not only for the cost sake but also for the world sustainability. Safe for the company, country and the world.

[Devpost](https://devpost.com/software/porting-big-data-platform-on-graviton2) · hackathon [[AWS Graviton Hackathon]]

## Facets

**domain** [[climate_energy]] [[developer_tools]]
**substrate** [[code_repository]] [[video_visual]]

**stack** airbyte, bigdata, c++, java, jvm, particle, scala

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for porting big data platform on graviton2

## Body

graviton2 from indonesia with <3 Inspiration I'm inspired by sustainability movement recently and how the country struggling to save the world for our kids. Also company looks forward to achieve more with less especially with the cloud elasticity. Given this problem, i would love to bring big data entering low carbon footprint, cost effective and increasing the safeties of the company financial and world sustainability. What it does This project is aim to port a couple of majors data platform especially dremio (query engine) and airbyte (ingestion tools). This component is the cornerstone of data platform. We also porting Spark easily. How we built it We recompile all and replace the majors component that written in native language like c++ for apache arrow and upgrading JVM into the latest version for better ARM64 supports. We also upgrading docker images, rebuilt and patch a couple of codes on the open source libraries. Challenges we ran into The dependencies on big data platform is quite huge. And the versioning of the java library is not so good. Java 17 is moving towards module system. This will be a huge boost JVM 17 protect the access to unsafe and private method so it can't be used for old codes. This is force us to recompile the library and upgrade the graph dependencies and some tests needs to be fixed Lots of container doesn't support multi arch so we need to rebuild the docker images. Accomplishments that we're proud of We prove that porting to Graviton2 is worth pain and we quite confidence that we will use "Graviton2 First" approach for our next gen infrastructure. We managed to port native Apache Arrow C++ library, Gandiva, LLVM and flatbuffers that used in dremio We successfully bring the costs down and with less effort can port large big data platform We are proud that we made the right decision to choose managed language runtime like Java so it's easier to port to another CPU architecture What we learned We need to have robust end to end test for giving confidence Small incremental steps is necessary to tackle complex problem Need to watch out our library dependencies and upgrade as soon as possible so the platform is not lagging behind with the latest improvement in compiler, os, cpu architecture etc Need better ARM client, desktop and laptop for doing ARM development. There's not much available in the market. We are doing remote development with visual studio code remote ssh and that's quite limited and the experience is clunky. What's next for Porting Big Data Platform on Graviton2 We will do extensive load testing using TPC-DS testing tools for our big data platform Contribute back the patch and pull request to Airbyte and Dremio open source community <div