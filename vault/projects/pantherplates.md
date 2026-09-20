---
slug: "pantherplates"
url: "https://devpost.com/software/pantherplates"
title: "PantherPlates"
hackathon: "ShellHacks 2024"
organization: "init"
winner: true
words: 820
team_size: 2
has_repo: true
has_live: false
has_video: false
tags:
  - "project"
  - "domain/agriculture_food"
  - "domain/education"
  - "user/educator_student"
  - "substrate/structured_db"
  - "substrate/web_dom"
---

# PantherPlates

> PantherPlates is a meal planning website to meet all dietary needs for FIU students eating at the campus dining hall.

[Devpost](https://devpost.com/software/pantherplates) · hackathon [[ShellHacks 2024]]

## Facets

  <sub>weak: cross_origin_web</sub>
**domain** [[agriculture_food]] [[education]]
**user** [[educator_student]]
**substrate** [[structured_db]] [[web_dom]]

**stack** beautiful-soup, figma, flask, mongodb, openai, python, react, selenium, tailwind

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for pantherplates

## Body

Landing Page Login Page Dashboard: where you can see most recently saved meal and create a new one See the full nutrition facts on the Saved Meals page Meal Creation Form Inspiration Coming into this Hackathon, we knew we wanted to build an application around dietary health for students. Coming from UNC at Chapel Hill, our dining hall website, along with many other schools' websites, can be lacking in important dietary information. We wanted to make searching for dining hall food easy for all students, regardless of health conditions, dietary restrictions, culture, or personal preferences. While both FIU and UNC list out full nutrition facts, it can leave students lost and frustrated, especially with those who don't have their options listed for them on the website. That's why we wanted to build this website! Instead of listing the most common dietary restrictions (or none at all), we wanted the opportunity for every student to have a tasty and healthy meal. What it does PantherPlates is an easy to use web application where users can sign up to generate meals from FIU's 8th Street Campus Kitchen. Our web-scraping script can be run daily to get the current menu from FIU's Dining Hall Menu . After signing up, users will be able to create a meal by filling out the form, specifying their health conditions, dietary restrictions, and more. If they're satisfied with the meal, the user can save it to their profile for later. All their preferences, along with the full nutrition facts, will be on their profile. How we built it Web Scraping: We used Selenium to execute JavaScript and navigate through FIU's dining website, which relies heavily on dynamic content. BeautifulSoup was utilized to parse the innerHTML and extract information for breakfast, lunch, and dinner menus. Our script can be run daily to keep up with the current menu. Backend API: We built a RESTful API using Flask to handle requests from the frontend. The API interacts with our MongoDB cluster, storing user data and meal information. Database: MongoDB was chosen for its ease of use and flexibility, allowing us to store and retrieve user preferences and meal data. AI Integration: To generate ideal meals tailored to each user, we used OpenAI's API. By feeding in the scraped menu data and the user's specified preferences, we made prompts for AI to suggest meal options that align with the user's dietary needs. Frontend: Our frontend was built using React.js and Tailwind CSS for quick development. Challenges we ran into One challenge we ran into was having to use Selenium. This is a technology we have never used and we thought the website we were scraping from would mostly be HTML. FIU's dining website's info is loaded dynamically by so many different buttons which posed a challenge. Another big problem we kept running into was data validation. Translating different types of objects, data, JSON, etc. into different versions of each other was tough. Sometimes it was hard to keep track of what we expected a function, Selenium, soup, or React was returning. After a lot of prints and console.logs, we got it figured out. Accomplishments that we're proud of We're proud of making a product that has the potential to make a lot of people feel seen. There are so many niche groups of people whose issues are never brought to light. We wanted our application to be as versatile as possible to cover as many of these groups as we could. We think we did a good job with this and are very proud. Both of us used a lot of technologies that were new to us, so we're proud of learning a new tech stack in a short amount of time! Driving all the way from NC to Miami was tough, but totally worth it. What we learned Something we learned was to use Figma. Each of us hasn't used it much in the past, but it was great for messing around with new ideas and experimenting. We also learned not to overthink the small stuff. Spending over an hour on a tiny detail when you have limited time doesn't make much sense and we were able to learn how to get more and more productive as time went on. We learned how to resolve merge conflicts...a lot of them. What's next for PantherPlates In the future, we would love to add some real authentication to ensure our users are fully protected. We also wanted to add more options to the form, or even a whole new one. Adding options for wanting to gain weight, lose weight, maintain weight, or other nutritional goals was something we really wanted to do, but unfortunately didn't have time for. We also want to improve our UI and deploy in the very near future! We want to expand to other universities as well. This isn't an FIU-specific issue and can be scaled. <div