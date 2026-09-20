---
slug: "test-rg4elc"
url: "https://devpost.com/software/test-rg4elc"
title: "Occupation-Shifter (by Skilllab)"
hackathon: "The European Commission's EUvsVirus Hackathon"
organization: "European Commission"
winner: true
words: 539
team_size: 3
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "domain/labor_employment"
  - "domain/media_journalism"
  - "substrate/geospatial"
---

# Occupation-Shifter (by Skilllab)

> A data driven approach to map from occupations and skills at risk to those in demand - today and during the recession. We show pathways to employment through technology.

[Devpost](https://devpost.com/software/test-rg4elc) · hackathon [[The European Commission-s EUvsVirus Hackathon]]

## Facets

**domain** [[labor_employment]] [[media_journalism]]
**substrate** [[geospatial]]

**stack** python, r, tensorflow

## How they structured the write-up

- the problem we solve
- what we did over the weekend
- the impact
- the value of the solution after the crisis
- how we built it
- the necessities in order to continue the project

## Body

The problem we solve We see that certain occupations and whole industries are at risk due to the current situation . In the mid-run, some occupations are potentially affected severely by the expected recession . In darker scenarios, the unemployment rate in the EU-27 could double by the end of the year. There is a high chance, that millions of individuals will not only have to change jobs but careers. The question is how. That's what we work on. What we did over the weekend We developed a prototype of a pathway-graph to map from occupation at risk to those in demand , building on the European Skills, Competences, Qualifications and Occupations Framework (ESCO). The graph creates direct matches to potential occupations in demand. At the same time, the graph maps pathways to desired occupations via transversal occupations , meaning feasible routes to pick up the required skills to get from occupation A to B. We worked with only a few occupations for the prototype. The impact The tool helps individuals and job services to identify, visualize, and plan either a direct transition into an in-demand occupation or work on a pathway via transversal occupations. The tool helps to make options clearer, provides orientation , and empowers the individual to grow in a changing labour market. The value of the solution after the crisis We expect this tool not to lose relevance but to gain relevance after the medical crisis around COVID-19. The exact magnitude of the recession triggered by the event is difficult to predict. However, we expect to witness the impact on labour markets for years to come. How we built it We use primarily phyton, tensorflow and R on the technical side. The base for the data model is provided by the European Skills, Competences, Qualifications and Occupations Framework. The assumptions about at-risk and in-demand occupations are evaluated qualitatively and fact-checked. Because generating a graph from semi-unstructured data is not straight forward, we apply ego-clustering techniques from NLP . This is similar to keeping only the top 1% of relations (represented as edges) between skills. We generate a graph from the skill vectors . Within that graph, we apply breadth first search, and pick out the top 5 pathways from the occupation at risk to any of the occupations in need. We then collapse all possible paths into a single subgraph, which represents the occupation shift from the occupation at risk, to any occupation in need. The necessities in order to continue the project The limitations to the model lie in the conceptual limitations of a single occupation to describe an individual . The more holistic an individual is captured (e.g. via more than one occupation), the more accurate and meaningful the mapping can be run - not from occupation to occupation but from the individual to an occupation . Our hackathon team is constituted of members of Skilllab.io - We normally work on skill-assessment technology to create rich skill-profiles and map to opportunity. We hope to integrate the prototype into Skilllab's existing technology, which would allow for faster production and an increased value proposition. This way the identified matches become more accurate, personal and meaningful as they link from the individual to the occupation. <div