---
slug: "expeditionexpertbot"
url: "https://devpost.com/software/expeditionexpertbot"
title: "ExpeditionExpertBot"
hackathon: "HackSwift 2024"
organization: "hackswift"
winner: true
words: 923
team_size: 2
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "domain/developer_tools"
  - "domain/education"
  - "user/developer"
  - "user/educator_student"
  - "substrate/code_repository"
---

# ExpeditionExpertBot

> Quick flight bookings with the best options, all within a Telegram bot

[Devpost](https://devpost.com/software/expeditionexpertbot) · hackathon [[HackSwift 2024]]

## Facets

**mechanism** [[realtime_stream]]
**domain** [[developer_tools]] [[education]]
**user** [[developer]] [[educator_student]]
**substrate** [[code_repository]]

**stack** python, pythonanywhere, telegram, tequila-api

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for expeditionexpertbot

## Body

Inspiration Being avid travellers, we wanted to create a user-friendly platform that will assist users in simplifying the tedious tasks in the process of planning a vacation, such as booking flights and hotels, and planning itineraries. What it does Currently, ExpeditionExpertBot offers real-time flight-searching functionality within a Telegram bot. Users can input their travel details, including dates, locations and whether they are looking for a return flight, and the bot retrieves the best available flight options and presents them in a user-friendly format that includes the price, number of stops, airlines and even the booking link. All these eliminate the need for tedious web-browsing. How we built it We used the pyTelegramBotAPI to enable us to create an interactive bot using Python. Additionally, we integrated a third-party flight-search API: Tequila Seach by Kiwi.com to retrieve the most accurate and up-to-date flight option, and to provide a link for the user to view more details of the flight and book the flight directly. Last but not least, we also tested it with multiple scenarios to debug and refine it into a polished and refined bot. Challenges we ran into As this was our first project, and thus our first time creating a Telegram bot, we faced issues trying to read and understand the pyTelegramBotAPI documentation to integrate the flow of the Telegram bot smoothly. One of the biggest issues we ran into was ensuring that the bot could handle multiple users at the same time, as we accidentally discovered that the bot would mix up user inputs when both of us were testing it at the same time. After countless hours of trying and testing solutions, we came up with the fix of storing each user's chat inputs in a json format and making sure the bot accesses and uses the correct user's details. Another challenge we faced was sourcing for APIs that were free-to-use for non-businesses. Many popular sites only allowed large businesses to integrate their API and thus those were out-of-reach to us. Thankfully, we found Kiwi.com which had a free-to-use flight search API. We wanted to integrate hotel searching into our bot too but we were unable to find free hotel search APIs. Lastly, we faced challenges with the bot interface as well. We deliberately tried to combine inputs that would "break" the bot, and these bugs took considerable time and effort to clean up. Accomplishments that we're proud of Being freshman students, we are very proud to be able to develop a fully-functional product from scratch. We had to learn on the go and there were many moments where we both wanted to give up, as it felt like this was outside of our current capabilities. Despite facing numerous obstacles and moments of doubt, we persevered and pushed ourselves beyond our perceived limits to bring our vision to fruition. Our ability to adapt and learn on the go impressed us. We are also proud that we were creative in our solutions, while at the same time leveraging what we have learnt in our course. Our resourcefulness and perseverance in searching for solutions online also helped us finish the product. What we learned Being quite new to programming, this hackathon was an eye-opening experience for us and we managed to learn a lot. We learnt to leverage APIs to extract information directly from the provider, and to design a user-friendly UI. Most importantly, integrate the UI with the API, so that the user is connected with the information that they want and the product is easy to use. Looking back, we should have been more involved in each other's work. Nichlos worked mostly on integrating the API, while Aik Chong worked mostly on implementing the UI. Although splitting the work into such segments is more time-effective, we realised that if we had been more involved with each other's work, we both could have learnt much more. If we could have done this from the start again, I think we would have chosen to make the bot asynchronous instead of synchronous. This would allow the bot to be better able to handle multiple users. However, we were not aware of this possibility when we first started. We also learnt the importance of writing "clean" code and to have good coding practices. In this aspect of our work, we are unsatisfied, and we felt that there was much room for improvement. We could have made the code much more modular and readable overall. Fixing bugs was tedious because of this, as we had to trace back our lengthy code to find errors. As software developers, we will constantly discover new bugs or errors that may be completely unexpected, and often, an elegant solution may not present itself immediately. But we should still always try to look for the most efficient and effective solutions to optimise our product. What's next for ExpeditionExpertBot We hope to be able to add more categories for flight search, such as multi-city flights, flight classes (economy, business, first class etc.), airlines, number of stops, number of kids and baggage so that users are able to find better flights that suit their requirements. We hope to further tidy up our codebase as well and implement an asynchronous bot that can handle a larger user base so that further development is easier. If the bot grows, we hope to gain access to a hotel search API to add the function of booking hotels and leverage AI tools to help users create a travel itinerary based on their provided trip details. <div