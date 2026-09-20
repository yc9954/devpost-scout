---
slug: "lab-monitor-fpo12a"
url: "https://devpost.com/software/lab-monitor-fpo12a"
title: "Lab monitor"
hackathon: "AWS Artificial Intelligence Hackathon"
organization: "Amazon"
winner: true
words: 957
team_size: 9
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/on_device_local"
  - "mechanism/realtime_stream"
  - "domain/education"
  - "user/educator_student"
  - "substrate/code_repository"
  - "substrate/video_visual"
  - "substrate/web_dom"
---

# Lab monitor

> Lab monitor changed the eTraining assessment model from final output to whole learning/development process

[Devpost](https://devpost.com/software/lab-monitor-fpo12a) · hackathon [[AWS Artificial Intelligence Hackathon]]

## Facets

**mechanism** [[on_device_local]] [[realtime_stream]]
**domain** [[education]]
**user** [[educator_student]]
**substrate** [[code_repository]] [[video_visual]] [[web_dom]]

**stack** amazon-comprehend, amazon-polly, amazon-rekognition, amazon-sumerian, api-gateway, athena, codecommit, cognito, dynamodb, glue, kinesis-data-analytics, kinesis-stream, lambda, python

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for lab monitor

## Body

Activity Analysis Demo Scene Inspiration Our institution - Hong Kong Institute of Vocational Education provides IT training to large number of students. While within a classroom, a common problem about IT related lab activity is that, students usually focus on something that is not related to course (Browsing website, playing games or watching youTube videos). As lab exercise solution are being submitted in softcopy. Teaching staff is having a big headache on challenging students' plagiarism, as generally there is only one version of solution. That's why we have built an opensource project “Lab Monitor” which uses AWS AI Services, serverless architecture, Amazon AR/VR services to enhance the learning experience and also gather data to understand what students/trainees are doing during lab/eTraining, and we want the project can be widely used not mainly for educational purpose but also applicable to all companies on eTraining session. What it does "Lab Monitor" can be applied from classrooms of institution to training rooms of company. It is providing 3 main features : - A lab monitor agent - A lab monitor collector - An AR lab assistant Lab monitor agent A Python application that runs locally on a student’s computer. To achieve sending required information AWS periodically. Since we need to identify students and prevent the API gateway being abused, an unique API key with a usage limit apply to each single student. Including the functions: Capturing all keyboard and mouse cursor events – Ensure students are really working on the exercise as it is NOT possible to complete a coding task without using keyboard and pointer! Monitoring and Controlling PC processes – Stop students from running programs that are NOT relevant to the lab. We can kill all browsers tabs and communication software, when computer test is taking place. Capturing Screens - Detect videos or content that are NOT appropriate by Amazon Rekognition . The extracted text content is able to trigger an Amazon Sumerian host to talk to a student automatically if certain circumstances match. But It is NOT possible for a teacher to monitor all students' screen (a 30 person class)! That's why we will use a presigned URL with S3 Transfer Acceleration, in order to speed up the image screenshots upload. Uploading source code to AWS when students save their code – Review the whole class performance and give support to students who are NOT follow the class tempo! Lab monitor collector An AWS Serverless Application Model that collects data and provides an API to AR Lab Assistant. Optionally, a teacher can give marks to students immediately every time they save code by running the unit test inside AWS Lambda. Also it saves the time for marking. All data will be constantly saved into an Amazon S3 data lake and Amazon Athena can be used for analysing data. For the sake of saving costs, a scheduled Lambda function being setup for checking the teacher’s class calendar every 15 minutes. So when there is an upcoming class, it will automatically create a Kinesis stream and Kinesis data analytics application. Then Teachers can have a nearly REAL-TIME view of all student activity to better manage the whole class. AR lab assistant A Amazon Sumerian application that can alert students to work on their lab exercise. It sends a camera image to Amazon Rekognition and gets back a student ID (A live camera showing on the top left of the screen). A Sumerian host, Christine, uses Amazon Polly to speak to students when following situation happens: Students Passed a unit test , Christine says congratulations. Students Watched any movie , Christine scolds them with the movie actor’s name, such as Tom Cruise. Students Watched any inappropriate content , Christine scolds them. Students Did something wrong such as forgetting to set up the Python interpreter, Christine reminds them to set it Students can also ask questions to Christine, for example, to check their overall class/training progress. The Amazon Sumerian host is able to connect to a Amazon Lex chatbot. Then the conversations with students will then be saved in DynamoDB with the Sentiment Analysis result by Amazon Comprehend. As you see, a student's screen is just like a projector showing inside the Sumerian application. Christine: “Stop, watching dirty thing during Lab! Tom Cruise should not be able to help you writing Python code!” How we built it The following shows a Simplified Architectural Diagrams: Challenges we ran into To capture the following user behaviours by: Capturing all keyboard and mouse events Monitoring and Controlling PC processes Capturing screens In order to get nearly real-time view of all student’s activity and analysis. To project students's screen into Sumerian. To make the interaction between users with VR Chatbot natural, and do Sentiment Analysis for all student’s conversation and transformed to text based. Text will then be easily being extracted and analysed Accomplishments that we're proud of By combining the power of each AWS Services, students will be encouraged to concentrate on their lab exercise and stop the dream of copying answer from others! Also, that will be much fun for them to work with Christine. The initial version without AR lab assistant is already being applied to real lab lessons in Hong Kong Institute of Vocational Education (Lee Wai Lee), and improved the learning and marking efficiency. What we learned The integration with multiple AWS AI Services. The integration of Lambda, S3, Athena, Glue and Kinesis for real time data stream analysis What's next for Lab monitor More than 4 months' effort has been paid off for this project and the development is still in progress. The current version aims for data collection and in future we plan to build machine learning model to predict users/students’ final grade against their class behaviour. <div