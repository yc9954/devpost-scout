---
slug: "converse-xash34"
url: "https://devpost.com/software/converse-xash34"
title: "Converse"
hackathon: "hack:now"
winner: true
words: 1051
team_size: 4
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "domain/developer_tools"
  - "domain/immigration_refugee"
  - "user/developer"
  - "user/general_public"
  - "substrate/web_dom"
---

# Converse

> A one-stop Interactive Voice Response (IVR) chatbot hosted on an actual phone number for reliable information dissemination to the masses.

[Devpost](https://devpost.com/software/converse-xash34) · hackathon [[hack-now]]

## Facets

**mechanism** [[realtime_stream]]
**domain** [[developer_tools]] [[immigration_refugee]]
  <sub>weak: health_clinical, retail_commerce</sub>
**user** [[developer]] [[general_public]]
**substrate** [[web_dom]]
  <sub>weak: geospatial</sub>

**stack** css, firebase, flask, html, javascript, python, tableau, twilio

## How they structured the write-up

- phone number (converse) ivr chatbot: +18634171298

## Body

Converse Logo Inspiration Covid-19 has impacted the world negatively, and social distancing has changed the way we live. Due to the restriction of our movement, millions rely on the internet for work, healthcare, education and shopping, and people want to know the precautionary steps, symptoms and other relevant news regarding this pandemic. The FCC said more than 21.3 million people don’t have any internet access, though many experts think this is an undercount according to the news [1]. Furthermore, misleading informations and fake news have been spreading rapidly as the battle against fake news is likely to last as long as the virus [2], especially in rural area [3], therefore, there is a strong need of the a system that is easily accessible, scalable and reliable which can cater the needs to fight fake news without using internet connectivity. [1] https://www.citylab.com/equity/2020/02/internet-access-rural-broadband-digital-divide-map-fcc-data/606424/ [2] https://www.weforum.org/agenda/2020/03/how-experts-are-fighting-the-coronavirus-infodemic/ [3] https://www.forbes.com/sites/claryestes/2020/03/17/coronavirus-and-rural-america/ What it does! Converse is a one-stop Interactive Voice Response solution hosted on an actual phone number (Google Assistant on Phone Call straight) to disseminate reliable news, stats, and safety measures to the public so as to curb confusion and rumors amongst the masses along with features to aid the users in this time of crisis. This chatbot can be used to order necessary items during this pandemic. There are key areas why our solution is effective to tackle the problem we are aiming to solve: Our app can reach people who are not well-versed with technology, especially for boomers. Our app is a dial-and-talk chatbot. It can help people from rural areas who might not have reliable internet access and news to get is straight from the phone call It can help governing bodies to get insights into the real-time current situation based on users Highly scalable with no hardware dependencies and easy to deploy software Monitor the needs of the public from kilometers away using the crowdsourcing methodology Act as a front-line tool for helpline call centers so they can cater to the more prioritized clients Bridges the gap between the supply-and-demand chain by connecting potential customers directly to vendors It can be immediately deployed which is currently the need of the hour for our nation as well as for the whole world. Phone Number (Converse) IVR chatbot: +18634171298 -Myth Buster segment (to check if your facts are valid or not using WHO MythBuster segment) -Current happenings around your country (determines your country with your phone number's country code) -Ordering essential supplies (hence bridging the supply-demand chains) -Stats regarding COVID 19 for countries only (currently built stats support for the USA) Examples: (Myth Buster Segment) User: Is it true that COVID 19 doesn't spread in humid places? Converse: According to my sources, this is a myth. You can verify it by visiting the World Health Organization (WHO) website. (News Headline Segment) User: Can you tell me the current happenings in America? Converse: [fetches news and speaks it - 2 headlines] (Order Requests Segment) User: I would like to order a few supplies Converse: [proceeds to collect user information, parses it and sends it to the Admin Dashboard] (Stats Segment) User: How many people have been affected by COVID-19 in America? Converse: [fetches stats and replies with the output] Our IVR chatbot implementation is unlike other chatbots in the market which are hosted either on Web or a mobile application. We had user accessibility in our minds and thus, our chatbot- hosted on a phone number- actually provides an easy-to-use source of reliable information to the technically illiterate population and in-general will appeal to everyone. It is a plug-and-play solution and is immediately deployable for usage in the real world, which is currently the need of the hour. We hope to develop this project beyond the scopes of this hackathon and turn it into a reality. How we built it! Using Twilio API for building IVR Chatbot Firebase and Flask are used for the backend of our application We used HTML, CSS, Bootstrap and JavaScript to make admin dashboard Challenges we ran into Connecting the Firebase DB with Tableau to let data streaming and updated visualization based on user’s queries automatically. Cross border collaboration with different time zones are quite new for some of us Technical stack could have been much more thought of so that we could save time. Accomplishments that we're proud of We managed to deliver that fully functional chatbot that is straight away to the phone call. We also managed to build the dashboard to let governing bodies to see what is happening. Hosting a chatbot on a phone number in a much more unique and effective way is fruitful. Furthermore, collaborating with others who have different backgrounds, time zones and nationality while delivering the product is a very nice experience indeed! What we learned! Learned how many companies out there are pulling around the globe around Covid-19 and created API’s for developers This project was a little different because it's not like you could find information on how to present COVID-19 we did everything in real-time so everything we implemented we learned hands-on. We also learned how to integrate time management with our team, seeing as how we had a group from Indonesia, India, Kansas, and California we dealt with great difficulty the first night so we had to task everything out and trust our teammates across the world in their time zone. There were some technical challenges we faced, and there were some last-minute changes due to some issues. We learned the importance of having software design architecture in mind before actually implementing this into the real project to reduce technical debt. What's next for Converse Built-in multiple languages support with better accuracy Setting up scalable architecture to accommodate large user-based Supporting a much wider range of essentials for orders Myth Buster segment Applying predictive model to generate more insights based on the data given Applying real-life data streaming using Apache Kafka for a better data pipelining scalability to the admin. Implementing the complaint feature of the chatbot, so people can speak up straight and let governing bodies listen, then, applying real-life text analytics based on the users major complaint about the current situation. Adding more tight encryption for the security purpose of the voice from users due to privacy reasons using data hiding techniques such as steganography. <div