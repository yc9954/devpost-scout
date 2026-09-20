---
slug: "sofia-stay-connected-without-a-connection"
url: "https://devpost.com/software/sofia-stay-connected-without-a-connection"
title: "Sofia: The No-Internet-Needed Personal Assistant"
hackathon: "Hack the North 2020++"
winner: true
words: 652
team_size: 4
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "domain/civic_government"
  - "domain/finance_payments"
---

# Sofia: The No-Internet-Needed Personal Assistant

> An Artificial Intelligence personal assistant that checks your emails, breaking news, government messages, stock/forex prices, and gets google searches without any internet connection. Just say "Hey"

[Devpost](https://devpost.com/software/sofia-stay-connected-without-a-connection) · hackathon [[Hack the North 2020-]]

## Facets

**domain** [[civic_government]] [[finance_payments]]

**stack** apify, currconv, flask, newsapi, nexmo, openweathermap, python, scaleserp, vonage, wit.ai

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what's next for sofia

## Body

banner GIF Initialization GIF Get stock/forex values (watchlist example) GIF Google search without internet GIF emials + government updates GIF covid updates GIF news alerts Inspiration Even in a world so connected today, many regions around the world are left lacking something we overlook: internet access! Half of the world's population is still offline, but almost 80% of people own mobile phones all over the world. We thought, why not bring internet essentials needs like email, searches, news, and updates to those people while also creating a powerful personal assistant perfect for anyone who values productivity and is always on the go. What it does Sofia is an Artificial Intelligence personal assistant that: Checks your emails for you and notifies you of any important emails Alerts you of any breaking news or government alert messages Notifies you of any weather changes, Keeps up to date with your stock and forex watchlist and send you updates if any of your positions move Understands needs through the conversation-like command structure Sends regular COVID-19 updates It even searches google to answer your questions Works fully off SMS It does all of this without your phone having to have an internet connection. All you need is this phone number to text, “Hey” How We built it Sofia is built on a modular multi-threaded architecture , with each feature running on its own thread, making the addition of new features more efficient. Flask is used to create a server that allows the project to run. The Vonage/Nexmo API for receiving and sending SMS messages is used heavily as it is SMS-based. The API allows Sofia to interact with the user and respond to specific requests. The messages retrieved are then interpreted by a trained wit.ai chatbot, which detects the intent and necessary variable that correspond with each intent. This intent is then used to determine which functions to call based on what the user wants. Feature/modular component uses different technologies/APIs to fulfil their need: chatbot: wit.ai COVID-19 updates: apify API Gmail: IMAP Government Alerts: NumPy News: newsapi API Google Search/Information Retrieval: scaleserp API Forex data: currconv API Weather: OpenWeatherMap API The application's main controller is multithreaded to allow for perpetual passive monitoring of things like the weather and stock prices while allowing for active commands like internet searches to go on simultaneously. As all communication is handled through Vonage/Nexmo API, we can remove the need for an internet connection on the user end. Challenges we ran into As all development journeys go, ours was riddled with its fair hair of bugs, mishaps, and errors. But in the end, we made it through. One of the first was when we ran out of credits for the Vonage/Nexmo API. As we were using a lot for testing and interaction, we ran out of credits to use on the platform. After trying to switch/set up a new account, the issue was fixed when one of the volunteers from Vonage (Bethany) was kind enough to give us a coupon with €10 of credits, allowing us to continue texting away. The second and probably the most unexpected was when an incorrect dependency sent us into an almost 1hr rabbit hole of fixing the project. However, we did come out victorious and were able to fix it. While annoying at the time, these setbacks allowed us to gain a greater understanding of the technologies used, along with giving us time to ponder new features. Accomplishments that We're proud of The creation of a platform that is fully functional in the scope defined at inception Creation of a system that mixed passive ad active commands The creation of many well-functioning modular components Devising a practical and innovative idea ## What We learned Use of several amazing APIs Serverside development in python using flask What's next for Sofia Asynchronous multi-user support Reducing server-side latency Adding extra functionality to existing components Addition of more components <div