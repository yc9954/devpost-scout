---
slug: "ivf"
url: "https://devpost.com/software/ivf"
title: "iVF"
hackathon: "Build Resilient Apps with Polkadot Cloud"
organization: "POLKADOT"
winner: true
words: 569
team_size: 2
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/structural_withholding"
  - "domain/developer_tools"
  - "domain/health_clinical"
  - "user/developer"
  - "substrate/code_repository"
  - "substrate/financial_record"
  - "substrate/geospatial"
  - "substrate/transcript_audio"
---

# iVF

> Automated generation of ink! v6 smart contract verifiers from Noir zero-knowledge proof circuits for PolkaVM.

[Devpost](https://devpost.com/software/ivf) · hackathon [[Build Resilient Apps with Polkadot Cloud]]

## Facets

**mechanism** [[structural_withholding]]
**domain** [[developer_tools]] [[health_clinical]]
**user** [[developer]]
**substrate** [[code_repository]] [[financial_record]] [[geospatial]] [[transcript_audio]]

**stack** bn128, ink!, noir, rust

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for ivf

## Body

Pallet-Revive brought ZKPs to Polkadot. iVF makes them native. Inspiration While Pallet-Revive's support for Solidity verifiers opened the door to Zero Knowledge Proofs, we recognized that the Polkadot ecosystem deserves native solutions that leverage its unique advantages; particularly PolkaVM's RISC-V architecture and ink!'s Rust foundations. What it does iVF (ink! Verifier Factory) is a code generation tool that transforms Noir zero-knowledge circuit verification keys into production-ready ink! v6 smart contracts. It automates the entire process: Parses Noir VK files to extract circuit specifications and verification parameters Generates complete ink! contracts with all necessary elliptic curve operations (BN128 pairing, point arithmetic) Integrates Pallet-Revive precompiles for optimal gas efficiency Implements the Plonk verification algorithm natively in Rust Provides comprehensive error handling with detailed diagnostic messages The result is a verifier contract that achieves ~25% gas savings, 45% smaller binary size, and full Rust type safety compared to Solidity alternatives; all while being completely self-contained and requiring zero external dependencies once deployed. How we built it The project is a Rust-based code generator with several key components: Binary VK Parser : Built a low-level parser that reads Noir's verification key format, extracting metadata (circuit size, public input count) and G1 curve points as 32-byte field elements in big-endian format. Code Generation Engine : Developed a template system that produces complete ink! v6 contracts with native BN254 field arithmetic, elliptic curve operations, and the full UltraHonk verification algorithm (Fiat-Shamir transcript, sumcheck verification, KZG opening checks). Precompile Integration : Leveraged Pallet-Revive's BN128 precompiles (bn128add, bn128mul, bn128pairing) for optimal gas efficiency, handling data marshalling between ink!'s type system and precompile binary interfaces. Build Pipeline : Configured generated contracts to compile for PolkaVM's riscv64emac-unknown-none-polkavm target using cargo-contract v6, with optimized build profiles for minimal binary size. The architecture follows a clean pipeline: VK file → Parser → Generator → ink! contract → PolkaVM binary → On-chain deployment. Challenges we ran into Precompile Integration : Mapping Pallet-Revive's BN128 precompiles to ink!'s interface required careful attention to data encoding and error handling. The precompile APIs are EVM-derived but needed to work seamlessly in a RISC-V context. Field Arithmetic Precision : Implementing BN128 field operations in native Rust while maintaining mathematical correctness and avoiding overflow was intricate. We had to balance precision with performance across 254-bit scalar operations. Variable Circuit Support : Making the generator truly circuit-agnostic meant handling edge cases in VK structures, different numbers of public inputs, varying commitment sizes, and diverse polynomial degrees, all needed robust handling. Accomplishments that we're proud of True One-Command Simplicity : We succeeded in making ZKP verification on Polkadot genuinely accessible; from Noir circuit to deployed verifier in a single command. Circuit Agnosticism : Successfully supporting circuits of vastly different complexities (57-128 field elements) without requiring manual tuning demonstrates robust generalisation. What we learned Type Safety is a Superpower : Rust's compile-time guarantees caught numerous subtle bugs in field arithmetic and proof handling that would have been runtime failures in Solidity. Precompiles are Game-Changers : Pallet-Revive's BN128 precompiles are incredibly powerful when used correctly. They're the key to making on-chain verification economically viable. What's next for iVF Batch Verification : Implement optimised batch verification for scenarios requiring multiple proof checks in a single transaction. Developer Tooling : Create cargo plugins, IDE integrations, and debugging tools specifically for ZK contract development. Barretenberg Backend Support : Integrate native Barretenberg (bb) CLI support, allowing developers to generate ink! verifiers directly using bb commands <div