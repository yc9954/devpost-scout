---
slug: "aisquar3d"
url: "https://devpost.com/software/aisquar3d"
title: "SquareCubed"
hackathon: "Square + Google AI Hackathon"
organization: "Square"
winner: true
words: 705
team_size: 2
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "mechanism/retrieval_grounding"
  - "domain/developer_tools"
  - "domain/labor_employment"
  - "domain/retail_commerce"
  - "substrate/financial_record"
  - "substrate/video_visual"
---

# SquareCubed

> Interactive 3D virtual showrooms for square sellers! Effortlessly add interactive 3D models, offering customers real-time, AI-driven customization.

[Devpost](https://devpost.com/software/aisquar3d) · hackathon [[Square - Google AI Hackathon]]

## Facets

**mechanism** [[realtime_stream]] [[retrieval_grounding]]
**domain** [[developer_tools]] [[labor_employment]] [[retail_commerce]]
**substrate** [[financial_record]] [[video_visual]]

**stack** google-vertex-ai, next.js, node.js, python, square, svelte, webgi

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for squarecubed

## Body

Product with our "Launch Virtual Experience" link SquareCubed App page to select the store to integrate SquareCubed with SquareCubed App page to select the items to integrate SquareCubed and convert to 3d with AI configurator Example configurator for a Bracelet Example configurator for a sofa set demonstrating use case for interior designs Another config for the sofa set Example configurator for a watch Inspiration The conception of SquareCubed was ignited by the evident gap in the e-commerce sphere, where store owners struggle with the absence of assistance for variations on e-commerce. Additionally, customers are often overwhelmed by the myriad of options available, leading to indecision, a high bounce rate, and a suboptimal shopping experience. Furthermore, sellers in luxury markets like interiors, and jewellery find it hard to sell products online without an engaging experience. For cases like these, 3D visualization has been shown to increase the conversion rate significantly. SquareCubed emerged as a solution, bridging this divide by offering a synergized, AI-driven, interactive 3D customization experience. What it does SquareCubed is an AI assisted virtual showroom experience for online sites and in-store kiosks. We try to elevate the e-commerce landscape by integrating AI and Photorealistic 3D rendering into Square Online stores. With the aid of Google’s PaLM 2 AI, WebGi Rendering and Configurators, store owners can now immerse their customers in a tailored, interactive shopping experience, be it interior design, jewellery, watches, apparel, etc. Customers engage in real-time conversations with AI, receiving personalized product customization suggestions visualized through a dynamic 3D model viewer, enhancing decision-making and user engagement, and acting like an assistant for querying and configuring the products. How we built it Leveraging Google Vertex AI’s PaLM 2 text-bison model and WebGi SDK for 3D Rendering and configurators and Square APIs for e-commerce, we constructed an intuitive interface in the Svelte framework bolstered by the robust support of Cloudflare Workers. The AI takes product metadata, including its title, description, all available variations for each configuration, customer's chat, and current configuration to determine a combination suited to the customer's need. The intricate orchestration of these technologies enabled the seamless integration of a 3D configurator and AI chatbox, crafting a harmonious user journey enriched by real-time, AI-powered interactions. Challenges we ran into Engineering a prompt that facilitates effective AI assistance posed an initial challenge, demanding meticulous engineering and refinement to get it working across multiple industries of products based on the metadata from the store. Integrating a 3D configurator and its symbiosis with AI recommendations required innovative solutions to ensure seamless functionality. Perfecting the user journey while adhering to the constraints of existing Square APIs, demanded creative problem-solving approaches. Accomplishments that we're proud of We are immensely proud of creating the first solution where a 3D configurator seamlessly integrates with an AI chat, creating an ecosystem where choices are not just suggested but visualized in real-time with photo-realistic. This amalgamation of technology elevates the customer’s journey from a transaction to an immersive experience, marked by personalized engagement and visual interaction. We believe this has a lot of scope and are working on creating a production version for sellers across the world selling luxury items. What we learned While developing SquareCubed, we got invaluable insights into harnessing the prowess of Google Vertex AI and PaLM 2. We delved deep into the integration of WebGI SDK and LLMs, unlocking new horizons in embedding 3D configurators into Square stores, automating the complete process of using custom 3D models and tweaking AI based on the model contents and material variations. What's next for SquareCubed We’re geared towards refining the user experience, adding nuanced controls for a more tailored 3D model interaction. The horizon includes enabling custom 3D model uploads with interactive Configurator Creator, making SquareCubed an even more personalized tool for store owners. Also, adding a mode for in-store terminal and kiosks for interactive shopping. Our vision is to launch SquareCubed as a fully-fledged Square App, having perfected every integration, poised to redefine the landscape of e-commerce engagement. With further improvements in LLM and other technologies at Google AI, the assistant would work exactly like a store employee, and sellers would be able to train their AI with different personalities like store managers, interior designers, jewellery designers, sales-person, etc. <div