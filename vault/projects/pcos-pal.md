---
slug: "pcos-pal"
url: "https://devpost.com/software/pcos-pal"
title: "PCOS Pal"
hackathon: "TreeHacks 2023"
organization: "Stanford TreeHacks"
winner: true
words: 602
team_size: 1
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/vision_ocr"
  - "domain/health_clinical"
  - "user/patient_family"
  - "user/researcher"
  - "substrate/structured_db"
  - "substrate/video_visual"
  - "substrate/web_dom"
---

# PCOS Pal

> Using machine-learning to aid in pcos diagnosis and awareness

[Devpost](https://devpost.com/software/pcos-pal) · hackathon [[TreeHacks 2023]]

## Facets

**mechanism** [[vision_ocr]]
**domain** [[health_clinical]]
**user** [[patient_family]] [[researcher]]
**substrate** [[structured_db]] [[video_visual]] [[web_dom]]

**stack** express.js, flask, intersystems, mongodb, node.js, python, react, sqlalchemy

## How they structured the write-up

- inspiration
- what it does
- how i built it
- challenges i ran into
- accomplishments that i'm proud of
- what i learned
- what's next for pcos pal

## Body

Inspiration Polycystic Ovary Syndrome, or PCOS, is a chronic condition known as the most prevalent endocrine–metabolic disorder, affecting around 6–10% of reproductive-aged women across the world. The exact cause is unknown and there is no direct cure, but the symptoms can be treatable. While there is not a specific test to diagnose PCOS, a diagnosis would commonly require at least 2 of the 3 following features: polycystic appearing ovaries, hyperandrogenism, and amenorrhea. An internal ultrasound is a common method of examination; however, they are not recommended for women younger than 20 years, thus making PCOS difficult to spot in early adulthood. The reality is that many people go undiagnosed. In a study done by Monash Centre for Health Research and Implementation, researchers found that people who have PCOS commonly reported that they were unsatisfied with their overall diagnosis experience, including the information provided about the condition, the number of health professionals they had to see, and the wait time for diagnosis. PCOS affects physical health and mental well-being over the life span, and a delay in diagnosis can exacerbate these effects and even lead to more long-term health complications. As someone who is experiencing the difficulties associated with PCOS, I wanted to come up with an application that could assist in the diagnosis process. What it does Anyone can have access to a questionnaire that will calculate the risk or likelihood of having PCOS, there is a log-in feature using authentication and logged in users will have access to other parts of the website. How I built it I utilized a dataset that has different fields containing symptoms or conditions that could be useful to predict PCOS, such as ovarian follicle size, cycle length, and whether the patient has an irregular cycle. I did pre-processing and then learned how to use Intersystems IntegratedML to train and validate models. Challenges I ran into Connecting the database to my application took a while and I also completely switched tech stacks in the middle of the development process and wasn't sure how to transfer things over. There is a lack of robust data on PCOS or PCOS symptoms, so the dataset I used was on the smaller side (542 rows) and was unbalanced. For one feature, I was running into problems with deploying semantic analysis with good accuracy. I also was working on image classification to detect PCOS in python using ultrasound images, but there were time constraints and unfortunately, I could not fully implement it, although I was most excited about that part. Accomplishments that I'm proud of I decided to work on something that strays away from what I normally do, which meant spending a lot of time learning and experimenting. I am proud that I ended this with a working model that can predict PCOS and I am walking away with new skillsets. What I learned I am excited that I had the opportunity to learn a different way of database management. I learned how to train models using Intersystems integrated ML and also how to use flask. I strengthened my SQL and python skills. What's next for PCOS Pal There are several other endpoints I would like to continue developing, such as daily mood check-ins and journal entries that could be analyzed with NLP. I also want to have a platform where people with PCOS can review birth control along with other common methods of treatment. To tie it all together, I want to have a better UX/UI design. I have a lot of visions for this product and hope to continue developing it to help other people like me. <div