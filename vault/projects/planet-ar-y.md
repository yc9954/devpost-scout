---
slug: "planet-ar-y"
url: "https://devpost.com/software/planet-ar-y"
title: "planet.AR.y"
hackathon: "Alexa Skills Challenge: Kids"
organization: "Amazon"
winner: true
words: 1443
team_size: 3
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "user/educator_student"
  - "user/researcher"
  - "substrate/code_repository"
  - "substrate/geospatial"
  - "substrate/structured_db"
  - "substrate/video_visual"
  - "substrate/web_dom"
---

# planet.AR.y

> An immersive augmented reality experience paired with Alexa to engage and teach kids about our solar system!

[Devpost](https://devpost.com/software/planet-ar-y) · hackathon [[Alexa Skills Challenge- Kids]]

## Facets

**user** [[educator_student]] [[researcher]]
**substrate** [[code_repository]] [[geospatial]] [[structured_db]] [[video_visual]] [[web_dom]]

**stack** alexa, android-studio, augmented-reality, blender, c#, heroku, javascript, node.js, unity, vuforia, xcode

## How they structured the write-up

- inspiration
- what it does
- how we built it
- step 1: create a unity application using vuforia
- step 2: building the alexa skill
- step 3: the nodejs alexa facing skill
- step 4: the intermediary server
- step 5: deploying to heroku
- how to use it
- challenges we ran into
- accomplishments that we're proud of
- vui design for the alexa skill + unity application and the javascript servers involved
- what we learned
- what's next for planet.ar.y

## Body

planet.AR.y Unity + Vuforia AR Interface App running on iOS Inspiration Ever since we were young children, we wanted to explore the universe as we both had a common passion for space and astronomy. Originally, we thought of creating a voice driven skill that took advantage of Amazon’s Alexa Voice Service that told stories to children. However, we realized there were two essential flaws with this idea. The first was that stories required little to no user interaction and we really wanted to harness the potential of using voice with Amazon Alexa. The second main flaw was that as humans, we are better visual learners than we are auditory (nearly 7 times more)! To solve this, we created a dynamic augmented reality experience that immerses children in a new environment and helps them learn about the solar system and satisfy their curiosity. What it does Users can download and launch the app which will be available on the Google Play Store and the Apple App Store. The app presents an augmented reality interface and projects a window into the solar system using the rear camera of the device. The skill then interfaces with this app and allows users to ask questions about the planet they are looking at, including its distance to the sun, some brief information about the planet, and more interesting details. How we built it The process of building this application was quite tedious and challenging, but it can be broken up into various modules. Load Unity and Vuforia and create models of all the planets with an ImageTarget that maps the planets to each other and a reference frame. Create an Alexa Skill in the Skill Builder portal and define the interaction models as well as the intent schema. This sets up the framework for the behavior of our skill. Create a Node.JS server that interfaces with the Amazon Alexa and translates the various intents into requests that can be passed on. Create another intermediary server that interfaces with both the Unity application and the Alexa skill by using HTTP requests to pass data between the phone and Alexa. Deploy the Node.JS servers onto a cloud based platform service such as Heroku that can run web apps from a stable and fast server. Step 1: Create a Unity application using Vuforia The first step is to install Unity with the Vuforia package which allows for the creation of augmented and virtual reality apps. On the Vuforia website, you can generate a database with an image target that renders your content on top of a specified image, which it uses as a reference point. In this case, we used a picture of a rocketship to go along with the space theme. Next, we had to download 3D models of all planets and position them accurately relative to each other. Step 2: Building the Alexa Skill The next step was to create the skill in the Alexa Skill builder. We had to write out all the utterances for our skill and define the intent schema in order to create the backbone of our skill. This was fairly straightforward as it takes you step by step through the process. Step 3: The NodeJS Alexa Facing Skill We decided not to use Lambda and instead create our own custom HTTP server that interfaces with the Amazon Echo. To do so, we used Node.JS and Express as well as a variety of other modules to make this task simpler. The server handles a variety of intent requests and returns a response after sending an HTTP request to the middle server which will be discussed in the next step. Step 4: The Intermediary Server In order to link the Alexa skill to the Unity application, we created another HTTP server that acted as a bridge between the phone and Unity application. The server sent HTTP requests to the Unity Application, which then responded with the nearest planet relative to the camera using a custom C# script. The server also responds to the Alexa Skill Server. Step 5: Deploying to Heroku We decided to deploy our Node.JS servers on heroku in order to give it a static url as well as ensure that our servers stayed up. You have to create a file called Procfile.txt, and inside type: web server.js Then, it’s as simple as posting the project on a Github repository and setting Heroku up to follow any commits made in that repository. How to use it Enable the Alexa Skill by asking Alexa to enable Reality Planets. Download the companion app from the link below or from the link Alexa will send to your phone. Ask Alexa to pair your phone and enter the code it gives you in the app you downloaded. Open the image down below on another device or print it out. Use the app to point at the picture and display the planets. Ask Reality Planets about the planet to get information about it. Challenges we ran into Unity does not support hosting an HTTP server that can handle incoming requests and it was extremely difficult to transfer information between the phone and the intermediary server. To establish a link between the Unity application and the Alexa skill, we needed a way to know which instance of the app was making requests in order to delivery information to the correct device. We had trouble with Unity resolving some Vuforia components, preventing us from working on multiple computers and merging our changes. When creating 3D models of all the planets, we had trouble resolving their textures and did not know how to create .mat (material) files that could be used. During testing we had issues using a tunneling reverse proxy (ngrok) as it repeatedly crashed and was unstable for our uses. The C# environment that Unity uses caused us some troubles as we had never used it previously. Our Heroku requests often failed because the servers were set to fall asleep after a set time period Challenge 1 Fix: We solved this by creating two different servers that could handle HTTP requests and allowed for the information from the Unity application (Planet) to be passed on to the Alexa skill. This was then processed through the various intents for each piece of information we wanted to deliver to the user (planet description, orbit time, diameter, and distance). Challenge 2 Fix: We used a server to bridge Alexa and the app in order to generate a unique UID that paired both of them in their own isolated instance. Alexa creates a one time alphanumeric seven character sequence that it then prompts the user to enter. This initiates a link between the two. Challenge 3 Fix: We were forced to use only one computer to run Unity on as it would compile properly on others. Challenge 4 Fix: We fixed this issue by learning how to convert satellite jpg or png images into that specific file type so that the .obj files would accept them as an overlay and so the planets would appear in color. Challenge 5 Fix: We deployed to Heroku to mitigate the issues we had with ngrok. Challenge 6 Fix: We learned the nuances of the language and restarted Unity which fixed a lot of the issues. Challenge 7 Fix: We used a Heroku App called Kaffeine to ping it every 30 minutes and keep it always running. Accomplishments that we're proud of We learned how to interface Unity and Alexa, which was very tricky and can help in future projects. We gained mastery of HTTP requests and NodeJS, as there were a lot of moving parts and requests that needed to be routed properly. A lot of the code for the servers and Unity can be repurposed for augmented reality applications that require connection to other platforms. Creating apps that work on other important platforms. We learned how to create an iOS app using Xcode for the first time. VUI Design for the Alexa Skill + Unity Application and the Javascript servers involved What we learned How to make a great Alexa skill that is accessible to all children and being able to provide a new way to learn about planets that was unique and not previously integrated with a voice platform. We also learned about the various hurdles that needed to be overcome to build a successful skill. What's next for planet.AR.y We hope to add different planets, moons, solar systems, and animate various orbits. Our skill can continue to grow as scientists increase their knowledge of space, allowing for fresh content to be added. iOS version coming soon! (App is ready but not published currently) <div