---
slug: "relightify"
url: "https://devpost.com/software/relightify"
title: "Relight Background"
hackathon: "Canva AI and Integrations Hackathon"
organization: "Canva"
winner: true
words: 575
team_size: 2
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "domain/developer_tools"
  - "domain/labor_employment"
  - "domain/retail_commerce"
  - "substrate/video_visual"
---

# Relight Background

> Your go-to solution for product photos: one-click background removal and replacement, with enhanced lighting. Achieve studio-quality images in seconds—perfect for e-commerce, photography, and design.

[Devpost](https://devpost.com/software/relightify) · hackathon [[Canva AI and Integrations Hackathon]]

## Facets

**domain** [[developer_tools]] [[labor_employment]] [[retail_commerce]]
**substrate** [[video_visual]]

**stack** amazon-dynamodb, amazon-ec2, amazon-sqs, amazon-web-services, cloudflare, comfyui, controlnet, directus, docker

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for relight background

## Body

feature image 1 feature image 2 feature image 3 CMS screenshot for config one background template CMS screenshot for background templates config ComfyUI workflow App UI on Canva Inspiration Our project was inspired by the need for a faster, more efficient way to create professional-quality product photos. Through insights from Facebook groups and Reddit, we discovered that background replacement and removal are top priorities for Canva users. Traditional photoshoots are costly and time-consuming, particularly for e-commerce businesses and marketing designers. We aimed to develop an AI-powered tool that simplifies this process, enabling users to remove backgrounds, adjust lighting, and create stunning visuals with just a few clicks. What it does Our app automatically replaces backgrounds and enhances lighting in product photos, allowing users to generate studio-quality images in seconds. With customizable templates and styles, it’s easy to create visually appealing photos that align with any brand’s aesthetic. Ideal for e-commerce, photography, and design, the app helps users produce professional-grade images without the need for expensive equipment or complex editing software. How we built it We leveraged Canva's Apps SDK (Selection API and other components) and advanced AI models for background removal and lighting enhancement. Our backend infrastructure uses Cloudflare Workers, R2 for file storage, and Durable Objects for managing tasks and data, while ensuring low latency for global users. We scaled the ComfyUI workflow for concurrent requests using AWS SQS and DynamoDB, with Docker-based processing to handle multiple requests simultaneously within the machine’s capacity. The AI models integrate with ComfyUI workflows, including ICLight for light style transfer, FACEID and IPAdapter for likeness preservation, and light depth ControlNet for consistency. We implemented a CMS based on Directus.io to manage templates, reducing manual configuration errors and allowing for tailored templates to suit different user scenarios. Challenges we ran into Ensuring precise background removal was critical for the relighting process. We needed a highly accurate model to effectively separate foreground objects from backgrounds. Maintaining the integrity of the subject while applying new backgrounds and lighting was complex, requiring a balance between AI enhancements and preserving original details. Integrating multiple AI capabilities—such as object segmentation, background removal, lighting adjustment, text prompt background generation, and image upscaling—added complexity to the workflow and challenges to scalability. Cost of maintaining the service with reasonable reliability is high when it comes to GPU jobs Accomplishments that we're proud of We’re proud of developing a tool that significantly reduces the time and cost of product photography. Our app successfully integrates various AI capabilities into a seamless user experience, making professional-grade photo editing accessible to all. We also built a scalable infrastructure capable of handling high volumes of requests without compromising performance. What we learned We learned the importance of balancing AI automation with user control to achieve the best results. While AI can manage many aspects of photo editing, user input remains crucial for fine-tuning outcomes. We gained valuable experience in optimizing AI workflows for scalability and performance. What's next for Relight Background We plan to expand the app’s features by adding more customizable templates and styles based on user feedback. We’re exploring the integration of text prompts or custom images for generating backgrounds and lighting setups to enhance the app’s flexibility. We aim to improve the AI’s ability to handle complex scenes and subjects, ensuring it meets the needs of e-commerce businesses and professional photographers alike. In terms of service sustainability, we’ll try monetize it with premium model if things go well. <div