---
slug: "vitality-ev0qpb"
url: "https://devpost.com/software/vitality-ev0qpb"
title: "Vitality"
hackathon: "Boost Hacks II"
organization: "Boost Hacks"
winner: true
words: 896
team_size: 1
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "domain/education"
  - "domain/mental_health"
  - "user/educator_student"
  - "substrate/structured_db"
  - "substrate/web_dom"
---

# Vitality

> A comprehensive health and wellness app that seeks to address and improve the declining health of first-gen, low-income students.

[Devpost](https://devpost.com/software/vitality-ev0qpb) · hackathon [[Boost Hacks II]]

## Facets

**domain** [[education]] [[mental_health]]
**user** [[educator_student]]
**substrate** [[structured_db]] [[web_dom]]

**stack** code.org, css, flask, html, javascript, openai, python, vercel

## How they structured the write-up

- inspiration
- what it does
- how i built it
- challenges i ran into
- accomplishments that i'm proud of
- what i learned
- what's next for vitality

## Body

Login / Signup Page Menu Page Resilience Reminders (Community Building Feature) Page Journaling Page FitBot Page Inspiration Many first-gen, low-income students face significant challenges in maintaining their mental and physical health due to the inundating stresses of their environment. In fact, in an article by the LA Times , a survey was commissioned to identify the top concerns of today's first-generation college students; 65% of respondents said they struggled with their mental health, with loneliness playing a big role in it. My app, Vitality, is a comprehensive health and wellness app - completely free of charge - which aims to support these students by providing comprehensive resources (journaling prompts and a community building feature), and personalized AI-powered guidance to help them achieve a balanced and healthy lifestyle. What it does Vitality has three main features - Resilience Reminders, Journaling Prompts, and FitBot (A Health and Wellness Chatbot). Resilience Reminders allows the user to gain motivation, insight, and advice from other FGLI scholars, ensuring that they never feel alone, and that there are others who are going through the same process as them. The journaling feature offers an introspective way to learn more about oneself and set goals, with evidence showing that writing out emotions and thoughts significantly improves mental health, while setting achievable goals can improve self-esteem and motivation. FitBot is an AI-powered chatbot that answers any health and wellness questions users may have, and can also serve as a friend when needed. How I built it My application has two main components: the main app and FitBot. The main app was built using Code.org's App Lab, incorporating (an unconventional form of) JavaScript, HTML, and CSS. I created record-synced Data Tables (databases on Code.org) to store user logins, journal prompt entries, and Resilience Reminders, making the stored information accessible even if the user logs out of their account. As such, this allows the user to have their own account, and store information that only belongs to them (ex. their journal prompt entries, login info). FitBot, on the other hand, was developed in Visual Studio Code, using HTML and CSS for the frontend, and Python with Flask for the backend. Despite being developed separately, FitBot is still linked within the main app, and is an integral part of the main app. For the deployment of FitBot, I used Vercel. In the beginning of this project, I knew I wanted to integrate AI, as it is a really fascinating feature that can provide more personalized support and enhance the user's experience. I did this using OpenAI's API (GPT-4o mini model), and integrating it into the Python + Flask backend. Most of the visuals within my Code.org app were created in Canva. Challenges I ran into Prior to this, I had never worked with HTML, CSS, Github, or Vercel, so there were a lot of things I needed to figure out within the given timeframe. I wanted to work with OpenAI's API to build FitBot, but I had never done so before, so I had to quickly learn how to integrate it into my project. This required knowing how to send queries to APIs, receive responses, handle them, and make sure the data was processed properly. Because I was unfamiliar with using Flask and HTML/CSS, I had difficulty connecting my frontend to my backend. With that being said, I still couldn't format the response string from the OpenAI API. Vercel was also an unfamiliar environment for me, so when I attempted to deploy FitBot on Vercel, I kept getting 404 errors. Lastly, due to security restrictions on Code.org, I was unable to utilize 'get' requests from the App Lab API directly to FitBot. As a result, I had to use a button on Vercel to redirect the user from Vercel (FitBot) to Code.org (Home/Main App), and another button on Code.org to redirect the user from Code.org to Vercel. Accomplishments that I'm proud of This is my first coding project, and I am proud of myself for going outside of my comfort zone and actually creating something that has the potential to make an impact. Integrating an advanced artificial intelligence model within my application, despite having a really simple interface, was a great achievement for me. Even with many other endeavors taking place during this hackathon, I was still able to complete a rudimentary version of Vitality. What I learned This hackathon was an invaluable learning experience, as I got to learn more about basic HTML/CSS, Flask, APIs, and Github. Software is already redefining the way we perceive the world, solving issues that have been pressing society for a long time, and I am glad that I got the opportunity to explore that. What's next for Vitality In the long run, I plan to code the main app (from Code.org) into a more widely recognized IDE, such as VSCode. With that, I will plan on making FitBot accessible right from the main app, from which both components are on the same platform. I will also focus on adequately formatting the strings to enhance readability. In future iterations, I will also plan on making the application more secure and free from malicious intent/language. By gathering user feedback, I can improve the app's features even more, of which I am excited to see what the future holds for Vitality, and the impact that it can bring to the first-gen, low-income population. <div