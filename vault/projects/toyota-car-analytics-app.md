---
slug: "toyota-car-analytics-app"
url: "https://devpost.com/software/toyota-car-analytics-app"
title: "ToyoTrends"
hackathon: "HackUTD 2024: Ripple Effect"
organization: "hackutd"
winner: true
words: 533
team_size: 4
has_repo: false
has_live: false
has_video: true
tags:
  - "project"
  - "domain/climate_energy"
  - "domain/transportation"
  - "user/developer"
  - "substrate/code_repository"
  - "substrate/structured_db"
  - "substrate/video_visual"
  - "substrate/web_dom"
---

# ToyoTrends

> ToyoTrends is a powerful web application designed for Toyota engineers to visualize and interpret fuel efficiency and carbon emissions data for both Toyota vehicles and competitor vehicles.

[Devpost](https://devpost.com/software/toyota-car-analytics-app) · hackathon [[HackUTD 2024- Ripple Effect]]

## Facets

**domain** [[climate_energy]] [[transportation]]
**user** [[developer]]
**substrate** [[code_repository]] [[structured_db]] [[video_visual]] [[web_dom]]

**stack** carsxe, chart.js, css, html, javascript, openai, react, sambanova

## How they structured the write-up

- key features
- libraries and technologies
- examples of data processing
- code structure
- development timeline
- installation and setup
- future improvements
- license
- contact

## Body

Landing Page for ToyoTrends Car Statistics Lookup Car Comparison over Time Manufacturer Comparison over Time Toyota x HackUTD ToyoTrends ToyoTrends is a powerful web application designed for Toyota engineers to visualize and interpret fuel efficiency and carbon emissions data for both Toyota vehicles and competitor vehicles. This tool provides actionable insights, helping engineers gain a competitive edge in the automotive industry. Key Features Immersive Intro Animation : Engages users with a visually appealing introduction. Reactive Web Components : Ensures a dynamic and responsive user experience. Data Analysis on Large Datasets : Processes vast amounts of data efficiently for actionable insights. Comparison Tools : Enables side-by-side analysis of multiple vehicles. Future Predictive Algorithms : Offers forecasts based on historical data trends. AI Navigation and Information Assistance : Utilizes SambaNova's AI API for a chatbot to streamline user interactions. Libraries and Technologies React.js : Framework for building the user interface. Chart.js : For advanced data visualization. queryString : Simplifies data processing and URL parameter manipulation. CarsXE : Generates accurate and high-quality vehicle images. SambaNova AI : Provides AI-driven chatbot assistance for seamless navigation. Examples of Data Processing Large Dataset Management : Organizes extensive datasets to enable quick access and computation. String Manipulation : Processes and formats vehicle data to gather and present images effectively. Code Structure The project is organized as follows: toyota-analytics-app |-- public | |-- data | |-- carImages | | |-- Toyota_CAMRY.png | | |-- Toyota_COROLLA.png | |-- manufacturers | | |-- Toyota | | |-- CAMRY | | |-- COROLLA | |-- filter.py | |-- uniqueCars.py |-- src | |-- assets | |-- components | | |-- charts | | |-- tables | |-- features | | |-- services | | |-- carComparison | | |-- dataProcessing | |-- hooks | |-- pages | |-- utils | |-- App.js | |-- App.css | |-- index.js | |-- index.css |-- .env |-- .gitignore |-- README.md Key Files and Directories public/data : Stores vehicle images and manufacturer-specific data. filter.py : Script to filter dataset information. uniqueCars.py : Script to identify unique vehicle entries. src/assets : Contains static assets. src/components : Includes reusable UI components like charts and tables. src/features : Houses core application features like car comparison and data processing. src/hooks : Custom React hooks for managing app state. src/utils : Utility functions for common operations. Development Timeline The entire project was completed in under 24 hours as part of HackUTD XI . Contributors Brandon Robertiello br@ou.edu LinkedIn Melissa Ng melissa.j.ng-1@ou.edu LinkedIn Lucas Ho lucas.ho-1@ou.edu LinkedIn Bryan Ho bryan.v.ho-1@ou.edu LinkedIn Installation and Setup Clone the Repository : git clone https://github.com/your-repo/toyota-analytics-app.git cd toyota-analytics-app Install Dependencies : npm install Environment Variables : Create a .env file in the root directory and populate it with necessary API keys and configurations (e.g., CarsXE and SambaNova). Run the Application : npm start Access the app at http://localhost:3000 . Future Improvements Enhanced predictive analytics for carbon emissions trends. Integration with more AI tools for advanced insights. Expansion to include more competitor data. License This project is open-source and available under the MIT License. Feel free to fork and contribute! Contact For more information, reach out to any of the contributors or submit an issue on the GitHub repository. <div