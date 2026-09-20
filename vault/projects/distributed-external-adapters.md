---
slug: "distributed-external-adapters"
url: "https://devpost.com/software/distributed-external-adapters"
title: "Hive"
hackathon: "Chainlink Spring 2023 Hackathon"
organization: "Chainlink Labs"
winner: true
words: 506
team_size: 1
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/structural_withholding"
  - "domain/developer_tools"
  - "user/developer"
  - "substrate/financial_record"
---

# Hive

> We want to build true External Adapters for Chainlink. It should be able to run in different environments, including browsers and native environments.

[Devpost](https://devpost.com/software/distributed-external-adapters) · hackathon [[Chainlink Spring 2023 Hackathon]]

## Facets

**mechanism** [[structural_withholding]]
**domain** [[developer_tools]]
**user** [[developer]]
**substrate** [[financial_record]]

**stack** rings, rust, wasm, wat

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for hive

## Body

Inspiration We want to build true External Adapters for Chainlink. It should be able to run in different environments, including browsers and native environments. What it does So we have built a new type of external adapter that is more decentralized because it supports compiling external adapter logic to WebAssembly (wasm). As you may know, wasm is a binary format that is easily distributable and runs on any platform, especially in web browsers. This enables us to achieve something: tasks can be issued by a Chainlink Node or Oracle and answered by adapters distributed across numerous nodes, which may be running in web browsers.These tasks can range from conducting surveys, initiating transactions, or virtually anything you can imagine. How we built it We compile the external adapter to WebAssembly (wasm) and define a specification for it to be better interpreted. The specification states that it should have a handler of type Fn ExternRef -> ExternRef. Additionally, we utilize the purely peer-to-peer Rings network to read and distribute the wasm handler. To meet the requirements of the external adapter, we have implemented an extension feature specifically for the Rings network. This enables the network to accept messages from Chainlink nodes and forward them to the external adapter. A simple adapter would look like this. It is a .wat file, which is a human-readable format for WebAssembly (wasm). You can compile it using any programming language. (module ;; Define a memory that is one page size (64kb) (memory (export "memory") 1) ;; fn handler(param: ExternRef) -> ExternRef (func $handler (param externref) (result externref) (local.get 0) return ) (export "handler" (func $handler)) ) Challenges we ran into Managing wasm memory and handling the wasm importObject can be the most significant challenges we face. The memory model of wasm_bindgen is very complex. Accomplishments that we're proud of For this hackathon, we have made some changes to our plans. Initially, we intended to decentralize the oracle gateway using Rings Network's browser native P2P capabilities. However, we felt that this approach might not be cool enough. Therefore, we came up with a more fundamental approach: decentralizing Chainlink's external adapters, allowing anyone to become an external adapter. This could potentially bring about even more exciting possibilities, such as a task platform (Link3/Layer3) based on Chainlink or an advertising delivery platform, and so on. What we learned The potential of the WebAssembly (wasm) ecosystem is indeed tremendous. It has the capability to support various functionalities such as networking, zero-knowledge proofs (zkp), and more. Throughout this development process, we have recognized the immense potential of wasm. However, we also acknowledge that the high development barrier and the fragile nature of the ecosystem are challenges that we have learned from. What's next for Hive We have now completed the compilation from Wat to message adapter, but currently, it only supports the Rust language. We plan to provide more examples and expand language support in the future. This will make it more user-friendly and versatile, allowing developers to utilize different programming languages for their External Adapters. <div