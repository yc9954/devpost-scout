---
slug: "kids-court"
url: "https://devpost.com/software/kids-court"
title: "Kids Court"
hackathon: "Alexa Skills Challenge: Kids"
organization: "Amazon"
winner: true
words: 879
team_size: 1
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/voice_speech"
  - "domain/education"
  - "domain/legal_justice"
  - "user/educator_student"
  - "user/legal_professional"
  - "substrate/video_visual"
---

# Kids Court

> No more fighting! Take your rivals to Kids Court and watch them get what they deserve.

[Devpost](https://devpost.com/software/kids-court) · hackathon [[Alexa Skills Challenge- Kids]]

## Facets

**mechanism** [[voice_speech]]
**domain** [[education]] [[legal_justice]]
**user** [[educator_student]] [[legal_professional]]
**substrate** [[video_visual]]

**stack** thestoryline.io

## How they structured the write-up

- inspiration
- what it does
- how i built it
- challenges i ran into
- accomplishments that i'm proud of
- what i learned
- what's next for kids court

## Body

Inspiration When I first observed how people interact with Alexa, I noticed most of the adult interactions are either voice commands ("add milk") or questions/answers ("What's the weather?"). Kids interact with Alexa magically. They treat her as a real person captivated in a small box and love to chat with her like a friend. Once realizing that, my motivation for this contest was to create a social interaction between Alexa and a group of kids. Usually Alexa dominates the interaction and the kids respond; My approach was reverse - I wanted the kids to be able to initiate their own story and talk about what troubles them , and have Alexa be an active participant that listens and responds to them. I decided to address one of the most agonizing parts of family life - kids fighting - and created Judge Lexy which is an objective, quirky judge that helps kids settle their battles. Welcome to Kids Court. What it does Kids Court lets kids (and their parents!) settle their arguments in a fun way, while getting a peek into how the legal system works. The prosecutor states their case, the defendant answers, the kids can call witnesses and present evidence and finally Honorable Judge Lexy rules with funny dare-style verdicts that the losing side must execute. While kids probably mostly enjoy the revenge aspect, in the process they learn about the roles of a defendant, prosecutor, evidence, witnesses and more. They also learn to stand up for themselves in a calm manner, to articulate their problems coherently, and to take responsibility for their actions. Kids Court is intended for kids age 8 and up. Younger children can enjoy it too if someone explains the legal vocabulary. How I built it I designed an algorithm that helps Judge Lexy determine if the defendant was guilty or not. I crafted a user experience that covers many use cases and is meant to be fun and engaging for the kids even if Judge Lexy rules against them. I also added a few easter eggs to surprise the kids, and put in explanations of some basic legal terms that the kids can ask about when they're unsure (i.e what's a prosecutor?). Technically, as I wanted to focus on content and user experience, I used thestoryline.io to build the entire skill. There are dozens of different logical paths and various possible responses for Lexy to make her character more engaging and the overall experience more entertaining. Challenges I ran into My motivation was to create an experience where Alexa is a social facilitator for a group of 2-4 participants. The skill has to let them talk freely and make them feel like Lexy is listening and responding to everyone. As every teacher/parent can probably attest, it was very challenging to create a natural yet structured conversation that keeps the kids in control, lets everyone feel heard, and teaches them something in the process. A major challenge was that Alexa doesn't pick up some of the things the kids say as either they talk too fast, get excited and step out of the flow, or can't help themselves and talk together. I tried to go around this by expanding the possible utterances for each state and creating default responses for almost everything they might say. Accomplishments that I'm proud of Kids and parents alike seem to really enjoy this skill. I tested it on a small focus group and it was beautiful to see how responsive the kids were, how naturally they engaged in the conversation and how much they enjoyed having Lexy listen to them. They interacted with the skill for a couple hours (!) and I'm really satisfied with how they believed Lexy was real and the pleasure they took in challenging her with many different cases. The best feedback was seeing their hilarious reactions whenever Lexy ruled. I was very pleased at how engaged the kids became even though there were no screens or any visual images involved. What I learned I learned how to design for voice and I learned a lot about how to design for kids. The idea I originally had changed tremendously once I tested it on real kids. Personally, this was the first product I ever built entirely on my own and not as part of a team. I had to deal with many issues that were new to me, such as voice design, use of ssml, technical jargon, finding and fixing vicious bugs that made the skill crash, legal aspects, sound effects, making a video and more. This was a super fascinating experience on many levels. What's next for Kids Court I plan to make Lexy smarter by implementing more investigation flows and a broader range of verdicts. Educationally, I'd like to take this game to the next level and introduce more concepts from the legal system such as an alibi, an objection, and more. I currently chose not to store any information about the users to make sure I comply with COPPA. I plan to look into it further and see how/if I can create a more personalized experience and create more value for returning players. Thank you for reading and I hope you enjoy it! Would love to hear feedback at Pretzel.Voice@gmail.com <div