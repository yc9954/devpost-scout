---
slug: "my-dream-destinations"
url: "https://devpost.com/software/my-dream-destinations"
title: "Coddiwomple"
hackathon: "Junction 2017"
winner: true
words: 987
team_size: 5
has_repo: true
has_live: true
has_video: false
tags:
  - "project"
  - "mechanism/vision_ocr"
  - "domain/developer_tools"
  - "user/developer"
  - "substrate/structured_db"
  - "substrate/video_visual"
---

# Coddiwomple

> Explore destinations around the world based on your social media profile. Get a full visual and auditory experience.

[Devpost](https://devpost.com/software/my-dream-destinations) · hackathon [[Junction 2017]]

## Facets

**mechanism** [[vision_ocr]]
**domain** [[developer_tools]]
**user** [[developer]]
**substrate** [[structured_db]] [[video_visual]]

**stack** azure, finnair, instagram, mongodb, ms-cognitive-services, node.js, react, redux, spotify

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for coddiwomple

## Body

Coddiwomple (v.) To travel in a purposeful manner towards a vague destination Inspiration Have you ever wanted to explore flights without specifying too much? The process today might look something like the following scenario. You go on your preferred social media and ask your friends where to go or browse your feed for inspiration. You might google for more information, look for pictures tagged to those places or even listen to the local music. Once you have some destinations in mind, you open multiple tabs on your browser to check the prices for each one of them on some random dates. Then you compare those prices and decide to proceed with a few reasonable ones. That is when you start the dance with the dates to find the best deals. After all these steps you finally have a destination to propose to your travel companion. How about we do all that for you? What it does Coddiwomple finds your travel preferences by analyzing the Instagram pictures you like and proposes Finnair flights to those destinations for you. Rather than just listing the flights Coddiwomple features each destination's vibe by showing the liked images tagged to that place and by playing a track from Spotify based on an analysis on those images to put you in the right mood. If you like the destination's vibe you can save it for later use and continue exploring. How we built it We started the project by innovating around the Finnair and Spotify challenges. We were figuring out what gives a person a certain feeling, a vibe, about a travel destination. Instagram is a platform where users give subtle clues about their interests by liking certain pictures in their feed. Instagram is also the most common place to post your travel photos nowadays. That is why we decided to start with it as the social media of choice. By using the Instagram API we fetch the geotags of the recently liked images to determine what kind of places the user likes. Then we wanted to incorporate the right music for that destination. First we tried selecting a track from a playlist featuring the name of the destination (city) from the Spotify API. Then we tried sending the liked Instagram images to backend to be fed through Microsoft’s Artificial Intelligence service Computer Vision API to analyze the contents of those photos. The tags with the highest appearance rate were then used to associate the best matching track from Spotify with the travel destination. After analyzing the track selection for random destinations and images, we added a country reference to each destination in our backend and started selecting Spotify tracks in playlists featuring the country name to get better matches. Ultimately, the user gets a fully personalized immersive experience of the travel destination of their dreams, including the visual and auditory experience. We used Node.js to handle most of the logic: API calls to Finnair, Spotify and Instagram API as well as leveraging the Artificial Intelligence in personalized suggestions at the backend side. Data is stored into MongoDB. The entire backend including the database is deployed to the Microsoft Azure cloud. The client is built to be a Progressive Web Application with a mobile-first approach. Technically the client application is engineered using React.js views library and Redux state management library to manage the application state. UPDATE November 27th Finnair disabled their API so we took the link to our live demo down, since it is not working anymore Challenges we ran into All apps trying to access Instagram API need to be approved by Instagram. Thus, we needed to use the Sandbox developer mode that has a very limited user pool and interactions. (For example just 20 most recently liked images can be fetched so we cannot display more images for each destination) How to select the best track from Spotify for each destination, should country, city or keywords identified from the pictures be used as the selection criteria. How to determine the music taste of the user from their Instagram profile to "personalize" the music selection for the destination for that user. Accomplishments that we're proud of That we managed to integrate the Instagram, Spotify and Finnair APIs to our project successfully That we tried so many different ways of selecting the right song for each destination Our team spirit throughout the whole project - can do attitude all the way What we learned Five complete strangers from four different countries and three hackathon newbies can get a lot done by just sitting together for few hours. Even if some task is new to you, you might figure it out by just sticking to it and by asking for help from your team mates. That unfortunately you cannot get the full access to APIs right away to enjoy everything they offer.. What's next for Coddiwomple The designs feature an idea that you could select the preferred travel duration for example between 3 and 5 days and the preferred time of travel for example March 1st to 31st. It would be great to implement a more capable search based on that criteria so that the results would feature the best deal with those filters for your destinations. Next it would be amazing to integrate more social medias like Spotify and Facebook as the personalization method. The search could take into account the type of music you listen to and where it is popular as well as where those artists are playing or are from and suggest flights to those places. A smarter algorithm for Instagram could also take advantage of the hashtags of the liked photos since those usually feature places as well. Another feature would be to integrate Spotify so that you can save the track playing to your own music if you like it. The hero Instagram images could also change automatically to feature more images from the fetched feed. <div