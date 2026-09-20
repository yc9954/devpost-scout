---
slug: "symptomsearch"
url: "https://devpost.com/software/symptomsearch"
title: "SymptomSearch"
hackathon: "Funathon"
organization: "Youth Pioneers in STEM"
winner: true
words: 378
team_size: 1
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "domain/health_clinical"
  - "substrate/web_dom"
---

# SymptomSearch

> Application where you input your symptoms if you are sick and it tells you what disease(s) you may have

[Devpost](https://devpost.com/software/symptomsearch) · hackathon [[Funathon]]

## Facets

**domain** [[health_clinical]]
**substrate** [[web_dom]]

**stack** java, jsoup

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for symptomsearch

## Body

Logo for SymptomSearch Inspiration Searching google for "What disease has fever, headache, vomiting, diarrhea, and abdominal pain" can be pretty rigorous and long with multiple overwhelming results. I wanted to make an application that gives short, concise information about what disease you may have/contracted with just the symptoms you told it What it does A user, that is primarily sick, inputs the symptoms that they are experiencing, and the application filters through all the data, taken off a website, and gives the top 5 diseases it may think the user has based on the information provided. How we built it I decided to challenge myself and only use Java for this project. For the medical data on the diseases and symptoms, I used JSoup to web scrape all the relevant data off a website. I then began building the UI portion of the application with Java swing. I then mapped all the symptoms and data that were processed in the algorithm into the UI. Challenges we ran into A major challenge I ran into was collecting and scraping all the medical data. I was originally going to manually go through each disease and pick out the relevant information. I realized that would take too long since there were over 2500 diseases with at least 5 symptoms on each page. In order to fix this issue, I decided to use a Java web scraper called JSoup to scrape all the symptoms on each page for each disease. Accomplishments that we're proud of One accomplishment I'm proud of is finishing this whole project in Java and not another language like HTML, CSS, JS or REACT.js. I'm very proud of this project especially being the first project I've done for hackathons like this What we learned I learned a lot more about Java swing in this project. What's next for SymptomSearch The next step for SymptomSearch is to make a better UI since this is one of my first times making a UI on this scale. Website for all the medical data: link Note: The "alpha_a" portion of the domain refers to the starting letter of every disease on that page. To search through all the diseases, you would have to change the letter after to underscore. E.g: "alpha_b", "alpha_c" <div