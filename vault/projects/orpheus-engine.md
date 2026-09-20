---
slug: "orpheus-engine"
url: "https://devpost.com/software/orpheus-engine"
title: "Orpheus Engine"
hackathon: "HP & NVIDIA Developer Challenge"
organization: "HP"
winner: true
words: 577
team_size: 1
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/retrieval_grounding"
  - "mechanism/voice_speech"
  - "domain/developer_tools"
  - "user/developer"
  - "substrate/structured_db"
  - "substrate/transcript_audio"
---

# Orpheus Engine

> The Orpheus Engine Workspace, the AI-powered DAW for audio restoration and analysis, offering seamless cross-device use and diverse plugin support for music, gaming, and data science!

[Devpost](https://devpost.com/software/orpheus-engine) · hackathon [[HP - NVIDIA Developer Challenge]]

## Facets

**mechanism** [[retrieval_grounding]] [[voice_speech]]
**domain** [[developer_tools]]
**user** [[developer]]
**substrate** [[structured_db]] [[transcript_audio]]

**stack** graphql, python, typescript

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for orpheus engine

## Body

DAW open in Electron Inspiration The Orpheus Engine Workspace is a Digital Audio Workstation that enables users to perform audio restoration and analysis with the assistance of an AI agent. The app is designed to work seamlessly within any environment, allowing users to continue their research in the browser, on desktops, and mobile devices. The use of various data technologies designed as plugins for diverse audio exports that include metadata or analysis results critical for audio applications. The OEW has input with various audio devices, nRF (Bluetooth), audio interfaces, and MADI. The use of the HP Ai Studio can leverage the CPU and GPU, enabling the use of more dynamic and pro-level processing plugins, which can be utilized for Gaming, music, and data science projects. What it does An audio professional will use Orpheus Engine Workspace to edit, analyze, and export data, while having an AI companion for research and the audio analysis from the visual process. With the recording capabilities, this allows a user to record from Bluetooth devices into the DAW, where the agent rag can analyze the audio data, identify the audio recordings for specific needs or suggestions of the Audio engineer. If the audio is a voice or speech, the AI will be able to conduct actions such as audio transcriptions, slice the sections of the audio when the user searches. To later be exported with metadata, or the transcript to be used for further development. How we built it We built this App using available TypeScript components and the demos of the HP Studio to help design the MLFlow and the Jupyter notebooks. A lot of the design and implementation was done using AI. The approach began with the backend, but I had to adjust and redesign the frontend to work within a browser, where the components were only displayed in Electron. This itself posed many challenges. Challenges we ran into The main challenge was fixing all the dependency issues with the components. So I designed a new test suite and refactored all the code to work seamlessly with the browser. This was one of the many other challenges. I began using a model from HuggingFace, later utilized the model within the HP AI Studio. Accomplishments that we're proud of Got it to work! Due to this project's complexity, there have been drawbacks; however, to get it working, many of the features I wanted to incorporate are only mockups. The Plugin Management systems and some of the uses of the nRF devices are not fully tested. What we learned I learned how to prioritize the usage of the App rather than how it is built. With larger projects that have a UI with many components, operating front-end testing suites and MLFlow helps keep track of the development processes. What's next for Orpheus Engine I want to see the Orpheus Engine functioning as a dDapp. I would love for this DAW to be available on AI platforms, repositories, as a decentralized source for exporting audio projects to Web3. With the framework of the plugin store system, OEW can allow other developers to construct apps for processes such as Minting, saving data to a Vector database, and IP plugins ( using Story for securing the rights of the audio) to a plugin. OEW multiple input plugin (VST, Python, Typscript, dApp) design allows an audio pro to use their preferred DAW, and this tool will be the bridge to exporting audio files to Web3. <div