---
slug: "song-lyrics-analyzer"
url: "https://devpost.com/software/song-lyrics-analyzer"
title: "Song Lyrics Analyzer for Taylor Swift"
hackathon: "Elastic Weekend with Code for Cause"
organization: "Code for Cause"
winner: true
words: 590
team_size: 1
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "substrate/financial_record"
  - "substrate/structured_db"
---

# Song Lyrics Analyzer for Taylor Swift

> We are "Swifties"

[Devpost](https://devpost.com/software/song-lyrics-analyzer) · hackathon [[Elastic Weekend with Code for Cause]]

## Facets

**substrate** [[financial_record]] [[structured_db]]

**stack** csv, kibana, pandas, python, scikit-learn

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for song lyrics analyzer for taylor swift

## Body

My data visualization in Kibana dashboard Inspiration I have this love for music. Its a such a great aspect in my life it brings me joy, happiness and I wanted to find a way to do cool analysis on music. I was also interested data science specially natural language processing. I discovered that using NLP we can find some sort of insights in language. So I wanted to look at an artist's lyrics and find some details/meanings conveyed by the lyrics. I made a small model not at all accurate though but gives some insights on the artist choice of topic for a song. What it does This Model is a way to look at the song lyrics and see if we can find some words in individual songs of an artist and then we can look how over years that topics are changing over time. Topics are like things/themes that artist is taking about in lyrics. It can be party, money, nostalgia, relationship, love, past, nature, situations, etc. We will find how those topics in the songs have changed through out there career. For example start with songs about love and my be after getting fame they had songs about money or luxury. So we will be going to plot this changes using Kibana lens graphs and visualize data with the help of Kibana instead of matplotlib or seaborn library. How we built it Collected Taylor Swift lyrics as csv file Used Pandas to make data frame Using data science (scikit-learn) filtered some words that Taylor uses rarely or particularly only for that individual songs. Excluded some words which occurs too often in our dataframe like of , the , etc. Categorized those words into topics as love , memories, etc. Updated dataframe with coloums of topic with values. 7.. Converted dataframe into a csv file imported it into Kibana. 8.. Created new indexes songs_ml and year_topics. Used Kibana lens to create visualizations. Challenges we ran into At starting I was confused it was like a alien thing to me and was how I am going to implement this new technology and make a project. Got confused over little things but things fell into place learnt some basics and asked some doubts about my obstacles to mentors and I am really happy that I made a project and did not quit after feeling overwhelmed. challenge still not able to fix - I was not able to change label of my vertical axis in my kibana graphs it automatically got it name from field / ledger as breakups actually my graphs are telling how those topics in the songs have changed through out there career over years and the second one telling majority/percentage of topics she had in her song in those years. Accomplishments that we're proud of This was my first hackathon. Really happy about my project, learnings and journey. What we learned I learned about basics of elastic search like cluster, node, index, shards, replicas etc. How to make queries, create indexes, import csv file and do data analysis on it . Learned how to use Kibana for awesome visualizations instead of matplotlib library. Also learned about scikit-learn library and little about NLP. What's next for Song Lyrics Analyzer for Taylor Swift I can improve this by making it accurate by learning more about scikit-learn and Natural Language Processing Or I can tweet and Share this with Taylor Swift But data are not at all accurate so may be she will be annoyed by my results :p <div