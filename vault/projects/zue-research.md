---
slug: "zue-research"
url: "https://devpost.com/software/zue-research"
title: "Zue Research"
hackathon: "TreeHacks 2025"
organization: "TreeHacks"
winner: true
words: 624
team_size: 3
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/multi_agent"
  - "mechanism/on_device_local"
  - "domain/accessibility"
  - "domain/education"
  - "user/educator_student"
  - "user/general_public"
  - "user/researcher"
  - "substrate/video_visual"
  - "substrate/web_dom"
---

# Zue Research

> interactive multimodal AI experiences for neurodivergent learners run entirely on the edge

[Devpost](https://devpost.com/software/zue-research) · hackathon [[TreeHacks 2025]]

## Facets

**mechanism** [[multi_agent]] [[on_device_local]]
  <sub>weak: realtime_stream</sub>
**domain** [[accessibility]] [[education]]
**user** [[educator_student]] [[general_public]] [[researcher]]
**substrate** [[video_visual]] [[web_dom]]

**stack** elevenlabs, groq, javascript, langchain, lumalabs, mistral, openai, perplexity, rust, typescript

## How they structured the write-up

- inspiration
- what it does
- how we built it
- accomplishments we're proud of
- what we learned
- sources

## Body

GIF A montage of screen grabs from Zue Research Schematic diagram of Zue Research Example of edge computing cluster with 3 consumer hardware nodes Interface for edge computing Example of LLM running inference on-the-edge A student uses the "enrich" feature being used to add context to a podcast in real time Agentic AI generates contrasting opinions to debate each other Agents search the web to build their theses in paralle Synthesization allows for easy access to sources A podcast discusses the burgeoning field of nuclear energy TL;DR: we created interactive multimodal AI journeys for neurodivergent learners which can be run entirely on the edge Inspiration 56% of students in the world do not have internet access at school [1]. Students learn best through multi-sensory, hands-on, structured experiences that are tailored to their interests. Yet, the primary method of learning for them continues to be textbooks. This is even more pertinent to the 129 million students globally who have ADHD [2]. We built in our product with neurodivergent and offline learners in mind. Drawing on bleeding edge research, we proved that multimodal applications can be deployed entirely at the edge using distributed inference using heterogeneous compute [3] [4]. What It Does After students describe what they’d like to learn more about, we create multiple adversarial agents which perform “deep research” (i.e. search the web, synthesize, reflect, and repeat). Think anything from “debate the entirety of modern Tunisian history” to “tell me how the organelles of a plant cell differ from those of an animal”. When these agents finish, they summarize their findings and provide related “branches” the students can look into. If the student is done researching, we generate a podcast with visual aids that shows multiple agents debating each other. At any point in the podcast, a student can double click on a segment to have a new research agent answer questions or clarify topics. How We Built It We needed to create a dynamic and engaging frontend that would be easy-to-use for teachers and students alike. We chose Typescript and spun up an application that could provide live insights into the actions that the agents were taking, and playback the podcast in a lively manner. For our backend, we faced the challenge of orchestrating researchers engaging in Multi-Agent Debates . Despite being first-time users, we chose Rust for its superior concurrent performance and memory safety features, which were crucial for managing shared state across multiple research agents and handling asynchronous web operations safely. To support our cloud implementations, we chose ElevenLabs to generate the voices of our podcast and to create an agent to converse with the student after the podcast to test their understanding using the Feynman technique . We used LumaLabs for the podcast image generation. We also made creative use of the Perplexity Sonar web search API and Mistral via groq . Accomplishments We're Proud Of We were able to get our backend to run locally by sharding full size large language models across multiple hardware devices (i.e. we ran Llama on between a MacBook Pro and 2x MacMinis). Despite never having written code in Rust, we wrote our entire research agent server in a Rust implementation of LangChain. Some cool things we did with Rust: Tokio for async runtime and concurrent processing for multiple agents let (track_one_result, track_two_result) = tokio::join!( self.process_track(state.clone(), "one"), self.process_track(state.clone(), "two") ); Arc> for thread-safe shared state let state = Arc::new(Mutex::new( SummaryState::with_research_topic(input.research_topic.clone()) )); What We Learned Building for education is both technologically challenging and highly rewarding. The members of our team were able to learn Rust from the ground up, taking advantage of its supreme efficiency, and learn how to build for the modern Ed-Tech consumer. Sources [1] https://ourworldindata.org/grapher/primary-schools-with-access-to-internet?tab=table [2] https://chadd.org/about-adhd/general-prevalence/ [3] https://arxiv.org/html/2405.14371v1 [4] https://github.com/exo-explore/exo <div