---
slug: "signal0ne"
url: "https://devpost.com/software/signal0ne"
title: "Signal0ne"
hackathon: "Docker AI/ML Hackathon"
organization: "Docker"
winner: true
words: 504
team_size: 2
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/retrieval_grounding"
  - "mechanism/sensor_fusion"
  - "domain/developer_tools"
  - "user/developer"
  - "substrate/sensor_telemetry"
---

# Signal0ne

> Quick, seamless and automated insights powered debugging for contenerized apps.

[Devpost](https://devpost.com/software/signal0ne) · hackathon [[Docker AI-ML Hackathon]]

## Facets

**mechanism** [[retrieval_grounding]] [[sensor_fusion]]
**domain** [[developer_tools]]
**user** [[developer]]
**substrate** [[sensor_telemetry]]

**stack** angular.js, docker, dockerdesktop, fastapi, llama2, python, qdrant, scikit-learn

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we run into
- accomplishments we are proud of
- what’s next for signal0ne

## Body

INSPIRATION The project was born from a simple idea, simple idea to produce automated insights from failed containers and containers with anomalous resource usage. The main value brought by this type of insights is shorter time to resolve/discover problems with containerized apps for experienced engineers and skyrocketed ability to debug for less experienced engineers. WHAT IT DOES Thanks to anomaly detection algorithms, large language models and Docker desktop extensions, current features of signal0ne extension allow to: Automatically detect anomalies in CPU or memory usage which can help in debugging issues like not sufficient resource limits or memory leaks, based on logs from container affected by anomaly initial insight is provided by signal0ne. Discover failed containers and provide insight about the issue based on logs, container state and container definition. HOW WE BUILT IT Signal0ne docker desktop extension is built using python and angular framework. On the backend there are two components api for extension ui and mlworker which actively scans for anomalies and failed containers. UI is simple and readable thanks to the layout known from other developer tools. After anomaly or failed container is discovered, LLaMa70b language model hosted on the hugging face inference api performs semantic log analysis with help of Retrieval Augmented Generation technique from quadrant vector db with vectorized data from different programming forums/publicly available troubleshooting guides. CHALLENGES WE RUN INTO There are a lot of types of runtimes. Each of these runtimes has its own default log structure, different stack traces and different behaviors regarding resource usage. We needed to handle that with help of LLMs general pre-trained “knowledge” and our data provided as context thanks to RAG technique. ACCOMPLISHMENTS WE ARE PROUD OF We’ve managed to make sense of logs from failed containers within seconds, insights produced by signal0ne are fairly accurate and provide a good starting point for complex issues with containerized apps. We even used signal0ne to debug signal0ne!!! WHAT WE LEARNED We’ve learned that there is a lot of room for improvement in how containerized apps are monitored and debugged with new ML techniques and GenAI technology helps to advance them. A lot more context can be provided to analisis for example: response times, error rates and other metrics which can be treated as service level indicators along with resource data from other systems. We’ve also learned that initial insight, while very useful is not definitive answer so that we are planning to add “further chat” feature where users can ask about additional info/log samples or visualizations. WHAT’S NEXT FOR Signal0ne In order to achieve even better results in semantic log analysis we are planning to prepare our fine tuned model based on llama2. We also plan to enhance anomaly detection capabilities using autoencoder architecture for our future anomaly detection model. Further “chat” feature where users can ask about additional info/log samples or visualizations. Last but not least we would like to extend supported ingested data for analysis with traces, logs and metrics produced by opentelemetry instrumentations, preparing signal0ne to be an observability tool. <div