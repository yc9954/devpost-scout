---
slug: "dark-ledger"
url: "https://devpost.com/software/dark-ledger"
title: "Dark Ledger"
hackathon: "Kiroween"
organization: "Kiro"
winner: true
words: 536
team_size: 0
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "domain/developer_tools"
  - "domain/finance_payments"
  - "user/developer"
  - "substrate/financial_record"
---

# Dark Ledger

> Legacy Math. Future Money A COBOL-Verified Payroll Engine settled on Base

[Devpost](https://devpost.com/software/dark-ledger) · hackathon [[Kiroween]]

## Facets

**domain** [[developer_tools]] [[finance_payments]]
**user** [[developer]]
**substrate** [[financial_record]]

**stack** cobol, coinbase, python, react

## How they structured the write-up

- inspiration
- what it does
- how we built it

## Body

DarkLedger COBOL Precision. Base Speed. Inspiration DarkLedger is born from a massive contradiction and an act of digital resurrection. COBOL is the language of the establishment—a "forgotten" giant that powers 95% of ATM swipes but has been abandoned by modern developers. Web3 (specifically stablecoins on Base) represents the exit from that system—a permissionless, bankless future. We wanted to force these two sworn enemies to cooperate. Our inspiration was to revive the "dead language" of the banking gods and hook it up to the decentralized rails of the future. It is the ultimate irony: we dug up the forgotten code that built Wall Street to power the ecosystem that aims to replace it. What it does DarkLedger is a hybrid payroll system. It uses a revived COBOL engine to calculate payroll with CPA-grade precision and a Python Bridge to settle those amounts instantly via the Coinbase SDK on Base . The core logic relies on strict fixed-point arithmetic, ensuring that we never lose a penny to rounding errors—a common issue in JavaScript-based math. The formula for Net Pay ($P_{net}$) is calculated as: $$P_{net} = (H \times R) - \left( \sum_{i=1}^{n} T_{fed} + T_{state} \right)$$ Where: ( H ) = Hours Worked ( R ) = Hourly Rate ( T ) = Tax brackets calculated with 2-decimal fixed precision. How we built it The architecture is a "Frankenstein" build, merging three distinct technologies: The Engine (COBOL): We dusted off the manuals and wrote the core payroll logic in GnuCOBOL. It accepts fixed-width text inputs and outputs a trusted ledger. The Bridge (Python): A middleware layer that sanitizes JSON from the frontend, converts it to legacy flat-files, executes the COBOL binary, and parses the result. The Settlement (Base L2): Using the Coinbase Developer Platform (CDP) SDK , we spin up MPC wallets to programmatically execute USDC transfers based on the COBOL output. The Frontend (React + Vite): A retro-futurist UI featuring CRT scanlines, phosphor glow effects, and a dual-theme toggle ("Operator" vs "Halloween") built with Tailwind CSS and Framer Motion. # The Bridge Logic (Simplified) def process_payroll(employee_data): # 1. Convert JSON to Fixed Width for COBOL flat_file = to_cobol_format(employee_data) # 2. Execute Legacy Binary result = subprocess.run(["./payroll.cbl", flat_file]) # 3. Settle on Base L2 if result.success: transfer = wallet.transfer(result.net_pay, "USDC") return transfer.hash ## Challenges we faced The "Lost Knowledge" Barrier: Reviving COBOL was difficult because modern resources are scarce. We couldn't just copy-paste from StackOverflow; we had to read documentation from the 1980s to understand column-sensitive syntax. The Philosophical Clash: Writing COBOL felt like archaeology, while writing the Base integration felt like sci-fi. Mentally switching between punch-card logic and asynchronous blockchain calls was disorienting. The "Frankenstein" Hook: Connecting a modern Python script to a compiled COBOL binary required strict management of standard input/output streams (STDIN/STDOUT) to prevent data corruption. ## What we learned We learned that the revolution still needs a calculator. While DeFi totally hates banks, it can't beat the mathematical perfection of the banking stack. By resurrecting this forgotten tech, we found that "antiquated" doesn't mean "useless." COBOL handles decimal math better than almost any modern language. The future of finance might not be about burning down the mainframe, but simply plugging it into the blockchain. <div