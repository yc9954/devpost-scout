---
slug: "nobeeswax"
url: "https://devpost.com/software/nobeeswax"
title: "NoBeesWax"
hackathon: "Nosu AI Hackathon $11,300+ in prizes"
organization: "nosu"
winner: true
words: 370
team_size: 4
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/cross_origin_web"
  - "mechanism/on_device_local"
  - "mechanism/retrieval_grounding"
  - "domain/retail_commerce"
  - "user/government_staff"
  - "substrate/structured_db"
---

# NoBeesWax

> A one-stop solution to find the best coupon codes and even generate your own! And guess what? We don't steal any affiliate money.

[Devpost](https://devpost.com/software/nobeeswax) · hackathon [[Nosu AI Hackathon -11-300- in prizes]]

## Facets

**mechanism** [[cross_origin_web]] [[on_device_local]] [[retrieval_grounding]]
**domain** [[retail_commerce]]
**user** [[government_staff]]
**substrate** [[structured_db]]

**stack** clerk, firebase, flask, google-colab, llama, ollama, qwen, react, reddit, vite

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for nobeeswax

## Body

Landing page Coupon generator Dashboard Community Leaderboard Inspiration To take a stand against the treacherous giant that steals creators' affiliate data. What it does Dynamically fetches coupon and gift card data from the internet (currently using r/coupons ). Features an AI-powered coupon generator (fine-tuned LLaMA 3.1 on a custom dataset) that generates coupon codes for your favorite brands. Includes a community feature that allows users to upload coupons to our site in exchange for points. Provides a dashboard to track your coupon finds and usage. Offers a leaderboard to compare user points. How we built it Frontend: React + Vite Backend: Flask Authentication: Clerk Database: Firebase Data Fetching: Reddit API + Qwen/Qwen2-VL-7B-Instruct via Nebius for scraping coupons for the dataset and dynamically accessing coupons. Model Fine-tuning: Unsloth's Colab notebook to fine-tune LLaMA 3.1 Model Hosting: Ollama for locally hosting the fine-tuned model Challenges we ran into Data scraping: There was no pre-existing dataset of coupon codes/gift cards for fine-tuning an LLM. Scraping coupon websites proved difficult as they use dynamic pages (making pytesseract unusable), and frequent requests led to IP bans (ruling out Selenium ). Fine-tuning the LLaMA 3.1 model on a completely custom dataset presented challenges, including adjusting hyperparameters for optimal performance. Limited time to implement all features meant prioritizing the most critical components of the project. Accomplishments that we're proud of Actually somehow tying up all the loose ends of the project and delivering a working project. Despite the complexities of scraping dynamic pages and handling IP bans, we found creative solutions to gather valuable coupon data. Seamlessly integrated multiple APIs (Reddit, Qwen, Clerk) to build a cohesive and dynamic system. What we learned Gained experience working with unfamiliar technologies. Improved our skills in web scraping. Learned how to create API calls and integrate multiple components (frontend, backend, and model) into a cohesive system. What's next for NoBeesWax Building a Retrieval-Augmented Generation (RAG) system using fetched data from the internet and user-submitted coupons, feeding it back to the LLM via Firebase as a vector database. Collaborating with brands to source coupons directly for our site. Develop a browser extension to automatically apply the best coupon codes at checkout. Identify additional sources for extracting coupons apart from reddit. <div