---
slug: "cbre-project"
url: "https://devpost.com/software/cbre-project"
title: "TrustEstate AI"
hackathon: "HackUTD 2025: Lost in the Pages"
organization: "hackutd"
winner: true
words: 775
team_size: 4
has_repo: false
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "domain/education"
  - "domain/media_journalism"
  - "user/general_public"
  - "substrate/geospatial"
  - "substrate/video_visual"
---

# TrustEstate AI

> TrustEstate AI is your go-to for real estate. We use AI and enterprise-grade trust verification to deliver market insights and property analytics you can actually trust. Make smarter, faster decisions

[Devpost](https://devpost.com/software/cbre-project) · hackathon [[HackUTD 2025- Lost in the Pages]]

## Facets

**mechanism** [[realtime_stream]]
**domain** [[education]] [[media_journalism]]
**user** [[general_public]]
**substrate** [[geospatial]] [[video_visual]]

**stack** google-gemini, google-maps, react, recharts, shadn, sonner, tailwind, typescript, vite

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for cbre project

## Body

Home Page AI Property Filter Saved Compare Analytics Inspiration We came up with this concept since we saw how hard it is for consumers to find reliable real estate information online. Most property listings and platforms give users a lot of information, but they don't really say whether that information is reliable or even current. We wanted to build a platform that combines CBRE's data with AI that can do live fact-checking so that everyone can be sure of the choices they make when it comes to real estate. We wanted to make property research not just easier, but also smarter and safer. What it does Our app is a full-featured real estate helper that helps you find and trust properties. People may find properties using a Google Map interface that is both interactive and easy to use. Each property profile has more information than what is available to the public, thanks to CBRE's data. This includes prices, features, photos, past sales, and more. The app has a smart AI assistant that can answer inquiries, summarize insights or property histories, and, most significantly, check facts using real Google Search results. Each property has a trust or confidence score that shows how well internal data matches outside sources like news, public records, and other listing sites. The experience is engaging, open, and focused on helping consumers not only find out which homes are available, but also which ones they can trust. How we built it We used React to build the front end and the Google Maps API to make browsing smooth and engaging on any device. We use a properties.json file to imitate our property data. We use browser localStorage to keep track of user preferences and saved attributes. This makes it easier to create personalized experiences without needing to log in to the backend for the demo. We included the Gemini AI model for intelligence. It can read our internal property data and use tool-calling to search Google and confirm facts in real time. The assistant looks at all the sources and gives each property a trust score. It then shows the results with comprehensive explanations and visual meters. We put a lot of thought into the UI design and worked hard to make sure that all the complicated analysis, chat interactions, and data checks are shown simply, with nice graphics and fluid animations. Challenges we ran into It was really hard to get Google Maps, Gemini AI, and live search APIs to operate together quickly and without any problems. We had trouble showing consumers a lot of complicated data (such as source checks and trust scores) without making the interface too busy or confusing. Performance was really important, especially making sure that maps loaded quickly and AI analysis showed up promptly, even for people on slower networks or mobile devices. Finally, since CBRE data is private, we worked hard to make realistic property profiles and make sure the AI verification stages felt real and important. Accomplishments that we're proud of We're glad that our app doesn't just offer real estate listings; it also tells users how much they can trust the information about each property. The AI-generated trust scores and verification logs work perfectly with the gorgeous map interactions and easy-to-read property profiles. Users can really use the app by asking questions, saving their favorite properties, and easily keeping track of changes. Our experience goes beyond just a basic prototype; it shows what can be done when you combine high-quality data with sophisticated AI in a design that puts the user first. What we learned This project taught us that users demand more than just access to a lot of data; they also want certainty and clarity and a trustworthy product. It's not enough to just exhibit something; you also need to show it clearly and openly. We learned that consumers believe things they can understand, especially when technology explains the reasoning and gives them reliable sources. We also learned that tiny UX features, like clear cards, seamless transitions, can make complicated software fun to use. What's next for CBRE Project We intend to add more real-time data to our research in the future. This may include things like crime and school ratings, neighborhood trends, and even user input on homes that we get from crowdsourcing. We want to go beyond local storage and add secure user accounts so that customers may save their data in the cloud and use the app from anywhere. Our goal is still the same: to help every user make smart, confident real estate decisions, even as we improve the AI's explanations and take in more data. <div