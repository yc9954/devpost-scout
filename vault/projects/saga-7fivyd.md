---
slug: "saga-7fivyd"
url: "https://devpost.com/software/saga-7fivyd"
title: "Saga"
hackathon: "TreeHacks 2023"
organization: "Stanford TreeHacks"
winner: true
words: 1182
team_size: 4
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "domain/immigration_refugee"
  - "domain/scientific_research"
  - "substrate/video_visual"
---

# Saga

> Custom, user driven bedtime stories for children using generative AI -- Saga makes reading more fun and educational

[Devpost](https://devpost.com/software/saga-7fivyd) · hackathon [[TreeHacks 2023]]

## Facets

**mechanism** [[realtime_stream]]
**domain** [[immigration_refugee]] [[scientific_research]]
**substrate** [[video_visual]]

**stack** express.js, flutter, mongodb, node.js, openai

## How they structured the write-up

- check out our site -> saga
- inspiration
- what it does
- how we built it
- challenges we ran into
- what we learned
- accomplishments that we're proud of
- what's next for saga
- references

## Body

Use Saga in 4 clicks to receive interesting, educational, and endless bedtime reading content! Saga is powered by AI to generate stories in real time from your input Rich imagery is generated in real time and will never be the same twice Readers are prompted to pick what they want to do next, and Saga changes the rest of the story based on their decisions Team Code on Tap going ham for 36 hours straight Check out our site -> Saga Inspiration There are few better feelings in the world than reading together with a child that you care about. “Just one more story!” — “I promise I’ll go to bed after the next one” — or even simply “Zzzzzzz” — these moments forge lasting memories and provide important educational development during bedtime routines. We wanted to make sure that our loved ones never run out of good stories. Even more, we wanted to create a unique, dynamic reading experience for kids that makes reading even more fun. After helping to build the components of the story, kids are able to help the character make decisions along the way. “Should Balthazar the bear search near the park for his lost friend? or should he look in the desert?” These decisions help children learn and develop key skills like decisiveness and action. The story updates in real time, ensuring an engaging experience for kids and parents. Through copious amounts of delirious research, we learned that children can actually learn better and retain more when reading with parents on a tablet. After talking to 8 users (parents and kiddos) over the course of the weekend, we defined our problem space and set out to create a truly “Neverending Story.” What it does Each day, Saga creates a new, illustrated bedtime story for children aged 0-7. Using OpenAI technology, the app generates and then illustrates an age and interest-appropriate story based on what they want to hear and what will help them learn. Along the way, our application keeps kids engaged by prompting decisions; like a real-time choose-your-own-adventure story. We’re helping parents broaden the stories available for their children — imprinting values of diversity, inclusion, community, and a strong moral compass. With Saga , parents and children can create a universe of stories, with their specific interests at the center. How we built it We took an intentional approach to developing a working MVP Needs finding: We began with a desire to uncover a need and build a solution based on user input. We interviewed 8 users over the weekend (parents and kids) and used their insights to develop our application. Defined MVP: A deployable application that generates a unique story and illustrations while allowing for dynamic reader inputs using OpenAI. We indexed on story, picture, and educational quality over reproducibility. Tech Stack: We used the latest LLM models (GPT-3 and DALLE-2), Flutter for the client, a Node/Express backend, and MongoDB for data management Prompt Engineering: Finding the limitations of the underlying LLM technology and instead using Guess and check until we narrowed down the prompt to produce to more consistent results. We explored borderline use cases to learn where the model breaks. Final Touches: Quality control and lots of tweaking of the image prompting functionality Challenges we ran into Our biggest challenges revolved around fully understanding the power of, and the difficulties stemming from prompt generation for OpenAI. This struggle hit us on several different fronts: Text generation - Early on, we asked for specific stories and prompts resembling “write me a 500-word story.” Unsurprisingly, the API completely disregarded the constraints, and the outputs were similar regardless of how we bounded by word count. We eventually became more familiar with the structure of quality prompts, but we hit our heads against this particular problem for a long time. Illustration generation - We weren’t able to predictably write OpenAI illustration prompts that provided consistently quality images. This was a particularly difficult problem for us since we had planned on having a consistent character illustration throughout the story. Eventually, we found style modifiers to help bound the problem. Child-safe content - We wanted to be completely certain that we only presented safe and age-appropriate information back to the users. With this in mind, we built several layers of passive and active protection to ensure all content is family friendly. What we learned So many things about OpenAI! Creating consistent images using OpenAI generation is super hard, especially when focusing on one primary protagonist. We addressed this by specifically using art styles to decrease the variability between images. GPT-3's input / output length limitations are much more stringent than ChatGPT's -- this meant we had to be pretty innovative with how we maintained the context over the course of 10+ page stories. How to reduce overall response time while using OpenAI's API, which was really important when generating so many images and using GPT-3 to describe and summarize so many things. Simply instructing GPT to not do something doesn’t seem to work as well as carefully crafting a prompt of behavior you would like it to model. You need to trick it into thinking it is someone or something -- from there, it will behave. Accomplishments that we're proud of We’re super excited about what we were able to create given that this is the first hackathon for 3 of our team members! Specifically, we’re proud of: Developing a fun solution to help make learning engaging for future generations Solving a real need for people in our lives Delivering a well-scoped and functional MVP based on multiple user interviews Integrating varied team member skill sets from barely technical to full-stack What's next for Saga Test and Iterate We’re excited to get our prototype project in the hands of users and see what real-world feedback looks like. Using this customer feedback, we’ll quickly iterate and make sure that our application is really solving a user need. We hope to get this on the App Store ASAP!! Add functionality Based on the feedback that we’ll receive from our initial MVP, we will prioritize additional functionality: Reading level that grows with the child — adding more complex vocabulary and situations for a story and character that the child knows and loves. Allow for ongoing universe creation — saving favorite characters, settings, and situations to create a rich, ongoing world. Unbounded story attributes — rather than prompting parents with fixed attributes, give an open-ended prompt for more control of the story, increasing child engagement Real-time user feedback on a story to refine the prompts — at the end of each story, capture user feedback to help personalize future prompts and stories. Monetize Evaluate unit economics and determine the best path to market. Current possible ideas: SaaS subscription based on one book per day or unlimited access Audible tokens model to access a fixed amount of stories per month Identify and partner with mid-market publishers to license IP and leverage existing fan bases Whitelabel the solution on a services level to publishers who don’t have a robust engineering team References https://www.frontiersin.org/articles/10.3389/fpsyg.2017.00677/full <div