---
slug: "fitnessflow"
url: "https://devpost.com/software/fitnessflow"
title: "FitnessFlow"
hackathon: "XHacks 2021"
organization: "XHacks Organization"
winner: true
words: 552
team_size: 2
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "domain/developer_tools"
  - "user/developer"
  - "substrate/geospatial"
  - "substrate/video_visual"
  - "substrate/web_dom"
---

# FitnessFlow

> Make fitness more accessible

[Devpost](https://devpost.com/software/fitnessflow) · hackathon [[XHacks 2021]]

## Facets

**domain** [[developer_tools]]
**user** [[developer]]
**substrate** [[geospatial]] [[video_visual]] [[web_dom]]

**stack** css, javascript, python, react, tensorflow

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for fitnessflow
- other links

## Body

Pitch Splash Customize workouts Pose detection Inspiration The pandemic is still not over, and only about 50% of Americans have been vaccinated at the time of this writing. People are using fitness mobile applications more often these days. Still, the fitness applications are not meeting their needs as it does not provide flexibility on exercises or has a social community. What it does FitnessFlow is a mobile application that suggests personalized workout plans, detects when a user does a pose incorrectly, offers correction through live audio, and has workout groups to help provide accountability. How we built it We mostly spent our time during the hackathon, researching and working on the business aspect of this project, including market research, revenue investigation. We built the pose detection with Tensorflow, Python, and the frontend with React and HTML APIs. There is much other complicated mathematics involved with pinning points onto the screen while running the detection algorithm. Challenges we ran into We ran into the challenge of one of our backend developers not being able to make it to the hackathon, so we had to learn TensorFlow in a limited amount of time, considering we have other tasks to complete as well. We don't know much about business, so we had to google and research business concepts to understand it more to complete the pitch deck. Our original plan was to use Tensorflow's MoveNet model. However, we had difficulties finding resources on porting it to applications such as web and mobile. Therefore, we had to downgrade the model to PoseNet instead. Doing so allowed as to develop an application using it. However, more challenges arise. During the development of our react application, there were many difficulties, such as integrating react-webcam, and issues with the asynchronous webcam components, HTML Canva, and integrating Tensorflow's PoseNet. At first, we got it working, but there were heavy performance drop and ended up crashing our development environments. Accomplishments that we're proud of We are proud of making a UI for a fitness mobile application that is friendly to everyone. For developing the application, we are proud to walk off from solving all complicated bugs, issues, and problems that arise everywhere. Solving these problems allows us to improve our existing skills by generally using a framework/working at hackathons. What we learned We learned how to use Tensorflow models with react and use its own Canva drawing functions to display and map points on the screen. We learned how to make react app more performant with heavy tasks running in the background multiples every second. Integrating webcam video stream with Tensorflow's model and drawing the positions to the string was very interesting to learn and implement. Many mathematics expressions and logic were backing the function up, allowing us to deliver our functionalities. What's next for FitnessFlow Developing applications and implementing our MVP Implement a backend to store user data Make our application run natively cross-platform Gather users for beta testing before release Enhance the machine learning model for a more performant and accurate detection Invest in new features that would make our application stand out compare to our competitors Maintaining our application by fixing bugs, improving existing features. Develop with user's suggestions and ratings Other links Check out our pitch deck here: Pitch Deck Check out our infographic here: Infographic <div