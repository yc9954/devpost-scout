---
slug: "debeat-coach"
url: "https://devpost.com/software/debeat-coach"
title: "DeBeat Coach"
hackathon: "The PartyRock Generative AI Hackathon by AWS"
organization: "Amazon"
winner: true
words: 923
team_size: 1
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "domain/education"
  - "substrate/video_visual"
---

# DeBeat Coach

> Debeat Coach is an debate coaching app on PartyRock, with some rap battle elements incorporated into it, designed to interactively coach and entertain people that are interested in debating.

[Devpost](https://devpost.com/software/debeat-coach) · hackathon [[The PartyRock Generative AI Hackathon by AWS]]

## Facets

**domain** [[education]]
**substrate** [[video_visual]]

**stack** partyrock

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for debeat coach

## Body

Inspiration As I was walking home with my colleagues one day, one of them mentioned about their child being in a debate club at school. At that time I was still thinking of ideas for the PartyRock hackathon, and I thought a debate coaching app would be a perfect idea for the hackathon. It facilitates interactive learning, it addresses a use case, and it could use multiple features of PartyRock (Text generation widgets for feedback and coaching, Chatbot widgets for a 'mock debate', plus image generation widgets to create images representing both sides). Additionally, I could add in a 'rap battle' component to make it more creative and entertaining. What it does DeBeat Coach is an interactive debate coaching app. It allows users to input a debate topic and their arguments, and the app will provide constructive feedback and suggestions to improve the debating skills of the user. The app also has an "Interactive debate" section that allows users to enrich their debating experience. Finally, the app also includes a rap battle of the debate topic, where the user can watch two rapper bots battling against each other in a rap style, along with persuasive images representing both sides. How we built it The application was built through comprehensive and iterative prompt engineering through PartyRock. PartyRock is an Amazon Bedrock Playground for building AI applications. Users can construct "widgets" through a straightforward interface, where they also define custom prompts for these widgets. Each widget utilizes a Large Language Model (LLM) chosen by the user, automatic interaction with the LLM to produce text outputs from the given prompts and inputs. The text outputs can also be referenced in a separate widget. Challenges we ran into I ran into two main challenges when building the application: Sometimes the prompt was too long and complex, and as a result the widgets often did not generate the desired output. I applied two techniques to overcome this challenge. Firstly, I broke down the original prompt into multiple prompts that were shorter, each in its own widget, which I named 'System' widgets. Each 'System' widget would solve a smaller problem in a sequential order through referencing one widget's output text to another, similar to how a 'Chain-of-Thought' prompting technique is applied. In addition, I also implemented 'One shot learning' , a prompt engineering technique where an example of an input and output pair is given in the 'System' widget prompt. Both these changes resulted in significant improvement in the accuracy and relevancy of the output. The other challenge I ran into was the rapper widgets occasionally generated text can be considered as potentially harmful or offensive. However when I prompted the widget to NOT generate any potentially harmful content, it frequently refused to generate Any content at all. I struggled to make sure the rapper widgets generate safe content consistently. To solve this problem, I prompted 'System' widgets to "describe visually the benefits that would happen to our world/people/environment, when the for/against side of the debate topic is actioned" , and prompted the 'Rapper' widgets to rap based on the 'System' widgets. This way, the AI focused more on promoting the good outcomes of the side that it represented, portraying a more positive image, instead of focusing on the negative outcomes of its opponents. This drastically improved the safety and positivity of the generated text. Accomplishments that we're proud of There are several accomplishments that I was proud of through developing DeBeat Coach: I was able to put the learnings from my online courses to practice through developing this DeBeat Coach application. I overcame the two challenges above and successfully created a functional, educational, and entertaining AI application without any code. I received valuable feedback from an application user, who told me where certain components are helpful and how other components can be improved. What we learned I learned that PartyRock is an easy-to-use platform for developing AI apps, it can be a great tool for prototyping AI projects. Additionally, just like regular problem solving, breaking down a complex prompt into multiple components/widgets/agents will allow LLMs to generate text that is more likely to match the desired output. What's next for DeBeat Coach The application to my colleague's child (who has several years of experience in debating), and I received valuable feedback. I was told that she found the "Counter arguments" component helpful, since it not only generated the counter-argument . I also learned that there are actually various types of debating, each one will have different rules and structure. For example, there is a "Model debate" (Also called Policy debate), in this format the affirmative side would propose a plan to be implemented in relation to the debate topic, whereas the negative side would attempt to rebuttal against in the plan or propose a counter-plan. From additional research, I learned that different countries also have different variations of rules and structure for each type of debate. An improvement for DeBeat Coach will be to make it more customised for different types of debate, so that the "Arguments" and "Interactive Debate" sections can adjust their output accordingly. This way, DeBeat Coach will provide even more tailored coaching and support for different types of debate. This can then be given to multiple debaters, and continuously improve the application from their feedback. On the other hand, my experience in PartyRock was so insightful that it sparked more project ideas. I will continuously learn, prototype, and develop more AI applications that can benefit people, both in PartyRock and using other tools. <div