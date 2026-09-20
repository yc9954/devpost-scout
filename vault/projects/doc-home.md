---
slug: "doc-home"
url: "https://devpost.com/software/doc-home"
title: "Doc@Home"
hackathon: "Garuda Hacks 2020"
winner: true
words: 1272
team_size: 1
has_repo: false
has_live: false
has_video: false
tags:
  - "project"
  - "mechanism/voice_speech"
  - "domain/finance_payments"
  - "domain/health_clinical"
  - "domain/mental_health"
  - "domain/security_privacy"
  - "user/clinician"
  - "user/general_public"
  - "user/patient_family"
  - "substrate/structured_db"
  - "substrate/web_dom"
---

# Doc@Home

> A web app to help cope with the present pandemic

[Devpost](https://devpost.com/software/doc-home) · hackathon [[Garuda Hacks 2020]]

## Facets

**mechanism** [[voice_speech]]
**domain** [[finance_payments]] [[health_clinical]] [[mental_health]] [[security_privacy]]
**user** [[clinician]] [[general_public]] [[patient_family]]
**substrate** [[structured_db]] [[web_dom]]

**stack** bootstrap, css, flask, flowxo, mysql, python, sqlalchemy

## How they structured the write-up

- inspiration
- why doc@home: the innovative and social impact
- tech stack used
- future updates
- how i built it
- challenges i ran into
- accomplishments that i'm proud of
- what i learned
- what's next for doc@home

## Body

Inspiration The recent coronavirus had bought the entire world to a standstill. I wish to bring about a small change to this scenario and that was what inspired me to build this app Doc@home The spread of the pandemic has caused a lot of changes in our lifestyle, people fearing to get outside their homes, transportation almost shut down and social distancing becoming all the more important. The three major health issues that we face during this pandemic are the deterioration of mental health due to lack of socialization difficulty in getting medical appointments due to travel restrictions the uncontrolled spread of fake news. Doc@home is a web app build with an indention for helping to cope up with the current COVID situation. The app has 3 main features:- 1. Became an AI companion for those in quarantine “Connectedness is important to all humans, so I think we are all at risk [of loneliness during quarantine],” - Deborah Roth Ledley, PhD, a licensed psychologist in Pennsylvania The new reality of prolonged quarantine period and lack of socialization with other family members, friends and managing the fear of contracting the virus and worry about people close to us who are particularly vulnerable, are all challenging for each one of us. While the physical impact of COVID-19 can be assessed and treated, the mental impact is often ignored. Many people are experiencing emotional breakdowns and having depression. The new reality of prolonged quarantine period and lack of socialization are adding up the mental struggle. More than 50% of those suffering from mental health issues are not seeking treatment, due to social stigma. This present environment in the country has increased stress and anxiety amongst the citizens. Introducing to you Jessica, your very own AI companion. Jessica can help you overcome your isolation and loneliness. 2. Provide a connecting medium for doctors and patients But sometimes a chatbot might not be enough. You might need to seek professional help The fear of traveling has resulted in the hampering of checkups of many people. Doc@home, helps patients to take their routine checkups from the comfort of their homes without the scare of the virus. It helps any patient to connect with the doctor of their choice, from the list of available doctors, and book an appointment according to their convenience either in offline or online mode. The app has 2 portals, one for the patients requiring the appointment, and the doctors available for consultation. The patients can enter their medical history, any undergoing medication, etc which can be viewed by the doctor if he/she confirms their appointment. The index page of the patient and the doctor shows all their upcoming consultations. The doctor is notified if there are any patients requiring their appointment, and have the option to either confirm or deny, which causes a corresponding notification to be sent to the patient. The doctor can also send the prescription with detailed feedback to the patient after consultation, along with the consultation fee to be paid. The patient can view the feedback in the history tab of their portal, which also provides the facility to pay the consultation fee by redirecting them to the Google Pay web page. 3. Create a forum for discussion between ordinary users and doctors Another big issue that we face during this time, is the spreading of COVID related fake news. News with no scientific basis like standing in sun can kill corona and your pets can spread CoronA are rapidly spreadly It is estimated there over 800 deaths have occurred due to WhatsApp fake msg Doc@home also tackles this issue I have created a forum (inspired by stack overflow website) that could help people differentiate fake news from the real ones. Here people can raise doubts regarding different aspects of COVID and get answers from professionals. It is a community-driven platform where doctors and ordinary people can meet and help each other out. This forum, to some extend, would help ordinary people seek professional help and advice, and use it as a methodology to separate fake and actual news Although, it isn't much this is a humble step from my side hoping to bring our world to normalcy with the pandemic on the spread. Why Doc@home: The innovative and social impact ⚕️ Easy and affordable medical consultations, at the comfort of your home: On average, a telehealth visit costs about $79, compared with about $146 for an office visit, according to the study. With doc@home users can consult any doctor 24*7 from anywhere in the world and the appointment scheduling process occurs in one well-organized platform so the endless back and forth communication can be avoided 📹 Get a detailed medical prescription from verified doctors: After every session, you would receive detailed feedback from the doctor having all the details about the medicines to be taken, its quantity, the duration, etc 💊 One-stop solution to keep track of your medical history and remind you to take your pills: The platform gives a track of all our past medical details and family heredity details. It also gives you an option to share this info with the doctor of your choice. Getting the medical history of the patient would surely help the doctor make better choices. 🧘 AI companion for managing daily stress, anxiety, and depression issues. 🤯 Combats the social stigma surrounding the seeking of help for mental health issues: The chatbot in the app has the potential to be useful tools for individuals with mental disorders, especially those who are reluctant to seek mental health advice due to stigmatization. 📱 Platform to verify the truth behind viral messages surrounding health and stop the spreading of fake news : The app provides a medium for users to seek professional opinions from doctors related to various COVID topics Tech stack used The backend of the project uses flask(python) and SQLite as the database The front end is built on bootstrap, css, js and jquery Future updates Implement a blockchain payment system to bring more transparency and security to the system Integrate Twilio API to create a bot, that calls you/sends a message to your phone 5hrs prior to the appointment schedule Add to speech to text conversion in the chatbot. So instead of typing the queries, the users can simply talk more naturally with Jessica How I built it With sleepless nights and coffee :) Tech stack used: Flask, bootstrap, MySQL Installation - Fork & Clone the repo - Install all requirements: pip install -r requirements.txt - Run: python3 main.py - Copy the localhost url (usually localhost:5000/) and paste in browser Challenges I ran into Configuration trouble, the difficulty is retrieving data from DB Accomplishments that I'm proud of That I completed the entire project on my own. That's a huge accomplishment for me. Even when the problem kept on coming, I still kept on going What I learned A lot. I have learned how to integrate front end and backend in the flask. I also learned how to build a chatbot. The project also helped me sharpen my front end skills What's next for Doc@home Must work on the UI A few silly errors still exist. Need to debug them Need to improve the chatbot In the forum section, I would differentiate the answers given a professional and a normal user (in order provide from authenticity to the answer provided by a doc) Do some web scrapping to get more info Add ethereum code to the payment (the payment between the doc and user) and also in the forum section. This would provide more transparency and security to the platform <div