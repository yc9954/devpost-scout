---
slug: "sss-sarah-safe-space"
url: "https://devpost.com/software/sss-sarah-safe-space"
title: "SSS- Sarah Safe Space"
hackathon: "Google's Women Techmakers presents She Builds AI"
organization: "Google"
winner: true
words: 455
team_size: 2
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/retrieval_grounding"
  - "substrate/document_pdf"
  - "substrate/structured_db"
---

# SSS- Sarah Safe Space

> "Sarah" is an empathetic AI assistant providing a safe, judgment-free space. guides users to recognize unhealthy situations and find healing pathways.Your compassionate guide to safety and healing.

[Devpost](https://devpost.com/software/sss-sarah-safe-space) · hackathon [[Google-s Women Techmakers presents She Builds AI]]

## Facets

**mechanism** [[retrieval_grounding]]
**substrate** [[document_pdf]] [[structured_db]]

**stack** chroma, colab, gemini, gradio, langchain, python

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for sss- sarah safe space

## Body

Inspiration At 17, I went through a painful experience and felt alone, unable to talk to friends or family. Finding a supportive friend online made all the difference, helping me heal without judgment. This experience inspired us to create a resource that provides others with that same kind of compassionate, non-judgmental support, so no one has to face their pain alone. What it does "SSS - Sarah Safe Space" is a virtual assistant that uses the Retrieval-Augmented Generation (RAG) technique to provide empathetic support while offering practical solutions. It helps individuals facing challenging situations by combining emotionally supportive language with actionable steps. The assistant retrieves relevant information from uploaded documents and integrates it into personalized responses to guide users through their situations. How we built it We used RAG to build "Sarah" because it enables us to combine large document retrieval with AI-generated responses, making the assistant more dynamic. Using LangChain for document loading, splitting, and storing embeddings, we implemented Google AI's Gemini API to generate thoughtful responses. The assistant’s structure was fine-tuned to balance empathy with practicality, and Gradio was used to create an intuitive interface for users to interact with the assistant. Challenges we ran into The biggest challenge was finding the right balance between empathy and practical solutions. Our initial prompt setups either focused too much on structured, impersonal responses or were overly emotional without providing practical guidance. We needed to modify the prompt to strike a balance, ensuring that responses remained compassionate while offering concrete steps and resources to help users Accomplishments that we're proud of We are proud of successfully implementing the RAG technique to create a responsive, supportive AI assistant. By customizing the prompt, we achieved a blend of emotional support and actionable solutions, which was a key challenge. We are also pleased with the assistant's flexibility in adding new resources and updating documents as needed, making it a sustainable solution for ongoing support. What we learned in this project, we gained valuable insights into the RAG technique, prompt engineering, and the role of empathy in AI-driven support. We learned to optimize document embedding and retrieval in the RAG pipeline, enhancing the assistant’s ability to retrieve relevant information from user-provided documents. LangChain’s tools for memory and conversation handling were also instrumental in shaping the experience. What's next for SSS- Sarah Safe Space Next, we plan to expand "Sarah's" capabilities by enhancing local resource databases, adding multilingual support, and improving its ability to assess the urgency in user queries. We aim to refine the RAG technique further to increase response accuracy and explore partnerships with local support organizations to broaden resource options for users. Enhancements to the UI and additional safety resources are also part of the future roadmap. <div