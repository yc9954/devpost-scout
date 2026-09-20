---
slug: "nowaste-ai"
url: "https://devpost.com/software/nowaste-ai"
title: "NoWaste.ai"
hackathon: "TreeHacks 2024"
organization: "TreeHacks"
winner: true
words: 845
team_size: 4
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/sensor_fusion"
  - "domain/agriculture_food"
  - "user/general_public"
  - "substrate/video_visual"
---

# NoWaste.ai

> Providing a practical and scalable solution to every-day food waste.

[Devpost](https://devpost.com/software/nowaste-ai) · hackathon [[TreeHacks 2024]]

## Facets

**mechanism** [[sensor_fusion]]
**domain** [[agriculture_food]]
  <sub>weak: housing_homeless</sub>
**user** [[general_public]]
**substrate** [[video_visual]]

**stack** flask, javascript, openai, python, raspberry-pi, react, swift, tailwind, togetherai

## How they structured the write-up

- our inspiration
- what do we do?
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what's next for nowaste.ai

## Body

Our Raspberry Pi and TreeHacks-made housing Our Postman API Integration Our app solution UI Our Inspiration Have you ever looked inside the fridge, saw a particular piece of food, and wondered if it was still edible? Maybe you felt it, or looked it up online, or even gave it the old sniff test! Yet, at the end of the day, you still threw it away. Did you know that US citizens waste an average of 200lbs of food per year, per person? Much of that waste can be traced back to food casually tossed out of the fridge without a second thought. Additionally, 80% of Americans rely on the printed ‘best by’ dates to determine if their food is still fresh, when in reality it is almost never a true indicator of expiration. We aim to address these problems and more. What do we do? NoWaste.ai is a two-pronged approach to the same issue, allowing us to extend our support to users all over the world. At its core, NoWaste allows users to snap photos of an edible product, describe its context, and harness the power of generative AI to receive a gauge on the quality of their food. An example could be the following: "Pizza left on a warm counter for 6 hours, then refrigerated for 8" + [Picture of the pizza], which would return the AI's score of the food's safety. In developed countries, everyone has a smartphone, which is why we provide a mobile application to make this process as convenient as possible. In order to create a product that users will be more likely to consistently use, the app has been designed to be extremely streamlined, rapidly responsive, and very lightweight. However, in other parts of the world, this luxury is not so common. Hence, we have researched extensively to design and provide a cheap and scalable solution for communities around the world via Raspberry Pi Cameras. At just $100 per assembly and $200 per deployment, these individual servers have potential to be dispersed all across the world, saving thousands of lives, millions of pounds of waste, and billions of dollars. How we built it Our hardware stack is hosted completely on the Raspberry Pi in a React/Flask environment. We utilize cloud AI models, such as LLAMA 70B on Together.ai and GPT4 Vision, to offload computation and make our solution as cheap and scalable as possible. Our software stack was built using Swift and communicates with similar APIs. We began by brainstorming the potential services and technologies we could use to create lightweight applications as quickly as possible. Once we settled on a general idea, we split off and began implementing our own responsibilities: while some of us prototyped the frontend, others were experimenting with AI models or doing market research. This delegation of responsibility allowed us to work in parallel and design a comprehensive solution for a problem as large (yet seemingly so clear) as this. Of course, our initial ideas were far from what we eventually settled on. Challenges we ran into Finalizing and completing our stack was one of our greatest challenges. Our frontend technologies changed the most over the course of the weekend as we experimented with Django, Reflex, React, and Flask, not to mention the different APIs and LLM hosts that we researched. Additionally, we were ambitious in wanting to only use open-source solutions to further drive home the idea of world-wide collaboration for sustainability and the greater good, but we failed to identify a solution for our Vision model. We attempted to train LLAVA using Intel cloud machines, but our lack of time made it difficult as beginners. Our team also faced hardware issues, from broken cameras to faulty particle sensors. However, we were successful in remedying each of these issues in their own unique ways, and we are happy to present a product within the timeframe we had. Accomplishments that we're proud of We are incredibly proud of what we were able to accomplish in such a short amount of time. We were passionate about both the underlying practicalities of our application as well as the core implementation. We created not only a webapp hosted on a Raspberry Pi, equipped with odor sensors and a camera, but a mobile app prototype and a mini business plan as well. We were able to target multiple audiences and clear areas where this issue prevails, and we have proposed solutions that suit all of them. What's next for NoWaste.ai The technology that we propose is infinitely extensible. Beyond this weekend at TreeHacks, there is room for fine-tuning or training more models to produce more accurate results on rotting and spoiled food. Dedicated chips and board designs can bring the cost of production and extension down, making it even easier to provide solutions across the world. Augmented Reality is becoming more prevalent every day, and there is a clear spot for NoWaste to streamline our technology to work seamlessly with humans. The possibilities are endless, and we hope you can join and support us on our journey! <div