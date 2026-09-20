---
slug: "goosehunt"
url: "https://devpost.com/software/goosehunt"
title: "GooseOnTheLoose"
hackathon: "Hack the North 2024"
organization: "Hack the North"
winner: true
words: 1021
team_size: 4
has_repo: true
has_live: false
has_video: false
tags:
  - "project"
  - "domain/developer_tools"
  - "domain/education"
  - "user/educator_student"
  - "user/researcher"
  - "substrate/geospatial"
  - "substrate/video_visual"
  - "substrate/web_dom"
---

# GooseOnTheLoose

> Seeing geese all over campus? Well now you can befriend and study with them!

[Devpost](https://devpost.com/software/goosehunt) · hackathon [[Hack the North 2024]]

## Facets

**domain** [[developer_tools]] [[education]]
**user** [[educator_student]] [[researcher]]
**substrate** [[geospatial]] [[video_visual]] [[web_dom]]

**stack** cohere, mongodb, next.js, react, tailwind, typescript

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for gooseontheloose

## Body

Shows a collection of the geese you have found. Camera screen scanning a goose plushie. Home screen with location (purple pin is your location). Inspiration Amid the fast-paced rhythm of university life at Waterloo, one universal experience ties us all together: the geese. Whether you've encountered them on your way to class, been woken up by honking at 7 am, or spent your days trying to bypass flocks of geese during nesting season, the geese have established themselves as a central fixture of the Waterloo campus. How can we turn the staple bird of the university into a asset? Inspired by the quintessential role the geese play in campus life, we built an app to integrate our feather friends into our academic lives. Our app, Goose on the Loose allows you to take pictures of geese around the campus and turn them into your study buddies! Instead of being intimidated by the fowl fowl, we can now all be friends! What it does Goose on the Loose allows the user to "capture" geese across the Waterloo campus and beyond by snapping a photo using their phone camera. If there is a goose in the image, it is uniquely converted into a sprite added to the player's collection. Each goose has its own student profile and midterm grade. The more geese in a player's collection, the higher each goose's final grade becomes, as they are all study buddies who help one another. The home page also contains a map where the player can see their own location, as well as locations of nearby goose sightings. How we built it This project is made using Next.js with Typescript and TailwindCSS. The frontend was designed using Typescript React components and styled with TailwindCSS. MongoDB Atlas was used to store various data across our app, such as goose data and map data. We used the @React Google Maps library to integrate the Google maps display into our app. The player's location data is retrieved from the browser. Cohere was used to help generate names and quotations assigned to each goose. OpenAI was used for goose identification as well as converting the physical geese into sprites. All in all, we used a variety of different technologies to power our app, many of which we were beginners to. Challenges we ran into We were very unfamiliar with Cohere and found ourselves struggling to use some of its generative AI technologies at first. After playing around with it for a bit, we were able to get it to do what we wanted, and this saved us a lot of head pain. Another major challenge we underwent was getting the camera window to display properly on a smartphone. While it worked completely fine on computer, only a fraction of the window would be able to display on the phone and this really harmed the user experience in our app. After hours of struggle, debugging, and thinking, we were able to fix this problem and now our camera window is very functional and polished. One severely unexpected challenge we went through was one of our computers' files corrupting. This caused us HOURS of headache and we spent a lot of effort in trying to identify and rectify this problem. What made this problem worse was that we were at first using Microsoft VS Code Live Share with that computer happening to be the host. This was a major setback in our initial development timeline and we were absolutely relieved to figure out and finally solve this problem. A last minute issue that we discovered had to do with our Cohere API. Since the prompt did not always generate a response within the required bounds, looped it until it landed in the requirements. We fixed this by setting a max limit on the amount of tokens that could be used per response. One final issue that we ran into was the Google Maps API. For some reason, we kept running into a problem where the map would force its centre to be where the user was located, effectively prohibiting the user from being able to view other areas of the map. Accomplishments that we're proud of During this hacking period, we built long lasting relationships and an even more amazing project. There were many things throughout this event that were completely new to us: various APIs, frameworks, libraries, experiences; and most importantly: the sleep deprivation. We are extremely proud to have been able to construct, for the very first time, a mobile friendly website developed using Next.js, Typescript, and Tailwind. These were all entirely new to many of our team and we have learned a lot about full stack development throughout this weekend. We are also proud of our beautiful user interface. We were able to design extremely funny, punny, and visually appealing UIs, despite this being most of our's first time working with such things. Most importantly of all, we are proud of our perseverance; we never gave up throughout the entire hacking period, despite all of the challenges we faced, especially the stomach aches from staying up for two nights straight. This whole weekend has been an eye-opening experience, and has been one that will always live in our hearts and will remind us of why we should be proud of ourselves whenever we are working hard. What we learned We learned how to use many new technologies that we never laid our eyes upon. We learned of a new study spot in E7 that is open to any students of UWaterloo. We learned how to problem solve and deal with problems that affected the workflow; namely those that caused our program to be unable to run properly. We learned that the W store is open on weekend. We learned one another's stories! What's next for GooseOnTheLoose In the future, we hope to implement more visually captivating transitional animations which will really enhance the UX of our app. Furthermore, we would like to add more features surrounding the geese, such as having a "playground" where the geese can interact with one another in a funny and entertaining way. <div