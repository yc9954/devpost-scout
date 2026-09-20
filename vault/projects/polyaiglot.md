---
slug: "polyaiglot"
url: "https://devpost.com/software/polyaiglot"
title: "LangUR"
hackathon: "TreeHacks 2024"
organization: "TreeHacks"
winner: true
words: 792
team_size: 4
has_repo: true
has_live: false
has_video: false
tags:
  - "project"
  - "mechanism/retrieval_grounding"
  - "domain/education"
  - "user/educator_student"
  - "substrate/sensor_telemetry"
---

# LangUR

> LangUR: Your language learning companion. Effortless fluency with personalized articles, translations, and progress tracking. Join us today, and master languages at your leisure!

[Devpost](https://devpost.com/software/polyaiglot) · hackathon [[TreeHacks 2024]]

## Facets

**mechanism** [[retrieval_grounding]]
**domain** [[education]]
  <sub>weak: security_privacy</sub>
**user** [[educator_student]]
**substrate** [[sensor_telemetry]]
  <sub>weak: web_dom</sub>

**stack** astro, bun, chromavectordb, flask, gpt, monsterapi, postmanapi, python, tailwindcss

## How they structured the write-up

- learning languages is one thing, but what does it take to be fluent in them?
- so the question stands: what helps set apart langur from language learning apps that help learners breach a beginner level of linguistic competence?
- efficiency. scalability. practicality.
- sample on a webpage
- research
- what's next for langur

## Body

Larsen the Lemur welcomes you on your language mastery journey! LangUR: Linguistic Mastery at Your Fingertips Learning languages is one thing, but what does it take to be fluent in them? LangUR is a groundbreaking project which bridges the difficult phases of learning languages. In a diverse business world with hundreds of languages being used in high commerical settings, modern applications serve to teach proficiency in langauges, but per a fluency study of Duolingo patrons learning French and Spanish, only 52.94% of 102 French learners reached a pre-intermediate level, and 66.03% of 156 Spanish speakers reached a similar level. (Jiang X, 2021) So the question stands: what helps set apart LangUR from language learning apps that help learners breach a beginner level of linguistic competence? Efficiency. Scalability. Practicality. Key Features: Uses a grounded evaluation metric to measure your performance (LIX scoring algorithm) Application learns and adapts to individual learner's abilities Learning of language conveniently incorporated into daily workflow Reinforced learning of queries words through review quizzes Development Tools: PostmanAPI: Testing and Integrating API Endpoints Between Frontend and Backend-> enabled synchronous development by different teams Testing of MonsterAPI's inference engine-> enable quick iteration and testing of various baseline models and their associated hyperparameters Facilitated collaboration between Frontend and Backend Team with a shareable link detailing communication format Bun: Leveraging Bun as a JavaScript ecosystem for web deployment ultra fast and all in one bundler, runtime and package manager that saved us a lot of time MonsterAPI: Fine tuning the baseline models and using the inference engines easy to access deployment and fine-tuning platform greatly reduced the learning curve round-clock support by staff made development easier Chroma Vector DB: Quick and reliable retrieval of semantic lists and articles for rapid processing with the LLM Engines. Tech Stack: Sample on a webpage Research The project's premise and continuity relies very heavily on social research. When Robin was learning his languages, he found that maintaining continuous performance on a daily basis aided his performance in learning a language, and such a trend is commonly correlated with higher testing proportions among students that are fed information on a consistent daily basis when studying, as demonstrated by the American Psychological Society (Mawhinney et al., 1971). Moreover, the concept of integrating language learning seamlessly into daily routines aligns with principles of habit formation and behavioral psychology. By embedding language practice within the natural flow of a user's day, LangUR capitalizes on the psychological phenomenon of habit stacking. This approach leverages existing habits as anchors for new behaviors, making language learning feel less like a burdensome task and more like an integrated aspect of daily life. Stacking habits is quintessential as evidenced for learning, so, how would one be able to consider a new approach to structuring a language learning app based off of this? Let's look back at the presented graph. In any instance, Distributed Practice and Practice Testing appear to be the largest factors associated with higher testing in general study areas, where we based our project idea off of: a gradual but slow streamline of language implementation, albeit slowly and consistently. By being passive and seamless, LangUR has the capability to gradually streamline language learning modes into a user's daily workflow, providing an excellent UI, with a diverse array of features such as translation, suggested articles based off of past history, and progressively improving the user's ability to take in the language with the readability algorithm. We often encounter the issue that learning a language is daunting, requiring continuous effort, where a lot of people simply don't have that time to invest, whereas the practicality of being fluent in languages has a high yield in business returns by eliminating barriers between multinational individuals and corporations. The idea behind LangUR had to critically emphasize the parallel and efficient nature of learning, which other applications failed to consider. Giving users a comfortable experience, automatically determining skill level through a customized LIX Algorithm, and structuring the application to cater to their learning pace was imperative during the building phase. In conclusion, taking into account human study patterns, the demanding needs of learning a language and daily time constraints, LangUR was built with the mindfulness that dedication is always on the users side, but we can do our job to make it as seamless as possible, accessible, and catered to the users. What's next for LangUR LangUR's potential is unbelievable. It has the ability to drive a stake in the educational world, collectivizing language learners, teachers, students, and anyone through simplicity. As the project's development continues, more functions will be added such as social integrations, connecting learners across the world, and more advanced algorithms will be put in place to create more personalized suggestions, helping people learn their new languages. <div