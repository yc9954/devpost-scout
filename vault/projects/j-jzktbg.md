---
slug: "j-jzktbg"
url: "https://devpost.com/software/j-jzktbg"
title: "Fluent.ly"
hackathon: "TreeHacks 2023"
organization: "Stanford TreeHacks"
winner: true
words: 1359
team_size: 4
has_repo: true
has_live: false
has_video: false
tags:
  - "project"
  - "mechanism/on_device_local"
  - "mechanism/voice_speech"
  - "domain/education"
  - "domain/health_clinical"
  - "domain/immigration_refugee"
  - "user/developer"
  - "user/educator_student"
  - "user/patient_family"
  - "substrate/structured_db"
  - "substrate/web_dom"
---

# Fluent.ly

> Fluent.ly revolutionizes the ability to refine language ability. The synergy between our mission and financial support cements our ethically driven approach to bettering the education of the world.

[Devpost](https://devpost.com/software/j-jzktbg) · hackathon [[TreeHacks 2023]]

## Facets

**mechanism** [[on_device_local]] [[voice_speech]]
  <sub>weak: cross_origin_web</sub>
**domain** [[education]] [[health_clinical]] [[immigration_refugee]]
**user** [[developer]] [[educator_student]] [[patient_family]]
**substrate** [[structured_db]] [[web_dom]]

**stack** auth0, convex, css, html, javascript, microsoft-azure-cognitive-services, openai, python

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of:
- what we learned
- what's next?
- bibliography

## Body

Fluent.ly's logo Fluent.ly's Login Page Fluent.ly's Log Data Fluent.ly's Homepage Fluent.ly's User Interface Interaction Fluent.ly's Convex Dashboard Inspiration We were motivated to tackle linguistic challenges in the educational sector after juxtaposing our personal experience with current news. There are currently over 70 million asylum seekers, refugees, or internally-displaced people around the globe, and this statistic highlights the problem of individuals from different linguistic backgrounds being forced to assimilate into a culture and language different than theirs. As one of our teammates was an individual seeking a new home in a new country, we had first hand perspective at how difficult this transition was. In addition, our other team members had volunteered extensively within the educational system in developing communities, both locally and globally, and saw a similar need with individuals being unable to meet the community’s linguistics standards. We also iterated upon our idea to ensure that we are holistically supporting our communities by making sure we consider the financial implications of taking the time to refine your language skills instead of working. What it does Fluently’s main purpose is to provide equitable education worldwide. By providing a user customized curriculum and linguistic practice, students can further develop their understanding of their language. It can help students focus on areas where they need the most improvement. This can help them make progress at their own pace and feel more confident in their language skills while also practicing comprehension skills. By using artificial intelligence to analyze pronunciation, our site provides feedback that is both personalized and objective. How we built it Developing the web application was no easy feat. As we were searching for an AI model to help us through our journey we stumbled upon OpenAI, specifically Microsoft Azure’s cognitive systems that utilize OpenAI’s comprehensive abilities in language processing. This API gave us the ability to analyze voice patterns and fluency and transcribe passages that are mentioned in the application. Figuring out the documentation as well as how the AI will be interacting with the user was most important for us to execute properly since the AI would be acting as the tutor/mentor for the students in these cases. We developed a diagram that would break down the passages read to the student phonetically and give them a score of 100 for how well each word was pronounced based on the API’s internal grading system. As it is our first iteration of the web app, we wanted to explore how much information we could extract from the user to see what is most valuable to display to them in the future. Integrating the API with the web host was a new feat for us as a young team. We were confident in our python abilities to host the AI services and found a library by the name of Flask that would help us write html and javascript code to help support the front end of the application through python. By using Flask, we were able to host our AI services with python while also continuously managing our front end through python scripts. This gave room for the development of our backend systems which are Convex and Auth0. Auth0 was utilized to give members coming into the application a unique experience by having them sign into a personalized account. The account is then sent into the Convex database to be used as a storage base for their progress in learning and their development of skills over time. All in all, each component of the application from the AI learning models, generating custom passages for the user, to the backend that communicated between the Javascript and Python server host that streamlines the process of storing user data, came with its own challenges but came together seamlessly as we guide the user from our simple login system to the passage generator and speech analyzer to give the audience constructive feedback on their fluency and pronunciation. Challenges we ran into As a majority beginning team, this was our first time working with many of the different technologies, especially with AI APIs. We need to be patient working with key codes and going through an experiment process of trying different mini tests out to then head to the major goal that we were headed towards. One major issue that we faced was the visualization of data to the user. We found it hard to synthesize the analysis that was done by the AI to translate to the user to make sure they are confident in what they need to improve on. To solve this problem we first sought out how much information we could extract from the AI and then in future iterations we would simply display the output of feedback. Another issue we ran into was the application of convex into the application. The major difficulty came from developing javascript functions that would communicate back to the python server hosting the site. This was resolved thankfully; we are grateful for the Convex mentors at the conference that helped us develop personalized javascript functions that work seamlessly with our Auth0 authentication and the rest of the application to record users that come and go. Accomplishments that we're proud of: One accomplishment that we are proud of was the implementation of Convex and Auth0 with Flask and Python. As python is a rare language to host web servers in and isn't the primary target language for either service, we managed to piece together a way to fit both services into our project by collaboration with the team at Convex to help us out. This gave way to a strong authentication platform for our web application and for helping us start a database to store user data onto. Another accomplishment was the transition of using a React Native application to using Flask with Python. As none of the group has seen Flask before or worked for it for that matter, we really had to hone in our abilities to learn on the fly and apply what we knew prior about python to make the web app work with this system. Additionally, we take pride in our work with OpenAI, specifically Azure. We researched our roadblocks in finding a voice recognition AI to implement our natural language processing vision. We are proud of how we were able to display resilience and conviction to our overall mission for education to use new technology to build a better tool. What we learned As beginners at our first hackathon, not only did we learn about the technical side of building a project, we were also able to hone our teamwork skills as we dove headfirst into a project with individuals we had never worked with before. As a group, we collectively learned about every aspect of coding a project, from refining our terminal skills to working with unique technology like Microsoft Azure Cognitive Services. We also were able to better our skillset with new cutting edge technologies like Convex and OpenAI. We were able to come out of this experience not only growing as programmers but also as individuals who are confident they can take on the real world challenges of today to build a better tomorrow. What's next? We hope to continue to build out the natural language processing applications to offer the technology in other languages. In addition, we hope to hone to integrate other educational resources, such as videos or quizzes to continue to build other linguistic and reading skill sets. We would also love to explore the cross section with gaming and natural language processing to see if we can make it a more engaging experience for the user. In addition, we hope to expand the ethical considerations by building a donation platform that allows users to donate money to the developing community and pay forward the generosity to ensure that others are able to benefit from refining their linguistic abilities. The money would then go to a prominent community in need that uses our platform to fund further educational resources in their community. Bibliography United Nations High Commissioner for Refugees. “Global Forced Displacement Tops 70 Million.” UNHCR, UNHCR, The UN Refugee Agency, https://www.unhcr.org/en-us/news/stories/2019/6/5d08b6614/global-forced-displacement-tops-70-million.html . <div