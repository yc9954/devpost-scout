---
slug: "activate-hackers"
url: "https://devpost.com/software/activate-hackers"
title: "Moodify"
hackathon: "Atlas Madness"
organization: "Google"
winner: true
words: 1107
team_size: 4
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "domain/health_clinical"
  - "domain/mental_health"
  - "user/legal_professional"
  - "substrate/structured_db"
  - "substrate/video_visual"
  - "substrate/web_dom"
---

# Moodify

> Moodify is a comprehensive web application that harnesses the power of ML, MongoDB and Google Cloud Platforms to provide an inclusive solution for mental health improvement.

[Devpost](https://devpost.com/software/activate-hackers) · hackathon [[Atlas Madness]]

## Facets

**domain** [[health_clinical]] [[mental_health]]
**user** [[legal_professional]]
  <sub>weak: patient_family</sub>
**substrate** [[structured_db]] [[video_visual]] [[web_dom]]

**stack** bootstrap, container-registry, docker, express.js, flask, google-cloud-run, huggingface, mongodb, mongoose, node.js, react, typescript

## Body

Moodify Logo Architecture Diagram Inspiration According to the World Health Organization in 2022, mental health conditions such as depression and anxiety have been on the rise. In response to this worrying trend, the Virtual Visionaries went out to ideate on creating a journaling platform to help users jot down their thoughts and seek professional help as needed. With that, Moodify was created, employing the power of Machine Learning and Artificial Intelligence, MongoDB and Google Cloud Platforms to deliver a comprehensive web application to support and help users along on their mental health journey. What it does We envision Moodify to be an all-encompassing application when it comes to bettering one's mental health. The features surrounding Moodify revolve around the concept of journaling, which according to Smyth et al. (2018) has provided strong evidence of alleviating the symptoms of depression and anxiety. There are 4 main features to the application. Track your mood Importance of feature With the increasingly stressful and hectic lifestyles that many are leading today, mental health issues are also escalating at a terrifying rate. It is more important now than ever to take a step back and journal our thoughts to relieve the stress we are feeling. We understand that it is difficult for people with mental health issues to approach this topic to their loved ones blatantly. Hence we decided to implement this feature to allow them to journal their thoughts freely without having to face the judgements of others. Instead, their loved ones will be notified if the user is showing extreme signs of distress which could pose a danger to his or her lives. Besides, it is proven that penning down your feelings helps you gain a greater control over your emotions and improve your mental health. Feature Breakdown Making use of a calendar flipbook style, users can jot down their feelings for the day and refer back to them later on. This journal entry will be passed to our ML model that we deployed using the Google Cloud Run service which would classify the emotion of the text to be stored in the MongoDB database. The users’ therapist will be notified of their emotion when the user has done their journaling for the day Streak count to notify the users therapist and/or emergency contact if the user failed to fill up the journaling for a number of days deemed as worrying by the heuristics Therapists and/or the user's chosen emergency contact will receive a SOS notification if the user displays extreme signs of distress as determined by our AI model Grateful Importance of feature: Research done by Harvard Business Review in 2016 found that by thoughtfully reflecting on several things one is grateful for every day, it builds mental resilience and brings users a more optimistic outlook on life. Thus, we decided to implement this feature, albeit simple, that can positively impact the users emotions. Noting down things that they are grateful for enables them to look back when they are feeling down to boost their mood as well. Feature Breakdown Users list down the things they are grateful for in the day All the gratitudes will be collated and saved into the database, allowing them to look back Video Consult Importance of feature: Although the number of people suffering from mental health issues are increasing, there are statistics showing that a large proportion of them seeking help from a therapist is very low. This is due to their fear that society still holds a stigma towards people with mental health issues. Therefore, we chose to implement this feature to ease the process for our users to speak to a therapist without any judgements. With just a simple few clicks on the website, users can quickly and easily get the help they need, conveniently in the comforts of their home. Feature Breakdown Users can select from a list of therapist who are available to assist them at their preferred time Users can reach out to a licensed therapist that we onboard onto our mental health program via video calling through our application directly (Integration of video calling into application to be implemented in the future) Resources Importance of feature: The resources for mental health issues are abundant but scattered all over the internet. Furthermore, people may not know what resources they are or should be looking for. Thus, this feature allows them to have the most important informations compiled all into just one website for their convenience. Feature Breakdown Tips on managing stress and feelings are consolidated on the resources page Future Plans That's not all! Our team has many other ideas to make this application even better. However, due to the time constraints, we are unable to implement all of them. Some of our future plans include: Porting over our web application into a mobile application as we believe that it is more user-friendly and convenient for our users. Include gamification aspects to further motivate people to use the application to reap the most benefits out of it, i.e. to be more encouraged to journal daily and write things that they are grateful for. In turn, this will improve the data for our ML model to determine the mental state of the user Integrating a chatting feature so that the therapist can check in with their patients periodically Improved SOS notification to allow their therapist and/or emergency contact to view the live location of the user when a extreme distressed SOS notification is sent Fully integrate the video calling function with Google Meets Load randomised motivational and inspirational quotes/messages popup on launching the application Challenges we ran into The main challenge we ran into came from ideating the features that would integrate well together to achieve our goal of improving our user's mental health holistically. From daily journaling to consultations with therapists, Moodify could then position itself as an all-in-one application to achieve the goals we strove to accomplish. Accomplishments that we're proud of Integrating Google Cloud Platforms into our application. Being university undergraduates, we did not have much exposure to cloud concepts and products. With that, learning and understanding the different products that GCP had and how to use them was slightly challenging but we managed to pull through in the end! Reflecting back, this hackathon gave us the valuable opportunity to work on a meaningful project that solves a pertinent problem that is extremely close to our hearts. At the same time, it enabled us to gain exposure to the power of the cloud using Google Cloud Platforms which we are very excited to continue exploring and create more impact on the world we live in. <div