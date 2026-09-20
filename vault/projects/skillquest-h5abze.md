---
slug: "skillquest-h5abze"
url: "https://devpost.com/software/skillquest-h5abze"
title: "SkillQuest"
hackathon: "Codegeist 2021"
organization: "Atlassian"
winner: true
words: 928
team_size: 5
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "domain/finance_payments"
  - "substrate/structured_db"
---

# SkillQuest

> SkillQuest is the app that believes your team is full of gems, and allows you to easily surface skills gaps and experts, not dig for them. 💎

[Devpost](https://devpost.com/software/skillquest-h5abze) · hackathon [[Codegeist 2021]]

## Facets

**domain** [[finance_payments]]
**substrate** [[structured_db]]

**stack** atlaskit, forge, love, react, recoil, typescript

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for skillquest

## Body

GIF Our very first mock-up made with our beloved tool Escalidraw GIF On your profile page, you'll see your Skills and experience points + the history of your last 10 rewards GIF First add Skills as Labels in Jira tickets GIF You also have a bunch of settings GIF You can also have an overview of your team skills Inspiration "Who's the best person in our organisation to tackle this security question ?" "What's the state of our team's skills level on AWS? Should we upskill or hire experts?" Usually, these questions find their answer in a skill matrix, but traditional skill matrixes have their limitations. they're manager or HR-led - Skills matrixes are often drawn up by a team leader or the HR department. Individual team members have little input over their content. they're hardly maintained - In its current popular spreadsheet form, a skills matrix is mostly static but employees' skill set and the requirements of work are constantly evolving. they're boring to create and read - Creating a skill matrix traditionally requires to get employees out of their work stream. Furthermore, identifying subject-matter experts, dominant and missing skills requires some tedious data crunching. At Elements, we believe there's a better way to track skills in our organizations, a way that's fun, engaging, collaborative and efficient. SkillQuest is the app that believes your team is full of gems, and allows you to easily surface skills gaps and experts, not dig for them. What it does In a nutshell, SkillQuest will : Dynamically build your skill matrix in your Jira work stream Level up your skills and earn you reward badges Surface skill gaps Reduce task reassignments by assigning tasks in Jira to the team player that has the right skills to work on those items. Let's dive into the features of this application: 1- Skills Jira labels are used as Skills list. In the settings menu, you can select or exclude values from the labels to customize the skill list. 2- Points Each ticket will have an experience value. You can customize that xp value and how it's divided between the skills in the settings menu. The person who'll do the development will get points credits in the skills set on the ticket. 3- Levels You can set levels based on the xp value. And set at which level a new badge will be granted. 4- Badges Depending on your experience value in one of the skills, you will be granted an achievement Gem. 5- Progress bar With just a glance, you can have an overview of your skill matrix with the progress bars. 6- Teamboard Same, at a glance you have an overview of the skill matrix of the team. 7- Smart assignee This is the feature we are the most proud to present. It's the crown jewel of this app! On the ticket creation, when the skills labels are set, the smart assignee feature will suggest to assign the ticket to the person the most suited for it. It also works on the least experienced person if you want to allow some ramp-up in the skills listed in the ticket. How we built it Skillquest uses: Forge trigger, to detect when rewards must be attributed; Forge modules (project page and issue action); And Custom UI Challenges we ran into At Elements we decided to try to build several apps for Codegeist and explore a number of different ideas. We faced a variety of issues while building multiple apps, and some of them didn't make the cut to be submitted for the competition. We thought it would better to assemble all the issues and remarks we had into one single feedback, available here Element's Feedback on Forge . Accomplishments that we're proud of We built this app in less than 2 weeks/dev. It's quite challenging to develop this fast but also it helps the team to rank the order the features will be added. We must be efficient. We like the final UI of the app, it's quite fresh and the gem management looks very cool. We also love the smart assignee feature. For us, it's the cherry on top that turns ice cream into a sundae. The whole reason to have this skill matrix is not just to compare to each other, but to facilitate the ticket assigning. This feature is the capstone of the application. What we learned The first goal of developing this app was to dive more into Forge framework. We were already familiar with Forge as we already tried to experiment with it, but it was the first time we would develop with the target of having a sharable application. It means having a complete settings page that can fit all users' needs and Jira usages. It also meant having reliable code and a fully functioning application. What's next for SkillQuest What we did is fulling functioning but we think that if we will publish it, we will try to propose more features. Today, it's more an advanced prototype than a real app. We would like to allow coworkers to thank teammates with "karma" points. It's not a skill, but still very important. Perhaps in the future we can allow managers to add rewards. Like a 10$ voucher when a level is reached (karma levels, then it urges people to help each other out :) ) Also, the smart assignee feature could be extended to select 2 coworkers. By example, a very skilled one and a low skilled one for job shadowing or pair programming that will help ramp-up. <div