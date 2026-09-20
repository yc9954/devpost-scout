---
slug: "frog-baby-for-alexa"
url: "https://devpost.com/software/frog-baby-for-alexa"
title: "Frog Baby for Alexa"
hackathon: "Amazon Alexa Skills Challenge"
organization: "Amazon"
winner: true
words: 1249
team_size: 3
has_repo: false
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/voice_speech"
  - "domain/developer_tools"
  - "domain/education"
  - "user/developer"
  - "user/educator_student"
  - "substrate/geospatial"
  - "substrate/structured_db"
  - "substrate/web_dom"
---

# Frog Baby for Alexa

> Find a place to eat, explore our majors, or learn about Ball State - all with Frog Baby for Alexa!

[Devpost](https://devpost.com/software/frog-baby-for-alexa) · hackathon [[Amazon Alexa Skills Challenge]]

## Facets

**mechanism** [[voice_speech]]
**domain** [[developer_tools]] [[education]]
**user** [[developer]] [[educator_student]]
**substrate** [[geospatial]] [[structured_db]] [[web_dom]]

**stack** .net, amazon-alexa, c#, firebase, google-places, raspberry-pi, web

## How they structured the write-up

- inspiration
- how it works
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for frog baby for alexa

## Body

Welcome screen for the Skill Find a place to eat based on food type or location View matching locations on the map, with additional info for each place View details for a specific location Explore our majors Determine your interests to better assist with your exploration For each interest, what majors are offered View the detail for the major Inspiration At the beginning of each summer, thousands of incoming students and their families arrive at Ball State University for Orientation. Over the course of a couple days, the new freshmen and transfer students will register for classes, get their Cardinal Card, and prepare to be a cardinal – the mascot of Ball State. Along the way, they will have questions about navigating their new home, finding all that campus and the city have to offer, and learning more about the university. Frog Baby for Alexa embraces the emerging world of voice assistants to interact with and help them explore the university in a new and exciting way. For years, we have relied upon kiosks, static displays, brochures, and other means to convey information to new students and their families. With the arrival of Alexa, we had a great opportunity to create a new interaction model, and approach that situation with an engaging and light-hearted conversation. We named our skill “Frog Baby” after an iconic symbol of the university – a beloved sculpture of a joyous little girl playfully holding a frog in each hand. For years, the statue was on display in the David Owsley Museum of Art, where students would visit her and rub her nose for good luck during exam week. More recently, Frog Baby became the centerpiece of a fountain outside of the main campus library, and instead of rubbing her nose for good luck, students dress her in a hat and scarf for those cold Indiana winters. How it works Our initial conversation focuses on three key topics – areas that are very important to hungry and inquisitive high school students and their families during orientation week at the university. Food and coffee – Naturally, food is always a top priority when visiting a new place. Frog Baby is able to offer suggestions on places to eat on or off campus, where to find a particular food type like pizza or sandwiches, or the location of a particular restaurant. And most importantly – coffee. Visitors can ask, “where is the closest place to get coffee” and a map immediately appears on the connected display, along with the hours, rating, and contact info. Knowing everyone has a hectic schedule during the visit, Frog Baby can even tell them how long it would take to walk or drive to the location. Majors – Students are able to explore the nearly 190 majors and minors offered at the university. Starting with a broad list of 14 categories, they are able to talk to Frog Baby and find something that matches their interests. Fun facts – As a light-hearted way to engage visitors, Frog Baby can tell them a fun fact about the university. With things like the Homecoming Bed Race, Benny, and the Scramble Light, visitors will quickly learn all of the fun and interesting traditions the university has to offer. How we built it When the team began working on Frog Baby, we knew we wanted to approach the project from a different perspective than most voice assistant skills. The skill follows the basic conversation pattern, whereas users can ask a question, receive an answer, and then ask follow-up questions. However, rather than relying on Alexa to provide all of the necessary information – which for us, could include some lengthy lists of majors and restaurants – we incorporated an external display as a companion to the voice output, along with the cards in the Alexa companion app. The setup includes 55” flat panel TV and a connected Raspberry Pi running Chromium in kiosk mode, which displays a website with a combination of a Firebase database and a traditional backend database using Azure SQL. As users talk to Alexa, corresponding and additional information appear on the screen, helping users navigate Alexa’s responses. The cards within the Alexa companion app mirror the content on the display, while maintaining the format and structure of the card implementation. When visitors talk to Alexa, a Microsoft Azure app service handles the interactions. The service communicates with Firebase to trigger the appropriate information on the display, and our backend Azure SQL database to retrieve the speech and card responses. By updating a few rows in the database, we are able to modify the conversation and responses spoken by Alexa, displayed on the screen, or within the companion app. Challenges we ran into Learning a new platform is always a challenge – but in a good way! Exploring the features and functionality of the Alexa Skills Kit was a nice change of pace from our typical projects (mobile and web), and allowed us to engage users in a new way. While our apps reside on a variety of platforms, our backend is primarily Microsoft, so working with the Alexa Skills Kit in the .NET environment was a bit tricky in the beginning. Thanks to the amazing community of developers, we found a great library from Ștefan Negrițoiu on GitHub ( https://github.com/AreYouFreeBusy/AlexaSkillsKit.NET ). After some experimentation and reading the JavaDocs (close approximation to this implementation), we managed to get everything up and running. A few months later, we have our Skill ready for certification! Accomplishments that we're proud of The team is proud of the work we accomplished with the project and the different technologies we integrated to realize the goals we had set forth at the beginning. By incorporating the Raspberry Pi, Firebase, and the cloud services on Azure, we were able to build a connected and engaging experience for our visitors. In addition, this serves as a great example of the technological prowess of the staff, our dedication to emerging technologies, and the type of experiences students can expect to have once they arrive on campus. What we learned Beyond the obvious – how to implement a Skill with the Alexa Skills Kit – we learned how to approach voice user interfaces, design an application for two-way conversation, and interact with the complexities of natural language processing. In addition, the project provided another opportunity to work with the technologies that connected everything together. We just scratched the surface of designing a voice interaction model – understanding how users speak, their expectations of a conversation, and the unknowns of ambient noise are all aspects of this technology that deserve further attention. Are the responses too long? Too short? Do they convey the appropriate information in a tone that engages the visitors? Does Frog Baby present the content in an engaging and informative way? All of these are questions we will continue to ask ourselves and we develop future projects on this platform – so we learned there is more to learn with this technology! What's next for Frog Baby for Alexa Frog Baby for Alexa is our first project using the Alexa Skills Kit, and we’re excited to continue exploring the capabilities of this platform, and the opportunities it can offer students, parents, staff, and other visitors to our campus. The project launches in early June as we welcome everyone to campus for the summer orientation. We cannot wait to see how they react to Alexa and the questions they’ll ask her! <div