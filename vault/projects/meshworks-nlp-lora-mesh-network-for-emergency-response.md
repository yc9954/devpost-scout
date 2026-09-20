---
slug: "meshworks-nlp-lora-mesh-network-for-emergency-response"
url: "https://devpost.com/software/meshworks-nlp-lora-mesh-network-for-emergency-response"
title: "Meshworks - NLP LoRa Mesh Network for Emergency Response"
hackathon: "TreeHacks 2024"
organization: "TreeHacks"
winner: true
words: 471
team_size: 4
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/voice_speech"
  - "domain/developer_tools"
  - "domain/disaster_emergency"
  - "domain/transportation"
  - "user/developer"
  - "user/frontline_worker"
  - "substrate/geospatial"
  - "substrate/video_visual"
---

# Meshworks - NLP LoRa Mesh Network for Emergency Response

> Imagine an earthquake disabling all telecommunication. We combine mesh-based radio technology with cutting-edge AI processing to build a resilient information network for emergency responders.

[Devpost](https://devpost.com/software/meshworks-nlp-lora-mesh-network-for-emergency-response) · hackathon [[TreeHacks 2024]]

## Facets

**mechanism** [[voice_speech]]
**domain** [[developer_tools]] [[disaster_emergency]] [[transportation]]
**user** [[developer]] [[frontline_worker]]
**substrate** [[geospatial]] [[video_visual]]

**stack** flask, image-augmentation, intel-development-cloud, intel-extension-for-pytorch-(model-optimization), lora, predicitionguardllm, python, pytorch, whisper-(speech-to-text), wio-terminal

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of:
- what we learned:
- what's next for meshworks - nlp lora mesh network for emergency response

## Body

Meshworks Device Nodes Meshworks system architecture Command UI speech to text and NLP demo Command UI AI satellite imagery damage assessment and automatic network notification demo Commemorative group photo Near-final architecture design Completed device node demo Coding the web server In-progress build Saturday night group photo LoRa test bed First messages over LoRa First architecture design Inspiration In times of disaster, the capacity of rigid networks like cell service and internet dramatically decreases at the same time demand increases as people try to get information and contact loved ones. This can lead to crippled telecom services which can significantly impact first responders in disaster struck areas, especially in dense urban environments where traditional radios don't work well. We wanted to test newer radio and AI/ML technologies to see if we could make a better solution to this problem, which led to this project. What it does Device nodes in the field network to each other and to the command node through LoRa to send messages, which helps increase the range and resiliency as more device nodes join. The command & control center is provided with summaries of reports coming from the field, which are visualized on the map. How we built it We built the local devices using Wio Terminals and LoRa modules provided by Seeed Studio; we also integrated magnetometers into the devices to provide a basic sense of direction. Whisper was used for speech-to-text with Prediction Guard for summarization, keyword extraction, and command extraction, and trained a neural network on Intel Developer Cloud to perform binary image classification to distinguish damaged and undamaged buildings. Challenges we ran into The limited RAM and storage of microcontrollers made it more difficult to record audio and run TinyML as we intended. Many modules, especially the LoRa and magnetometer, did not have existing libraries so these needed to be coded as well which added to the complexity of the project. Accomplishments that we're proud of: We wrote a library so that LoRa modules can communicate with each other across long distances We integrated Intel's optimization of AI models to make efficient, effective AI models We worked together to create something that works What we learned: How to prompt AI models How to write drivers and libraries from scratch by reading datasheets How to use the Wio Terminal and the LoRa module What's next for Meshworks - NLP LoRa Mesh Network for Emergency Response We will improve the audio quality captured by the Wio Terminal and move edge-processing of the speech-to-text to increase the transmission speed and reduce bandwidth use. We will add a high-speed LoRa network to allow for faster communication between first responders in a localized area We will integrate the microcontroller and the LoRa modules onto a single board with GPS in order to improve ease of transportation and reliability <div