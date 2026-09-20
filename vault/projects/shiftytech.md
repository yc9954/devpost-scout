---
slug: "shiftytech"
url: "https://devpost.com/software/shiftytech"
title: "ShiftyTech"
hackathon: "Hack the North 2023"
organization: "Techyon"
winner: true
words: 671
team_size: 4
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/retrieval_grounding"
  - "mechanism/structural_withholding"
  - "domain/developer_tools"
  - "user/developer"
  - "substrate/structured_db"
  - "substrate/video_visual"
  - "substrate/web_dom"
---

# ShiftyTech

> Dance dance revolutionize the way you code!

[Devpost](https://devpost.com/software/shiftytech) · hackathon [[Hack the North 2023]]

## Facets

**mechanism** [[retrieval_grounding]] [[structural_withholding]]
**domain** [[developer_tools]]
**user** [[developer]]
**substrate** [[structured_db]] [[video_visual]] [[web_dom]]

**stack** .tech, machine-learning, nextjs, pose-estimation, python, replit, typescript

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for shifty tech

## Body

Jort, our mascot, based off of Mort from Madagascar Inspiration We planned weeks ahead to do a hardware hack but on the day of the event, we couldn't secure the hardware within reasonable starting time. As such we were contemplating our future in the lineup for the funnel cakes, when suddenly we were blessed with a vision from the future: coding through interpretive dance. Jokes aside, we noticed that a lot of programmers spend a lot of time sitting at their desk. This is atrocious for your physical and mental well-being: insufficient physical activity is the 4th leading risk factor for death and is responsible for 3.2 million deaths per year worldwide ( citation ). Shifty Tech enables programmers to be productive and get their morning yoga done at the same time. What it does Unlike treadmills under tables or other office products, Shifty Tech fuses physical exercise and programming so that movement is the source of productivity. Upon running our program, you will see a camera appear that tracks your movement. Every a few seconds, a frame will be captured and translated into Python code. We don't aim for efficiency. We aim to improve the mental and physical health of fellow programmers by recovering the creativity and joy they experience when they complete a program that was difficult to write, through dance-like exercise. Our project help programmers truly enjoy every component that goes into making their programs run. How we built it The backed manoeuvre for recognizing user poses was done in Python, with the pose estimation model TensorFlow MoveNet Thunder. The output of our MoveNet Thunder model was a multi-dimensional tensor that we flat-mapped and normalized into its vector representation, which is stored on Milvus through the Google Cloud Platform. Our website and code-editing is done through Replit, Next, and TypeScript. Our domain name is from .Tech and deployed on Vercel. Challenges we ran into There were a number of challenges that we ran into. First, we went through a variety of pose estimation models before settling on TensorFlow Thunder, such as TensorFlow MoveNet Lightning and Openpose. Each had their own benefits and drawbacks; for example while the Lightning model was very fast, it compromised on accuracy. Finding the right model for our live recognition took some time. We also tried a few different ways of storing our vector representations of our data. As our product interprets the poses live, optimizing the speed in which we interpret images matters. We tried Google Cloud for an instantiation of a virtual machine and MongoDB for their vector database, but settled on Milvus for optimizing running kNN on all the pose categories. Accomplishments that we're proud of For some of us, this was our first hack-a-thon and we were really proud of how we were able to create a full-fledged programming language using the full human body, which is something we've never seen before. Not only were we able to make that happen, we were also able to divide our time well and work diligently, so that we were able to deploy a full website dedicated to our new language as well. What we learned That cold showers are absolute doodoo. As well, we learned the hard way that when different local machines have different permissions and abilities, that can result in many many hours of debugging to change one line of code. What's next for Shifty Tech Shifty Tech has a lot more in store and there are many functionalities that could be added to the existing MVP. For example, you could add increased functionality in types of poses to increase editing and flexibility with your code. You could record a short video and upload it to Shifty Tech and have it return the result of your video to you, as opposed to solely coding live. Since Replit also allows for collaboration, we could extend the Shifty Tech functionality to include collaboration on the same code as well. We're excited for all the ways Shifty Tech can continue to evolve! <div