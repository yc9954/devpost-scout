---
slug: "problempal"
url: "https://devpost.com/software/problempal"
title: "ProblemPal"
hackathon: "Disrupt SF Hackathon 2018"
organization: "TechCrunch"
winner: true
words: 1135
team_size: 0
has_repo: false
has_live: false
has_video: false
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "mechanism/runtime_tool_creation"
  - "mechanism/voice_speech"
  - "domain/developer_tools"
  - "domain/education"
  - "user/educator_student"
  - "substrate/document_pdf"
  - "substrate/structured_db"
---

# ProblemPal

> Integrating Alexa with Google Classroom to share and generate practice questions from Wikipedia articles

[Devpost](https://devpost.com/software/problempal) · hackathon [[Disrupt SF Hackathon 2018]]

## Facets

**mechanism** [[realtime_stream]] [[runtime_tool_creation]] [[voice_speech]]
**domain** [[developer_tools]] [[education]]
**user** [[educator_student]]
**substrate** [[document_pdf]] [[structured_db]]

**stack** alexa-python-sdk, alexa-skills-kit, amazon-alexa, python, wikipedia

## How they structured the write-up

- inspiration
- what it does
- how i built it
- challenges i ran into
- accomplishments that i'm proud of
- what i learned
- what's next for problempal

## Body

ProblemPal's workflow ProblemPal Alexa interface ProblemPal Alexa interface Inspiration Most people might not realize this, but the classroom is fundamentally a voice-driven environment. Teachers use their voices to deliver instructions, content, and other important information to students during each class period. This makes the classroom the perfect place to use Alexa. There's a huge opportunity for building voice-controlled edtech applications because they can significantly simplify how teachers interact with students and parents. As a full-time high school student, I've seen instances firsthand where Alexa can be used to improve the educational experience. ProblemPal is a small step towards this goal of integrating Alexa into the classroom experience. It tackles one of the biggest problems that teachers across the world face: spending excessive amounts of time outside of class preparing instructional materials. According to a report by K-12 Market Advisors, teachers spend over 12 hours every week finding and creating their own instructional materials, including practice worksheets. What if, instead of wasting time outside class, teachers could use their voice to automatically create practice questions during a lesson? That's where ProblemPal comes in. It's an Alexa skill that automatically generates practice questions based on teachers' voice commands and then uploads these questions to Google Classroom. For the prototype version of ProblemPal, these problems are sourced from Wikipedia articles related to teachers' queries, but the plan is to extend ProblemPal to other knowledge bases (see What's next for ProblemPal). What it does ProblemPal is a voice-controlled Alexa skill that automatically generates practice questions from Wikipedia articles and shares them to Google Classroom. It's meant to be used by teachers during a lesson to reinforce student knowledge. Teachers can ask ProblemPal questions like, "Make some questions about the Boston Tea Party" and ProblemPal will automatically generate questions and share them to Google Classroom as a series of announcements or an assignment. Importantly, ProblemPal is the first Alexa skill (that I know of) that integrates Alexa with the Google Classroom API. Within the context of this project, it means that generated questions can easily be shared, but in the future, this framework can be used to integrate Alexa into classrooms in many other ways. Also, it should be emphasized that while ProblemPal can be used outside the classroom, it's main focus is on enabling personalized learning in the classroom. Teachers, who once had to create all their worksheets before lessons, can now use ProblemPal to dynamically create worksheets that fit their students' immediate needs during a lesson. How I built it I used the Alexa Skills Kit SDK for Python, the Google Classroom API, the Wikipedia API for Python, and the NLTK NLP library to build ProblemPal. I created a custom intent called "MakeQuestionsIntent" that is activated by a phrase such as "Make some questions about {Text}". {Text} is an 'AMAZON.SearchQuery' slot that captures teachers' raw queries. Keywords and topics are extracted from these raw queries and used to search for relevant Wikipedia articles. Next, a question generation engine based on semantic analysis and topic modeling generates short answer and multiple-choice questions from these relevant Wikipedia articles. NLTK was used for this. Next, the generated questions are formatted into JSON templates and then shared to Google Classroom automatically as an assignment or series of announcements. This connection between Amazon Alexa and the Classroom API is the most powerful part of the project, because even though ProblemPal uses it to share questions, there's many more possibilities to be explored (like automated lecture transcribing, note creation, and more). Challenges I ran into There were four main challenges I faced over the course of the project: 1) Figuring out how to pull raw text from Alexa in order to build custom NLP. (I solved this by learning about and using the AMAZON.SearchQuery slot type) 2) Connecting the Google Classroom API to Alexa (I solved this by learning about how to use OAuth2.0 and using Alexa's Account Linking feature to enable Alexa to create Google Classroom announcements from a Lambda function) 3) Designing a custom NLP algorithm to autonomously generate questions from Wikipedia articles (I used semantic analysis and topic models to solve this) 4) One unsolved problem I had was generating formatted Google Drive documents from the generated questions. In the future, it would be cool to add a feature where instead of posting the questions as an announcement/assignment on Google Drive, all that's posted is a link to a Google Doc with the questions. Accomplishments that I'm proud of Connecting the Google Classroom API to the Alexa Skills Kit (building a framework that others can continue building off of) Developing a custom NLP engine on top of Alexa queries by using the 'AMAZON.SearchQuery' slot to get raw user text, searching for topic keywords in that text, and then automatically finding practice problems from the web about those topics (Hopefully) Demonstrating that Amazon Alexa has the potential to be a valuable educational tool Working alone. Most hackathon projects are done by teams, but I had to learn how to do design, coding, and delivery all in one package independently as a high school student. What I learned I learned how to use the Alexa Skills Kit to access other web APIs I learned how to use the Alexa Skills Kit Python SDK to build custom intents I learned how to deploy Python code on a Lambda function instance I learned about topic modeling and the Wikipedia API for Python What's next for ProblemPal Immediate Goals for ProblemPal The prototype version of ProblemPal automatically generates multiple choice questions from Wikipedia, but in the future, I want to expand this capability to add more question types, more subjects, and more sources for the questions. Possible ideas including integrating ProblemPal with the Khan Academy API or the Wolfram Alpha API. Because ProblemPal is already integrated with Google Classroom, these connections would make it easy for teachers to use voice commands to create and deliver practice materials to their students. The other concrete idea I have is building a crowdsourcing functionality where teachers can suggest their own problems to the ProblemPal database, which can then be used by the skill when generating questions. The Alexa for Education Vision ProblemPal is just one step towards building an entire Alexa-based educational experience. In the works are a skill to help parents monitor their child's progress in the classroom in real time with Alexa, as well as a skill to increase student participation in discussions. Ultimately, my vision is for Alexa to be integrated fully with the classroom, so that it can enable students and teachers to make the learning process faster and more personalized. I want to build many skills to achieve this goal, and getting the Alexa Disrupt SF Prize would give me capital and devices to build and pilot-test these skills in real classroom environments. <div