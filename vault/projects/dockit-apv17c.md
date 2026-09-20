---
slug: "dockit-apv17c"
url: "https://devpost.com/software/dockit-apv17c"
title: "DockIt"
hackathon: "QuantumHacks"
organization: "Quantumhacks"
winner: true
words: 1039
team_size: 2
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/vision_ocr"
  - "domain/civic_government"
  - "user/small_business"
  - "substrate/document_pdf"
  - "substrate/geospatial"
  - "substrate/regulation_legal_text"
  - "substrate/structured_db"
---

# DockIt

> An an AI-powered platform helping small businesses discover and manage city-specific licenses, permits, documents, and compliance requirements.

[Devpost](https://devpost.com/software/dockit-apv17c) · hackathon [[QuantumHacks]]

## Facets

**mechanism** [[vision_ocr]]
**domain** [[civic_government]]
**user** [[small_business]]
**substrate** [[document_pdf]] [[geospatial]] [[regulation_legal_text]] [[structured_db]]

**stack** ai, css3, generative, google-gemini, html5, javascript, jspdf, ocr, pdf.js, postgresql, react, rest-api, supabase, tesseract.js

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for dockit

## Body

Landing Page Dashboard View with comprehensive summary of license details, their expiry and compliance score. Requirements section with a list of all required licenses needed. Inspiration We started with a pretty simple question: If someone wanted to open a food truck tomorrow, would they actually know every license, permit, inspection, and certificate they need before they can start serving customers? We realized that finding the answer is not that simple. The information is spread across different government websites and authorities, and the requirements can change depending on the type of business and the city. For a small business owner, this can mean spending hours searching through websites, comparing information, and trying to understand complicated rules. It gets even harder when the business expands to another city. They should not have to go through the whole process again just to figure out what is different. That is what gave us the idea for DockIt . We wanted to make compliance something that a business owner can actually understand and manage without needing to be an expert in regulations. What it does DockIt starts with two simple things: what your business is and where you operate. Based on that, it creates a checklist of the licenses, permits, inspections, and other requirements that apply to your business and puts everything in one place. One of the features we are most excited about is our Smart Diff system. For example, if a food truck is already operating in New York and the owner wants to expand to another city, DockIt compares the existing requirements with the requirements for the new city. Things that are already satisfied or can be reused are not shown as completely new requirements. Instead, the owner can focus on what they actually need to do for the new location. The platform also lets users track the status of their requirements, upload documents, extract expiry dates using OCR, fill official application forms, and see their overall compliance status across different cities. How we built it We built DockIt as a full stack web application. The frontend handles the onboarding process, compliance checklist, document uploads, form filling, map view, and dashboard. For the backend, we built the logic for handling businesses, cities, requirements, documents, authorities, and compliance status. We used Supabase as our database and structured data layer. The requirement discovery system filters requirements based on the business type and location and then combines them into one checklist. For the Smart Diff feature, we compare the requirements of a new city with the requirements that the business already has. This lets us identify which requirements are actually new. We also added OCR for uploaded documents so that information such as expiry dates can be extracted and used to update the compliance status. For form filling, we worked with actual official PDF templates and mapped the required business information to the appropriate fields to generate a completed application packet. We also use AI to help with interpreting and organizing information, but we wanted the core compliance information to stay structured and traceable instead of relying completely on AI generated answers. Challenges we ran into One of the biggest challenges was figuring out how to structure compliance information. A requirement is not just a name. It can depend on the business type, city, authority, jurisdiction, renewal period, document, and source. Some requirements can also apply across multiple locations while others are specific to one city. This made the Smart Diff feature more complicated than it initially seemed. We had to figure out how to tell the difference between a requirement that is actually new and one that the business already satisfies. Document processing was another challenge. Uploaded documents can have different layouts and formats, so extracting information like expiry dates and connecting it to the right requirement was not always straightforward. We also learned that using AI for compliance needs to be handled carefully. A confident but incorrect answer can cause more problems than having no answer at all. Because of that, we focused on combining AI with structured compliance data and validation. Accomplishments that we're proud of We are proud that DockIt is more than just a list of licenses. We built a complete workflow that goes from business information to requirements, Smart Diff, documents, forms, and compliance tracking . The Smart Diff feature is probably the part we are most proud of because it solves a problem that comes up naturally when a business expands. Instead of giving the owner another huge checklist, DockIt helps them focus on what has actually changed. We also managed to bring requirement discovery, OCR based document tracking, official PDF form filling, city based visualization, and compliance scoring together in one platform. What we learned One of the biggest things we learned is that building an AI product does not mean putting an LLM everywhere. For a project like this, the underlying data matters just as much. We had to think about how requirements are stored, where the information comes from, how it is retrieved, and how we can make the results reliable. We also realized that a question that sounds simple, like "What do I need to open my business?" , can actually involve a lot of different factors such as business type, location, authority, documents, and deadlines. Most importantly, we learned to build around the actual problem and user workflow instead of just building around the technologies we wanted to use. What's next for DockIt Right now, our prototype demonstrates the main workflow, but there is a lot more we want to do with it. We want to add more business types and cities, improve how we verify and update the compliance information, and make DockIt more proactive about upcoming renewals and changes in requirements. We also want to improve document verification and make the application process more automated. Eventually, we want DockIt to become something a business owner can keep using throughout the life of their business, instead of something they only use when they are first trying to figure out their licenses. Our goal is simple: A business owner should be able to focus on running their business without spending hours trying to figure out what they need to stay compliant. <div