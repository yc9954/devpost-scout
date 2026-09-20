---
slug: "tbd-cnueo8"
url: "https://devpost.com/software/tbd-cnueo8"
title: "ByNextMonday"
hackathon: "monday Apps Challenge: Dream it, build it"
organization: "Monday.com"
winner: true
words: 400
team_size: 1
has_repo: false
has_live: true
has_video: false
tags:
  - "project"
  - "domain/education"
  - "user/educator_student"
  - "substrate/geospatial"
  - "substrate/structured_db"
---

# ByNextMonday

> AI Driven Auto Scheduling to Optimize Tasks Simply

[Devpost](https://devpost.com/software/tbd-cnueo8) · hackathon [[monday Apps Challenge- Dream it- build it]]

## Facets

**domain** [[education]]
**user** [[educator_student]]
**substrate** [[geospatial]] [[structured_db]]

**stack** angular.js, c++, firebase, ionic, node.js, python

## How they structured the write-up

- inspiration
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for bynextmonday

## Body

By Next Monday A step by step app walkthrough can be found here: https://vimeo.com/453458291 Inspiration Part of the inspiration comes from having to wear so many hats during the pandemic. To having to coordinate schedules across many different projects, from developing medical devices (current job) to scheduling kids getting schooled right at home over two households. Monday brings simplicity to the task of scheduling and tracking a team. But when the tasks get small (assignments) and there are many people with many dependencies, creating a schedule is problematic. ByNextMonday aims to put that load onto the computer and synchronize a very visual board with the Monday database. By letting the computer solve the most efficient routes, I think it could be bring monday to new areas, like education and even personal health care (scheduling at home visits ). And, simplifying the generation of scheduling increases the amount that can be scheduled. What it does BNM reads from a stream of jobs (collections of tasks) and users, transforms them (say, a school lesson to lessons for every student), and distributes them over user's available time, casting the right tasks to the right actors and optimizing all of this with constraints of time, location, skill, etc. Currently, it has to be hardwired to read jobs from /assets/classroom_jobs.json /assets/classroom_users.json How we built it The front end is an angular web app. The backend is python on top of mathematical libraries. Firebase handles the primary storage and communications issues Challenges we ran into Currently, we can solve the schedule more efficiently that we can scale number of tasks written into the monday db, There definitely may be a better way to do this and I'd love to work with Monday to figure this out. Unfortunately, the db calls to create items had to be throttled down to 1 item creation per 4 seconds or the server would start throwing errors and all the items could not be created. I'd love to find out how to programmatically batch import into the system. Accomplishments that we're proud of That I got to the end, considering work and home school What we learned Resolving dependencies for large bunches of tasks is something best left to computers. What's next for ByNextMonday Bring it out to the real world and have people use it. There are already folks who use Monday who want to start trying it out! <div