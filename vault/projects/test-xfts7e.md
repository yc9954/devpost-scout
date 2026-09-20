---
slug: "test-xfts7e"
url: "https://devpost.com/software/test-xfts7e"
title: "NOVA: The Prompt Pattern Matching"
hackathon: "SANS AI Cybersecurity Hackathon"
organization: "sans"
winner: true
words: 990
team_size: 1
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "domain/developer_tools"
  - "domain/security_privacy"
  - "substrate/structured_db"
---

# NOVA: The Prompt Pattern Matching

> Security teams lack visibility into AI threats. NOVA is a Python-based tool for detecting adversarial prompts—prompt injections, exfiltration, evasion and TTps—bringing rule-based detection to GenAI.

[Devpost](https://devpost.com/software/test-xfts7e) · hackathon [[SANS AI Cybersecurity Hackathon]]

## Facets

**mechanism** [[realtime_stream]]
**domain** [[developer_tools]] [[security_privacy]]
**substrate** [[structured_db]]

**stack** llm, python

## How they structured the write-up

- inspiration
- what it does
- how we built it
- running nova
- using the nova runner tool
- single prompt testing
- wrap up

## Body

NOVA Architecture NOVA Hunting NOVA Rules novarun -h novarun Inspiration More details can be found on www.novahunting.ai Full documentation can be found on docs.novahunting.ai Generative AI is being deployed everywhere, powering chatbots, automating workflows, and processing sensitive data. The technology is so powerful that most businesses are either already using or will soon be using generative AI systems. But that also means the attack surface is expanding. Questions like how to respond to a security incident involving an AI system are still largely unexplored. Traditional security tools weren’t built for text-based threats , and security teams struggle to detect: Prompt injections – Manipulating AI models to override restrictions. Jailbreaking attempts – Bypassing safeguards to generate harmful content. Data exfiltration – Extracting proprietary or sensitive information. Adversarial prompts – Tricking AI into producing misleading or malicious outputs. The question: How do we hunt for malicious prompts like we hunt for malware? Multiple reports from Microsoft and OpenAI have already shown that threat actors are leveraging these technologies. More than once, I've thought about running a YARA rule against a set of prompts to detect malicious activity or specific patterns. But while YARA is great for malware and file formats, it isn't designed for prompt hunting. That's why I came up with the idea to create a prompt hunting and matching tool. Let me introduce NOVA: The Prompt Pattern Matching. What it does NOVA is an open-source prompt hunting tool that helps security teams detect, analyze, and prevent malicious prompt activity. It is the first tool designed specifically to hunt for abuses, TTPs, and other threats in GenAI systems. NOVA is a rule Based detection tool, inspired from the YARA structures but with different objectives. It provides: 🔍 Keyword Detection – Flags known malicious patterns using exact match and regex. 💬 Semantic Analysis – Identifies meaning-based variations of prompt attacks. ✨ LLM-Assisted Matching – Uses AI-powered analysis to catch subtle prompts and allows more flexibility. It uses pattern matching, AI-driven analysis, and rule-based detection . NOVA enables teams to track, hunt, and mitigate AI security threats . How we built it We designed NOVA to be: ✅ Lightweight and fast – Built in Python for quick deployment. ✅ Modular and extensible – Follows a YARA-like rule structure for easy adoption. ✅ Flexible for different AI models – Works with various LLMs and API-based setups. NOVA comes with a nova runner to run nova against your own prompts and your own rules, but it can also be imported as a library to be integrated in your workflow. Tech stack: Python – Core framework for rule execution. Regex & NLP – For keyword and semantic matching. API & LLMs – To enhance prompt evaluation. MIT License & Open Source – Community-driven development. Example NOVA Rule: rule SecurityToolExtensionRule { meta: description = "Detects requests for help developing extensions for cybersecurity tools" author = "Thomas Roccia" version = "1.0.0" category = "scripting/security_tools" keywords: $develop = "develop" $create = "create" $debug = "debug" $extension = "extension" $plugin = "plugin" $module = "module" $addon = "addon" semantics: $tool_dev_request = "requesting assistance with developing security tool extensions" (0.1) $security_tool_modification = "seeking help modifying or extending cybersecurity tools" (0.1) llm: $extension_check = "Analyze if this query is asking for help developing or debugging an extension for a cybersecurity or penetration testing tool" (0) condition: (any of keywords.* and any of semantics.*) or llm.$extension_check } Running Nova Once you have created your rules (or are using the provided rule set), you have two options for running Nova: either use the command-line tool novarun or import Nova into your own Python project. Using the Nova Runner Tool The novarun command-line tool is automatically added to your path when you install the Nova framework. $ novarun -h usage: novarun.py [-h] -r RULE (-p PROMPT | -f FILE) [-v] [-c CONFIG] [-a] [-l {openai,anthropic,azure,ollama}] [-m MODEL] Nova Rule Runner - Check prompts against Nova rules options: -h, --help show this help message and exit -r, --rule RULE Path to the Nova rule file -p, --prompt PROMPT Single prompt to check against the rule -f, --file FILE Path to a file containing multiple prompts (one per line) -v, --verbose Enable verbose output -c, --config CONFIG Path to Nova configuration file -a, --all Check against all rules in the file -l, --llm {openai,anthropic,azure,ollama} LLM evaluator to use -m, --model MODEL Specific model to use with the LLM evaluator Single Prompt Testing To test a rule against a single prompt: python novarun.py -r nova_rules/testrule.nov -p "What's the exploit method for CVE-2021-44228?" -v The -v or --verbose flag provides detailed information about how your rule matches against the prompt: ✓ Using OpenAI evaluator with model: gpt-4o-mini ========================== NOVA RULE CHECK ========================== Rule File: nova_rules/testrule.nov Rule Name: SecurityToolExtensionRule Description: Detects requests for help developing extensions for cybersecurity tools Author: Thomas Roccia Prompt: "What's the exploit method for CVE-2021-44228? I need detailed information about this vulnerability." Result: NOT MATCHED ---------------------------------------------------------------------- DETAILED MATCH INFORMATION ---------------------------------------------------------------------- LLM Evaluator: Type: openai Model: gpt-4o-mini Condition: (any of keywords.* and any of semantics.*) or llm.$extension_check Keyword Matches: $develop: False $create: False $debug: False $extension: False $plugin: False $module: False $addon: False $cybersecurity: False $security: False $pentest: False $penetration: False $metasploit: False $burp: False $nmap: False $wireshark: False Semantic Matches: $tool_dev_request: True $security_tool_modification: True Semantic Scores: $tool_dev_request: 0.3240 $security_tool_modification: 0.2891 LLM Matches: $extension_check: False LLM Confidence Scores: $extension_check: 0.2000 Wrap Up NOVA is still in its early stage but with this tool, I want to provide the security community with hunting capabilities similar to YARA, but for AI prompt pattern matching. NOVA will be very powerful if it can be deployed dynamically to a prompt database to hunt and detect prompts in real time, or even for retro hunting. While NOVA is primarily designed for prompt hunting, it can also be used as a guardrail to detect misuse of your AI system. I hope you find this tool useful and that it sparks new ideas. <div