---
slug: "campus-companion-making-student-life-easy"
url: "https://devpost.com/software/campus-companion-making-student-life-easy"
title: "Campus Companion – Making Student Life Easy"
hackathon: "Student HackPad 2025"
organization: "Student Hackpad"
winner: true
words: 465
team_size: 1
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/cross_origin_web"
  - "mechanism/realtime_stream"
  - "domain/education"
  - "user/educator_student"
---

# Campus Companion – Making Student Life Easy

> The simplest way to manage college life — instantly.

[Devpost](https://devpost.com/software/campus-companion-making-student-life-easy) · hackathon [[Student HackPad 2025]]

## Facets

**mechanism** [[cross_origin_web]] [[realtime_stream]]
**domain** [[education]]
  <sub>weak: developer_tools</sub>
**user** [[educator_student]]

**stack** base44sdk, lucidereact, react, shadcn/ui, tailwind, tanstack/react-query, typescript

## Body

Home Login Page Profile Page in Light mode Profile Page in Dark mode Edit Profile Page Home Dash Board Free class room finder page class room check in page time table page add class in time table page Assignment page Assignment add page Notice Page AI study Help page student chat area posting in chat page GPA calculator Marks adding page Lost & found things page add lost and found things page event page NOTE Our software is available on both Web and Android (APK). The APK version provides the best user experience. Both links are attached below. THANK YOU Inspiration On campus, we constantly noticed the same problems: Students wandering around looking for empty classrooms Friends missing deadlines because they forgot submissions Confusion about daily timetables No single place to organize class schedules and assignments We wanted to build something simple but powerful—an app that genuinely makes student life easier. That idea became Campus Companion, inspired by the hackathon theme: “Build whatever makes students’ lives easy.” What We Learned While building this project, we learned: How to design clean and minimal UI that works well for students How to manage and structure real-time data using Firebase/Supabase How to compare time slots to detect free classrooms How to handle overlapping schedules logically How to stay focused on building an MVP instead of overbuilding We even formalized our free-room detection logic through a simple condition: If the current time t does not fall between startTime and endTime, the room is free. How We Built It Planning We listed the top struggles students face: Finding free classrooms Managing schedules Tracking assignments Getting reminders Then we picked the Empty Classroom Finder as the standout feature for the MVP. UI/UX We designed a fast, clean interface: Home Screen with today’s schedule Free Classroom Finder screen Assignment Tracker Timetable input form Everything was kept minimal to deliver quick access with no clutter. Backend Created collections for users, timetables, and assignments Implemented time-based filtering for free rooms Added support for adding, editing, and storing timetables Frontend Built all screens with a simple and intuitive layout Implemented fast refresh for real-time free room availability Added assignment lists and countdowns to deadlines Testing We tested with multiple sample timetables to ensure: No false “free rooms” Overlapping classes handled correctly Assignments show correct countdowns App reacts instantly to time changes Challenges We Faced Handling overlapping class timings correctly Ensuring fast refresh without slowing down the app Designing a polished UI under hackathon time pressure Keeping scope small while maintaining useful features Final Result Campus Companion is a simple, efficient tool that solves daily student problems by providing: A clear daily schedule Assignment and deadline tracking Real-time classroom availability Automatic reminders It makes campus life more organized, less stressful, and easier for every student. <div