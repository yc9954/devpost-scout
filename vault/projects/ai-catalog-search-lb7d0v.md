---
slug: "ai-catalog-search-lb7d0v"
url: "https://devpost.com/software/ai-catalog-search-lb7d0v"
title: "AI Product Catalog"
hackathon: "HackAI - Dell and NVIDIA Challenge"
organization: "Dell"
winner: true
words: 669
team_size: 1
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/provenance_signing"
  - "mechanism/retrieval_grounding"
  - "domain/developer_tools"
  - "domain/retail_commerce"
  - "domain/supply_logistics"
  - "substrate/code_repository"
  - "substrate/video_visual"
---

# AI Product Catalog

> An AI engine to make description about product, search product by image or just describe it. Perfect fit for tailor-made product, pawnshop and ecommerce.

[Devpost](https://devpost.com/software/ai-catalog-search-lb7d0v) · hackathon [[HackAI - Dell and NVIDIA Challenge]]

## Facets

**mechanism** [[provenance_signing]] [[retrieval_grounding]]
**domain** [[developer_tools]] [[retail_commerce]] [[supply_logistics]]
**substrate** [[code_repository]] [[video_visual]]
  <sub>weak: structured_db</sub>

**stack** clip, database, frappe, nvidia-ai-workbench, python, text-embedding, vector, vision-language-model

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for ai product catalog

## Body

Architecture Function to search product by dropping an image Result of function to search product by dropping an image Result of function to search product by just describing what you need, no need to limit by exact keyword System automatically generate highly detailed description of image Manage product page Overview about function to manage Inspiration The inspiration for AI Product Catalog (AI Catalog Search) came from observing challenges faced by pawnshop chains in Southeast Asia. When stores receive unique items like a "ring with a dragon shape," they often only record basic descriptions like Gold 22K, ring, and images. This makes it difficult for stores in other locations to find such items when customer request something like "I want to have a cool ring with dragon shape on ruby" without manually sifting through images, which is time-consuming. With AI, we can solve this using image search. Beyond pawnshops, this solution can be applied to e-commerce and industries dealing with non-standardized, tailor-made products. What It Does AI Product Catalog streamlines inventory management by enabling efficient product searches through image and text. It helps businesses quickly locate items, improving customer satisfaction and operational efficiency. Instead of only image embedding search like traditional (using CLIP), this one include high level detail of item by using Visual Large Model for incredible search result. This application ready for end-user by API-ready for mobile apps and webapps. How We Built It We built AI Product Catalog using cutting-edge technologies. We integrated high level of image captioning with VLM, natural language processing, image embedding and leveraging Visual Language Models for accurate semantic searches and simplifying the integration process without complex setups. Experimenting models is quite expensive process with trials and errors. Thanks to NVIDIA AI Workbench, I could save many efforts in setting up environment for each model. Challenges We Ran Into Model Quality: Initial attempts using the CLIP model for image embedding didn't yield satisfactory results for specific descriptions like "ring with dragon head" even work great with image embedding search. Alternative models like BLIP also fell short until we adopted Visual Language Models paired for semantic text search. Performance: The CLIP model from Hugging Face was slow with many dependencies. I have challenge with activate CLIP model from NVIDIA NIM to switch on because of continuing error of failing to execute. Switching to CLIPP.CPP improved speed through pure C++ implementation. Stability: Building for enterprise-grade use was challenging. The initial Next.js setup wasn't stable under aggressive testing about security, authentication and audit trail. Moving to the Frappe framework improved stability but required overcoming a learning curve and limitations. Running multiple containers with NVIDIA AI Workbench: The complex permission of running docker containers by Apps features of NVIDIA Workbench (through docker deamon at /var/host-run/docker.sock) is challenging. Leading to consuming time how to set permission and discover the mechanism how Nvidia AI Workbench running an apps (from which user, from which source). Accomplishments That We're Proud Of We're proud of creating a powerful, user-friendly tool that significantly reduces search time and enhances inventory management across industries. Built on ERP platform, I will compatible with standard of security, compliance standard in enterprise. Successfully integrating advanced AI features into an enterprise-grade system is a major achievement. Furthermore, I discover new way to work with remote GPU server that is more efficient, time-saving and could create an multi-user environment for team to develop AI project without creating JupyterHub with conflicting in python environment. What We Learned We learned the importance of selecting the right models for specific use cases. Furthermore, NVIDIA AI Workbench is very efficient in making a covenient environment to development. Instead of consuming build and rebuild docker container over time every updating environment, just leave it to NVIDIA AI Workbench. This approach allowed me streamlining development. What's Next for AI Product Catalog Next, we plan to improve the codebase to handle more exceptional cases and deploy the system in a cluster mode for scalability. This will ensure robustness and the ability to scale with business growth. <div