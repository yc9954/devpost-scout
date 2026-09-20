---
slug: "oasis-8iv1lu"
url: "https://devpost.com/software/oasis-8iv1lu"
title: "Oasis"
hackathon: "TreeHacks 2024"
organization: "TreeHacks"
winner: true
words: 905
team_size: 3
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/benchmark_measured"
  - "mechanism/deterministic_policy"
  - "mechanism/realtime_stream"
  - "mechanism/retrieval_grounding"
  - "mechanism/vision_ocr"
  - "domain/civic_government"
  - "domain/climate_energy"
  - "substrate/document_pdf"
  - "substrate/sensor_telemetry"
  - "substrate/structured_db"
---

# Oasis

> AI agents help benchmark, assess, and enhance corporate sustainability practices

[Devpost](https://devpost.com/software/oasis-8iv1lu) · hackathon [[TreeHacks 2024]]

## Facets

**mechanism** [[benchmark_measured]] [[deterministic_policy]] [[realtime_stream]] [[retrieval_grounding]] [[vision_ocr]]
**domain** [[civic_government]] [[climate_energy]]
**substrate** [[document_pdf]] [[sensor_telemetry]] [[structured_db]]

**stack** figma, flask, iris, langchain, mongodb, next.js, python

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for oasis

## Body

Inspiration As the world grapples with challenges like climate change, resource depletion, and social inequality, it has become imperative for organizations to not only understand their environmental, social, and governance (ESG) impacts but also to benchmark and improve upon them. However, one of the most significant hurdles in this endeavor is the complexity and inaccessibility of sustainability data, which is often buried in lengthy official reports and varied formats, making it challenging for stakeholders to extract actionable insights. Recognizing the potential of AI to transform this landscape, we envision Oasis as a solution to democratize access to sustainability data, enabling more informed decision-making and fostering a culture of continuous improvement toward global sustainability goals. By conversing with AI agents, companies are able to collaborate in real-time to gain deeper insights and work towards solutions. What it does Oasis is a groundbreaking platform that leverages AI agents to streamline the parsing, indexing, and analysis of sustainability data from official government and corporate ESG reports. It provides an interface for companies to assess their records and converse with an AI agent that has access to their sustainability data. The agent helps them benchmark their practices against practices of similar companies and narrow down ways that they can improve through conversation. Companies can effortlessly benchmark their current sustainability practices, assess their current standings, and receive tailored suggestions for enhancing their sustainability efforts. Whether it's identifying areas for improvement, tracking progress over time, or comparing practices against industry standards, Oasis offers a comprehensive suite of features to empower organizations in their sustainability journey. How we built it Oasis uses a sophisticated blend of the following: LLM (LLaMA 2) parsing to parse data from complex reports. We fine-tuned an instance of meta-llama/Llama-2-7b-chat-hf on the HuggingFace dataset Government Report Summarization using MonsterAPI. We use this model to parse data points from ESG PDF text, since these documents are in a non-standard format, into a JSON format. LLMs are incredibly powerful at extracting key information and summarization, which is why we see such a strong use case here. Open-source text embedding model (SentenceTransformers) to index data including metrics and data points within a vector database. LLM-parsed data points contain key descriptors. We use an embedding model to index these descriptors in semantic space, allowing us to compare similar metrics across companies. Two key points may not have the same descriptions, but are semantically similar, which is why indexing with embeddings is beneficial. We use the SentenceTransformer model msmarco-bert-base-dot-v5 for text embeddings. We also use the InterSystems IRIS Data Platform to store embedding vectors, on top of the LangChain framework. This is useful for finding similar metrics across different companies and also for RAG, as discussed next. Retrieval augmented generation (RAG) to incorporate relevant metrics and data points into conversation To enable users to converse with the agent and inspect and make decisions based on real data, we use RAG integrated with our IRIS vector database, running on the LangChain framework. We have a frontend UI for interacting with our agent in real time. Embedding similarity to semantically align data points for benchmarking across companies Our frontend UI also presents key metrics for benchmarking a user’s company. It uses embedding similarity to find company metrics and relevant metrics from other companies. Challenges we ran into One of the most challenging parts of the project was prompting the LLM and running numerous experiments until the LLM output matched what was expected. Since LLMs are non deterministic in nature and we required outputs in a consistent JSON form (for parsed results), we needed to prompt the LLM and reinforce the constraints multiple times. This was a valuable lesson that helped us learn how to leverage LLMs in intricate ways for niche applications. Accomplishments that we're proud of We are incredibly proud of developing a platform that not only addresses a critical global challenge but does so with a level of sophistication and accessibility that sets a new standard in the field. Successfully training AI models to navigate the complexities of ESG reports marks a significant technical achievement. The ability to turn dense reports into clear, actionable insights represents a leap forward in sustainability practice. What we learned Throughout the process of building Oasis, we learned the importance of interdisciplinary collaboration in tackling complex problems. Combining AI and sustainability expertise was crucial in understanding both the technical and domain-specific challenges. We also gained insights into the practical applications of AI in real-world scenarios, particularly in how NLP and machine learning can be leveraged to extract and analyze data from unstructured sources. The iterative process of testing and feedback was invaluable, teaching us that user experience is as important as the underlying technology in creating impactful solutions. What's next for Oasis The journey for Oasis is just beginning. Our next steps involve expanding the corpus of sustainability reports to cover a broader range of industries and geographies, enhancing the platform's global applicability. We are also exploring the integration of predictive analytics to offer forward-looking insights, enabling users to not just assess their current practices but also to anticipate future trends and challenges. Collaborating with sustainability experts and organizations will remain a priority, as their insights will help refine our models and ensure that Oasis continues to meet the evolving needs of its users. Ultimately, we aim to make Oasis a cornerstone in the global effort towards more sustainable practices, driving change through data-driven insights and recommendations. <div