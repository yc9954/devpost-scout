---
slug: "prosperio"
url: "https://devpost.com/software/prosperio"
title: "Prosperia"
hackathon: "Amazon Sumerian AR/VR Challenge"
organization: "Amazon"
winner: true
words: 996
team_size: 5
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/simulation_digital_twin"
  - "mechanism/voice_speech"
  - "domain/labor_employment"
  - "user/educator_student"
  - "substrate/transcript_audio"
  - "substrate/video_visual"
  - "substrate/web_dom"
---

# Prosperia

> Prosperia is a job interview simulation builder and practice platform that can be integrated at enterprise scale

[Devpost](https://devpost.com/software/prosperio) · hackathon [[Amazon Sumerian AR-VR Challenge]]

## Facets

**mechanism** [[simulation_digital_twin]] [[voice_speech]]
**domain** [[labor_employment]]
**user** [[educator_student]]
**substrate** [[transcript_audio]] [[video_visual]] [[web_dom]]
  <sub>weak: structured_db</sub>

**stack** amazon-dynamodb, amazon-ec2, amazon-elastic-transcoder, amazon-polly, amazon-rds-relational-database-service, amazon-sumerian, amazon-transcribe, amazon-web-services, angularx, aws-lambda, dynamo-db, ionic, s3

## How they structured the write-up

- inspiration
- what it does
- tips for doing a walkthrough of the application
- how we built it
- accomplishments that we're proud of
- what's next for prosperia

## Body

Inspiration From Jacki, team founder – I attended Kirby Shabaga’s Introduction to Amazon Sumerian demo at Eastside Virtual Reality Meetup and was immediately inspired to create a job interview simulator. At the end of Kirby’s demo, he shared info for this hackathon and CHALLENGE WAS ACCEPTED. We rounded out our group quickly with Drew Stone, Olga Milovanova, Alex Pirogof and of course, Kirby. Our inspiration comes from my own job search, a need for innovation in career services, and the gap that exists between career training programs and actually securing a position. What it does For the end user, Prosperia is an interactive simulator we developed to practice and prepare for job interviews. It was built in mind for people returning to the workforce after time away, recent graduates, underserved populations, and anyone who wants to build confidence and competency in interviews. Application features for end users include: Build out customized interview simulations from the questions you are commonly asked, that you need to practice most, or have found through research. Practice with an Amazon Sumerian interviewer. Record your responses to shareable video sessions. Transcription of voice recordings to text. Ability to review session video and transcribed text with stats including word count, non-talking time and average speech rate. Sharing of session recordings and data for review by others. You can retake an interview as is, or try another version generated from relevant questions. Beyond interview simulation for the end user, Prosperia is a customizable simulated interview session builder and sharing platform that can be integrated at enterprise scale. Organizations and institutions such as colleges, professional associations, military veteran and minority STEM programs, or any stakeholder in the support of others’ professional success can now have an actionable tool to make a difference. "This application is VERY useful for interviewing. It is important to know not only how you sound, but your facial expressions. I was also looking at my mouth and how I pronounced each syllable. Another takeaway from Prosperia is how long I'm taking to answer a question when I'm unsure of the answer." ~ Beta user, Dee Tips for doing a walkthrough of the application Prosperia Practice Interview Session Builder and Simulation Walkthrough Use this tutorial to experience an overview of Prosperia features: Take a practice interview Review recorded interviews Create a new interview simulation experience ~Chrome is the recommended browser~ Take a Practice Interview: Practicing interviews sets you up for success, give it a shot! Go to the Prosperia Dashboard at https://web.prosperia.tk Select an interview. Click unmute to hear the host’s greeting, and when prompted, give camera and mic permissions to the app. Click the Prosperia Cube to stop recording after you answer each question. After your interview is finished, return to the dashboard where you can take more interviews, and your most recent session will appear under “Completed Interviews” shortly. Review Recorded Interviews: Review past interview sessions and look for areas for improvement. Share your interviews with mentors to gain their feedback. Go to https://web.prosperia.tk Select the “Completed Interviews” tab and scroll down to find your interview. Here you can review the text transcript and recording stats, review the video of your interview, and share it with a colleague for their feedback. To advance to the next question in the recorded interview playback, click the Prosperia Cube. Create a new interview simulation experience: Create and adjust interview questions and question types, build new Roles, and activate different roles and interview sets. Go to http://s3.amazonaws.com/cloud.prosperia.com/index.html#/pages/interviews to access the Prosperia Administrations page. Changes will appear upon refresh at the Prosperia Dashboard: https://web.prosperia.tk Click on the “+” icon on the left menu to select “Interview Builder” Give the Interview a relevant title and description in the blank fields. Click “Next”. Set the Roles that will be used in this interview. You can create a new role, or select from existing roles. Click “Next”. Configure the categories of questions that you will be asking in this interview, e.g. Situational, Behavioral, Cultural, + Technical, etc., or you can create new categories that are relevant to the interview you are building. Click “Save” to finish editing. Click on the microphone icon on the left menu to select “Manage Interviews” to edit existing interviews, or interview drafts. How we built it We broke off into three sub-groups: Sumerian development, GUI building, and product research and management. We progressed from industry research, to scribbled diagrams on notepaper, to a digital UX sketch, to engineering and design. We pieced together our project starting with a single Sumerian scene, built it into an app, and then scaled it out into an enterprise platform prototype. Stack: Amazon Sumerian, AWS Lambda, Dynamo DB, Amazon Polly, Amazon S3, Amazon Transcribe, Amazon Elastic Transcoder, Amazon EC2, AngularX, ionic, Amazon RDS Accomplishments that we're proud of Building an innovative tool that can truly help people practice interviewing in customized sessions, improve, and succeed at securing a job. What's next for Prosperia We hope to win AWS services to continue our build, offer it to beta testers, and grow the functionality along with Amazon Sumerian updates. We feel that our project has real potential to disrupt professional development organizations and career services programs. We would love your feedback to make it even better! Next Steps and Fixes: Adding Amplify will make the experience smoother Create admin dashboard with number of interview invites/number actually taken, number of reviewers, user leaderboard... Add alert that interview processing has completed Security measures such as user authentication; non-public S3; encrypted files at rest and on the wire; user ability to download their content; user ability to delete their content... Timing for the transcription to text requires CloudWatch Logs and some logic to make it so that the entire interview is transcribed before processing ends Enhance playback controls and features Add Features: Grammar check Um and uh count Mentor feedback capture and added into the recordings lists Multi language capability AR mode option Accounts and admin roles Email interview invites Social sharing <div