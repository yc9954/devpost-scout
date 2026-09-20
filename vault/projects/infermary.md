---
slug: "infermary"
url: "https://devpost.com/software/infermary"
title: "INFERmary"
hackathon: "Cal Hacks 11.0"
organization: "Cal Hacks"
winner: true
words: 1292
team_size: 4
has_repo: false
has_live: false
has_video: false
tags:
  - "project"
  - "mechanism/simulation_digital_twin"
  - "domain/disaster_emergency"
  - "domain/health_clinical"
  - "domain/media_journalism"
  - "user/clinician"
  - "user/legal_professional"
  - "user/patient_family"
  - "substrate/geospatial"
---

# INFERmary

> Simulating virtual cities to outsmart viral outbreaks

[Devpost](https://devpost.com/software/infermary) · hackathon [[Cal Hacks 11.0]]

## Facets

**mechanism** [[simulation_digital_twin]]
**domain** [[disaster_emergency]] [[health_clinical]] [[media_journalism]]
**user** [[clinician]] [[legal_professional]] [[patient_family]]
**substrate** [[geospatial]]
  <sub>weak: code_repository</sub>

**stack** fast, fetch, groq, mapbox, python, react

## How they structured the write-up

- 💥 how it all started
- 📖 what it does
- 🔧 how we built it
- 🚩 challenges we ran into
- 🏆 accomplishments that we're proud of
- 📝 what we learned
- ✈️ what's next for infermary
- 📋 evaluator's guide to infermary

## Body

### FOR EVALUATORS/SPONSORS: Scroll down for a handy guide to navigating our repository and our project's assets. 💥 How it all started I'm sure we're all well aware that having an informed response to an epidemic is crucial. The viral outbreak simulations that currently inform these responses are largely rules and statistics-based. These may work well at approximating human behavior, but they fail to account for how personal choices, life circumstances, and unpredictable interactions influence the spread of a virus. With the shadow of COVID-19 receding into the past, we thought it important to stay vigilant and look towards the future to safeguard our communities against the next outbreak, whenever it may be. We realized that having a more powerful simulation tool to test response plans before they happen would be one of the best ways to stay prepared, and we set our sights on finding a better way to model the spread of epidemics. By leveraging fetch.ai's ability to create AI agents that could act intelligently by themselves and interact organically with each other, we aimed to simulate a living, breathing city that could better model the nuanced nature of humanity that statistical models can only approximate. This allows for us to better capture the complex emergent behaviors of a community, and therefore better simulate viral outbreaks and the efficacy of potential responses. 📖 What it does Enter INFERmary , a simulation tool designed to realistically simulate an organic city and test out potential disaster responses. INFERmary starts out by getting context information about the city in question, like locations of interest. Using the city's demographic data, it then generates independent agents according to represent a scaled-down version of the city's population. The user can then tweak the virus spread parameters like its infectiousness and the number of initially infected patients, as well as add custom directions for the simulation. Here’s how INFERmary leverages advanced technologies to better achieve its goal: Intelligent AI Agents: Thanks to fetch.ai, our simulated city is populated by AI agents, each with their own real life. Every agent has a personalized profile, encompassing their age, socioeconomic status, habits, and more. They don’t just follow scripted paths—they generate their own daily routines, engaging in the kind of organic interactions you’d expect to see in any real-world city. Central Direction System: A central LLM system powered by Groq allows the user to act as a regulatory body and issue directives to all agents (such as enforcing a lockdown, setting mask mandates, or establishing vaccination campaigns), allowing for deep simulation of not only viral spread but also the societal response to those interventions. 🔧 How we built it To build INFERmary, we leveraged the power of generative AI to generate various personalities. These personalities are turned into their own individual Fetch.ai agents who control their own lives and communicate with each other. To power the generative abilities of our solution, we used Groq’s various hosted models. To visualize our agents, we display them on our React front end. Technologies: fetch.ai: Used for creating multiple AI agents for simulating Groq: Used for initializing all the AI agents as well as general LLM tasks Mapbox: Used to visualize the simulated agents in an intuitive way React: Used to create user friendly frontend 🚩 Challenges we ran into Alex: We were pretty tired of working with the same old LLMs and functions, so we wanted to experiment with something new this hackathon! I was responsible for generating people and implementing their actions with agents, and wow was it hard. Figuring out how to take advantage of agents fully was a tall task. I loved it though, it was something fresh and unique from what we usually do! Nicholas: The biggest challenge for me was wrapping my head around the paradigm shift from one or very few backend services to many agents that all communicate with each other. Most of my time was spent reading documentation and asking questions instead of coding which was interesting. 🏆 Accomplishments that we're proud of The ability to generate multiple AI agents with unique personalities and interests Implementing 📝 What we learned Alex: This is probably the last ever collegiate hackathon I'll ever be at, so I want this to be more of a reflection on everything I've done. I think the greatest lesson I learned here and everywhere else is my potential. I never guessed I would be able to do this much in such little time with other people. A lot can be done in an hour, and a lot more can be done in 36. Hackathons have given me so much confidence in my abilities and allowed me to have so much fun with my friends. Specifically here though, I also learned a lot about agentic AI and how versatile they are. I never expected how good they would be at checking each other and how much the agentic factor improves LLM and application performance. It was really fun using fetch.ai's technology! Ethan: I specifically wanted to approach Cal Hacks 11.0 with a focus on presentation and marketing, so I was the team's UX designer as well as marketing lead. It allowed me to see the project from a different angle than I usually tackle them from, and emphasized to me the importance of a good pitch. I think I've gained some valuable experience with selling our product and representing it in a way that not only plays to its strengths, but my and my teammates' strengths as well. Nicholas: I learned a lot about the use of AI agents. From what I’ve seen, utilizing multiple AI agents is the next big thing in tech. Being able to work with agent technology and see how others use it was very fun. Wesley: This was my first hackathon and keeping up with contributing to the project with other experienced members was definitely a challenge that many people overlook. I worked on and learned about frontend development using Reactjs and integrated Mapbox to render the map simulation environment. ✈️ What's next for INFERmary With a simulation system as advanced as INFERmary, simulating basic situations and outbreak reponses is just the tip of the iceberg! We've got a ton of ideas for INFERmary going forward to turn it into the best possible version of what it can be. AI Agent-Powered Outbreak Response Team: In addition to just dictating blanket commands, this will allow the user to act as the head of an outbreak response team, managing AI agents that fulfill the role of epidemiologists, onsite doctors, and more. This will allow for an even more in-depth simulation of a health agency's possible response to an outbreak. Mutating Viruses and Different Strains: Currently, the virus has set parameters at the beginning of the simulation. However, viruses could be simulated to mutate and develop into different strains with the passage of time, developing different transmission rates, mortality rates, or resistance to treatments. This would allow for a more comprehensive look at long-term epidemic management. Public Sentiment and Media Influence: We all have first-hand experience with how media and public influence shape the response to an epidemic. Simulating the influence of media, social networks, and public sentiment on behavior—such as how misinformation or social pressure might impact mask-wearing, social distancing, or vaccine uptake—could offer a unique insight into outbreak response in today's media-driven world. 📋 Evaluator's Guide to INFERmary Intended for judges, however the viewing public is welcome to take a look. Hey! We wanted to make this guide in order to help provide you further information on our implementations of certain programs and provide a more in-depth look to cater to both the viewing audience and evaluators like yourself. SPONSOR SERVICES WE HAVE USED THIS HACKATHON fetch.ai Groq <div