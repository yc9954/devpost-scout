---
slug: "mapping-19th-century-jewish-charity-in-new-york"
url: "https://devpost.com/software/mapping-19th-century-jewish-charity-in-new-york"
title: "Mapping 19th Century Jewish Charity in New York"
hackathon: "Google Maps Platform Awards"
organization: "Google"
winner: true
words: 511
team_size: 4
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "domain/immigration_refugee"
  - "user/government_staff"
  - "substrate/document_pdf"
  - "substrate/financial_record"
  - "substrate/geospatial"
  - "substrate/structured_db"
  - "substrate/video_visual"
---

# Mapping 19th Century Jewish Charity in New York

> An interactive historical map tracing the divide between poverty and philanthropy in immigrant-era Manhattan—built on Google Maps Platform from a forgotten 1899 charity ledger.

[Devpost](https://devpost.com/software/mapping-19th-century-jewish-charity-in-new-york) · hackathon [[Google Maps Platform Awards]]

## Facets

**domain** [[immigration_refugee]]
**user** [[government_staff]]
**substrate** [[document_pdf]] [[financial_record]] [[geospatial]] [[structured_db]] [[video_visual]]

**stack** google-maps, wordpress

## How they structured the write-up

- about the project

## Body

About the Project Inspiration In 1899, a young clerk named Louis Lewengood hand-delivered a booklet to the United Hebrew Charities in New York City. It contained over a thousand names and addresses of Jewish immigrants who had received aid—alongside a list of donors who made that aid possible. The document, though modest, revealed something profound: the geography of poverty and philanthropy in 19th-century Manhattan. When we, Awsm Innovations , were approached to build an interactive version of this data, we saw a unique opportunity. This wasn’t just about mapping old addresses. It was about giving voice to forgotten lives, visualizing the social divides of a rapidly growing city, and turning static archival records into something living, searchable, and human. What We Built Worthy and Unworthy is an interactive digital map that overlays more than 1,500 historic addresses from 1899 onto present-day New York City. It distinguishes between charity recipients (orange dots) and donors (blue dots), visually revealing patterns in where wealth and need existed—and rarely overlapped. Users can: Filter by recipient or donor Search by donation amount, type of charity, and year Compare historic addresses with modern locations View scanned images of the original 1899 ledger entries The project was designed with a clean, retro aesthetic to reflect the historical nature of the data, while remaining intuitive and responsive for modern users. How We Built It Frontend: We built the interactive map interface using Google Maps JavaScript API with custom styling to match the historical tone. Data Mapping: The original ledger data was digitized, cleaned, geocoded, and plotted with precision across the Manhattan landscape. Filtering & UX: We built a custom filtering engine to let users drill down into the dataset by year, category, and more—all without breaking the flow of exploration. Overlay System: Clicking a point opens an overlay with details including the individual’s name, address (then and now), donation or aid received, and a scan of the original handwritten entry. Key Technologies Used Google Maps JavaScript API Custom address geocoding and normalization Lightweight JS framework for UI interactivity Responsive, mobile-friendly design Scanned archival images hosted and served with performance in mind Challenges We Faced Geocoding 19th-century addresses: Many locations no longer exist or have been renamed, merged, or moved. We had to manually validate and adjust dozens of entries to make the dataset as accurate as possible. Balancing design with data: We wanted the map to feel vintage and respectful, without sacrificing usability or performance. Performance optimization: With over 1,500 mapped points and dynamic filters, keeping the map responsive—especially on mobile—required careful optimization. Historical ambiguity: Not every record had clear labels. Some donation types or categories were unclear or used outdated terminology. We worked closely with the client to interpret and present the data thoughtfully. What We Learned This project reinforced how powerful maps can be—not just for navigation, but for storytelling, empathy, and historical reflection. We learned how small datasets, when mapped well, can reveal large social truths. And we saw firsthand how Google Maps Platform can help bridge the gap between the past and the present. <div