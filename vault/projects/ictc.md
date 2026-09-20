---
slug: "ictc"
url: "https://devpost.com/software/ictc"
title: "ICTC"
hackathon: "Supernova "
organization: "DFINITY Foundation"
winner: true
words: 401
team_size: 3
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "domain/developer_tools"
  - "user/developer"
  - "substrate/financial_record"
---

# ICTC

> A distributed transaction framework for Defi applications on IC network

[Devpost](https://devpost.com/software/ictc) · hackathon [[Supernova]]

## Facets

**domain** [[developer_tools]]
**user** [[developer]]
**substrate** [[financial_record]]

**stack** motoko

## How they structured the write-up

- inspiration
- what it does
- how we built it
- transaction manager
- task actuator
- transaction compensator
- example
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for ic transaction coordinator（ictc）

## Body

logo Inspiration Motoko developers need a development framework that addresses the issue of atomicity in order to lower the development threshold. The core idea of ICTC is inspired by the DTC (Distributed Transaction Coordinator), which is commonly used in the financial sector. What it does ICTC is a distributed transaction framework for Defi applications on IC network. It supports Motoko language. How we built it ICTC consists of Transaction Manager (TM), Task Actuator (TA), and Transaction Compensator (TC). Transaction Order: A transaction, including one or more transaction tasks, that requires all tasks to be either fully successful or fully rejected. Transaction Task: A task within a transaction, including local tasks of the caller and remote tasks of other parties involved. Transaction Manager The Transaction Manager is used to manage the status of transactions, operate the Actuator, handle exceptions and call the Compensator. Transaction Manager implementation includes the Saga Transaction Manager (SagaTM) and the 2PC Transaction Manager (TPCTM). Task Actuator The Task Actuator uses a "best-effort delivery" policy and will definitely return a result (success/failure). Synchronous actuator and asynchronous actuator are supported. Transaction Compensator The Transaction Compensator function is implemented in Transaction Manager and is used to execute compensation operations when an exception occurs in a transaction, including automatic compensation, governance or manual compensation. Example Challenges we ran into Motoko does not support polymorphism, and also does not support reflection. So this posed some challenges to our development process and we had to spend some time and effort doing some underlying packaging. Fortunately, we solved all these problems. Accomplishments that we're proud of An Alpha version of ICTC has now been developed to support Saga mode, with support for Forward and Backward modes. The basic needs of Defi development can be met. DeSwap (OrderBook Dex), ICSwap (AMM Dex) are currently using ICTC. What we learned IC does not support atomicity for cross-canister calls, but improves scalability and performance, which opens up more possibilities for Defi. What's next for IC Transaction Coordinator（ICTC） Next we plan to make ICTC support 2PC mode and encapsulate it in vessel to make it easy for developers to use. And then ICTC Framework V1.0 and technical documentation will be completed. Our technical staff will be reaching out to the community to introduce the framework, giving technical talks and code demos. We will also seek the cooperation of the official Dfinity operations staff to promote the motoko technology <div