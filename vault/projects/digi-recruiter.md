---
slug: "digi-recruiter"
url: "https://devpost.com/software/digi-recruiter"
title: "Digi Recruiter"
hackathon: "Automation Anywhere Bot Games"
organization: "Automation Anywhere"
winner: true
words: 596
team_size: 3
has_repo: false
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/revocation_withdrawal"
  - "domain/labor_employment"
  - "domain/supply_logistics"
  - "substrate/geospatial"
  - "substrate/structured_db"
---

# Digi Recruiter

> Your Recruitment Buddy

[Devpost](https://devpost.com/software/digi-recruiter) · hackathon [[Automation Anywhere Bot Games]]

## Facets

**mechanism** [[revocation_withdrawal]]
**domain** [[labor_employment]] [[supply_logistics]]
**substrate** [[geospatial]] [[structured_db]]
  <sub>weak: document_pdf</sub>

**stack** a360, database, excel, inputforms, office, office-365, outlook, pdf, vbscript, word

## How they structured the write-up

- inspiration:
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for digi recruiter

## Body

Digi Recruiter Process Flow Interview Invite to Candidate Inspiration: For any of the opening within a company, HR are bombarded with thousands of resumes. At times, most of the resumes do not event match with the required skill set for the Job Description. This involves manual screening of each resume and removing the outlier. To overcome this situation and have proper skill set mapping being done, we introduce Digi Recruiter. This would be a solution for the mapping of HR requirement and screening the desired candidate as per relevant skills. Along with that, we provide a complete package to conduct seamless interviews and releasing the offer letters. What it does • Collect the Job Requirement details from Organization via Email to HR. • HR will fill in the details in a Requirement form basis on New or Existing role opening. • Bot will refer all the resumes from the shared folder. • Bot will screen the resumes basis on the openings and filter out the data. • Bot creates a Tracker with the skill set scoring. • Basis the rating provided bot sends invite email to the shortlisted candidates and interviewers with Interview Date and Time. • The qualified resumes from Phase-1 will be moved to the panelist to start with Interview process. • Interview process is conducted in three rounds (Tech/Managerial/HR) and offer letter is released to selected candidates. How we built it • Job Opening email received from Organization to HR. • HR enters the details in the requirement form. • HR will make a new entry for new role and bot update in the database. • HR will select the required details if the opening is for existing role. • Bot will screen all the resumes basis on role and requirement detail and prepares the tracker with skill set scoring. • Interviewer and Interviewees will be provided with email notification for the Interview Date. • Resumes will be forwarded to Panelist for Interview Process. • Panelist(Tech/Managerial/HR) will fill the form with ratings and select / reject the resume. • Bot will release the offer letter to the selected candidate Challenges we ran into • We tried using O365 Calendar for blocking available time slot of the Interviewer and Interviewee but it was unable to fetch appropriate time slot. • Using the form elements of AARI • Setting the predefined variables to AARI • Controlling the visibility of form elements based on dynamic selection of fields. Accomplishments that we're proud of • To get the desired Outputs what has been thought of and decided in the Project Planning Phase. • Got well Equipped with the new functionalities added in A360. • Proud to generate and help the HR to reduce their day to day mundane work of shortlisting resumes with a less number instead of evaluating 1000+ resumes. • Having a seamless interview process with minimal documentation needed. What we learned • Using the forms with database and hot keys • Identifying the connector for using Excel as DB. • Seamless process flow with Humans and BOTs working together. What's next for Digi Recruiter • Integration of social media platforms like LinkedIn for Job Posting Fetching required candidate resume • Integrating with O365 SharePoint and Calendar • Using WLM for scaling the process for handling large volume of resumes • Using IQ bots for dynamic screening of Resumes • Calculating BOT efficiency by analyzing monthly, Yearly data collected. • Adding Onboarding Module for Logistic request on portal Automated emails for granting necessary access • Adding Offboarding Module for Return of Assets Revoking access <div