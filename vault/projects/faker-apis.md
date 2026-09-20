---
slug: "faker-apis"
url: "https://devpost.com/software/faker-apis"
title: "Faker APIs"
hackathon: "The Postman API Hack"
organization: "Postman"
winner: true
words: 457
team_size: 2
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "substrate/structured_db"
---

# Faker APIs

> Multiple API Collections to get realistic dummy data from various categories. Provides easy to use visualization and ability to export data in JSON,XML,SQL,CSV,TSV formats

[Devpost](https://devpost.com/software/faker-apis) · hackathon [[The Postman API Hack]]

## Facets

**substrate** [[structured_db]]

**stack** css, csv, handlebars.js, javascript, json, postman, sql, tsv, xml

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for faker apis

## Body

All Collections of Fake APIs API visualization Inspiration While building applications, often we run into situations where we need some dummy data to test our application. We have to search the web to get the required fake data or create fake data ourselves. Many times we require data in formats like CSV or SQL but it's very difficult to find it as most APIs support only JSON. This is a time consuming tedious process that should ideally take very little time. Thus we created this project to provide a one-stop solution for all the dummy data needs What it does Our Project provides a one-stop solution where you can find APIs to get dummy data from various categories. Our intuitive visualizations allow you to convert and view data in various different formats like XML, CSV, TSV, or even SQL with just a click of a button. How we built it The first step was exploring the web for APIs in different categories. We went through hundreds of APIs online and selected the best in each category that provide rich data and as many filtering options as possible. Our core requirement was that all the selected APIs be public and free to use. After this, we came up with a design for how our visualization was going to look like and all the actions available to the user. The last step was coding the parsers and transformers for different formats and the UI templates. Challenges we ran into While all of us were familiar with Postman and had used it before, we had never used the tests and the visualization features. We learnt how to create visualizations and templates in postman. Halfway through our coding, we realised our approach was not going to work directly in postman and we had to re-write a significant part of our code. Accomplishments that we're proud of We are able to provide a solution that makes it very easy to get realistic dummy data in various formats. We believe this will be extremely helpful to the community. What we learned We learnt how to build parsers and transformers for different data formats. We learnt how to write tests for APIs in postman. We learnt how to create visualizations for data in Postman. We learnt how to use monitors and schedule it over a period of time. What's next for Faker APIs Currently we support JSON,XML,CSV,TSV and SQL formats. While this is enough for a majority of use cases, some people may require data in other formats. We plan to include support more formats later. The support for SQL is currently very minimal. We can not insert data across different tables. We plan to improve our parser to support rich SQL queries <div