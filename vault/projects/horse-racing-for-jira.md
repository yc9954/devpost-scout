---
slug: "horse-racing-for-jira"
url: "https://devpost.com/software/horse-racing-for-jira"
title: "Horse Racing for Jira"
hackathon: "Devs Unleashed"
organization: "Atlassian"
winner: true
words: 942
team_size: 1
has_repo: false
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "domain/developer_tools"
  - "user/developer"
---

# Horse Racing for Jira

> The app Horse Racing for Jira allows users to create sprints to race against each other and clear all tickets from the backlog. The winner of the race is the one who closes all their tickets first.

[Devpost](https://devpost.com/software/horse-racing-for-jira) · hackathon [[Devs Unleashed]]

## Facets

**mechanism** [[realtime_stream]]
**domain** [[developer_tools]]
**user** [[developer]]

**stack** forge, jira, node.js, react, slack, typescript

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for horse racing for jira

## Body

Racing Dashboard GIF Real-Time Races Create New Races Configure Slack Integration See Live Updates in Slack Inspiration The idea of a "Horse Racing" app for Jira came from seeing the passion of developers around the world. We noticed that teams often had friendly competitions to see who could complete tasks the fastest, and we wanted to create a way for these teams to measure their progress and compare their speed formally. We believe healthy competition between groups can lead to higher productivity, better collaboration, and increased motivation for developers. What it does Our Horse Racing app allows you to race against other teams on Jira projects utilizing sprints to create a race to take issues from to-do to done. Our Algorithm assumes that all users will start with issues disputed evenly. First, you choose your Board and choose an active or upcoming sprint. Our App will automatically create a horse race based on assigned issues and the progress of the issues. The sprint start and end dates were used to create the timeline of the race. Issues in the sprint were used to get the participants of the race. Using the status and updated time for the issues, we were able to determine the progress and winners of the race. The App provides visibility into progress for users and managers, allowing them to quickly understand what needs to be done to stay on top of their projects. In addition, this App can also help teams detect any potential risks or hiccups ahead of time so they can take appropriate actions early on. How we built it For our Horse Racing app, we've harnessed the power of Atlassian Software-as-a-Service (SaaS) data and Atlassian Forge to make the game more exciting and engaging for teams. By connecting to Jira projects, our app allows users instant access to their sprints and issues and real-time updates on how their team is progressing compared to others. Using Typescript, React, and Atlas Kit, we developed an App that allowed us to organize all of our issues into races with corresponding timelines. Additionally, leveraging Slack API integration, we provided a channel where users could track the progress of each race in real time. To ensure accuracy and speed, we incorporated features such as automated race notifications and live updates when someone crossed the finish line. Challenges we ran into One of the most significant challenges we encountered when creating the Horse Racing app was finding a fair and accurate algorithm for all players. We had to consider various factors, such as the size of each team, the ticket complexity, and other obstacles that could affect the race outcome. We also had to ensure that no team had an unfair advantage over another, which meant considering any possible advantages or disadvantages in terms of resources or skillsets. Additionally, our Algorithm needed to account for minor changes over time so that teams didn't feel stuck with the same results or chances despite having worked hard on their sprints. We worked hard to ensure that our Algorithm was balanced and fair for all players involved while still giving them a realistic chance at winning each race. Accomplishments that we're proud of We are proud of our Horse Racing app's achievements at the hackathon. Not only did our team create a game-like atmosphere that encourages creativity and productivity to complete tasks, but we also offered real-time tracking of sprints and teams competing for the win. This deeper level of visibility makes it easier for participants to stay motivated and focused on closing tickets as quickly as possible while finding ways to improve their performance. Additionally, we created custom reports to track each team's progress over time so users can see how fast they can work against others. We believe this innovative approach makes an enjoyable experience that motivates employees to be more productive and strive for higher levels of excellence in their work. What we learned We learned a lot from building the Horse Racing app for this hackathon. It was an eye-opening experience that allowed us to gain insight into how teams can work together in a more motivating, game-like atmosphere. By assigning tasks, creating sprints, and planning out timelines, we could see how quickly our team could close tickets before their teammates. This showed us that friendly competition amongst all team members could lead to better collaboration and performance. Through this project, we also realized that it is essential to define clear goals and reward systems to keep members motivated and focused on achieving success. Overall, this was a great learning experience and has given us even more confidence in providing practical solutions and strategies for future projects. What's next for Horse Racing for Jira The next step for this App would be developing more features to help teams become even more productive. First, we could add features to customize the racing experience and make it more personal. This could include different difficulty levels, individualized progress tracking, custom race rules, rewards, and allowing users to design their unique teams and tracks. Second, we could integrate additional data points into the App to provide insights into sprint performance. This could include a visual dashboard that provides an overview of all races across the workplace, highlights any areas of improvement or growth, and provides detailed information on each team's performance over time. Finally, we could enhance the game's social aspect by allowing multiple users to join a race or create races with friends for more competitive races. With all these features combined, our Horse Racing app should be an enjoyable and beneficial tool for teams to stay motivated and focused on sprints! <div