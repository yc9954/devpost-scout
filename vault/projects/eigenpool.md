---
slug: "eigenpool"
url: "https://devpost.com/software/eigenpool"
title: "EigenPool"
hackathon: "QuantumHacks"
organization: "Quantumhacks"
winner: true
words: 816
team_size: 1
has_repo: false
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/deterministic_policy"
  - "mechanism/realtime_stream"
  - "substrate/financial_record"
  - "substrate/geospatial"
  - "substrate/sensor_telemetry"
---

# EigenPool

> A quantum game-theoretic clearinghouse rendering market front-running mathematically irrational.

[Devpost](https://devpost.com/software/eigenpool) · hackathon [[QuantumHacks]]

## Facets

**mechanism** [[deterministic_policy]] [[realtime_stream]]
**substrate** [[financial_record]] [[geospatial]] [[sensor_telemetry]]
  <sub>weak: code_repository</sub>

**stack** algorithms, axum, financial-engineering, fintech, game-theory, high-frequency-trading, mathematics, next.js, physics, python, quantum-computing, react, rust, tailwindcss

## Body

Homepage Inspiration If you have ever provided liquidity or executed a sizable order in modern financial markets, you know a very specific kind of frustration.You spend hours analyzing an asset, structure a clean trade, and hit execute—only to watch a high-frequency algorithm spot your intent in the precise microseconds before inclusion, step directly in front of your transaction, and extract the margin. It feels like playing a card game where the dealer is quietly showing your hand to the player across the table.It sounds like a corrupt system. But the uncomfortable truth is that the system isn’t broken—it’s performing exactly as designed.Classically, transaction routing is structured as a non-cooperative Prisoner's Dilemma. Because classical order books leak intent the moment an order hits the wire, predatory actors (MEV bots and front-runners) have a dominant strategy: Defect. When defection guarantees risk-free profit, telling traders to "play fair" is useless.We realized that to stop predatory execution, we shouldn't try to regulate behavior through rules or slow down the wire with arbitrary latency penalties. Instead, we needed to change the underlying physics of the order book itself.The Core Realization: You cannot appeal to the ethics of an adversarial market actor. But you can change the mathematical space of the game so that bad behavior yields strictly zero return.How We Built ItEigenPool replaces the classical limit order book with a quantum game-theoretic clearinghouse. Instead of processing discrete scalar bids and asks, EigenPool maps order intents into a $4$-dimensional Hilbert space using the Eisert-Wilkens-Lewenstein (EWL) quantum game protocol.1. The Physics & Game TheoryWhen two market actors (e.g., a liquidity provider and an incoming order) enter the matching engine, their strategies are entangled via a initial unitary operator:$$J = \exp\left(i \frac{\gamma}{2} \sigma_x \otimes \sigma_x\right)$$Where:$\sigma_x$ represents the Pauli-X operator (bit flip / classical defection strategy).$\gamma \in \left[0, \frac{\pi}{2}\right]$ measures the degree of computational entanglement in the clearing process.In a classical market ($\gamma = 0$), front-running ($D$) against an honest liquidity provider ($C$) yields an asymmetric payoff matrix where the attacker wins $5.0$ units and the provider loses everything ($0.0$).When we dial the entanglement factor to maximum ($\gamma = \frac{\pi}{2}$), the execution state operates under full quantum superposition. The orders literally do not resolve into classical state values until the exact microsecond of batch execution.If an attacker attempts a classical front-running strategy against an entangled order, the strategy operator breaks the state symmetry, collapsing the wave function into an unproductive subspace. The expected payoff for the attacker drops instantly to $0.0$.This enforces a new Quantum Nash Equilibrium ($Q, Q$), where providing honest liquidity yields the maximum sustainable payoff ($3.0 / 3.0$), rendering front-running mathematically irrational.2. High-Frequency Rust Core (/backend)To build an engine capable of handling real-world order flow without latency penalties, we built the matching pipeline in raw, zero-abstraction Rust:Zero Heap Allocation: Matrix transformations and tensor Kronecker products are computed strictly using fixed-size stack arrays ([Complex64; 4]).SIMD Auto-Vectorization: All unitary matrix multiplications ($\hat{U}_A \otimes \hat{U}_B$) are structured with deterministic bounds, allowing the compiler to unroll loops and leverage AVX-512 hardware registers.Async Streaming: An Axum & Tokio WebSocket pipeline broadcasts wave-function collapse events to connected terminals at sub-millisecond tick intervals.3. Institutional Terminal (/frontend)The frontend is built with Next.js (App Router) and Tailwind CSS. It ingests the live WebSocket stream from the Rust core, updating an execution tape and dynamically mapping real-time payoffs onto a $2 \times 2$ payoff matrix grid.Challenges We FacedEliminating Matrix Multiplication Latency: Simulating quantum operations usually involves heavy linear algebra libraries like LAPACK or Eigen, which introduce heap allocations and dynamic memory overhead. In a high-frequency context, heap allocation is death. We had to hand-roll the 4x4 matrix tensor multiplication routines using fixed-size stack arrays to ensure the hot path remained deterministic.Preventing Precision Leakage: Floating-point rounding errors during unitary transformations can cause the total probability distribution to drift from $1.0$ ($\sum \vert{}\psi_i\vert{}^2 \neq 1.0$). We had to strictly track the imaginary components using num-complex to guarantee exact mathematical state collapse.Translating Quantum Abstract Math to a Visual UI: Making abstract Hilbert state collapses intuitive to a human trader was tough. We engineered a dynamic UI that highlights how classical market states collapse into red "Attack" regimes, while entangled states immediately lock into blue "Quantum Nash" safe zones.What We LearnedMarket Structure is Geometry: Most financial engineering attempts to solve MEV at the software layer (e.g., commit-reveal schemes, private mempools). EigenPool proved that MEV is fundamentally a geometric problem—if your system represents orders as exposed scalar values, leakage is inevitable.Hardware Alignment: Writing zero-allocation Rust highlighted how much performance is left on the table by modern high-level frameworks. By aligning our data structures directly with CPU cache lines and SIMD registers, complex quantum simulations can run at microsecond speeds.What's Next for EigenPoolMulti-Party Entanglement ($N$-Player Extensions): Scaling the EWL protocol from 2-player buyer/seller matches to $N$-party liquidity pools using multi-qubit GHZ states.Hardware Acceleration: Offloading the tensor matrix transformation pipeline directly to FPGA smartNICs for sub-nanosecond institutional clearinghouses. <div