---
slug: "releaf-ai-ml-analysis-of-satellite-imagery"
url: "https://devpost.com/software/releaf-ai-ml-analysis-of-satellite-imagery"
title: "ReLeaf - AI/ML Analysis of Satellite Imagery"
hackathon: "Hack for Humanity | 2025"
organization: "Kuba Apps"
winner: true
words: 560
team_size: 3
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/sensor_fusion"
  - "domain/climate_energy"
  - "domain/developer_tools"
  - "user/developer"
  - "substrate/geospatial"
  - "substrate/video_visual"
---

# ReLeaf - AI/ML Analysis of Satellite Imagery

> ReLeaf leverages AI to transform satellite and drone imagery into actionable insights on deforestation and land use, empowering informed decisions for impactful environmental conservation.

[Devpost](https://devpost.com/software/releaf-ai-ml-analysis-of-satellite-imagery) · hackathon [[Hack for Humanity - 2025]]

## Facets

**mechanism** [[sensor_fusion]]
  <sub>weak: cross_origin_web</sub>
**domain** [[climate_energy]] [[developer_tools]]
**user** [[developer]]
**substrate** [[geospatial]] [[video_visual]]

**stack** flask, gcp, geocoding, github, json, mailtrap, markdown, numpy, openai, openai-api, opencv, pillow, python, tensorflow/keras

## How they structured the write-up

- 📌 introduction
- 💡 what inspired us
- 🛠️ how we built releaf
- 🌟 what we learned
- ⚡ challenges we faced
- 🌍 impact
- 🔮 future of releaf
- 📣 join us on this journey

## Body

Thumbnail Drone Footage Upload Main Page Poster 🌱 ReLeaf: Empowering Environmental Conservation with AI 📌 Introduction Deforestation and environmental degradation are among the biggest challenges our planet faces today. ReLeaf was born out of a deep passion to leverage cutting-edge technology to combat these pressing issues. By analyzing high-resolution satellite and drone imagery, ReLeaf empowers decision-makers with actionable insights, driving meaningful efforts toward conservation and sustainability. 💡 What Inspired Us The Problem Every year, millions of acres of forests are lost due to human activity. Despite having access to vast amounts of satellite and aerial data, decision-makers struggle to derive actionable insights from it. This gap between data and insight inspired us to create ReLeaf — a platform that bridges this divide with the power of artificial intelligence. Realizing the Potential As AI enthusiasts and advocates for sustainable development, we envisioned a tool that: Extracts detailed information from satellite images. Provides instant, user-friendly insights. Promotes collaborative efforts for conservation. We saw an opportunity to not only aid environmental efforts but also push the boundaries of technology’s role in driving sustainability. 🛠️ How We Built ReLeaf Technology Stack Frontend : Developed using Python and Tkinter for an intuitive, modern, and visually engaging user interface. Backend : Powered by a server-side application that integrates: A refined U-Net architecture optimized for multi-class segmentation. Python APIs for efficient server-client communication. Data Processing : Images were processed with cloud services such as Google Cloud Platform (GCP) for enhanced computational capabilities. Workflow Overview Input : Users upload high-resolution satellite or drone images. Segmentation : ReLeaf’s AI model classifies land use into 6 distinct classes: Buildings, Land, Roads, Vegetation, Water, and Unlabeled regions. Insights : Output is presented as segmentation masks and actionable analytics. Export : Users can export results and feedback data to improve future analyses. 🌟 What We Learned This project was a rewarding journey of discovery and growth. Key takeaways include: Teamwork & Collaboration : Balancing skillsets while working remotely to ensure progress was seamless. Advanced AI Techniques : Gaining expertise in loss functions (Dice Loss + Cross-Entropy) and model optimizations for large datasets. User-Centric Design : Designing a tool that’s not only powerful but also accessible to non-technical users. ⚡ Challenges We Faced Data Quality : Many publicly available datasets required significant preprocessing to ensure compatibility with our model. Computational Constraints : Training deep learning models on high-resolution images was resource-intensive. Leveraging cloud solutions helped us overcome this hurdle. Integrating Drone Footage : Scaling the solution to support dynamic inputs like drone footage introduced complexities in handling various resolutions and formats. User Interface : Ensuring a balance between sophistication and simplicity to meet the needs of diverse users was a constant design challenge. 🌍 Impact ReLeaf serves as a catalyst for meaningful change by: Simplifying complex ecological data for actionable results. Enhancing collaboration among stakeholders through transparent insights. Fostering scalable solutions that adapt to different use cases (e.g., urban planning, reforestation, water body management). 🔮 Future of ReLeaf We envision expanding ReLeaf’s capabilities to: Integrate IoT devices like ground sensors for hybrid data analysis. Include predictive modeling to forecast environmental trends. Launch an API for developers to build custom solutions using ReLeaf’s core technology. 📣 Join Us on This Journey Conservation is a collective effort. Together, we can make a difference. Explore, contribute, and collaborate with ReLeaf to drive sustainable futures. 🌿 <div