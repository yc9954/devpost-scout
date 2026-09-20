---
slug: "via-dappia"
url: "https://devpost.com/software/via-dappia"
title: "Via Dappia"
hackathon: "Chainlink Spring 2023 Hackathon"
organization: "Chainlink Labs"
winner: true
words: 1554
team_size: 1
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "mechanism/vision_ocr"
  - "domain/civic_government"
  - "domain/disaster_emergency"
  - "domain/education"
  - "domain/finance_payments"
  - "domain/transportation"
  - "user/frontline_worker"
  - "user/general_public"
  - "user/patient_family"
  - "substrate/financial_record"
  - "substrate/geospatial"
  - "substrate/regulation_legal_text"
---

# Via Dappia

> Revolutionizing road infrastructure: This project tokenizes roads, decentralizing ownership & upkeep, cutting bureaucracy, improving maintenance efficiency, and creating income-generating RWAs.

[Devpost](https://devpost.com/software/via-dappia) · hackathon [[Chainlink Spring 2023 Hackathon]]

## Facets

**mechanism** [[realtime_stream]] [[vision_ocr]]
**domain** [[civic_government]] [[disaster_emergency]] [[education]] [[finance_payments]] [[transportation]]
**user** [[frontline_worker]] [[general_public]] [[patient_family]]
**substrate** [[financial_record]] [[geospatial]] [[regulation_legal_text]]

**stack** google-maps, hardhat, mapbox, node.js, react, solidity

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for via dappia

## Body

Inspiration Background: The idea for this project began to be seeded in 2017. At the time, I was sweeping floors of construction sites in southwest Florida all day, every day, and in doing that, I had a lot of time to let my mind consider a variety of ideas. I was really fascinated by smart contracts at the time, and Southwest Florida was experiencing an incredible boom in construction, thanks to a strong and vibrant private sector that celebrated financial success. I could also recognize a lot of valuable rules and regulations that were in place to help protect the public: everything from unique hurricane codes that would make buildings withstand natural forces and necessary strategies to protect the resplendent wildlife and natural features of the area to more germane fire codes and safety procedures. I would watch high rise condos go from breaking ground to ribbon cutting ceremony in a matter of months. **bold A noticed contrast: In early 2018, I went on a skiing trip to Vermont with some family members (I remember strongly telling them to consider buying this crypto project called Chainlink, but they pooh-poohed the idea). We drove from New Jersey to Vermont and I remember being awakened in Vermont by the car shaking so much due to how awful the roads were. I'd thought the roads would be a bit more maintained since the skiing industry is so important to that area, but year after year, the roads were just awful. My cousin explained that Vermont is a poor state, and this was when the world had become hyper-politicized, so he had to get his digs in about the Democratically run state. By this time, I'd already begun to have a worldview that the private sector is a lot better at getting stuff done than the public sector–all government websites I'd visit looked out-dated with poor UI, I was constantly hearing about the government's feuds with the private sector regarding military and aerospace products, etc. **bold Fast forward a bit So one day I was sweeping floors and it really just dawned on me that roads could probably become privately-owned assets by which private companies could make revenue, and I imagined we could have some really maintained roads, especially in places where there’s a high degree of traffic. I started devising how that would work using smart contracts for automatic micropayments as a person drove, but I kind of shelved the idea in the back of my head. Since that time, I've gone back to school to study Software Engineering and have gone all in on the Web3 world, and I recently moved to Salt Lake City, UT, where the roads are just as bad as Vermont's, if not worse, thus reminding me of this project idea. Utah doesn't have the excuse of Vermont of being a poor state, or my cousin's justification of it being a Democratically-run state, as it is quite wealthy and has a Republican government. Having just attended Consensus 2023, I was inspired to start building a simple proof of concept to show that this could actually work in real life. What it does The DAPP has two main components: the local frontend application and the smart contract. The frontend application is responsible for querying the road information for owned road pieces, letting the smart contract know that a new trip is starting/ending, and determining whether or not a user is currently traveling on one of those road pieces. If yes, then the application will track the distance traveled and communicate that information to the smart contract in order to facilitate the user’s payment to the road owner. The smart contract handles the minting and organization of road pieces (each road piece’s ownership is in the form of an NFT with metadata associated with that road). Additionally, the smart contract handles the payment of each driver to the road owner and organizing the data associated with each trip. How we built it I just dove in and built this from scratch. I started off with a blank react project and just researched everything I needed. I familiarized myself with the Mapbox API since it had a good free tier, messed around with the Google Maps API because it was easier to use with Chainlink Functions, and just started devising how I wanted it to accomplish this basic MVP. Challenges we ran into The biggest challenge I ran into was devising a way to get around not really being able to necessarily to "real-time, live micropayments," which is something I can hopefully devise a strategy for in the future. Then I also struggled with a way of making this as trustless an application as possible, but I think unfortunately location-tracking of a single user with the tools I have available really comes down to a single point of failure issue (i.e. if the user is trying to spoof his location). Accomplishments that we're proud of I'm honestly just proud that I've been able to build this into a working minimum viable product. I've been building this on my own in my free time and am proud of myself for getting this up and running and having disparate systems working in unison to operate an idea I have and prove that it really can be done. I can't imagine what would be possible if I actually had some resources to explore other ideas in the project. What we learned I learned so much in building this project. I really didn't have much of an idea of how it'd work and just kind of jumped in head first in devising how it'd work. I had the pleasure of recently speaking with Zubin in the Chainlink Discord Office Hours and was interested to know that he'd had some experience in dealing with roads from a software perspective. I learned about using road polygons to define simple roads with more specificity, and for roads with more complex shapes, I could represent road polygons as GeoJSON objects using the turf.js library (I devised an alternative approach for demonstration purposes that has worked well for a minimum viable product, but will likely devise a GeoJSON approach in future iterations). I also learned a lot about the taxation labyrinth that is used to maintain roads, and despite speaking with government representatives from the states of Florida, Arkansas, and Utah, none of them could really give me a clear picture of EXACTLY how the process works; however, there are taxes applied to everything from fuel, to tires, to cars themselves, while the rest of the costs of these roads are borne by general fund receipts, bond issues, designated property taxes, and other taxes. It truly seems like a system very much in need of some increased transparency, and who knows how much of that money actually ends up being used how it is supposed to? Finally, I was fortunate enough to learn a lot about Chainlink Functions in the process of building this application. I was hoping to use Functions to do a sort of "decentralized user location getting" and ultimately realized that when I was trying to get the user's location, I was actually querying the location of each node in the DON which was making the getLocation API call and I was likely getting some kind of medianized returned hex response which wasn't very useful. What's next for Via Dappia I've got a lot of interesting implementations I'd love to do in the backlog. Obviously this is a very big-scope project, and were it to ever be used at scale, there'd have to be massive governmental overhuals and a way of mandating that users must have this calibrated app during car registration or something. That aside, I'd really love to mess around with the Tesla APIs to see if I could get this project working entirely on a Tesla's built-in computer, as that's how I really envision the product working: a user turns on the car and the app is started up, and when they turn off the car, everything relating to that trip is processed (I've also really played the tape forward into how this might work with self-driving cars, how road assets might symbiotically interact with businesses along the roads, etc etc). I've also developed a relationship with the company that is building the roads for a brand new community being built in Utah called "The Point." I'm hoping to learn more about that process and see where that leads. Finally, as I mentioned, I'll probably devise a much more sound road-definition structure using GeoJSON road polygons for maximum specificity of road location definition, and then explore other means of user tracking that are much more advanced like cell tower/wifi triangulation and ultimately smooth live-map rendering. Also, there are just so many different things that can be explored using this kind of foundation. One that I am especially interested in is a sort of "pay-per-use auto insurance" application where when you turn your car on and are being tracked while driving, you're submitting micropayments to a sort of insurance underwriter. Why pay for insurance if you're not using your car? Obviously this would be another huge undertaking, but it would be awesome to have some resources, especially intellectual resources, to explore these ideas and help build them out. <div