---
slug: "well-connected"
url: "https://devpost.com/software/well-connected"
title: "Well&Connected"
hackathon: "HackZurich 2021"
organization: "HackZurich"
winner: true
words: 755
team_size: 5
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "domain/labor_employment"
  - "domain/mental_health"
  - "substrate/video_visual"
---

# Well&Connected

> Well&Connected is the new social well-being platform built for individuals and organisations to help strengthen resilience, create a sense of team wellbeing and better connect employees.

[Devpost](https://devpost.com/software/well-connected) · hackathon [[HackZurich 2021]]

## Facets

**domain** [[labor_employment]] [[mental_health]]
**substrate** [[video_visual]]

**stack** azure, fitrockrapi, mongodb, next.js, node.js, numpy, outlookcalendar, outlookcalendarapi, python, react, scikit-learn, scipy

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for well&connected

## Body

Inspiration Employees' mental health concerns have seen a sharp increase since the COVID19 pandemic. This can be addressed and minimised by acting quickly and building a solution that can achieve better workplace wellbeing and resilience. We believe this is a group effort and not an individual burden hence we strengthen teams and with that individuals. What it does Well&Connected is the new social well-being platform built for individuals and organisations to help strengthen resilience, create a sense of team wellbeing, better connect employees, increase engagement and team feeling. Well&Connected works by allowing the user to connect various devices and data sources such as their calendar and health data, it uses machine learning to understand patterns in their data to predict and warn against potential burn-outs and intervene and help before it’s too late. As it gives the user the option to share concerns with help groups within the organisation and get support. Well&Connected is designed with data privacy at its core, as users have full control of what to share and who to share it with. Well&Connected uses matching algorithms on calendar data and input from users such as (desire to help others, social appetite) to create opportunities to connect team members as often as possible and help them socialize. It also helps better manage workload of employees under pressure through suggestions of increased collaborations between co-workers based on their capacity. Through the use of “TagForHelp” functionality, users can define topics where they need help and guidance so other users and SME groups across the organisation can contribute to the solution and provide support such as finding out the best gadgets for WFH setups How we built it We used the OutlookAPI to pull data from the user Calendar such as average daily working time average meeting time average number of meetings per day average number of meetings per hour total meeting time empty slots holidays sick days location (home vs different offices) and also WatchHealthAPI to pull data such as Heart Rate Activity Steps To achieve the following objectives Use AI/ML to predict when pressure of work is high and the employee's work pressure is trending badly through a "Burn-out Risk" Score/Indicator. The user can then confirm this prediction by simply moving a slider on the page, this is used to further optimise the machine learning model. It takes input from the user on his/her appetite to help others or to socialise with others, This is then fed to a matching algorithm that uses this information and calendar information to match events with immediate team members such as common free lunch slots and common locations where they can potentially meet and socialise. as well as potential colleagues that may be able to help with workload We then used React to build a front-end web app to deliver the outcome in way of recommendations and also take input from the user on preferences of type of recommendation. User can choose to receive social recommendations or work related support as well as exercise and activities Challenges we ran into Parsing calendar information into meaningful data and categories can be challenging based on the type of calendar. However the metadata of meetings were extremely useful in coming up with the correct categories. Doing all this while maintaining the user's privacy and making sure this tool and design is not used as a monitoring tool but giving the user full freedom on who can see what data. Accomplishments that we're proud of Being able to pull the features we wanted and build a robust (decent working) UI/UX. Being able to build a tool that we could personally see ourselves using and recommend to friends as we care about their health and think this app will help everyone to strengthen their resilience and help take care of themselves. What we learned Work wellbeing is a very challenging topic with many aspects and potential solutions. It is very hard to crack as it needs a large number of people to come together with determination to address it well. We learned a lot about people and ourselves and what we would like to see organisations do What's next for Well&Connected We have had great ideas around integrating other data sources such as emails and more data from fitness apps to provide more services and also connect this with women health-apps. Furthermore to make our app more interactive we're planning to provide users the option to share photos on the app and give the possibility to chat with their team members. <div