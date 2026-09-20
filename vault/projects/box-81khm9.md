---
slug: "box-81khm9"
url: "https://devpost.com/software/box-81khm9"
title: "box"
hackathon: "Go Hack"
organization: "Google"
winner: true
words: 534
team_size: 1
has_repo: true
has_live: false
has_video: false
tags:
  - "project"
  - "domain/developer_tools"
  - "domain/finance_payments"
  - "user/developer"
  - "user/general_public"
---

# box

> A container-first command runner

[Devpost](https://devpost.com/software/box-81khm9) · hackathon [[Go Hack]]

## Facets

**domain** [[developer_tools]] [[finance_payments]]
**user** [[developer]] [[general_public]]

**stack** docker, golang

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for box ?

## Body

Inspiration Box started with the need to run ANTLR (a CLI tool) written in Java. Java runtime is a heavy dependency to introduce in your development environment and one that I would seldom need. Docker provides excellent isolation capability, but what if your development environment is a container? Do I need to remember the docker CLI syntax in detail or create a shell script for running simple CLI commands? These questions inspired the creation of box - A simple container-first command runner. What it does box allows storing CLI commands and running them inside ephemeral containers. It automatically detects whether it is being invoked from inside a container and mounts the correct directory for sharing artifacts. With support for GPU acceleration, it is perfect for running one-off ML workflows. How we built it Our primary focus was creating a beautiful user experience and avoiding unnecessary complexity or bloat. Before jumping toward the code, we sketched possible ways users might want to use such a command-line runner and what the CLI should look like. Starting from just 3 simple commands (add, run and rm), Cobra allowed us to create a unified and structured way to manage how our CLI would be invoked. The logic of interacting with and managing containers is written with the help of Docker Go SDK. Once all the essential pieces were in place, we moved towards the quality-of-life features such as a command library and fetching remote commands. Challenges we ran into One of the challenges in developing with Docker Go SDK is the lack of proper documentation. While it extensively lists the available classes and methods, examples and explanations are scarce. We overcome this by trying commands out and comparing them against the Python SDK. A core challenge was making the tool host agnostic. Docker CLI and the SDK only accepts host path as mounting points. This makes running them inside a Docker-out-of-docker (DOOD) setup (the recommended way to access containers from inside a container as it only requires a single volume to be mounted) problematic. We created library functions to detect if box is invoked inside a container and find its host path through comparison against current mounts. We expect these functions to be helpful to fellow go developers. Accomplishments that we're proud of As a newcomer to golang, creating a well-functioning tool is something I am proud of. Go's simplicity and support of the ecosystem enabled us to accomplish the minimum viable product we had in mind when we started and to reach the majority of the stretch goals and nice-to-haves. What we learned We learned golang and interfacing with containers through Docker SDK. Beyond the technical skills, it allowed us to think from a general consumer-centric point of view and design our interfaces focusing on that (while solving the original problem we began this project with). What's next for box ? box follows the Unix philosophy of small, simple tools. It might be considered feature-complete unless users demand specific additions. However, a possible extension that I am very interested in is designing a proper terminal UI (through bubbletea) that would allow for command line interactivity (when providing arguments) and displaying additional information such as running time. <div