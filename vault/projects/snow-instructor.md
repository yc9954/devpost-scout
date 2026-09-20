---
slug: "snow-instructor"
url: "https://devpost.com/software/snow-instructor"
title: "Snow Instructor"
hackathon: "THE FUTURE OF AI IS OPEN"
organization: "Snowflake"
winner: true
words: 637
team_size: 1
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "substrate/code_repository"
  - "substrate/web_dom"
---

# Snow Instructor

> Master Snowflake by playfully answering questions and collecting points.

[Devpost](https://devpost.com/software/snow-instructor) · hackathon [[THE FUTURE OF AI IS OPEN]]

## Facets

**substrate** [[code_repository]] [[web_dom]]

**stack** arctic, hatch, python, scrapy, snowflake, snowpark, streamlit

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for snow instructor
- snowflake deployment

## Body

Meet your Snow Instructor! Inspiration Our Snow Instructor project was inspired by the quiz show "Who Wants to Be a Millionaire?" and the fact that our team was looking for a fun way to learn and test their Snowflake knowledge. We also drew inspiration from real-world AI and Streamlit applications, as we wanted to combine common components into an easy-to-understand application that could be used for learning purposes by exploring the source code. What it does Our application crawls the Snowflake documentation at https://docs.snowflake.com/en/ and saves it in a Snowflake table. This is done in an initialization step. The actual Snow Instructor app is now a Streamlit app that reads a page from the stored Snowflake documentation and passes it to the Artic LLM to generate a question. This question is now presented to the user as a quiz with four possible answers to choose from. The user selects an answer and is rewarded with points and snappy comments from the game master :-) How we built it We used the cookiecutter template hatchlor to start our Python project with a modern setup and common best practices. Then we used scrapy to scrape the Snowflake documentation, markdownify to shrink the HTML pages without losing semantic information, typer and hatch to create command line scripts for the setup, the Snowflake & Snowpark Python API to access Snowflake, Snowpark as well as the Cortex functions, especially Artic, and finally Streamlit to link everything together. We also used the Snowflake CLI to make the deployment of the app on Snowflake really easy. Challenges we ran into One challenge was the fact that Streamlit on Snowflake still only supports Python 3.8, while we wanted to use a more modern version for better type hinting support. This wasn't really a problem, but we had to rewrite our code a bit when we started deploying to Snowflake. Likewise, some Streamlit functions like switch_page are currently not available on Snowflake, so we had to introduce a special code path for our Streamlit app when it runs on Snowflake. Accomplishments that we're proud of We are very proud that our app demonstrates the key components of an AI-based app to the user in a simple and fun way. Since our project setup utilizes the latest best-practice development methodologies as well as Snowflake features and tools, we provide a holistic yet simple overview of what is possible with Snowflake and Streamlit. We'd also like to mention a few special tidbits, such as prefetching quiz questions using concurrent.futures and various advanced Streamlit features to top it all off :-) What we learned We learned how easy it is to develop an AI-based, user-centric application from start to finish with Snowflake and Streamlit. Developing and deploying a Streamlit and Snowflake based AI app really is a bliss and the new Snowflake Arctic LLM as well as the Cortex API in general, are easy to use and fun. Overall it took us less than two working days from the first idea to our final version. What's next for Snow Instructor First and foremost, Snow Instructor is used internally at inovex to make learning Snowflake more enjoyable. Since our app is released under the permissive MIT license, we hope that it will also help others to learn about Snowflake, not only by playing quizzes, but also by looking at the source code and learning from it. We also welcome PRs and further improvements to the app. A future feature is that users will be able to select quiz questions from different topics to enable a more topic-based approach to learning. The topic data from the Snowflake documentation is already extracted and available in Snowflake. Snowflake deployment Check out the Snowflake deployment on a Snowflake trial account until 2024-06-02 with user name anonymous and password Public1234 . Please play nice! <div