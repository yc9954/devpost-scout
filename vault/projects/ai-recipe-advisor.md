---
slug: "ai-recipe-advisor"
url: "https://devpost.com/software/ai-recipe-advisor"
title: "ChefMate"
hackathon: "RAG 'n' ROLL Amp up Search with Snowflake & Mistral"
organization: "Snowflake"
winner: true
words: 312
team_size: 3
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/retrieval_grounding"
  - "domain/agriculture_food"
  - "substrate/structured_db"
---

# ChefMate

> From fridge to fork – your guide to sustainable, portion-perfect cooking.

[Devpost](https://devpost.com/software/ai-recipe-advisor) · hackathon [[RAG -n- ROLL Amp up Search with Snowflake - Mistral]]

## Facets

**mechanism** [[retrieval_grounding]]
**domain** [[agriculture_food]]
**substrate** [[structured_db]]

**stack** cortexsearch, github, mistral.ai, python, streamlit

## How they structured the write-up

- about the project
- inspiration
- how we built it
- challenges we faced

## Body

ChefMate – Your perfect kitchen companion. Project Story: ChefMate About the Project ChefMate is a chatbot designed to help users create perfect meals tailored to their ingredients, specifically for one person. The inspiration for this project stems from my personal journey of living alone. I often struggled with cooking the right portion sizes, which led to wasted food and money. I wanted to solve this problem not just for myself but for others facing the same challenge. The primary goal of this project is to reduce food waste by suggesting recipes based on available ingredients while providing accurate portion sizes for a single serving. ChefMate offers users the recipe details, ingredient quantities, the cuisine type, and step-by-step cooking instructions. Inspiration The idea for ChefMate was born out of a very personal need. Living alone, I found it difficult to estimate the right amounts of ingredients for meals, leading to overcooking and discarding leftovers. I realized that many others share this problem, and with rising concerns about food waste globally, I saw an opportunity to create a solution that is both practical and impactful. How We Built It Technologies Used: RAG (Retrieval-Augmented Generation): Used to enhance the chatbot's ability to generate accurate and diverse recipe suggestions. Snowflake: Leveraged for data storage and efficient querying of recipe and ingredient databases. Mistral Model: Implemented for natural language understanding and conversational responses. Process: Gathered a database of recipes with ingredient details, cuisine types, and cooking instructions. Designed the chatbot to accept user input of available ingredients and portion size. Developed a recommendation engine to match recipes with user-provided inputs. Added features to calculate exact ingredient quantities for one serving. Challenges We Faced Ingredient Matching: One of the initial hurdles was designing a system that could accurately match user inputs with recipes, even when ingredients were listed in different formats. Portion Calculations: Adapting recipes for single <div