---
slug: "easy-agile-jira-hero"
url: "https://devpost.com/software/easy-agile-jira-hero"
title: "Easy Agile Jira Hero"
hackathon: "Codegeist 2021"
organization: "Atlassian"
winner: true
words: 1065
team_size: 7
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/cross_origin_web"
  - "domain/developer_tools"
  - "domain/supply_logistics"
  - "user/developer"
  - "substrate/code_repository"
---

# Easy Agile Jira Hero

> Teamwork in Jira should be fun. With Easy Agile Jira Hero App for Jira, you can celebrate your team’s Jira milestones and achievements.

[Devpost](https://devpost.com/software/easy-agile-jira-hero) · hackathon [[Codegeist 2021]]

## Facets

**mechanism** [[cross_origin_web]]
**domain** [[developer_tools]] [[supply_logistics]]
**user** [[developer]]
**substrate** [[code_repository]]

**stack** atlaskit, jest, ngrok, react, react-router, react-spring, styled-components, typescript, webhooks

## How they structured the write-up

- inspiration
- what it does
- badges available:
- other features
- how we built it
- challenges we ran into
- what's next for easy agile jira hero

## Body

Leaderboard Profile Page Badge Board Team at work Inspiration Hi, Sean from Easy Agile here. We’re a Platinum Atlassian Marketplace Partner and thanks for reading about our Codegeist submission. Our team worked hard on this submission during 2 internal hackathon weeks we call inception week. Although we've been building apps for the Atlassian Marketplace for 5 years, this is something new for us. This was our first experience using Forge and we are delighted with the outcome. Easy Agile Jira Hero helps new and existing teams in Jira celebrate wins, reward milestones and work together around a shared leaderboard. This app makes getting started in Jira a seamless and fun experience. Gamify-ing Jira onboarding makes getting to know your team a little bit easier. What it does When you first open the app you will see the badge board, explaining which badges are available to collect. badges are reward tokens for actions you take in Jira. There’s 8 badges to collect and some badges have different levels and points to earn. The badges reward taking an action in Jira, like Epic Eagle, awarded for creating epics and Bug Exterminator, awarded to those who squash the most bugs. Badges available: Creator (Created 1st issue) plus badge for creating 5, 10, 25, 50, 75, 100, 150, 200 issues Awarded to those addicted to creating Jira issues, even when sleeping. Getting Stuff Done (Resolved 1st issue) plus badge for 5, 10, 25, 50, 75, 100, 150, 200 Awarded for those who detest work in progress and must resolve everything. Delegator (assigned issue to someone else) Awarded to those who cannot do the work Bug Exterminator (squashed 1st bug) plus badge for squashing 5, 10, 25, 50, 75, 100, 150, 200 bugs For those with the determination to squash the most persistent and ugly bugs Eager Estimator (add story point estimation to an issue) For those who put their finger in the air and love to have a good guess. Backlog Bandit (re-ranked an issue on the backlog) Drag and drop is the name of the game. Earn this badge for tweaking the backlog Epic Eagle (created 1st Epic) plus badge for creating 5, 10, 25, 50, 75, 100, 150, 200 epics Creating an epic is a big commitment. Have a badge for your bravery Epic Ending (resolved 1st epic) Like a four hour movie with plot holes everywhere, you’re just happy it’s over. Enjoy your badge Label legend (added first label) plus badge for creating 5, 10, 25, 50, 75, 100, 150, 200 epics What brings you joy? Labels. Lot’s of labels. Other features On the Game board, you’ll see the podium. This is where you need to be to become known as the Jira Hero! Coming second is not an option. The game board shows both how many and which badges your team has collected. Facts don’t lie, the game board shows you where you stand and what you need to do to climb to the top! Hot tip: hover over a badge to see how it was earned. If you click on someone’s face, you’ll bring up the profile view This is how you can see which badges you’ve earned and how many more you need to collect to beat your team mates. Finally, we built an integration with Slack, so every time someone earns a badge, a notification can be pushed to a channel in Slack. We've heard from our customers that getting started in Jira can be hard. If you are new to Jira or joining a team that has been using Jira for a long time, it can be intimidating to know how to get started Easy Agile Jira Hero makes getting to know your team and getting to know Jira more fun. We built this app remotely during COVID lockdown. As we started to play and see the Slack notifications come through, the mood of the team quickly improved. Any tool or app that can help remote teams feel more connected to their work and more connected to each other is welcome. How we built it This was our first forge app as a team, and we were building it from scratch. Thanks to the Forge CLI we were able to get a template up and running based on the Custom UI template. Once we had our template under source control, we where able to define our workflow for individually using our development environment and Atlassian development accounts. We realized quickly that we’d need separate manifest files and also a way to load our custom front end without re-deploying. The app development has progressed over two weeks split by a 5 week block, at the end of week 1 we had a working prototype and at the end of the second week we had been able to do some polishing. Challenges we ran into Initial challenge was working out our development environment as we all wanted to be able to deploy and test our changes without stomping each other. We ran into some timing limitation with the storage API, the 10 requests per second was problematic when trying to seed data. Because we wanted to allow users to oAuth with Slack, we can across a challenge in presenting a nice flow to move out to slack and then redirect back to the app for authentication. We ended up using a web trigger, however we could not get a suitable response to direct the user back to the forge app. How the iframe height is set seemed to change on the 2nd of September which prevented the ability for the app to have its own scrollbar. Some more info about this problem here: https://community.developer.atlassian.com/t/custom-ui-iframe-rendering-at-16px-in-height/51577/9 Methods that eventually made network requests to the /graphql endpoint (like invoke, requestJira) seemed to be slow. For example we were seeing ~1 second round trip times with requestJira when using the /user api. Under these constraints we implemented frontend caching of data in local storage to help make the application appear quicker to load. What's next for Easy Agile Jira Hero Time will tell. We have some other badges we’d like to add and who knows, maybe this will be the next successful Easy Agile app for Jira available on the Atlassian Marketplace. Thanks for watching the video and letting Easy Agile be a part of Codegeist 2021. Check out our other apps for Jira at link <div