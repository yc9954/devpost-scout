---
slug: "alon"
url: "https://devpost.com/software/alon"
title: "Alon"
hackathon: "IGNITION | A Global Solana Hackathon"
organization: "Solana Capital"
winner: true
words: 686
team_size: 2
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "domain/developer_tools"
  - "domain/finance_payments"
  - "domain/labor_employment"
  - "user/developer"
  - "substrate/code_repository"
---

# Alon

> Remix for Solana. Alon enables developers to rapidly build, test, iterate and deploy Solana-powered decentralized applications and assets straight from their browser.

[Devpost](https://devpost.com/software/alon) · hackathon [[IGNITION - A Global Solana Hackathon]]

## Facets

**domain** [[developer_tools]] [[finance_payments]] [[labor_employment]]
**user** [[developer]]
**substrate** [[code_repository]]

**stack** c, emscripten, llvm, monaco, react, solana, tailwind, treesitter

## How they structured the write-up

- inspiration
- what it does
- how we built it
- what's next for alon

## Body

Inspiration So first, let’s be real: it’s not easy to get started building Solana programs. There’s a huge barrier to entry right from the very beginning, which is that Solana’s developer tooling only really works on macOS, alongside a very small handful of Linux distros. So if you’re part of the 60 to 70% of developers out there that use Windows or some variant of Linux that is NOT Ubuntu, you’re out of luck. And this is a very real issue: For my friends that recently took up positions to develop Solana programs, some of them took a day, some took a week, and others even bought a whole new laptop just to get a Solana developer environment set up and working. This was the inspiration to me and my friend Matt, who works with BPF professionally. The inspiration that led us to spend the hackathon making Solana’s developer tooling more accessible by picking apart and porting Solana’s entire compiler suite into one of the most portable assembly languages out there: WebAssembly. And least to say, our efforts have been a resounding success, which is what led us to build Alon. What it does Alon is essentially a better Remix for Solana. Alon is an IDE empowered by a WebAssembly port of Solana's compiler suite which allows developers to rapidly build, iterate, test, and deploy decentralized apps and assets on Solana right from their browser. By writing a very thin compiler and linker frontend on top of a WebAssembly port of Solana’s compiler suite, and by writing a barebones JavaScript port of Solana’s program virtual machine syscalls, Alon is able to cut down the time it takes to compile, run, and test Solana programs down to a few hundred milliseconds. As a matter of fact, compiling a Solana program on Alon is so fast that we even added an option to have Alon automatically compile and run tests every time you make edits to your code. The code editor for Alon comes with Treesitter integrated, which allows for Alon to incrementally build and update an entire syntax tree of your Solana programs in under a millisecond. Integrating Treesitter into Alon's code editor allows for the development of all new kinds of static analysis tools that may help significantly simplify and speed up the development of reliable Solana programs. Examples of static analysis tools enabled by Alon includes: automatic TypeScript client generation for your Solana programs, automatic serialization/deserialization code generation, and automatic instruction/error union code generation. So connect your Solana wallet, create or mint tokens and NFTs, airdrop yourself some SOL, deploy/upgrade your programs, and do so much more - take advantage of the full suite of features provided by Alon. How we built it We tackled porting Solana's patched LLVM compiler backend and BPF tooling to WebAssembly by using both Docker and Emscripten. Given the large amount of dependencies and syscalls which LLVM relies on, we also wrote and cross-compiled a very thin clang/lld frontend in C++ instead of cross-compiling the official clang/lld frontend that comes with LLVM. We then created our WebAssembly-based test runner by implementing as many relevant Solana program syscalls as we could by reading the source code of Solana. We then combined everything together using React and Tailwind and Solana's Web3.js, and based Alon's code editor on top of Monaco Editor. Given that Monaco Editor is very flexible, and given the compilation speeds we realized with our WebAssembly port of Solana's patched LLVM compiler suite, we also then decided to integrate Treesitter into Alon's code editor to allow for the development of static analysis tools on top of Solana programs. What's next for Alon Better code/file navigation Keyboard navigation/shortcuts Treesitter-based code completion Port the clangd language server to WebAssembly Support other languages such as Zig, Rust, and Solang Completion of the UI for all of the static analysis tooling Port all remaining subcommands of the Solana CLI to Alon's UI Standalone executable to integrate Alon into your favorite editors Deploy/upgrade programs on the UI using the Upgradeable BPF Loader Program Port all remaining Solana program syscalls to Alon's WebAssembly-based test runner <div