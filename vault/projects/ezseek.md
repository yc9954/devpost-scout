---
slug: "ezseek"
url: "https://devpost.com/software/ezseek"
title: "EzSeek"
hackathon: "2024 TikTok TechJam"
organization: "TikTok"
winner: true
words: 672
team_size: 3
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "mechanism/retrieval_grounding"
  - "domain/retail_commerce"
  - "domain/transportation"
  - "substrate/structured_db"
  - "substrate/video_visual"
  - "substrate/web_dom"
---

# EzSeek

> EzSeek: Simplify Shopping with GenAI for productivity and promoting ESG

[Devpost](https://devpost.com/software/ezseek) · hackathon [[2024 TikTok TechJam]]

## Facets

**mechanism** [[realtime_stream]] [[retrieval_grounding]]
**domain** [[retail_commerce]] [[transportation]]
**substrate** [[structured_db]] [[video_visual]] [[web_dom]]

**stack** flutter, gemini, image-to-image, langchain, python, rag, stable-diffusion, text-to-image, tiktok-api, virtual-try-on

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for ezseek

## Body

Inspiration EzSeek was inspired by the need for a more intuitive and engaging online shopping experience. Traditional internet shopping frequently lacks engagement and personalisation, resulting in a less enjoyable user experience. We sought to use AI technology to provide a more immersive and personalised shopping experience, while also pushing items that promote environmental and social well-being. What It Does EzSeek has various new features: Multimodal RAG Product Search: Users may search for items using both text and picture inputs, increasing search accuracy, relevancy and productivity. Virtual Try-On: Offers a virtual try-on experience for clothing items, allowing customers to see how the things will appear on them before purchasing. Image-to-Image features to give users a visualization of the outfit to increase engagement rate and suitability. Stable Diffusion to promote ESG and SDG: Highlights and recommends products that support Environmental, Social, and Governance (ESG) initiatives and Sustainable Development Goals (SDG), encouraging more sustainable shopping choices. Text-to-Image will generate random images using stable diffusion and users can redeem the reward with random images that's related to ESG/SDG. At the same time, it can create awareness related to ESG/SDG to contribute to a sustainable and responsible future. How We Built It EzSeek was created by utilising a variety of current technologies and tools: Backend: Developed using Python and FastAPI to handle server-side logic and API interactions with various models and features such as Multimodal RAG, LLM RAG, Virtual Try on and Stable diffusion with fast API. Frontend: Created with Flutter for a responsive and cross-platform user experience. APIs and Models: Gemini AI API: Used to create the Multimodal Retrieval-Augmented Generation (RAG) model, which incorporates the most recent Gemini Flash model for processing pictures and text. TikTok Oembed API: This API is used to embed external material and video into Video Feeds, as well as Author URL data via a get request. Data Processing: Used Pandas for data processing and the Google Text Embedding Model to embed product data in an FAISS vector database. AI Development: Used LangChain to build a multimodal RAG model that delivers personalised product suggestions based on user inputs, such as text and photos to perform LLM/Multimodal RAG using Gemini APIs. IDM-VTON open source to perform virtual tryon provide try on on different clothes. stabilityai/stable-diffusion-xl-base-1.0 to perform stable diffusion and generate images that are related to ESG/SDG. Challenges We Ran Into Integration Complexity: Combining different AI models and APIs posed significant challenges in terms of integration and ensuring seamless functionality. Performance Optimization: Achieving optimal performance for large datasets and ensuring quick response times for product searches required extensive optimization and GPU requirements User Experience Design: Balancing advanced AI features with a user-friendly interface involved iterative design and user testing to ensure a positive user experience. Accomplishments That We're Proud Of Successfully combined image and text processing LLM/Multimodal with RAG to search the product database in FAISS. Virtual Try-On Feature: Created a useful and engaging virtual try-on feature to improve the online purchasing experience. Promotion of ESG and SDG Products using Stable Diffusion: Features have been included to promote ecologically and socially responsible products, hence promoting sustainability goals once users purchase/redeem rewards based on screening hours. What We Learned AI Model Integration: Gained deep insights into integrating and optimizing various AI models and APIs such as Virtual Try-On, Stable Diffusion, Multimodal and LLM RAG. Data Management and Processing: Enhanced skills in handling and processing large datasets, such as data cleaning and transforming them into vector databases for efficient search functionalities. User-Centered Design: Learned the importance of designing with the user in mind to ensure that complex AI functionalities are accessible and useful. What's Next for EzSeek Enhanced AI Capabilities: Plan to integrate more advanced AI features, such as real-time product recommendations and enhanced personalization. Expanded Product Range: Work on incorporating a broader selection of products and improving search accuracy. User Feedback Integration: Actively seek and incorporate user feedback to continuously improve the system's features and usability. Scalability and Performance: Focus on optimizing scalability and performance to accommodate larger datasets and increased user traffic. <div