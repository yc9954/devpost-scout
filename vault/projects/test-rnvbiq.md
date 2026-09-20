---
slug: "test-rnvbiq"
url: "https://devpost.com/software/test-rnvbiq"
title: "The Virtual Office"
hackathon: "Quick Base Virtual Hackathon"
organization: "Quickbase"
winner: true
words: 1043
team_size: 3
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "mechanism/retrieval_grounding"
  - "domain/education"
  - "domain/labor_employment"
  - "user/educator_student"
---

# The Virtual Office

> Reconnect your workforce using the power of Quick Base

[Devpost](https://devpost.com/software/test-rnvbiq) · hackathon [[Quick Base Virtual Hackathon]]

## Facets

**mechanism** [[realtime_stream]] [[retrieval_grounding]]
**domain** [[education]] [[labor_employment]]
**user** [[educator_student]]
  <sub>weak: web_dom</sub>

**stack** daily.co, freeclimb, highcharts, html, javascript, jquery, pipelines, quickbase

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we’re proud of
- what we learned
- what's next for the virtual office

## Body

Walk the Halls of the Office - See Who's Available Virtual Office Dashboard Free Climb Pipeline Virtual Office Cafeteria Virtual Office Schema User Interactions Dashboard Inspiration The traditional workplace has been disrupted. The experiences of 2020 have resulted in an influx of literature across industries on the difficulty of maintaining interpersonal relationships, building team cohesion, and cultivating company culture. These result in negative impacts on employee engagement, job satisfaction, and new employee recruitment. Despite these challenges there are many companies looking to make these changes permanent; spending less money on the “brick and mortar” and investing more in the technology and diverse talent to bring their innovations and vision into 2021. We imagined a world where businesses not only function but thrive in a remote workplace powered by Quick Base. Our mission was to create an inclusive environment free from physical barriers where employees can be recruited from a global talent pool and engage with each other to create a fully remote or hybrid company culture. Employees easily collaborate, innovate, and build lasting relationships in the same location as their existing Quick Base applications What it does The application is built to enhance relationships and team building. The functionality can sit within your current application or as a separate application. This brings real interpersonal connections to your work flows. Here’s how we do it: “Walk the Halls” of our office! Users are able to browse all employees by department. Each employee has a contact card with self-selected interests meant to be used as conversation starters. Our “Knock on Door” functionality allows people to stop by other people’s workspace to see if they’re available for a face to face chat. “Conference room – 5 minutes!” – Michael Scott. Each group has a Team Room where employees can go to collaborate together. Gone are the days of manually scheduling Zoom meetings and sending out calendar invites. Grab lunch or sip coffee with your coworkers in the cafeteria! Employees can visit the cafeteria where they can catch up and decompress with other employees. You can visit the cafeteria to read company announcements, check out upcoming birthdays, and even play checkers! Track user interactions! We also track the which rooms employees visit and how often. An analytics dashboard represents this data in real time. This dashboard can be used to gain insight to how employees are interacting with the application at an enterprise and individual level. How we built it This application showcases the power of Quick Base. We use code pages, the API, and pipelines to make our solution possible. We integrated Quick Base with the daily.co video conferencing API. Button clicks call Quick Base code pages which embed the video conferencing technology within Quick Base on demand. We are also able to track the real time status of individuals using this API. Quick Base knows when someone is meeting with another individual or team. This automatically updates the user status to "Busy". We couldn’t assume that people always had to be in Quick Base in order to be reached by others. We solved for this by integrating with the FreeClimb text messaging API. If a you knock on a door, that person will receive a text message to let them know you’d like to chat. They are able to respond to the text message to let you know if they’re coming or busy. The text message response is returned to Quick Base using the Webhooks Requests Pipeline. We use pipelines to automatically create a virtual collaboration room once a new employee or group is created. All a user has to do is navigate to the room they'd like to visit and they'll automatically be joined. This is meant to solve for the use case where you may be asked "Hey, we're in the conference room and need your opinion. Can you swing down when you have a chance?" Spontaneous conversations are a bedrock of the traditional office experience. We solved for this by embedding a virtual room that can joined at any time. All a user has to do is navigate to the Cafeteria dashboard to be connected with other individuals looking to take a break. Challenges we ran into The biggest challenge was trying reimagine the office in a virtual environment. Our objective was to make it as simple as possible to navigate the application and outreach individuals to maintain and build connections. We originally integrated with Zoom. It became impossible to host a cafeteria without a user starting the meeting. This defeated the purpose of spontaneous connection. It would also be cost prohibitive for organization to scale with Zoom as the video conferencing solution. Daily.co solves for this by providing the same experience at a maximum price of $200 per month for an enterprise solution. This would allow our solution to be cost effective for any organization. Accomplishments that we’re proud of We believe we’ve created a solution that removes proximity as a barrier to relationship building between employees. People now have a new way to connect with others. Employees from different departments can see each other to catch up outside of work meetings. New employees can finally meet people that may not be part of their typical day to day experience. Emails, phone calls, Slack messages, and prescheduled Zoom meetings are no longer the only ways to connect. We are most proud that our application is scalable and can implemented within any Quick Base environment. Your office can now sit alongside other Quick Base applications. What we learned We were not heavy pipelines users until this project and learned how powerful they can be. For example, we used pipelines to automate the creation of a new virtual collaboration space in the daily.co platform based on Quick Base record creation. It can't get any easier for the user than that! What's next for The Virtual Office Our focus has been on the workplace. We can extend this solution by incorporating group discussion boards or direct messaging/chat features. This is a solution that could also be transformed into a remote learning tool. Student interactions outside the virtual classroom are limited. We believe this solution could be adjusted to become a virtual school where students are able to learn, collaborate, or just hang out. <div