---
slug: "covid-challenges"
url: "https://devpost.com/software/covid-challenges"
title: "COVID challenges"
hackathon: "Hack Quarantine"
organization: "Hackathons UK"
winner: true
words: 1046
team_size: 1
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "domain/education"
  - "domain/mental_health"
  - "user/educator_student"
  - "substrate/code_repository"
  - "substrate/geospatial"
  - "substrate/structured_db"
  - "substrate/web_dom"
---

# COVID challenges

> Trace indoor exercise (rowing machine, exercise bike, running in circles) along real paths. Compete with friends, complete a challenge to be proud of together.

[Devpost](https://devpost.com/software/covid-challenges) · hackathon [[Hack Quarantine]]

## Facets

**domain** [[education]] [[mental_health]]
**user** [[educator_student]]
**substrate** [[code_repository]] [[geospatial]] [[structured_db]] [[web_dom]]

**stack** bootstrap, css3, google-maps, html5, javascript, php5, sqli

## How they structured the write-up

- contribution
- completion
- design, ui and ux
- technology
- originality

## Body

Visit covid challenges here: https://www.covidchallenges.online/ To see an example of a complex route being mapped visit: https://www.covidchallenges.online/route/route.php?multipleUserID=2 Please note, now that the hackathon is over the site no longer has an ssl certificate. Feel free to register and explore for yourself, or if you'd rather not I have provided a dummy account: email: hello@hello.com password: password Contribution With COVID challenges I wanted to create a solution to some of the biggest challenges presented by the pandemic. Sedentary lifestyle and poor fitness are known contributors to complications from COVID-19, also mental health and well-being are seriously affected by being forced to stay at home for extended periods. Charities and voluntary organisations have seen a dramatic drop in funding since the start of the pandemic estimated at £4.3 billion (see front page of website). In order to try and overcome these challenges I decided to create a way for people to exercise at home in a fun way, whilst socialising. My website allows you to create distance challenges that you can share with others and compete together to achieve a goal. This will allow people to become fitter in order to bolster their immune system and improve their mental health, linking these challenges to a charity will help to overcome some of the financial deficits through sponsorship. The social aspect will also assist with mental health and well being. This, I hope, will create a way of overcoming some of the biggest challenges associated with the pandemic. Also, the ability to view your location in google earth returns some much needed adventure and motivation. Completion The website is available to use at the top of this page to verify what I have implemented. Each user is given their own profile upon registration which they can use to create their own challenges (using 2-8 sets of latitude longitude points which can be viewed from google maps or view the most popular challenges and select between them) They can make their profile private and update profile details like a display name and profile picture. Each route is displayed using the google maps Javascript API (See technology section). Users can add "updates" to their routes to add to the total distance (try with the dummy account) and their progress is tracked against the others in the challenge as to how far each of them have contributed. Any mistaken updates can be removed by the user in the "view updates" section, as well as one user who is deemed the "main user" (the user who created the challenge) and can delete any users distances in order to moderate actions. Any accounts which are private are hidden appropriately in the challenges page and when trying to view their user page. Challenges themselves can also be made private, appearing on the users profile page only for that user, and displaying a privacy notification if the challenge page is viewed by a user who is not a member of the challenge. Links for inviting users to view, join and try (start a new one of the same route) for themselves are found in the challenge, share route tab. And the settings tab is only visible for the main user and allows that user to change the privacy of the challenge. You can also view the charity link which is entered by the creator when the challenge is created I have taken full care to protect the site against online attacks, I have used password encryption and implemented protection against SQL injections. As well as notifications when the user is to be directed to a link which has been entered by another user, allowing them to back out if it looks fishy. If I had extra time I would amend a few minor things: Extension of the challenge settings to allow for changing the name of the challenge and the main user An other section for travel distance, to allow the user to showcase the originality of how they choose to perform the challenge Design, UI and UX I think the UI and UX design is quite nice here, my general philosophy was to make every button obvious as to what you are pressing and what it's function is. As well as limiting the actions required to perform certain actions, for example adding an update involves only four absolutely necessary clicks (logging in, viewing challenge, adding update, confirming distance). View the website to make up your own mind :) Technology To build the site I used HTML, CSS, Javascript, PHP, Bootstrap and JQuery as well as the google maps Javascript API. I am most proud of the feature to plot your current location on the route, which is not something that comes with the API and took a broad understanding of how the returned javascript objects were made up. I'm also proud of the features in place to check the validity of the users custom made challenges. Entering in a value which is not a valid latitude and longitude, or google cannot find a route between throws an error. This ensures the user created routes are always valid and work 100% correctly. As a first year student I have never worked with a backend before and thus this was the main allure of the task for me. Learning PHP and web security completely from scratch for this project, I am proud of the outcome. Originality There are no other similar fitness type websites, that directly address the pandemic challenges I have described. An example of a concept is Zwift however, the competition element of this program is oriented towards short term racing without charitable links and long term social contact. The ability to create your own challenges as well as do them however you like (treadmill, rowing machine, hopping even ping pong ball hit distance all contributing to one challenge) allows you to tailor your experience to allow grandma to compete with her teenage grandchildren even if her contribution is small. Creating the desired outcomes across all generations and ability levels. If you have any questions please feel free to direct message my discord oliver_ursell (I'm a member of the hack quarantine server). Please note, I have kept my git repository private to protect database passwords, if you'd like to view it let me know. <div