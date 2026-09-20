---
slug: "greencart-j9kio3"
url: "https://devpost.com/software/greencart-j9kio3"
title: "GreenCart"
hackathon: "Hack for Humanity | 2025"
organization: "Kuba Apps"
winner: true
words: 499
team_size: 1
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/cross_origin_web"
  - "domain/developer_tools"
  - "domain/retail_commerce"
  - "user/developer"
  - "substrate/sensor_telemetry"
  - "substrate/structured_db"
---

# GreenCart

> GreenCart is a Chrome extension that shows the CO2 footprint of products on Amazon, helping you shop sustainably with instant insights and easy-to-use tools.

[Devpost](https://devpost.com/software/greencart-j9kio3) · hackathon [[Hack for Humanity - 2025]]

## Facets

**mechanism** [[cross_origin_web]]
**domain** [[developer_tools]] [[retail_commerce]]
**user** [[developer]]
**substrate** [[sensor_telemetry]] [[structured_db]]

**stack** gemini, react, tailwindcss, typescript, vite

## How they structured the write-up

- about the project

## Body

About the Project Inspiration GreenCart was born out of my environmental concerns. Without realizing it, we actively contribute to the worsening of our environment with every purchase we make. I noticed a gap—most people don’t understand the impact of a product’s CO2 footprint. While it’s just a small fraction of the broader environmental challenges we face, understanding these metrics can provide valuable insight into our overall impact. Unfortunately, companies, including major platforms like Amazon, rarely include such metrics in their sales pitches. This gap inspired me to create GreenCart—a Chrome extension to help people see the environmental impact of the products they shop for online. What I Learned I learned so much during the development of GreenCart. I consider myself a backend developer, I’ve always struggled with frontend-related tasks, but this project pushed me to grow in that area. Here are some of the key things I learned: TypeScript : I became more comfortable using TypeScript, which improved the overall reliability of my code. TailwindCSS : I learned how to design responsive and clean interfaces using TailwindCSS. Gemini API : I explored the Google Gemini API and its official SDK to calculate CO2 values for products. Chrome Extensions : While I had dabbled in basic Chrome extensions before, this was my first time creating something feature-rich and impactful. How I Built It I built GreenCart using the following technologies: React : For building the user interface of the extension. TailwindCSS : For styling and ensuring a clean, user-friendly design. TypeScript : To ensure type safety and minimize errors. Gemini API : To calculate the CO2 footprint values for products. The extension extracts data from Amazon product pages, sends it to the Gemini API, and displays the CO2 footprint in an overlay on the page. Users can also view a history of analyzed products, with options to sort, filter, or export this history as a CSV. Challenges One of the biggest challenges I faced was calculating accurate CO2 values. My extension relies entirely on the Gemini API for these metrics, but I noticed some inconsistencies in the API responses when using custom prompts. While this approach was the most accessible and free option available, it is far from perfect. I believe this is an area where GreenCart can significantly improve. Another challenge was balancing my lack of frontend expertise with the need to create a polished, intuitive user experience. Learning and applying TailwindCSS helped me overcome this. Future Improvements GreenCart has room to grow. Here are some key improvements I’d like to make: Enhanced CO2 Calculation : Improve accuracy by connecting to a comprehensive database or using a more reliable API. Support for More Stores : Expand beyond Amazon and support additional online stores. Better Product Coverage : Extend support to all Amazon endpoints for broader functionality. GreenCart is a step toward making online shopping more environmentally conscious. While it’s not perfect, I hope it inspires others to consider the impact of their purchases and make more sustainable choices. <div