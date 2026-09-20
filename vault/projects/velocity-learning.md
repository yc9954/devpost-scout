---
slug: "velocity-learning"
url: "https://devpost.com/software/velocity-learning"
title: "Velocity Learning"
hackathon: "Youth Code x AI"
organization: "Youth Code Foundation"
winner: true
words: 734
team_size: 1
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "domain/education"
  - "user/educator_student"
  - "substrate/web_dom"
---

# Velocity Learning

> Empowering young learners globally through an AI platform that turns abstract science lessons into instant, tailor-made videos.

[Devpost](https://devpost.com/software/velocity-learning) · hackathon [[Youth Code x AI]]

## Facets

**domain** [[education]]
**user** [[educator_student]]
  <sub>weak: researcher</sub>
**substrate** [[web_dom]]

**stack** ai, google-cloud, html, media, python, react, visuals

## Body

Inspiration Every student learns differently, yet traditional education often relies on a "one-size-fits-all" approach. For visual learners, the internet is both a blessing and a curse. While the information exists, it is severely scattered across thousands of disconnected platforms, articles, and generic videos. Visual learners are left severely disadvantaged, spending more time hunting for clear, cohesive visual explanations than actually learning. I was inspired by a simple question: What if the perfect, visually rich science video didn’t just exist somewhere out there, but was created instantly just for you? I wanted to build a platform that acts as a personalized visual sandbox, turning abstract scientific concepts into custom animations on demand, tailored exactly to a student's level and learning pace. What it does Velocity Learning is an AI-driven educational platform that automatically generates hyper-personalized, high-quality science videos at remarkable speeds. Instead of scrolling through endless search results, a student simply enters what they want to learn to make a bespoke video featuring dynamic animations and tailored explanations. It acts as an on-demand, global educational companion that breaks down complex, abstract theories into clear visual intelligence. How I built it The backend of the project is essentially split into a video service and an audio service. The parameters which are chosen by the user are given to an LLM which generates the script. This audio service then uses TTS to produce human-like audio from the script provided. There will also a video service which makes visual animations for every scene within the video. This is then assembled in the frontend. The backend is written in python and the frontend is React based. Challenges I ran into One of the biggest hurdles was minimizing generation time to truly live up to the name "Velocity." Combining text processing, script generation, asset creation, and video rendering into an instantaneous pipeline required aggressive optimizations. Specifically, I faced two massive technical challenges during development: Humanizing the Audio: It was incredibly difficult to ensure that the generated video audio sounded human-like and natural rather than robotic. Perfecting the voice synthesis to keep students engaged took significant fine-tuning. Rendered vs. Non-Rendered Scalability: It was a big challenge for me to switch from fully rendered to non-rendered formats. I had to optimize the project heavily to ensure the entire system was as scalable as possible, making the video generation process highly cost-efficient without sacrificing quality. Accomplishments that I'm proud of I am proud of the time I have spent finding solutions to problems and the experience that I have gained along the way. Much of this was very new to me being a year 10 student myself who threw himself in the deep end. But this was the best decision that I made in my opinion as it taught me the importance of hard work and dedication to make something that I was truly proud of. Now I know how to talk to LLMs, I know the importance of prompt engineering and learning how to deploy my website to the cloud which meant using a container to ensure that my website was accessible to everyone. What I learned I learned that building for education requires a razor-sharp focus on voice modulation and clear animation to ensure cognitive retention. I also gained deep technical knowledge regarding voice AI synthesis and how to manage media rendering payloads across external API clusters. Ultimately, this project taught me how to architect an end-to-end platform with strict data security and cost-efficiency in mind. Something I have made sure is that my project was scalable and after this hackathon is over I will persist to add more parameters and expand it out of the UK syllabus and add in more subjects to welcome in all users on a global scale. What's next for Velocity Learning To scale the project globally, I plan to expand the content catalogue across multiple academic disciplines. On top of this, I want to introduce an interactive quiz feature at the end of each video to help students immediately test their knowledge retention to ensure that all my users revise actively in order to ace their exams. Additionally, I would like to include little fun facts around the chosen content to make it more interesting to my users. Being a student myself I will use my own site to help enhance my revision as I believe that Velocity Learning will truly accelerate anyone's intellect... <div