---
slug: "weather-app-kogj2f"
url: "https://devpost.com/software/weather-app-kogj2f"
title: "Weather App"
hackathon: "The Postman API Hack"
organization: "Postman"
winner: true
words: 261
team_size: 1
has_repo: true
has_live: true
has_video: false
tags:
  - "project"
  - "substrate/web_dom"
---

# Weather App

> Weather App is a web application which will display the current temperature in both Celsius and Fahrenheit along with the location.

[Devpost](https://devpost.com/software/weather-app-kogj2f) · hackathon [[The Postman API Hack]]

## Facets

**substrate** [[web_dom]]

**stack** api, css, html, javascript, rest, vscode

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for weather app

## Body

Inspiration I always wanted to learn more and work with different APIs, get the data from them and play with them around. What it does Weather App is a live weather tracking web application which takes the current latitude and longitude of the user once the user turns on the location on their devices. Using this data, the application makes a GET request to the OpenWeather API and get the location, weather summary and the temperature at that particular user location. The temperature what we get from the API is in Kelvin, so we converted it to Celsius. By clicking on the temperature unit ("C" or "F") in the web page, the Celsius data is converted to Fahrenheit and is displayed, and vice-versa. How we built it We uses OpenWeather( https://openweathermap.org/ ) API to make GET request and use the data in out application. The basic application is built using HTML, CSS and JavaScript. We use Postman to make the GET request and analyze the data from the Postman Interface. Challenges we ran into The main challenge is to use the correct data, process it and display it. Also, changing the icons according to the temperature and weather conditions, like using "cloud" icon for cloudy weather, "sunny" icon for sunny weather etc. is another challenge that we ran into. Accomplishments that we're proud of The project works fine as planned. What we learned Using APIs with JavaScript and using Postman to make Collections. What's next for Weather App We will try to improve our application to display more weather data. <div