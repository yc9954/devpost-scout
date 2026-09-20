---
slug: "femicide-in-bolivia-from-news-to-narrative"
url: "https://devpost.com/software/femicide-in-bolivia-from-news-to-narrative"
title: "Femicide in Bolivia: From News to Narrative"
hackathon: "Plotly Analytics Vibe-a-Thon"
organization: "Plotly"
winner: true
words: 439
team_size: 1
has_repo: false
has_live: true
has_video: false
tags:
  - "project"
  - "domain/legal_justice"
  - "substrate/structured_db"
---

# Femicide in Bolivia: From News to Narrative

> A data-driven storytelling project that transforms news into a visual narrative of femicide in Bolivia, revealing patterns of violence and restoring visibility to women whose lives were taken.

[Devpost](https://devpost.com/software/femicide-in-bolivia-from-news-to-narrative) · hackathon [[Plotly Analytics Vibe-a-Thon]]

## Facets

**domain** [[legal_justice]]
**substrate** [[structured_db]]

**stack** gemini, plotly, plotlystudio, python

## How they structured the write-up

- inspiration
- what it does
- how i built it
- the power of visualization
- challenges i ran into
- accomplishments i'm proud of
- what i learned
- what's next for femicide in bolivia: from news to narrative

## Body

Inspiration Bolivia ranks first among 13 countries with the highest rates of physical violence against women. Local news outlets report at least one femicide case daily, yet this reality is often reduced to general statistics that are rarely updated. I wanted to build a tool that transforms fragmented news into structured, searchable data—giving visibility to patterns that are otherwise lost in headlines. What it does This solo project scrapes femicide reports from Bolivian digital newspapers, applies natural language processing (NLP) and Gemini-based extraction to identify key case details, and visualizes the results through interactive dashboards. Users can explore trends by department, relationship type, weapon used, and more—turning news into narrative and data into insight. How I built it I developed a web scraper tailored to Bolivian news sites, then used Gemini for entity extraction—capturing structured information such as victim and aggressor profiles, crime context, and location. The data was cleaned, normalized, and stored in a MongoDB database. Finally, I built visualizations using Plotly and Dash to support exploration and storytelling. The power of visualization Narrative dashboards built with Plotly allow users to move beyond raw numbers and into meaningful patterns. By combining muted palettes, interactive filters, and emotionally sensitive design, I help users explore femicide data with clarity and dignity. These visualizations make complex relationships—like motivation vs. weapon type or victim vs. aggressor age—accessible to both technical and non-technical audiences, empowering deeper understanding and action. Challenges I ran into Inconsistent reporting formats across news outlets. Missing or ambiguous data (e.g., unknown occupations, vague crime contexts). Balancing emotional sensitivity with analytical clarity in visual design. Normalizing terminology across Spanish-language sources. Accomplishments I'm proud of Built a reusable pipeline for scraping and structuring femicide data. Integrated Gemini for robust entity extraction from unstructured text. Created visualizations that reveal hidden patterns in violence. Enabled regional filtering and narrative exploration in a context with limited open data. Designed with dignity: muted palettes, respectful framing, and clear storytelling. What I learned Gemini can unlock powerful insights from unstructured news content. Visual design matters—especially when working with sensitive topics. Data normalization is key to making comparisons across cases and regions. Even in low-data environments, meaningful analysis is possible with the right tools. What's next for Femicide in Bolivia: From News to Narrative I plan to: Expand scraping to more regions and media sources. Improve entity recognition for motivations, occupations, and legal outcomes. Collaborate with local organizations to validate and enrich the dataset. Share the pipeline so others can replicate it in countries with similar challenges. This project is a step toward transforming daily tragedy into structured knowledge—and empowering communities to demand change through data. <div