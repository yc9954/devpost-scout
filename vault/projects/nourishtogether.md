---
slug: "nourishtogether"
url: "https://devpost.com/software/nourishtogether"
title: "Nourish Together"
hackathon: "GNEC Hackathon 2025 Fall - Compete For UN-Affiliated/NGO Internships & Prizes"
organization: "Global NGO Executive Committee"
winner: true
words: 764
team_size: 3
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "mechanism/retrieval_grounding"
  - "domain/agriculture_food"
  - "domain/developer_tools"
  - "domain/finance_payments"
  - "domain/transportation"
  - "substrate/geospatial"
  - "substrate/structured_db"
---

# Nourish Together

> Tech meets heart to fight hunger.

[Devpost](https://devpost.com/software/nourishtogether) · hackathon [[GNEC Hackathon 2025 Fall - Compete For UN-Affiliated-NGO Internships - Prizes]]

## Facets

**mechanism** [[realtime_stream]] [[retrieval_grounding]]
**domain** [[agriculture_food]] [[developer_tools]] [[finance_payments]] [[transportation]]
**substrate** [[geospatial]] [[structured_db]]

**stack** csv-parser, express.js, fastapi, google-maps, lovable, node.js, python, railway, react, shadcn, supabase, tailwindcss

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for nourishtogether

## Body

Nourish Together logo Inspiration Our inspiration behind creating a donor-facing solution including an interactive UK charity custom recommendation engine aligned with inputted donor interests, an embedded UK and USA food bank location map with an additional search button which finds food banks in your current location and a dashboard tracking a donation's journey was the transparency and honesty a donor needs whilst making a contribution to charitable causes such as food banks. What it does Our NourishTogether app provides the following features; An interactive UK charity custom recommendation engine which suggests charities based on donor interest. An embedded food bank location map for the UK and USA with an additional local food bank search button for any user's location and country! How we built it Our tech stack was: Frontend React (Vite + TypeScript) - for building an interactive and fast user interface. TailwindCSS + Shadcn/UI - for responsive design and clean visuals. Backend Node.js + Express.js - lightweight API server. csv-parser - for efficiently loading and querying charity data. Supabase PostgreSQL Database - built the web application by providing essential backend services like a database and for secure frontend-backend communication. Python + FastAPI (Charity Recommender API) - Uses a Sentence Transformer to embed charity descriptions and store them in a FAISS index for fast, natural-language charity search. Deployed via Railway with CI/CD. API live at Recommender-FastAPI ( https://recommender-fast-api-production.up.railway.app/ ) and docs are at ( https://recommender-fast-api-production.up.railway.app/docs ). Data cleaned_charity_data.csv - dataset of charities with activity descriptions. UK Food Banks location data (detailed below in citations) Challenges we ran into We faced a few challenges including; Backend-frontend connection - implementing a smooth communication between the backend API and the frontend UI was challenging due to CORS restrictions, differing local server ports and API query handling. Whilst building the custom recommendation engine, we found that embeddings and the index were being rebuilt every time the script ran. This caused slow performance and unnecessary API calls, slowing down development and testing. Navigating API deployment using new technologies such as Railway. Accomplishments that we're proud of We are proud to build a full-stack end-to-end app with both a frontend and backend, with interactive capabilities that will help donors understand their donation's journey, tailor charities to donate to by their interests and also help them select food banks local to them! What we learned During this project, we gained valuable experience working with several tools and techniques: Meld - we learnt how to effectively use Meld for visualising and resolving merge conflicts, which greatly improved our Git workflow and collaboration. Supabase - we got hands-on experience with Supabase as a backend service, managing data storage, authentication and real-time updates. Prompting Lovable effectively - explored crafting effective prompts to interact with Lovable to create our user interface, improving the way we can leverage language models in future iterations. We learned how dependency management affects API deployment - Conda couldn’t install some pip-only packages like FastAPI and Uvicorn. Fixing the YAML structure and separating pip dependencies taught us the importance of proper environment setup for smooth deployment. What's next for NourishTogether To further improve user experience and semantic accuracy, our future plans are: Add personalised recommendations based on user preferences/history. Add explainability - short text explaining why a charity was recommended. Integrate multilingual support for charity search. Add user feedback loop to improve the recommendations over time. Our custom recommendation agent uses embeddings for semantic search, and adding a lightweight LLM would make recommendations more context-aware, conversational and user-friendly. We would also extend beyond UK charities by using an open registry or Charity Navigator API for global expansion and access to all. Data Sources Citations UK Charity Register - Charity text data from the Charity Commission for England and Wales Full Register Download ( https://register-of-charities.charitycommission.gov.uk/en/register/full-register-download ). UK Food Banks location data - This dataset was custom-compiled from publicly available UK charity and food aid data to create a unified reference for the Charity Recommender API. It includes details such as food bank names, locations, contact info, charity registration links, and network affiliations. Data was collected from open registers and verified sources including: Charity Commission for England and Wales OSCR – Scottish Charity Register Trussell Trust Food Bank Directory Independent Food Aid Network (IFAN) Publicly available local charity websites and social media pages. The dataset was aggregated and structured with assistance from ChatGPT for research and development purposes, ensuring ethical use of open data only. US Food Bank Master Dataset – Compiled with assistance from ChatGPT using publicly available information from multiple open sources (e.g., national and regional food bank directories). <div