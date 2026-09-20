---
slug: "gradeai-s9ptdc"
url: "https://devpost.com/software/gradeai-s9ptdc"
title: "gradeAI"
hackathon: "TreeHacks 2024"
organization: "TreeHacks"
winner: true
words: 1205
team_size: 4
has_repo: true
has_live: false
has_video: false
tags:
  - "project"
  - "mechanism/multi_agent"
  - "mechanism/on_device_local"
  - "mechanism/retrieval_grounding"
  - "mechanism/vision_ocr"
  - "domain/developer_tools"
  - "domain/education"
  - "domain/labor_employment"
  - "user/developer"
  - "user/educator_student"
  - "user/legal_professional"
  - "substrate/document_pdf"
  - "substrate/geospatial"
  - "substrate/structured_db"
  - "substrate/web_dom"
---

# gradeAI

> Efficient teaching, effective learning

[Devpost](https://devpost.com/software/gradeai-s9ptdc) · hackathon [[TreeHacks 2024]]

## Facets

**mechanism** [[multi_agent]] [[on_device_local]] [[retrieval_grounding]] [[vision_ocr]]
**domain** [[developer_tools]] [[education]] [[labor_employment]]
**user** [[developer]] [[educator_student]] [[legal_professional]]
**substrate** [[document_pdf]] [[geospatial]] [[structured_db]] [[web_dom]]

**stack** fastapi, fetch.ai, google-cloud, openai, python, reflex

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for gradeai

## Body

Course Display Assignments for Course Feedback Screen Assignment Creation Inspiration As engineering students who attend public universities, class sizes of 300 are no rarity. Sadly, that also means that oftentimes, our most important classes can take weeks or months to supply us with feedback for our assignments, hamstringing the learning process and creating a larger disconnect between the professor and the student. A quarter system is 10 weeks long, and having 3 weeks of ungraded assignments means learning 30% of the class without any feedback. We're also keenly aware that now more than ever, teachers are overworked. The average teacher logs upwards of 180 hours per year on grading alone, making it the most worked-on task outside of actual teaching inside the classroom. The solutions they have right now are few. Hiring extra teaching assistants to aid with grading is an extensive process that demands thorough interviewing to ensure the applicants actually know the material. Simultaneously, money is something that most universities can't spare on extra graders, meaning those that are qualified face heavily inflated workloads. At the moment, it seems there's no feasible out. With less time spent grading, there's more time spent with students. Enter gradeAI, our AI-based tool that aims to streamline grading by automatically processing assignments and evaluating them based on a given rubric. Our goal isn't to replace the teacher or the TA, but rather to appraise assignments quickly, let educators review and alter judgements made, and expedite grading large volumes of similar assignments. What it does It utilizes AI Agents from Fetch.ai to break down multiple steps of grading assignments. First on the frontend, the teacher can create an assignment in a course, then name it and provide a rubric. As students submit their homework, the assignment will start getting graded after the due date. We have multiple AI Agents with the first being locally run and ported publicaly using Fetch.AI's mailbox. This first agent is responsible for pulling submitted homework files and the associated rubric from our Google Cloud Platform storage. This agent also processes the text and is the handler for sending homework to be graded in our pipeline, and eventually write the processed grades to our database. Next in the process is our pipeline of 4 agents on the Agentverse! The first agent is responsible for sending all of the processed text in a clean format to our next agent which parses the homework into readable chunks. The second agent-let's name it Parser-takes each problem number and associated work with it, and puts them all into an array! Parser does this for both the solution and homework submitted! This agent then sends this data to our third AI Agent and let's name this one Solver! This is where all of the grading happens. This AI Agent cross examines each problem's solution and attempt one at a time, which increases accuracy of grading. We ask this AI Agent to return data in a JSON format with the grade, confidence level, summary, and details for each problem. From there, Solver sends all of the graded problems that it did one by one to ensure accuracy to our last AI Agent on the Agentverse! This last agent aggregates all of the data and sends it back to our first agent being locally ran! Our locally ran agent then writes everything to our database, where we show it on our frontend! How we built it We used the Reflex framework and Fetch.AI to accomplish all of our goals. This proved to be both difficult and convenient, as we never used these technologies before, but everything was written in Python! Thanks to Reflex, we built our entire website in Python, and Fetch.AI is all in python, which was great. In terms of Fetch.AI, we used many of their products such as the Agentverse, mailbox, template agents, and a little bit of DeltaV! We utilized the Agentverse, as it provided a convenient way to deploy our agents and have them run 24/7, which allowed us to keep a constant pipeline! The integrated development environment was also helpful in debugging and creating agents from scratch. Mailbox provided by Fetch.AI allowed our locally ran AI Agent to communicate with all of the deployed agents. Using a combination of all of these tools, we were able to piece together multiple agents with using a combination of openAI's API and OCR. Reflex was also a great tool and we utilized it's documentation and ability to wrap React code to create nice and complex components with functionality. Challenges we ran into We took a big challenge in using technology we've never touched before! Reflex and Fetch.AI were the two major components of our project, and there was a big learning curve. One of the issues we ran into was a lack of documentation. Being a relatively newer product that also had a recent name change, Reflex didn't have as many resources as many of the tools we were more accustomed to. As a result, it took us a while to get the hang of what we were doing, and complex issues such as managing routes and backend integration with GCP were made even more difficult as we searched for solutions. Simpler issues like embedding PDF views of files was also made demanding, and our time frame for design was expanded due to underestimation of what we thought wouldn't be issues. Accomplishments that we're proud of What we learned In terms of our web framework, we chose to use Reflex to build out our web app that incorporated Fetch.ai, FAST APIs, and OpenAI APIs. For Reflex, we learned how to develop the architecture of our application by fully understanding the Reflex documentation, and of course, reaching out to the Reflex developers for assistance. Additionally, we learned to link the various pages together and to incorporate components into our pages in order to fully immerse the user(s) and to provide a platform for the students and teachers to view the graded papers and their respective results. What's next for gradeAI Given a time frame of 36 hours, our team had many more features planned than we were able to execute. Primarily, we'd love to add a plagiarism checker, LLM integration for student follow-ups, and textbook breakdowns for relevant questions in the homework. If gradeAI were a product in wide circulation, plagiarism would undoubtedly be the number one threat to its efficacy; as such, this implement demands our most immediate attention. Textbook breakdowns would also be a great quality of life feature we'd love to be able to tackle, but in truth, the feature we'd most look towards would be the LLM integration. Our undertaking of this project was meant to challenge us from the very beginning, and LLM is something we're all excited about and ready to learn and apply. Outside of features, we're looking to simply run and test a wider variety of materials so gradeAI can be the product it was meant to be. We've been nothing but thoroughly impressed with what we've been able to make, and we hope educators will be too. There's a long road to come for gradeAI, but whatever comes our way, we're confident we have the tools to ace it. <div