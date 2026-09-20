---
slug: "finance-dashboard"
url: "https://devpost.com/software/finance-dashboard"
title: "Finance Dashboard"
hackathon: "HackSwift 2024"
organization: "hackswift"
winner: true
words: 399
team_size: 2
has_repo: false
has_live: false
has_video: true
tags:
  - "project"
  - "user/general_public"
  - "substrate/structured_db"
---

# Finance Dashboard

> We aim to simplify the process of obtaining financial information for public companies. Instead of directly going to the SEC filings or enterprise websites, we simplify the process with our project.

[Devpost](https://devpost.com/software/finance-dashboard) · hackathon [[HackSwift 2024]]

## Facets

**user** [[general_public]]
**substrate** [[structured_db]]
  <sub>weak: financial_record, sensor_telemetry</sub>

**stack** dash, edgarapi, flask, numpy, pandas, plotly, sqlalchemy, sqlite

## Body

HackSwift 2024 Hackathon: Ethan Chan, Vincent Chang Inspiration : The inspiration came from our personal journey with finance and investing with traditional sites such as MSN Stocks, Wallmine, etc., that often provide too much information. Consumers are often not interested in knowing the 50 different stock metrics for a specific company. Instead, they are interested in a few key important financial numbers and want them delivered in a way that is easily digestible. What it does : Our web application aims to simplify the process of obtaining financial information for public companies. Instead of directly going to the SEC filings or enterprise websites that make people feel overwhelmed, we simplify the process with our project. How we built it : Data is aggregated from the SEC via their EDGAR API (that is open to the public) and then imported into SQLite database. However, the current number of public companies that the database contains is limited, primarily because there isn't a standardization among what general ledger (GL) accounts each company has as well as their names (ex. one company might have "cost of goods sold" and another company might have "cost of revenue", even though these two effectively represent the same costs). Because of this, custom methods must be built and then tested to see if it will work for a select company. The web application itself is built on Flask and Plotly/Dash. Challenges we ran into : The biggest challenge we ran into was integrating the Dash application as part of a larger Flask application. There is little to no documentation regarding how to embed a Dash app (possibly because Dash has their own enterprise software that they offer), so we had to hack our way through and eventually were able to integrate the two. Accomplishments that we're proud of : We're proud to have been able to build a web application that supports user login, password resets, and successfully provide consumers with what we believe to be an easy way of viewing financial data. What we learned : The biggest and most important thing we learned is overcoming challenges and being able to come up with innovative solutions. What's next : Next steps would be to: Continue adding more public companies, as well as other important charts. API/Data Download to Excel for custom financial modeling and valuation. Macroeconomic data utilizing the FRED API (Federal Reserve Economic Data) <div