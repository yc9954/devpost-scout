---
slug: "virgo-etfnya"
url: "https://devpost.com/software/virgo-etfnya"
title: "Virgo"
hackathon: "Google's Women Techmakers presents She Builds AI"
organization: "Google"
winner: true
words: 843
team_size: 1
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "mechanism/simulation_digital_twin"
  - "mechanism/vision_ocr"
  - "domain/labor_employment"
  - "substrate/structured_db"
---

# Virgo

> Virgo is an AI-powered app that promotes economic empowerment & leadership for women and girls by providing them with a highly customizable suite of tools to assist them in their job-seeking journey.

[Devpost](https://devpost.com/software/virgo-etfnya) · hackathon [[Google-s Women Techmakers presents She Builds AI]]

## Facets

**mechanism** [[realtime_stream]] [[simulation_digital_twin]] [[vision_ocr]]
**domain** [[labor_employment]]
**substrate** [[structured_db]]

**stack** dart, firebase, firestore, flask, flutter, gemini, google-cloud, python

## How they structured the write-up

- inspiration
- what it does
- how i built it
- challenges i ran into
- accomplishments that i'm proud of
- what i learned
- what's next for virgo

## Body

Virgo Inspiration Virgo was born out of the need to address the systemic barriers women and girls face in the workforce. This project seeks to address the underrepresentation of women in leadership roles and aims to increase the lower global labour force participation rate of women compared to their male counterparts. According to the World Economic Forum, the proportion of roles held by women falls dramatically from entry-level (~50%) to C-suite (~25%) . In STEM roles, it drops all the way to 12%. I wanted to create a tool that could level the playing field, offering women resources to succeed in their careers. Virgo was designed to give women the confidence, guidance, and personalized support they need to break down barriers and to open doors to meaningful employment opportunities. What it does Virgo is an AI-powered career development app that helps women optimize their job-seeking journey by aligning their career goals with actionable insights. The app has several features that empowers women to present their best selves to their future employers. The Gemini model analyzes their resumes, as well as relevant details of the jobs there are targeting to generate the following: A comprehensive skills gap analysis that offers clear insights into the areas that they need to improve on and actionable recommendations on how to up-skill themselves accordingly Tailored learning pathways that will enable them to acquire the skills they need to excel Interview questions to simulate the job application process and to allow them to anticipate employer expectations A customizable professional cover letter to help them stand out in the competitive job market Virgo serves as a mentor, a coach, and a guide, helping women make informed decisions to unlock new career opportunities. How I built it Virgo was developed using Google AI technologies , primarily the Gemini API , and other GCP products like Flutter and Firebase. The frontend of the app was built with Flutter, ensuring a smooth and intuitive user experience across platforms. Firebase was used for authentication, database management, and storage, providing a reliable and scalable backend infrastructure. To power the core features of Virgo, I integrated the Gemini API with a Flask server, enabling advanced natural language processing (NLP) to extract and analyze resumes and job descriptions. I used the Gemini 1.5 Flash model to match users' skills with the job requirements and to ultimately generate the skills gap analysis, the learning pathway, the interview questions, and the cover letter for the users. I also used AI Studio for experimentation purposes. Challenges I ran into Leveraging generative AI to build a tool that is both maximally accurate and flexible came with its challenges. One of the primary obstacles was ensuring that the output was both personalized and precise, as every woman's career journey and experiences are unique. Finding the right balance between generating insightful and personalized content while maintaining accuracy was tricky. Experimenting with different prompt engineering techniques was crucial in striking this balance, allowing the model to generate compelling, customized results that met the diverse needs of users. Accomplishments that I'm proud of I am incredibly proud of the positive response I received after pilot testing Virgo with a small group of 5 women who were actively seeking employment opportunities in different fields. Out of the 5 women whom I shared access to, 2 of them have already landed jobs, which speaks volumes about the tool's effectiveness. This validated the concept and showed the real-world impact of Virgo. Some key testimonies that demonstrate the real-world impact of Virgo are: "Virgo has allowed me to take control of my professional growth. Before using Virgo, I struggled to find training resources and felt overwhelmed whenever I would try to look for them myself. The skills gap analysis helped me identify exactly where I needed to focus, and the learning pathway gave me a clear direction." "I used the interview questions to prepare for my technical interview, and I was pleasantly surprised by how relevant they were. I felt so much more prepared going into the interview." What I learned Through developing Virgo, I gained valuable insights into the complexities of women’s professional journeys and the challenges they face in the workforce. I learned the immense value of personalized feedback, realizing how small adjustments can significantly impact career trajectories. This project also highlighted the potential of AI to democratize access to employment and educational opportunities, offering women the tools they need to overcome barriers. Lastly, I discovered the critical role of continuous iteration in prompt engineering when working with LLMs. What's next for Virgo I plan to expand Virgo’s capabilities by integrating real-time job market insights, enabling users to receive up-to-date recommendations based on market trends and demands. I would also like to enhance the learning pathways by partnering with educational platforms to offer seamless access to relevant courses and certifications. Additionally, I want to scale the app by introducing a robust analytics dashboard so users can track their career progress. Ultimately, Virgo will continue evolving to empower women globally, helping them achieve their highest career aspirations. <div