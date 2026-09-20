---
slug: "peer-reviewers-app"
url: "https://devpost.com/software/peer-reviewers-app"
title: "Peer Reviewers App"
hackathon: "Azure AI Hackathon"
organization: "Microsoft"
winner: true
words: 288
team_size: 2
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "domain/scientific_research"
  - "user/educator_student"
  - "user/researcher"
  - "substrate/document_pdf"
---

# Peer Reviewers App

> A web application for recommending peer reviewers for academic journals using document similarity

[Devpost](https://devpost.com/software/peer-reviewers-app) · hackathon [[Azure AI Hackathon]]

## Facets

**domain** [[scientific_research]]
**user** [[educator_student]] [[researcher]]
**substrate** [[document_pdf]]

**stack** angular.js, asp.net, azure, c#, expertai, pdfpig

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for peer reviewers app

## Body

Inspiration Peer Reviewers App is a web application that uses AI knowledge extraction to perform document similarity to help recommend peer reviewers for academic and scholarly journals and articles. A possible peer reviewer for a submitted scholarly article or paper is a researcher or academic with experience in the research area of the submitted research paper. Using knowledge extraction and document similarity we can compare research papers of academics to determine possible reviewers. The inspiration for this project is based on a university project I worked on where I used the Bag of Words approach to search indexed documents in a search store. In this application we take advantage of Expert AI Keyphrase API to extract key phrases from submitted research papers, the topics and main sentences are used to build an intelligent query to retrieve the best matching document from a document store built using Azure Cognitive Search What it does It uses knowledge extraction and document similarity to compare research papers of academics to determine possible reviewers. How we built it We built the project using Angular for the application UI, PDFPig for extracting content from the documents. Expert AI for key phrase extraction and topic classification and Azure Cognitive Search for indexing the search documents. Challenges we ran into The main challenge of this project was extracting content from the pdf files. It took a while to find an open source library for that as most of the options out there required a paid license. Accomplishments that we're proud of First online hackathon!! What we learned Expert AI for knowledge extraction Azure Cognitive Search for indexing and searching documents. What's next for Peer Reviewers App Open source, tutorial on document similarity and cloud indexes. <div