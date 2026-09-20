---
slug: "genomiq"
url: "https://devpost.com/software/genomiq"
title: "GenomIQ"
hackathon: "Hack the North 2024"
organization: "Hack the North"
winner: true
words: 662
team_size: 1
has_repo: true
has_live: false
has_video: false
tags:
  - "project"
  - "mechanism/benchmark_measured"
  - "domain/agriculture_food"
  - "domain/scientific_research"
  - "substrate/genomic_bio"
  - "substrate/geospatial"
  - "substrate/sensor_telemetry"
  - "substrate/structured_db"
  - "substrate/video_visual"
  - "substrate/web_dom"
---

# GenomIQ

> Automating The Code of Life

[Devpost](https://devpost.com/software/genomiq) · hackathon [[Hack the North 2024]]

## Facets

**mechanism** [[benchmark_measured]]
**domain** [[agriculture_food]] [[scientific_research]]
**substrate** [[genomic_bio]] [[geospatial]] [[sensor_telemetry]] [[structured_db]] [[video_visual]] [[web_dom]]

**stack** alphafold, chroma, cohere, flask, llm, python, vector-db

## How they structured the write-up

- inspiration
- what it does
- how i built it
- challenges i ran into
- accomplishments that i'm proud of
- what i learned
- what's next for genomiq
- dictionary

## Body

comparison between fine tuned model and normal model A dictionary is at the end for reference to biology terms. Inspiration We're at a hackathon right? So I thought, why stop at coding with 1s and 0s when we can code with A, T, G, and C? 🧬 Genetic engineering is a cornerstone of the modern world, whether its for agriculture, medicine, and more; but let's face it, it's got a bit of a learning curve. That's where GenomIQ comes in. I wanted to create a tool that lets anyone – yes, even you – play around with editing plasmids and dive into genetic engineering. But here's the kicker: we're not just making it easier, we're turbocharging it with the expressive ability of LLMs to potentially generate functional protein-coding DNA strings. What it does GenomIQ streamlines plasmid engineering by combining AI-powered gene generation with a curated gene database. It uses a custom-finetuned Cohere model to create novel DNA sequences, validated for biological plausibility via AlphaFold 2 and iterated on. Alternatively, you can rapidly search for existing genes stored in our Chroma vectordb. The platform automatically optimizes restriction sites and integrates essential genetic elements. Users can easily design, modify, and export plasmids ready for real-world synthesis, bridging the gap between computational design and practical genetic engineering. How I built it This is a Flask web app built with python, and vanilla html/css/js on the frontend. The vectordb is powered by Chroma. LLM is Cohere fine tuned on a short custom dataset included in the github repo. Restriction sites are automatically scored and sorted based on usefulness for clean insertion. Verification is performed by a local instance of Alphafold 2, which based on the provided DNA sequence will give you a structure file. I found a website that implements Prosa, a scoring metric for proteins, and built a web scrapper/bot that uploads your structure file and gathers the z-score from there. The plasmid viewer is a canvas that is updated whenever a route returns new features. The repo also includes a file for a short fine tuning dataset builder tool with a GUI, that I put together to make it easier to fine tune my model. I developed a benchmark set and performed an evaluation of the standard cohere model vs the fine tuned model, and compared their z-score across. As displayed in the image, the fine tune is much more capable of producing biologically plausible strings of DNA. Challenges I ran into Cohere api timeouts: lots of requests would not work randomly, had to use threading to check how long it was running, and be able to cut it off if it takes too long. Frontend as a whole was a big challenge, I have hardly built web apps before so this was a lot of back and forth, wondering why X element wont go to the center of the page no matter how hard I try. Accomplishments that I'm proud of Building a cool project in a day and a half :) What I learned Vector db, alphafold, genetic engineering, What's next for GenomIQ I want to evaluate what a tool like GenomIQ's place in the world could be. I want to reach out to people who would be interested in such a tool, and see what direction to take it in. There are a lot of improvements that can be made, as well as opportunity for some incredible new features. Dictionary Plasmid : Small circular ring of DNA. These are typically cut up and have new genes inserted into them. Afterwards, these plasmids are inserted into organisms like yeast, bacteria, etc who will now express the new gene. Restriction site : The zones on the plasmid where we do the cutting. Some sites are more desirable than others, typically given by uniqueness (only want to cut in one spot) and distance from other genes/features (don't want to cut up something important). Sorry if any of this seems jumbled... im really tired. <div