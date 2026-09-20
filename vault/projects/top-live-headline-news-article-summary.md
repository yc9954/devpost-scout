---
slug: "top-live-headline-news-article-summary"
url: "https://devpost.com/software/top-live-headline-news-article-summary"
title: "MULTI-MODAL RAG: Building Personalized Knowledge Models"
hackathon: "MEGA Hackathon 2025"
organization: "MegaHackathonLeague"
winner: true
words: 726
team_size: 1
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/graph_reasoning"
  - "mechanism/on_device_local"
  - "mechanism/retrieval_grounding"
  - "mechanism/structural_withholding"
  - "user/educator_student"
  - "substrate/document_pdf"
  - "substrate/structured_db"
  - "substrate/video_visual"
---

# MULTI-MODAL RAG: Building Personalized Knowledge Models

> Experience seamless knowledge retrieval with our Multi-Modal RAG app. Combining text and visuals, it ensures accuracy and reduces hallucination, providing reliable answers with enhanced user trust

[Devpost](https://devpost.com/software/top-live-headline-news-article-summary) · hackathon [[MEGA Hackathon 2025]]

## Facets

**mechanism** [[graph_reasoning]] [[on_device_local]] [[retrieval_grounding]] [[structural_withholding]]
**user** [[educator_student]]
**substrate** [[document_pdf]] [[structured_db]] [[video_visual]]
  <sub>weak: financial_record</sub>

**stack** faiss, langchain, mindsdb, python, streamlit

## How they structured the write-up

- problem statement
- current solution
- desired solution
- basic architectures for pkm, mmr-pdf (multi-modal rag for pdf) & mmr-video (multi-modal rag for video)
- basic pkm architecture
- mmr-pdf (multi-modal rag for pdf) architecture (static)
- mmr-video (multi-modal rag for video) architecture (static)
- features:
- demo:

## Body

Live Web Application Home Page User asking a question from the attached pdf related to the text and table data As I mentioned, LLM hallucinates in the answer Clear cut information from the retreived image (Power of Multi Modal RAG) User asking a question from attached youtube video Web Application retreives the relevant information and relevant frame image for better answer Problem Statement Finding relevant information paired with matching images is a significant challenge. Users often struggle to get satisfactory results, especially when relying on traditional retrieval methods. These methods may provide textual information, but they fall short when it comes to presenting relevant images that can enhance understanding and trust. This issue becomes even more pronounced when dealing with complex queries or data presented in formats like tables or videos. The inability to retrieve and display relevant visual information alongside text not only hampers user experience but also leads to mistrust in the system's accuracy. In addition, the phenomenon of "hallucination" in language models further complicates the retrieval process. When an LLM generates text based on the input it receives, it can sometimes produce information that is plausible but incorrect or fabricated. This poses a serious challenge, as users depend on these models for accurate and reliable information. The lack of visual evidence or supplementary data exacerbates this problem, making it difficult for users to discern the validity of the information provided. Therefore, there is a critical need for a solution that can effectively combine relevant text and images, providing a comprehensive and trustworthy answer to user queries. Such a solution should mitigate the risk of hallucination by supporting textual responses with visual evidence, ensuring users receive accurate and reliable information. Current Solution Traditional RAG applications retrieve relevant information from a vector database and pass it to the LLM along with the user's question to generate the final answer. However, LLMs can sometimes hallucinate. Adding images or tables as evidence can reduce these hallucinations. Desired Solution 🤖 MULTI-MODAL RAG APPLICATION 🤖 Building Essence Toward's Personalized Knowledge Model (PKM) To avoid hallucinations, I propose a multi-modal RAG application that provides relevant information and images. The relevant information is passed as context to the LLM along with the user's question, and the relevant image is sent directly to the user. This ensures that even if the LLM hallucinates, the user receives accurate information. Users can also ask questions based on table data. Building a multi-modal vector database requires significant computation and memory. For the competition, I used a static PDF and a YouTube video. Users can ask questions from the PDF or video, and the application retrieves relevant text and images, or video frames. I'm exploring solutions for a dynamic multi-modal vector database for dynamic user data. This innovation leads to the creation of a "Personalized Knowledge Model" (PKM), utilizing the user's device GPU to build advanced knowledge graphs. Microsoft Graphrah uses LLMs to extract entities and relationships for graph creation, which exposes user data to the LLM. Using on-device GPUs for knowledge creation is a better solution for privacy. To help others use their own resources, I have created awesome Colab tutorials. You can find them on my GitHub: GitHub Link Basic Architectures for PKM, MMR-PDF (Multi-Modal RAG for PDF) & MMR-Video (Multi-Modal RAG for Video) Basic PKM Architecture MMR-PDF (Multi-Modal RAG for PDF) Architecture (Static) MMR-Video (Multi-Modal RAG for Video) Architecture (Static) The trickiest part of this project is creating custom LLM and embedding functions using LangChain base class and MDB.ai client. Below are the code blocks for reference: Custom LLM function Code:- Custom Embedding function Code:- Features: Multi-Modal Retrieval :books::movie_camera:: Instantly fetches text, images, and video frames from static PDFs and YouTube videos to answer your queries. Nice UI for User Interaction :art:: Enjoy a user-friendly interface that makes interacting with the chatbot smooth and intuitive. Demo: Live WebApp Link Detailed YouTube Explanation Video Future Enhancements: Dynamic Multi-Modal RAG: Addressing the high computational challenge of creating a multi-modal vector database for dynamic data. On-Device Privacy :lock:: Ensuring data never leaves your device for complete privacy and security. Knowledge Graph Without LLMs: Moving towards a knowledge graph-based approach without relying on LLMs. Open Source Collaboration :globe_with_meridians:: Encouraging contributions to push the boundaries of machine learning and privacy-centric technology. On-Device GPUs Access: Ensuring the creation of advanced knowledge graphs without relying on any cloud services. <div