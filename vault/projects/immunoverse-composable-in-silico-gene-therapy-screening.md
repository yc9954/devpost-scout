---
slug: "immunoverse-composable-in-silico-gene-therapy-screening"
url: "https://devpost.com/software/immunoverse-composable-in-silico-gene-therapy-screening"
title: "ImmunoVerse: Composable In Silico Gene Therapy Screening"
hackathon: "UC Berkeley AI Hackathon 2026"
organization: "Cal Hacks"
winner: true
words: 1349
team_size: 1
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/multi_agent"
  - "mechanism/voice_speech"
  - "domain/developer_tools"
  - "domain/health_clinical"
  - "domain/mental_health"
  - "domain/scientific_research"
  - "user/developer"
  - "user/patient_family"
  - "substrate/genomic_bio"
  - "substrate/geospatial"
  - "substrate/structured_db"
  - "substrate/transcript_audio"
  - "substrate/web_dom"
---

# ImmunoVerse: Composable In Silico Gene Therapy Screening

> A decentralized network of AI specialist agents running patient-specific, systems-level safety screenings for gene therapies in seconds to catch clinical failures before the wet lab.

[Devpost](https://devpost.com/software/immunoverse-composable-in-silico-gene-therapy-screening) · hackathon [[UC Berkeley AI Hackathon 2026]]

## Facets

**mechanism** [[multi_agent]] [[voice_speech]]
**domain** [[developer_tools]] [[health_clinical]] [[mental_health]] [[scientific_research]]
**user** [[developer]] [[patient_family]]
**substrate** [[genomic_bio]] [[geospatial]] [[structured_db]] [[transcript_audio]] [[web_dom]]

**stack** agentverse, asi:one, esmfold, iedb-bepipred, iedb-netmhciipan-4.0, iedb-netmhcpan-4.1, python, uagents, uv

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for immunoverse: composable in silico gene therapy screening

## Body

Inspiration There isn't a very mature way to put this, but my inspiration stems from a childhood fear of death - more specifically, watching a scene where a dead skeleton lay on the ground in Disney's Tangled kicked this whole thing off. After worrying about it for years, I started wondering why we died in the first place. The strongest indicator seemed to be the accumulation of harmful genetic mutations over time: given enough mutations, cells either produce faulty proteins that the immune system flags for destruction, or they become senescent and stop dividing. This led me to rediscover the idea of extending longevity, or possibly even achieving biological immortality, by editing the genome back to healthier states, or toward beneficial mutations as our environments change. Gene therapy is the most credible path I've found toward that goal. But there's a gap between the vision and the clinic: the therapies that reach patients today fail at an alarming rate not because the science is wrong, but because safety problems are discovered too late. ImmunoVerse is my attempt to close that gap. What it does ImmunoVerse screens gene therapy candidates for safety before they reach the wet lab. It is a patient-personalized, multi-stage in silico safety screening system for gene editing therapies. Given an edited protein sequence and a patient's HLA profile, it evaluates two independent failure modes before a therapy ever reaches the wet lab: Immunogenic rejection - will the immune system recognize the modified protein as foreign, mount a T-cell or antibody response, and destroy the edited cells? Systems-level disruption - even if the immune system tolerates the edit, will it destabilize cellular function by introducing a cryptic splice site, disrupting transcription factor binding, or triggering apoptotic signaling? The pipeline runs four stages in sequence: structural modeling (ESMFold + SASA surface exposure), HLA binding prediction (NetMHCpan Class I + II via IEDB), parallel immune reactivity analysis (T-cell and B-cell branches), and whole-transcriptome systems dynamics. A final LLM node - powered by ASI:One or Claude - synthesizes the results into a plain-language clinical report with a headline verdict, per-stage findings, risk rationale, and actionable mitigation suggestions. Each stage is implemented as an independent specialist agent registered on Agentverse. Any AI agent on the network can call individual stages directly or route through the orchestrator for a full pipeline run - making the system composable infrastructure for the broader biotech AI ecosystem, not just a one-off screening tool. The individual tools - ESMFold, NetMHCpan, BepiPred - are already used in research labs. They exist, but the integration doesn't. Commercial immunogenicity services are out there but are slow, expensive, and black boxes. No one has an open, composable, multi-agent pipeline that exposes each stage individually as a callable API. How we built it The pipeline has two parallel implementations that share the same underlying tool layer: LangGraph StateGraph drives the Streamlit web app and terminal demo. The graph uses conditional edges for the Stage 1 retry loop (low-confidence structural prediction triggers a fallback re-run), parallel Send dispatch for the Stage 3 T-cell and B-cell branches, and a single aggregation node that computes the weighted risk vector before the LLM report node. Fetch AI uAgents provides the multi-agent network layer. Seven specialist agents, one per pipeline stage plus an orchestrator, are independently registered on Agentverse using register_chat_agent with cryptographic identity derived from seed phrases. The orchestrator holds the addresses of all specialists and routes messages through the Agentverse relay. Each agent can also be called directly by any Agentverse-compatible client. Real biology tools are wired at Stage 1 (ESMFold via the ESM Atlas REST API), Stage 2 (IEDB's NetMHCpan-4.1 and NetMHCIIpan-4.0), and Stage 3b (BepiPred via IEDB). Stages 3a (NetTCR-2.0) and 4 (GenBio AI AIDO) use high-fidelity mock implementations that replicate the expected output schemas. All tools share a common abstract base class layer, so swapping a mock for a real implementation requires no changes to the pipeline graph or agent logic. Challenges we ran into Agentverse endpoint routing was the hardest bug to diagnose. When agents were registered with http://localhost:{port}/submit endpoints via the registration API, Agentverse attempted push-delivery to localhost - which it can't reach from its servers. The fix required running all agents with mailbox=True first so the uAgents runtime updates the Almanac with the relay URL, then re-running registration to store the correct endpoint. The client also needed to route via the Almanac rather than Agentverse's push-delivery system, or it would hit the same localhost failure. Parallel fan-out in LangGraph required understanding the Send primitive. Standard edges broadcast state to both Stage 3 branches simultaneously, but without Send the graph couldn't dispatch different payloads to each branch independently. Getting the join node to wait for both branches to complete before proceeding to Stage 4 required careful state merging. Schema consistency across both implementations was a recurring constraint. The Pydantic models powering the LangGraph state also needed to survive serialization through uAgents JSON message passing, which caught several field name mismatches between what the orchestrator sent and what the specialist agents expected. Real biology API quirks - IEDB's rate limits, ESMFold's sequence length constraints, and BepiPred's non-standard response format meaning each required custom retry logic and fallback handling. Accomplishments that we're proud of Running a biologically meaningful end-to-end screen from a raw sequence to plain-language clinical verdict in under 30 seconds, personalized to a patient's HLA haplotype, is something that would have taken a computational biologist days to do manually a few years ago. Getting seven specialist agents independently registered and callable on Agentverse, each with a clean public message contract, demonstrates that AI-native biomedical infrastructure is achievable today. The LOW_IMMUNOGENIC scenario is my favorite result: the HLA bindings are low and so there is little T-Cell reactivity which wouldn't reject the KRAS edit. However, the BepiPred B-Cell reactivity is high which means the edit would get flagged. Stage 4 catches the RAS/MAPK pathway disruption independently at the systems level. That's the case for always running the full pipeline - if there was neither high T-Cell or B-Cell reactivity experimentation would continue, but having insight into how these edits work on a cellular level can save a lot of time and money. What we learned Designing message contracts first and implementations second makes multi-agent systems dramatically easier to debug. Every inter-agent message in ImmunoVerse is a typed Pydantic model with a single serialization path and so when something breaks, it's immediately obvious which stage sent the wrong shape. Agentverse's relay model (agent polls Agentverse, not the other way around) is the right mental model for agents running behind NAT or on developer laptops. The documentation undersells this; most of the routing confusion stemmed from conflating push-delivery with mailbox polling. Designing the risk scoring and clinical report to communicate uncertainty honestly - not overstating confidence in a result that's only as good as its weakest tool - required as much thought as the engineering. What's next for ImmunoVerse: Composable In Silico Gene Therapy Screening The immediate next step is retrospective validation - running the pipeline against gene therapy candidates with known clinical immunogenicity outcomes to measure sensitivity and specificity end-to-end. That's the study that moves this from a promising screening tool to an evidence-based one. The two mock stages are the next most important near-term targets. Wiring NetTCR-2.0 behind a local Docker service and connecting to the GenBio AI AIDO API for real transcriptome perturbation prediction would make the systems-level signal clinically actionable rather than illustrative. Beyond completing the tool layer, the most compelling direction is cohort-level analysis: given a proposed edit and a population's HLA frequency distribution, what fraction of patients would be at high risk? That's the question gene therapy developers actually need answered before Phase I. The composable Agentverse architecture makes it straightforward to fan out hundreds of personalized pipeline runs in parallel. Longer term, integrating with clinical trial databases to validate predictions against known immunogenicity outcomes would let the risk model be calibrated on real-world data - closing the loop between in silico prediction and clinical observation that is currently the biggest gap in the field. <div