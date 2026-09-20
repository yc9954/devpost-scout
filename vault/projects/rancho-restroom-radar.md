---
slug: "rancho-restroom-radar"
url: "https://devpost.com/software/rancho-restroom-radar"
title: "Rancho Restroom Radar"
hackathon: "Student HackPad 2025"
organization: "Student Hackpad"
winner: true
words: 501
team_size: 2
has_repo: true
has_live: true
has_video: false
tags:
  - "project"
  - "domain/accessibility"
  - "domain/developer_tools"
  - "domain/education"
  - "user/educator_student"
  - "substrate/geospatial"
  - "substrate/structured_db"
  - "substrate/video_visual"
  - "substrate/web_dom"
---

# Rancho Restroom Radar

> A mobile web app that tracks opened and closed bathrooms in Rancho Cotate High School.

[Devpost](https://devpost.com/software/rancho-restroom-radar) · hackathon [[Student HackPad 2025]]

## Facets

**domain** [[accessibility]] [[developer_tools]] [[education]]
**user** [[educator_student]]
**substrate** [[geospatial]] [[structured_db]] [[video_visual]] [[web_dom]]

**stack** css, firebase, html, javascript

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for rancho restroom radar

## Body

Opening page Joining a bathroom queue Inspiration Rancho Cotate High's bathrooms are constantly being closed and opened due to maintenance issues. In addition, our school has a prevalent amount of delinquency and vaping in our bathrooms, further contributing to our school administration closing a majority of our bathrooms. This results in only a select few bathrooms open and longer lines. Peers at our school complain about lengthy lines and walking to bathrooms that are already closed as a result. What it does Rancho Restroom Radar is a mobile web app designed to track bathrooms that are closed or opened. It provides a map of closed or opened bathrooms too and allows admins to change the status of bathrooms if they have the correct passcode. How we built it We used Firebase to help with server and database handling, and with HTML/CSS/Javascript for the front end. We used AI assistance from Co-pilot and ChatGPT to generate the main framework behind our code, and it was used in every file, i.e., index.html, style.css, app.js. It wrote a large portion of our code, approximately 80%+. Challenges we ran into We had to figure out how to place marker's using coordinates from the image using our limited CSS experience. We solved it by using a clicker that provides coordinates upon clicking the map image, then putting in those coordinates in the Firebase database for every bathroom that gets placed onto the map. Another issue was that the coordinates we received from the clicker function didn't provide the correct coordinates, but we fixed it by setting the map image correctly to its width. In addition, we had no experience using Firebase and had to learn how their backend services work in conjunction with the whole tech stack. We had to deal with debugging generated code. Accomplishments that we're proud of We're proud that the app can serve its main purpose of demonstrating which bathrooms are closed and open, which is the main concern for Rancho students trying to walk around and find bathrooms. We also feel more confident in using AI to assist with code generation and being able to debug generated code which happens frequently. We're also proud that we created a minimum viable product/demo considering this is our first hackathon. What we learned We learned how to use Firebase and Javascript. Also how to utilize AI to quickly jumpstart the app and allow us to debug minor issues and build upon what AI creates for us. What's next for Rancho Restroom Radar We need to implement a queue status which is in the works. It would show where the user is in the queue, and we also need to prevent a user from being in two queues at once. Yet another feature would be a filter for boys/girls bathrooms. We plan to show this to our school's administration and are willing to polish features and design further, and also provide web accessibility to desktops. We want to add this to a custom domain. <div