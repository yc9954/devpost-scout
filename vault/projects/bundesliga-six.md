---
slug: "bundesliga-six"
url: "https://devpost.com/software/bundesliga-six"
title: "Bundesliga Six"
hackathon: "AWS Graviton Hackathon"
organization: "Amazon"
winner: true
words: 679
team_size: 2
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "substrate/video_visual"
---

# Bundesliga Six

> Migrating a soccer prediction game to ARM64

[Devpost](https://devpost.com/software/bundesliga-six) · hackathon [[AWS Graviton Hackathon]]

## Facets

  <sub>weak: developer_tools</sub>
**substrate** [[video_visual]]

**stack** adoptium-openjdk, alertmanager, aws-sdk-java2, consul, drone, fedora-coreos, gitea, grafana, idea, loki, maven, mongodb, nats, nomad

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for bundesliga six
- about us

## Body

Current Round Automation - Coreship Multi-Architecture Build Inspiration We were always looking to be able to run our entire tech stack on ARM architecture because we wanted to show-case how light weight and lean our applications are built so they could even run on Raspberry PI boards. The last missing piece to that goal was to have Fedora CoreOS builds as all the other components did already support ARM. It was a lucky coincidence that the Graviton 2 instance types were already available, so we could easily use our existing tools to play around. As we always look for a low footprint we did as well like the environmental aspect of lower power consumption of this CPU architecture. The price benefit is definitely as well a factor why we would switch our entire workload from development to production on ARM powered instances. What it does As a company we develop and run a lot of projects and services but for this particular hackathon we decided to choose an application were it makes the most sense to highlight the benefits of migrating to a different architecture. It's basically a soccer prediction game based on a microservice platform that powers as well our licensed iGaming products. It does not only support user activities were it can handle several thousand of requests per second but also result calculation were millions of predictions get evaluated. How we built it The microservices are built on a Vert.x / Java 17 stack, scheduled and deployed as container images via Nomad on Fedora CoreOS hosts. Service discovery and configuration is done via Consul . The frontend is built on React using Typescript bootstrapped via our Vert.x based integration layers which are responsible for frontend optimized APIs and user session handling. Most container images we use are supporting multiple architectures, for the rest we created open-source repositories with automated multi-architecture builds. Open-source containers are automated with github actions. (e.g. nomad ) Internal service builds are done with drone. Pipelines run in parallel on aarch64 and amd64 build agents. Challenges we ran into Resource reservation for the Nomad scheduling algorithm did not work out of the box. We identified, that the host fingerprinting was not able to discover the clock speed and did fallback to 1GHz so we had to adapt our deployment workflows accordingly. This behavior can be easily tested with comparing lscpu on an amd64 and aarch64 linux host. Another challenge was making it easy and transparent for our development teams to use different architectures via our internal automation. There we mapped aws instance types to architectures and used them to discover the latest AMIs for our initial Fedora CoreOS bootstrap when we create new stacks. The architecture for the container workload is then automatically chosen based on the host one. On the vert.x dependency project we had to file a PR to get the native epoll netty transport version supported but this was more of a cosmetic bugfix. Accomplishments that we're proud of Our automation did nearly work out of the box, so we are proud that we could built it in a way to support future shifts in the IT sector. We built as well a custom bot framework to (load-)test full setups. This came really handy in running tests against different instance/stack types and architectures in nearly no time, so we could compare all the graphs from system up to the service level. What we learned We were really impressed with the performance and what's already possible on these Graviton 2 instances. It feels a bit as this journey is not over yet. The next big thing could be Risc-V architectures... What's next for Bundesliga Six We hope there will be many more German Bundesliga seasons to come. Maybe we will migrate to other leagues or sports in the future but it will be definitely a blue-print for all our other more critical setups. About us 5G Systems If you like our project and want to get in contact with the team, feel free to write us or visit us in Vienna. <div