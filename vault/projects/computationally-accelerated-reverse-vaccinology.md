---
slug: "computationally-accelerated-reverse-vaccinology"
url: "https://devpost.com/software/computationally-accelerated-reverse-vaccinology"
title: "Computationally Accelerated Reverse Vaccinology"
hackathon: "COVID-19 Global Hackathon 1.0"
winner: true
words: 508
team_size: 1
has_repo: false
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/on_device_local"
  - "domain/mental_health"
  - "domain/scientific_research"
  - "substrate/financial_record"
  - "substrate/genomic_bio"
  - "substrate/geospatial"
  - "substrate/video_visual"
---

# Computationally Accelerated Reverse Vaccinology

> Accelerating process of reverse vaccination by predicting virus mutation and advancing modeling of protein to protein interaction

[Devpost](https://devpost.com/software/computationally-accelerated-reverse-vaccinology) · hackathon [[COVID-19 Global Hackathon 1.0]]

## Facets

**mechanism** [[on_device_local]]
**domain** [[mental_health]] [[scientific_research]]
**substrate** [[financial_record]] [[genomic_bio]] [[geospatial]] [[video_visual]]
  <sub>weak: structured_db</sub>

**stack** c++, caffe, python, pytorch

## How they structured the write-up

- inspiration
- what it does
- how i built it
- challenges i ran into
- accomplishments that i'm proud of
- what i learned
- what's next for computationally accelerated reverse vaccinology

## Body

Traditional vaccinology path and its challenges reverse vaccinology cov-2 database Inspiration Traditional vaccinology is based on 3 stages: isolate, inactivate, and inject weakened or dead microbes. There are challenges with the approach: Cannot be used with pathogens that cannot be cultivated in vitro (in the lab). Often leads to side effects such as sickness. Takes a very long time to make Reverse Vaccinology uses a microbe’s genome, or part of its genome to create a vaccine. Here are a few notes about the approach: The solution uses the idea that certain surface proteins trigger immune responses If the right immune responses are created then that protein can be used for vaccines Reverse vaccinology can be accelerated by computational means. We have identified 3 processes that map well with RNA based vaccines: 1- Narrow Down Variables : Computationally evaluate which genes in an RNA can be coding for proteins that are on the surface of the virus or bacteria 2- Reduce the Problem Space : The rapid identification of host proteins targeted by viral proteins during infection provides significant insights into mechanisms of viral protein function. The resulting discoveries often lead to unique and innovative hypotheses on viral protein function. However, protein-to-protein interaction is complex and time consuming. Computational approaches have been proposed to accelerate this effort, such as in the work by Zhou et al , but the accuracy of the models leaves much room for improvement. 3- Bound Variation in the Problem space : Another challenge is that viruses mutate at different rates. Some mutate at a very high rate, which makes any lengthy development process ineffective. Predicting the mutation can further optimize landing vaccines ahead of the virus’s new formation each season, and thus having more effective immunization. What it does Develops computational tools to model pathogen interaction with cell protein, enabling faster vaccine development process How I built it Using Covid-19 strains , develop a model to predict COVID-19 mutation process. Using the predicted strains, narrow down the reverse vaccination problem space by predicting PPI (protein-protein interaction) and thereby shorten the vaccine development process. How I built it Challenges I ran into 1- the problem statement is not presented well for computational challenges. There are a number of publications on using computational tools to accelerate the development process, but we did not find an in depth analysis of why certain tools were used. In a number of occasions, we found out that latest development in other field of computer science, i.e. image processing, on device machine learning and cloud rendering can be of major help for genome therapy. 2 - The datasets are not in a common format and hard to parse 3- Disagreement on the problem space: There are different claims on what the top priority issue is in accelerating reverse vaccinology. 4- Lack of public tools: Each firm or university lab develops their own tools and there is no consolidated open source public platform for genome therapy Accomplishments that I'm proud of What I learned What's next for Computationally Accelerated Reverse Vaccinology <div