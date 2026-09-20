---
slug: "public-libraries-peer-to-peer-performance-analysis"
url: "https://devpost.com/software/public-libraries-peer-to-peer-performance-analysis"
title: "Public Libraries Peer-to-Peer Performance Analysis"
hackathon: "Hex-a-thon"
organization: "Hex"
winner: true
words: 333
team_size: 3
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/vision_ocr"
  - "domain/finance_payments"
  - "domain/supply_logistics"
  - "substrate/sensor_telemetry"
---

# Public Libraries Peer-to-Peer Performance Analysis

> Public libraries often work with limited resources and need grants which require writing grants and data analysis for advocacy. This tool democratizes insights and data narratives for libraries.

[Devpost](https://devpost.com/software/public-libraries-peer-to-peer-performance-analysis) · hackathon [[Hex-a-thon]]

## Facets

**mechanism** [[vision_ocr]]
**domain** [[finance_payments]] [[supply_logistics]]
**substrate** [[sensor_telemetry]]

**stack** ai, dbt, groq, hex, llama, poltly, python, snowflake, sql

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of

## Body

Overview Page Inspiration Public libraries are struggling. Many operate with flat or shrinking budgets, outdated collections, and skeleton staff, yet are expected to do more every year. With limited resources, libraries struggle to: Advocate effectively for their community's needs Know whether they are falling behind due to lack of resources Improve with what they have Libraries rely on taxes and grants to fund themselves. Writing grants and advocating for resources requires explaining their needs—which means understanding how they're performing compared to their peers. But data analysis requires resources, creating a vicious cycle where understaffed libraries are disproportionately affected. IMLS provides a Search and Compare tool using a Tableau-based platform that allows libraries to view their data and basic charts. While it enables comparison by displaying raw data side-by-side, its capabilities are limited, requiring users to do most of the analytical heavy lifting. With this Hex Dashboard , we've done the heavy lifting for them. Our aim is to enable library staff to better understand their performance through the lens of their true peers by providing automated metrics, data-driven narratives, and natural language insights they can access simply by asking questions. What it does Allows libraries to find their true peers based on customizable criteria and similarity score calculation Dynamically builds performance metrics for the selected peer group and enable per capita analysis Generates data-driven narratives by calling LLM APIs with relevant metrics and context How we built it Data Warehousing: Snowflake Data Modeling: dbt + Semantic Modeling (in Hex) Dashboarding: Hex (Notebook, Agent, and Threads) Languages: SQL, Python LLM: Groq API with llama-3.1-8b-instant Challenges we ran into Getting the data and preprocessing, eventually built a Snowflake data warehouse to allow scaling Understanding the problem space deeply enough to design the right solution for technical and non-technical users Choosing the optimal tech stack for scalability and ease of use Accomplishments that we're proud of Building a tool that's both useful and scalable for real-world library needs Making complex analytics accessible through natural language <div